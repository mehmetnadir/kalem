"""YouTube dikey parçaları ölçümleri (istem YT-2, 15.11.2026). PNG/WAV/JSON yazar; mp4 üretmez, ses sentezlemez.
  /usr/bin/python3 -I olc.py ses   giriş ve uzun çıkış sesi = yatay dosyanın kopyası (sha256 eşit); kısa çıkış sesi =
                                   önbellek parçası "Faydalı olduysa abone ol." (yatay çıkışta ayrı parça) → olcum/ses.json
  /usr/bin/python3 -I olc.py alt   uzun çıkışta y ≥ 960 zemin dışı piksel (yalnız-zemin kıyası) + öğe kutularının bölge
                                   denetimi (içerik bölgesi, alt yarı, Shorts sağ şeridi) → olcum/alt.json
  /usr/bin/python3 -I olc.py yer   iki dikey dersin kareleri → içerik maskesi → kart yeri → bildirim/yer.json
                                   + bildirim/olcum/yer-tablo.json + bildirim/ornek-*.png + bildirim/ders/*.png
Önkoşul: calistir.sh kareleri yakalamış olur."""
from __future__ import annotations

import glob
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import wave
from pathlib import Path

import numpy as np
from PIL import Image

DY = Path(__file__).resolve().parent
YT = DY.parent
K = YT.parent.parent
OLCUM = DY / "olcum"
sys.path.insert(0, str(DY))
import uret as D  # noqa: E402  (dikey sabitleri; D.Y = yatay üretici)
Y = D.Y
W, H = D.W, D.H
ONB = Path.home() / ".local/share/elevenlabs-onbellek"


def yaz(yol: Path, veri: object) -> None:
    yol.parent.mkdir(parents=True, exist_ok=True)
    yol.write_text(json.dumps(veri, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")


def sha(yol: Path) -> str:
    return hashlib.sha256(yol.read_bytes()).hexdigest()


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
    """10 ms pencere RMS'i eşiği ilk aşan pencerenin başı, son aşanın sonu (sn); yatay olc.py ile aynı yöntem."""
    n = sr // 100
    p = a[: len(a) // n * n].reshape(-1, n)
    db = 20 * np.log10(np.sqrt((p ** 2).mean(1)) + 1e-9)
    i = np.nonzero(db > esik_db)[0]
    return round(i[0] * n / sr, 3), round((i[-1] + 1) * n / sr, 3)


def onbellek_anahtari(t_ses: str, onceki: str, sonraki: str, ses: str, tohum: int) -> str:
    """el.py iste() anahtarı (yatay olc.py ile aynı): ses-sunucu.sh HIZ_EN=0.9 → hız eki [1.0, 0.9]."""
    return hashlib.sha1(json.dumps([t_ses, "tr", onceki, sonraki, ses, "eleven_v4", tohum, 1.0, 0.9],
                                   ensure_ascii=False).encode()).hexdigest()


def ses() -> None:
    out: dict = {"kopya": {}}
    for ad in ("giris", "cikis"):
        kay, hed = YT / ad / "ses" / ("%s.wav" % ad), DY / ad / "ses" / ("%s.wav" % ad)
        hed.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(kay, hed)
        a, sr = wav_oku(hed)
        s0, s1 = soz_araligi(a, sr)
        out["kopya"][ad] = {"kaynak": os.path.relpath(kay, K), "dosya": os.path.relpath(hed, K), "sha256_kaynak": sha(kay),
                            "sha256_dosya": sha(hed), "esit": sha(kay) == sha(hed), "sure": round(ffprobe_sure(hed), 3),
                            "hz": sr, "ilk_soz": s0, "soz_sonu": s1}
    # ---- kısa çıkış: yatay çıkış cümlesinin 1. parçası (el.py ayrı parça olarak sentezledi, önbellekte) ----
    d = YT / "cikis" / "ses"
    senaryo = json.loads((d / "senaryo.json").read_text(encoding="utf-8"))
    rapor = json.loads((d / "sentez.wav.rapor.json").read_text(encoding="utf-8"))
    sure = json.loads((d / "sureler.json").read_text(encoding="utf-8"))[0]
    kimlik, parcalar = senaryo["sesler"]["ogrenci"], senaryo["cumleler"][0]["parcalar"]
    assert parcalar[0][1] == D.KISA_METIN and rapor[0]["metin"] == D.KISA_METIN, parcalar
    metinler = [r.get("ses_metni", r["metin"]) for r in rapor]
    anahtar = onbellek_anahtari(metinler[0], "", " ".join(metinler[1:]), kimlik, rapor[0]["tohum"])
    onb_wav = ONB / (anahtar + ".wav")
    kontrol = sorted(ONB.glob(anahtar + ".kontrol-*.json"))
    assert onb_wav.exists() and kontrol, "önbellekte parça yok: %s → el.py ile sentez gerekir" % anahtar[:12]
    duyulan = json.loads(kontrol[0].read_text(encoding="utf-8"))["duyulan"]
    cumle, sr = wav_oku(d / "cumle-1.wav")
    b0, b1 = sure["parcalar"][0]
    parca = cumle[round(b0 * sr): round(b1 * sr)]
    onb, sr2 = wav_oku(onb_wav)
    assert sr2 == sr and len(onb) == len(parca), (sr2, sr, len(onb), len(parca))
    kazanc = float(np.dot(parca, onb) / np.dot(onb, onb))
    ilinti = float(np.corrcoef(parca, onb)[0, 1])
    assert ilinti > 0.999, "cümle parçası önbellek wav'ı ile aynı değil: %.4f" % ilinti
    kd = DY / "cikis-kisa" / "ses"
    kd.mkdir(parents=True, exist_ok=True)
    pw = kd / "parca.wav"
    with wave.open(str(pw), "wb") as w:
        w.setnchannels(1); w.setsampwidth(2); w.setframerate(sr)
        w.writeframes((np.clip(parca, -1, 32767 / 32768) * 32768).astype("<i2").tobytes())
    kayma = D.kisa_kayma()
    hedef = kd / "cikis-kisa.wav"
    subprocess.run(["ffmpeg", "-nostdin", "-loglevel", "error", "-y", "-i", str(pw), "-af",
                    "adelay=%d:all=1,apad=whole_dur=%.2f,atrim=0:%.2f" % (round(kayma * 1000), D.KISA_SURE, D.KISA_SURE),
                    "-ar", "48000", "-ac", "1", "-c:a", "pcm_s16le", str(hedef)], check=True)
    a, sr3 = wav_oku(hedef)
    s0, s1 = soz_araligi(a, sr3)
    kisa = {"metin": D.KISA_METIN, "yol": "önbellek", "ses_kimligi": kimlik, "onbellek_anahtari": anahtar[:12],
            "onbellek_wav": str(onb_wav), "whisper_kaydi": kontrol[0].name, "duyulan": duyulan,
            "benzerlik": rapor[0]["benzerlik"], "tohum": rapor[0]["tohum"],
            "kaynak_kesit": "%s %.2f–%.2f sn" % (os.path.relpath(d / "cumle-1.wav", K), b0, b1),
            "kesit_onbellek_ilinti": round(ilinti, 6), "kesit_onbellek_kazanc": round(kazanc, 4),
            "dosya": os.path.relpath(hedef, K), "sure": round(ffprobe_sure(hedef), 3), "hz": sr3,
            "kayma": kayma, "ilk_soz": s0, "soz_sonu": s1, "sha256": sha(hedef), "maliyet_karakter": 0}
    out["cikis_kisa"] = kisa
    yaz(kd / "kaynak.json", kisa)
    yaz(OLCUM / "ses.json", out)
    for ad, v in out["kopya"].items():
        print("%s: kopya sha256 eşit %s · %.2f sn · ilk söz %.2f · söz sonu %.2f" % (ad, v["esit"], v["sure"], v["ilk_soz"],
                                                                                v["soz_sonu"]))
    print("cikis-kisa: önbellek %s · Whisper '%s' %.2f · ilinti %.4f · %.2f sn · ilk söz %.2f · söz sonu %.2f"
          % (kisa["onbellek_anahtari"], duyulan, kisa["benzerlik"], ilinti, kisa["sure"], s0, s1))


def rgb(yol: str | Path) -> np.ndarray:
    return np.asarray(Image.open(yol).convert("RGB")).astype(np.int16)


def kutular(dosya: Path) -> dict[str, list]:
    out = {}
    for satir in dosya.read_text().splitlines():
        s = json.loads(satir)
        out[s["t"]] = json.loads(s["olc"])
    return out


def alt() -> None:
    """Uzun çıkış alt yarısı (y ≥ 960) piksel ölçümü + bütün parçalarda öğe kutusu bölge denetimi."""
    piksel = {}
    for tema in ("acik", "koyu"):
        ref = rgb(OLCUM / ("zemin-%s.png" % tema))
        k_ = "" if tema == "acik" else "koyu/"
        for t in ("0.5", "4.0", "19.9"):
            fark = np.abs(rgb(DY / "cikis" / "k" / ("%scikis-%s.png" % (k_, t))) - ref).max(2)
            piksel["%s %s" % (tema, t)] = {"alt_fark_0": int((fark[D.YARI:] > 0).sum()),
                                           "alt_fark_8": int((fark[D.YARI:] > 8).sum()),
                                           "ust_fark_8": int((fark[:D.YARI] > 8).sum())}
    sx, sy0, sy1 = D.SAG_SERIT
    denetim, hata = {}, []
    for parca, kural in (("giris", "icerik"), ("cikis", "ust_yari"), ("cikis-kisa", "icerik")):
        for tema in ("acik", "koyu"):
            for t, bx in kutular(OLCUM / ("%s-kutu-%s.jsonl" % (parca, tema))).items():
                for ad, x0, y0, x1, y1 in bx:
                    if x1 - x0 <= 0:
                        continue
                    sorun = []
                    if x0 < 48 or x1 > W - 48:
                        sorun.append("kenar 48")
                    if kural == "icerik" and (y0 < D.ICERIK[0] or y1 > D.ICERIK[1]):
                        sorun.append("içerik bölgesi dışı")
                    if kural == "ust_yari" and y1 >= D.YARI:
                        sorun.append("alt yarıda")
                    if x1 > sx and y1 > sy0 and y0 < sy1:
                        sorun.append("Shorts sağ şeridi")
                    if y1 > 1536:
                        sorun.append("alt %20")
                    if sorun:
                        hata.append([parca, tema, t, ad, sorun])
                denetim["%s %s %s" % (parca, tema, t)] = bx
    en_alt = {k: max(b[4] for b in v) for k, v in denetim.items() if k.startswith("cikis ")}
    en_sag_kisa = {k: max(b[3] for b in v) for k, v in denetim.items() if k.startswith("cikis-kisa")}
    yaz(OLCUM / "alt.json", {"piksel": piksel, "kutu": denetim, "hata": hata, "cikis_en_alt_y": en_alt,
                             "kisa_en_sag_x": en_sag_kisa})
    for k, v in piksel.items():
        print("uzun çıkış %s: y≥960 fark>0 %d · fark>8 %d · (üst yarı fark>8 %d) · en alt öğe y %.1f"
              % (k, v["alt_fark_0"], v["alt_fark_8"], v["ust_fark_8"], en_alt["cikis %s %s" % tuple(k.split())]))
    print("kutu denetimi: %d sorun" % len(hata), hata[:6])


# ---- bildirim yeri ----
ESIK = 24             # zemin kıyası, kanal farkı (yatay YT-1 ile aynı)
PAY = 16              # kart ile içerik arası en az boşluk (px)
KENAR = 48            # dikey ders güvenli kenarı
UST_YASAK = 250       # huni-v2 §2: platform arayüzü üst 0–250 (istemin yasak listesine ek, aynı kaynak)
ALT_YASAK = 1536      # alt %20 (Shorts başlık, kanal, ses)
OLCEK = 2             # maske 2x küçültülür (540x960); aday adımı 4 px
OLCEKLER = (1.0, 0.9, 0.8)
DERSLER = {"02-04-ydt-temel-dikey": 0.30, "simple-present-temel-dikey": 0.30}   # değer: örnek kare anı (ders payı)
ADAYLAR = ("kunye_alti_sol", "altyazi_ustu_sol")                                  # istem aday sırası
KART_PNG = YT / "bildirim" / "bildirim-acik.png"


def tema_degerleri() -> dict[str, tuple[np.ndarray, float]]:
    """hf_tema CSS'inden zemin rengi ve vinyet koyuluğu (ham renk yazılmaz)."""
    css = Y.hf_tema.CSS
    out = {}
    for tema, kalip in (("koyu", r"#root\{([^}]*)\}"), ("acik", r"#root\.tema-acik\{([^}]*)\}")):
        g = re.search(kalip, css).group(1)
        z = re.search(r"--zemin:#([0-9a-fA-F]{6})", g).group(1)
        v = float(re.search(r"--vin:([0-9.]+)", g).group(1))
        out[tema] = (np.array([int(z[i:i + 2], 16) for i in (0, 2, 4)], np.float32), v)
    return out


def zemin_ref() -> dict[str, list[np.ndarray]]:
    """Tema başına iki zemin modeli: HF sahneleri (circle 1150px, %40 → %100) ve canvas sahneleri (kunye.js vinyetAl:
    r 0,45 H → 0,95 H). Zemin = renk × (1 − α(r)); gren (opaklık ≤ 0,045) eşiğin altında kalır."""
    yy, xx = np.mgrid[0:H, 0:W].astype(np.float32)
    r = np.hypot(xx - W / 2, yy - H / 2)
    out = {}
    for tema, (renk, vin) in tema_degerleri().items():
        hf = vin * np.clip((r - 460) / 690, 0, 1)
        cv = vin * np.clip((r - 0.45 * H) / (0.5 * H), 0, 1)
        out[tema] = [(renk[None, None, :] * (1 - a[..., None])).astype(np.int16) for a in (hf, cv)]
    return out


def maske(a: np.ndarray, ref: list[np.ndarray]) -> np.ndarray:
    """İçerik maskesi (2x küçük): iki zemin modelinden de ESIK'ten çok ayrışan piksel; 3x3 açma tek piksel lekeyi atar."""
    a = a.astype(np.int16)
    m = np.minimum(np.abs(a - ref[0]).max(2), np.abs(a - ref[1]).max(2)) > ESIK
    e = m.copy()
    for dy in (-1, 0, 1):
        for dx in (-1, 0, 1):
            e &= np.roll(np.roll(m, dy, 0), dx, 1)
    d = e.copy()
    for dy in (-1, 0, 1):
        for dx in (-1, 0, 1):
            d |= np.roll(np.roll(e, dy, 0), dx, 1)
    return d.reshape(H // OLCEK, OLCEK, W // OLCEK, OLCEK).any((1, 3))


def tema_bul(a: np.ndarray) -> str:
    return "acik" if np.median(a[::8, ::8]) > 128 else "koyu"


def kareler(ders: str) -> list[dict]:
    """Var olan kareler: sahneler/*/k/*.png + alt dizinleri (ara, ek, koyu, acik), kapak 90-* hariç, yalnız 1080x1920;
    + bu iş için yakalanan bildirim/olcum/<ders>/{,koyu/,sn/} (sn/: pencerede saniyede 1 kare, açık)
    + cikti(-koyu).mp4 saniyede 1 kare (sahne sınırına < 0,5 sn hariç)."""
    kok = K / "projeler" / ders
    z = json.loads((kok / "zaman.json").read_text(encoding="utf-8"))
    sah = {s["klasor"]: s for s in z["sahneler"]}
    ek = DY / "bildirim" / "olcum" / ders
    kaynak = [(p, "var") for p in glob.glob(str(kok / "sahneler/*/k/*.png")) + glob.glob(str(kok / "sahneler/*/k/*/*.png"))]
    kaynak += [(p, "yakalanan") for p in glob.glob(str(ek / "*.png")) + glob.glob(str(ek / "koyu/*.png"))
                + glob.glob(str(ek / "sn/*.png"))]
    out = []
    for p, tur in sorted(kaynak):
        yol, ad = Path(p), Path(p).name
        if tur == "yakalanan":
            sahne = re.match(r"(\d\d-[a-z0-9-]+?)-[\d.]+\.png$", ad).group(1)
        else:
            i = yol.parts.index("k")
            sahne = yol.parts[i - 1]
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
        out.append({"ders": ders, "kaynak": os.path.relpath(p, K), "tur": tur, "sahne": sahne, "t": round(t, 2)})
    sinir = [s["t_son"] for s in z["sahneler"]]
    for mp4 in ("cikti.mp4", "cikti-koyu.mp4"):
        if not (kok / mp4).exists():
            continue
        for i in range(int(z["sahneler"][-1]["t_son"])):
            if min(abs(i - b) for b in sinir) < 0.5:
                continue
            sahne = next(s["klasor"] for s in z["sahneler"] if s["t_bas"] <= i < s["t_son"])
            out.append({"ders": ders, "kaynak": "%s#%d" % (os.path.relpath(kok / mp4, K), i), "tur": "mp4",
                        "sahne": sahne, "t": float(i), "mp4": str(kok / mp4), "i": i})
    return out


def mp4_akisi(yol: str):
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


def adaylar(kw: int, kh: int) -> tuple[np.ndarray, np.ndarray]:
    """Kart sol üst köşe adayları (4 px adım): kenar 48, y ≥ 250, alt %20 dışı, Shorts sağ şeridine girmez."""
    X, Y_ = np.meshgrid(np.arange(KENAR, W - KENAR - kw + 1, 4), np.arange(UST_YASAK, ALT_YASAK - kh + 1, 4))
    X, Y_ = X.ravel(), Y_.ravel()
    sx, sy0, sy1 = D.SAG_SERIT
    serit = (X + kw > sx) & (Y_ + kh > sy0) & (Y_ < sy1)
    return X[~serit], Y_[~serit]


def bos_mu(S: np.ndarray, X: np.ndarray, Y_: np.ndarray, kw: int, kh: int) -> np.ndarray:
    """Kart + PAY kutusunda içerik yok mu (integral görüntü S, maske ölçeğinde)."""
    mh, mw = S.shape[0] - 1, S.shape[1] - 1
    x0 = np.clip((X - PAY) // OLCEK, 0, mw); x1 = np.clip(-(-(X + kw + PAY) // OLCEK), 0, mw)
    y0 = np.clip((Y_ - PAY) // OLCEK, 0, mh); y1 = np.clip(-(-(Y_ + kh + PAY) // OLCEK), 0, mh)
    return (S[y1, x1] - S[y0, x1] - S[y1, x0] + S[y0, x0]) == 0


def integral(m: np.ndarray) -> np.ndarray:
    S = np.zeros((m.shape[0] + 1, m.shape[1] + 1), np.int32)
    S[1:, 1:] = m.cumsum(0).cumsum(1)
    return S


def aday_bolgesi(ad: str, X: np.ndarray, Y_: np.ndarray, kh: int) -> np.ndarray:
    """Aday bölgeleri: künye altı (y 300–700, sol) · altyazı üstü (kart altı 1000–1400, sol; altyazıyla PAY maskede)."""
    sol = X <= W // 2 - 40
    if ad == "kunye_alti_sol":
        return sol & (Y_ >= 300) & (Y_ <= 700)
    return sol & (Y_ + kh >= 1000) & (Y_ + kh <= 1400)


def sec_konum(ad: str, X: np.ndarray, Y_: np.ndarray, puan: np.ndarray, kh: int) -> int:
    """Bölgede en yüksek puan; eşitlikte çapaya en yakın (künye altı: en küçük y; altyazı üstü: en büyük y), sonra en sol."""
    bol = np.nonzero(aday_bolgesi(ad, X, Y_, kh))[0]
    en = puan[bol].max()
    eş = bol[puan[bol] >= en - 1e-9]
    anahtar = Y_[eş] if ad == "kunye_alti_sol" else -Y_[eş]
    eş = eş[anahtar == anahtar.min()]
    return int(eş[np.argmin(X[eş])])


def zaman_kurali(kayit: list[dict], tablo: dict, sonuc: list[dict], secim: dict) -> list[dict]:
    """Bildirim anı kuralı denetimi: saniyede 1 karelik açık seride (02-04 cikti.mp4, simple-present sn/ yakalaması)
    standart anına (%30, ders ≥ 4 dk ise %70; ilk 30 sn hariç) en yakın, 3 ardışık saniyesi boş başlangıç (pencerede)."""
    out = []
    B = tablo[secim["olcek"]]
    for r in sonuc:
        if r["olcek"] != secim["olcek"] or r["aday"] not in ADAYLAR:
            continue
        for d in DERSLER:
            T = json.loads((K / "projeler" / d / "zaman.json").read_text(encoding="utf-8"))["sahneler"][-1]["t_son"]
            seri = {int(k["t"]): bool(B[i, r["_ai"]]) for i, k in enumerate(kayit) if k["ders"] == d and k["tema"] == "acik"
                    and (k["tur"] == "mp4" or "/sn/" in k["kaynak"]) and float(k["t"]).is_integer()}
            hedefler = [max(30.0, 0.30 * T)] + ([0.70 * T] if T >= 240 else [])
            for h in hedefler:
                bas = [s for s in seri if s >= 30 and s + 3 <= T - 20 and all(seri.get(s + j) for j in range(3))]
                en = min(bas, key=lambda s: (abs(s - h), s)) if bas else None
                out.append({"ders": d, "aday": r["aday"], "x": r["x"], "y": r["y"], "hedef": round(h, 1), "seri_kare": len(seri),
                            "bos_bas": en, "fark": None if en is None else round(en - h, 1)})
    return out


def yer() -> None:
    ref = zemin_ref()
    kart = Image.open(KART_PNG)
    KW, KH = kart.size
    olc = {s: (round(KW * s), round(KH * s)) for s in OLCEKLER}
    aday = {s: adaylar(*olc[s]) for s in OLCEKLER}
    kayit: list[dict] = []
    bos: dict[float, list[np.ndarray]] = {s: [] for s in OLCEKLER}
    platform = []                         # platform bandı (y ≥ 1560) maske pikseli: zemin modeli denetimi
    birlesik = {d: np.zeros((H // OLCEK, W // OLCEK), bool) for d in DERSLER}

    def isle(k: dict, a: np.ndarray) -> None:
        k["tema"] = tema_bul(a)
        m = maske(a, ref[k["tema"]])
        S = integral(m)
        for s in OLCEKLER:
            bos[s].append(bos_mu(S, *aday[s], *olc[s]))
        platform.append(int(m[1560 // OLCEK:].sum()))
        if k["pencere"]:
            birlesik[k["ders"]] |= m
        kayit.append(k)

    for ders in DERSLER:
        z = json.loads((K / "projeler" / ders / "zaman.json").read_text(encoding="utf-8"))
        T = z["sahneler"][-1]["t_son"]
        mp4: dict[str, dict[int, dict]] = {}
        for k in kareler(ders):
            k["pencere"] = 30 <= k["t"] <= T - 20
            if "mp4" in k:
                mp4.setdefault(k["mp4"], {})[k["i"]] = k
                continue
            isle(k, np.asarray(Image.open(K / k["kaynak"]).convert("RGB")))
        for yol, ks in mp4.items():
            for i, a in mp4_akisi(yol):
                if i in ks:
                    isle(ks[i], a)
        print("%s: %d kare işlendi" % (ders, sum(1 for k in kayit if k["ders"] == ders)), flush=True)
    print("zemin modeli denetimi: platform bandı (y ≥ 1560) maske pikseli en çok %d, ortanca %d"
          % (max(platform), int(np.median(platform))))
    pen = np.array([k["pencere"] for k in kayit])
    dersv = np.array([k["ders"] for k in kayit])
    sonuc, tablo = [], {}
    for s in OLCEKLER:
        B = np.array(bos[s])
        X, Y_ = aday[s]
        kw, kh = olc[s]
        oran = {d: B[pen & (dersv == d)].mean(0) for d in DERSLER}
        oran_hep = {d: B[dersv == d].mean(0) for d in DERSLER}
        puan = np.minimum(*oran.values())
        for ad in ADAYLAR + ("en_iyi",):
            if ad == "en_iyi":
                en = puan.max()
                eş = np.nonzero(puan >= en - 1e-9)[0]
                ai = int(eş[np.lexsort((X[eş], Y_[eş]))[0]])
            else:
                ai = sec_konum(ad, X, Y_, puan, kh)
            satir = {"aday": ad, "olcek": s, "x": int(X[ai]), "y": int(Y_[ai]), "w": kw, "h": kh, "puan": round(float(puan[ai]), 4)}
            for d in DERSLER:
                mp = pen & (dersv == d)
                satir[d] = {"pencere_bos": int(B[mp, ai].sum()), "pencere": int(mp.sum()),
                            "hepsi_bos": int(B[dersv == d, ai].sum()), "hepsi": int((dersv == d).sum()),
                            "oran_hep": round(float(oran_hep[d][ai]), 4)}
            satir["_ai"] = ai
            sonuc.append(satir)
        tablo[s] = B
    for r in sonuc:
        print("%-17s ölçek %.1f  x %4d y %4d (%dx%d)  puan %.3f  %s" % (
            r["aday"], r["olcek"], r["x"], r["y"], r["w"], r["h"], r["puan"],
            " · ".join("%s pencere %d/%d hepsi %d/%d" % (d[:13], r[d]["pencere_bos"], r[d]["pencere"], r[d]["hepsi_bos"],
                                                        r[d]["hepsi"]) for d in DERSLER)))
    # seçim: aday sırası × ölçek (büyükten küçüğe), pencere karelerinin hepsinde boş olan ilk yer. Yoksa ölçek 1,0'da
    # en yüksek puanlı aday (küçültme ancak yeri bütün karelerde boşaltıyorsa: kart yazısı 40 px ≈ telefonda 14 px)
    secim = next((r for s in OLCEKLER for ad in ADAYLAR for r in sonuc
                  if r["aday"] == ad and r["olcek"] == s and r["puan"] >= 1.0), None)
    if secim is None:
        secim = max((r for r in sonuc if r["aday"] in ADAYLAR and r["olcek"] == OLCEKLER[0]), key=lambda r: r["puan"])
    B = tablo[secim["olcek"]]
    ai = secim["_ai"]
    zk = zaman_kurali(kayit, tablo, sonuc, secim)
    yer_json = {"x": secim["x"], "y": secim["y"], "w": secim["w"], "h": secim["h"], "kose": secim["aday"],
                "olcek": secim["olcek"]}
    yaz(DY / "bildirim" / "yer.json", yer_json)
    # sahne dökümü (seçilen yer, pencere kareleri)
    dokum = {}
    for d in DERSLER:
        for i, k in enumerate(kayit):
            if k["ders"] == d and k["pencere"]:
                v = dokum.setdefault(d, {}).setdefault(k["sahne"][:2], [0, 0])
                v[0] += int(B[i, ai]); v[1] += 1
    # örnek kareler: ders başına açık + koyu; zaman kuralının bulduğu bildirim anının ortasına (başlangıç + 1,5 sn) en yakın,
    # yer boş olan kare (PNG ya da mp4). Açık → 1. bildirim, koyu → son bildirim.
    ornek = {}
    (DY / "bildirim" / "ders").mkdir(parents=True, exist_ok=True)
    for d in DERSLER:
        anlar = [r["bos_bas"] for r in zk if r["ders"] == d and r["aday"] == secim["aday"] and r["bos_bas"] is not None]
        for tema, an in (("acik", anlar[0]), ("koyu", anlar[-1])):
            aday_k = [(abs(k["t"] - an - 1.5), "mp4" in k, i) for i, k in enumerate(kayit)
                      if k["ders"] == d and k["tema"] == tema and k["pencere"] and B[i, ai]]
            k = kayit[min(aday_k)[2]]
            if "mp4" in k:
                r_ = subprocess.run(["ffmpeg", "-nostdin", "-loglevel", "error", "-i", k["mp4"], "-vf",
                                     "fps=1,select=eq(n\\,%d),format=rgb24" % k["i"], "-frames:v", "1", "-f", "rawvideo", "-"],
                                    capture_output=True, check=True)
                taban = Image.fromarray(np.frombuffer(r_.stdout, np.uint8).reshape(H, W, 3)).convert("RGBA")
            else:
                taban = Image.open(K / k["kaynak"]).convert("RGBA")
            assert bos_mu(integral(maske(np.asarray(taban.convert("RGB")), ref[tema])), np.array([secim["x"]]),
                          np.array([secim["y"]]), secim["w"], secim["h"])[0], "örnek karede yer dolu: %s" % k["kaynak"]
            taban.convert("RGB").save(DY / "bildirim" / "ders" / ("%s-%s.png" % (d, tema)))
            kp = Image.open(YT / "bildirim" / ("bildirim-%s.png" % tema)).convert("RGBA")
            if secim["olcek"] != 1.0:
                kp = kp.resize((secim["w"], secim["h"]), Image.LANCZOS)
            taban.alpha_composite(kp, (secim["x"], secim["y"]))
            hedef_png = DY / "bildirim" / ("ornek-%s-%s.png" % (d, tema))
            taban.convert("RGB").save(hedef_png)
            ornek["%s %s" % (d, tema)] = {"kaynak": k["kaynak"], "t": k["t"], "sahne": k["sahne"], "bildirim_bas": an,
                                          "png": os.path.relpath(hedef_png, K)}
    # birleşik maske (pencere): seçilen yer kutusu içinde içerik pikseli
    bm = {d: int(m[(secim["y"] - PAY) // OLCEK: -(-(secim["y"] + secim["h"] + PAY) // OLCEK),
                   (secim["x"] - PAY) // OLCEK: -(-(secim["x"] + secim["w"] + PAY) // OLCEK)].sum())
          for d, m in birlesik.items()}
    for d, m in birlesik.items():
        Image.fromarray((~m * 255).astype(np.uint8)).save(DY / "bildirim" / "olcum" / ("birlesik-%s.png" % d))
    ozet = {"yer": yer_json, "yontem": {"esik": ESIK, "pay": PAY, "kenar": KENAR, "ust_yasak": UST_YASAK,
                                        "alt_yasak": ALT_YASAK, "sag_serit": D.SAG_SERIT, "olcekler": OLCEKLER,
                                        "pencere": "30 sn ≤ t ≤ ders sonu − 20 sn"},
            "aday": [{k: v for k, v in r.items() if k != "_ai"} for r in sonuc],
            "sahne_dokumu": dokum, "zaman_kurali": zk, "ornek": ornek, "birlesik_maske_kutu_pikseli": bm,
            "platform_bandi_maske": {"en_cok": max(platform), "ortanca": int(np.median(platform))},
            "kare_sayisi": {d: {t: sum(1 for k in kayit if k["ders"] == d and k["tur"] == t) for t in ("var", "yakalanan", "mp4")}
                            for d in DERSLER},
            "kareler": [{**{k: v for k, v in kk.items() if k not in ("mp4", "i")}, "bos": bool(B[i, ai])}
                        for i, kk in enumerate(kayit)]}
    yaz(DY / "bildirim" / "olcum" / "yer-tablo.json", ozet)
    print("seçilen:", yer_json, "· sahne dökümü", dokum, "· birleşik maske kutuda", bm)
    for r in zk:
        print("zaman kuralı %(ders)s %(aday)s: hedef %(hedef).1f sn → en yakın 3 sn boş başlangıç %(bos_bas)s (fark %(fark)s)" % r)
    print("örnekler:", {k: (v["sahne"], v["t"]) for k, v in ornek.items()})


if __name__ == "__main__":
    {"ses": ses, "alt": alt, "yer": yer}[sys.argv[1]]()
