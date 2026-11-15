uretici_model: Claude Opus 5.5 (claude-opus-5-5, şef oturumu) + ajan yok

# DUZ4-0204S2 raporu — `02-04-ydt-temel-s2` (kol a) · J3 A sınıfı düzeltmeleri ve üretilebilir kanıtlar · 16.11.2026

| Ölçüm | Değer |
|---|---|
| Düzeltilen kusur | A1 (DK-1, sahne 02 + 03), A2 (HV-20b / KS-4, başlık B), A9 (EB-1, altyazı sağ sınırı) |
| Üretilen kanıt | C1 (KS-6, 168 px), C2 (EK-8, kontak), C3 (ST-2, `hyperframes check`), C4 (HV-13, kare çifti), C5 (EK-12, zaman kapısı) |
| Ses | değişmedi: 8/8 dosya sha256 önce = sonra; yeniden sentez 0 cümle |
| Karaoke (sahne 02) | 19 kare ölçüldü, 19 karede çizgi doğru sözcüğün altında |
| Karaoke (sahne 03) | `karaoke` dizisi 0 → 8 öğe (= altyazı sözcük sayısı 8); 9 altyazılı karenin 9'unda çizgi doğru sözcükte |
| Altyazı en büyük x | sahne 02: 1015 → 910 · sahne 03: 963 → 936 (karaoke çizgisi dahil en büyük 944) |
| HV-13 (19,0 ↔ 21,0 sn, kart bölgesi) | eşiksiz fark 0 px · kanal başına > 3/255 fark 0 px |
| Çakışma kapısı | çıkış 0 (01: 13 örnek, 02: 60, 08: 23, 03: 28; çakışma yok) |
| `hyperframes check` | 7 HTML sahnesi, 7/7 çıkış 0; hata 0; uyarı yalnız craft (rozet 26 px, kapanış satırı süresi) |
| Huni kapısı | çıkış 1: 16 GEÇTİ, 2 KALDI (JR-1b beklenen, KR-1 kapı hatası), 5 ÖLÇÜLEMEDİ, 7 UYGULANMAZ |
| mp4 | yok (render koşulmadı) |
| Kol b | ayrı rapor: `../../02-04-ydt-temel-s2b/uretim-tutanagi/DUZ4-RAPOR.md` (`diff -rq` beklenmeyen 0) |

Girdi: `uretim-hatti/raporlar/J3-OZET-1611.md` §3A (A1, A2, A9, karar notları), §3C.1 (C1–C5), §3D, §5; `juri/J2-hukum-1611-0001.md`
(EB-1 dahil); `DUZ2-RAPOR.md`; `D/.claude/docs/` `huni-v2-standart.md` §2, §3, §6, `huni-ab-sozlesme.md` §4, `kapak-standardi.md`,
`juri-olcutleri.md`; skill `motion-grafik-ders` "Bağlayıcı standartlar".
Sıra: A1 kodu (kol a) → kol b kopyası → A2 metin → C1 → 03 HTML yeniden üretimi → C3 → kareler tek koşuda (02, 03 açık + koyu; 08 çifti;
koyu kontak için 01 ve 08 ek koyu kare) → ölçüm → C2 → C5 → tazelik → çakışma → huni kapısı → `surumler.json`.

## 1. Düzeltmeler

| # | J3 · jüri | Dosya | Önce → sonra | Kanıt |
|---|---|---|---|---|
| 1 | A1 · DK-1 (sahne 02) | `ortak/kunye.js`: `altyaziParca()` (yeni dışa aktarım; `altyaziMetin` onu kullanır), `altyaziCiz(ctx, metin, { alfa, sozcukler, t })`, `karaokeCiz()` | altyazı düz metin → `sozcukler` ve `t` verilirse `t0 ≤ t < t1` sözcüğünün altına çizgi. Görünüm sahne 08 karaokesiyle aynı: renk `vurgu` (açık `#d9900f`, koyu `#f2a93b`), 6 px, taban + 12 px, yuvarlak uç, 0,15 sn soldan çizilme (`power2.out`). Seçeneksiz çağrı eskisi gibi çizer; sözcük sayısı tutmazsa çizgi yok | §3 karaoke tablosu (19/19) |
| 2 | A1 · DK-1 (sahne 02) | `sahneler/02-paperjs-ornek/kalem-paper.js`: içe aktarma `altyaziParca`; `sahneKur({ …, ekSozcuk })`; `altyaziSozcuk(p)`; `kare()` çağrısı | `altyaziCiz(oc, altyaziMetin(…))` → `altyaziCiz(oc, p.metin, { sozcukler: altyaziSozcuk(p), t: tA })`. Sözcük zamanları `ortak/anlatim/sozcukler.json` (küresel sn); çizgi sonraki sözcüğün t0'ına dek kalır, son sözcükte t1 + 0,25 (sahne 08 `altyazi_svg` kuralı) | aynı |
| 3 | A1 · DK-1 (sahne 02) | `sahneler/02-paperjs-ornek/sahne-02.js` | `sahneKur(…)` → `sahneKur(…, ekSozcuk: EN2)`. Parça 3 (`She is wearing her pink T-shirt today.`, 8,37–11,17) `sozcukler.json`'da yok (el.py `T shirt`); sahnenin var olan EN2 çapası (ElevenLabs hizalaması, kart 2 karaokesi de bunu kullanır) altyazıya da girer. Çapa olmasa bu satır karaokesiz kalırdı | 9,55 · 10,1 kareleri (`pink`, `T-shirt`) |
| 4 | A9 · EB-1 (sahne 02) | `ortak/kunye.js` `KUNYE.altyaziEn: 900`, `altyaziMerkez: 510`; `altyaziCiz` ve `altyaziDilimle` genişliği 984 → 900 | satır x 48–1032 (merkez 540, en 984) → x 60–960 (merkez 510, en 900); en çok 2 satır kalır | §4 altyazı x tablosu |
| 5 | A1 · DK-1 (sahne 03) | `sahneler/03-hyperframes-cta/yardim.py`: `altyazi_svg()` üç değer döner; yeni `_altyazi_satir_svg()`, `_karaoke_svg()` (sahne 08 `yardim.py` kalıbı) | `(svg, zaman)` → `(svg, zaman, karaoke)`; satır başına `<line id="ak<i>_<j>">` (vurgu, 6 px, taban + 12) | `proje/index.html`: 8 `<line id="ak…">` + `"karaoke"` dizisi 8 öğe |
| 6 | A1 · DK-1 (sahne 03) | `sahneler/03-hyperframes-cta/uret.py` `:97`, `veri`, zaman çizelgesi | `alt_svg, alt_zaman = …` → `alt_svg, alt_zaman, karaoke_zaman = …`; `veri["karaoke"]`; `V.karaoke.forEach` (08 `index.html` kalıbı birebir: `strokeDashoffset` 0,15 sn) | aynı; 9/9 altyazılı kare |
| 7 | A9 · EB-1 (sahne 03) | `sahneler/03-hyperframes-cta/yardim.py` `HUD.altyaziMerkez 510`, `altyaziEn 900`; satır `text-anchor="start"`, x = 510 − en/2, `font-kerning:none`, `assert 60 ≤ x ∧ x + en ≤ 960` | `x="540" text-anchor="middle"`, en 984 → x 60–960 | §4 |
| 8 | A2 · HV-20b / KS-4 | `aciklama-b.md` satır 19 (YouTube başlığı) ve satır 72 (TikTok metninin soru satırı) | `Today varsa hangi zaman?` → `Today görünce hangi zamanı seçersin?` (`\| YDT İngilizce #Shorts` eki kalır) | `grep` aşağıda; kapak B değişmedi (`kapak-b.png` 15.11 23:38:00) |
| 9 | C1 · KS-6 | `kapak-a-168.png`, `kapak-b-168.png`, `kapak-c-168.png` (yeni) | yok → 168 × 299 (PIL LANCZOS, oran korunur; P3 yöntemi) | §6 |
| 10 | C3 · ST-2 | `uretim-tutanagi/hf-check-duz4.txt` (yeni) | yok → 7 HTML sahnesi | §7 |
| 11 | C2 · EK-8 | `uretim-tutanagi/kontak/02-04-ydt-temel-s2-duz4-kontak.png`, `…-duz4-kontak-koyu.png` (yeni) | yok → açık 24 kare + 5 türev, koyu 13 kare + 5 türev | §8 |
| 12 | C4 · HV-13 | `sahneler/08-hyperframes-kaydet/k/hv13/08-hyperframes-kaydet-19.png`, `-21.png` (yeni) | 22,27 geçiş karesi → 19,0 ↔ 21,0 | §5 |
| 13 | C5 · EK-12 | `uretim-tutanagi/zaman-kapisi.md` (yeni) | yok → 56 satır | §9 |
| 14 | kayıt | `surumler.json` `revizyonlar` | r1 → r1 + r2 (419 karakter, `no: "r2"`; yeni alan yok) | dosya |

A2 taraması (`grep -rn "Today varsa hangi zaman"`, iki paket, `aciklama*.md`, `surumler.json`, `BRIEF-S2.md`):

| Zaman | Satır |
|---|---|
| önce | `02-04-ydt-temel-s2/aciklama-b.md:19`, `:72` · `02-04-ydt-temel-s2b/aciklama-b.md:19`, `:72` · `02-04-ydt-temel-s2/uretim-tutanagi/aciklama-taslak.md:103`, `:140` |
| sonra | yalnız `uretim-tutanagi/aciklama-taslak.md:103`, `:140`: taslak (tarihî üretim kaydı; aynı dosyada "Tam ders süresi: 4 dakika 26 saniye" gibi yayından çıkmış satırlar var), yayın metni değil; değişmedi. `surumler.json` ve `BRIEF-S2.md` başlığı taşımaz |

İki kolda `aciklama-b.md` gövdesi aynı (satır 8'den sona, `s2b-` → `s2-` normalleştirmesiyle `diff` boş); fark yalnız üst bilgi ve `utm_content`.

## 2. Ses sha256 (önce = sonra)

Ölçüm: `sha256sum cumle-*.wav sentez.wav anlatim.*` (`ortak/anlatim/`), iş başında 01:5x ve iş sonunda 02:16. `diff` boş.

| Dosya | sha256 (ilk 16) | Değişti mi |
|---|---|---|
| `cumle-1.wav` | `0b0dafd59a9813b1` | hayır |
| `cumle-2.wav` | `1d805b981216fb41` | hayır |
| `cumle-3.wav` | `720b3d7cc5524ca8` | hayır |
| `cumle-4.wav` | `b192db36b66bd3a2` | hayır |
| `sentez.wav` | `5cc72c39c21b786a` | hayır |
| `anlatim.m4a` | `8945bfafa6043897` | hayır |
| `anlatim.m4a.imza` | `5574c4b12cb60933` | hayır |
| `anlatim.wav` | `33ae53946c6fd609` | hayır |

## 3. Karaoke tablosu

Ölçüm: altyazı bandı y 1400–1550; karaoke pikseli r > 200, 130 < g < 200, b < 120 (açık `#d9900f` ve koyu `#f2a93b` bu aralıkta).
Beklenen sözcük: kare zamanında `t0 ≤ t < sonraki t0` olan sözcük. Beklenen x: Lexend 500 44 px fontTools genişliği (kerning yok, ± 5 px),
satır merkezi 510. Ölçülen çizgi uçları yuvarlak uç payı 3 px içerir. Sahne 02 kare zamanı `sahne-kare.mjs` kuralıyla kareye iner
(t = 2,84 + ⌊(t − 2,84) · 30⌋ / 30; ör. 3,77 → 3,74). "Çizilme sürüyor" = sözcüğün ilk 0,15 sn'si (çizgi soldan uzar; 08 ile aynı).

Sahne 02 (Paper.js; 19 kare; sözcük ortası kareleri `k/karaoke/`):

| Kare | Tema | Okunan sözcük (t0–t1) | Beklenen x | Çizgi x | Çizgi y | px | Sonuç |
|---|---|---|---|---|---|---|---|
| `k/02-paperjs-ornek-2.84.png` | açık | `mı?` (2,52–2,92; kanca cümlesi kuyruğu) | 645–698 | 642–700 | 1493–1498 | 346 | doğru |
| `k/karaoke/…-3.77.png` (orta) | açık | `wears` (3,67–3,87) | 247–377 | 247–344 | 1493–1498 | 582 | doğru (çizilme sürüyor) |
| `k/ara/…-4.9.png` | açık | `winter.` (4,67–5,31) | 719–855 | 718–859 | 1493–1498 | 848 | doğru |
| `k/karaoke/…-5.76.png` (orta) | açık | `Genel` (5,56–5,96) | 216–340 | 213–342 | 1493–1498 | 772 | doğru |
| `k/karaoke/…-6.32.png` (orta) | açık | `durum:` (6,04–6,60) | 353–495 | 350–498 | 1493–1498 | 886 | doğru |
| `k/koyu/…-6.32.png` (orta) | koyu | `durum:` | 353–495 | 350–497 | 1493–1498 | 882 | doğru |
| `k/ara/…-7.6.png` | açık | `zaman.` (7,00–8,12) | 647–794 | 645–796 | 1493–1498 | 908 | doğru |
| `k/karaoke/…-9.55.png` (orta) | açık | `pink` (EN2 9,45–9,65) | 518–611 | 517–601 | 1493–1498 | 502 | doğru |
| `k/koyu/…-9.55.png` (orta) | koyu | `pink` | 518–611 | 518–601 | 1493–1498 | 496 | doğru |
| `k/02-paperjs-ornek-10.1.png` | açık | `T-shirt` (EN2 9,65–10,13) | 624–766 | 624–767 | 1493–1498 | 860 | doğru |
| `k/ara/…-12.png` | açık | `Today` (11,42–12,22) | 103–239 | 103–239 | 1465–1470 | 818 | doğru |
| `k/karaoke/…-12.62.png` (orta) | açık | `zamanda` (12,46–12,78) | 317–520 | 312–520 | 1465–1470 | 1248 | doğru |
| `k/koyu/…-13.38.png` (orta) | koyu | `geçebilir;` (13,02–13,74) | 603–791 | 598–790 | 1465–1470 | 1154 | doğru |
| `k/karaoke/…-13.92.png` (orta) | açık | `farkı` (13,78–14,06) | 816–917 | 811–914 | 1465–1470 | 616 | doğru |
| `k/ara/…-14.6.png` | açık | `yapar.` (14,51–15,10; 2. satır) | 515–644 | 514–602 | 1521–1526 | 528 | doğru (çizilme sürüyor) |
| `k/koyu/…-14.9.png` | koyu | `yapar.` (2. satır) | 515–644 | 515–648 | 1521–1526 | 798 | doğru |
| `k/ara/…-16.1.png` | açık | `anı:` (15,81–16,45) | 411–477 | 407–479 | 1493–1498 | 428 | doğru |
| `k/karaoke/…-16.13.png` (orta) | açık | `anı:` | 411–477 | 407–479 | 1493–1498 | 427 | doğru |
| `k/02-paperjs-ornek-17.35.png` | açık | `zaman.` (16,89–17,49; kare 17,31'de donar) | 669–816 | 665–817 | 1493–1498 | 906 | doğru |

Sözcük ortasına düşen kare: 10 (7 açık + 3 koyu); hepsinde çizgi pikseli > 0 ve doğru sözcükte.

Sahne 03 (HyperFrames; 11 kare; `k/karaoke/` sözcük ortası):

| Kare | Tema | Okunan sözcük (t0–t1) | Beklenen x (`<line>`) | Çizgi x | Çizgi y | px | Sonuç |
|---|---|---|---|---|---|---|---|
| `k/03-hyperframes-cta-22.75.png` | açık | — (söz 23,30'da başlar; sahne yalnız cümle 4 altyazısını taşır) | — | — | — | 0 | doğru (altyazı yok) |
| `k/karaoke/…-23.74.png` (orta) | açık | `Bitmedi,` (23,30–24,18) | 375–543 | 372–545 | 1493–1498 | 1040 | doğru |
| `k/koyu/…-23.74.png` (orta) | koyu | `Bitmedi,` | 375–543 | 372–545 | 1493–1498 | 1034 | doğru |
| `k/karaoke/…-24.5.png` (orta) | açık | `gel.` (24,26–24,74) | 568–635 | 565–637 | 1493–1498 | 428 | doğru |
| `k/karaoke/…-25.77.png` (orta) | açık | `tamamı` (25,45–26,09) | 229–396 | 226–398 | 1465–1470 | 1034 | doğru |
| `k/koyu/…-25.77.png` (orta) | koyu | `tamamı` | 229–396 | 226–398 | 1465–1470 | 1028 | doğru |
| `k/03-hyperframes-cta-26.5.png` | açık | `YDS` (26,17–26,57) | 409–500 | 406–502 | 1465–1470 | 570 | doğru |
| `k/karaoke/…-27.45.png` (orta) | açık | `YouTube` (27,29–27,61) | 751–943 | 748–944 | 1465–1470 | 1176 | doğru |
| `k/karaoke/…-28.09.png` (orta) | açık | `kanalında.` (27,69–28,49; 2. satır) | 397–613 | 394–615 | 1521–1526 | 1324 | doğru |
| `k/koyu/…-28.5.png` | koyu | `kanalında.` (son sözcük, t1 + 0,25) | 397–613 | 394–614 | 1521–1526 | 1318 | doğru |
| `k/03-hyperframes-cta-29.35.png` | açık | — (altyazı 28,76'da kapanır) | — | — | — | 0 | doğru (altyazı yok) |

`proje/index.html`: `"karaoke"` dizisi 8 öğe (`ak0_0` `Bitmedi,` 0,55–1,51 · `ak0_1` `gel.` · `ak1_0`…`ak1_5` `Dersin` … `kanalında.`), `<line id="ak…">` 8;
altyazı sözcük sayısı (`altyazi.json` cümle 4) 8. Çizgi rengi `#f2a93b`; açık temada `#root [stroke="#f2a93b"]{stroke:var(--vurgu)}` kuralıyla `#d9900f`.
Sözcük ortasına düşen kare: 7; hepsinde çizgi doğru sözcükte.

## 4. Altyazı x tablosu (y 1400–1550, mürekkep x aralığı)

| Sahne | Kare | Tema | Önce (DUZ2 karesi) | Sonra (DUZ4) |
|---|---|---|---|---|
| 02 | 12 | açık | 63–1015 | 107–910 |
| 02 | 14,6 | açık | 63–1015 | 107–910 |
| 02 | 14,9 | koyu | 63–1015 | 107–910 |
| 02 | 4,9 · 6,32 · 9,55 · 17,35 | açık | — | 159–860 · 218–801 · 109–910 · 199–822 |
| 03 | 26,5 | açık | 119–963 | 82–935 |
| 03 | 28,5 | koyu | 119–963 | 82–936 |
| 03 | 23,74 | açık / koyu | — | 379–639 / 373–639 |

En büyük x: sahne 02 910 (çizgi dahil 917 → ölçülen 914), sahne 03 936 (çizgi dahil 944). Hepsi ≤ 960; en küçük x 82 ≥ 60.
Satır sayısı en çok 2 (`Today iki zamanda da geçebilir; farkı` / `anlam yapar.` · `Dersin tamamı YDS Publishing YouTube` / `kanalında.`).
Tam boy kırpım (x 60 ve 960 kılavuz çizgisiyle) bakıldı: yazı ve çizgi iki çizginin içinde.

## 5. HV-13 kare çifti (C4)

| Ölçü | Değer |
|---|---|
| Kareler | `sahneler/08-hyperframes-kaydet/k/hv13/08-hyperframes-kaydet-19.png` (19,0 sn) · `…-21.png` (21,0 sn), açık tema |
| Bölge | x 60–960, y 560–1000 (397.341 piksel) |
| Eşiksiz fark (herhangi bir kanal > 0) | **0** |
| Kanal başına > 3/255 fark | **0** (en büyük kanal farkı 0) |
| Bölge dışı (bilgi) | 13.779 piksel > 3/255, y 1117–1498: yer imi çizimi (20,47 `kuralı`), altyazı satırı ve karaoke değişimi; beklenen |

Kart 18,4–22,15 sn sabit; `Today` hapı 22,15'te döner. Çift bu aralığın içinde ve 2 sn arayla.

## 6. 168 px kapaklar (C1)

| Dosya | Boyut | Ana yazı okunur mu (Read ile bakıldı) |
|---|---|---|
| `kapak-a-168.png` | 168 × 299 | evet: `GENEL` / `≠ ŞU AN`; çizim ve `wears` / `is wearing` seçilir |
| `kapak-b-168.png` | 168 × 299 | evet: `TODAY VARSA` / `HANGİ ZAMAN?`; karakter ve `?` seçilir |
| `kapak-c-168.png` | 168 × 299 | evet: `AYNI FİİL,` / `İKİ ZAMAN`; iki kart cümlesi küçük ama okunur |

Kanal katmanı ve künye 168 px'te okunmaz (krom; ölçüt ana yazıyı arar). Yöntem: `PIL.Image.resize((168, 299), LANCZOS)`; kaynak kök `kapak-*.png`
(15.11, değişmedi).

## 7. `hyperframes check` (C3) ve sahne 02 boyut sabitleri

Dosya: `uretim-tutanagi/hf-check-duz4.txt` (komut sahne dizininde `hyperframes check proje`; ham çıktı).

| Sahne | Çıkış | Lint / Runtime / Motion | Layout | Kontrast (WCAG AA) | Craft uyarısı |
|---|---|---|---|---|---|
| 01 | 0 | 0 hata, 0 uyarı | 0 sorun | 39/39 | `text_below_floor` 1 (rozet 26 px) · `line_unread` 6 |
| 03 | 0 | 0 / 0 | 0 | 34/34 | `text_below_floor` 1 |
| 04 | 0 | 0 / 0 | 0 | 65/65 | `text_below_floor` 1 · `line_unread` 13 |
| 05 | 0 | 0 / 0 | 0 | 30/30 | `text_below_floor` 1 · `line_unread` 6 |
| 06 | 0 | 0 / 0 | 0 | 45/45 | `text_below_floor` 1 · `line_unread` 9 |
| 07 | 0 | 0 / 0 | 0 | 65/65 | `text_below_floor` 1 · `line_unread` 13 |
| 08 | 0 | 0 / 0 | 0 | 36/36 | `text_below_floor` 1 · `line_unread` 1 (`Kaydet` 0,93 sn) |

Uyarılar düzeltilmedi (istem: B1 bekler). `text_below_floor`: rozet `YDT · TEMEL` 26 px < 28 px taban (huni §2 künye "küçük"; B1 önerisi
rozet ≥ 26 px). `line_unread`: aracın "kapanış satırı ≥ 2 sn" ölçütü; 04–07 tek karelik durağan türevdir (1,00 sn), 01 ve 08 sahne sonu
sonraki sahneye geçer. `audio_none` bilgi satırı: önizleme sessiz (ses ayrı katmanda).
Koşu her sahnenin `proje/.hyperframes/artifacts/checks/` altına bir JSON bıraktı (git dışı, kapı `.hyperframes` dizinini dışlar).

Sahne 02 (Paper.js) boyut sabitleri:

| Öğe | Kaynak | px |
|---|---|---|
| Altyazı | `ortak/kunye.js` `KUNYE.altyaziYazi` (sığmazsa 40, 36), satır `altyaziSatir` | 44 (yedek 40 / 36) · satır 56 |
| Altyazı genişlik / merkez | `KUNYE.altyaziEn` / `altyaziMerkez` | 900 / 510 |
| Kanal `@ydspublishing` | `sahne-02.js` `kanalCiz` (Lexend 700) | 42 (logo yüksekliği 48) |
| Künye konu adı | `sahne-02.js` `KONU_BOY` (Fredoka 700; 34'ten 28'e sığma döngüsü) | 34 |
| Rozet `YDT · TEMEL` | `sahne-02.js` (Lexend 700), hap yüksekliği 48 | 26 |
| v1 HUD sabitleri (`dersYazi` 56, `rozetYazi` 36, `cipYazi` 40) | `ortak/kunye.js` `KUNYE` | huni v2'de çizilmez (`kalem-paper.js` `kunyeCiz` çağırmaz) |

## 8. Kontak (C2) ve 18 klişe ön sayımı

| Sayfa | İçerik |
|---|---|
| `uretim-tutanagi/kontak/02-04-ydt-temel-s2-duz4-kontak.png` (açık, 1752 × 2180) | 01: 0 · 0,9 · 1,5 · 2,4 · 2,8 · 02: 2,84 · 3,77 · 6,32 · 9,55 · 12,62 · 14,6 · 17,35 · 08: 17,41 · 19 · 20,1 · 21 · 22,27 · 22,7 · 03: 22,75 · 23,74 · 25,77 · 26,5 · 27,45 · 29,35 · türev: kapak A/B/C, hikâye A/B |
| `…-duz4-kontak-koyu.png` (koyu, 1300 × 2180) | 01: 0,9 · 1,5 · 2,6 · 02: 6,32 · 9,55 · 13,38 · 14,9 · 08: 20,1 · 22,27 · 22,7 · 03: 23,74 · 25,77 · 28,5 · türev: 5 koyu karşılık |

Eski `kontak/s2-huni-yanyana.png` kanıt sayılmaz; taşınmadı, yerinde.
Ön sayım (kanıt jürinin sayımıdır): 17 madde 0; **#16 metin duvarı 1 işaret**. Sahne 02 son yarısında (14,6–17,35) içerik bölgesinde
(y 460–1380) aynı anda 10 yazı öbeği var: soru satırı, kart 1 (2 satır), `Simple Present`, `GENERAL`, `now`, `MEANING`, kart 2 (2 satır),
`Present Continuous`, `RIGHT NOW`, `now`. Öğeler sözle tek tek gelir, ama son karede B6 önerisindeki "≥ 5 öbek" eşiği aşılır. A listesinde
yok; dokunulmadı (şef / jüri kararı; P2 A7 ile aynı sınıf). #8 (ease, nefes) ve #11 (ses) kontaktan ölçülmez: kodda giriş `power3.out`,
önizleme sessiz. #10: karaoke sözcüğü zıplatmaz, büyütmez, rengini değiştirmez (yalnız alt çizgi).

## 9. Zaman kapısı (C5)

Dosya: `uretim-tutanagi/zaman-kapisi.md` (56 satır: kanca 0–4 sn 10, gövde 46). Kaynak: sahne 01, 03, 08 `zamanlar.json`; sahne 02 çalışma anı
`not()` kaydı (`kalem-paper.js` ZAMAN dizisi; `sahne-kare.mjs --png 0 --olc` ile son karedeki `/log` gövdesi yakalandı).

| Sınıf | Satır | Not |
|---|---|---|
| Fark ≥ 0 | 46 | öğe sözcüğüyle aynı anda ya da sonra |
| Kanca istisnası | 2 | başlık `GENEL ≠ ŞU AN` + kanca kartı (0,00) ve `≠` (0,30); ilk söz 1,00 |
| Kare yuvarlaması | 6 | fark −0,01…−0,02 sn (< 1 kare = 0,033 sn): `fr()` en yakın kareye yuvarlar |
| Yazısız kart çerçevesi | 2 | kart 1 kutusu (−0,15, kanca bandı), kart 2 kutusu (−0,33): metinsiz çerçeve; kart metni `She` ile açılır |
| **Gerçek (öğe sözden önce)** | **0** | |

## 10. Kare tazeliği

Kaynak kümesi: sahnenin `sahne-*.js`, `kalem-*.js`, `uret.py`, `yardim.py`, `proje/index.html`; `ortak/kunye.js` yalnız sahne `.js` dosyası onu
içe aktarıyorsa (sahne 02). Kareler: `k/` ve alt dizinleri (`ara`, `koyu`, `karaoke`, `hv13`).

| Sahne | Kare | En eski kare | En yeni kare | En yeni kaynak | kunye.js bağımlı | Sonuç |
|---|---|---|---|---|---|---|
| 01 | 11 | 15.11 23:38:23 | 16.11 02:05:31 | `proje/index.html` 15.11 23:36:51 | hayır | taze |
| 02 | 19 | 16.11 02:04:59 | 16.11 02:05:16 | `sahne-02.js` 16.11 01:57:20 (`kunye.js` 01:56:58) | evet | taze (bütün kareler yeni) |
| 03 | 11 | 16.11 02:05:17 | 16.11 02:05:25 | `proje/index.html` 16.11 02:01:10 | hayır | taze (bütün kareler yeni) |
| 04 | 3 | 15.11 23:37:28 | 15.11 23:37:51 | `proje/index.html` 15.11 23:37:46 | hayır | taze |
| 05 | 3 | 15.11 23:37:39 | 15.11 23:38:00 | `proje/index.html` 15.11 23:37:52 | hayır | taze |
| 06 | 3 | 15.11 23:37:45 | 15.11 23:38:05 | `proje/index.html` 15.11 23:38:01 | hayır | taze |
| 07 | 6 | 15.11 23:37:15 | 15.11 23:44:12 | `proje/index.html` 15.11 23:38:06 | hayır | taze |
| 08 | 10 | 15.11 23:38:45 | 16.11 02:05:28 | `proje/index.html` 15.11 23:36:52 | hayır | taze |

04–07'de en eski kare (`k/koyu/`) kaynaktan eskidir: durağan türev önce koyu, sonra açık çekilir; açık koşu `index.html`'i yeniden yazar
(DUZ2 akışı). Değişen sahneler (02, 03) bütün kareleriyle bu oturumda yeniden çekildi; eski kare kalmadı.
Not: `08-hyperframes-kaydet-19.png` ve `-21.png` adları aracın biçimidir (`19.0` → `19`).

## 11. Kapı çıktıları

| Kapı | Komut (çalışma dizini K) | Çıkış | Sonuç |
|---|---|---|---|
| Çakışma | `node araclar/cakisma-kapisi.mjs 02-04-ydt-temel-s2 --port 41333 --sunucu 41022 --json projeler/02-04-ydt-temel-s2/uretim-tutanagi/cakisma-DUZ4.json` | **0** (47 sn) | 4 sahne çakışma yok; `cakisma-DUZ4.json`, `.txt` |
| Huni | `node D/araclar/huni-kapi.mjs K/projeler/02-04-ydt-temel-s2` (kapı `8afc202`, 16.11 02:03) | **1** | 16 GEÇTİ, 2 KALDI, 5 ÖLÇÜLEMEDİ, 7 UYGULANMAZ; `huni-kapi-duz4.txt` |
| `hyperframes check` | §7 | 0 × 7 | hata 0 |

Huni kapısı KALDI sınıflaması:

| Madde | Sınıf | Gerekçe |
|---|---|---|
| JR-1b | gerçek, beklenen | jüri `J2-hukum-1611-0001.md` 00:03 < son içerik 02:14 (`surumler.json`). DUZ4 içeriği değiştirdi; 3. tur jüri kapatır (J3 §0 sıra 4) |
| KR-1 | **kapı hatası K7** (uygulama) | `huni-kapi.mjs:697–725`: (1) `ortak/kunye.js` zamanını her sahneye uygular; HTML sahneleri kunye.js'i içe aktarmaz (01, 03–08 `uret.py`, `yardim.py`, `index.html`: 10 satır, hepsi belge dizgisi; içe aktarma 0). (2) `yardim.py` kaynak kümesinde yok (HTML sahnelerinin asıl kaynağı). (3) yalnız `k/*.png` üst düzeyine bakar, `k/koyu`, `k/ara` sayılmaz. Kanıt: 01 @0,9 · @2,8 ve 08 @20,1 · @22,7 bu oturumda yeniden çekildi; eski karelerle kanal başına > 3/255 fark 0 piksel (08 @22,7'de 33.657 piksel ≤ 3/255 işleme gürültüsü, B8). Öneri: kunye.js yalnız içe aktaran sahnede; `yardim.py` kümeye; `k/` derinlik 2 |

HV-1s artık GEÇTİ (kapı 8/8 sahnede kanal kaynağını buldu; J2 hükmündeki HV-1s kapı hatası kapandı).

## 12. Kol b ile ilişki (AB-3, AB-8, `diff -rq`)

Ortak dosyalar önce burada düzeltildi, sonra kol b'ye kopyalandı (`sed 's#/projeler/02-04-ydt-temel-s2/#/projeler/02-04-ydt-temel-s2b/#g'`):
`ortak/kunye.js`, `02-paperjs-ornek/kalem-paper.js`, `02-paperjs-ornek/sahne-02.js`, `03-hyperframes-cta/yardim.py`. Paket adı
normalleştirilerek `diff` dördünde boş. Kol b `03-hyperframes-cta/uret.py` kendi metniyle aynı üç değişikliği aldı (değişken sahne).
`diff -rq` sınıflaması, AB-8 taraması ve kol b'de bulunan `calistir.sh` kol a yolu (düzeltildi): kol b raporu §5–§7.
Sahne 01 ve 02 kareleri iki kolda bayt aynı (`diff -rq` bu karelerin hiçbirini listelemez).

## 13. Düzeltilmeyen maddeler

| Madde | Sebep |
|---|---|
| ST-2 yazı boyutları (rozet 26 px `text_below_floor`) | istem: B1 bekler; kanıt §7 |
| EK-4 (şef gönderim satırı), EK-11 (Nadir dinlemesi) | istem: insan kanıtı; bu oturum yazmaz |
| AB-4, AB-5, AB-7 | yayın sonrası |
| EK-12 kol b `Ekran görüntüsü` açılışı | istem: B2 kararı bekler; kol b'de bilgi satırı |
| #16 metin duvarı ön sayımı (sahne 02 son yarısı, 10 öbek) | A listesinde yok; jüri sayımı ve şef kararı (§8) |
| KR-1 KALDI | kapı hatası (§11); kapı işi, üretim işi değil |
| Sahne 01 altyazı genişliği 984 (`yardim.py`) | A9 kapsamı 02 ve 03; kanca altyazısı `Genel mi, şu an mı?` x 302–718. `yardim.py` belge dizgisindeki "kunye.js altyaziCiz ile aynı kural" artık eski (kunye.js 900); kare çıktısı değişmeyeceği için dokunulmadı |
| Süre 29,41 sn > hedef 22–26 | açık nokta; ses değişmez kararı |
| EB-2 (`RIGHT NOW` etiketi) | ölçüt dışı gözlem |

## 14. Değişen ve yeni dosyalar

Kaynak: `ortak/kunye.js`, `sahneler/02-paperjs-ornek/kalem-paper.js`, `sahneler/02-paperjs-ornek/sahne-02.js`,
`sahneler/03-hyperframes-cta/yardim.py`, `sahneler/03-hyperframes-cta/uret.py`, `aciklama-b.md`, `surumler.json`.
Türetilmiş: `sahneler/03-hyperframes-cta/proje/index.html`, `zamanlar.json`, `olaylar.json`; kareler `02/k/**` (19), `03/k/**` (11),
`08/k/hv13/` (2), `08/k/koyu/08-hyperframes-kaydet-20.1.png`, `01/k/koyu/01-hyperframes-kapak-1.5.png`, `-2.6.png`; `kapak-a|b|c-168.png`.
Tutanak: `DUZ4-RAPOR.md`, `zaman-kapisi.md`, `hf-check-duz4.txt`, `cakisma-DUZ4.json`, `cakisma-DUZ4.txt`, `huni-kapi-duz4.txt`, `kontak/…-duz4-kontak(-koyu).png`.
Ana ders paketi, öteki kısalar ve `K/ortak/` değişmedi. Geçici ölçüm dosyaları: `~/Silinecekler/2026-11-16-duz4-0204S2/` (silme yok).

---
Son Güncelleme: 16.11.2026 02:2x — DUZ4-0204S2 (Opus 5.5).
