#!/usr/bin/env python3
"""Sahneleri tek videoya birleştirir: sahneler arası geçiş + kareye kilitli Tone.js efekt sesi (+ isteğe bağlı anlatım).
  python3 birlestir.py ornek/ucan-makine [--gecis BookFlip] [--etiket] [--anlatim ses.wav] [--plan] [--tema acik|koyu] [--efekt hisirti|tam]
--efekt KIP: efekt sesi olayları. hisirti (varsayılan) = yalnız kalem hışırtısı (tur "cizgi"); tam = bütün olaylar
  (tık, vuruş, sayfa ...). zaman.json["efekt"] varsa o, bayrak üstün.
--gecis ADI: varsayılan geçiş (sahnede "gecis" yoksa). Sahne başına: zaman.json sahneler[i]["gecis"] = i. ile i+1. sahne arası.
  Ad gl-transitions'ta varsa (BookFlip, Fade...) gl-transitions yolu; yoksa ffmpeg xfade adı sayılır (ör. "fade").
  Sayfa ses olayı yalnız gl-transitions geçişlerinde basılır; xfade geçişinde olay yok.
--anlatim WAV: yol proje dizinine, sonra paket köküne göre (ya da mutlak). Yoksa zaman.json["anlatim"] kullanılır; o da
  yoksa eski davranış (yalnız efekt sesi). Karışım: anlatım tam seviye, efekt sesi -9 dB; loudnorm; süre = video süresi.
--plan: hiçbir şey render etmez, _is silmez; sahne/kare/ofset/geçiş tablosunu ve anlatım süresini basıp çıkar.
--etiket: her sahnenin altına motor kartı basar (zaman.json'da sahne "etiket": [motor, ne yapıyor, (yardımcı)],
ilk geçişte "gecis_etiketi"). Anlatım/tanıtım videosu için; düz kullanımda kapalı.
--tema: zaman.json["tema"] (varsayılan "acik", K19) değerini geçersiz kılar. Sahne videoları o temayla yakalanmış olmalıdır
  (sahnenin calistir.sh --tema ...). --plan ve --etiket tema adını yazar; çıktı adı: acik -> cikti.mp4, koyu -> cikti-koyu.mp4.
Girdi: <proje>/zaman.json + her sahnenin <proje>/sahneler/<klasor>/video.mp4 ve olaylar.json. <proje> mutlak yol da olur.
Çıktı: <proje>/cikti.mp4 (+ <proje>/_is/ ara dosyalar, <proje>/kontrol.png: 12 karo, her karoda zaman etiketi).
Geçiş, A'nın son N karesiyle B'nin ilk N karesini üst üste bindirir; toplam süre = kareler toplamı - N x (sahne-1)."""
from __future__ import annotations
import contextlib, json, os, shutil, subprocess, sys, tempfile

KOK = os.path.dirname(os.path.abspath(__file__))
GL_JSON = os.path.join(KOK, "motorlar/yardimci/node_modules/gl-transitions/gl-transitions.json")
ARIAL, MENLO = "/System/Library/Fonts/Supplemental/Arial.ttf", "/System/Library/Fonts/Menlo.ttc"
EFEKT_VOLUME = 0.35   # -9 dB (tam kip)
EFEKT_VOLUME_HISIRTI = 3.0   # +9,5 dB: yalnız hışırtı -9 dB ile kısıktı (tepe -43 dB, 04.11)
TEMALAR = ("acik", "koyu")
EFEKTLER = ("hisirti", "tam")


# ---------- saf işlevler (ağ/ffmpeg yok; testler bunları sınar) ----------

def planla(sahneler: list[dict], N: int, varsayilan: str = "BookFlip") -> list[dict]:
    """Her sahne için gövde aralığı [bas, son), küresel ofset, sonraki sahneye geçiş adı ve kare sayısı.
    Kare sayısı gerçek sayı (_k) varsa o, yoksa zaman.json'daki "kare". Son sahnenin geçişi None."""
    plan, ofs = [], 0
    for i, s in enumerate(sahneler):
        k = s.get("_k", s["kare"])
        son_sahne = i == len(sahneler) - 1
        plan.append({"no": s.get("no", i + 1), "klasor": s.get("klasor", ""), "kare": k, "ofs": ofs,
                     "bas": N if i > 0 else 0, "son": k if son_sahne else k - N,
                     "gecis": None if son_sahne else s.get("gecis", varsayilan)})
        ofs += k - N
    return plan


def tema_oku(z: dict, ezme: str | None = None) -> str:
    """Tema: --tema ezmesi > zaman.json["tema"] > "acik" (K19: render varsayılanı açık). Geçersiz ad hata verir."""
    t = ezme or z.get("tema") or "acik"
    if t not in TEMALAR: raise ValueError(f"tema acik ya da koyu olmalı: {t!r}")
    return t


def efekt_oku(z: dict, ezme: str | None = None) -> str:
    """Efekt kipi: --efekt ezmesi > zaman.json["efekt"] > "hisirti". Geçersiz ad hata verir."""
    e = ezme or z.get("efekt") or "hisirti"
    if e not in EFEKTLER: raise ValueError(f"efekt hisirti ya da tam olmalı: {e!r}")
    return e


def olaylari_suz(olaylar: list[dict], kip: str) -> list[dict]:
    """hisirti: yalnız tur == "cizgi" (kalem hışırtısı; sayfa/tık/vuruş çalmaz). tam: hepsi."""
    if kip == "tam": return list(olaylar)
    if kip == "hisirti": return [o for o in olaylar if o.get("tur") == "cizgi"]
    raise ValueError(f"bilinmeyen efekt kipi: {kip!r}")


def efekt_kunyesi(kip: str, n: int, m: int) -> str:
    return f"efekt: {kip} ({n}/{m} olay)"


def cikti_adi(tema: str, taban: str = "cikti") -> str:
    """Açık tema: cikti.mp4 (varsayılan); koyu: cikti-koyu.mp4. Aynı kural kontrol.png için de geçerlidir."""
    return f"{taban}.mp4" if tema == "acik" else f"{taban}-koyu.mp4"


def toplam_kare(plan: list[dict], N: int = 0) -> int:
    """Son sahnede N düşülmedi: TOPLAM = Σ(kare-N) + N = son sahnenin ofseti + karesi."""
    return plan[-1]["ofs"] + plan[-1]["kare"] if plan else 0


def gecis_turu(ad: str, gl_adlari: set[str]) -> str:
    """'gl' = gl-transitions (ortak/yakala.py + gecis.html), 'xfade' = ffmpeg xfade adı."""
    return "gl" if ad in gl_adlari else "xfade"


def gl_adlari_oku(yol: str = GL_JSON) -> set[str]:
    try:
        with open(yol) as f: return {t["name"] for t in json.load(f)}
    except (OSError, ValueError, KeyError):
        return set()


def xfade_filtre(ad: str, k: int, N: int, fps: int) -> str:
    """A'nın son N karesi ile B'nin ilk N karesi: tam N kare çıkan xfade zinciri (girdi 0 = A, girdi 1 = B)."""
    return (f"[0:v]trim=start_frame={k - N}:end_frame={k},setpts=PTS-STARTPTS[a];"
            f"[1:v]trim=start_frame=0:end_frame={N},setpts=PTS-STARTPTS[b];"
            f"[a][b]xfade=transition={ad}:duration={N / fps:.6f}:offset=0,format=yuv420p")


def karisim_filtre(anlatim_var: bool, sure_sn: float = 0.0, kip: str = "tam") -> list[str]:
    """Ses filtre_complex parçaları; çıkış etiketi [s]. Girdi 1 = efekt sesi, girdi 2 = anlatım (varsa).
    Anlatım var: efekt -9 dB, amix (normalize=0), süre video süresine kırpılır/sessizlikle dolar, loudnorm."""
    ln = "loudnorm=I=-16:TP=-1.5:LRA=11"
    if not anlatim_var:
        return [f"[1:a]{ln}[s]"]
    hacim = EFEKT_VOLUME_HISIRTI if kip == "hisirti" else EFEKT_VOLUME
    return [f"[1:a]volume={hacim}[e]",
            f"[2:a]apad[an]",
            f"[an][e]amix=inputs=2:duration=longest:normalize=0,atrim=duration={sure_sn:.3f},{ln}[s]"]


def kontrol_etiketleri(toplam: int, fps: int, adet: int = 12) -> list[tuple[int, str]]:
    """kontrol.png karoları: (kare no, 'k=<kare>  t=<sn>') — select ile aynı adım."""
    adim = max(1, toplam // adet)
    return [(n, f"k={n}  t={n / fps:.2f} sn") for n in range(0, toplam, adim)][:adet]


def plan_tablosu(plan: list[dict], N: int, fps: int, gercek: dict[str, int | None], gl_adlari: set[str],
                 anlatim: str | None = None, anlatim_sn: float | None = None, tema: str = "acik",
                 efekt: str | None = None) -> str:
    """--plan çıktısı: sahne tablosu + toplam + anlatım. gercek: klasör -> ffprobe kare (None = video.mp4 yok)."""
    sat = [f"{'no':>2} {'klasör':<26} {'kare':>5} {'video':<7} {'gövde':<11} {'ofs(kare)':>9} {'ofs(sn)':>8}  geçiş"]
    for p in plan:
        g = gercek.get(p["klasor"])
        v = "yok" if g is None else (f"{g}" if g == p["kare"] else f"{g}!")
        gc = "-" if p["gecis"] is None else f"{p['gecis']} ({gecis_turu(p['gecis'], gl_adlari)})"
        sat.append(f"{p['no']:>2} {p['klasor']:<26} {p['kare']:>5} {v:<7} {p['bas']}-{p['son']:<8} "
                   f"{p['ofs']:>9} {p['ofs'] / fps:>8.2f}  {gc}")
    T = toplam_kare(plan, N)
    sat.append(f"TOPLAM {T} kare = {T / fps:.2f} sn (N={N}, fps={fps}); video sütunu: 'yok' = video.mp4 yok, '!' = zaman.json'dan farklı")
    sat.append(f"tema: {tema}  (çıktı: {cikti_adi(tema)})")
    if efekt: sat.append(efekt)
    sat.append("anlatım: " + ("yok" if not anlatim else f"{anlatim}  " +
               ("(dosya yok)" if anlatim_sn is None else f"{anlatim_sn:.2f} sn")))
    return "\n".join(sat)


def yol_coz(yol: str, *tabanlar: str) -> str:
    """Mutlak yol aynen; göreli yol tabanların ilkinde varsa orada, yoksa ilk tabana göre."""
    if os.path.isabs(yol): return yol
    for t in tabanlar:
        if os.path.exists(os.path.join(t, yol)): return os.path.join(t, yol)
    return os.path.join(tabanlar[0], yol)


def arg_degeri(argv: list[str], bayrak: str) -> str | None:
    return argv[argv.index(bayrak) + 1] if bayrak in argv else None


# ---------- ffmpeg / ffprobe sarmalayıcıları ----------

def ff(*a: str) -> None: subprocess.run(["ffmpeg", "-y", "-loglevel", "error", *a], check=True)


def kare_say(v: str) -> int:
    return int(subprocess.run(["ffprobe", "-v", "error", "-count_frames", "-select_streams", "v:0", "-show_entries",
                               "stream=nb_read_frames", "-of", "csv=p=0", v], capture_output=True, text=True, check=True).stdout.strip())


def sure_sn(dosya: str) -> float | None:
    if not os.path.exists(dosya): return None
    r = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", dosya],
                       capture_output=True, text=True)
    try: return float(r.stdout.strip())
    except ValueError: return None


@contextlib.contextmanager
def kok_ici(d: str):
    """yakala.py/render.mjs dosyaları paket kökünden HTTP ile sunar; d paket dışındaysa (mutlak proje yolu) iş geçici
    bir klasörde, paket kökü altında yapılır (with bitince silinir). Paket içindeyse d aynen kullanılır."""
    if not os.path.relpath(d, KOK).startswith(".."):
        os.makedirs(d, exist_ok=True); yield d; return
    with tempfile.TemporaryDirectory(prefix=".gecici-", dir=KOK) as t:
        yield t


def ses_render(olaylar: str, wav: str) -> None:
    """ses/render.mjs olay dosyasını paket kökünden HTTP ile okur (paket dışı proje için kok_ici ile kopyalanır)."""
    with kok_ici(os.path.dirname(olaylar)) as d:
        if d != os.path.dirname(olaylar): shutil.copy(olaylar, os.path.join(d, "olaylar.json"))
        subprocess.run(["node", os.path.join(KOK, "ses/render.mjs"), os.path.relpath(os.path.join(d, "olaylar.json"), KOK), wav], check=True)


def kart(satirlar, yol):
    """Defter kağıdı rengi küçük kart: motor adı (Fell) + ne yaptığı (Garamond italik) + isteğe bağlı yardımcı satırı."""
    from PIL import Image, ImageDraw, ImageFont
    F = lambda d, n: ImageFont.truetype(os.path.join(KOK, "ortak/font", d), n)
    yazi = [(satirlar[0], F("IMFeENrm28P.ttf", 58), (43, 29, 18)), (satirlar[1], F("EBGaramond-Italic.ttf", 37), (90, 70, 50))]
    if len(satirlar) > 2: yazi.append((satirlar[2], F("EBGaramond.ttf", 30), (120, 98, 72)))
    d0 = ImageDraw.Draw(Image.new("RGBA", (1, 1)))
    gen = max(d0.textlength(t, font=f) for t, f, _ in yazi) + 2 * 30 + 26
    yuk = 24 + 68 + 46 + (40 if len(yazi) > 2 else 0) + 20
    im = Image.new("RGBA", (int(gen) + 12, yuk + 12), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    d.rounded_rectangle((8, 9, gen + 8, yuk + 9), 8, fill=(60, 40, 20, 40))                     # yumuşak gölge
    d.rounded_rectangle((3, 3, gen + 3, yuk + 3), 8, fill=(244, 235, 214, 238), outline=(43, 29, 18, 200), width=2)
    d.ellipse((30, 26 + 24, 46, 26 + 40), fill=(179, 38, 30, 255))                                 # tek kırmızı nokta
    y = 22
    for i, (t, f, c) in enumerate(yazi):
        d.text((30 + (26 if i == 0 else 0), y), t, font=f, fill=c + (255,)); y += [70, 46, 40][i]
    im.save(yol); return im.size


def kontrol_yaz(cikti: str, hedef: str, toplam: int, fps: int, kunye: str = "") -> None:
    """12 karoluk 6x2 kontrol.png üretir; karolara zaman etiketi basar.
    Bu ffmpeg freetype'sız (drawtext yok) olduğundan etiket PIL ile çizilir; PIL yoksa etiketsiz bırakılır (uyarı)."""
    adim = max(1, toplam // 12)
    ff("-i", cikti, "-vf", f"select='not(mod(n\\,{adim}))',scale=320:-1,tile=6x2", "-frames:v", "1", "-fps_mode", "passthrough", hedef)
    try:
        from PIL import Image, ImageDraw, ImageFont
    except ImportError:
        print("uyarı: PIL yok, kontrol.png karoları etiketsiz"); return
    yazi = next((ImageFont.truetype(f, 15) for f in (ARIAL, MENLO) if os.path.exists(f)), ImageFont.load_default())
    im = Image.open(hedef).convert("RGB"); d = ImageDraw.Draw(im)
    kh = im.size[0] // 6; kv = im.size[1] // 2
    for j, (_, et) in enumerate(kontrol_etiketleri(toplam, fps)):
        x, y = (j % 6) * kh + 4, (j // 6) * kv + 4
        w = d.textlength(et, font=yazi)
        d.rectangle((x - 2, y - 1, x + w + 3, y + 19), fill=(0, 0, 0))
        d.text((x, y), et, font=yazi, fill=(255, 255, 255))
    if kunye:
        sar = Image.new("RGB", (im.size[0], im.size[1] + 24), (0, 0, 0))
        sar.paste(im, (0, 0)); ImageDraw.Draw(sar).text((6, im.size[1] + 3), kunye, font=yazi, fill=(255, 255, 255)); im = sar
    im.save(hedef)


# ---------- akış ----------

def main(argv: list[str]) -> None:
    pozisyonel = [a for i, a in enumerate(argv[1:], 1) if not a.startswith("--") and argv[i - 1] not in ("--gecis", "--anlatim", "--tema", "--efekt")]
    proje = pozisyonel[0].rstrip("/")
    GECIS = arg_degeri(argv, "--gecis") or "BookFlip"
    P = proje if os.path.isabs(proje) else os.path.join(KOK, proje)
    Z = json.load(open(os.path.join(P, "zaman.json")))
    FPS, W, H, N = Z["fps"], Z["genislik"], Z["yukseklik"], Z["gecis_kare"]
    S = Z["sahneler"]
    try: TEMA = tema_oku(Z, arg_degeri(argv, "--tema"))
    except ValueError as e: sys.exit(str(e))
    try: EFEKT = efekt_oku(Z, arg_degeri(argv, "--efekt"))
    except ValueError as e: sys.exit(str(e))
    gl = gl_adlari_oku()
    an = arg_degeri(argv, "--anlatim") or Z.get("anlatim")
    an_yol = yol_coz(an, P, KOK) if an else None

    if "--plan" in argv:
        gercek = {}
        for s in S:
            v = os.path.join(P, "sahneler", s["klasor"], "video.mp4")
            gercek[s["klasor"]] = kare_say(v) if os.path.exists(v) else None
        pl = planla([{**s, "_k": gercek[s["klasor"]]} if gercek[s["klasor"]] else s for s in S], N, GECIS)
        tum = []
        for i, (s, p) in enumerate(zip(S, pl)):
            oj = os.path.join(P, "sahneler", s["klasor"], "olaylar.json")
            tum += json.load(open(oj)) if os.path.exists(oj) else []
            if p["gecis"] and gecis_turu(p["gecis"], gl) == "gl": tum.append({"tur": "sayfa"})
        ek = efekt_kunyesi(EFEKT, len(olaylari_suz(tum, EFEKT)), len(tum))
        print(plan_tablosu(pl, N, FPS, gercek, gl, an_yol, sure_sn(an_yol) if an_yol else None, TEMA, ek)); return

    IS = os.path.join(P, "_is"); shutil.rmtree(IS, ignore_errors=True); os.makedirs(IS)
    KOD = ["-c:v", "libx264", "-crf", "16", "-pix_fmt", "yuv420p", "-r", str(FPS)]
    if an_yol and not os.path.exists(an_yol): sys.exit(f"eksik anlatım: {an_yol}")

    for s in S:
        v = os.path.join(P, "sahneler", s["klasor"], "video.mp4")
        if not os.path.exists(v): sys.exit(f"eksik: {v}")
        k = kare_say(v)
        if k != s["kare"]: print(f"uyarı: {s['klasor']} {k} kare, beklenen {s['kare']} (gerçek sayı kullanılır)")
        s["_v"], s["_k"] = v, k

    PL = planla(S, N, GECIS)
    parca, olay = [], []
    for i, (s, p) in enumerate(zip(S, PL)):
        ofs = p["ofs"]
        g = os.path.join(IS, f"govde{i}.mp4")
        ff("-i", s["_v"], "-vf", f"trim=start_frame={p['bas']}:end_frame={p['son']},setpts=PTS-STARTPTS", "-an", *KOD, g)
        parca.append(g)
        oj = os.path.join(P, "sahneler", s["klasor"], "olaylar.json")
        for o in (json.load(open(oj)) if os.path.exists(oj) else []):
            olay.append({**o, "kare": o["kare"] + ofs, "sahne": s["no"]})
        if i < len(S) - 1:
            ad = p["gecis"]; gv = os.path.join(IS, f"gecis{i}.mp4")
            if gecis_turu(ad, gl) == "gl":
                with kok_ici(os.path.join(IS, f"gecis{i}")) as d:
                    os.makedirs(d + "/a", exist_ok=True); os.makedirs(d + "/b", exist_ok=True)
                    ff("-i", s["_v"], "-vf", f"select=gte(n\\,{s['_k'] - N})", "-fps_mode", "passthrough", "-start_number", "0", d + "/a/%04d.png")
                    ff("-i", S[i + 1]["_v"], "-vf", f"select=lt(n\\,{N})", "-fps_mode", "passthrough", "-start_number", "0", d + "/b/%04d.png")
                    rel = os.path.relpath(d, KOK)
                    subprocess.run([sys.executable, os.path.join(KOK, "ortak/yakala.py"), f"ortak/gecis.html?k={rel}&ad={ad}&n={N}&w={W}&h={H}",
                                    d + "/cikis", str(W), str(H)], check=True)
                    ff("-framerate", str(FPS), "-i", d + "/cikis/%04d.png", *KOD, gv)
                olay.append({"kare": ofs + s["_k"] - N, "tur": "sayfa", "guc": 0.8})
            else:
                ff("-i", s["_v"], "-i", S[i + 1]["_v"], "-filter_complex", xfade_filtre(ad, s["_k"], N, FPS),
                   "-frames:v", str(N), "-an", *KOD, gv)
                if kare_say(gv) != N: sys.exit(f"xfade {ad}: {kare_say(gv)} kare, beklenen {N}")
            parca.append(gv)

    TOPLAM = toplam_kare(PL, N)
    if "--etiket" in argv: print(f"etiket: tema={TEMA}, çıktı {cikti_adi(TEMA)}")

    if "--etiket" in argv:
        kartlar = []
        for i, (s, p) in enumerate(zip(S, PL)):
            bas = p["ofs"] + p["bas"]; son = p["ofs"] + p["son"]
            if s.get("etiket"): kartlar.append((s["etiket"], bas + 12, son - 6, "sol"))
            if i == 0 and Z.get("gecis_etiketi"): kartlar.append((Z["gecis_etiketi"], son - 20, son + N + 30, "sag"))
        girdi, zincir, onceki = [], [], "[0:v]"
        for k, (st, a, b, yer) in enumerate(kartlar):
            yol = os.path.join(IS, f"kart{k}.png"); w, h = kart(st, yol)
            x = 48 if yer == "sol" else W - w - 48; y = H - h - 40
            girdi += ["-loop", "1", "-framerate", str(FPS), "-t", f"{TOPLAM / FPS:.3f}", "-i", yol]
            ta, tb = a / FPS, b / FPS
            zincir.append(f"[{k + 1}:v]format=rgba,fade=in:st={ta:.3f}:d=0.4:alpha=1,fade=out:st={tb - 0.4:.3f}:d=0.4:alpha=1[e{k}]")
            zincir.append(f"{onceki}[e{k}]overlay={x}:{y}:enable='between(t,{ta:.3f},{tb:.3f})'[v{k}]"); onceki = f"[v{k}]"
        _etiket = (girdi, zincir, onceki, os.path.join(IS, "etiketli.mp4"))
    liste = os.path.join(IS, "liste.txt")
    open(liste, "w").write("".join(f"file '{p}'\n" for p in parca))
    sessiz = os.path.join(IS, "sessiz.mp4")
    ff("-f", "concat", "-safe", "0", "-i", liste, "-c", "copy", sessiz)
    if "--etiket" in argv and _etiket[1]:
        girdi, zincir, onceki, etiketli = _etiket
        ff("-i", sessiz, *girdi, "-filter_complex", ";".join(zincir), "-map", onceki, "-frames:v", str(TOPLAM), *KOD, etiketli); sessiz = etiketli
    toplam_olay = len(olay)
    olay = olaylari_suz(olay, EFEKT)
    olay.sort(key=lambda o: o["kare"])
    json.dump({"fps": FPS, "kare": TOPLAM, "olaylar": olay}, open(os.path.join(IS, "olaylar.json"), "w"), ensure_ascii=False, indent=0)
    wav = os.path.join(IS, "ses.wav")
    ses_render(os.path.join(IS, "olaylar.json"), wav)
    cikti = os.path.join(P, cikti_adi(TEMA))
    if an_yol:
        ff("-i", sessiz, "-i", wav, "-i", an_yol, "-filter_complex", ";".join(karisim_filtre(True, TOPLAM / FPS, EFEKT)),
           "-map", "0:v", "-map", "[s]", "-c:v", "copy", "-c:a", "aac", "-b:a", "192k", "-ar", "48000", "-t", f"{TOPLAM / FPS:.3f}", cikti)
    else:
        ff("-i", sessiz, "-i", wav, "-af", "loudnorm=I=-16:TP=-1.5:LRA=11", "-c:v", "copy", "-c:a", "aac", "-b:a", "192k", "-shortest", cikti)
    kontrol_yaz(cikti, os.path.join(P, cikti_adi(TEMA, "kontrol").replace(".mp4", ".png")), TOPLAM, FPS,
                 efekt_kunyesi(EFEKT, len(olay), toplam_olay))
    print(f"tamam: {cikti}  {kare_say(cikti)} kare ({kare_say(cikti) / FPS:.1f} sn), {efekt_kunyesi(EFEKT, len(olay), toplam_olay)}")


if __name__ == "__main__":
    main(sys.argv)
