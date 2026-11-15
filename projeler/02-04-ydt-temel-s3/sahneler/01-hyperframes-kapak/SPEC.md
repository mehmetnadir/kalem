# SPEC — 02-04-ydt-temel-s3 · sahne 01-hyperframes-kapak (HyperFrames, 1080×1920, 102 kare)

Kaynak: `BRIEF-S3.md` ("Sahneler" satır 01, "Sahne içeriği" 0,00–3,00, "Kapak A"), `uretim-tutanagi/kapak-taslak.md` §1–§3 (A),
`uretim-tutanagi/senaryo-taslak.md` §2 satır 01, `uretim-tutanagi/S3-duzeltme.md`, `../present-continuous-dikey/BRIEF-DIKEY.md` §0, §2, §3,
`K/.claude/docs/sozlesme.md` (HF dersleri). Yazan: şef (15.11.2026). Bu belge tasarım verir; tam kod içermez.
K = `/home/sef/01dev/_worktrees/kalem-0204`. D = `K/projeler/02-04-ydt-temel-s3/sahneler/01-hyperframes-kapak/` (bu sahne dizini).

## 1. Dosyalar

| Dosya | Durum | İş |
|---|---|---|
| `D/uret.py` | YOK | §3'e göre yaz (agy) |
| `D/yardim.py` | VAR (S1 sahne 01 `yardim.py` birebir kopyası; `ORTAK` = S3 `ortak/`) | DOKUNMA; `import yardim as Y` |
| `D/olay.py` | VAR (şef uyarladı) | DOKUNMA; `uret.zamanlar()` arayüzü §3.10'da |
| `D/calistir.sh`, `D/zamanlar.json`, `D/nesneler.json`, `D/cizim/ogretmen.json`, `D/cizim/KAYNAK.md` | VAR (şef) | DOKUNMA |

Yalnız `D/uret.py` yazılır. Başka dosyaya dokunma. Silme yok. Test, render, git yok. Betik koşma yok (şef koşar).
Python: girinti 4 boşluk (S1 kalıbıyla uyum), satır ≤ 120, yeni işlevlerde tip ipucu. Çalıştırma `/usr/bin/python3 uret.py`
(fontTools kullanıcı site-packages'ta; `-I` YOK).

## 2. Kalıp kaynakları (salt oku)

| Kalıp | Mutlak yol | Ne alınır |
|---|---|---|
| Ana iskelet (aynı motor, aynı ders, dikey kapak) | `K/projeler/02-04-ydt-temel-s1/sahneler/01-hyperframes-kapak/uret.py` | BÜTÜN yapı: okuma, sabitler, `_denetimler()` (power3 ease işlevleri, `_kesisir`, örnekleme döngüsü), `zamanlar()`, `uret()` HTML iskeleti (`#root` data-*, `#sahne` svg, `<defs>` clip), `ac()`, kırpmayla yazım (`#crN` width tween), `uc2()` (svgOrigin bir kez `gsap.set`, x/y `power3.inOut`, scale `power3.out`), altyazı aç/kapa, 0. kare `gsap.set`'leri, `window.__timelines["main"]`, `__main__` (font kopya, index.html, devir.json) |
| Kalem geometrisi | `K/projeler/02-04-ydt-temel-s3/ortak/kalem-canvas.js` satır 48–56 (`hash`, `gurul`), 254–263 (`elips`), 279–291 (`kutu`) | Python'a birebir taşı (§3.2) |
| Çizim geometrisi | `K/projeler/02-04-ydt-temel/sahneler/05-canvas-ornek3/sahne.js` satır 81–142 (`trenParcalari`, `saatParcalari`, `biletParcalari`) | parça listeleri, tohumlar, kalınlıklar (§3.3) |
| Künye, tema | `D/yardim.py` (`kunye_svg`, `altyazi_svg`, `rozet_konumu`, `HUD`, `DERS`, `RENK`) · `K/projeler/02-04-ydt-temel-s3/ortak/hf_tema.py` | uret.py KOYU hex yazar; §3.7 |

## 3. `uret.py`

### 3.1 Okuma
- `Z = zamanlar.json` (D içinde): fps 30, kare 102, sure 3,4, `alti` [0,30, 0,50], `yazi_cap` 0,28, `ucus` [2,00, 0,85], `ucus_olcek` 0,72,
  `rozet_kay` [2,00, 0,40], `sahne_sol` [2,00, 0,40], `kunye_ac` [2,62, 0,23], `baslik_sol` [2,49, 0,18], `ucus_ayrik` 16, `kapak_kare` 59,
  `kart_ciz` [2,62, 0,28], `tren_olcek` 0,5.
- `SOZ` = `ORTAK/anlatim/sozcukler.json` içinde `cumle == 1` sözcükler. Assert: ilk 7 sözcük
  `["The", "train", "to", "Izmir", "leaves", "at", "seven"]`. Zaman dosyadan okunur (sahne 01: küresel sn = yerel sn).
  Ölçülen: The 1,00–1,16 · train 1,28–1,40 · to 1,48–1,56 · Izmir 1,64–2,12 · leaves 2,20–2,44 · at 2,56–2,68 · seven 2,80–2,92.
- `ALT` = `ORTAK/anlatim/altyazi.json`, EKRAN dönüşümüyle kopyalanır: her öğenin `metin` alanında `"Izmir"` → `"İzmir"`,
  `"seven p.m."` → `"7 pm"` (ekranda noktalı İ ve `7 pm` kuralı; ses değişmez). Sözlük modül düzeyinde `EKRAN` adıyla durur.
- `FIG` = `D/cizim/ogretmen.json` (`kutu` [x0,y0,x1,y1], `el` [x,y], `yollar` [{parca, d}]) — S1 ile aynı veri.

### 3.2 Kalem geometrisi (kalem-canvas.js → Python, birebir)
- `_imul(a, b)`: 32 bit tamsayı çarpımı (`(a & 0xFFFFFFFF) * (b & 0xFFFFFFFF) & 0xFFFFFFFF`).
- `hash(a, b=0, c=0) -> float`: JS ile aynı: h = (imul(a,374761393) + imul(b,668265263) + imul(c,1274126177)) mod 2³²;
  h = imul(h ^ (h >> 13), 1274126177); h ^= h >> 16; dönüş h / 4294967296 (bütün işlemler işaretsiz 32 bit).
- `gurul(x, s)`: i = floor(x), f = x − i, u = f²(3 − 2f); lerp(hash(i, s, 7), hash(i + 1, s, 7), u) − 0,5.
- `elips(cx, cy, rx, ry, egim=0, tohum=1) -> list[(x, y)]` ve `kutu(x, y, w, h, tohum=1) -> list[list[(x, y)]]` (4 kenar, her biri 3 nokta):
  JS satır 254–263 ve 279–291 ile aynı formül.
- SVG yolu: kutu kenarı `[a, m, b]` → `"M a Q m b"`; öbür nokta dizileri → `"M p0 L p1 L …"`. Sayılar 2 ondalık.

### 3.3 Çizimler (yerel birim = px; `u(n) = n`)
| Öğe | Geometri (ana ders sahne 05'ten) | Kalınlık · renk |
|---|---|---|
| Tren `g#tren > g#tren-ic` | `trenParcalari(0, 0)` parça listesinin aynısı: lokomotif kutu(200,55,170,75,31), kabin kutu(200,10,75,45,32), baca kutu(320,22,26,33,33), ön burun düz [(370,95),(398,130),(370,130)], vagon kutu(0,45,175,85,34), bağlantı düz [(175,112),(200,112)], vagon camları kutu(20,60,50,30,35) + kutu(100,60,50,30,36), kabin camı kutu(215,20,42,25,37), tekerlek elips(x,138,17,17,0,50+i) x∈{40,135,240,335}, ray düz [(−10,158),(420,158)], duman elips(345,2,11,9,0.2,61) + elips(372,−16,8,7,0.3,62) | gövde 4,5 · ince 3,6 (baca, bağlantı, camlar) · ray 4 · duman 3,4 / 3,2; gövde/ince `#f3efe6`, ray ve duman `#c9c2b3`; her yolda `vector-effect="non-scaling-stroke"` |
| Saat `g#saat` (`#eskiz` içinde) | `saatParcalari(SAAT_X, SAAT_Y, SAAT_R)`: kadran elips(cx,cy,r,0.97r,0.05,41); 4 çentik (12, 3, 6, 9) 0,8r → 0,66r; yelkovan merkez → (cx, cy − 0,66r); akrep merkez → 210° yönünde 0,5r (kollar yedide). Rakam YOK | kadran 5, çentik 4, yelkovan 5, akrep 6; hepsi `#f3efe6` (akrep sarı DEĞİL: tek vurgu kuralı) |
| Bilet `g#bilet` (`#eskiz` içinde, figürden ÖNCE) | `biletParcalari` noktaları ölçek BS ile: P(x, y) = (BCX + BS·(x·cos e − y·sin e), BCY + BS·(x·sin e + y·cos e)); 4 kenar (sağ/sol kenarda 13 noktalı çentik yayı, yarıçap 22), 6 delik çizgisi (x 100, y0 = −58 + 20i, boy 11), 3 baskı satırı ([−150,−30→60], [−150,0→30], [−150,30→70]) | kenar 4,5 `#f3efe6`; delik 3,4 ve baskı 4 `#c9c2b3`. Önce örtü: köşeler (±180, ±70) dönüşmüş çokgen, `stroke="none" style="fill:var(--zemin)"` |
| Figür `g#fig` (`#eskiz` içinde, biletten SONRA: el bileti tutar) | S1 ile aynı: `translate(FIG_X − x0·fs  (ZEMIN_Y − FIG_H) − y0·fs) scale(fs)`, yollar `f0…` | gövde 4,4 · saç 3,6 · yüz 2,6 (ekranda; `/ fs`), `#f3efe6` |

`#tren` dışta dönüşümsüz grup (GSAP bunu sürer); yerleştirme içteki `g#tren-ic transform="translate(TX TY)"`'de. Dış grupta transform
özniteliği OLMAZ (GSAP öznitelikteki translate'i x/y diye okur, uçuşta kaybolur). Yer çizgisi YOK: tren rayı zemin; figür ayağı aynı y'de.

### 3.4 Sabitler ve türetilen ölçüler (px; g(m, aile, ağırlık, boy) = `Y.genislik`)
| Ad | Değer | Not (şef ölçümü) |
|---|---|---|
| KENAR | `Y.HUD["kenar"]` = 48 | |
| BAS1, BAS2Y | `TARİFE`, `PLAN` | başlık; Türkçe İ; `text-transform` yok |
| PAD | 0,20 em | hap yatay iç boşluğu |
| B | floor(min(190, 952 / g(BAS1,1), 952 / (g(`= PLAN`,1) + 2·PAD))) | = 190; assert 150 ≤ B ≤ 190 |
| g1, t1x | g(BAS1, Fredoka 700, B), (W − g1)/2 | ≈ 647,9 · 216,0 |
| T1 | 354 + 0,921·B | ≈ 529,0 (İ noktası üstü 354 ≥ 352) |
| ALTI_Y | T1 + 0,16·B | ≈ 559,4 (TARİFE'de kuyruk yok) |
| HAP_UST | ALTI_Y + 29 | ≈ 588,4 |
| T2 | HAP_UST + 0,88·B | ≈ 755,6 (`PLAN` başlık 2 tabanı) |
| HAP_ALT | T2 + 0,18·B | ≈ 789,8 |
| hap | w = g(`= PLAN`, B) + 2·PAD·B, x = (W − w)/2, h = HAP_ALT − HAP_UST, rx = h/2 | ≈ x 195,6 · w 688,8 |
| GX | hap.x + PAD·B | ≠ glif kutusunun solu ≈ 233,6 |
| PX | GX + g(`= `, B) | `PLAN` yazısının x'i ≈ 362,8 (text-anchor start) |
| ≠ çizgileri (em → px: x = GX + a·B, y = T2 − b·B) | çubuk 1 (0,093; 0,159) → (0,352; 0,159); çubuk 2 (0,093; 0,356) → (0,352; 0,356); eğik (0,322; 0,555) → (0,150; −0,005) | Fredoka `=` glif ölçüsü (çubuk kalınlığı 0,158 em). Çubuk w 0,158·B, eğik w 0,14·B, round cap. QA tur 1: ilk eğik (0,330; 0,560) → (0,115; −0,045) hap kavisinden taşıdı |
| SOL | 97 | kart yazısı solu (kart x 57 + iç boşluk 40) |
| KB | 64 | kart yazısı Fredoka 700 64 (sahne 02 kart yazısıyla aynı; BRIEF-DIKEY §3) |
| SATIR_ARA | 98 | ≈ 1,54·KB (sözleşme: kalıcı altçizgi alt satıra değmez) |
| R1_K, R2_K | 876, R1_K + SATIR_ARA = 974 | kapak konumu tabanları |
| KART | x 57, y 368, w 966, h 260, tohum 71 | `kutu(57, 368, 966, 260, 71)`; taşma payı 9 px ile x 48–1032 |
| R1_SON, R2_SON | 468, 566 | uçuş sonrası = sahne 02 kare 0 |
| DY | R1_SON − R1_K = −408 | iki satıra aynı kayma |
| ZEMIN_Y | 1384 | tren rayı ve figür ayağı |
| TX, TY | 58, ZEMIN_Y − 158 = 1226 | tren yerel (−10, 158) → ekran (48, 1384); tren kutusu yerel [−10, 420] × [−24, 158] → ekran [48, 478] × [1202, 1384] |
| SAAT_X, SAAT_Y, SAAT_R | 160, 1100, 72 | ekranda ≈ 82–238 × 1022–1178 (elips taşması 1,09·r) |
| FIG_H, FIG_X | 460, 600 | fs = FIG_H / (y1 − y0); figür 600–742,6 × 924–1384; el EX, EY ≈ (728,8, 1167,9) (S1 formülü) |
| BS, egim | 0,42, −0,18 | bilet ölçeği ve eğimi |
| BCX, BCY | EX + BS·150, EY − 6 | ≈ (791,8, 1161,9); bilet sol ucu elin üstünde |
| E1 (`leaves`) | x 380 `text-anchor="middle"`, taban 1080 | Caveat 700 72; ≈ 309–451 × 1030–1098 |
| E2 (`am going`) | x W − KENAR = 1032 `text-anchor="end"`, taban 1080 | Caveat 700 72; ≈ 816–1032 |
| TREN_SON | kutu [785, 392] – [1000, 483]; o3 = kapak kutusu merkezi (263, 1293); h3 = (892,5, 437,5); hs3 = `tren_olcek` 0,5 | kart 1 sağ üst köşesi (kart içinde, satır 1'in sağında) |

### 3.5 Olay listesi (kare = round(sn × 30))
| # | Olay | sn (kare) | Cümle sözcüğü |
|---|---|---|---|
| 1 | Kapak tam görünür: logo, rozet `YDT · BASIC` (x 48'de), `TARİFE`, hap `≠ PLAN`, tren + saat, bilet tutan figür, etiketler `leaves` / `am going` | 0,00 (0) | söz öncesi |
| 2 | `TARİFE` altına sarı el altçizgisi kalemle çizilir (`strokeDashoffset`, `sine.inOut`) | `alti` 0,30–0,80 (9–24) | söz öncesi |
| 3 | altyazı dilimi açılır (cümle 1, EKRAN metni), sahne sonuna kadar | SOZ[0].t0 − 0,05 = 0,95 (29) | The |
| 4 | satır 1 kırpmayla sözcük sözcük yazılır: `The` · `train` · `to` · `İzmir`; her sözcük t0'da başlar, süre min(t1 − t0, `yazi_cap`) | 1,00–1,16 · 1,28–1,40 · 1,48–1,56 · 1,64–1,92 | The 1,00 · train 1,28 · to 1,48 · Izmir 1,64 |
| 5 | KAPAK A KARESİ: uçuş öncesi, çip yok, ders adı yok, satır 1 tam, altçizgi tam | 1,97 (59) | — |
| 6 | rozet sağa kayar: x 48 → `Y.rozet_konumu()[0]` | `rozet_kay` 2,00–2,40 (60–72) | — |
| 7 | `#kapak-sahne` (saat, bilet, figür, etiketler) solar | `sahne_sol` 2,00–2,40 | — |
| 8 | uçuş: başlık 1 → ders adı 1. satır, hap → ders adı 2. satır (S1 `uc2`, opaklık `baslik_sol`'da 0'a); tren küçülerek kart 1 sağ üst köşesine iner (aynı x/y/scale kalıbı, opaklık DEĞİŞMEZ); `#r1`, `#r2` DY kadar yukarı | `ucus` 2,00–2,85 (60–85) | — |
| 9 | satır 2 sözcük sözcük: `leaves` · `at` · `7` (satır grubu uçuşla birlikte yerine iner) | 2,20–2,44 · 2,56–2,68 · 2,80–2,92 | leaves 2,20 · at 2,56 · seven 2,80 |
| 10 | başlıklar solar (2,49–2,67), ders adı açılır (2,62–2,85), çip `Hook` açılır (u1 − 0,22 = 2,63, 0,2 sn) | 2,49–2,85 | — |
| 11 | kart 1 çerçevesi kalemle çizilir: 4 kenar sırayla (kutu sırası), süre kenar boyuyla orantılı, toplam `kart_ciz`; her kenar başlangıcında opaklık 0 → 1 | 2,62–2,90 (79–87) | — |
| 12 | durgun; son 12 kare geçiş altında | 2,92–3,40 (88–101) | `p.m.` 3,00 → sahne 02 |

### 3.6 Yerleşim
```
y   48 ┌ logo 387×96 (0. kareden)                        [Hook] çip 2,63'ten ┐ HUD 0–320
  ~173 │ SIMPLE PRESENT vs  (ders, 2,62'den; taban 212)                       │
   216 │ [YDT · BASIC] kapakta x 48 ─(2,0–2,4)→ x ≈ 670 · PRESENT CONTINUOUS   │
   354 │ TARİFE (B 190, ortalı x 216–864, kontur 12)       ← uçuşla ders 1     │ içerik 352–1392
   559 │ ~~~~~~ sarı altçizgi TARİFE altında (x 210–870)                        │
   588 │ ( ≠ PLAN ) sarı hap x 196–884, ≠ kalemle çizili    ← uçuşla ders 2     │
   876 │ The train to İzmir   Fredoka 64, x 97              → uçuşta taban 468  │
   974 │ leaves at 7  (2,20'den yazılır; uçuşla taban 566)                     │
  1080 │      leaves (Caveat 72, x≈380)                     am going (sağa 1032)│
  1100 │ (saat r72, x≈160)                [figür 600–743, 924–1384][bilet ≈ 714–870]
  1236 │ [tren 48–478, 1202–1384 → uçuşta kart köşesi 785–1000 × 392–483]       │
  1384 │ ═════ ray (tren) ═════                    figür ayağı                  │
  1456 │ The train to İzmir leaves at 7 pm today.  (Lexend 500 44)              │ altyazı 1400–1536
  1536 └ PLATFORM: öğe yok                                                      ┘
Son hal (2,92+): HUD tam · kart 1 çerçevesi 57,368 966×260 · satır 1 taban 468 · satır 2 `leaves at 7` taban 566 · tren köşede.
```

### 3.7 Ekran metni, yazı, renk (KOYU hex yaz; hf_tema temaya çevirir)
| Öğe (ID) | Metin | Yazı | Renk (hex → tema) |
|---|---|---|---|
| başlık 1 `text#bas1t` (grup `#bas1`) | `TARİFE` | Fredoka 700 B, x t1x, taban T1, `font-kerning:none`, kontur `stroke="#1b1a17"` 12, `paint-order:stroke fill` | `fill="#f3efe6"` → murekkep |
| altçizgi `path#alti` (`#bas1` içinde) | — | x: t1x − 6 → t1x + g1 + 6; ALTI_Y çevresinde ±5 px dalgalı tek kübik yol (S1 kalıbı); w 10, round cap; 0. karede opaklık 0 | `stroke="#f2a93b"` → vurgu |
| hap `rect#hap` (grup `#bas2`) | — | §3.4 | `fill="#f2a93b"` → vurguDolgu (açık `#ffe066`) |
| ≠ `g#neq` (`#bas2` içinde, 3 `path`) | — | §3.4 çizgileri; `fill="none"`, round cap; stroke ÖZNİTELİĞİ YOK, `style="stroke:var(--pilMetin)"` (sözleşme: `stroke="#1b1a17"` zemine boyanır) | pilMetin (açık `#1b2440`) |
| başlık 2 `text#bas2t` (`#bas2` içinde) | `PLAN` | Fredoka 700 B, x PX, taban T2, `font-kerning:none` | `fill="#1b1a17"` → pilMetin |
| satır 1 `g#r1 > text` | `The train to İzmir` | Fredoka 700 64, x SOL, taban R1_K, `font-kerning:none`, `clip-path="url(#cp1)"` | `#f3efe6` → murekkep |
| satır 2 `g#r2 > text` | `leaves at 7` (yalnız bu; `pm today.` sahne 02'de) | Fredoka 700 64, x SOL, taban R2_K, `clip-path="url(#cp2)"` | murekkep |
| kırpma `clipPath#cp1/#cp2 > rect#cr1/#cr2` | — | x SOL − 12, y taban − 64, h 1,35·64, width 0 | — |
| kart `g#kart > path#kc0…#kc3` | — | `kutu(57, 368, 966, 260, 71)` kenarları; w 4, round cap, `fill="none"`; 0. karede opaklık 0 | `stroke="#f3efe6"` |
| etiket `text#etk1`, `text#etk2` | `leaves`, `am going` | Caveat 700 72, §3.4 E1/E2; `stroke="none"` | `fill="#f3efe6"` |
| tren / saat / bilet / figür | — | §3.3 | §3.3 |
| künye | `Y.kunye_svg("Hook")` (`KUNYE.cipler["01-hyperframes-kapak"]` = `Hook`) | S1 ile aynı | |
| altyazı `g#altyazi` | `Y.altyazi_svg(0.0, Z["sure"], ALT)` (ALT = EKRAN dönüşümlü kopya) | Lexend 500 44 | murekkep |

Tek vurgu = altçizgi + hap + rozet + çip (aynı sarı). Kırmızı, yeşil, emoji, gradyan, gölge YOK. Ekranda `İzmir` noktalı, `7` rakam.
"kanal" sözü, QR, süre YOK.

### 3.8 SVG düzeni ve zaman çizelgesi
- Sıra (alttan üste): `g#kapak-sahne` [`g#eskiz` (`#saat`, `#bilet`, `#fig`) + `#etk1` + `#etk2`] → `#tren` → `#kart` → `#r1` → `#r2` →
  `#bas2` → `#bas1` → künye → `#altyazi`. `#eskiz`: `fill="none" stroke="#f3efe6" stroke-linecap="round" stroke-linejoin="round"`.
- 0. kare `gsap.set`: `#ku-ders` opaklık 0, `#ku-cip` opaklık 0, `#rz0` x = KENAR − rozet_konumu().x, `#alti` ve `#kc0…3` dash gizli.
  Bütün tween'ler `immediateRender: false` (`ac()`).
- Altçizgi: S1 kalıbı (`tl.set` opaklık 1 + `strokeDashoffset` 0, `sine.inOut`).
- Satır 1: `#cr1` genişliği 4 adımda; adım k genişliği = 12 + g(önek_k) + 8 (önekler `The`, `The train`, `The train to`), son adım
  12 + g(tam satır) + 12. Her adım `fromTo` önceki genişlikten, `ease: "none"`, başlangıç t0, süre min(t1 − t0, `yazi_cap`).
  Satır 2: aynı kalıp 3 adım (önekler `leaves`, `leaves at`; son `leaves at 7`).
- Uçuş: `uc2(id, o, h, hs, sol)` — S1 `uc2` + `sol` bayrağı (false ise opaklık tween'i yok). `svgOrigin` uçuştan önce bir kez `gsap.set`
  (`smoothOrigin: false`), tween'lerde YOK (S1 QA tur 3). UK = 0,85.
  o1 = (t1x + g1/2, T1 − 0,35·B), h1 = (KENAR + UK·gd1/2, dersTaban − 0,35·56 − `ucus_ayrik`), hs1 = UK·gd1 / g1;
  o2 = (540, (HAP_UST + HAP_ALT)/2), h2 = (KENAR + UK·gd2/2, dersTaban + dersSatir − 0,35·56 + `ucus_ayrik`), hs2 = UK·gd2 / hap.w;
  gd1, gd2 = g(DERS[0|1], Fredoka 700, 56). `#bas1`, `#bas2` sol = true; `#tren` o3, h3, hs3 (§3.4), sol = false.
  `#ku-ders` 0 → 1 (`kunye_ac`, `power1.out`); `#ku-cip` 0 → 1 (0,2 sn, u1 − 0,22); `#rz0` x → 0 (`rozet_kay`, `power3.inOut`);
  `#kapak-sahne` opaklık → 0 (`sahne_sol`, `power1.in`); `#r1`, `#r2` y → DY (`ucus`, `power3.inOut`).
- Kart çerçevesi: 4 kenar sırayla; kenar boyu `getTotalLength()`; süreler boy oranıyla `kart_ciz[1]`'e bölünür; her kenarda `tl.set`
  opaklık 1 + `strokeDashoffset` → 0, `ease: "none"`.
- Altyazı: S1 `V.alt.forEach` aç/kapa.

### 3.9 Denetimler (uret.py içinde assert; ihlalde dur, sabiti kendin değiştirme, ihlali yaz)
1. B ∈ [150, 190]; hap ve başlık 1 x ∈ [63, 1017]; T1 − 0,921·B ≥ 352.
2. Satır metinleri ≤ 24 karakter (`The train to İzmir`, `leaves at 7 pm today.`); SOL + g(`leaves at 7 pm today.`, 64) ≤ 57 + 966 − 40.
3. Kapak dikey (≥ 24 px ara): HAP_ALT → R1_K − 0,921·64; R1_K + 0,212·64 → min(figür üstü ZEMIN_Y − FIG_H, etiket üstü 1080 − 0,70·72,
   saat üstü SAAT_Y − 1,09·SAAT_R); etiket altı (1080 + 0,25·72) + 12 ≤ bilet üst köşesi (dönmüş 4 köşenin en küçük y'si);
   `leaves` altı + 24 ≤ tren üstü (1202).
4. Yatay (≥ 20 px): `am going` sol (1032 − g) ≥ figür sağı (FIG_X + (x1 − x0)·fs) + 20; `leaves` sağı (380 + g/2) + 20 ≤ FIG_X;
   saat sağı (SAAT_X + 1,09·SAAT_R) + 20 ≤ `leaves` sol; bilet sağı (dönmüş köşe + çentik payı yok) ≤ W − KENAR; tren sağı 478 + 20 ≤ FIG_X.
5. Son hal: kart taşma payıyla x ∈ [48, 1032], üstü ≥ 352; R1_SON − 0,921·64 ≥ 368 + 40; R2_SON + 0,48·64 + 24 ≤ 368 + 260;
   TREN_SON kutusu kart iç payı ≥ 20 (sağ 1000 ≤ 1023 − 20, üst 392 ≥ 368 + 20); TREN_SON altı 483 + 24 ≤ R2_SON − 0,75·64;
   TREN_SON solu 785 ≥ SOL + g(satır 1, 64) + 40. TREN_SON kutusu §3.4 formülünden hesaplanır (h3 + hs3·(kapak kutusu − o3)), elle yazılmaz.
6. Zaman: satır 1 son bitiş ≤ kapak_kare/30 − 1/30; satır 2 son bitiş ≤ 2,93 (2,95 karesinde `7` tam; S1 QA tur 2);
   u1 ≤ (Z.kare − 12)/30; kart_ciz bitişi ≤ 2,97.
7. Uçuş çakışma örneklemesi (S1 §4.7 kalıbı, adım 1/30, 6 px pay): t = u0 … u1. Kutular: `#bas1` [t1x, t1x + g1] × [T1 − 0,921·B, ALTI_Y + 5],
   `#bas2` hap, `#rz0` (kayan x, y 216–288), `#r1` [SOL, SOL + g(satır 1)] × [R1_K − 0,921·64, R1_K + 0,212·64] + DY·ease,
   `#r2` [SOL, SOL + g(o ana kadar açılmış önek)] × [R2_K − 0,75·64, R2_K + 0,212·64] + DY·ease (yalnız t ≥ 2,20),
   `#tren` kapak kutusu o3 çevresinde es ile ölçeklenip et ile kayar. Çiftler: bas1 × rz0, bas2 × rz0, bas2 × r1, bas1 × bas2 (S1 c4,
   T1 + 0,01·B ve T2 − 0,69·B ile), yalnız başlık opaklığı ≥ 0,5 iken (S1 sınırı); tren × r1, tren × r2, tren × rz0 bütün uçuşta;
   tren × bas1, tren × bas2 başlık opaklığı ≥ 0,5 iken. Düşerse t ve çifti yazıp dur.

### 3.10 Çıktı ve arayüz
- `uret() -> str` (index.html metni). Modül düzeyinde `Z`, `SOZ`, `EKRAN`; ayrıca `zamanlar() -> dict`:
  `{"alti": [bas, sure], "r1": [[bas, sure] ×4], "r2": [[bas, sure] ×3], "ucus": [bas, sure], "kart": [bas, sure]}` (olay.py okur:
  `r1[0]`, `r1[3]`, `r2[0]`, `kart`).
- `__main__`: `proje/` yoksa aç; `Y.font_kopyala(AD/"proje"/"assets"/"fonts")`; `proje/index.html` yaz; `D/devir.json` yaz ve tek satır
  `devir: <json>` bas. devir alanları: `font` "Fredoka", `agirlik` 700, `boy` 64, `kerning` "none", `sol` 97, `taban` [468, 566],
  `satir` ["The train to İzmir", "leaves at 7 pm today."], `gorunen` ["The train to İzmir", "leaves at 7"],
  `sozcuk` [[metin, satır, x0, x1] ×9] (tam satırlarda: x0 = SOL + g(önceki sözcükler + boşluk), x1 = x0 + g(sözcük); `pm`, `today.` dahil),
  `kart` {x 57, y 368, w 966, h 260, tohum 71, cizgi 4, bicim "kutu (ortak/kalem-canvas.js)"},
  `tren` {kutu [785, 392, 1000, 483] (hesaplanmış), olcek 0,5, yerel_kutu [−10, −24, 420, 158], tx 58, ty 1226, kaynak "trenParcalari"},
  `altyazi_ekran` EKRAN, `t` 3.0.
- Kök: `data-width="1080" data-height="1920"`, `data-duration` = Z.sure, `data-fps` 30; `#sahne` `viewBox="0 0 1080 1920"`.

## 4. Kabul ölçütü (şef koşar)
1. `cd D && /usr/bin/python3 uret.py && /usr/bin/python3 olay.py` çıkış 0; assert yok; `olaylar.json` 7 olay, hepsi kare < 90.
2. `proje/index.html`: 1080×1920; `#kunye` içinde `#ku-ders`, `#rz0`, `#ku-cip`, `#logoimg`; `#bas1`, `#bas2`, `#neq`, `#r1`, `#r2`,
   `#kapak-sahne`, `#tren`, `#tren-ic`, `#kart`, `#al0`. `#tren` öğesinde transform özniteliği yok.
3. `cd K && bash araclar/qa-yerel.sh 02-04-ydt-temel-s3 01-hyperframes-kapak 0.2,1.97,2.95 1.97 --hazirla` çıkış 0.
4. Kareler: taşma, kesik yazı, üst üste binme, okunmaz kontrast, boş kare YOK; platform bandında öğe YOK; 1,97'de satır 1 tam, çip yok,
   ders adı yok; 2,95'te kart çerçevesi, iki satır (`leaves at 7`), tren köşede, HUD tam.
