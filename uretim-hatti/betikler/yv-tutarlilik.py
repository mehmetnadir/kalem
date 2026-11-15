#!/usr/bin/python3
"""YouTube yayın verisi: dersler arası tutarlılık ölçümü (YV-DUZ, 15.11.2026).

Salt okur; yalnız standart kitaplık. Çıkış 0 = sorun yok, 1 = en az bir sorun, 2 = girdi eksik.

  /usr/bin/python3 -I uretim-hatti/betikler/yv-tutarlilik.py [--kok <kalem kökü>]
      [--katalog <katalog.json>] [--kilitli <paket,paket>]

Ders kümesi: `projeler/*/uretim-tutanagi/juri/YVJ-hukum.md` dosyası olan paketler; `<paket>-dikey` varsa o da.
`--kilitli`: başka oturumun değiştirdiği paketler. Yalnız bu paketlere düşen sorun "[kilitli]" yazılır,
çıkış koduna sayılmaz (düzeltmesi rapora gider). Ölçütler: juri-olcutleri.md §2f ve §1d;
youtube-yayin-verisi-sozlesme.md §2; youtube-surumu-standart.md §3; istem YV-DUZ madde 4.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import unicodedata
from collections import defaultdict
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

KANAL_ETIKETLERI = ("İngilizce", "gramer", "YDT")  # sözleşme §2: kitle, "İngilizce", "gramer"
ES_ADLAR = {"present simple", "past simple"}  # bilinçli eş ad (Simple Present ↔ Present Simple)
EK_TEMEL = " | YDT İngilizce"
EK_ILERI = " | YDT İngilizce İleri"
BASLIK_SINIR, BASLIK_HEDEF = 100, 60
ACIKLAMA_SINIR, ETIKET_SINIR = 5000, 500
BOLUM_EN_AZ, BOLUM_EN_KISA = 3, 10.0
BILDIRIM_ILK, BILDIRIM_SON = 30.0, 20.0
CUMLE_EN_COK_DERS = 2
ORTAK_ALANLAR = ("baslik", "etiketler", "sabitYorum", "gonderiler", "liste", "giris", "cikis")
OLCUTLER = ("sinir", "zaman", "damga", "kanal-etiketi", "emoji", "baslik", "liste",
            "etiket-yazim", "kopya", "dikey")


@dataclass
class Paket:
    ad: str
    yt: dict[str, Any]
    aciklama: str
    sure: float
    konu: str
    kod: str
    sahne_baslari: set[float] = field(default_factory=set)
    dikey: Paket | None = None


@dataclass
class Rapor:
    kilitli: set[str]
    sorunlar: dict[str, list[str]] = field(default_factory=lambda: defaultdict(list))
    kilitli_sorunlar: list[str] = field(default_factory=list)
    bilgiler: list[str] = field(default_factory=list)

    def ekle(self, olcut: str, paketler: list[str], metin: str) -> None:
        if paketler and all(p in self.kilitli for p in paketler):
            self.kilitli_sorunlar.append(f"{olcut}: {metin}")
        else:
            self.sorunlar[olcut].append(metin)


def oku_json(yol: Path) -> Any:
    with yol.open(encoding="utf-8") as f:
        return json.load(f)


def paket_oku(yol: Path) -> Paket:
    yt = oku_json(yol / "youtube.json")
    aciklama = (yol / yt.get("aciklamaDosya", "youtube-aciklama.md")).read_text(encoding="utf-8")
    sahneler = oku_json(yol / "zaman.json")["sahneler"]
    sure = max(float(s["t_son"]) for s in sahneler)
    surum = yol / "surumler.json"  # dikey pakette olmayabilir; konu yatay paketten okunur
    konu = oku_json(surum)["video"]["konu"] if surum.is_file() else ""
    m = re.search(r"utm_campaign=([A-Za-z0-9-]+)", aciklama)
    baslar = {round(float(s["t_bas"]), 2) for s in sahneler}
    return Paket(yol.name, yt, aciklama, sure, konu, m.group(1) if m else "", baslar)


def damga(t: float) -> str:
    s = int(t + 0.5)
    return f"{s // 60:02d}:{s % 60:02d}"


def etiket_toplam(etiketler: list[str]) -> int:
    """YouTube sayımı: ayırıcı virgüller + boşluklu etikete iki tırnak."""
    return sum(len(e) + (2 if " " in e else 0) for e in etiketler) + max(len(etiketler) - 1, 0)


def bolum_blogu(aciklama: str) -> list[tuple[str, str]] | None:
    """`Bölümler:` başlığının altındaki damga satırları; başlık yoksa None."""
    satirlar = aciklama.splitlines()
    if "Bölümler:" not in satirlar:
        return None
    cikti: list[tuple[str, str]] = []
    for s in satirlar[satirlar.index("Bölümler:") + 1:]:
        m = re.match(r"^(\d{2}:\d{2}) (.+)$", s)
        if not m:
            break
        cikti.append((m.group(1), m.group(2)))
    return cikti


def tekil_olc(p: Paket, r: Rapor) -> None:
    yt, ad = p.yt, p.ad
    b = yt["baslik"]
    if len(b) > BASLIK_SINIR:
        r.ekle("sinir", [ad], f"{ad}: başlık {len(b)} > {BASLIK_SINIR} karakter")
    elif len(b) > BASLIK_HEDEF and not ad.endswith("-dikey"):
        r.bilgiler.append(f"{ad}: başlık {len(b)} karakter (hedef ≤ {BASLIK_HEDEF})")
    n = len(p.aciklama.encode("utf-8"))
    if n > ACIKLAMA_SINIR:
        r.ekle("sinir", [ad], f"{ad}: açıklama {n} > {ACIKLAMA_SINIR} bayt")
    et = etiket_toplam(yt["etiketler"])
    if et > ETIKET_SINIR:
        r.ekle("sinir", [ad], f"{ad}: etiket toplamı {et} > {ETIKET_SINIR}")
    for k in KANAL_ETIKETLERI:
        if k not in yt["etiketler"]:
            r.ekle("kanal-etiketi", [ad], f"{ad}: '{k}' etiketi yok")
    bol = yt["bolumler"]
    if len(bol) < BOLUM_EN_AZ:
        r.ekle("zaman", [ad], f"{ad}: {len(bol)} bölüm < {BOLUM_EN_AZ}")
    if not bol or float(bol[0]["t"]) != 0.0:
        r.ekle("zaman", [ad], f"{ad}: ilk bölüm 0'da değil")
    sinir = [float(x["t"]) for x in bol] + [p.sure]
    for i, x in enumerate(bol):
        t = float(x["t"])
        if t >= p.sure:
            r.ekle("zaman", [ad], f"{ad}: bölüm {i + 1} t={t} ≥ ders süresi {p.sure}")
        if round(t, 2) not in p.sahne_baslari:
            r.ekle("zaman", [ad], f"{ad}: bölüm {i + 1} t={t} zaman.json sahne başı değil")
        if sinir[i + 1] - t < BOLUM_EN_KISA:
            r.ekle("zaman", [ad], f"{ad}: bölüm {i + 1} {sinir[i + 1] - t:.2f} sn < {BOLUM_EN_KISA}")
    for x in yt.get("bildirimler", []):
        t, s = float(x["t"]), float(x["sure"])
        if t + s > p.sure:
            r.ekle("zaman", [ad], f"{ad}: bildirim {t}+{s} ders süresini ({p.sure}) aşıyor")
        if t < BILDIRIM_ILK or t + s > p.sure - BILDIRIM_SON:
            r.ekle("zaman", [ad], f"{ad}: bildirim {t} ilk 30 sn ya da son 20 sn içinde")
    blok = bolum_blogu(p.aciklama)
    if blok is None:
        r.ekle("damga", [ad], f"{ad}: açıklamada 'Bölümler:' başlığı yok")
    elif blok != [(damga(float(x["t"])), x["ad"]) for x in bol]:
        r.ekle("damga", [ad], f"{ad}: Bölümler bloğu youtube.json bolumler ile aynı değil")
    metinler = [b, p.aciklama, yt["sabitYorum"]] + [g["metin"] for g in yt["gonderiler"]]
    if any(unicodedata.category(c) == "So" for m in metinler for c in m):
        r.ekle("emoji", [ad], f"{ad}: metinde emoji var")
    print(f"  {ad:34s} başlık {len(b):3d} kr · açıklama {n:4d} B · etiket {et:3d} · "
          f"bölüm {len(bol):2d} · süre {p.sure:.2f} sn")


def seviye(p: Paket) -> str:
    return "ileri" if p.kod.endswith("-I") else "temel"


def baslik_konusu(p: Paket) -> str:
    b = p.yt["baslik"]
    if b.endswith(EK_ILERI):
        return b[: -len(EK_ILERI)].split(": ")[0]
    return b[: -len(EK_TEMEL)] if b.endswith(EK_TEMEL) else b


def baslik_olc(paketler: list[Paket], r: Rapor) -> None:
    gorulen: dict[str, str] = {}
    for p in paketler:
        b = p.yt["baslik"]
        if b.casefold() in gorulen:
            r.ekle("baslik", [p.ad, gorulen[b.casefold()]],
                   f"{p.ad}: başlık '{b}' {gorulen[b.casefold()]} ile aynı")
        gorulen[b.casefold()] = p.ad
        if seviye(p) == "temel":
            konu = b[: -len(EK_TEMEL)]
            if not b.endswith(EK_TEMEL) or b.endswith(EK_ILERI):
                r.ekle("baslik", [p.ad], f"{p.ad}: temel başlık '<Konu>{EK_TEMEL}' kalıbında değil")
            elif konu not in (p.konu, p.konu.split(":")[0].strip()):
                r.ekle("baslik", [p.ad], f"{p.ad}: başlıktaki konu '{konu}' ≠ surumler.json '{p.konu}'")
            continue
        m = re.match(r"^(.+?): (.+)" + re.escape(EK_ILERI) + "$", b)
        if not m:
            r.ekle("baslik", [p.ad], f"{p.ad}: ileri başlık '<Konu>: <içerik>{EK_ILERI}' kalıbında değil")
            continue
        if m.group(1) != p.konu:
            r.ekle("baslik", [p.ad], f"{p.ad}: başlıktaki konu '{m.group(1)}' ≠ '{p.konu}'")
        sozcuk = [s for s in re.split(r"[\s,]+", m.group(2)) if re.search(r"\w", s)]
        if not 2 <= len(sozcuk) <= 4:
            r.ekle("baslik", [p.ad], f"{p.ad}: ayırt edici içerik {len(sozcuk)} sözcük (2–4)")


def katalog_haritasi(katalog: dict[str, Any]) -> dict[str, dict[str, Any]]:
    """video kodu -> beklenen liste alanları (ad, sira, onceki, sonraki)."""
    harita: dict[str, dict[str, Any]] = {}
    for u in katalog["uniteler"]:
        konular = sorted(u.get("konular", []), key=lambda k: k["sira"])

        def komsu(j: int, kitle: str, sev: str) -> str | None:
            if not 0 <= j < len(konular):
                return None
            for w in konular[j].get("videolar", []):
                if w["kitle"] == kitle and w["seviye"] == sev:
                    return str(w["kimlik"])
            return None

        for i, k in enumerate(konular):
            for v in k.get("videolar", []):
                kitle = katalog["kitleler"].get(v["kitle"], v["kitle"])
                sev = katalog["seviyeler"].get(v["seviye"], v["seviye"])
                harita[v["kod"]] = {
                    "ad": f"{u['ad']} · {kitle} {sev}", "sira": k["sira"],
                    "onceki": komsu(i - 1, v["kitle"], v["seviye"]),
                    "sonraki": komsu(i + 1, v["kitle"], v["seviye"]),
                }
    return harita


def liste_olc(paketler: list[Paket], katalog: dict[str, Any] | None, r: Rapor) -> None:
    sira: dict[tuple[str, int], str] = {}
    harita = katalog_haritasi(katalog) if katalog else {}
    for p in paketler:
        li = p.yt["liste"]
        anahtar = (str(li["ad"]), int(li["sira"]))
        if anahtar in sira:
            r.ekle("liste", [p.ad, sira[anahtar]],
                   f"{p.ad}: '{li['ad']}' sıra {li['sira']} {sira[anahtar]} ile çakışıyor")
        sira[anahtar] = p.ad
        if katalog is None:
            continue
        bek = harita.get(p.kod)
        if bek is None:
            r.ekle("liste", [p.ad], f"{p.ad}: kod '{p.kod}' katalogda yok")
            continue
        for alan in ("ad", "sira", "onceki", "sonraki"):
            if li.get(alan) != bek[alan]:
                r.ekle("liste", [p.ad], f"{p.ad}: liste.{alan} '{li.get(alan)}' ≠ katalog '{bek[alan]}'")


def etiket_anahtar(e: str) -> str:
    """Aynı kavram: sözcük kümesi aynı ("since for" = "for ve since")."""
    return " ".join(sorted(s for s in re.split(r"[\s/,'’-]+", e.casefold()) if s and s != "ve"))


def etiket_olc(paketler: list[Paket], r: Rapor) -> None:
    konular = {baslik_konusu(p).casefold() for p in paketler} | {p.konu.casefold() for p in paketler}
    yazim: dict[str, dict[str, set[str]]] = defaultdict(lambda: defaultdict(set))
    for p in paketler:
        for e in p.yt["etiketler"]:
            yazim["etiket:" + etiket_anahtar(e)][e].add(p.ad)
        son = [s for s in p.aciklama.splitlines() if s.startswith("#")]
        for h in (son[-1].split() if son else []):
            yazim["hashtag:" + h.casefold()][h].add(p.ad)
    for anahtar, bicimler in yazim.items():
        kalan = {b: d for b, d in bicimler.items() if b.casefold() not in ES_ADLAR | konular}
        if len(kalan) > 1:
            dersler = sorted({x for d in kalan.values() for x in d})
            ayrinti = "; ".join(f"'{b}' ({', '.join(sorted(d))})" for b, d in kalan.items())
            r.ekle("etiket-yazim", dersler, f"{anahtar.split(':')[0]}: aynı kavram, farklı yazım: {ayrinti}")


def cumleler(metin: str) -> list[str]:
    """Cümleler ve noktalı virgülle ayrılan yan cümleler (en az 3 sözcük), küçük harf."""
    cikti: list[str] = []
    for c in re.split(r"(?<=[.!?;])\s+", metin.strip()):
        n = re.sub(r"\s+", " ", re.sub(r"[\"“”'’]", "", c).strip().rstrip(".!?;").casefold())
        if len(n.split()) >= 3:
            cikti.append(n)
    return cikti


def kopya_olc(paketler: list[Paket], r: Rapor) -> None:
    tum: dict[str, set[str]] = defaultdict(set)
    gecis: dict[str, set[str]] = defaultdict(set)
    for p in paketler:
        for m in [p.yt["sabitYorum"]] + [g["metin"] for g in p.yt["gonderiler"]]:
            tum[m.strip()].add(p.ad)
            for c in cumleler(m):
                gecis[c].add(p.ad)
    for m, d in sorted(tum.items()):
        if len(d) > 1:
            r.ekle("kopya", sorted(d), f"birebir aynı metin ({', '.join(sorted(d))}): '{m[:70]}'")
    for c, d in sorted(gecis.items()):
        if len(d) > CUMLE_EN_COK_DERS:
            r.ekle("kopya", sorted(d), f"'{c[:70]}' {len(d)} derste: {', '.join(sorted(d))}")


def aciklama_govde(aciklama: str) -> str:
    satirlar = [s for s in aciklama.splitlines() if not re.match(r"^\d{2}:\d{2} ", s)]
    return re.sub(r"utm_content=[A-Za-z0-9-]+", "utm_content=*", "\n".join(satirlar))


def dikey_olc(p: Paket, r: Rapor) -> None:
    d = p.dikey
    if d is None:
        return
    for alan in ORTAK_ALANLAR:
        if p.yt.get(alan) != d.yt.get(alan):
            r.ekle("dikey", [d.ad], f"{d.ad}: '{alan}' yatay paketle aynı değil")
    if aciklama_govde(p.aciklama) != aciklama_govde(d.aciklama):
        r.ekle("dikey", [d.ad], f"{d.ad}: açıklama yataydan farklı (utm_content ve damga dışında)")
    if "utm_content=dikey" not in d.aciklama:
        r.ekle("dikey", [d.ad], f"{d.ad}: açıklamada utm_content dikey değil")


def main() -> int:
    dosya = globals().get("__file__")
    kok_v = Path(dosya).resolve().parents[2] if dosya and dosya != "<stdin>" else Path.cwd()
    ap = argparse.ArgumentParser(description="YouTube yayın verisi tutarlılık ölçümü")
    ap.add_argument("--kok", type=Path, default=kok_v)
    ap.add_argument("--katalog", type=Path,
                    default=Path.home() / "01dev/dijital-anlatim/varlik/grammar/katalog.json")
    ap.add_argument("--kilitli", default="", help="virgülle paket adları")
    a = ap.parse_args()
    projeler = a.kok / "projeler"
    hukumler = sorted(projeler.glob("*/uretim-tutanagi/juri/YVJ-hukum.md"))
    if not hukumler:
        print(f"girdi yok: {projeler}/*/uretim-tutanagi/juri/YVJ-hukum.md", file=sys.stderr)
        return 2
    paketler: list[Paket] = []
    for h in hukumler:
        p = paket_oku(h.parents[2])
        dy = projeler / f"{p.ad}-dikey"
        if (dy / "youtube.json").is_file():
            p.dikey = paket_oku(dy)
            p.dikey.konu = p.konu
        paketler.append(p)
    katalog = oku_json(a.katalog) if a.katalog.is_file() else None
    r = Rapor(kilitli={x.strip() for x in a.kilitli.split(",") if x.strip()})
    if katalog is None:
        r.bilgiler.append(f"katalog yok ({a.katalog}): liste katalogla karşılaştırılmadı")
    print(f"yv-tutarlilik: {len(paketler)} ders, {sum(1 for p in paketler if p.dikey)} dikey eş")
    for p in paketler:
        tekil_olc(p, r)
        if p.dikey:
            tekil_olc(p.dikey, r)
            dikey_olc(p, r)
    baslik_olc(paketler, r)
    liste_olc(paketler, katalog, r)
    etiket_olc(paketler, r)
    kopya_olc(paketler, r)
    print("başlıklar:")
    for p in paketler:
        print(f"  {p.ad:28s} {seviye(p):5s} {len(p.yt['baslik']):3d} kr  {p.yt['baslik']}")
    for o in OLCUTLER:
        s = r.sorunlar.get(o, [])
        print(f"[{'TAMAM' if not s else 'SORUN'}] {o}: {len(s)}")
        for m in s:
            print(f"    - {m}")
    for m in r.kilitli_sorunlar:
        print(f"[kilitli] {m}")
    for b in r.bilgiler:
        print(f"[bilgi] {b}")
    toplam = sum(len(v) for v in r.sorunlar.values())
    print(f"toplam sorun: {toplam} · kilitli pakette: {len(r.kilitli_sorunlar)}")
    return 1 if toplam else 0


if __name__ == "__main__":
    sys.exit(main())
