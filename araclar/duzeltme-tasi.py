#!/usr/bin/env python3
"""present-perfect-temel'de yapılan iki düzeltmeyi öteki paketlere taşır (12.11, pp g-11, D-0147).

1) Günlük koruması (kalem 1b6b1a6): sahne yardımcılarındaki (kalem-paper.js, sahne-ortak.js)
   `fetch("/log", <seçenek>)` çağrısı `logGonder(<seçenek>)` olur; logGonder yalnız yerel geliştirme
   sunucusunda (localhost, 127.0.0.1, 10.x, 192.168.x) istek atar, yayında sessizce geçer.
2) Zemin önbelleği (kalem 2a349f5 + 565d7a9): ortak/kunye.js `zeminCiz` gövdesi, eski sürümle birebir
   aynıysa, karo + vinyet önbellekli sürümle değişir (ölçüm: 9,7 → 1,6 ms/kare, piksel farkı ≤ 1/255).
   Gövde farklıysa paket atlanır ve raporlanır (elle bakılır).

Kullanım: duzeltme-tasi.py [--yaz] [--paket AD]...   (varsayılan kuru koşu; bütün paketler)
Çıktı: paket başına satır + toplam. Değişen dosya yalnız --yaz ile yazılır (atomik).
"""
from __future__ import annotations

import argparse
import os
import re
import sys
from pathlib import Path

KOK = Path(__file__).resolve().parent.parent / "projeler"
KAYNAK = "present-perfect-temel"
YARDIMCI = ("kalem-paper.js", "sahne-ortak.js")
CAGRI = 'fetch("/log", '
TANIM = (
  "// Geliştirme günlüğü (12.11, pp g-11): POST /log yalnız yerel geliştirme sunucusunda; yayında istek yok.\n"
  "const YEREL_SUNUCU = /^(localhost|127\\.0\\.0\\.1|\\[::1\\]|10\\.\\d+\\.\\d+\\.\\d+|192\\.168\\.\\d+\\.\\d+)$/\n"
  "  .test(location.hostname);\n"
  "const logGonder = (o) => (YEREL_SUNUCU ? fetch(\"/log\", o).catch(() => {}) : Promise.resolve());\n"
)
ZEMIN_BLOK = re.compile(r"export function zeminCiz\(ctx, f, K\) \{\n.*?\n\}\n", re.S)


def zemin_bloklari(kaynak: str) -> tuple[str, str]:
  """Kaynak paketin (yeni) kunye.js'inden yeni blok: yorum + zeminCiz + zeminKaroAl + vinyetAl."""
  bas = kaynak.index("// Zemin önbelleği (10.11")
  son = kaynak.index("\n}\n", kaynak.index("function vinyetAl()")) + 3
  return kaynak[bas:son], ESKI_ZEMIN


ESKI_ZEMIN = (
  "export function zeminCiz(ctx, f, K) {\n"
  "  ctx.save(); ctx.globalCompositeOperation = \"source-over\"; ctx.globalAlpha = 1;\n"
  "  ctx.fillStyle = RENK.zemin; ctx.fillRect(0, 0, W, H);\n"
  "  if (K && K.grenler) {\n"
  "    ctx.globalAlpha = temaAd === \"acik\" ? 0.03 : 0.045; ctx.globalCompositeOperation = \"overlay\";\n"
  "    const g = K.grenler[f % 3], ox = (f * 97) % 512, oy = (f * 61) % 512;\n"
  "    for (let y = -oy; y < H; y += 512) for (let x = -ox; x < W; x += 512) ctx.drawImage(g, x, y);\n"
  "  }\n"
  "  ctx.globalAlpha = 1; ctx.globalCompositeOperation = \"source-over\";\n"
  "  const v = ctx.createRadialGradient(W / 2, H / 2, H * 0.45, W / 2, H / 2, H * 0.95);\n"
  "  v.addColorStop(0, \"rgba(0,0,0,0)\"); v.addColorStop(1, temaAd === \"acik\" ? \"rgba(0,0,0,0.10)\""
  " : \"rgba(0,0,0,0.38)\");\n"
  "  ctx.fillStyle = v; ctx.fillRect(0, 0, W, H); ctx.restore();\n"
  "}\n"
)


def gunluk_donustur(metin: str) -> tuple[str, int]:
  """fetch("/log", X) → logGonder(X); tanımı son import satırından sonra ekler. (yeni metin, çağrı sayısı)"""
  sayi = metin.count(CAGRI)
  if sayi == 0 or "const logGonder" in metin:
    return metin, 0
  yeni = metin.replace(CAGRI, "logGonder(")
  satirlar = yeni.split("\n")
  son_import = max((i for i, s in enumerate(satirlar) if s.startswith("import ")), default=-1)
  # çok satırlı import: son import satırının bittiği satırı bul (";" ile biten ilk satır)
  j = son_import
  while j >= 0 and not satirlar[j].rstrip().endswith(";") and j + 1 < len(satirlar):
    j += 1
  ek = j + 1 if son_import >= 0 else 0
  satirlar[ek:ek] = TANIM.rstrip("\n").split("\n")
  return "\n".join(satirlar), sayi


def yaz(yol: Path, metin: str) -> None:
  gecici = yol.with_name(f"{yol.name}.{os.getpid()}.tmp")
  gecici.write_text(metin, encoding="utf-8")
  gecici.replace(yol)


def main() -> int:
  ap = argparse.ArgumentParser()
  ap.add_argument("--yaz", action="store_true")
  ap.add_argument("--paket", action="append", default=[])
  a = ap.parse_args()
  kaynak = (KOK / KAYNAK / "ortak" / "kunye.js").read_text(encoding="utf-8")
  yeni_zemin, eski_zemin = zemin_bloklari(kaynak)
  paketler = a.paket or sorted(p.name for p in KOK.iterdir() if (p / "sahneler").is_dir())
  toplam = {"dosya": 0, "cagri": 0, "zemin": 0, "zemin_atla": 0}
  for ad in paketler:
    if ad in (KAYNAK, KAYNAK + "-dikey"):
      continue
    p = KOK / ad
    dosya = cagri = 0
    for yol in sorted(p.glob("sahneler/*/*.js")):
      if yol.name not in YARDIMCI or yol.is_symlink():
        continue
      eski = yol.read_text(encoding="utf-8")
      yeni, n = gunluk_donustur(eski)
      if n:
        dosya += 1; cagri += n
        if a.yaz:
          yaz(yol, yeni)
    zemin = "-"
    k = p / "ortak" / "kunye.js"
    if k.is_file() and not k.is_symlink():
      s = k.read_text(encoding="utf-8")
      if "zeminKaroAl" in s:
        zemin = "zaten"
      elif s.count(eski_zemin) == 1:
        zemin = "tasindi"; toplam["zemin"] += 1
        if a.yaz:
          yaz(k, s.replace(eski_zemin, yeni_zemin + "\n"))
      else:
        zemin = "ATLANDI (gövde farklı)"; toplam["zemin_atla"] += 1
    toplam["dosya"] += dosya; toplam["cagri"] += cagri
    if dosya or zemin not in ("-", "zaten"):
      print(f"{ad}: günlük {dosya} dosya / {cagri} çağrı · zemin {zemin}")
  print(f"TOPLAM: günlük {toplam['dosya']} dosya / {toplam['cagri']} çağrı · zemin {toplam['zemin']} paket"
        f" · zemin atlanan {toplam['zemin_atla']}" + ("" if a.yaz else " (kuru koşu; yazmak için --yaz)"))
  return 0


if __name__ == "__main__":
  sys.exit(main())
