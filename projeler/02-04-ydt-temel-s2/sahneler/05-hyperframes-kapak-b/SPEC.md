# SPEC v2 (huni v2) — 02-04-ydt-temel-s2 · sahne 05-hyperframes-kapak-b (HyperFrames, 1080×1920, tek kare, ses yok)

Yazan: şef (15.11.2026, istem D-S2-V2). Kod yazmaz; tasarım verir. K = `/home/sef/01dev/_worktrees/kalem-0204`.
Sahne dizini D = `K/projeler/02-04-ydt-temel-s2/sahneler/05-hyperframes-kapak-b/`. Paket P = `K/projeler/02-04-ydt-temel-s2/`.
Bağlayıcı: `/home/sef/01dev/dijital-anlatim/.claude/docs/huni-v2-standart.md` §1–§2, §6 · `P/BRIEF-S2.md` "Yerleşim" ve "Kapak B" B sütunu.
v1 SPEC/RAPOR/uret.py yedeği: `~/Silinecekler/2026-11-15-huni-v2/02-04-ydt-temel-s2/sahneler/05-hyperframes-kapak-b/`.
Kapak B = soru kapağı. Cevap karede YOK (zaman adı, `wears`, `is wearing` yazılmaz). v1'deki çizilmiş öğretmen figürü, zemin çizgisi,
v1 HUD (logo y 48, rozet y 216) KALKAR; yerine kapak görseli (`karakter.png`) ve v2 kanal katmanı + künye gelir.

## 1. Dosyalar

| Dosya | Durum | İş |
|---|---|---|
| `D/uret.py` | VAR (v1) | **BAŞTAN YAZILACAK** — mutlak yol `/home/sef/01dev/_worktrees/kalem-0204/projeler/02-04-ydt-temel-s2/sahneler/05-hyperframes-kapak-b/uret.py` |
| `D/yardim.py` | VAR (şef v2'ye çekti: `HUD`, `konu_boyu`, `rozet_konumu`, `kunye_svg`) | DOKUNMA; `import yardim as Y` |
| `D/cizim/question-mark.svg` | VAR | salt oku (`Y.tabler("question-mark", AD / "cizim")`) |
| `P/ortak/cizim/tabler/calendar.svg` | VAR | salt oku (`Y.tabler("calendar")`) |
| `P/ortak/kapak/karakter.png` | VAR (896×1200 RGBA) | salt oku (PIL); `calistir.sh` bunu `D/proje/assets/karakter.png`'ye kopyalar |
| `D/calistir.sh`, `D/olay.py`, `D/zamanlar.json` | VAR (şef) | DOKUNMA |
| `D/nesneler.json` | uret.py yazar | §6 madde 6 |

Başka dosyaya dokunma. Silme yok. Test, render, snapshot, `calistir.sh`, git YOK. `D/cizim/ogretmen-dusunen.json` artık OKUNMAZ.

## 2. Kalıp kaynakları (salt oku)

| Kalıp | Mutlak yol | Ne alınır |
|---|---|---|
| İskelet (aynı sahne v1) | yedek: `/home/sef/Silinecekler/2026-11-15-huni-v2/02-04-ydt-temel-s2/sahneler/05-hyperframes-kapak-b/uret.py` | dosya düzeni; `zaman.json` + `zamanlar.json` doğrulaması (AYNEN); `hesapla_s()` döngüsü (önce 100 ile ölç, sonra 1'er küçült); başlık `<text>` konturu (`fill` mürekkep, `stroke` zemin, `stroke-width="12"`, `stroke-linejoin="round"`, `style="font-kerning:none;paint-order:stroke fill"`, `xml:space="preserve"`); takvim yolları (ilk 4 yol, başlarını assert et) + `today` yazısı; soru işareti 2 yolu; `kesisim()`; HTML kabuğu (`Y.font_css()`, `Y.ZEMIN_CSS`, `Y.zemin_html()`, `#root data-…`, `lib/gsap.min.js`, iki `tl.set`, `window.__timelines["main"]`); `__main__` (`proje/`, `Y.font_kopyala`, `proje/index.html`, `nesneler.json`, stdout) |
| Çıkartma kenarı + krem daire + `<img>` | `/home/sef/01dev/_worktrees/kalem-0204/projeler/02-04-ydt-temel-dikey/sahneler/90-hyperframes-kapak/uret.py` | `alfa_kutusu()`, `maske()`, `bos_mu()`, `maske_kutusu()`, `daire_kutu_uzakligi()` (satır 65–99, ESIK 64); `gorsel_img()` (satır 282–287, `<img class="abs kenar">`); `kenar` filtre dizisi (satır 296–298: `KENAR_GECIS = 3` geçiş × 4 yön, adım 10/3 px, renk krem); `<svg id="alt">` + `<circle id="daire">` deseni. Oradaki renk/tema CSS'i ALINMAZ (bizim tema `ortak/hf_tema.py`) |

## 3. Okuma ve sabitler

- `PAKET = AD.parent.parent`. `zaman.json`: `duragan` içinde `klasor == AD.name` TEK kayıt; `kare == 1`, `cikti == "kapak-b.png"`;
  `sahneler[]` içinde `AD.name` YOK. `zamanlar.json`: `sure` 1,0 · `kare` 1 · `fps` 30 (v1 assert'leri AYNEN).
- Anlatım, sözcük, altyazı dosyası OKUNMAZ (ses yok).
- SVG renkleri yalnız `Y.RENK`: `zemin #1b1a17`, `murekkep #f3efe6`, `vurgu #f2a93b`. CSS'te yalnız krem `#f3efe6` (kenar + daire).
- Sabitler: `KENAR_X = 60`, `SAG = 960`, `ICERIK_UST = 460`, `ICERIK_ALT = 1380`, `BASLIK_ALT = 800`, `SAHNE_UST = 820`,
  `BASLIK_GEN = 900`, `S_UST = 190`, `KENAR_PX = 10`, `KENAR_GECIS = 3`, `ESIK = 64`, `PAY = 16`.

## 4. Yerleşim (px; y = yazı tabanı)

```
y    0 ┌──────────────────────────────────────────┐ 0–280 yalnız zemin
   291 │ [logo 193,5×48] @ydspublishing           │ kanal katmanı 280–350 (Y.kunye_svg)
   420 │ Simple Present vs Present Continuous (YDT · BASIC) │ künye 360–450 (Y.kunye_svg)
 598,8 │ TODAY VARSA                               │ Fredoka 700 S=125, sola yaslı x 60
 756,3 │ HANGİ ZAMAN?                              │ (İ noktalı), en geniş satır 899,9 ≤ 900
  ≈845 │            ┌○────○┐                      │ takvim yaprağı (+4°), x 490–690
       │  ( daire ) │today │        ╭─╮           │ büyük ? (vurgu), x 740–950, y 900–1248
       │  karakter  └──────┘          │           │
       │  \o/ avuçlar açık            •           │
  1370 │  karakter alt kenarı (görünür)            │ içerik 1380'de biter
  1400 ├──────────────────────────────────────────┤ 1400–1920 BOŞ (altyazı yok, ses yok)
```
Sağ 960–1080 platform arayüzü altında: hiçbir öğe x 960'ı geçmez.

### 4.1 Kanal katmanı + künye
`Y.kunye_svg()` çıktısı AYNEN `<svg id="sahne">` içinde İLK öğe. Kendi künye/logo/rozet kodunu YAZMA. Çıktı yapısı:
`<g id="kunye"><g id="kanal"><image id="logoimg" …/><text id="kanal-yazi" …>@ydspublishing</text></g><text id="ku-konu" …/><g id="rz0">…</g></g>`.
Kanal katmanı hiçbir tween'e girmez: zaman çizelgesi yalnız `#baslik`'i hedefler (§5).

### 4.2 Başlık — `<g id="baslik">` (hapsız, tek renk mürekkep)
- `<text id="bs-1">TODAY VARSA</text>`, `<text id="bs-2">HANGİ ZAMAN?</text>` (`İ` = U+0130). Fredoka 700, AYNI boy `S`.
- `S = floor(min(S_UST, BASLIK_GEN·100/g1_100, BASLIK_GEN·100/g2_100))`; S ile yeniden ölç; `g1 ≤ 900` ve `g2 ≤ 900` olana dek 1 azalt.
  Beklenen S = 125 (g1 ≈ 862,0 · g2 ≈ 899,9).
- Taban: `T1 = 630 − 0,25·S`, `T2 = T1 + 1,26·S` (blok 460–800 bandının ortası 630). Beklenen T1 = 598,75 · T2 = 756,25.
- Yatay: iki satır SOLA yaslı, `x = KENAR_X = 60` (künye ile aynı sol kenar; `text-anchor` YOK).
- Blok kutusu: x 60 → 60 + max(g1, g2); y `T1 − 0,86·S` → `T2 + 0,10·S` (≈ 491,3 → 768,8).

### 4.3 Karakter (kapak görseli) — HTML `<img id="karakter" class="abs kenar" src="assets/karakter.png" alt="">`
- `KS = 0,56` (sabit). Alfa kutusu (ESIK 64) `(ax0, ay0, ax1, ay1)` = PIL'den ölçülür (beklenen 21, 173, 878, 1112; assert ±2).
- Görünür sol kenar x 70 (= 60 + KENAR_PX), görünür alt kenar y 1370 (= 1380 − KENAR_PX):
  `X0 = 70 − ax0·KS`, `Y0 = 1370 − ay1·KS`; `<img>` stili `left:X0px;top:Y0px;width:896·KSpx;height:1200·KSpx` (1 ondalık).
  Beklenen X0 ≈ 58,2 · Y0 ≈ 747,3; görünür kutu ≈ x 70–549,9 · y 844,2–1370.
- `karakter` bloğu = görünür kutu her yana +KENAR_PX (≈ x 60–559,9 · y 834,2–1380).
- Maske: `maske(KARAKTER, X0, Y0, KS)` (1080×1920 bool). Çakışma denetimleri bu maskeyle yapılır (§6.3).
- Çıkartma kenarı CSS: `.kenar{filter: <12 drop-shadow>}`; dizi 90-kapak satır 296–298 ile aynı biçim, renk `#f3efe6`
  (iki temada da krem; CSS dizesi olduğu için hf_tema dokunmaz).
- Yüz ortası (dosya px) `YUZ_PNG = (461, 470)` → ekran `F = (X0 + 461·KS, Y0 + 470·KS)` (≈ 316,4 · 1010,5).

### 4.4 Krem daire (yalnız açık tema) — `<svg id="alt" class="abs" width="1080" height="1920" viewBox="0 0 1080 1920">`
- `<circle id="daire" cx cy r/>` — `fill` ÖZNİTELİĞİ YOK (hf_tema `[fill="#f3efe6"]` kuralı onu mürekkebe çevirirdi).
- Merkez `F`. `r = floor(min(0,36·(ay1 − ay0)·KS, uzaklık(F, takvim bloğu) − PAY, F.y − SAHNE_UST, uzaklık(F, başlık bloğu) − PAY))`.
  Beklenen r ≈ 147 (takvim sınırlar).
- CSS: `#daire{fill:#f3efe6;display:none;}` ve `.tema-acik #daire{display:inline;}`.
  **DİKKAT:** CSS'te `#root.tema-acik` dizesi GEÇMEZ: `hf_tema.py` bu dize varsa tema CSS'ini hiç eklemez (satır 49).
- z sırası: zemin → `#alt` (daire) → `<img id="karakter">` → `<svg id="sahne">`.

### 4.5 Takvim yaprağı — `<g id="takvim" transform="rotate(4 TCx TCy) translate(Ox Oy) scale(k)" fill="none" stroke=murekkep stroke-width="{6/k}" stroke-linecap="round" stroke-linejoin="round">`
- `Y.tabler("calendar")` ilk 4 yolu: `M4 7a2…` (sayfa), `M16 3v4`, `M8 3v4` (halkalar), `M4 11h16` (başlık çizgisi); 5. ve 6. yol (rakam) YOK.
- `TK = 200`, `k = TK / 16 = 12,5`. Döndürülmemiş sayfa x `490 → 690`, y `870 → 1070`; `Ox = 490 − 4k`, `Oy = 870 − 5k`.
  Dönme merkezi sayfa ortası `TC = (590, 970)`, saat yönünde 4°.
- `takvim` bloğu = 6 noktanın TC etrafında +4° döndürülmüş sınır kutusu, her yana +3 px: sayfa 4 köşesi + halka üstleri
  `(Ox + 8k, Oy + 3k)`, `(Ox + 16k, Oy + 3k)`. Beklenen ≈ x 480–700 · y 836–1080.

### 4.6 Takvim yazısı — `<g id="tk-yazi-g" transform="rotate(4 TCx TCy)"><text id="tk-yazi" …>today</text></g>`
- Caveat 700, `fill` mürekkep, kontursuz, `text-anchor="middle"`, küçük harf `today`.
- `TT = min(100, floor((TK − 56)·100 / Y.genislik("Caveat", 700, "today", 100)))`; beklenen TT = 76; `TT ≥ 64` assert.
  (Şef 1. düzeltme turu: TK − 32 ile TT 89'da `y` sağ kenara ≈ 12 px, kuyruk alt kenara ≈ 10 px yaklaştı.)
- x = `590 − 0,09·TT` (Caveat mürekkebi ilerleme kutusundan sağa kayar); taban = `(Hy + 1070) / 2 + 0,30·TT`, `Hy = Oy + 11k`.
- `takvim-yazi` bloğu = (590 ± w/2, taban − 0,75·TT → taban + 0,30·TT) kutusunun 4 köşesinin TC etrafında +4° döndürülmüş sınırı;
  tamamen `takvim` bloğu içinde olmalı.

### 4.7 Soru işareti — `<g id="soru" transform="translate(QX QY) scale(q)" fill="none" stroke=vurgu stroke-width="{26/q}" stroke-linecap="round" stroke-linejoin="round">`
- `Y.tabler("question-mark", AD / "cizim")` 2 yolu (kıvrım `M8 8a3.5 3…` + nokta `M12 19l0 .01`); ızgara x 8→16, y 5→19.
- `q = 23`. Sağ kenar 950: `QX = 950 − 13 − 16q`; üst 900: `QY = 900 + 13 − 5q`.
- `soru` bloğu: x `8q + QX − 13` → `16q + QX + 13`, y `5q + QY − 13` → `19q + QY + 13` (≈ x 740–950 · y 900–1248).
- TEK vurgu bu `?`'dir (açıkta hf_tema vurgu çizgisi `#d9900f`). Rozet hapı künye öğesidir, vurgu sayılmaz. Başka vurgu YOK.

## 5. HTML kabuğu ve tema

```
<style> Y.font_css() · Y.ZEMIN_CSS · #sahne,#alt{position:absolute;left:0;top:0;} · .kenar{filter:…} ·
        #daire{fill:#f3efe6;display:none;} · .tema-acik #daire{display:inline;} </style>
<div id="root" data-composition-id="main" data-start="0" data-duration="1.0" data-fps="30" data-width="1080" data-height="1920">
  Y.zemin_html() · <svg id="alt">daire</svg> · <img id="karakter"> · <svg id="sahne">künye · başlık · takvim · tk-yazi-g · soru</svg>
</div>
<script src="lib/gsap.min.js"></script>
<script> tl = gsap.timeline({paused:true}); tl.set("#baslik",{opacity:1,immediateRender:false},0);
         tl.set("#baslik",{opacity:1,immediateRender:false},1.0); window.__timelines["main"] = tl; </script>
```
- `Y.ZEMIN_CSS` ve `Y.zemin_html()` DEĞİŞTİRMEDEN (hf_tema birebir dize arar). Başka renk CSS kuralı YOK.
- Renkler SVG özniteliği, küçük harf hex: mürekkep `fill/stroke="#f3efe6"`, vurgu `stroke="#f2a93b"`, başlık konturu `stroke="#1b1a17"`.

## 6. Kurallar ve kabul ölçütü (uret.py içinde `assert`)
1. Bloklar (nesneler sırası): `kanal` (x 53, y 291, w = 263 + Y.genislik("Lexend",700,"@ydspublishing",42) − 53, h 50) ·
   `kunye` (x 60, y 386, w = rozet sağ kenarı − 60, h 48; rozet = `Y.rozet_konumu()`) · `baslik` · `karakter` · `daire`
   (cx−r, cy−r, 2r, 2r) · `takvim` · `takvim-yazi` · `soru`.
2. Sınırlar: `kanal` y ∈ [280, 350]; `kunye` y ∈ [360, 450] ve sağ kenar ≤ 960; `baslik` y ∈ [460, 800];
   `karakter`, `daire`, `takvim`, `soru` y ∈ [820, 1380]; bütün bloklar x ∈ [53, 960] (kanal hariç hepsi x ≥ 60);
   hiçbir blok y + h > 1380 değil (1400–1920 boş).
3. Çakışma: `[kanal, kunye, baslik, takvim, soru]` çiftlerinin kesişimi 0; `karakter`–`baslik` 0; `karakter`–`soru` 0;
   `bos_mu(maske, takvim, KENAR_PX + PAY)` ve `bos_mu(maske, soru, KENAR_PX + PAY)` ve `bos_mu(maske, baslik, KENAR_PX + PAY)` doğru;
   `daire`–(`takvim`, `baslik`, `soru`) uzaklık ≥ PAY (`daire_kutu_uzakligi ≥ r + PAY`).
   Boşluk: `soru.x − takvim.sağ ≥ 32`; `min(takvim.y, soru.y, karakter.y) − baslik.alt ≥ 48`;
   satır 1 alt (`T1 + 0,25·S`) < satır 2 `İ` noktası üstü (`T2 − 0,94·S`).
4. Yazı boyu: `S ≥ 64`, `S ≤ 190`, `TT ≥ 64` (kanal 42, konu ve rozet 26 künye öğesidir, hariç). İçerik satırları
   `["TODAY VARSA", "HANGİ ZAMAN?", "today"]` her biri ≤ 24 karakter; başlık 2 satır, toplam 4 sözcük; `"HANGİ"` içinde U+0130.
5. Yapı: `'<g id="kanal">'` html'de TAM 1 kez ve `'<g id="kunye">'` içinde; `id="logoimg"` 1 kez; `@ydspublishing` 1 kez;
   GSAP hedefi yalnız `#baslik` (html'de `tl.set("#sahne"` ve `"#kanal"` GEÇMEZ); `#root.tema-acik` dizesi GEÇMEZ;
   `<circle` yalnız 1 kez ve `fill=` özniteliği yok; `src="assets/karakter.png"` 1 kez.
6. `nesneler.json`: `[{"ad","x","y","w","h"}]` tam sayı (round); madde 1 sırası.
7. Hex beyaz listesi: `re.findall(r"#[0-9a-fA-F]{6}\b", html)` kümesi ⊆ {`#1b1a17`, `#f3efe6`, `#c9c2b3`, `#f2a93b`}.
8. Yasak (html küçük harfte): `tam ders`, `dakika`, ` dk`, `qr`, `izle`, `oynat`, `wears`, `is wearing`, `şimdiki`, `geniş`,
   `math.random`, `date.now`, `new date`, `opacity:0`, `try`, `catch`. Emoji yok
   (`re.search(r"[\U0001F000-\U0001FAFF☀-➿]", html)` boş). Kırmızı, yeşil, gradyan (zemin vinyeti hariç) YOK.
9. Python: bütün işlevlerde tür ipuçları; `from __future__ import annotations`; `PIL` + `numpy` kullanılır.
   `/usr/bin/python3 uret.py` stdout'a `index.html yazıldı <bayt>` ve `S=<S> TT=<TT> KS=<KS> r=<r> X0=<X0:.1f> Y0=<Y0:.1f>` basar; hata yoksa çıkış 0.

Kabul (şef koşturur, ajan koşturmaz): `ONIZLE_YALNIZ=1 bash calistir.sh` → "önizleme hazır"; `bash calistir.sh --tema acik|koyu` →
`P/kapak-b.png` ve `D/k/koyu/kapak-b-koyu.png` 1080×1920; kanal katmanı iki karede yerinde; taşma, kesik yazı, üst üste binme yok.
