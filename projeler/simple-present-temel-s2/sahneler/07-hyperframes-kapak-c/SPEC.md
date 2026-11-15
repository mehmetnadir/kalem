# SPEC — simple-present-temel-s2 · sahne 07-hyperframes-kapak-c (huni v2; HyperFrames, 1080×1920, tek kare, ses yok)

> DUZ2 (16.11): `SAT2 = "GÜÇLÜ İPUCU"` (S 140); karakter ana paketin kadın öğrencisi (sol el yukarı-sola işaret), ölçek 0,455; aramaya kutu kesişimi şartı (sart5) eklendi.

Yazan: şef (15.11.2026, istem D-V2). Kod yazmaz; tasarım verir. K = `/home/sef/01dev/_worktrees/kalem-0204`.
Sahne dizini D = `K/projeler/simple-present-temel-s2/sahneler/07-hyperframes-kapak-c/`. Paket P = `K/projeler/simple-present-temel-s2/`.
Bağlayıcı: `/home/sef/01dev/dijital-anlatim/.claude/docs/huni-v2-standart.md` §2, §6 · `kapak-standardi.md` §2 (krem çıkartma kenarı) ·
`P/BRIEF-S2.md` "Yerleşim", "Kanal katmanı", "Kapak" C.

## 1. Dosyalar

| Dosya | Durum | İş |
|---|---|---|
| `D/uret.py` | YOK | **YAZILACAK** — mutlak yol `/home/sef/01dev/_worktrees/kalem-0204/projeler/simple-present-temel-s2/sahneler/07-hyperframes-kapak-c/uret.py` |
| `D/yardim.py` | VAR (emsal 06 v2 kopyası, `KONU = "Simple Present"`) | DOKUNMA; yalnız `import yardim as Y` |
| `D/calistir.sh`, `D/olay.py`, `D/zamanlar.json` | VAR | DOKUNMA |
| `D/nesneler.json`, `D/proje/index.html`, `D/proje/assets/karakter.png`, `D/proje/assets/fonts/` | uret.py yazar | §6 |

Başka dosyaya dokunma. Silme yok. Test, render, snapshot, `calistir.sh`, git YOK.

## 2. Kalıp kaynakları (salt oku)

| Kalıp | Mutlak yol | Ne alınır |
|---|---|---|
| Kod düzeni (aynı rol) | `K/projeler/02-04-ydt-temel-s1/sahneler/06-hyperframes-kapak-c/uret.py` | dosya iskeleti aynen: `zaman.json` `duragan[]` ve `zamanlar.json` doğrulaması (satır 19–33; klasör adı `AD.name`, çıktı `kapak-c.png`), sabitler `Y.HUD`'dan, `baslik_svg` kontur biçimi, `blok_kutulari`, `kesisim`, `kurallari_dogrula`, HTML kabuğu, GSAP tek `set` çizelgesi, `__main__` (font kopyası, `nesneler.json`, stdout satırları) |
| Karakter + krem kenar | `K/projeler/02-04-ydt-temel-s1/sahneler/05-hyperframes-kapak-b/uret.py` | `alfa_kutusu`, `maske`, `bos_mu`, `gorsel_kopyala`, `gorsel_img` (satır 70–118) aynen; `.kenar` filtresi (satır 573–577) aynen; `<img>` yeri: `Y.zemin_html()`'den SONRA, `<svg id="sahne">`'den ÖNCE (satır 588–591) |
| Elle çizilmiş kart kenarı | `K/projeler/simple-present-temel-s2/sahneler/03-hyperframes-kaydet/uret.py` satır 80–108 `kart_kenar_yolu` | tek `M`, kenar başına 3 ara nokta, sabit `kay` kayma listesi, sol üstte bindirme, sınır assert'i; köşe değerleri §4.3 |
| Künye | `D/yardim.py` | `Y.kunye_svg()` (argümansız; `#kanal` = `#logoimg` + `#kanal-yazi`, `#ku-konu`, `#rz0`), `Y.HUD`, `Y.rozet_konumu()`, `Y.KANAL_YAZI`, `Y.genislik`, `Y.tabler`, `Y._font`, `Y.RENK`, `Y.font_css`, `Y.ZEMIN_CSS`, `Y.zemin_html`, `Y.font_kopyala` |

## 3. Sabitler

`KENAR = Y.HUD["kenar"]` (60) · `SAG = Y.HUD["sagSinir"]` (960) · `ICERIK_BAS = Y.HUD["icerikBas"]` (460) · `ICERIK_SON = Y.HUD["icerikSon"]` (1380) ·
`ORTA = 510` · `BAS_UST = 462` · `BAS_ALT = 800` · `BASLIK_GEN = 900` · `KONTUR = 12` ·
`KARAKTER = ORTAK / "kapak" / "karakter.png"` (`ORTAK = PAKET / "ortak"`; 896×1200 RGBA) · `ESIK = 64` · `KENAR_PX = 10` · `KENAR_GECIS = 3` · `PAY = 12` ·
`KAR_X0 = 620` · `KAR_SAG = 948` (görünür sağ; kenarla 958).
`R = Y.RENK`; `KREM = R["murekkep"]` (yalnız `.kenar` CSS filtresinde).

## 4. Yerleşim (y = yazı tabanı, px; içerik x 60–960)

```
y    0 ┌───────────────────────────────────────────┐───────┐
       │ (boş zemin, çip YOK)                       │       │
   280 │ [logo] @ydspublishing                      │ sağ   │  Y.kunye_svg() → #kanal
   360 │ Simple Present  (YDT · TEMEL)              │ 960–  │  #ku-konu + #rz0
   462 │        ÜÇ İFADE,                           │ 1080  │  başlık S = 143, ortalı (orta 510)
   ≈767│     TEK İŞARET                             │ boş   │  alt ≈ 799
   830 │ ┌──────────────────────┐                   │       │  kart 64–596 × 832–1148
   912 │ │ usually        [takv]│      ┌karakter┐   │       │  Fredoka 72
  1008 │ │ always               │      │  (sola │   │       │
  1104 │ │ every day            │  ◄───┤ işaret)│   │       │  parmak ucu y ≈ 1122
  1150 │ └──────────────────────┘      │        │   │       │
  1162 │        ↓ (kalem oku)          └────────┘   │       │  karakter görünür alt ≈ 1309
  1268 │ (  Simple Present  ) ← sarı hap            │       │  hap 60–660 × 1268–1372
  1380 ├────────────────────────────────────────────┤       │
  1400 │ (boş: altyazı yok)                          │       │
```

### 4.1 Kanal + künye
`Y.kunye_svg()` çıktısı değiştirilmeden girer. uret.py logo, rozet, çip, konu adı YAZMAZ.

### 4.2 Başlık — `<g id="baslik">` (mürekkep, hapsız, iki satır aynı boy)
- Satırlar: `SAT1 = "ÜÇ İFADE,"`, `SAT2 = "TEK İŞARET"` (Ü, Ç, İ, Ş tam bu karakterler; ASCII yedek yok).
- Glif sınırı: `glif_sinir(metin) -> (ust, alt)` = metindeki her karakterin Fredoka 700 glif kutusunun en büyük `yMax`'ı ve en küçük `yMin`'i
  (em oranı). Glif `Y._font("Fredoka", 700, "latin")`, yoksa `"latin-ext"`; kutu `fontTools.pens.boundsPen.BoundsPen` ile ölçülür.
  Beklenen: SAT1 (0,928, −0,182) · SAT2 (0,921, −0,182).
- `U1, A1 = glif_sinir(SAT1)`, `U2, A2 = glif_sinir(SAT2)`. `ARA = (−A1 + U2 + 0,06)` (satır aralığı, em).
- Boy: `S` 190'dan aşağı 1'er azalır; ilk geçen değer alınır. Şart (a) `max(g(SAT1), g(SAT2)) + KONTUR ≤ BASLIK_GEN`
  (`g(m) = Y.genislik("Fredoka", 700, m, S)`); şart (b) `(U1 + ARA − A2)·S + KONTUR ≤ BAS_ALT − BAS_UST`. Beklenen `S = 143`.
- `T1 = BAS_UST + KONTUR/2 + U1·S` (≈ 600,7) · `T2 = T1 + ARA·S` (≈ 767,0) · `baslik_alt = T2 − A2·S + KONTUR/2` (≈ 799,0; ≤ 800 assert).
- Her satır ortalı: `x = ORTA − g(satır)/2`.
- `bs-1`, `bs-2`: `<text>` Fredoka 700 `font-size=S`, `fill` murekkep, `stroke` zemin, `stroke-width` 12, `stroke-linejoin="round"`,
  `style="font-kerning:none;paint-order:stroke fill"` (emsal 06 `bs-1` biçimi). Sarı kutu YOK, `t2` id YOK.

### 4.3 Kart — `<g id="kart">` (solda, x 60–600)
- Kâğıt: `<rect id="kagit" x="66" y="834" width="528" height="312" rx="18" fill="#f3efe6" fill-opacity="0.06"/>` (hf_tema `murekkep`e çevirir;
  iki temada zeminden hafif ayrışır).
- Kalem kenarı: `<path id="kart-kenar">`, `fill="none"`, `stroke` murekkep, `stroke-width` 4.5, round. Yol `kart_kenar_yolu()`: 03-kaydet
  kalıbı; köşeler sol 64, sağ 596, üst 832, alt 1148; ara noktalar kenarın 1/4, 1/2, 3/4'ünde; kayma listesi aynı
  `[1.6, -1.2, 2.2, -0.8, 1.0, -2.0, 0.6, 1.8, -1.4, 0.4, -2.2, 1.2]`; bindirme: son nokta (88, 832). Assert: her nokta x ∈ [62, 598], y ∈ [830, 1150].
- Satırlar (`<text>`, Fredoka 700 72, `fill` murekkep, kontursuz, `style="font-kerning:none"`, x 100):
  `k-1` `usually` taban 912 · `k-2` `always` taban 1008 · `k-3` `every day` taban 1104.
- Takvim: `<g id="takvim" transform="translate(476 846) scale(4)" fill="none" stroke=murekkep stroke-width="1" stroke-linecap="round"
  stroke-linejoin="round">` + `Y.tabler("calendar")` yolları (yerel `ortak/cizim/tabler/calendar.svg`). Kutu (çizgi dahil) x 490–558, y 856–932.
- Kart içi kurallar: satır kutuları (x 100 … 100 + genişlik; y taban − 0,75·72 … taban + 0,25·72) ve takvim kutusu kart iç kenarından
  (64, 832, 596, 1148) en az 24 px içeride; satırlar ile takvim kesişmez.

### 4.4 Kalem oku — `<g id="ok" fill="none" stroke=murekkep stroke-width="5" stroke-linecap="round" stroke-linejoin="round">`
- Gövde `<path d="M 316 1162 C 296 1192, 330 1212, 330 1252"/>`, uç `<path d="M 313 1235 L 330 1253 L 347 1235"/>`.
- Kutu (çizgi dahil) x 294–350, y 1159–1256. Kart altı ile ok başı arası ≥ 8; ok ucu ile hap üstü arası ≥ 8.

### 4.5 Sarı hap — `<g id="hap">` (karenin tek sarısı)
- `gh = Y.genislik("Fredoka", 700, "Simple Present", 80)` (≈ 540,4). `<rect x="60" y="1268" width="gh + 60" height="104" rx="52" fill=vurgu>`
  (`R["vurgu"]` `#f2a93b`; açık temada hf_tema `vurguDolgu #ffe066` verir).
- `<text>` `Simple Present`: x = 60 + (gh + 60)/2, `text-anchor="middle"`, taban 1340, Fredoka 700 80, `fill` zemin (`R["zemin"]` `#1b1a17`;
  açıkta `pilMetin #1b2440`), kontursuz.
- Assert: hap sağ kenarı ≤ SAG; hap alt ≤ ICERIK_SON.

### 4.6 Karakter — HTML `<img id="karakter" class="abs kenar">` (SVG dışı; sağda, karta işaret eder)
- `gorsel_kopyala(AD / "proje" / "assets")` (05 kalıbı). `ax0, ay0, ax1, ay1 = alfa_kutusu(KARAKTER)` (ölçüm 152, 89, 744, 1113).
- Parmak ucu: `PARMAK_Y` = alfa maskesinde (eşik ESIK) `ax0` sütunundaki dolu satırların ortalaması (ölçüm ≈ 710).
- Ölçek araması: `s` 0,540'tan 0,300'e 0,005 adımla iner (her adımda `round(s, 3)`); ilk geçen `s` alınır. Her `s` için:
  `kx = KAR_SAG − ax1·s` · `ky = KUST − ay0·s` (`KUST = baslik_alt + 24 + KENAR_PX`) · `m = maske(KARAKTER, kx, ky, s)`. Şartlar:
  1. `ky + ay1·s + KENAR_PX ≤ ICERIK_SON`;
  2. `kx + ax0·s − KENAR_PX ≥ KAR_X0`;
  3. `bos_mu(m, kutu, KENAR_PX + PAY)` hap, ok ve kart kutusu (x 62–598, y 830–1150) için;
  4. parmak `ky + PARMAK_Y·s` ∈ [kart üst 832 + 24, kart alt 1148 − 24].
  Hiçbir `s` geçmezse `AssertionError`. Beklenen (ölçüm): `s = 0,465`, `kx ≈ 602`, `ky ≈ 791,6`, görünür kutu x 672,7–948, y 833–1309, parmak y ≈ 1122.
- `gorsel_img(kx, ky, s)` ile yazılır. `.kenar` filtresi: `KENAR_GECIS` × 4 yön `drop-shadow`, adım `KENAR_PX / KENAR_GECIS`, renk `KREM` (05 satır 573–577).
  Krem daire YOK. Görsel iki temada aynı dosya.

### 4.7 HTML
05 ve 06 kabuğu: `<style>` = `Y.font_css()` + `Y.ZEMIN_CSS` + `#sahne{position:absolute;left:0;top:0;}` + `.kenar{filter:…}`.
Gövde sırası: `Y.zemin_html()` → `<img id="karakter">` → `<svg id="sahne" …>` (kunye, baslik, kart, ok, hap). GSAP: emsal 06'daki iki
`tl.set("#sahne", {opacity: 1, immediateRender: false})` (0 ve `Z['sure']`), `window.__timelines["main"]`. Başka tween yok.

## 5. Tema (hf_tema.py ile uyum)
- Renkler yalnız `Y.RENK` değerleri, SVG özniteliği, küçük harf hex: murekkep `#f3efe6`, zemin `#1b1a17`, vurgu `#f2a93b`.
- Sarı yalnız hap `<rect>`'inde. `<path fill="#1b1a17">` YOK. id `t2`, `ku-nokta`, `rz1` KULLANMA.
- CSS'e `#root.tema-acik` dizgesi YAZILMAZ (hf_tema onu "çevrildi" sayar, açık tema koyu çıkar; sözleşme).

## 6. Kurallar ve kabul ölçütü (uret.py içinde `assert`)
1. Bloklar (x, y, w, h): `kanal` (x 60, y 280, w = `Y.HUD["kanalYaziX"] + Y.genislik("Lexend", 700, Y.KANAL_YAZI, 42) − 60`, h 70) ·
   `kunye` (x 60, y 360, w = `rx + rw − 60`, h 90; `rx + rw ≤ 960`) · `baslik` (iki satırın birleşik kutusu ± KONTUR/2; y `BAS_UST` … `baslik_alt`) ·
   `kart` (62, 830, 536, 320) · `takvim` (490, 856, 68, 76) · `ok` (294, 1159, 56, 97) · `hap` (60, 1268, gh + 60, 104) ·
   `karakter` (görünür kutu ± KENAR_PX).
2. İçerik blokları (kanal, kunye dışı): x ∈ [KENAR − 2, SAG], y ∈ [ICERIK_BAS, ICERIK_SON]. Hiçbir blok y < 280, y > 1380, x > 960 değil.
3. Kesişim 0: `kanal`, `kunye`, `baslik`, `kart`, `ok`, `hap`, `karakter` çiftleri (takvim kartın içinde, listeye girmez). `baslik` alt ile
   `kart` ve `karakter` üstü arası ≥ 24 (karşılaştırmalarda 1e-6 tolerans; karakter üstü tanım gereği tam 24). Karakter–hap/ok/kart ayrımı
   maskeyle (§4.6 şart 3).
4. Yazı boyu ≥ 64 (kanal 42 ve künye ≤ 34 / 26 hariç): başlık S, kart 72, hap 80. Başlık 2 satır, toplam 4 sözcük. Her satır ≤ 24 karakter.
5. `nesneler.json`: `[{"ad", "x", "y", "w", "h"}]` tam sayı; sıra kanal, kunye, baslik, kart, takvim, ok, hap, karakter.
6. Yasak: emoji, kırmızı, yeşil, yeni gradyan, gölge (krem `drop-shadow` kenarı dışında), `Math.random`, `Date`, try/catch, `opacity:0` başlangıç,
   tween. Standart §1 kural 4–5'teki sözler, QR ve "izle" sözü ekranda YOK; bu sözler koda liste olarak da YAZILMAZ (dış tarama komutunu
   kirletir; denetim dış grep'te). Python: bütün işlevlerde tür ipucu.
7. `/usr/bin/python3 uret.py` stdout'a `index.html yazıldı <bayt>`, `S=<boy>`, `s=<ölçek>` basar; hata yoksa çıkış 0.

Kabul (şef koşturur, ajan koşturmaz): `bash calistir.sh --tema acik|koyu` → `P/kapak-c.png` ve `D/k/koyu/kapak-c-koyu.png` 1080×1920;
kanal katmanı x 60'tan, y 280–350; künye y 360–450; içerik 460–1380 ve x ≤ 960; 0–280 ve 1400–1920 boş; taşma, kesik yazı, üst üste binme yok.
