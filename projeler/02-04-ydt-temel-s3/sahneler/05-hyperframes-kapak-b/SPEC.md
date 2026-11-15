# SPEC — 02-04-ydt-temel-s3 · sahne 05-hyperframes-kapak-b (HyperFrames, 1080×1920, tek kare, ses yok)

Yazan: şef (15.11.2026, istem D-S3). Kod yazmaz; tasarım verir. K = `/home/sef/01dev/_worktrees/kalem-0204`.
Sahne dizini D = `K/projeler/02-04-ydt-temel-s3/sahneler/05-hyperframes-kapak-b/`. Paket P = `K/projeler/02-04-ydt-temel-s3/`.
Kaynak: `P/BRIEF-S3.md` "Kapak B ve C" (B satırı) · `P/uretim-tutanagi/kapak-taslak.md` §1–§3 (B) · `S3-duzeltme.md` madde 5.
Kapak B = soru kapağı. Başlık soruyu sorar, kart can alıcı öğeyi (`leaves`) gösterir. Cevap karede YOK.

## 1. Dosyalar

| Dosya | Durum | İş |
|---|---|---|
| `D/uret.py` | YOK | **YAZILACAK** (mutlak yol `/home/sef/01dev/_worktrees/kalem-0204/projeler/02-04-ydt-temel-s3/sahneler/05-hyperframes-kapak-b/uret.py`) |
| `D/yardim.py` | VAR (S1 sahne 05 kopyası) | DOKUNMA; yalnız `import yardim as Y` |
| `D/cizim/ogretmen.json` | VAR | salt oku (`kutu`, `el`, `yollar[].d`, `yollar[].parca`) |
| `D/calistir.sh`, `D/olay.py`, `D/zamanlar.json` | VAR (şef) | DOKUNMA |
| `D/nesneler.json` | uret.py yazar | §6 madde 4 |

Başka dosyaya dokunma. Silme yok. Test, render, snapshot, `calistir.sh`, git YOK. `P/ortak/`, `P/zaman.json` ve başka sahneler salt okunur.

## 2. Kalıp kaynakları (salt oku)

| Kalıp | Mutlak yol | Ne alınır |
|---|---|---|
| İskelet (aynı tür, aynı ders, bitmiş) | `/home/sef/01dev/_worktrees/kalem-0204/projeler/02-04-ydt-temel-s1/sahneler/05-hyperframes-kapak-b/uret.py` | dosya düzeni; `zaman.json` + `zamanlar.json` doğrulaması (satır 20–32, aynısı); `kunye_svg()` (satır 99–112, aynısı); başlık `<text>` konturu (satır 128–131); figür çizimi (satır 154–167); `kesisim()`; HTML kabuğu + tek `set` çizelgesi (satır 374–400, aynısı); `__main__` (satır 406–426) |
| Tren yolları (SVG) | `/home/sef/01dev/_worktrees/kalem-0204/projeler/02-04-ydt-temel/sahneler/06-hyperframes-soru1/uret.py` | `kutu_d` (satır 74–91), `daire_d` (satır 94–103), `tren_parcalari` (satır 123–169). Bu sahnede `u()` YOK: `u(n)` yerine `n` yaz (dikey 1080 px doğrudan) |
| Saat geometrisi | `/home/sef/01dev/_worktrees/kalem-0204/projeler/02-04-ydt-temel/sahneler/05-canvas-ornek3/sahne.js` satır 106–116 `saatParcalari` | kadran + 4 çentik + yelkovan 12'de + akrep 7'de; SVG yoluna çevir (§4.4) |
| İşaret kalıbı | `.../02-04-ydt-temel/sahneler/06-hyperframes-soru1/SPEC.md` satır 64 | figürden hedefe kalem oku (ok başı iki kısa çizgi) |

## 3. Okuma ve sabitler

- `PAKET = AD.parent.parent`. `zaman.json` → `duragan` içinde `klasor == AD.name` TEK kayıt; `kare == 1`, `cikti == "kapak-b.png"`;
  `sahneler[]` içinde `AD.name` YOK (assert, S1 satır 20–27 ile aynı). `zamanlar.json`: `sure` 1,0 · `kare` 1 · `fps` 30 assert.
- Anlatım, sözcük, altyazı dosyası OKUNMAZ (ses yok; kapak B sese bağlı değil).
- Renk yalnız `Y.RENK` anahtarlarıyla: `zemin #1b1a17`, `murekkep #f3efe6`, `ikincil #c9c2b3`, `vurgu #f2a93b`. Başka hex YOK.
- Sabitler: `KENAR 48 · SAG 1032 · BASLIK_GEN 952 · BANT_UST 864 · BANT_ALT 1344 · PLATFORM 1536`.
- Sahne sabitleri: `K_TREN = 1.1 · TX0 = 196 · RAY_Y = 1172 · TY0 = RAY_Y − 158·K_TREN` (= 998,2).

## 4. Yerleşim (y = yazı tabanı, px; açık tema görünümü)

```
y    0 ┌───────────────────────────────────────────┐
       │ [logo 387×96]                              │ HUD (çip YOK, ders adı YOK; S1 kapak B ile aynı)
   216 │ (YDT · BASIC)                              │ rozet 216–288
  ≈497 │            NEDEN -ING                      │ Fredoka 700 S, ortalı, kontur
  ≈716 │          (   YOK?   )                      │ Fredoka 700 S, sarı hap içinde, ortalı
   864 │      ◯saat      ?(sarı)                    │ saat (wagon üstü) · el çizimi ? (kabin üstü)
       │   ┌──────┐┌──┐    duman        ┌fig┐       │
       │   │ vagon││lok▶   ←───────────╮│   │       │ tren sağa bakar; figür aynalı, trene bakar; kalem oku
  1172 │  ═══════════════ ray           │   │       │
  1202 │ ┌──────────────────────────┐   │   │       │
  1294 │ │ The train leaves …       │   │   │       │ kart: Fredoka 700 72; leaves altında sarı el altçizgisi
  1344 │ └──────────────────────────┘  ─┴───┴─      │ kısa zemin çizgisi yalnız figür altında
  1536 ├───────────────────────────────────────────┤ 1344–1920: BOŞ (platform)
```

### 4.1 HUD — `<g id="kunye">`
S1 `kunye_svg()` birebir: logo `<g id="ku-logo"><image id="logoimg" href="assets/logo.svg" x="48" y="48" width="96·Y.LOGO_EN_BOY" height="96"/>`;
rozet `<g id="rz0">` hap x 48, y 216, h 72, rx 36, w = `Y.genislik("Lexend", 700, "YDT · BASIC", 36) + 56`, `<rect fill=vurgu>`;
yazı Lexend 700 36, `text-anchor="middle"`, taban 265, `<text fill=zemin>`. Ders adı ve çip YOK.

### 4.2 Başlık — `<g id="baslik">`
- Satır 1 `NEDEN -ING` (elle büyük harf; `I` = Latin U+0049; `text-transform` YOK). Satır 2 `YOK?` sarı hapta.
- Boy `S`: boy 100 ile ölç: `g1_100 = genislik("Fredoka", 700, "NEDEN -ING", 100)`, `g2_100 = genislik(…, "YOK?", 100)`.
  `S = floor(min(190, 952·100/g1_100, 952·100/(g2_100 + 60)))` (hap genişliği `g2 + 0,60·S`). S ile yeniden ölç: `g1 ≤ 952`,
  `g2 + 0,60·S ≤ 952` assert (gerekirse S'i 1'er azalt, S1 satır 67–74 kalıbı). Beklenen S = 174.
- Taban: `T1 = 375 + 0,70·S`; `T2 = T1 + 1,26·S`. İki satır aynı boy S.
- `<text id="bs-1">`: x = `540 − g1/2`, y T1, Fredoka 700 S, `fill` murekkep, `stroke` zemin, `stroke-width` 12, `stroke-linejoin="round"`,
  `style="font-kerning:none;paint-order:stroke fill"`, `xml:space="preserve"`.
- `<rect id="bk-hap">`: pay `p = 0,30·S`; x = `540 − g2/2 − p`, w = `g2 + 2p`, y = `T2 − 0,90·S`, h = `1,10·S`, rx = `h/2`, `fill` vurgu.
  Hap, `bs-2`'nin ALTINDA çizilir (önce rect, sonra text).
- `<text id="bs-2">`: x = `540 − g2/2`, y T2, Fredoka 700 S, `fill` zemin (açık temada pilMetin `#1b2440` olur), KONTURSUZ,
  `style="font-kerning:none"`.
- Başlıkta başka renk, altçizgi, ikinci hap YOK.

### 4.3 Sahne grubu — `<g id="eskiz" fill="none" stroke=murekkep stroke-linecap="round" stroke-linejoin="round">`
Sırayla: zemin çizgisi, tren, saat, figür, kalem oku. `ikincil` renkli parçalar kendi `stroke` özniteliğini taşır.

| Öğe | Ölçü |
|---|---|
| tren `<g id="tren">` | 06 `tren_parcalari(TX0, TY0, K_TREN)` (u yok). Parça başına `<path id="tr{i}" d=… stroke-width=…>`; kalınlık: gövde 4,5 · ince 3,6 · ray 4,0 (`stroke` ikincil) · duman 3,4 (`stroke` ikincil). Tren sağa bakar (lokomotif sağda) |
| saat `<g id="saat">` | merkez `SC = (TX0 + 87,5·K_TREN, 924)` (vagon ortasının üstü), `SR = 56`. Kadran `daire_d(SC, SR)` w 5. 4 çentik (12, 3, 6, 9 yönü) `0,80·SR → 0,66·SR` w 4. Yelkovan merkez → 12 yönü, boy `0,66·SR`, w 5. Akrep merkez → 7 yönü (açı `a = 7/12·2π`, uç `(cx + sin a·0,5·SR, cy − cos a·0,5·SR)`), w 7. **Akrep ve yelkovan murekkep** (sarı DEĞİL; tek vurgu kuralı). Rakam YOK |
| figür `<g id="fig">` | `FIG_H = 476`, `FIG_ALT = 1341`, `FIG_SAG = 1016`. `x0, y0, x1, y1 = kutu`; `fs = FIG_H/(y1 − y0)`; `FIG_SOL = FIG_SAG − (x1 − x0)·fs`; `FIG_UST = FIG_ALT − FIG_H`. **Yatay ayna:** `transform="translate({FIG_SOL + x1·fs} {FIG_UST − y0·fs}) scale({−fs} {fs})"`. Yollar ve kalınlıklar S1 satır 160–164 (`govde 4.4 · sac 3.6 · yuz 2.6` / fs). Aynalı el noktası: `EL = (FIG_SOL + (x1 − el[0])·fs, FIG_UST + (el[1] − y0)·fs)` (≈ 882, 1117) |
| zemin çizgisi `<path id="zc">` | `M{FIG_SOL − 24} 1342 L1016 1342`, w 4 (yalnız figür altı) |
| kalem oku `<g id="ok">` | Gövde `<path id="ok-g">`: ikinci derece eğri `M S Q C E`. `S = (FIG_SOL − 12, EL.y − 10)`; `E = (TREN_SAG + 16, 1086)`, `TREN_SAG = TX0 + 420·K_TREN`; `C = ((S.x + E.x)/2, min(S.y, E.y) − 50)`. Ok başı `<path id="ok-b">`: E'den, yön `C → E` vektörünün tersi ±0,5 rad döndürülmüş, iki çizgi, boy 26 (`M uç1 L E L uç2`). w 6, murekkep |

### 4.4 Soru işareti — `<g id="soru">` (eskiz DIŞINDA)
- El çizimi yol, yazı tipi DEĞİL. Birim kutu (genişlik 0,62, yükseklik 1; sol üst 0,0):
  gövde `M0.05 0.27 C0.06 0.07 0.30 -0.01 0.47 0.05 C0.64 0.11 0.66 0.33 0.50 0.43 C0.36 0.52 0.31 0.56 0.31 0.72`;
  nokta `M0.31 0.92 L0.311 0.92` (sıfıra yakın boy + yuvarlak uç = nokta).
- Ölçü: `SH = 112`, `SY0 = 872`, merkez x `SCX = TX0 + 237,5·K_TREN` (kabin ortasının üstü), `SX0 = SCX − 0,31·SH`.
  Grup `transform="translate(SX0 SY0) scale(SH)"`, `fill="none"`, `stroke` vurgu, `stroke-linecap="round"`, `stroke-linejoin="round"`.
  Gövde `stroke-width = 12/SH`; nokta `stroke-width = 16/SH`.

### 4.5 Kart — `<rect id="kart">` + `<text id="kart-yazi">` + `<path id="alti">` (eskiz DIŞINDA)
- Metin `The train leaves …` (sonda boşluk + U+2026). `KB = 72`. `KW = genislik("Fredoka", 700, metin, 72) + 80` (beklenen ≈ 688,6).
- Kart: x 66, y 1202, w KW, h 140, rx 28, `fill="none"`, `stroke` murekkep, w 4 (kontur payıyla sol kenar 64).
- Yazı: x 106, taban 1294, Fredoka 700 72, `fill` murekkep, kontursuz, `style="font-kerning:none"`, `xml:space="preserve"`.
- Altçizgi (`leaves`): `LX = 106 + genislik("Fredoka", 700, "The train ", 72)`, `LW = genislik(…, "leaves", 72)`.
  `d = M{LX − 4} 1314 Q{LX + LW/2} 1320 {LX + LW + 4} 1311`, `fill="none"`, `stroke` vurgu, w 10, round cap.
- Kartta başka vurgu YOK. `train` altı çizilmez.

## 5. Tema (hf_tema.py ile uyum)
- `Y.ZEMIN_CSS` ve `Y.zemin_html()` DEĞİŞTİRMEDEN kullan. Renkler SVG özniteliği, küçük harf hex; CSS `style` içinde renk YOK.
- Dönüşüm (açık tema): `rect fill #f2a93b` → `#ffe066` (rozet, hap) · `text fill #1b1a17` → `#1b2440` (rozet yazısı, `YOK?`) ·
  `stroke #f2a93b` → `#d9900f` (`?`, altçizgi) · `#f3efe6` → `#1b2440` · `stroke #1b1a17` → zemin (başlık konturu).
- `<circle>` KULLANMA (tema `circle fill #f2a93b` kuralı karışır). id `t2`, `ku-nokta`, `rz1` KULLANMA.

## 6. Kurallar ve kabul ölçütü (uret.py içinde `assert`)
Blok kutuları kontur payıyla (yarım kalınlık) hesaplanır; başlık yazı kutusu S1 gibi kontursuz.
1. Bloklar: `hud` (48, 0, 984, 288) · `baslik` (x min(bs-1 x, hap x) → max sağ; y `T1 − 0,75·S` → `T2 + 0,20·S`) · `bk-hap` ·
   `saat` (`SC ± (1,02·SR + 2,5)`) · `soru` (x `SX0 − 6` → `SX0 + 0,62·SH + 6`; y `SY0 − 6` → `SY0 + 0,92·SH + 8`) ·
   `duman` (x `TX0 + 334·K − 2` → `TX0 + 380·K + 2`; y `TY0 − 23·K − 2` → `TY0 + 11·K + 2`) ·
   `tren` (x `TX0 − 10·K − 2` → `TX0 + 420·K + 2`; y `TY0 + 10·K − 3` → `RAY_Y + 2`) · `kart` (64, 1200, KW + 4, 144) ·
   `kart-yazi` (x 106, y `1294 − 0,75·72`, w metin genişliği, h 72) · `alti` (x `LX − 9`, y 1306, w `LW + 18`, h 19) ·
   `fig` (FIG_SOL, FIG_UST, `(x1 − x0)·fs`, FIG_H; kontursuz) · `ok` (eğri 40 noktada örneklenir + ok başı uçları, ± 3).
2. Bütün bloklar x ∈ [48, 1032], y ≥ 0, alt ≤ 1344. Başlık ve sahne blokları x ∈ [64, 1016]. Sahne blokları (saat, soru, duman,
   tren, kart, fig, ok) y ≥ 864. 1344–1920 arasında hiçbir öğe yok.
3. Kesişim 0: `hud, baslik, saat, soru, duman, tren, kart, fig, ok` çiftleri (yalnız `duman–tren` çifti hariç).
   `bk-hap` `baslik` içinde; `kart-yazi` ve `alti` `kart` içinde (kapsama assert).
   Boşluklar: hud alt → başlık üst ≥ 40 · başlık alt → en üst sahne bloğu ≥ 48 · saat alt ve soru alt → tren üst ≥ 16 ·
   tren alt → kart üst ≥ 20 · kart sağ → fig sol ≥ 60 · ok sol − tren sağ ≥ 8 · fig sol − ok sağ ≥ 4 · soru sağ → duman sol ≥ 24 ·
   saat sağ → soru sol ≥ 24.
4. `nesneler.json`: `[{"ad", "x", "y", "w", "h"}]` tam sayı; sıra madde 1'deki gibi (12 blok).
5. Yazı boyu ≥ 64 (rozet 36 hariç): S ≥ 64, KB = 72. Başlık 2 satır, 3 sözcük (`NEDEN`, `-ING`, `YOK?`). Her satır ≤ 24 karakter
   (`YDT · BASIC`, `NEDEN -ING`, `YOK?`, `The train leaves …`). `"İ"` (İ) başlık metninde YOK; `-ING` içinde U+0049 var.
6. Yasak (html küçük harfe çevrilip aranır): `kanal`, `qr`, `tarife`, `timetable`, `6 dk`, `text-transform`, `math.random`,
   `date.now`, `new date`, `opacity:0`, `<circle`. `id="t2"`, `id="ku-nokta"`, `id="rz1"` YOK. html'deki 6 haneli hex kümesi
   ⊆ {`#1b1a17`, `#f3efe6`, `#c9c2b3`, `#f2a93b`}. Yeşil, kırmızı, gradyan (zemin vinyeti hariç), gölge, emoji YOK. try/catch YOK.
   Hareket yok: tek `set` çizelgesi (S1 satır 393–399).
7. Python: bütün işlevlerde tür ipuçları. `/usr/bin/python3 uret.py` stdout'a `index.html yazıldı <bayt>` ve `S=<boy> KW=<genişlik>`
   basar; hata yoksa çıkış 0.

## 7. Olay listesi (durağan kare)

| Olay | Kare / sn | Cümle · sözcük |
|---|---|---|
| bütün öğeler tam görünür (tek `set`) | kare 0; yakalama 0,5 sn (`zamanlar.json` `yakala_sn`) | yok (ses yok, zaman çizelgesi dışı) |

`olaylar.json` boş liste (`olay.py`). Ekran metni: `YDT · BASIC` · `NEDEN -ING` · `YOK?` · `The train leaves …`. Başka metin YOK.

Kabul (şef koşturur, ajan koşturmaz): `ONIZLE_YALNIZ=1 bash calistir.sh` → "önizleme hazır"; `bash calistir.sh --tema acik|koyu` →
`P/kapak-b.png` ve `D/k/koyu/kapak-b-koyu.png` 1080×1920; taşma, kesik yazı, üst üste binme yok.
