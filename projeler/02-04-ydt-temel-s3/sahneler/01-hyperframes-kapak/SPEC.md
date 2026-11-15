# SPEC v2 — 02-04-ydt-temel-s3 · sahne 01-hyperframes-kapak (kanca, HyperFrames, 1080×1920, 102 kare) · huni v2 · 15.11.2026

Yazan: şef. Bu belge tasarım verir; tam kod içermez. Bağlayıcı: `/home/sef/01dev/dijital-anlatim/.claude/docs/huni-v2-standart.md` §2, §3, §6.
K = `/home/sef/01dev/_worktrees/kalem-0204`. D = `K/projeler/02-04-ydt-temel-s3/sahneler/01-hyperframes-kapak/` (bu sahne dizini).
v1 SPEC ve kod yedeği: `/home/sef/Silinecekler/2026-11-15-huni-v2/02-04-ydt-temel-s3/sahneler-v1/01-hyperframes-kapak/`.

## 1. Dosyalar

| Dosya | Durum | İş |
|---|---|---|
| `/home/sef/01dev/_worktrees/kalem-0204/projeler/02-04-ydt-temel-s3/sahneler/01-hyperframes-kapak/uret.py` | VAR (v1, 849 satır) | YERİNDE DÜZENLE: §3 delta listesi. Yalnız bu dosya yazılır |
| `D/yardim.py` | VAR (v1 HUD) | DOKUNMA. `Y.genislik`, `Y.font_css`, `Y.font_kopyala`, `Y.ZEMIN_CSS`, `Y.zemin_html`, `Y.LOGO_EN_BOY`, `Y.LOGO_KAYMA` kullanılır. `Y.kunye_svg`, `Y.altyazi_svg`, `Y.HUD`, `Y.rozet_konumu`, `Y.DERS` ARTIK KULLANILMAZ (v1 HUD) |
| `D/olay.py` | VAR | DOKUNMA; `uret.zamanlar()` arayüzü v1 ile aynı kalır (§3.10) |
| `D/zamanlar.json` | VAR (şef v2'ye çevirdi) | DOKUNMA; §3.1 |
| `D/calistir.sh`, `D/cizim/ogretmen.json` | VAR | DOKUNMA |

Başka dosyaya dokunma. Silme yok. Test, render, git yok. Betik koşma yok (şef koşar). Python: girinti 4 boşluk, satır ≤ 120,
yeni işlevlerde tip ipucu. Çalıştırma `/usr/bin/python3 uret.py` (fontTools kullanıcı site-packages'ta; `-I` YOK).

## 2. Kalıp kaynağı

Örnek sahne = bu sahnenin v1 kodu: `D/uret.py` (yedeği yukarıdaki dizinde). Alınacak kalıp: BÜTÜN v1 yapısı korunur — kalem geometrisi
(`hash_`, `gurul`, `elips`, `kutu`, `pts_to_d`, `kutu_kenar_to_d`), çizim üreticileri (`_tren_parcalari_svg`, `_saat_svg`, `_bilet_svg`,
`_fig_svg`), `_denetimler()` iskeleti (ease işlevleri, `_kesisir`, örnekleme döngüsü), `zamanlar()`, `uret()` HTML iskeleti, `ac()`, kırpmayla
yazım (`#cr1`/`#cr2` width tween), altçizgi, kart çerçevesi çizimi, `uc2()` (svgOrigin bir kez `gsap.set`, `smoothOrigin:false`), `__main__`.
Değişen yalnız: yerleşim sabitleri, künye/kanal/altyazı (v1 HUD → v2), uçuş hedefleri ve eksen ease'leri, devir değerleri, denetimler.

## 3. `uret.py` delta listesi

### 3.1 Okuma
- `Z` = `D/zamanlar.json` (v2): fps 30, kare 102, sure 3,4, `alti` [0,30, 0,50], `yazi_cap` 0,28, `ucus` [2,00, 0,85], `ucus_olcek` 0,72,
  `sahne_sol` [2,00, 0,30], `kunye_ac` [2,62, 0,23], `baslik_sol` [2,49, 0,18], `kapak_kare` 59, `kart_ciz` [2,62, 0,28], `tren_olcek` 0,5.
  v1'deki `rozet_kay` ve `ucus_ayrik` alanları YOK; koddan da kaldır (rozet kaymaz, ayrık yok).
- `SOZ`, `EKRAN`, `ALT`, `FIG`: v1 ile aynı (sözcük zamanları dosyadan; ilk 7 sözcük assert'i kalır).

### 3.2 Kalem geometrisi ve çizim geometrisi
v1 ile birebir aynı (değişmez). Tren, saat, bilet, figür yollarının iç geometrisi aynı; yalnız yerleşim sabitleri değişir (§3.4).

### 3.3 Kaldırılanlar (v1 HUD)
`KENAR` (48), `DERS`, `ROZET` (v1 36 px), `rz_x/rz_w` (`Y.rozet_konumu`), `gd1/gd2`, `dersTaban/dersSatir`, `Y.kunye_svg("Hook")`, çip,
`#ku-ders`, `#ku-cip`, rozet kayma tween'i, `V.rz_kayma`. Üst logo (y 48–144) YOK. Ekranda "Hook" yazısı YOK.

### 3.4 Sabitler ve türetilen ölçüler (px; g(m, aile, ağırlık, boy) = `Y.genislik`)
| Ad | Değer | Not (şef ölçümü) |
|---|---|---|
| ORTA_X | 510 | içerik bandı x 60–960'ın ortası (v1 540) |
| B | floor(min(190, 900 / g(BAS1,1), 900 / (g(`= PLAN`,1) + 2·PAD))) | = 190; assert B == 190 (900 sınırı 263 / 249 verir) |
| g1, t1x | g(`TARİFE`, Fredoka 700, B), ORTA_X − g1/2 | ≈ 647,9 · 186,05 |
| T1 | 466 + 0,921·B | ≈ 640,99 (İ noktası üstü 466 ≥ 460) |
| ALTI_Y | T1 + 0,16·B | ≈ 671,39 |
| HAP_UST | ALTI_Y + 29 | ≈ 700,39 |
| T2 | HAP_UST + 0,88·B | ≈ 867,59 |
| HAP_ALT | T2 + 0,18·B | ≈ 901,79 |
| hap | w = g(`= PLAN`, B) + 2·PAD·B ≈ 688,75; x = ORTA_X − w/2 ≈ 165,63; h = HAP_ALT − HAP_UST; rx = h/2 | |
| GX, PX | hap.x + PAD·B ≈ 203,63; GX + g(`= `, B) ≈ 332,83 | ≠ çizgileri v1 em formülüyle (GX, T2, B'ye göre; değişmez) |
| SOL, KB, SATIR_ARA | 97, 64, 98 | v1 ile aynı |
| R1_K, R2_K | 986, 1084 | kapak konumu tabanları (satır 1 üstü 927 = HAP_ALT + 25) |
| R1_SON, R2_SON | 568, 666 | uçuş sonu = sahne 02 kare 0 (v1 468/566 + 100; istem sabiti) |
| DY | R1_SON − R1_K = −418 | iki satıra aynı kayma |
| ZEMIN_Y | 1376 | tren rayı + figür ayağı (ray çizgisi 4 → alt 1378 ≤ 1380) |
| TX, TY | 70, ZEMIN_Y − 158 = 1218 | tren yerel kutusu [−10, 420] × [−24, 158] → ekran [60, 490] × [1194, 1376]; tren iç ölçeği 1 |
| SAAT_X, SAAT_Y, SAAT_R | 130, 1170, 58 | ekranda ≈ 66,8–193,2 × 1106,8–1233,2 (taşma 1,09·r); vagon üstü 1263'e 30 px |
| FIG_H, FIG_X | 340, 600 | fs = FIG_H / (y1 − y0) ≈ 0,11517; figür 600–705,4 × 1036–1376; el EX, EY ≈ (695,2, 1216,3) (v1 formülü) |
| BS, egim | 0,42, −0,18 | v1 ile aynı |
| BCX, BCY | EX + BS·150, EY − 6 | ≈ (758,2, 1210,3); bilet ≈ x 678,6–837,8 (+ çentik 9) × y 1167,8–1252,8 |
| E1 (`leaves`) | x 300 `text-anchor="middle"`, taban 1196 | Caveat 700 72; ≈ 229–371 × 1146–1214; kabin üstü 1228 |
| E2 (`am going`) | x 956 `text-anchor="end"`, taban 1136 | Caveat 700 72; ≈ 739,9–956 × 1086–1154 |
| KART | `kutu(71, 472, 878, 254, 71)` | x 62–958 (titreşim ±9 + çizgi 2 ile 60–960), üst ≥ 461 |
| o3, h3, hs3 | (275, 1285) kapak kutusu merkezi · (819,5, 540,0) · `tren_olcek` 0,5 | uçuş sonu tren kutusu h3 + hs3·(kapak kutusu − o3) = [712, 494,5, 927, 585,5]; hesapla, elle yazma |
| KONU | `Simple Present vs Present Continuous` | künye satırı metni (büyük-küçük harf aynen) |
| ROZET | `YDT · BASIC` | Lexend 700 26 |
| ROZET_W | g(ROZET, Lexend 700, 26) + 40 | ≈ 203,6 (iç boşluk 20 + 20) |
| KB_K | {34, 33, …, 28} içinde 60 + g(KONU, Fredoka 700, k) + 20 + ROZET_W ≤ 960 sağlayan EN BÜYÜK k | = 34 (868,2 ≤ 960); 28'de de sığmazsa assert |
| ROZET_X | 60 + g(KONU, Fredoka 700, KB_K) + 20 | ≈ 664,6 |
| UK | 0,85 | başlık hedef genişlik payı (v1 ile aynı) |
| ga, gs, gb | g(`Simple Present vs`, KB_K), g(`Simple Present vs `, KB_K), g(`Present Continuous`, KB_K) | ≈ 264,8 · 272,5 · 294,9 |
| KONU_ORTA_Y | 420 − 0,35·KB_K | ≈ 408,1 |
| o1, h1, hs1 | (t1x + g1/2, T1 − 0,35·B) · (60 + UK·ga/2, KONU_ORTA_Y) · UK·ga / g1 | ≈ (510, 574,5) · (172,5, 408,1) · 0,3474; uçuş sonu `#bas1` konu satırının ilk yarısında (x 60–285) |
| o2, h2, hs2 | (ORTA_X, (HAP_UST + HAP_ALT)/2) · (60 + gs + UK·gb/2, KONU_ORTA_Y) · UK·gb / hap.w | ≈ (510, 801,1) · (457,9, 408,1) · 0,3639; uçuş sonu `#bas2` konu satırının ikinci yarısında (x 332,5–583) |

### 3.5 Kanal katmanı + künye + altyazı (yeni, uret.py içinde; v1 `Y.kunye_svg` / `Y.altyazi_svg` yerine)
Değerler istem ve BRIEF-S3 "Yerleşim" tablosundan; değiştirme.

| Öğe (ID) | Değer |
|---|---|
| `g#kunye` | dış grup (kapı `#kunye` içini künye sayar). İçinde sırayla `g#kanal`, `text#ku-konu`, `g#rz0` |
| `g#kanal` | `image#logoimg` `href="assets/logo.svg"` (calistir.sh tema logosunu buraya kopyalar; hf_tema `#logoimg` kimliğini arar): height 48, width = 48·`Y.LOGO_EN_BOY` (≈ 193,49), x = 60 − `Y.LOGO_KAYMA`·width (≈ 53,15), y 291 · `text#kanal-ad` `@ydspublishing`: x 263, y 330, Lexend 700 42, `fill="#f3efe6"` (→ murekkep). Hiçbir tween, set, opaklık, dönüşüm YOK (0. kareden 102. kareye sabit) |
| `text#ku-konu` | KONU: x 60, y 420, Fredoka 700 KB_K, `fill="#f3efe6"`, `style="font-kerning:none"`. 0. kare `gsap.set` opaklık 0; `kunye_ac`'ta 0 → 1 (`power1.out`) |
| `g#rz0` | `rect` x ROZET_X, y 386, w ROZET_W, h 48, rx 24, `fill="#f2a93b"` (→ vurguDolgu; açık `#ffe066`) · `text` x ROZET_X + ROZET_W/2, y 419,4, `text-anchor="middle"`, Lexend 700 26, `fill="#1b1a17"` (→ pilMetin; açık `#1b2440`). 0. kareden SON KONUMUNDA, opaklık 1, tween YOK |
| `g#altyazi` | içinde her parça `g#al<i>` (`style="opacity:0"`), aç/kapa v1 zaman kuralıyla (aç = t0 − 0,05 − t_bas, kapat = min(t1 + 0,35, sonraki t0 − 0,05) − t_bas, sure ile kırp). Satır kırma: genişlik 900, Lexend 500; boy 44, 2 satıra sığmazsa 40, sonra 36; 36'da da > 2 satır ise assert. `text-anchor="middle"`, x 510, `fill="#f3efe6"`. Taban: tek satır 1490; iki satır 1462 ve 1518. Metin EKRAN dönüşümlü `ALT` (`İzmir`, `7 pm`). Karaoke vurgusu YOK (sözcük zamanı karttaki kırpmayla verilir) |

Kanal yazısı ve logo kimliği kapıda `kunye:kanal…` adıyla görünür (`#kunye` > `#kanal`).

### 3.6 Olay listesi (kare = round(sn × 30); küresel sn = yerel sn)
| # | Olay | sn (kare) | Cümle sözcüğü |
|---|---|---|---|
| 1 | Kapak tam görünür: kanal katmanı, rozet (son konum), `TARİFE`, hap `≠ PLAN`, satır yeri boş, saat + tren, bilet tutan figür, etiketler `leaves` / `am going` | 0,00 (0) | söz öncesi |
| 2 | `TARİFE` altına sarı el altçizgisi (`strokeDashoffset`, `sine.inOut`) | `alti` 0,30–0,80 (9–24) | söz öncesi |
| 3 | altyazı dilimi açılır (cümle 1 EKRAN metni, tek satır), sahne sonuna kadar | 0,95 (29) | The − 0,05 |
| 4 | satır 1 kırpmayla sözcük sözcük: `The` · `train` · `to` · `İzmir` | 1,00–1,16 · 1,28–1,40 · 1,48–1,56 · 1,64–1,92 | The 1,00 · train 1,28 · to 1,48 · Izmir 1,64 |
| 5 | KAPAK A KARESİ: uçuş öncesi, konu adı yok, satır 1 tam, altçizgi tam | 1,97 (59) | — |
| 6 | `#kapak-sahne` (saat, bilet, figür, etiketler) solar (`power1.in`) | `sahne_sol` 2,00–2,30 (60–69) | — |
| 7 | uçuş: `#bas1` → konu ilk yarısı, `#bas2` → konu ikinci yarısı; `#tren` küçülerek kart 1 sağ üst köşesine; `#r1`, `#r2` DY yukarı | `ucus` 2,00–2,85 (60–85) | — |
| 8 | satır 2 sözcük sözcük: `leaves` · `at` · `7` | 2,20–2,44 · 2,56–2,68 · 2,80–2,92 | leaves 2,20 · at 2,56 · seven 2,80 |
| 9 | başlıklar solar (`baslik_sol` 2,49–2,67, `power1.in`); konu adı açılır (`kunye_ac` 2,62–2,85) | 2,49–2,85 | — |
| 10 | kart 1 çerçevesi 4 kenar sırayla (süre kenar boyuyla orantılı) | `kart_ciz` 2,62–2,90 (79–87) | — |
| 11 | durgun; son 12 kare geçiş altında | 2,92–3,40 (88–101) | `p.m.` 3,00 → sahne 02 |

Kanal katmanı her satırda görünür; hiçbir olay ona dokunmaz.

### 3.7 Uçuş (eksen ease'leri; şef ölçümü: tek ease ile `#bas1 × #bas2` 2,47–2,53'te, `#tren × #r1` 2,50'de çakışıyordu)
- `uc2(id, o, h, hs, sol, ex, ey)`: v1 `uc2` + eksen başına ease. x tween ease `ex`, y tween ease `ey`, ikisi de süre `ud`, başlangıç `u0`;
  scale `power3.out`, süre `Z.ucus_olcek`; `sol` true ise opaklık 0'a (`baslik_sol`, `power1.in`). `svgOrigin` uçuştan önce bir kez `gsap.set`.
- `#bas1`: ex `power3.out`, ey `power3.inOut`, sol true. `#bas2`: ex/ey `power3.inOut`, sol true. `#tren`: ex `power3.inOut`, ey
  `power2.inOut`, sol false (opaklık değişmez). `#r1`, `#r2`: y → DY, `power3.inOut`, süre `ud`.
- `#tren` dış grubunda transform özniteliği OLMAZ; yerleştirme içteki `g#tren-ic transform="translate(70 1218)"` (v1 kuralı).

### 3.8 SVG düzeni (alttan üste) ve renk
`g#kapak-sahne` [`g#eskiz` (`#saat`, `#bilet`, `#fig`) + `#etk1` + `#etk2`] → `#tren` → `#kart` → `#r1` → `#r2` → `#bas2` → `#bas1` →
`g#kunye` (§3.5) → `g#altyazi`. Renkler v1 gibi KOYU hex (hf_tema temaya çevirir): murekkep `#f3efe6`, ikincil `#c9c2b3`, vurgu
`#f2a93b` (altçizgi stroke; hap ve rozet rect fill → vurguDolgu), hap/rozet yazısı `fill="#1b1a17"` (→ pilMetin), `≠` çizgileri
`style="stroke:var(--pilMetin)"` (stroke özniteliği yok), `TARİFE` konturu `stroke="#1b1a17"` 12 `paint-order:stroke fill`.
Tek vurgu = altçizgi + hap (rozet künye öğesidir). Kırmızı, yeşil, emoji, gradyan, gölge YOK. Ekranda `İzmir` noktalı, `7` rakam.
"Tam ders", "dakika", süre sözü, QR, "izle" düğmesi, "Hook" YOK.

### 3.9 Yerleşim (kapak karesi ve son hal)
```
y   0–280  boş zemin
  291–339  [logo 53,2–246,6] @ydspublishing (x 263, taban 330)                 kanal: 0→102 sabit
  360–450  künye: (kapakta yalnız rozet)            [YDT · BASIC] x 664,6–868,2 · y 386–434
  466–641  TARİFE (B 190, ortası 510, x 186–834, kontur 12)      → uçuşla konu ilk yarısı (x 60–285)
     671   ~~~~ sarı altçizgi (x 180–840)
  700–902  ( ≠ PLAN ) hap x 165,6–854,4                           → uçuşla konu ikinci yarısı (x 332–583)
  927–1000 The train to İzmir   Fredoka 64, x 97, taban 986      → taban 568
 1036–1098 (boş: satır 2 `leaves at 7` 2,20'den yazılır, taban 1084 → 666)
 1036–1376 saat (66–193 × 1107–1233) · leaves (229–371, taban 1196) · tren 60–490 × 1194–1376 |
           figür 600–705 × 1036–1376 · am going (740–956, taban 1136) · bilet 679–847 × 1168–1253
 1400–1550 altyazı: The train to İzmir leaves at 7 pm today. (Lexend 500 44, orta 510, taban 1490)
 1570–1920 boş zemin
Son hal (2,92+): kanal · künye `Simple Present vs Present Continuous` (34) + rozet · kart 71,472 878×254 · satır 1 taban 568 ·
satır 2 `leaves at 7` taban 666 · tren [712, 494,5, 927, 585,5] · altyazı.
```

### 3.10 Denetimler (`_denetimler()`; assert, ihlalde dur, sabiti kendin değiştirme, ihlali mesaja yaz)
1. B == 190; hap ve başlık 1 x ∈ [60, 960]; T1 − 0,921·B ≥ 460; KB_K ∈ [28, 34] ve ROZET_X + ROZET_W ≤ 960.
2. Satır metinleri ≤ 24 karakter; SOL + g(`leaves at 7 pm today.`, 64) ≤ 71 + 878 − 26.
3. Kapak dikey (≥ 24 px): HAP_ALT → R1_K − 0,921·64; R1_K + 0,212·64 → min(figür üstü ZEMIN_Y − FIG_H, E2 üstü 1136 − 0,70·72).
   Satır 2 yeri (≥ 6 px): R2_K + 0,212·64 + 6 ≤ min(saat üstü SAAT_Y − 1,09·SAAT_R, E1 üstü 1196 − 0,70·72).
   E2 altı (1136 + 0,25·72) + 12 ≤ bilet üstü (dönmüş 4 köşenin en küçük y'si). E1 altı (1196 + 0,25·72) + 12 ≤ kabin üstü TY + 10.
   saat altı + 20 ≤ vagon üstü TY + 45. ZEMIN_Y + 2 ≤ 1380.
4. Yatay (≥ 20 px): E2 sol (956 − g) ≥ figür sağı + 20; saat sağı + 20 ≤ E1 sol (300 − g/2); E1 sağı + 20 ≤ duman solu TX + 334;
   tren sağı TX + 420 + 20 ≤ FIG_X; bilet sağı (dönmüş köşe) + 9,24 ≤ 960; E2 sağı 956 ≤ 960; saat solu ≥ 60; tren solu TX − 10 ≥ 60.
5. Son hal: kart titreşim + çizgi payıyla (x − 11, x + w + 11) ⊂ [60, 960], y − 11 ≥ 460; R1_SON − 0,921·64 ≥ 472 + 30;
   R2_SON + 0,48·64 + 20 ≤ 472 + 254; tren son kutusu kart içinde ≥ 20 px (sağ ≤ 71 + 878 − 20, üst ≥ 472 + 20);
   tren son altı + 24 ≤ R2_SON − 0,75·64; tren son solu ≥ SOL + g(satır 1, 64) + 40; rozet altı 434 + 20 ≤ kart üstü 472 − 11.
6. Zaman: satır 1 son bitiş ≤ kapak_kare/30 − 1/30; satır 2 son bitiş ≤ 2,93; u1 ≤ (Z.kare − 12)/30; kart_ciz bitişi ≤ 2,97;
   başlık opaklığı 0,5'in altına iner (baslik_sol[0] + 0,71·baslik_sol[1]) < konu opaklığı 0,5'i geçer (kunye_ac[0] + 0,29·kunye_ac[1]).
7. Uçuş çakışma örneklemesi (adım 1/30, t = u0 … u1, 6 px pay; v1 `_kesisir`). Ease işlevleri: power3.inOut (v1), power3.out (v1),
   power2.inOut (p < 0,5 ise 4p³, değilse 1 − 4(1 − p)³). Kutular: `#bas1` [t1x, t1x + g1] × [T1 − 0,921·B, ALTI_Y + 5] (o1 çevresinde
   ölçek es, x kayması ex ile, y kayması ey ile), `#bas2` hap kutusu (o2), `#rz0` [ROZET_X, ROZET_X + ROZET_W] × [386, 434] (sabit),
   `#kanal` [53, 602] × [291, 339] (sabit), `#r1` [SOL, SOL + g(satır 1)] × [R1_K − 0,921·64, R1_K + 0,212·64] + DY·et,
   `#r2` [SOL, SOL + g(o ana kadar açılmış önek)] × [R2_K − 0,75·64, R2_K + 0,212·64] + DY·et (yalnız t ≥ 2,20),
   `#tren` kapak kutusu [60, 490] × [1194, 1376] o3 çevresinde es ile ölçeklenip x'te power3.inOut, y'de power2.inOut ile kayar.
   Çiftler: başlık opaklığı ≥ 0,5 iken bas1 × rz0, bas2 × rz0, bas1 × kanal, bas2 × kanal, bas2 × r1, bas1 × r1, bas1 × bas2 (tam kutu),
   tren × bas1, tren × bas2; bütün uçuşta tren × r1, tren × r2, tren × rz0. Düşerse t ve çifti yazıp dur.
   (Şef benzetimi: bu parametrelerle hiçbir çift düşmez; en dar aralık bas1 × bas2 24 px, tren × r1 23,6 px.)

### 3.11 Çıktı ve arayüz
- `uret() -> str` (index.html). Modül düzeyinde `Z`, `SOZ`, `EKRAN`; `zamanlar() -> dict` v1 ile AYNI şema
  (`alti`, `r1` ×4, `r2` ×3, `ucus`, `kart`); olay.py değişmez.
- `V` (sayfa verisi): v1 alanları − `rz_kayma`; + `ex`/`ey` ease adları ya da uc2 çağrısında sabit dizgeler. `gsap.set("#ku-konu",{opacity:0})`;
  `#ku-ders`/`#ku-cip`/`#rz0` set'leri YOK.
- Kök: `data-width="1080" data-height="1920"`, `data-duration` = Z.sure, `data-fps` 30, `data-composition-id="main"`; `#sahne`
  `viewBox="0 0 1080 1920"`; `window.__timelines["main"] = tl`.
- `__main__`: `proje/` yoksa aç; `Y.font_kopyala(AD/"proje"/"assets"/"fonts")`; `proje/index.html` yaz; `D/devir.json` yaz ve tek satır
  `devir: <json>` bas. devir alanları: `font` "Fredoka", `agirlik` 700, `boy` 64, `kerning` "none", `sol` 97, `taban` [568, 666],
  `satir` ["The train to İzmir", "leaves at 7 pm today."], `gorunen` ["The train to İzmir", "leaves at 7"], `sozcuk` (v1 kuralı, 9 sözcük),
  `kart` {x 71, y 472, w 878, h 254, tohum 71, cizgi 4, bicim "kutu (ortak/kalem-canvas.js)"},
  `tren` {kutu (hesaplanmış, tamsayıya yuvarla), olcek 0,5, yerel_kutu [−10, −24, 420, 158], tx 70, ty 1218, kaynak "trenParcalari"},
  `kanal` {logo [x, y, w, h] (2 ondalık), yazi "@ydspublishing", yazi_x 263, yazi_taban 330, font "Lexend 700 42"},
  `kunye` {konu KONU, boy KB_K, taban 420, rozet [ROZET_X, 386, ROZET_W, 48] (1 ondalık)},
  `altyazi` {x 510, boy (seçilen), taban [1490] ya da [1462, 1518]}, `altyazi_ekran` EKRAN, `t` 3.0.

## 4. Kabul ölçütü (şef koşar)
1. `cd D && /usr/bin/python3 uret.py && /usr/bin/python3 olay.py` çıkış 0; assert yok; `olaylar.json` 7 olay, hepsi kare < 90.
2. `proje/index.html`: 1080×1920; `#kunye` içinde `#kanal` (`#logoimg`, `#kanal-ad`), `#ku-konu`, `#rz0`; `#ku-ders`, `#ku-cip`, "Hook" YOK;
   `#bas1`, `#bas2`, `#neq`, `#r1`, `#r2`, `#kapak-sahne`, `#tren`, `#tren-ic`, `#kart`, `#altyazi`, `#al0`. `#tren`'de transform özniteliği yok;
   `#kanal` hiçbir tween/set hedefinde geçmez.
3. `cd K && bash araclar/qa-yerel.sh 02-04-ydt-temel-s3 01-hyperframes-kapak 0.0,1.5,2.97 1.97 --hazirla` çıkış 0.
4. Çakışma kapısı 0 uyarı. Kareler: 0–280 ve 1570–1920 boş; içerik x ≤ 960; kanal katmanı dört karede aynı yerde; 1,97'de konu adı yok,
   satır 1 tam; 2,97'de künye satırı, kart çerçevesi, `leaves at 7`, tren köşede.
