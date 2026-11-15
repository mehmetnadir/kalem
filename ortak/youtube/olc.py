"""YouTube ortak parçaları ölçümleri (istem YT-1, 15.11.2026). Kareleri ve sesi okur, PNG/WAV/JSON yazar; mp4 üretmez.
  /usr/bin/python3 -I olc.py ses     giris/ses/giris.wav (3,00 sn) + cikis/ses/cikis.wav (20,00 sn), 48 kHz mono;
                                     söz başı/sonu (enerji eşiği), el.py önbellek anahtarı denetimi → olcum/ses.json
  /usr/bin/python3 -I olc.py sag     çıkış karelerinde x ≥ 960 zemin dışı piksel (yalnız-zemin kıyası) → olcum/sag.json
  /usr/bin/python3 -I olc.py yer     iki dersin kareleri → içerik maskesi → köşe adayları → bildirim/yer.json
                                     + bildirim/olcum/yer-tablo.json + bildirim/ornek-*.png
Önkoşul: calistir.sh kareleri yakalamış olur (olcum/zemin-{acik,koyu}.png, cikis/k/…)."""
from __future__ import annotations

import glob
import hashlib
import json
import os
import re
import subprocess
import sys
import wave
from pathlib import Path

import numpy as np
from PIL import Image

YT = Path(__file__).resolve().parent
K = YT.parent.parent
OLCUM = YT / "olcum"
sys.path.insert(0, str(YT))
import uret  # noqa: E402  (süre ve söz başı sabitleri tek kaynak)

ONB = Path.home() / ".local/share/elevenlabs-onbellek"
W, H = 1920, 1080


def yaz(yol: Path, veri: object) -> None:
    yol.parent.mkdir(parents=True, exist_ok=True)
    yol.write_text(json.dumps(veri, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")


def ffprobe_sure(yol: Path) -> float:
    r = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(yol)],
                       capture_output=True, text=True, check=True)
    return float(r.stdout.strip())


def wav_oku(yol: Path) -> tuple[np.ndarray, int]:
    with wave.open(str(yol)) as w:
        assert w.getsampwidth() == 2, "16 bit PCM bekleniyor: %s" % yol
        a = np.frombuffer(w.readframes(w.getnframes()), dtype="<i2").astype(np.float32) / 32768.0
        return a.reshape(-1, w.getnchannels()).mean(1), w.getframerate()


def soz_araligi(a: np.ndarray, sr: int, esik_db: float = -40.0) -> tuple[float, float]:
    """10 ms pencere RMS'i eşiği ilk aşan pencerenin başı, son aşanın sonu (sn)."""
    n = sr // 100
    p = a[: len(a) // n * n].reshape(-1, n)
    db = 20 * np.log10(np.sqrt((p ** 2).mean(1)) + 1e-9)
    i = np.nonzero(db > esik_db)[0]
    return round(i[0] * n / sr, 3), round((i[-1] + 1) * n / sr, 3)


def onbellek_anahtari(t_ses: str, onceki: str, sonraki: str, ses: str, tohum: int) -> str:
    """el.py iste(): sha1([ses metni, dil, önceki, sonraki, ses kimliği, model, tohum] + hız eki).
    ses-sunucu.sh HIZ_EN=0.9 verir → hız eki [1.0, 0.9] (varsayılan 1.0/0.8 dışı)."""
    return hashlib.sha1(json.dumps([t_ses, "tr", onceki, sonraki, ses, "eleven_v4", tohum, 1.0, 0.9],
                                   ensure_ascii=False).encode()).hexdigest()


def ses() -> None:
    out = {}
    for ad, bas, sure in (("giris", uret.GIRIS_SES_BAS, uret.GIRIS_SURE), ("cikis", uret.CIKIS_SES_BAS, uret.CIKIS_SURE)):
        d = YT / ad / "ses"
        hedef = d / ("%s.wav" % ad)
        subprocess.run(["ffmpeg", "-nostdin", "-loglevel", "error", "-y", "-i", str(d / "cumle-1.wav"), "-af",
                        "adelay=%d:all=1,apad=whole_dur=%.2f,atrim=0:%.2f" % (round(bas * 1000), sure, sure),
                        "-ar", "48000", "-ac", "1", "-c:a", "pcm_s16le", str(hedef)], check=True)
        senaryo = json.loads((d / "senaryo.json").read_text(encoding="utf-8"))
        kimlik = senaryo["sesler"]["ogrenci"]
        rapor = json.loads((d / "sentez.wav.rapor.json").read_text(encoding="utf-8"))
        metinler = [r.get("ses_metni", r["metin"]) for r in rapor]
        anahtar = []
        for i, r in enumerate(rapor):
            k = onbellek_anahtari(metinler[i], " ".join(metinler[:i]), " ".join(metinler[i + 1:]), kimlik, r["tohum"])
            ogretmen = onbellek_anahtari(metinler[i], " ".join(metinler[:i]), " ".join(metinler[i + 1:]),
                                         "gsJ9nrlXYbPztJxC4fwc", r["tohum"])
            anahtar.append({"metin": r["metin"], "anahtar": k[:12], "wav_var": (ONB / (k + ".wav")).exists(),
                            "ogretmen_anahtari_var": (ONB / (ogretmen + ".wav")).exists()})
        a, sr = wav_oku(d / "cumle-1.wav")
        s0, s1 = soz_araligi(a, sr)
        b, sr2 = wav_oku(hedef)
        y0, y1 = soz_araligi(b, sr2)
        out[ad] = {"ses_kimligi": kimlik, "whisper": [{"metin": r["metin"], "duyulan": r["duyulan"],
                                                       "benzerlik": r["benzerlik"], "tohum": r["tohum"]} for r in rapor],
                   "onbellek": anahtar, "cumle_sure": round(len(a) / sr, 2), "cumle_soz": [s0, s1],
                   "parca": hedef.relative_to(YT).as_posix(), "parca_sure": round(ffprobe_sure(hedef), 2),
                   "parca_hz": sr2, "ilk_soz": round(y0, 2), "soz_sonu": round(y1, 2), "soz_bas_ayar": bas}
    yaz(OLCUM / "ses.json", out)
    for ad, v in out.items():
        print("%s: parça %.2f sn · ilk söz %.2f · söz sonu %.2f · Whisper %s · önbellek %s"
              % (ad, v["parca_sure"], v["ilk_soz"], v["soz_sonu"], [w["benzerlik"] for w in v["whisper"]],
                 [o["wav_var"] for o in v["onbellek"]]))


def rgb(yol: str | Path) -> np.ndarray:
    return np.asarray(Image.open(yol).convert("RGB")).astype(np.int16)


def sag() -> None:
    out = {}
    for tema in ("acik", "koyu"):
        ref = rgb(OLCUM / ("zemin-%s.png" % tema))
        alt = "" if tema == "acik" else "koyu/"
        for t in ("0.5", "4.0", "19.9"):
            k = rgb(YT / "cikis" / "k" / ("%scikis-%s.png" % (alt, t)))
            d = np.abs(k - ref).max(2)[:, 960:]
            sol = np.abs(k - ref).max(2)[:, :960]
            out["%s %s" % (tema, t)] = {"sag_fark_0": int((d > 0).sum()), "sag_fark_8": int((d > 8).sum()),
                                        "sol_fark_8": int((sol > 8).sum())}
    kutu = {}
    for tema in ("acik", "koyu"):
        for satir in (OLCUM / ("cikis-kutu-%s.jsonl" % tema)).read_text().splitlines():
            s = json.loads(satir)
            kutu["%s %s" % (tema, s["t"])] = max(b[3] for b in json.loads(s["olc"]))
    yaz(OLCUM / "sag.json", {"piksel": out, "en_sag_kutu_x": kutu})
    for k, v in out.items():
        print("çıkış %s: x≥960 fark>0 %d · fark>8 %d · (sol yarı fark>8 %d) · en sağ kutu %.1f"
              % (k, v["sag_fark_0"], v["sag_fark_8"], v["sol_fark_8"], kutu[k]))


# ---- bildirim yeri ----
KART = (520, 140)
ESIK = 24             # zemin kıyası, kanal farkı (ders zeminleri referanstan ≤ 3 ayrışır, 15.11 ölçümü)
PAY = 16              # kart ile içerik arası en az boşluk (px)
KENAR = 40            # kart ile kare kenarı arası en az boşluk (px)
OLCEK = 2             # maske 2x küçültülür (960x540); aday adımı 4 px
DERSLER = {"02-04-ydt-temel": "yeni kuşak", "simple-present-temel": "eski kuşak"}
KOSELER = ("sag_ust", "sol_alt", "sol_ust")      # aday sırası (istem); sağ alt YASAK (YouTube filigranı)


def kareler(ders: str) -> list[dict]:
    """Ders kareleri: sahneler/*/k (kapak 90-* hariç) + eski kuşak için yakalanan bildirim/olcum/<ders> + yeni kuşak
    cikti(-koyu).mp4 saniyede 1 kare (sahne sınırına 0,5 sn'den yakın kareler geçiş sayılır, alınmaz)."""
    kok = K / "projeler" / ders
    z = json.loads((kok / "zaman.json").read_text(encoding="utf-8"))
    sah = {s["klasor"]: s for s in z["sahneler"]}
    out = []
    kaynak = [(p, "acik") for p in glob.glob(str(kok / "sahneler/*/k/*.png"))]
    kaynak += [(p, "koyu") for p in glob.glob(str(kok / "sahneler/*/k/koyu/*.png"))]
    ek = YT / "bildirim" / "olcum" / ders
    kaynak += [(p, "acik") for p in glob.glob(str(ek / "*.png"))] + [(p, "koyu") for p in glob.glob(str(ek / "koyu/*.png"))]
    for p, tema in sorted(kaynak):
        ad = Path(p).name
        sahne = Path(p).parts[-3] if Path(p).parent.name == "k" else Path(p).parts[-4]
        if Path(p).is_relative_to(ek):
            sahne = re.match(r"(\d\d-[a-z0-9-]+?)-[\d.]+\.png$", ad).group(1)
        if sahne.startswith("90-") or sahne not in sah:
            continue
        m = re.match(r".*-([\d.]+)\.png$", ad)
        if m:
            t = float(m.group(1).rstrip("."))
        elif re.match(r"^\d+\.png$", ad):
            t = sah[sahne]["t_bas"] + int(ad[:-4]) / 30
        else:
            continue
        with Image.open(p) as im:
            if im.size != (W, H):
                continue
        out.append({"ders": ders, "kaynak": os.path.relpath(p, K), "sahne": sahne, "t": round(t, 2), "tema": tema})
    for tema, mp4 in (("acik", "cikti.mp4"), ("koyu", "cikti-koyu.mp4")):
        if not (kok / mp4).exists():
            continue
        sinir = [s["t_son"] for s in z["sahneler"]]
        for i in range(int(z["sahneler"][-1]["t_son"])):
            if min(abs(i - b) for b in sinir) < 0.5:
                continue
            sahne = next(s["klasor"] for s in z["sahneler"] if s["t_bas"] <= i < s["t_son"])
            out.append({"ders": ders, "kaynak": "%s#%d" % (os.path.relpath(kok / mp4, K), i), "sahne": sahne,
                        "t": float(i), "tema": tema, "mp4": str(kok / mp4), "i": i})
    return out


def mp4_kareleri(yol: str) -> list[np.ndarray]:
    r = subprocess.run(["ffmpeg", "-nostdin", "-loglevel", "error", "-i", yol, "-vf", "fps=1,format=rgb24",
                        "-f", "rawvideo", "-"], capture_output=True, check=True)
    a = np.frombuffer(r.stdout, dtype=np.uint8)
    return list(a.reshape(-1, H, W, 3))


def tema_bul(a: np.ndarray) -> str:
    """Kare teması parlaklıktan (dizin adı güvenilmez: 02-04 k/ kökündeki 4 haneli kareler koyu)."""
    return "acik" if np.median(a[::8, ::8]) > 128 else "koyu"


def maske(a: np.ndarray, ref: np.ndarray) -> np.ndarray:
    """İçerik maskesi (2x küçük): zeminden ESIK'ten çok ayrışan piksel; 3x3 açma tek piksel lekeyi atar."""
    m = np.abs(a.astype(np.int16) - ref).max(2) > ESIK
    e = m.copy()
    for dy in (-1, 0, 1):
        for dx in (-1, 0, 1):
            e &= np.roll(np.roll(m, dy, 0), dx, 1)
    d = e.copy()
    for dy in (-1, 0, 1):
        for dx in (-1, 0, 1):
            d |= np.roll(np.roll(e, dy, 0), dx, 1)
    return d.reshape(H // OLCEK, OLCEK, W // OLCEK, OLCEK).any((1, 3))


def adaylar() -> tuple[np.ndarray, np.ndarray]:
    """Kart sol-üst köşe adayları (gerçek px, 4 px adım), kenar payı içinde."""
    xs = np.arange(KENAR, W - KENAR - KART[0] + 1, 4)
    ys = np.arange(KENAR, H - KENAR - KART[1] + 1, 4)
    return np.meshgrid(xs, ys)


def bos_mu(m: np.ndarray, X: np.ndarray, Y: np.ndarray) -> np.ndarray:
    """Her aday için kart + PAY kutusunda içerik yok mu (integral görüntü)."""
    S = np.zeros((m.shape[0] + 1, m.shape[1] + 1), np.int32)
    S[1:, 1:] = m.cumsum(0).cumsum(1)
    x0 = np.clip((X - PAY) // OLCEK, 0, m.shape[1]); x1 = np.clip(-(-(X + KART[0] + PAY) // OLCEK), 0, m.shape[1])
    y0 = np.clip((Y - PAY) // OLCEK, 0, m.shape[0]); y1 = np.clip(-(-(Y + KART[1] + PAY) // OLCEK), 0, m.shape[0])
    return (S[y1, x1] - S[y0, x1] - S[y1, x0] + S[y0, x0]) == 0


def kose_icinde(kose: str, X: np.ndarray, Y: np.ndarray) -> np.ndarray:
    sag, alt = X >= W // 2, Y + KART[1] <= H // 2
    if kose == "sag_ust":
        return sag & alt
    if kose == "sol_alt":
        return (X + KART[0] <= W // 2) & (Y >= H // 2)
    return (X + KART[0] <= W // 2) & alt


def kose_uzakligi(kose: str, X: np.ndarray, Y: np.ndarray) -> np.ndarray:
    dx = (W - KENAR - KART[0] - X) if kose.startswith("sag") else (X - KENAR)
    dy = (Y - KENAR) if kose.endswith("ust") else (H - KENAR - KART[1] - Y)
    return dx + dy


def en_buyuk_bos(m: np.ndarray) -> tuple[int, int, int, int]:
    """İkili maskede en büyük boş dikdörtgen (histogram yöntemi): (x, y, w, h) maske px."""
    hgt = np.zeros(m.shape[1], int)
    en = (0, 0, 0, 0, 0)
    for y in range(m.shape[0]):
        hgt = np.where(m[y], 0, hgt + 1)
        yigin: list[int] = []
        for x in range(m.shape[1] + 1):
            h = hgt[x] if x < m.shape[1] else 0
            while yigin and hgt[yigin[-1]] >= h:
                hh = hgt[yigin.pop()]
                sol = yigin[-1] + 1 if yigin else 0
                if hh * (x - sol) > en[0]:
                    en = (hh * (x - sol), sol, y - hh + 1, x - sol, hh)
            yigin.append(x)
    return en[1:]


def mp4_akisi(yol: str):
    """cikti mp4'ünden saniyede 1 kare (fps=1: kare i ≈ i. sn), bellekte tek kare."""
    p = subprocess.Popen(["ffmpeg", "-nostdin", "-loglevel", "error", "-i", yol, "-vf", "fps=1,format=rgb24",
                          "-f", "rawvideo", "-"], stdout=subprocess.PIPE)
    i, n = 0, W * H * 3
    while True:
        b = p.stdout.read(n)
        if len(b) < n:
            break
        yield i, np.frombuffer(b, np.uint8).reshape(H, W, 3)
        i += 1
    p.wait()


def ornek_sec(kayit: list[dict], bos: np.ndarray, ai: int, ders: str, tercih: str) -> dict[str, dict]:
    """Ders için açık + koyu örnek kare: önce tercih edilen sahne karesi (iki temada var ve yer boşsa), yoksa
    pencerede yer boş olan ilk PNG karesi."""
    sec = {}
    for tema in ("acik", "koyu"):
        aday = [(i, k) for i, k in enumerate(kayit) if k["ders"] == ders and k["tema"] == tema and "mp4" not in k
                and k["pencere"] and bos[i, ai]]
        tr = [x for x in aday if Path(x[1]["kaynak"]).name == tercih]
        if tr or aday:
            sec[tema] = (tr or aday)[0][1]
    return sec


def yer() -> None:
    ref = {t: rgb(OLCUM / ("zemin-%s.png" % t)) for t in ("acik", "koyu")}
    X, Y = adaylar()
    X, Y = X.ravel(), Y.ravel()
    kayit, bos, birlesik = [], [], np.zeros((H // OLCEK, W // OLCEK), bool)
    for ders in DERSLER:
        z = json.loads((K / "projeler" / ders / "zaman.json").read_text(encoding="utf-8"))
        T = z["sahneler"][-1]["t_son"]
        ks = kareler(ders)
        mp4 = {}
        for k in ks:
            if "mp4" in k:
                mp4.setdefault(k["mp4"], {})[k["i"]] = k
                continue
            k["pencere"] = 30 <= k["t"] <= T - 20
            a = np.asarray(Image.open(K / k["kaynak"]).convert("RGB"))
            k["tema"] = tema_bul(a)
            m = maske(a, ref[k["tema"]])
            kayit.append(k); bos.append(bos_mu(m, X, Y))
            birlesik |= m if k["pencere"] else False
        for yol, istek in mp4.items():
            for i, a in mp4_akisi(yol):
                if i in istek:
                    k = istek[i]
                    k["pencere"] = 30 <= k["t"] <= T - 20
                    k["tema"] = tema_bul(a)
                    m = maske(a, ref[k["tema"]])
                    kayit.append(k); bos.append(bos_mu(m, X, Y))
                    birlesik |= m if k["pencere"] else False
        print(ders, "kare", sum(1 for k in kayit if k["ders"] == ders),
              "· pencere (30 sn ≤ t ≤ son − 20 sn)", sum(1 for k in kayit if k["ders"] == ders and k["pencere"]))
    bos = np.array(bos)
    pen = {d: np.array([k["ders"] == d and k["pencere"] for k in kayit]) for d in DERSLER}
    hep = {d: np.array([k["ders"] == d for k in kayit]) for d in DERSLER}
    oran = {d: bos[pen[d]].mean(0) for d in DERSLER}
    puan = np.minimum(*oran.values())
    tablo = {}
    for kose in KOSELER:
        ic = kose_icinde(kose, X, Y)
        en = puan[ic].max()
        sec = np.nonzero(ic & (puan >= en - 1e-9))[0]
        ai = int(sec[np.argmin(kose_uzakligi(kose, X[sec], Y[sec]))])
        qx = slice(W // OLCEK // 2, None) if kose.startswith("sag") else slice(0, W // OLCEK // 2)
        qy = slice(0, H // OLCEK // 2) if kose.endswith("ust") else slice(H // OLCEK // 2, None)
        bx, by, bw, bh = en_buyuk_bos(birlesik[qy, qx])
        ox, oy = (W // 2 if kose.startswith("sag") else 0), (0 if kose.endswith("ust") else H // 2)
        carp = {}
        for d in DERSLER:
            for i in np.nonzero(pen[d] & ~bos[:, ai])[0]:
                carp.setdefault("%s/%s" % (d, kayit[i]["sahne"]), []).append(kayit[i]["t"])
        tablo[kose] = {"ai": ai, "x": int(X[ai]), "y": int(Y[ai]), "puan": round(float(puan[ai]), 3),
                       "ders": {d: {"pencere_bos": int(bos[pen[d], ai].sum()), "pencere": int(pen[d].sum()),
                                    "hep_bos": int(bos[hep[d], ai].sum()), "hep": int(hep[d].sum())} for d in DERSLER},
                       "en_buyuk_bos_bolge": {"x": int(ox + bx * OLCEK), "y": int(oy + by * OLCEK), "w": int(bw * OLCEK),
                                              "h": int(bh * OLCEK)},
                       "carpisan": {k: sorted(set(v)) for k, v in sorted(carp.items())}}
    tam = [k for k in KOSELER if tablo[k]["puan"] >= 1.0]
    if tam:
        secilen, neden = tam[0], "bütün pencere karelerinde boş; aday sırasında ilk"
    else:
        enb = max(tablo[k]["puan"] for k in KOSELER)
        secilen = next(k for k in KOSELER if tablo[k]["puan"] >= enb - 0.02)
        neden = "hiçbir köşe bütün karelerde boş değil; en yüksek boş oranı (aday sırası, 0,02 pay)"
    s = tablo[secilen]
    yaz(YT / "bildirim" / "yer.json", {"x": s["x"], "y": s["y"], "w": KART[0], "h": KART[1], "kose": secilen})
    ornek = {}
    for ders, tercih in (("02-04-ydt-temel", "04-canvas-ornek2-68.6.png"),
                         ("simple-present-temel", "04-canvas-ornek2-31.5.png")):
        for tema, k in ornek_sec(kayit, bos, s["ai"], ders, tercih).items():
            taban = Image.open(K / k["kaynak"]).convert("RGBA")
            (YT / "bildirim" / "ders").mkdir(exist_ok=True)
            taban.convert("RGB").save(YT / "bildirim" / "ders" / ("%s-%s.png" % (ders, tema)))
            kart = Image.open(YT / "bildirim" / ("bildirim-%s.png" % tema)).convert("RGBA")
            assert kart.size == KART, kart.size
            taban.alpha_composite(kart, (s["x"], s["y"]))
            ad = "ornek-%s-%s.png" % (ders, tema)
            taban.convert("RGB").save(YT / "bildirim" / ad)
            ornek[ad] = k["kaynak"]
    yaz(YT / "bildirim" / "olcum" / "yer-tablo.json",
        {"esik": ESIK, "pay": PAY, "kenar": KENAR, "kart": KART, "pencere": "30 sn ≤ t ≤ ders sonu − 20 sn (standart §3)",
         "secilen": secilen, "neden": neden, "koseler": tablo, "ornek": ornek,
         "kare_sayisi": {d: {"hep": int(hep[d].sum()), "pencere": int(pen[d].sum()),
                             "kaynak": sorted({k["kaynak"].split("#")[0].split("/sahneler/")[0] + ("#mp4" if "mp4" in k else "")
                                               for k in kayit if k["ders"] == d})} for d in DERSLER},
         "kareler": [{"ders": k["ders"], "kaynak": k["kaynak"], "sahne": k["sahne"], "t": k["t"], "tema": k["tema"],
                      "pencere": k["pencere"], **{kose: bool(bos[i, tablo[kose]["ai"]]) for kose in KOSELER}}
                     for i, k in enumerate(kayit)]})
    for kose in KOSELER:
        t = tablo[kose]
        print("%s: x %d y %d · puan %.3f · %s · en büyük boş bölge %s"
              % (kose, t["x"], t["y"], t["puan"], {d: "%d/%d" % (v["pencere_bos"], v["pencere"]) for d, v in t["ders"].items()},
                 t["en_buyuk_bos_bolge"]))
    print("seçilen:", secilen, "·", neden, "· örnek:", list(ornek))


if __name__ == "__main__":
    {"ses": ses, "sag": sag, "yer": yer}[sys.argv[1]]()
