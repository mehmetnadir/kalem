# SPEC — 02-04-ydt-temel-s3 · sahne 06-hyperframes-kapak-c (HyperFrames, 1080×1920, tek kare, ses yok)

Yazan: şef (15.11.2026, istem D-S3). Kod yazmaz; tasarım verir. K = `/home/sef/01dev/_worktrees/kalem-0204`.
Sahne dizini D = `K/projeler/02-04-ydt-temel-s3/sahneler/06-hyperframes-kapak-c/`. Paket P = `K/projeler/02-04-ydt-temel-s3/`.
Kaynak: `P/BRIEF-S3.md` "Kapak B ve C" (C satırı), `P/uretim-tutanagi/kapak-taslak.md` §1–§3 (C), `P/uretim-tutanagi/S3-duzeltme.md`
madde 1 ve 5. Kapak C = karşıt çift: başlık `İKİ ÖRNEK` / `İKİ ZAMAN`, iki kart `The train leaves …` / `I am going …`.

## 1. Dosyalar

| Dosya | Durum | İş |
|---|---|---|
| `D/uret.py` | YOK | **YAZILACAK** — mutlak yol `/home/sef/01dev/_worktrees/kalem-0204/projeler/02-04-ydt-temel-s3/sahneler/06-hyperframes-kapak-c/uret.py` |
| `D/yardim.py` | VAR (S1 kapak C kopyası) | DOKUNMA; yalnız `import yardim as Y` (`Y.genislik`, `Y.font_css`, `Y.font_kopyala`, `Y.ZEMIN_CSS`, `Y.zemin_html`, `Y.RENK`, `Y.LOGO_EN_BOY`, `Y.W`, `Y.H`) |
| `D/cizim/ogretmen.json` | VAR | salt oku (`kutu`, `yollar[].d`, `yollar[].parca`) |
| `D/calistir.sh`, `D/olay.py`, `D/zamanlar.json` | VAR (şef) | DOKUNMA |
| `D/nesneler.json` | uret.py yazar | §6 |

Başka dosyaya dokunma. Silme yok. Test, render, snapshot, `calistir.sh`, git YOK. `P/ortak/`, `P/zaman.json`, başka sahneler salt okunur.

## 2. Kalıp kaynakları (salt oku)

| Kalıp | Mutlak yol | Ne alınır |
|---|---|---|
| İskelet (aynı tür, aynı ders, bitmiş) | `/home/sef/01dev/_worktrees/kalem-0204/projeler/02-04-ydt-temel-s1/sahneler/06-hyperframes-kapak-c/uret.py` | dosya düzeni ve sırası: `zaman.json` + `zamanlar.json` doğrulaması, `kunye_svg()` (logo + rozet; çip YOK, ders adı YOK), başlık `<text>` konturu (`stroke` zemin, `stroke-width` 12, `stroke-linejoin="round"`, `style="font-kerning:none;paint-order:stroke fill"`), sarı kutu `<rect id="bk-kutu">` + kutudaki yazı `fill` zemin KONTURSUZ, figür çizimi (`fig_kalinlik` govde 4.4 · sac 3.6 · yuz 2.6, `/ fs`), `kesisim()`, HTML kabuğu (aynen: `Y.font_css()`, `Y.ZEMIN_CSS`, `#root data-composition-id="main" data-start="0" data-duration=… data-fps="30" data-width="1080" data-height="1920"`, `Y.zemin_html()`, tek `<svg id="sahne" … viewBox="0 0 1080 1920">`, `lib/gsap.min.js`, iki `tl.set("#sahne", …)` satırı, `window.__timelines["main"]`), `__main__` bloğu (aynen) |
| Kart çizgisi (el kutusu) | `/home/sef/01dev/_worktrees/kalem-0204/projeler/02-04-ydt-temel/sahneler/12-hyperframes-ozet/yardim.py` satır 308–313 `el_kutu(x, y, w, h)` | işlevi uret.py içine aynen al (tür ipucu ekle) |
| İkon ızgarası ve yerleştirme | `/home/sef/01dev/_worktrees/kalem-0204/projeler/02-04-ydt-temel/sahneler/12-hyperframes-ozet/uret.py` satır 72–156 | `_kutu`, `TREN` (yalnız lokomotif alt kümesi, §4.3), `_bilet()` / `BILET`, `_kutusu`, `_daire_yolu`, `ikon_yollari` (Catmull-Rom `egri` dalı dahil). `ikon_yollari`'yı kutu ölçüsünü parametre alacak biçimde uyarla: `ikon_yollari(parcalar, mx0, my0, en, boy)` (sabit `IKON_EN`/`IKON_BOY` yerine) |
| Çizim kaynağı (doğrulama) | `/home/sef/01dev/_worktrees/kalem-0204/projeler/02-04-ydt-temel/sahneler/05-canvas-ornek3/sahne.js` satır 81–142 | `trenParcalari` (duman elipsleri), `biletParcalari`; yalnız koordinat okunur |
| Tema dönüşümü | `P/ortak/hf_tema.py` | §5 |

## 3. Okuma ve sabitler

- `PAKET = AD.parent.parent`. `PAKET/zaman.json` oku. `duragan` içinde `klasor == AD.name` olan TEK kayıt assert; kaydın `kare == 1`,
  `cikti == "kapak-c.png"` assert. `sahneler[]` içinde `AD.name` YOK assert (S1 iskeletiyle aynı).
- `D/zamanlar.json`: `sure == 1.0`, `kare == 1`, `fps == 30` assert.
- Anlatım, sözcük, altyazı dosyası OKUNMAZ (ses yok, altyazı yok, karaoke yok).
- Renk yalnız `Y.RENK` anahtarlarıyla: `zemin #1b1a17`, `murekkep #f3efe6`, `ikincil #c9c2b3`, `vurgu #f2a93b`. Başka hex YOK.
- Sabitler: `KENAR = 48`, `SAG = 1032`, `BASLIK_GEN = 952`, `BANT_UST = 864`, `BANT_ALT = 1344`.
- Ölçü işlevi `g(m, b) = Y.genislik("Fredoka", 700, m, b)` (kerning yok; her yazıda `style="font-kerning:none"`).

## 4. Yerleşim (y = yazı tabanı, px)

```
y    0 ┌──────────────────────────────────────────────┐
       │ [logo 387×96]                                 │ HUD: logo + rozet; çip YOK, ders adı YOK
   216 │ (YDT · BASIC)                                 │ rozet 216–288
   358 │ İKİ ÖRNEK                                     │ Fredoka 700 S=190 (hesaplanır), kontur 12
  ≈544 │[İKİ ZAMAN]                                    │ satır 2 tamamen sarı kutuda
  ≈772 │                                               │
   884 │ ┌─────────────────────────────────┐           │ kart 1: [tren] The train [leaves] …
       │ └─────────────────────────────────┘     o     │
  1124 │ ┌─────────────────────────────────┐    /|\    │ kart 2: [bilet] I am going …
  1324 │ └─────────────────────────────────┘   _/ \_   │ figür 340 px, ayak 1324; kısa zemin çizgisi
  1344 ├───────────────────────────────────────────────┤ 1344–1920 BOŞ (hiçbir öğe yok)
```

### 4.1 HUD — `<g id="kunye">` (S1 iskeletindeki `kunye_svg()` aynen)
| Öğe | Ölçü | Renk |
|---|---|---|
| logo `<g id="ku-logo"><image id="logoimg" href="assets/logo.svg" …/>` | x 48, y 48, yükseklik 96, genişlik `96 · Y.LOGO_EN_BOY` (387) | dosya |
| rozet `<g id="rz0">` hap | x 48, y 216, h 72, rx 36, w = `Y.genislik("Lexend", 700, "YDT · BASIC", 36) + 56` | `<rect fill=vurgu>` |
| rozet yazısı | Lexend 700 36, `text-anchor="middle"`, x = hap ortası, taban 265 | `<text fill=zemin>` |

### 4.2 Başlık — `<g id="baslik">`
- Metin (elle büyük harf, Türkçe `İ` U+0130; `text-transform` YOK): satır 1 `İKİ ÖRNEK`, satır 2 `İKİ ZAMAN`.
- Boy: `p(S) = 0,08·S` (kutu yatay payı). Önce 100 ile ölç: `w100 = g("İKİ ZAMAN", 100) + 2·p(100)`;
  `S = floor(min(190, 952·100 / w100))`. S ile `B = max(g("İKİ ÖRNEK", S), g("İKİ ZAMAN", S) + 2·p)`; `B > 952` ise S'yi 1'er azalt;
  `B ≤ 952` assert. Beklenen: S = 190, B ≈ 944.
- Yatay: blok ortalı. Kutu solu `KX = 540 − B/2`; iki satırın yazı başı AYNI `x0 = KX + p` (iki `İKİ` alt alta).
  Kutu genişliği `g("İKİ ZAMAN", S) + 2·p`.
- Dikey (İ noktası ve Ö iki noktası yazı tabanının 0,93·S üstüne çıkar; kutu bunları içine almalı):
  `T1 = 358 + 0,93·S` · kutu üstü `KU = T1 + 0,12·S` · `T2 = KU + 1,00·S` · kutu altı `KA = T2 + 0,20·S` · rx `0,10·S`.
  Beklenen: T1 ≈ 534,7 · KU ≈ 557,5 · T2 ≈ 747,5 · KA ≈ 785,5. (Şef düzeltmesi 1. tur: 344 → 358; kontur dahil üst 352 = içerik bandı üstü.)
- `<text id="bs-1">` `İKİ ÖRNEK`: x0, T1, `fill` murekkep + kontur (S1 kalıbı: `stroke` zemin, 12, round, paint-order stroke fill).
- `<rect id="bk-kutu">`: x KX, y KU, w `g("İKİ ZAMAN", S) + 2·p`, h `KA − KU`, rx `0,10·S`, `fill` vurgu.
- `<text id="bs-2">` `İKİ ZAMAN`: x0, T2, `fill` zemin (`#1b1a17`), KONTURSUZ, `style="font-kerning:none"`.
- Başlıkta başka renk, altçizgi, hap YOK. id `t2` YOK.

### 4.3 Kartlar — `<g id="kartlar">` (iki kart üst üste, AYNI boy ve AYNI genişlik)
| Ölçü | Değer |
|---|---|
| Kart kutusu | x `KART_X0 = 64` → `KART_X1 = 880` (w 816), h `KART_H = 200` |
| Kart 1 / kart 2 üstü | `884` / `1124` (ara 40); kart 2 altı 1324 |
| Çizgi | `<path id="kc1">` / `<path id="kc2">` d = `el_kutu(64, y, 816, 200)`, `fill="none"`, `stroke` murekkep, `stroke-width` 4, `stroke-linecap/linejoin` round |
| Kart ortası | `cy = y + 100`; yazı tabanı `b = cy + 26` (kart 1 b = 1010, kart 2 b = 1250) |
| Yazı başı (iki kartta aynı) | `METIN_X = KART_X1 − 28 − g("The train leaves …", 72)` (≈ 243,4) |
| İkon kutusu (iki kartta aynı) | x `88` → `METIN_X − 24` (en ≈ 131,4), boy `112`, merkez y = cy; ikon kutuya oranı korunarak sığar, ortalanır |

Kart 1 (`<g id="kart1">`): `The train leaves …` — Fredoka 700 72, `style="font-kerning:none"`, üç ayrı `<text>`:
- `<text id="m1a">` `The train` → x METIN_X, `fill` murekkep.
- `<rect id="hap-leaves">` → x `XL − 0,12·72`, y `b − 0,86·72`, w `g("leaves", 72) + 2·0,12·72`, h `(0,86 + 0,18)·72`, rx 12, `fill` vurgu.
  `XL = METIN_X + g("The train ", 72)` (sondaki boşluk dahil).
- `<text id="m1b">` `leaves` → x XL, `fill` zemin (`#1b1a17`), KONTURSUZ. **Kapaktaki tek kart vurgusu budur.**
- `<text id="m1c">` `…` (U+2026) → x `XL + g("leaves ", 72)`, `fill` murekkep.
- Tren ikonu `<g id="ik-tren" fill="none" stroke-linecap="round" stroke-linejoin="round">`, solda ikon kutusunda.

Kart 2 (`<g id="kart2">`): `<text id="m2">` `I am going …` → x METIN_X, b, Fredoka 700 72, `fill` murekkep. `am going` VURGUSUZ (hap, altçizgi, renk yok).
- Bilet ikonu `<g id="ik-bilet" …>` aynı ikon kutusunda.

İkon parçaları (12-hyperframes-ozet/uret.py ızgarası; `ikon_yollari` yolları ekran koordinatına çevirir, stroke-width ekran px'i):
- **Tren = lokomotif alt kümesi** (vagon ve bağlantı YOK; kutuya büyük sığsın diye): `_kutu(200, 55, 170, 75)` gövde ·
  `_kutu(200, 10, 75, 45)` kabin · `_kutu(320, 22, 26, 33, True)` baca · `{"n": [(370, 95), (398, 130), (370, 130)]}` burun ·
  `_kutu(215, 20, 42, 25, True)` kabin camı · `{"daire": (240, 138, 17)}`, `{"daire": (335, 138, 17)}` tekerlek ·
  `{"n": [(190, 158), (410, 158)], "ince": True}` ray · duman `{"daire": (345, 2, 10), "ince": True}`, `{"daire": (372, -16, 7.5), "ince": True}`
  (sahne 05 duman elipslerinin daire karşılığı).
- **Bilet** = `_bilet()` aynen (çentikli çerçeve + 6 delik çizgisi + 3 baskı satırı), eğim yok.
- Çizgi: ince olmayan parça `stroke` murekkep, `stroke-width` 4 · `"ince": True` parça `stroke` ikincil, `stroke-width` 3. Dolgu yok.

### 4.4 Figür — `<g id="eskiz" fill="none" stroke=murekkep stroke-linecap="round" stroke-linejoin="round">`
| Öğe | Ölçü |
|---|---|
| figür `<g id="fig">` | `cizim/ogretmen.json` (`kadro.ogretmen`: ShirtPantsWB / Smile / Short). `FIG_H = 340`, ayak `FIG_ALT = 1324` (kart 2 altıyla aynı). `fs = FIG_H / (kutu.y1 − kutu.y0)`, `fw = (kutu.x1 − kutu.x0)·fs` (≈ 105), `FIG_X = 1016 − fw` (≈ 910,6). Çizim S1 iskeletindeki `eskiz_svg()` figür bölümüyle aynı (transform, `fig_kalinlik / fs`) |
| kısa zemin çizgisi `<path id="zc">` | `M{FIG_X − 16} 1324 L1016 1324`, `stroke-width` 4 |

## 5. Tema (hf_tema.py ile uyum)
- `Y.ZEMIN_CSS` ve `Y.zemin_html()` DEĞİŞTİRMEDEN kullan. Renkler SVG özniteliği, küçük harf hex. CSS `style` içinde renk YAZMA.
- Dönüşüm (açık temada): `rect fill #f2a93b` → `#ffe066` · `text fill #1b1a17` → `#1b2440` · `stroke #1b1a17` → zemin ·
  `#f3efe6` → `#1b2440` · `#c9c2b3` → `#5a6275`. Bu yüzden: rozet, `bk-kutu`, `hap-leaves` = `<rect fill="#f2a93b">`;
  rozet yazısı, `bs-2`, `m1b` = `<text fill="#1b1a17">`. `<path fill="#1b1a17">` YOK. Kart çizgisi `fill="none"`.
- id `t2`, `ku-nokta`, `rz1` KULLANMA.

## 6. Kurallar ve kabul ölçütü (uret.py içinde `assert`)
1. Bloklar (nesneler.json sırası): `hud` (48, 0, 984, 288) · `baslik` (x KX, y `T1 − 0,93·S`, w B, alt KA) · `bk-kutu` · `kart-1` ·
   `ik-tren` · `m-1` · `hap-leaves` · `kart-2` · `ik-bilet` · `m-2` · `fig`. Yazı kutusu: y_üst = taban − 0,75·boy, y_alt = taban + 0,25·boy;
   `m-1` x METIN_X, w `g("The train leaves …", 72)`; `m-2` w `g("I am going …", 72)`. İkon kutusu = çizilen yolların gerçek dış kutusu
   (`ikon_yollari` girdisinden hesapla). Kart kutusu el kutusunun ±4 px salınımını içersin (x − 4, y − 4, w + 8, h + 8).
2. Bütün bloklar x ∈ [48, 1032]; `hud` dışı bütün bloklar x ∈ [64 − 4, 1016]; hiçbir blok alt kenarı 1344'ü geçmez.
3. Yazı boyu ≥ 64 (rozet 36 hariç); başlık 2 satır; satır ≤ 24 karakter (`İKİ ÖRNEK`, `İKİ ZAMAN`, `The train leaves …`, `I am going …`, `YDT · BASIC`).
4. Kesişim 0: `hud`, `baslik`, `kart-1`, `kart-2`, `fig` çiftleri. Aralar: hud alt → başlık üstü ≥ 40 · başlık altı → kart 1 üstü ≥ 48 ·
   kart 1 altı → kart 2 üstü ≥ 24 · kart sağı (`KART_X1`) → `FIG_X` ≥ 24.
5. Kart içi: `ik-*` ve `m-*` kendi kartının iç kutusunda (kenara ≥ 16); ikon sağı → METIN_X ≥ 20; `m-1` sağı ≤ `KART_X1 − 24`.
   `hap-leaves` solu ≥ `METIN_X + g("The train", 72) + 4`; sağı ≤ `XL + g("leaves ", 72) − 4` (hap `train`e ve `…`e değmez).
6. Kart 1 ile kart 2 aynı (x, w, h) assert. Başlık kutusu `bs-2`'nin İ noktasını içerir: `KU ≤ T2 − 0,93·S`.
7. Üretilen HTML'de `#[0-9a-fA-F]{6}` eşleşmelerinin kümesi ⊆ {`#1b1a17`, `#f3efe6`, `#c9c2b3`, `#f2a93b`} assert.
   HTML'de `kanal`, `QR`, ` dk` geçmez assert. Emoji, kırmızı, yeşil, gradyan (zemin vinyeti hariç: `Y.ZEMIN_CSS`), gölge YOK.
8. Yasak: `Math.random`, `Date`, try/catch, `opacity:0` başlangıç, tween (iki `set` dışında hareket yok). Python: bütün işlevlerde tür ipucu.
9. `nesneler.json`: `[{"ad", "x", "y", "w", "h"}]` tam sayı (yuvarla), §6.1 sırası, `ensure_ascii=False`, `indent=2`.
10. `/usr/bin/python3 uret.py` stdout'a `index.html yazıldı <bayt>` ve `S=<boy>` basar; hata yoksa çıkış 0.

Kabul (şef koşturur, ajan koşturmaz): `ONIZLE_YALNIZ=1 bash calistir.sh` → "önizleme hazır"; `bash calistir.sh --tema acik|koyu` →
`P/kapak-c.png` ve `D/k/koyu/kapak-c-koyu.png` 1080×1920; taşma, kesik yazı, üst üste binme yok; 1344 altı boş.
