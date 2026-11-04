"""anlatim.wav yeniden kurucu: cumle-N.wav dosyalarını sozcukler.json'daki mutlak zamanlara yerleştirir.
Tek kaynak: sozcukler.json (cümle başı = ilk sözcüğün t0'ı − sureler.json'daki ilk sözcük payı),
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
    """Cümle no -> küresel başlangıç sn."""
    soz = json.loads((AD / "sozcukler.json").read_text())
    sure = {s["i"]: s for s in json.loads((AD / "sureler.json").read_text())}
    out: dict[int, float] = {}
    for no, s in sure.items():
        ilk = min(w["t0"] for w in soz if w["cumle"] == no)
        out[no] = round(ilk - s["sozcukler"][0][1], 3)
    return out


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
