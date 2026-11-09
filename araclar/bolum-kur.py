#!/usr/bin/env python3
"""Kalem paketlerinin zaman.json dosyalarındaki sahnelere bolum alanı ekler."""

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any, Dict, List, Tuple


def bolum_turet(sahne: Dict[str, Any]) -> str:
    """Sahne için bölüm değerini ad veya klasörden türetir."""
    ad = sahne.get("ad")
    if ad is not None and str(ad).strip() != "":
        return str(ad)
    klasor = str(sahne.get("klasor", ""))
    return re.sub(r"^\d+-[a-z]+-", "", klasor)


def sahneye_bolum_ekle(sahne: Dict[str, Any], yeni_bolum: str) -> Dict[str, Any]:
    """bolum alanını ad varsa ad alanından, yoksa klasor alanından hemen sonra ekler."""
    yeni: Dict[str, Any] = {}
    ad_var: bool = (
        "ad" in sahne
        and sahne["ad"] is not None
        and str(sahne["ad"]).strip() != ""
    )
    for anahtar, deger in sahne.items():
        if anahtar == "bolum":
            continue
        yeni[anahtar] = deger
        if ad_var and anahtar == "ad":
            yeni["bolum"] = yeni_bolum
        elif not ad_var and anahtar == "klasor":
            yeni["bolum"] = yeni_bolum
    if "bolum" not in yeni:
        yeni["bolum"] = yeni_bolum
    return yeni


def paketi_isle(
    dosya_yolu: Path, yaz: bool, zorla: bool
) -> Tuple[int, int, int]:
    """Tek bir zaman.json dosyasını inceler ve gerekirse günceller."""
    metin: str = dosya_yolu.read_text(encoding="utf-8")
    veri: Dict[str, Any] = json.loads(metin)
    sahneler: List[Dict[str, Any]] = veri.get("sahneler", [])

    sahne_sayisi: int = len(sahneler)
    yazilacak: int = 0
    degismez: int = 0
    yeni_sahneler: List[Dict[str, Any]] = []

    for sahne in sahneler:
        bolum_var: bool = "bolum" in sahne
        if bolum_var and not zorla:
            degismez += 1
            yeni_sahneler.append(sahne)
        else:
            yazilacak += 1
            yeni_bolum: str = bolum_turet(sahne)
            yeni_sahneler.append(sahneye_bolum_ekle(sahne, yeni_bolum))

    if yaz and yazilacak > 0:
        veri["sahneler"] = yeni_sahneler
        yeni_metin: str = json.dumps(veri, ensure_ascii=False, indent=2) + "\n"
        dosya_yolu.write_text(yeni_metin, encoding="utf-8")

    return sahne_sayisi, yazilacak, degismez


def main() -> int:
    """Komut satırı argümanlarını ayrıştırır ve paketleri işler."""
    parser = argparse.ArgumentParser(
        description="Zaman dosyalarındaki sahnelere bolum alanı kurar."
    )
    parser.add_argument(
        "--yaz", action="store_true", help="Dosyalara değişiklikleri yazar."
    )
    parser.add_argument(
        "--zorla", action="store_true", help="Mevcut bölüm alanlarını yeniden yazar."
    )
    parser.add_argument(
        "--paket", type=str, default=None, help="Yalnızca belirtilen paketi işler."
    )
    parser.add_argument(
        "--kok",
        type=Path,
        default=None,
        help="Paketlerin aranacağı kök dizin (varsayılan: depo kökü).",
    )

    args = parser.parse_args()

    kok: Path = (
        args.kok.resolve()
        if args.kok
        else Path(__file__).resolve().parent.parent
    )
    projeler_dizini: Path = kok / "projeler"

    toplam_sahne: int = 0
    toplam_yazilacak: int = 0
    toplam_degismez: int = 0

    if projeler_dizini.is_dir():
        dosyalar = sorted(
            projeler_dizini.glob("*/zaman.json"),
            key=lambda p: p.parent.name,
        )
        for dosya in dosyalar:
            paket_adi: str = dosya.parent.name
            if paket_adi.startswith("deneme-") or paket_adi == "katalog":
                continue
            if args.paket and paket_adi != args.paket:
                continue

            sahne_n, yaz_k, deg_m = paketi_isle(
                dosya, yaz=args.yaz, zorla=args.zorla
            )
            print(
                f"{paket_adi} | sahne {sahne_n} | "
                f"yazılacak {yaz_k} | değişmez {deg_m}"
            )

            toplam_sahne += sahne_n
            toplam_yazilacak += yaz_k
            toplam_degismez += deg_m

    print("-" * 50)
    print(
        f"toplam | sahne {toplam_sahne} | "
        f"yazılacak {toplam_yazilacak} | değişmez {toplam_degismez}"
    )
    print("yazıldı" if args.yaz else "kuru koşu (--yaz ile uygula)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
