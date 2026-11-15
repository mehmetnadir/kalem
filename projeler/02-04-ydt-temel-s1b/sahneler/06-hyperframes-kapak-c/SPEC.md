# SPEC v2 — 02-04-ydt-temel-s1 · sahne 06-hyperframes-kapak-c (huni v2; HyperFrames, 1080×1920, tek kare, ses yok)

Yazan: şef (15.11.2026, istem V2-D06). Kod yazmaz; tasarım verir. K = `/home/sef/01dev/_worktrees/kalem-0204`.
Sahne dizini D = `K/projeler/02-04-ydt-temel-s1/sahneler/06-hyperframes-kapak-c/`. Paket P = `K/projeler/02-04-ydt-temel-s1/`.
Bağlayıcı: `/home/sef/01dev/dijital-anlatim/.claude/docs/huni-v2-standart.md` §1–§2, `P/BRIEF-S1.md` "Yerleşim" + "Kanal katmanı".
v1 SPEC yedeği: `~/Silinecekler/2026-11-15-huni-v2/02-04-ydt-temel-s1/sahneler/06-hyperframes-kapak-c/SPEC.md`.
İçerik v1 ile aynı (`I LIVE` / `I AM LIVING`, ev · figür · bavul, `kalıcı` / `geçici`). Değişen: kanal katmanı + künye satırı + v2 bantları.

## 1. Dosyalar

| Dosya | Durum | İş |
|---|---|---|
| `D/uret.py` | VAR (v1) | **YENİDEN YAZILACAK** (mutlak yol `/home/sef/01dev/_worktrees/kalem-0204/projeler/02-04-ydt-temel-s1/sahneler/06-hyperframes-kapak-c/uret.py`) |
| `D/yardim.py` | VAR, v2'ye çevrildi (sahne 01 v2 kopyası) | DOKUNMA; yalnız `import yardim as Y` |
| `D/cizim/ogretmen.json`, `D/cizim/luggage.svg` | VAR | salt oku |
| `D/calistir.sh`, `D/olay.py`, `D/zamanlar.json` | VAR | DOKUNMA |
| `D/nesneler.json` | uret.py yazar | §6 madde 4 |

Başka dosyaya dokunma. Silme yok. Test, render, snapshot, `calistir.sh`, git YOK.

## 2. Kalıp kaynakları (salt oku)

| Kalıp | Mutlak yol | Ne alınır |
|---|---|---|
| v1 kod tabanı (aynı sahne) | `~/Silinecekler/2026-11-15-huni-v2/02-04-ydt-temel-s1/sahneler/06-hyperframes-kapak-c/uret.py` (= şu anki `D/uret.py`) | dosya düzeni aynen: `zaman.json`/`zamanlar.json` doğrulaması (satır 19–33), `hesapla_s_ve_baslik`, `baslik_svg` (kontur, id'ler), `eskiz_svg` (figür, ev, bavul çizimi), `etiketler_svg`, `blok_kutulari`, `kesisim`, `kurallari_dogrula`, HTML kabuğu ve GSAP tek `set` çizelgesi, `__main__` |
| v2 künye ve sabitler | `D/yardim.py` | `Y.kunye_svg()` (argümansız; `<g id="kunye">` içinde `<g id="kanal">` logo `#logoimg` + `@ydspublishing`, `#ku-konu`, `#rz0`), `Y.HUD` (kenar 60, sagSinir 960, icerikBas 460, icerikSon 1380, kanal ve künye ölçüleri), `Y.rozet_konumu()` → `(x, w)`, `Y.KANAL_YAZI`, `Y.genislik` |
| v2 sabit kullanımı örneği | `K/projeler/02-04-ydt-temel-s1/sahneler/01-hyperframes-kapak/uret.py` satır 39–40, 96–99, 126–150 | `KENAR = Y.HUD["kenar"]`, `SAG = Y.HUD["sagSinir"]`, `Y.HUD["icerikBas"]` / `["icerikSon"]` assert biçimi |

## 3. Değişiklik listesi (v1 → v2)

1. uret.py'deki yerel `kunye_svg()` işlevi SİLİNİR; HTML'de `{kunye}` yerine `Y.kunye_svg()` çıktısı girer. uret.py logo, rozet, çip, ders adı YAZMAZ.
2. Sabitler: `KENAR = Y.HUD["kenar"]` (60) · `SAG = Y.HUD["sagSinir"]` (960) · `ICERIK_BAS = Y.HUD["icerikBas"]` (460) ·
   `ICERIK_SON = Y.HUD["icerikSon"]` (1380) · `ORTA = (KENAR + SAG) / 2` (510) · `BASLIK_GEN = 880` · `BASLIK_UST = 470` · `ZEMIN_Y = 1360`.
   v1 sabitleri `SAG = 1032`, `BASLIK_GEN = 952`, `ZEMIN_Y = 1344`, `PLATFORM = 1536`, `KENAR = 48` KALKAR.
3. Başlık, sahne, etiket konumları §4'teki değerlere geçer. Boy, kontur, renk, id ve çizim yöntemi v1 ile aynıdır.
4. Blok listesi ve assert'ler §6'ya göre güncellenir (`hud` bloğu yerine `kanal` + `kunye`).
5. Modül docstring'i: "Bantlar: kanal (280–350) → künye (360–450) → içerik (460–1380: başlık 470–779, sahne 880–1360) → alt boş (1570–1920)".

## 4. Yerleşim (y = yazı tabanı, px; x içerik bandı 60–960, orta 510)

```
y    0 ┌──────────────────────────────────────┐────────┐
       │ (boş zemin, çip YOK)                  │        │
   280 │ [logo] @ydspublishing                 │ sağ    │  Y.kunye_svg() → #kanal (x 60'tan)
   360 │ Simple Present vs Present Continuous (YDT · BASIC) │  #ku-konu + #rz0 (taban 420, hap 386–434)
   470 │   I LIVE                              │ 960–   │  Fredoka 700 S=160, x0 ≈ 72
   615 │   I [AM LIVING]                       │ 1080   │  kutu 616–779
   984 │  kalıcı                  geçici       │ boş    │  Caveat 700 88
  1090 │ ┌ev┐        fig        ┌bavul┐        │        │
  1360 │─┴──┴────────┴┴─────────┴─────┴────── │        │  zemin çizgisi
  1380 ├──────────────────────────────────────┤        │  içerik sonu
  1570 │ (boş)                                 │        │
```

### 4.1 Kanal + künye
`Y.kunye_svg()` çıktısı değiştirilmeden kullanılır. uret.py yalnız blok kutularını hesaplar (§6 madde 3).

### 4.2 Başlık — `<g id="baslik">` (v1 §4.2 aynen, yalnız şu değerler)
- `g(m) = Y.genislik("Fredoka", 700, m, S)`; `p = 0,08·S`; `gb = g("I AM LIVING") + p`.
- Boy: önce 100 ile ölç; `S = floor(min(190, BASLIK_GEN·100 / gb_100))`; `gb > BASLIK_GEN` iken S'yi 1 azalt. Beklenen S = 160, gb ≈ 875,7.
- `x0 = ORTA − gb/2` (≈ 72,2). İki satır aynı sol x (iki `I` alt alta).
- `T1 = BASLIK_UST + 0,75·S` (= 590); `T2 = T1 + 1,02·S` (≈ 753,2).
- Kutu `#bk-kutu`: sol `x0 + g("I ") − p`, sağ `x0 + g("I AM LIVING") + p`; üst `T2 − 0,86·S`, alt `T2 + 0,16·S` (≈ 778,8); rx `0,10·S`; `fill` vurgu.
- Kutu sol kenarı `> x0 + g("I") + 0,04·S` (kutu `I` harfine değmez).
- `bs-1` (`I LIVE`) ve `bs-2i` (`I`): `fill` murekkep + kontur (`stroke` zemin, 12, round, `style="font-kerning:none;paint-order:stroke fill"`).
  `bs-2v` (`AM LIVING`): `fill` zemin, kontursuz, `style="font-kerning:none"`. Sıra: bs-1, bk-kutu, bs-2i, bs-2v. `t2` id YOK.

### 4.3 Sahne — `<g id="eskiz" fill="none" stroke=murekkep stroke-linecap="round" stroke-linejoin="round">`
| Öğe | Ölçü |
|---|---|
| zemin çizgisi `<path id="zc">` | `M70 1360 L950 1360`, `stroke-width` 4 |
| ev `<g id="ev">` | `Y.tabler("home")`, `EV_S = 15`. Izgara (3, 21) → (80, 1360): `translate(80 − 3·15, 1360 − 21·15)` = `translate(35 1045) scale(15)`, `stroke-width = 4/15`. Ev kutusu x 80–350, y 1090–1360, orta x 215 |
| figür `<g id="fig">` | v1 ile aynı çizim (`cizim/ogretmen.json`, kalınlık `govde 4.4 · sac 3.6 · yuz 2.6` / fs). `FIG_H = 480`, `fs = FIG_H/(y1−y0)`, `fw = (x1−x0)·fs` (≈ 148,8), `FIG_X = ORTA − fw/2` (≈ 435,6), alt = `ZEMIN_Y`, üst = 880. Eli boş |
| bavul `<g id="bavul">` | `Y.tabler("luggage", AD / "cizim")`, `BV_S = 11`. Izgara (18, 21) → (876, 1360): `translate(876 − 18·11, 1360 − 21·11)` = `translate(678 1129) scale(11)`, `stroke-width = 4/11`. Bavul kutusu x 744–876, y 1162–1360, orta x 810. İç dolgu YOK |

Etiketler (`<text>`, eskiz grubunun DIŞINDA, `fill` murekkep, kontursuz, Caveat 700 88, `text-anchor="middle"`):
- `et-kalici` `kalıcı`: x 215 (ev ortası), taban 1050 (= ev üstü 1090 − 40).
- `et-gecici` `geçici`: x 810 (bavul ortası), taban 1122 (= bavul üstü 1162 − 40).
Konumlar sabit sayı değil, ev/bavul kutusundan türetilir (ev ortası, ev üstü − 40).

## 5. Tema (hf_tema.py ile uyum; v1 §5 aynen)
- `Y.ZEMIN_CSS`, `Y.zemin_html()`, `Y.font_css()` DEĞİŞTİRMEDEN kullan. Renkler yalnız `Y.RENK` anahtarları, SVG özniteliği, küçük harf hex.
- `bk-kutu` dolgusu `<rect fill="#f2a93b">` (açıkta `vurguDolgu #ffe066`); `AM LIVING` `<text fill="#1b1a17">` (açıkta `pilMetin #1b2440`).
- `<path fill="#1b1a17">` YOK. id `t2`, `ku-nokta`, `rz1` KULLANMA. Logo `#logoimg` `Y.kunye_svg()` içinde gelir.

## 6. Kurallar ve kabul ölçütü (uret.py içinde `assert`)
1. İçerik blokları (`baslik`, `bk-kutu`, `et-kalici`, `et-gecici`, `ev`, `fig`, `bavul`, `zc` = x 70–950, y 1358–1362):
   x ∈ [KENAR, SAG], y ∈ [ICERIK_BAS, ICERIK_SON]. Hiçbir blok y < 280, y > 1380, x > 960 değil.
2. Yazı boyu: başlık S ≥ 64, etiket 88 ≥ 72. Başlık 2 satır. Her satır ≤ 24 karakter (`I LIVE`, `I AM LIVING`, `kalıcı`, `geçici`).
3. Bloklar (yazı kutusu y_üst = taban − 0,75·boy; y_alt = taban + 0,30·boy Caveat, + 0,25·boy diğer):
   - `kanal`: x 60, y 280, w = `Y.HUD["kanalYaziX"] + Y.genislik("Lexend", 700, Y.KANAL_YAZI, 42) − 60`, h 70.
   - `kunye`: x 60, y 360, w = `rx + rw − 60` (`rx, rw = Y.rozet_konumu()`), h 90. `rx + rw ≤ 960` assert.
   - `baslik`: x0, `BASLIK_UST` → kutu altı; w gb. `bk-kutu`: kutu. `et-kalici`, `et-gecici`: Caveat genişliği ortalı. `ev`, `fig`, `bavul`: §4.3 kutuları.
   Çiftler arası kesişim 0: kanal, kunye, baslik, et-kalici, et-gecici, ev, fig, bavul (bk-kutu başlığın içinde, listeye girmez).
   `baslik` üstü ≥ ICERIK_BAS; `baslik` alt ile en üst sahne öğesi arası ≥ 48; ev–fig ve fig–bavul yatay ara ≥ 60; etiket alt ile kendi ikonu üstü arası ≥ 12;
   `ZEMIN_Y + 2 ≤ ICERIK_SON`.
4. `nesneler.json`: `[{"ad", "x", "y", "w", "h"}]` tam sayı; sıra: kanal, kunye, baslik, bk-kutu, et-kalici, et-gecici, ev, fig, bavul.
5. Yasak: emoji, kırmızı, yeşil, gradyan, gölge, `Math.random`, `Date`, try/catch, `opacity:0` başlangıç, hareket (tek `set` dışında tween yok).
6. Ekranda "Tam ders", "dakika", QR, "izle" sözü YOK (dosyada da bu sözcükler geçmez). Python: tür ipuçları bütün işlevlerde.
7. `/usr/bin/python3 uret.py` stdout'a `index.html yazıldı <bayt>` ve `S=<boy>` basar; hata yoksa çıkış 0.

Kabul (şef koşturur, ajan koşturmaz): `bash calistir.sh --tema acik|koyu` → `P/kapak-c.png` ve `D/k/koyu/kapak-c-koyu.png` 1080×1920;
kanal katmanı x 60'tan, y 280–350; künye y 360–450; içerik 460–1380 ve x ≤ 960; 0–280 ve 1570–1920 boş; taşma, kesik yazı, üst üste binme yok.
