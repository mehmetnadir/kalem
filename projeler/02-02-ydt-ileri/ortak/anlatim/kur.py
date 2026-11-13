"""anlatim.wav kurucu: cumle-N.wav dosyalarını hesaplanan başlangıçlara yerleştirir.
Başlangıçlar sabit dizi DEĞİL: sureler.json (cümle süresi) + cümle arası sessizlik kuralından türer
(K23 soğuk açılış: ilk cümlenin İLK SÖZÜ 1,00 sn'de başlar).
Boşluk kuralı (taslak §4 süre ölçüsü): cümle sonrası 0,55 sn; öğrenci cümlesinden sonra 0,70 sn.
Sayaç sessizliği (2,0 sn, satır 7.2) cümlenin kendi `sus` parçasıdır, sureler.json süresine dahildir.
Toplam süre = son cümlenin bitişi + 0,5 sn (zaman.json son sahne t_son ile aynı kural).
Kullanım: /usr/bin/python3 -I kur.py [cikti.wav]   (varsayılan: anlatim.wav, bu dizinde)"""
import json
import subprocess
import sys
from pathlib import Path

AD = Path(__file__).resolve().parent
FFMPEG = "/opt/homebrew/bin/ffmpeg"
ILK_SOZ = 1.00
BOSLUK = 0.55
BOSLUK_OGRENCI = 0.70
KUYRUK = 0.5


def plan() -> list[dict]:
    """[{i, bas, bitis, sure, konusan}] küresel sn."""
    sure = {s["i"]: s for s in json.loads((AD / "sureler.json").read_text())}
    sen = json.loads((AD / "senaryo.json").read_text())["cumleler"]
    out: list[dict] = []
    t = None
    for i in sorted(sure):
        s = sure[i]
        konusan = sen[i - 1].get("ses", "ogretmen")
        if t is None:
            t = ILK_SOZ - s["sozcukler"][0][1]
        out.append({"i": i, "bas": round(t, 3), "bitis": round(t + s["sure"], 3), "sure": s["sure"], "konusan": konusan})
        t = t + s["sure"] + (BOSLUK_OGRENCI if konusan == "ogrenci" else BOSLUK)
    return out


def baslar() -> dict[int, float]:
    return {p["i"]: p["bas"] for p in plan()}


def toplam() -> float:
    return round(plan()[-1]["bitis"] + KUYRUK, 3)


def kur(cikti: Path) -> float:
    p = plan()
    tot = toplam()
    girdi: list[str] = []
    filtre: list[str] = []
    for k, e in enumerate(p):
        girdi += ["-i", str(AD / f"cumle-{e['i']}.wav")]
        ms = round(e["bas"] * 1000)
        filtre.append(f"[{k}:a]aresample=48000,aformat=channel_layouts=mono,adelay={ms}[a{k}]")
    ad = "".join(f"[a{k}]" for k in range(len(p)))
    filtre.append(f"{ad}amix=inputs={len(p)}:normalize=0:duration=longest,"
                  f"apad=whole_dur={tot},atrim=0:{tot}[c]")
    cmd = [FFMPEG, "-y", "-loglevel", "error", *girdi, "-filter_complex", ";".join(filtre),
           "-map", "[c]", "-ac", "1", "-ar", "48000", "-c:a", "pcm_s16le", str(cikti)]
    subprocess.run(cmd, check=True)
    return tot


if __name__ == "__main__":
    hedef = Path(sys.argv[1]) if len(sys.argv) > 1 else AD / "anlatim.wav"
    print("başlar", baslar())
    print("toplam sn", kur(hedef), "->", hedef)
