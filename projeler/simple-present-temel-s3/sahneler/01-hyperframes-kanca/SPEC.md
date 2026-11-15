# SPEC — simple-present-temel-s3 · sahne 01-hyperframes-kanca (huni v2, HyperFrames 1080×1920, 129 kare)

Kaynak: `uretim-tutanagi/istem/sahne/D-01-hyperframes-kanca.md`, `BRIEF-S3.md` ("Yerleşim", "Kanal katmanı", "Sahne içeriği"
0,00–3,89, "Kapak"), `D/.claude/docs/huni-v2-standart.md` §1, §2, §6, §7, `uretim-tutanagi/kapak-taslak.md` §2–§3. Yazan: şef (15.11.2026).
Bu belge tasarım verir; tam kod içermez. K = `/home/sef/01dev/_worktrees/kalem-0204`.
S = `K/projeler/simple-present-temel-s3/sahneler/01-hyperframes-kanca/` (bu sahne dizini). P = `K/projeler/simple-present-temel-s3/`.

## 1. Dosyalar

| Dosya | Durum | Kim |
|---|---|---|
| `S/uret.py` | YOK. Bu SPEC'e göre YAZ. | agy |
| `S/yardim.py` | VAR (emsal kopyası; `KONU = "Simple Present"`). DOKUNMA. | şef |
| `S/olay.py`, `S/calistir.sh`, `S/zamanlar.json`, `S/nesneler.json` | VAR. DOKUNMA. | şef |

Kalıp (yalnız okunur): `K/projeler/02-04-ydt-temel-s1/sahneler/01-hyperframes-kapak/uret.py` (HTML iskeleti, `ac()`, kalem darbesi
`strokeDasharray/strokeDashoffset`, `gsap.set`/`tl.*` düzeni, `_denetimler()` ve uçuş örneklemesi, `zamanlar()`, `__main__` + devir.json) ve
`K/projeler/02-04-ydt-temel-s2/sahneler/05-hyperframes-kapak-b/uret.py` (karakter: `alfa_kutusu`, `maske`, `bos_mu`, `gorsel_img`, çıkartma
kenarı `drop-shadow` zinciri `KENAR_PX` 10 / `KENAR_GECIS` 3, `<svg id="alt">` daire, `<img class="abs kenar">`). Altyazı sözcük zamanlı
açılış + karaoke çizgisi: `K/projeler/02-04-ydt-temel-s2/sahneler/01-hyperframes-kapak/uret.py` satır 432–488 ve JS "2." ile "3.".
Python: girinti 4 boşluk, satır ≤ 120, her işlevde tip ipucu, `getattr`/`hasattr` yedek dalı yok. Çalıştırma `/usr/bin/python3 uret.py`
(fontTools, PIL, numpy kullanıcı site-packages'ta; `-I` YOK). Test, render, git, betik koşma yok (şef koşar).

## 2. Girdi (uret.py okur)

| Ad | Kaynak | Değer |
|---|---|---|
| `Z` | `S/zamanlar.json` | süreler (aşağıda) |
| `SOZ` | `P/ortak/anlatim/sozcukler.json`, `cumle == 1` | `He` 1,00–1,16 · `doesn't` 1,32–1,64 · `goes.` 1,72–2,44 · `Hata` 2,69–3,01 · `nerede?` 3,09–3,89 |
| `ALT_EN`, `ALT_TR` | `P/ortak/anlatim/altyazi.json`, `cumle == 1`, `dil` en / tr | `He doesn't goes.` 1,00–2,44 · `Hata nerede?` 2,69–3,89 |
| karakter | `P/ortak/kapak/karakter.png` (896×1200 RGBA; calistir.sh `proje/assets/karakter.png`'ye kopyalar) | alfa kutusu (eşik 64) 152, 89, 744, 1113 |
| `Y` | `S/yardim.py` | `HUD`, `genislik`, `kunye_svg()`, `font_css()`, `font_kopyala()`, `zemin_html()`, `ZEMIN_CSS`, `RENK`, `W`, `H` |

Denetim (assert, metinli): `[s["sozcuk"] for s in SOZ] == ["He", "doesn't", "goes.", "Hata", "nerede?"]`; SOZ[0..2] boşlukla birleşince
`ALT_EN["metin"]` ve `KART` ile aynı; SOZ[3..4] birleşince `ALT_TR["metin"]` ile aynı. Hiçbir saniye elle yazılmaz: başlangıçlar sözcük çapasından.

## 3. Sabitler ve türetilen ölçüler (px; g(m, aile, ağırlık, boy) = `Y.genislik`)

| Ad | Değer / formül | Ölçüm (şef, 15.11) |
|---|---|---|
| KENAR, SAG, ORTA | `Y.HUD["kenar"]` 60, `Y.HUD["sagSinir"]` 960, (KENAR+SAG)/2 | 510 |
| BAS1, BAS2 | `"BU CÜMLE"`, `"YANLIŞ"` | |
| PAD, PADY | 0,20 em (hap yan payı, emsal) · 0,10 em (hap üst/alt payı) | |
| ACC, CED, CAP | 0,93 (`Ü` noktası üstü) · 0,19 (`Ç`/`Ş` çengeli altı) · 0,70 (büyük harf üstü) — em; Fredoka 700 glif sınırı ölçüldü | |
| KONTUR | 10 (başlık 1 zemin konturu; dışa 5) | |
| G1, CW | 18 (başlık 1 altı → hap çerçevesi üstü) · 5 (çerçeve kalınlığı) | |
| BAS_UST, BAS_SON | 468 (başlık 1 mürekkep üstü, kontur dahil) · 796 (çerçeve altı en çok) | |
| BANT | (BAS_SON − BAS_UST − KONTUR − G1 − CW) / (ACC + CED + PADY + CAP + CED + PADY) | 133,48 |
| B | floor(min(190, (SAG−KENAR−KONTUR)/g(BAS1,1), (SAG−KENAR)/(g(BAS2,1)+2·PAD), BANT)) — motor ölçer | **133** |
| g1, t1x | g(BAS1, Fredoka 700, B), ORTA − g1/2 | 639,2 / 190,4 |
| T1 | BAS_UST + KONTUR/2 + ACC·B | 596,7 |
| HAP_UST | T1 + CED·B + KONTUR/2 + G1 + CW/2 | 647,5 |
| T2 | HAP_UST + PADY·B + CAP·B | 753,9 |
| HAP_ALT | T2 + CED·B + PADY·B | 792,4 |
| hap | w = g(BAS2,B) + 2·PAD·B, x = ORTA − w/2, h = HAP_ALT − HAP_UST, rx = h/2 | w 501,3 · x 259,4 · h 144,9 |
| KART | `"He doesn't goes."` | 16 karakter |
| KB | 80 (Fredoka 700; alt sınır 72, küçültme YOK) | |
| KX, KY, KH, KRX | 60, 840, 160, 18 | |
| KPS, KPD | 40 (sol iç pay), 56 (sağ iç pay; `?` köşesi için) | |
| KW, KSON | KPS + g(KART, KB) + KPD, KX + KW | 677,0 / 737,0 |
| KYX, KTABAN | KX + KPS (100), KY + 108 (948) | yazı x, taban |
| KY_SON | 480 (sahne 02 kare 0; D-02 aynı sabit) → DY = KY_SON − KY = −360 | |
| KK_Y | KTABAN + 24 (karaoke çizgisi, kalınlık 6) | |
| QW, QH | 56, 100 (`?` yerel kutusu) | |
| QX, QY | KSON − 4 − QW/2, KY − 24 | 705 / 816 (kutu 705–761 × 816–916) |
| KAR_SOL | KSON + 20 + KENAR_PX (10) | 767 (alfa sol ucu) |
| KS | (SAG − KENAR_PX − 2 − KAR_SOL) / (alfa x1 − alfa x0) (2 px yuvarlama payı) | 0,3057 |
| KAR_X0, KAR_Y0 | KAR_SOL − ax0·KS, 880 − ay0·KS (dosyanın sol üstü; alfa üstü y 880) | 720,5 / 852,8 |
| DAIRE | cx = (KSON + 20 + SAG)/2, r = (SAG − (KSON + 20))/2 − 2, cy = KAR_Y0 + 470·KS (yüz ortası, PNG y 470) | 858,5 / 996,5 / 99,5 |
| boy, rz | `Y.konu_boyu()`, `Y.rozet_konumu()` | 34 / x 309,7 w 203,6 |
| ALT_Y, ALT_ORTA | 1484 (`HUD["altyaziBas"]` + 84), `HUD["altyaziOrta"]` 510 | `Hata nerede?` g 294,1 → x 363,0 |

## 4. Olay listesi (kare = round(sn × 30); küresel sn = yerel sn, t_bas 0,00)

| # | Olay | sn (kare) | Cümle sözcüğü / çapa |
|---|---|---|---|
| 1 | Kapak tam görünür: kanal katmanı, künye (konu + rozet), başlık 2 satır + sarı hap (çerçevesiz), kart, karakter + sarı daire | 0,00 (0) | söz öncesi (kapak istisnası) |
| 2 | `#cerceve` hap çerçevesi kalemle (dash, `sine.inOut`) | `Z.cerceve` 0,30–0,80 (9–24) | söz öncesi |
| 3 | KAPAK A karesi (çerçeve tam; karaoke ve `?` yok) | `Z.kapak_t` 0,90 (27) | — |
| 4 | kart karaoke `kk0` | SOZ[0] 1,00–1,16 (30–35) | He |
| 5 | kart karaoke `kk1` | SOZ[1] 1,32–1,64 (40–49) | doesn't |
| 6 | kart karaoke `kk2` | SOZ[2] 1,72–2,44 (52–73) | goes. |
| 7 | altyazı `aw0` açılır, `ak0` karaoke | aç SOZ[3].t0 − 0,05 = 2,64 · çizgi 2,69–3,01 | Hata |
| 8 | kırmızı `?`: `#soru-kanca` dash 0,34 sn (`sine.inOut`), sonra 0,04 ara, `#soru-nokta` opaklık 0→1 0,06 sn | 2,69–3,13 (81–94); toplam ≤ `Z.soru_en_cok` | Hata (2,69) |
| 9 | altyazı `aw1` açılır, `ak1` karaoke | aç 3,04 · çizgi 3,09–3,89 | nerede? |
| 10 | çıkış: `#baslik` opaklık → 0 (`Z.baslik_sol`, `power1.in`), `#soru` opaklık → 0 (`Z.soru_sol`, `power1.in`) | C0 = SOZ[4].t1 − `Z.cikis_sure` = 3,39 (102) | nerede? sonu |
| 11 | çıkış: `#kart-g` y 0 → DY (−360) (`Z.cikis_sure`, `power3.inOut`) | 3,39–3,89 (102–117) | — |
| 12 | çıkış: `#kgrup` x 0 → `Z.karakter_dx` (420), opaklık → 0 (`Z.karakter_cik`, `power2.in`) | 3,39–3,84 | — |
| 13 | altyazı kapanır (`aw*`, `ak*` kapalı) | min(ALT_TR.t1 + `Z.altyazi_kuyruk`, `Z.sure`) = 4,24 | — |
| 14 | durgun; son 12 kare geçiş altında | 3,89–4,30 (117–128) | → sahne 02 (kart y 480) |

Karaoke kapanışı (kk ve ak): min(t1, sonraki sözcük t0 − `Z.karaoke_ara`); kapı açılışı `tl.set` opaklık (emsal S2). Altyazı sözcüğü açılışı
t0 − `Z.altyazi_on`. Kanal katmanı (`#kanal`) ve künye (`#ku-konu`, `#rz0`) bütün sahne boyunca opaklık 1, konum sabit: onlara hiçbir
`gsap.set`/`tl.*` YAZMA (emsal S1'deki `#ku-konu` gizleme ve `#rz0` kaydırma bu sahnede YOK).

## 5. Yerleşim

```
y  291 ┌ [logo 53–247] @ydspublishing (Lexend 42, x 263, taban 330) — 0. kareden son kareye, hareketsiz         ┐ kanal 280–350
   386 │ Simple Present (Fredoka 34, x 60, taban 420) + [YDT · BASIC] x ≈ 310 — hareketsiz                         │ künye 360–450
   468 │ BU CÜMLE  (B ≈ 133, orta 510, zemin konturu 10)                                                         │ içerik 460–1380
   648 │ ( YANLIŞ ) sarı hap x ≈ 259–761, çerçeve 0,30–0,80 kalemle (hap kenarı üstünde, mürekkep 5)               │
   816 │                                         ? kırmızı (2,69; kutu 705–761 × 816–916, kartın sağ üst köşesi)  │
   840 │ ┌ kart x 60–737, y 840–1000, rx 18 ──────┐   (sarı daire cx 858, cy 996, r 99,5)                        │
   948 │ │ He doesn't goes.  Fredoka 700 80, x 100 │   [karakter alfa x 767–948, y 880–1193; el ucu (767, 1070)]  │
  1000 │ └─────────────────────────────────────────┘   sola karta işaret eder; 10 px krem çıkartma kenarı          │
  1484 │ Hata nerede?  Lexend 500 44, orta x 510, sözcük zamanlı + sarı karaoke çizgisi (y 1494)                   │ altyazı 1400–1550
  1570 └ boş zemin                                                                                                ┘
Son hal (3,89): kanal + künye · kart x 60, y 480–640 (yazı taban 588) · altyazı `Hata nerede?` (4,24'te kapanır).
```

## 6. Öğeler, kimlik, renk (KOYU hex yaz; `ortak/hf_tema.py` temaya çevirir)

Sıra (alttan üste): zemin (`Y.zemin_html()`) → `<div id="kgrup" class="abs">` → `<svg id="sahne">` [`#baslik` → `#kart-g` → `#kunye` →
`#altyazi`]. Karakter ve daire `#sahne` DIŞINDA (çakışma kapısı `#sahne` içini ölçer; karakter denetimi §7'deki maske denetimidir).

| Kimlik | Öğe | Ayrıntı |
|---|---|---|
| `#kgrup` | `<div class="abs" style="left:0;top:0;width:1080px;height:1920px">` | içinde `<svg id="alt" class="abs" width="1080" height="1920" viewBox="0 0 1080 1920">` + `<circle id="daire" cx cy r fill="#fece00"/>`, sonra `<img id="karakter" class="abs kenar" src="assets/karakter.png">` (S2 `gorsel_img` kalıbı: left KAR_X0, top KAR_Y0, width 896·KS, height 1200·KS) |
| `.kenar` CSS | `filter:` drop-shadow zinciri | S2 kalıbı: KENAR_GECIS 3 × 4 yön, adım 10/3 px, renk `#f3efe6` (iki temada aynı) |
| `#baslik` | `<g>` | `#bas1t`, `#hap`, `#bas2t`, `#cerceve` |
| `#bas1t` | `<text>` x t1x, y T1, Fredoka 700, size B, fill `RENK["murekkep"]`, stroke `#1b1a17`, stroke-width KONTUR, `stroke-linejoin="round"`, `style="font-kerning:none;paint-order:stroke fill"` | `BU CÜMLE` |
| `#hap` | `<rect>` hap x/y/w/h/rx, fill `RENK["vurgu"]` (`#f2a93b` → açık `vurguDolgu` `#ffe066`) | |
| `#bas2t` | `<text>` x ORTA, `text-anchor="middle"`, y T2, Fredoka 700, size B, fill `#1b1a17` (→ `pilMetin`), `font-kerning:none`; kontur YOK (emsal S1/S2 hap yazısı) | `YANLIŞ` |
| `#cerceve` | `<path>` fill none, stroke `RENK["murekkep"]`, width CW, round cap/join, `style="opacity:0"` | yol: hap kenarı üstünde hap biçimi: M(x+rx, HAP_UST) → L(x+w−rx, HAP_UST) → sağ yarım daire (iki çeyrek kübik, k = 0,5523) → L(x+rx, HAP_ALT) → sol yarım daire → L(x+rx+36, HAP_UST) (36 px el taşması). Dash JS'te `getTotalLength()` (emsal `#alti`) |
| `#kart-g` | `<g>` | `#kart-zemin`, `#kart-yazi`, `#kk0`–`#kk2`, `#soru` |
| `#kart-zemin` | `<rect>` x KX, y KY, w KW, h KH, rx KRX, stroke `RENK["murekkep"]`, stroke-width 4 | dolgu CSS ile: `#kart-zemin{fill:#fff9e6}` ve `.tema-acik #kart-zemin{fill:#fffdf6}` (kâğıt; `fill=` özniteliği YAZMA) |
| `#kart-yazi` | `<text>` x KYX, y KTABAN, Fredoka 700, size KB, fill `#1b1a17` (→ `pilMetin`), `font-kerning:none` | KART (tek öğe) |
| `#kk0`…`#kk2` | `<path>` yatay: x0 = KYX + g(önceki sözcükler + boşluk) − 2, x1 = x0 + 2 + g(sözcük, sondaki `.,?!` atılmış) + 2, y KK_Y; stroke `RENK["vurgu"]`, width 6, round cap, `style="opacity:0"` | He · doesn't · goes |
| `#soru` | `<g transform="translate(QX QY)">` | `#soru-kanca`: `<path d="M3 27 C3 11 15 2 29 2 C44 2 54 12 54 27 C54 41 44 47 35 53 C29 57 28 63 28 72" fill="none" stroke="#e0473b" stroke-width="10" stroke-linecap="round" stroke-linejoin="round" style="opacity:0">` · `#soru-nokta`: `<circle cx="28" cy="92" r="6.5" fill="#e0473b" style="opacity:0">` |
| `#kunye` | `Y.kunye_svg()` (argümansız; `#kanal` + `#logoimg` + `#kanal-yazi`, `#ku-konu`, `#rz0`) | DEĞİŞTİRME |
| `#altyazi` | `<g>` | `#aw0`, `#aw1`: `<text>` Lexend 500 44, fill `RENK["murekkep"]`, `text-anchor="start"`, x = ALT_ORTA − g(ALT_TR metni)/2 + g(önceki sözcükler + boşluk), y ALT_Y, `style="opacity:0;font-kerning:none"`; `#ak0`, `#ak1`: `<path>` y ALT_Y + 10, stroke `RENK["vurgu"]`, width 5, round cap, `style="opacity:0"`, x sözcük ±2 (noktalama hariç) |

CSS (`<style>`): `Y.font_css()`, `Y.ZEMIN_CSS`, `#sahne,#alt{position:absolute;left:0;top:0;}`, `.kenar{…}`, `#kart-zemin{…}`.
Tek vurgu sarı (hap, karaoke çizgileri; daire kapak görselinin parçasıdır, D-01 istemi). Kırmızı YALNIZ `?`. Yeşil, emoji, gradyan,
gölge YOK. Ekranda "Tam ders", "dakika", süre, QR, "izle" düğmesi YOK. Kök: `data-composition-id="main" data-start="0"
data-duration` = Z.sure, `data-fps="30" data-width="1080" data-height="1920"`; `#sahne` viewBox `0 0 1080 1920`.

## 7. Denetimler (`_denetimler()`, assert; ihlalde dur, metinde değer yaz; sabiti kendin değiştirme)

1. Başlık: 100 ≤ B ≤ 190; t1x − KONTUR/2 ≥ KENAR, t1x + g1 + KONTUR/2 ≤ SAG; hap x ≥ KENAR, x + w ≤ SAG; T1 − ACC·B − KONTUR/2 ≥ BAS_UST − 0,5;
   HAP_ALT + CW/2 ≤ BAS_SON + 0,5; T1 + CED·B + KONTUR/2 + 12 ≤ HAP_UST − CW/2.
2. Kart: len(KART) ≤ 24; KB ≥ 72; KSON ≤ SAG; KY − (HAP_ALT + CW/2) ≥ 24; yazı (KYX … KYX + g(KART, KB)) ve (KTABAN − CAP·KB … KTABAN + 0,22·KB)
   kart içinde ≥ 8 px payla; KK_Y + 3 ≤ KY + KH − 8; son hal KY_SON ≥ `HUD["icerikBas"]` + 20 ve KY_SON + KH ≤ `HUD["icerikSon"]`.
3. `?`: QY − 5 ≥ HAP_ALT + CW/2 + 12; QX ≥ KYX + g(KART, KB) + 16 (kart yazısının sağında); QX + QW + 5 ≤ SAG.
4. Karakter (S2 `maske`/`bos_mu` kalıbı; eşik 64): KS ≥ 0,25 (değilse `ValueError`, metinde KS ve KSON); maske kutusu x ≥ KSON + 20 + KENAR_PX
   − 1 ve x1 + KENAR_PX ≤ SAG, y0 ≥ KY + 20 ve y1 + KENAR_PX ≤ `HUD["icerikSon"]`; `bos_mu(maske, kart kutusu, KENAR_PX + 16)` ve
   `bos_mu(maske, ? kutusu, KENAR_PX + 16)` doğru.
5. Daire: cx − r ≥ KSON + 20; cx + r ≤ SAG; cy − r ≥ HAP_ALT + 24; cy + r ≤ `HUD["icerikSon"]`; daire merkezinin `?` kutusuna uzaklığı ≥ r + 16
   (S2 `daire_kutu_uzakligi`).
6. Altyazı: g(ALT_TR metni, Lexend 500 44) ≤ `HUD["altyaziGen"]`; ALT_Y + 0,25·44 ≤ `HUD["altyaziSon"]`; ALT_Y − 0,75·44 ≥ `HUD["altyaziBas"]`.
7. Zaman: Z.cerceve bitişi < SOZ[0].t0 − 0,1 ve ≤ Z.kapak_t − 1/30; soru toplamı (kanca + ara + nokta) ≤ Z.soru_en_cok ve bitişi ≤ SOZ[4].t1;
   C0 + Z.cikis_sure ≤ (Z.kare − 12)/30; C0 ≥ SOZ[4].t0 (çıkış `nerede?` içinde başlar); abs(Z.sure − Z.kare / 30) < 1e-6.
8. Çıkış örneklemesi: t = C0 … C0 + Z.cikis_sure, adım 1/30. Kart dy = DY·e(t) (`power3.inOut` Python karşılığı: emsal `_p3_in_out`);
   başlık ve `?` opaklığı 1 − p² (`power1.in`, p = (t − C0)/süre, [0, 1] kırpılı). Kutular: kart yazısı [KYX, KYX + g(KART)] × [KTABAN − CAP·KB,
   KTABAN + 0,22·KB] + dy; kart [KX, KSON] × [KY, KY + KH] + dy; `?` [QX − 5, QX + QW + 5] × [QY − 5, QY + 99] + dy; başlık 1 [t1x, t1x + g1] ×
   [T1 − ACC·B, T1 + CED·B]; hap [x, x + w] × [HAP_UST − CW/2, HAP_ALT + CW/2]; künye bandı [60, 960] × [360, 450]; kanal [60, 602] × [291, 341].
   Çiftler (6 px pay, kesişim yok): başlık opaklığı ≥ 0,5 iken kart yazısı × başlık 1, kart yazısı × hap; başlık ve `?` opaklığı ≥ 0,5 iken
   `?` × başlık 1, `?` × hap; bütün çıkış boyunca kart × künye bandı, kart × kanal. Düşerse t'yi ve çifti yazıp dur.

## 8. Çıktı

- `zamanlar() -> dict`: `{"cerceve": [t0, süre], "soru": [SOZ[3].t0, kanca + ara + nokta], "cikis": [C0, Z.cikis_sure],
  "karaoke": [[t0, t1] × 3]}` (olay.py `cerceve`, `soru`, `cikis` okur).
- `uret() -> str`: tam HTML. JS düzeni emsal S1: `var V = {...}` (json.dumps), `tl = gsap.timeline({paused:true})`, `ac(o)` (`immediateRender =
  false`), `#cerceve` dash hazırlığı (`getTotalLength`, emsal `#alti`), `#soru-kanca` dash hazırlığı aynı yolla, `tl.set`/`tl.to`/`tl.fromTo`,
  `window.__timelines["main"] = tl`. 0. kare `gsap.set` YOK (kanal/künye/başlık/kart/karakter ilk karede tam). `#kgrup` tween'i `x` ve
  `opacity` (div; svgOrigin yok). `#kart-g` tween'i yalnız `y`.
- `__main__`: `proje/` ve `Y.font_kopyala(AD / "proje" / "assets" / "fonts")`; `proje/index.html` yaz; `devir.json` yaz:
  `{"kart": {"x": 60, "y": KY_SON, "w": KW, "h": KH, "rx": KRX, "kenar": 4, "kenarRenk": "murekkep", "dolgu": {"koyu": "#fff9e6",
  "acik": "#fffdf6"}}, "yazi": {"metin": KART, "font": "Fredoka", "agirlik": 700, "boy": KB, "kerning": "none", "x": KYX, "taban":
  KY_SON + 108, "renk": "pilMetin"}, "sozcuk": {"He": [x0, x1], "doesn't": […], "goes.": […], "does": […], "go": […], "es": […]}, "t": SOZ[4].t1,
  "not": "huni v2 (15.11): sahne 02 kare 0 kartı; x değerleri mürekkep değil ilerleme genişliği (kerning yok)"}` (x0 = KYX + g(önek),
  x1 = x0 + g(parça); `does` = `doesn't` içindeki ilk 4 harf, `go`/`es` = `goes` içindeki parçalar; 2 ondalık). Konsola tek satır `devir: …`.

## 9. Kabul ölçütü (şef koşar)

1. `cd S && /usr/bin/python3 uret.py && /usr/bin/python3 olay.py` çıkış 0, assert yok; `olaylar.json` 4 olay, hepsi kare < 117.
2. `proje/index.html`: `#kunye` içinde `#kanal` (`#logoimg` + `#kanal-yazi`), `#ku-konu`, `#rz0`; `#kanal`, `#ku-konu`, `#rz0`'a tween YOK;
   `#altyazi` grubu var; `<circle id="daire"` ve `assets/karakter.png` `#sahne` dışında, birer kez.
3. `cd K && bash araclar/qa-yerel.sh simple-present-temel-s3 01-hyperframes-kanca 0.00,1.95,3.80 1.95 --hazirla` çıkış 0.
4. `node araclar/cakisma-kapisi.mjs simple-present-temel-s3 --sahne 01-hyperframes-kanca --port 41333 --sunucu 41022` çıkış 0, 0 uyarı.
5. Karelerde: 0–280 ve 1570–1920 boş; x 960–1080'de içerik yok; kanal katmanı her karede aynı yer ve boyda; karakter kartla çakışmıyor.
