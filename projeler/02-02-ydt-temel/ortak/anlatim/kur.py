"""anlatim.wav yeniden kurucu: cumle-N.wav dosyalarını sozcukler.json'daki mutlak zamanlara yerleştirir.
Tek kaynak: cumle-baslar.json (sozcuk_uret.py: ilk söz 1,00 sn; sonraki başlar = önceki + süre + 0,55 sn),
toplam süre = zaman.json son sahne t_son. Çıktı 48 kHz mono 16 bit.
Kullanım: /usr/bin/python3 -I kur.py [cikti.wav]   (varsayılan: anlatim.wav, bu dizinde)"""
import json
import subprocess
import sys
from pathlib import Path

AD = Path(__file__).resolve().parent
PROJE = AD.parent.parent
FFMPEG = "/opt/homebrew/bin/ffmpeg"


def baslar() -> dict[int, float]:
    """Cümle no -> küresel başlangıç sn (cumle-baslar.json; sozcuk_uret.py sureler.json + cümle arası sessizlikten hesaplar)."""
    return {b["i"]: b["baslar"] for b in json.loads((AD / "cumle-baslar.json").read_text())}


def kur(cikti: Path) -> float:
    zaman = json.loads((PROJE / "zaman.json").read_text())
    toplam = zaman["sahneler"][-1]["t_son"]
    b = baslar()
    girdi: list[str] = []
    filtre: list[str] = []
    for k, (no, t) in enumerate(sorted(b.items())):
        girdi += ["-i", str(AD / f"cumle-{no}.wav")]
        ms = round(t * 1000)
        filtre.append(f"[{k}:a]aresample=48000,aformat=channel_layouts=mono,adelay={ms}[a{k}]")
    ad = "".join(f"[a{k}]" for k in range(len(b)))
    filtre.append(f"{ad}amix=inputs={len(b)}:normalize=0:duration=longest,"
                  f"apad=whole_dur={toplam},atrim=0:{toplam}[c]")
    cmd = [FFMPEG, "-y", "-loglevel", "error", *girdi, "-filter_complex", ";".join(filtre),
           "-map", "[c]", "-ac", "1", "-ar", "48000", "-c:a", "pcm_s16le", str(cikti)]
    subprocess.run(cmd, check=True)
    return toplam


if __name__ == "__main__":
    hedef = Path(sys.argv[1]) if len(sys.argv) > 1 else AD / "anlatim.wav"
    print("başlar", baslar())
    print("toplam sn", kur(hedef), "->", hedef)
