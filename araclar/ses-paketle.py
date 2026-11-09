#!/usr/bin/env python3
"""Kalem paketlerinin anlatım seslerini AAC-LC formatına sıkıştırır."""

import argparse
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

AYAR_DIZESI: str = "aac-96k-48000-mono"


def ffmpeg_bul() -> str:
    """ffmpeg ikili dosyasının yolunu bulur."""
    adaylar: List[str] = [
        "/opt/homebrew/bin/ffmpeg",
        "/usr/local/bin/ffmpeg",
    ]
    for aday in adaylar:
        p = Path(aday)
        if p.is_file() and os.access(p, os.X_OK):
            return str(p)
    bulunan = shutil.which("ffmpeg")
    if bulunan:
        return bulunan
    raise RuntimeError("ffmpeg bulunamadı")


def ffprobe_bul() -> str:
    """ffprobe ikili dosyasının yolunu bulur."""
    adaylar: List[str] = [
        "/opt/homebrew/bin/ffprobe",
        "/usr/local/bin/ffprobe",
    ]
    for aday in adaylar:
        p = Path(aday)
        if p.is_file() and os.access(p, os.X_OK):
            return str(p)
    bulunan = shutil.which("ffprobe")
    if bulunan:
        return bulunan
    raise RuntimeError("ffprobe bulunamadı")


def dosya_md5(dosya_yolu: Path) -> str:
    """Dosyanın MD5 özetini hesaplar."""
    h = hashlib.md5()
    with open(dosya_yolu, "rb") as f:
        while True:
            parca = f.read(65536)
            if not parca:
                break
            h.update(parca)
    return h.hexdigest()


def ses_suresi(ffprobe_yolu: str, ses_yolu: Path) -> float:
    """ffprobe ile ses dosyasının süresini saniye cinsinden döndürür."""
    cmd: List[str] = [
        ffprobe_yolu,
        "-v",
        "error",
        "-show_entries",
        "format=duration",
        "-of",
        "default=noprint_wrappers=1:nokey=1",
        str(ses_yolu),
    ]
    sonuc = subprocess.run(
        cmd,
        capture_output=True,
        text=True,
        check=True,
    )
    return float(sonuc.stdout.strip())


def mb_bicimlendir(bayt: int) -> str:
    """Bayt miktarını virgüllü MB dizesine dönüştürür."""
    mb: float = bayt / (1024 * 1024)
    return f"{mb:.1f}".replace(".", ",") + " MB"


def aac_donustur(ffmpeg_yolu: str, wav_yolu: Path, m4a_yolu: Path) -> None:
    """WAV dosyasını AAC-LC formatında M4A olarak kodlar."""
    cmd: List[str] = [
        ffmpeg_yolu,
        "-y",
        "-i",
        str(wav_yolu),
        "-c:a",
        "aac",
        "-b:a",
        "96k",
        "-ar",
        "48000",
        "-ac",
        "1",
        "-movflags",
        "+faststart",
        "-vn",
        str(m4a_yolu),
    ]
    subprocess.run(
        cmd,
        capture_output=True,
        check=True,
    )


def paketi_isle(
    paket_dizini: Path,
    yaz: bool,
    zorla: bool,
    ffmpeg_yolu: Optional[str],
    ffprobe_yolu: Optional[str],
    gercek_ses_durumu: Dict[Path, Dict[str, Any]],
) -> Optional[Tuple[str, int, int, bool, bool]]:
    """Tek bir paketin zaman.json ve ses dosyasını inceler ve gerekirse işler."""
    paket_adi: str = paket_dizini.name
    zaman_yolu: Path = paket_dizini / "zaman.json"
    if not zaman_yolu.is_file():
        return None

    try:
        metin: str = zaman_yolu.read_text(encoding="utf-8")
        veri: Dict[str, Any] = json.loads(metin)
    except Exception as e:
        raise RuntimeError(f"{zaman_yolu} okunamadı: {e}") from e

    anlatim_alani = veri.get("anlatim")
    if not anlatim_alani or not str(anlatim_alani).strip():
        print(f"{paket_adi} | wav yok")
        return None

    anlatim_str: str = str(anlatim_alani)
    if anlatim_str.endswith(".wav"):
        wav_yolu = (paket_dizini / anlatim_str).resolve()
    elif anlatim_str.endswith(".m4a"):
        wav_yolu = (paket_dizini / anlatim_str).with_suffix(".wav").resolve()
    else:
        wav_yolu = (paket_dizini / anlatim_str).resolve()

    if not wav_yolu.is_file():
        print(f"{paket_adi} | wav yok")
        return None

    wav_boyut: int = wav_yolu.stat().st_size
    m4a_yolu: Path = wav_yolu.parent / f"{wav_yolu.stem}.m4a"
    imza_yolu: Path = wav_yolu.parent / f"{m4a_yolu.name}.imza"

    # Daha önce bu gerçek ses dosyası işlendi mi (ör. dikey paket symlink ise)
    if wav_yolu in gercek_ses_durumu:
        durum = gercek_ses_durumu[wav_yolu]
        uretildi: bool = durum["uretildi"]
        atlandi: bool = durum["atlandi"]
        m4a_boyut: int = durum["m4a_boyut"]
        m4a_var: bool = durum["m4a_var"]
        eylem: str = durum["eylem"]

        if yaz:
            yeni_anlatim: str = re.sub(r"\.wav$", ".m4a", anlatim_str)
            if veri.get("anlatim") != yeni_anlatim:
                veri["anlatim"] = yeni_anlatim
                yeni_metin: str = json.dumps(veri, ensure_ascii=False, indent=2) + "\n"
                zaman_yolu.write_text(yeni_metin, encoding="utf-8")

        durum_str: str = "m4a var" if m4a_var else "m4a yok"
        print(f"{paket_adi} | wav {mb_bicimlendir(wav_boyut)} | {durum_str} | {eylem}")
        return paket_adi, wav_boyut, m4a_boyut, uretildi, atlandi

    wav_md5: str = dosya_md5(wav_yolu)
    beklenen_imza: str = f"{wav_md5} {AYAR_DIZESI}"
    m4a_var_diskte: bool = m4a_yolu.is_file()

    imza_eslesiyor: bool = False
    if m4a_var_diskte and imza_yolu.is_file():
        try:
            imza_eslesiyor = imza_yolu.read_text(encoding="utf-8").strip() == beklenen_imza
        except OSError:
            imza_eslesiyor = False

    atla: bool = imza_eslesiyor and not zorla

    if not yaz:
        if atla:
            eylem = "atlandı"
            uretildi = False
            atlandi = True
            m4a_boyut = m4a_yolu.stat().st_size if m4a_var_diskte else 0
        else:
            eylem = "üretilecek"
            uretildi = True
            atlandi = False
            m4a_boyut = m4a_yolu.stat().st_size if m4a_var_diskte else 0
        durum_str = "m4a var" if m4a_var_diskte else "m4a yok"
        print(f"{paket_adi} | wav {mb_bicimlendir(wav_boyut)} | {durum_str} | {eylem}")
        gercek_ses_durumu[wav_yolu] = {
            "uretildi": uretildi,
            "atlandi": atlandi,
            "m4a_boyut": m4a_boyut,
            "m4a_var": m4a_var_diskte,
            "eylem": eylem,
        }
        return paket_adi, wav_boyut, m4a_boyut, uretildi, atlandi

    # --yaz kipi
    if atla:
        eylem = "atlandı"
        uretildi = False
        atlandi = True
        m4a_boyut = m4a_yolu.stat().st_size if m4a_var_diskte else 0
        m4a_var = True
    else:
        if not ffmpeg_yolu or not ffprobe_yolu:
            raise RuntimeError("ffmpeg veya ffprobe bulunamadı")
        aac_donustur(ffmpeg_yolu, wav_yolu, m4a_yolu)
        wav_sure = ses_suresi(ffprobe_yolu, wav_yolu)
        m4a_sure = ses_suresi(ffprobe_yolu, m4a_yolu)
        if abs(m4a_sure - wav_sure) > 0.1:
            print(
                f"HATA: SÜRE FARKI ({paket_adi}): wav={wav_sure:.3f} sn, m4a={m4a_sure:.3f} sn",
                file=sys.stderr,
            )
            sys.exit(2)
        imza_yolu.write_text(beklenen_imza + "\n", encoding="utf-8")
        eylem = "üretildi"
        uretildi = True
        atlandi = False
        m4a_boyut = m4a_yolu.stat().st_size
        m4a_var = True

    yeni_anlatim = re.sub(r"\.wav$", ".m4a", anlatim_str)
    if veri.get("anlatim") != yeni_anlatim:
        veri["anlatim"] = yeni_anlatim
        yeni_metin = json.dumps(veri, ensure_ascii=False, indent=2) + "\n"
        zaman_yolu.write_text(yeni_metin, encoding="utf-8")

    durum_str = "m4a var" if (m4a_var_diskte and eylem == "atlandı") else "m4a yok"
    if eylem == "üretildi" and m4a_var_diskte:
        durum_str = "m4a var"
    print(f"{paket_adi} | wav {mb_bicimlendir(wav_boyut)} | {durum_str} | {eylem}")

    gercek_ses_durumu[wav_yolu] = {
        "uretildi": uretildi,
        "atlandi": atlandi,
        "m4a_boyut": m4a_boyut,
        "m4a_var": m4a_var,
        "eylem": eylem,
    }
    return paket_adi, wav_boyut, m4a_boyut, uretildi, atlandi


def main() -> int:
    """Komut satırı argümanlarını ayrıştırır ve paketleri işler."""
    parser = argparse.ArgumentParser(
        description="Paket anlatım seslerini AAC-LC formatına sıkıştırır."
    )
    parser.add_argument(
        "--yaz", action="store_true", help="m4a üretir ve zaman.json dosyalarını günceller."
    )
    parser.add_argument(
        "--zorla", action="store_true", help="İmza eşleşse bile yeniden üretir."
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

    ffmpeg_yolu: Optional[str] = None
    ffprobe_yolu: Optional[str] = None
    if args.yaz:
        ffmpeg_yolu = ffmpeg_bul()
        ffprobe_yolu = ffprobe_bul()

    toplam_paket: int = 0
    toplam_uretilen: int = 0
    toplam_atlanan: int = 0
    toplam_wav_bayt: int = 0
    toplam_m4a_bayt: int = 0

    gercek_ses_durumu: Dict[Path, Dict[str, Any]] = {}

    if projeler_dizini.is_dir():
        dizinler = sorted(
            [p for p in projeler_dizini.iterdir() if p.is_dir()],
            key=lambda p: p.name,
        )
        for p in dizinler:
            paket_adi: str = p.name
            if paket_adi.startswith("deneme-") or paket_adi == "katalog":
                continue
            if args.paket and paket_adi != args.paket:
                continue

            sonuc = paketi_isle(
                p,
                yaz=args.yaz,
                zorla=args.zorla,
                ffmpeg_yolu=ffmpeg_yolu,
                ffprobe_yolu=ffprobe_yolu,
                gercek_ses_durumu=gercek_ses_durumu,
            )
            if sonuc is not None:
                _, wav_b, m4a_b, uret, atla = sonuc
                toplam_paket += 1
                if uret:
                    toplam_uretilen += 1
                if atla:
                    toplam_atlanan += 1
                toplam_wav_bayt += wav_b
                toplam_m4a_bayt += m4a_b

    print("-" * 50)
    print(
        f"toplam | paket {toplam_paket} | üretilen {toplam_uretilen} | "
        f"atlanan {toplam_atlanan} | wav {mb_bicimlendir(toplam_wav_bayt)} → "
        f"m4a {mb_bicimlendir(toplam_m4a_bayt)}"
    )
    print("yazıldı" if args.yaz else "kuru koşu (--yaz ile uygula)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
