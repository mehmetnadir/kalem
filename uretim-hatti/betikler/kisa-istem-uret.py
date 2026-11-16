#!/usr/bin/python3 -I
"""Huni kısası (S<N>) istemlerini üretir: A, B-dil, B-kural, C.

Kullanım: kisa-istem-uret.py <kod> <paket> <N> [--cikti DİZİN] [--kuru] [--zorla]
          [--konu-json YOL] [--tarih GG.AA.YYYY] [--projeler DİZİN] [--kaydet M] [--cagri M]

Şablon tek kaynaktır: uretim-hatti/istemler/sablon/{A,B-dil,B-kural,C}.md ({{alan}} yer tutucu).
Derse özgü değerler ders verisinden gelir; bulunamayan değer uydurulmaz.
Çıkış: 0 tamam · 2 eksik alan/girdi · 3 hedef dosya var (--zorla yok).
"""
from __future__ import annotations

import argparse
import datetime
import json
import re
import sys
from pathlib import Path
from typing import Any

BU = Path(__file__).resolve().parent
HAT = BU.parent
SABLON = HAT / "istemler" / "sablon"
PROJELER = HAT.parent / "projeler"
DOSYALAR = ("A", "B-dil", "B-kural", "C")
SEVIYE = {"T": "temel", "I": "ileri"}


class Eksik(Exception):
  """Derse özgü bir alan bulunamadı."""


def oku_json(yol: Path) -> Any:
  try:
    return json.loads(yol.read_text(encoding="utf-8"))
  except (OSError, ValueError) as e:
    raise Eksik(f"{yol} okunamadı ({e.__class__.__name__})") from e


def kisalt(metin: str, en_cok: int = 70) -> str:
  """İlk anlamlı cümle: en az 4 sözcüklü ilk cümle ("Birinci örnek.", "Look!" atlanır)."""
  cumleler = [c for c in re.split(r"(?<=[.!?])\s+", metin.strip()) if c]
  ilk = next((c for c in cumleler if len(c.split()) >= 4), cumleler[0] if cumleler else "")
  return ilk if len(ilk) <= en_cok else ilk[: en_cok - 1].rstrip() + "…"


def kapak_metni(surumler: dict[str, Any]) -> str:
  """Ana dersin kısa/dikey kapak metni: önce shorts, sonra dikey-tam."""
  satir = {s.get("kimlik"): s.get("kapak") for s in surumler.get("surumler", [])}
  for k in ("shorts", "dikey-tam"):
    if satir.get(k):
      return str(satir[k])
  raise Eksik("surumler.json: shorts/dikey-tam satırında kapak metni yok")


def karakter_tarifi(kaynak: dict[str, Any]) -> str:
  for g in kaynak.get("gorseller", []):
    if g.get("dosya") == "karakter.png" and g.get("tarif"):
      t = re.sub(r"\s*\([^)]*\)\s*$", "", str(g["tarif"]))
      return t.split(";")[0].strip()
  raise Eksik("ortak/kapak/KAYNAK.json: karakter.png tarifi yok")


def adayi_bul(konu: dict[str, Any], n: int) -> dict[str, Any]:
  for a in konu.get("adaylar", []):
    if a.get("sira") == n or a.get("kimlik") == f"s{n}":
      return a
  raise Eksik(f"huni-konu: s{n} adayı yok")


def topla(kod: str, paket: str, n: int, a: argparse.Namespace) -> dict[str, str]:
  proje = Path(a.projeler) / paket
  eksik: list[str] = []
  v: dict[str, str] = {"kod": kod, "paket": paket, "n": str(n), "tarih": a.tarih}
  if not proje.is_dir():
    raise Eksik(f"paket dizini yok: {proje}")
  m = re.fullmatch(r"(\d{4})([TI])", kod)
  if not m:
    raise Eksik(f"kod biçimi 0201T / 0201I olmalı: {kod}")
  v["oge"] = f"{m.group(1)[:2]}-{m.group(1)[2:]}-ydt-{SEVIYE[m.group(2)]}"

  def dene(ad: str, f: Any) -> None:
    try:
      v.update(f())
    except Eksik as e:
      eksik.append(f"{ad}: {e}")

  def surum() -> dict[str, str]:
    s = oku_json(proje / "surumler.json")
    vid = s.get("video", {})
    for k in ("konu", "seviye", "kitle"):
      if not vid.get(k):
        raise Eksik(f"surumler.json video.{k} yok")
    return {"konu": vid["konu"], "seviye": vid["seviye"], "kitle": vid["kitle"],
            "kapak_metni": kapak_metni(s)}

  def senaryo() -> dict[str, str]:
    d = oku_json(proje / "ortak" / "anlatim" / "senaryo.json")
    return {"_cumleler": json.dumps([c.get("metin", "") for c in d.get("cumleler", [])]),
            "kadro_anahtar": "`kadro`" if d.get("kadro") else "`sesler`"}

  def konu() -> dict[str, str]:
    yol = Path(a.konu_json) if a.konu_json else proje / "uretim-tutanagi" / "huni-konu.json"
    ad = adayi_bul(oku_json(yol), n)
    for k in ("bicim", "kaynak_cumle"):
      if not ad.get(k):
        raise Eksik(f"{yol.name} s{n}.{k} yok")
    baslik = ad.get("baslik") or ad.get("bilgi")
    if not baslik:
      raise Eksik(f"{yol.name} s{n}: baslik/bilgi yok")
    return {"baslik": str(baslik).rstrip(". "), "bicim": ad["bicim"], "_not": ad.get("kaynak_not", ""),
            "_idx": json.dumps(ad["kaynak_cumle"])}

  def karakter() -> dict[str, str]:
    return {"karakter": karakter_tarifi(oku_json(proje / "ortak" / "kapak" / "KAYNAK.json"))}

  def kalip() -> dict[str, str]:
    tablo = oku_json(SABLON / "kaydet-cagri.json").get(str(n), {})
    k, c = a.kaydet or tablo.get("kaydet"), a.cagri or tablo.get("cagri")
    if not k or not c:
      raise Eksik(f"S{n} için kaydet/çağrı kalıbı yok (--kaydet, --cagri ver)")
    return {"kaydet": k, "cagri": c}

  for ad, f in (("surumler", surum), ("senaryo", senaryo), ("konu", konu),
                ("karakter", karakter), ("kalıp", kalip)):
    dene(ad, f)
  if "_idx" in v:
    if v["_not"]:
      v["kaynak"] = v["_not"]
    elif "_cumleler" in v:
      cum = json.loads(v["_cumleler"])
      parca = []
      for i in json.loads(v["_idx"]):
        if not isinstance(i, int) or not 1 <= i <= len(cum) or not cum[i - 1]:
          eksik.append(f"konu: kaynak cümle {i} senaryo.json'da yok")
          continue
        parca.append(f"cümle {i} ({kisalt(cum[i - 1])})")
      v["kaynak"] = " ve ".join(parca)
  # N=1 ve paket kökünde eski kısa içeriği varsa: eski içeriği taşıma adımı
  kok = Path(a.projeler) / f"{paket}-s{n}"
  eski = n == 1 and kok.is_dir() and any(p.name != "uretim-tutanagi" for p in kok.iterdir())
  v["eski_a"] = ("; paket ESKİ bir kısa içeriyor — ona dokunma, yalnız `uretim-tutanagi/` "
                 "altına yaz; eski senaryoyu `ortak/anlatim/senaryo.json` içinden okuyup değer "
                 "sahnesinde yararlanabilirsin") if eski else ""
  v["eski_c"] = ("- ÖNCE (yalnız S1): paket ESKİ bir kısa içeriyor. `uretim-tutanagi/` DIŞINDAKİ her "
                 "şeyi (eski `sahneler/`, `ortak/`, `zaman.json`, `surumler.json`,\n  BRIEF, kök "
                 "PNG/MD/JSON dosyaları) `~/Silinecekler/2026-11-15-huni-v2/" + paket + "-s1-eski/` "
                 "altına TAŞI (`mv`; silme yok), sonra yeni\n  paketi emsal iskeletiyle kur. Eski "
                 "`uretim-tutanagi/` içindeki eski dosyalara dokunma; yeni taslaklar ve jüri aynı "
                 "dizinde.\n") if eski else ""
  if eksik:
    raise Eksik("\n  ".join(eksik))
  return v


def doldur(sablon: str, v: dict[str, str]) -> str:
  cikti = sablon
  for k, d in v.items():
    if not k.startswith("_"):
      cikti = cikti.replace("{{" + k + "}}", d)
  kalan = sorted(set(re.findall(r"\{\{(\w+)\}\}", cikti)))
  if kalan:
    raise Eksik(f"şablonda doldurulmamış alan: {', '.join(kalan)}")
  return cikti


def main(argv: list[str]) -> int:
  p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawTextHelpFormatter)
  p.add_argument("kod")
  p.add_argument("paket")
  p.add_argument("n", type=int)
  p.add_argument("--cikti", default=str(HAT / "istemler"))
  p.add_argument("--kuru", action="store_true")
  p.add_argument("--zorla", action="store_true")
  p.add_argument("--konu-json")
  p.add_argument("--tarih", default=datetime.date.today().strftime("%d.%m.%Y"))
  p.add_argument("--projeler", default=str(PROJELER))
  p.add_argument("--kaydet")
  p.add_argument("--cagri")
  a = p.parse_args(argv)
  try:
    v = topla(a.kod, a.paket, a.n, a)
    metinler = {d: doldur((SABLON / f"{d}.md").read_text(encoding="utf-8"), v) for d in DOSYALAR}
  except Eksik as e:
    print(f"EKSİK (istem üretilmedi):\n  {e}", file=sys.stderr)
    return 2
  cikti = Path(a.cikti)
  yollar = {d: cikti / f"P{a.kod}-S{a.n}-{d}.md" for d in DOSYALAR}
  var = [str(y) for y in yollar.values() if y.exists()]
  if var and not a.zorla and not a.kuru:
    print("VAR (üstüne yazılmaz; --zorla ile):\n  " + "\n  ".join(var), file=sys.stderr)
    return 3
  for d, y in yollar.items():
    if a.kuru:
      print(f"kuru: {y} ({len(metinler[d].encode('utf-8'))} bayt)")
    else:
      cikti.mkdir(parents=True, exist_ok=True)
      y.write_text(metinler[d], encoding="utf-8")
      print(f"yazıldı: {y}")
  return 0


if __name__ == "__main__":
  sys.exit(main(sys.argv[1:]))
