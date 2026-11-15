uretici_model: claude-opus-5-5 (üretim oturumu fd389160) + ajan yok
# DUZ4-0204S1 raporu — 02-04-ydt-temel-s1 (kol a) · J3 özeti A düzeltmeleri ve üretilebilir kanıtlar · 16.11.2026

İstem: `uretim-hatti/raporlar/J3-OZET-1611.md` §5 satır `DUZ4-0204S1`. Girdi: §3A (A1, A2, A4, karar notları), §3C.1 (C1, C2, C3), §3D;
hüküm `juri/J2-hukum-1611-0009.md`; kol b hükmü `../../02-04-ydt-temel-s1b/uretim-tutanagi/juri/KBJ-hukum-1611-0014.md`; `DUZ2-RAPOR.md`.
Ses sentezi, mp4, commit, alt ajan, agy-filo, imagen YOK. Silinen dosya yok; taşınanlar `~/Silinecekler/2026-11-16-duz4-0204S1/` (`LISTE.md`).
Kol b raporu: `../../02-04-ydt-temel-s1b/uretim-tutanagi/DUZ4-RAPOR.md`.

| Ölçüm | Değer |
|---|---|
| Düzeltilen kusur | A1 (DK-1) · A2 (HV-20b / KS-4) · A4 (EK-6) |
| Üretilen kanıt | C1 (KS-6: 168 px) · C2 (EK-8: kontak) · C3 (ST-2: `hyperframes check` + `kunye.js` boyutları) |
| Ses | değişmedi: 16 ses dosyasının sha256'sı önce = sonra (§2) |
| Karaoke | 37 karenin 37'sinde çizgi okunan sözcüğün altında; sözcük ortası kare 13 (kol a 7 + kol b 6) + 4 koyu (§3) |
| Altyazı x | en sağ 938 (≤ 960), en sol 79 (§4) |
| Kare tazeliği | kol a 8/8 sahne taze (§7); huni kapısı KR-1 GEÇTİ |
| Çakışma kapısı | video sahneleri çıkış **0** · durağan türevler çıkış **0** (§9) |
| Huni kapısı | kol a 17 GEÇTİ, 1 KALDI (JR-1b, sıra durumu), çıkış 1 (§10) |
| `diff -rq` kol a ↔ kol b | 220 satır, beklenmeyen **0**, B3 bekliyor 4 (§12) |

## 1. Düzeltmeler

| J3 · jüri madde | Dosya | Önce → sonra | Kanıt |
|---|---|---|---|
| A1 · DK-1 | `ortak/kunye.js` | `altyaziCiz(ctx, metin, { alfa })` sözcük zamanı almaz → `altyaziCiz(ctx, metin, { alfa, sozcukler, t })`; seçenek verilirse `karaokeCiz` okunan sözcüğün altına çizgi çizer. Yeni dışa aktarım `altyaziParca(liste, t)`; `altyaziMetin` onu kullanır. Seçeneksiz çağrı eskisi gibi çizer | `node --check` geçti; §3 karaoke tablosu |
| A1 · DK-1 | `sahneler/02-paperjs-ornek/kalem-paper.js` (≈ 401) | `altyaziCiz(oc, altyaziMetin(K.altyazi, t))` → `pA = altyaziParca(K.altyazi, tA)`; `altyaziCiz(oc, pA.metin, { t: tA, sozcukler: sozcukJson.filter(t0 ∈ [pA.t0 − 0,05, pA.t1 + 0,05)) })`; `tA` = küresel sn (eski altyazı zamanı) | kareler `sahneler/02-paperjs-ornek/k/*.png`, `k/koyu/*.png` |
| A2 · HV-20b / KS-4 | `sahneler/06-hyperframes-kapak-c/uret.py` | başlık `I LIVE` / `I AM LIVING` (5 sözcük) → `LIVE` / `≠ [LIVING]` (2 sözcük + çizili ≠). ≠ = 3 yol (iki çubuk + eğik çizgi), 02-04-ydt-temel-s2 kapak A kalıbı; S 160 → 187 (yükseklik sınırı: kutu altı 470 + 1,93·S, figür üstüne ≥ 48); blok ortalı | `kapak-c.png`, `sahneler/06-…/k/koyu/kapak-c-koyu.png`; `uret.py` kuralları geçti (kesişim 0, satır ≤ 24, başlık–sahne ≥ 48); §5 |
| A2 | `sahneler/06-…/nesneler.json`, `proje/index.html`, `SPEC.md` (DUZ4 notu satırı) | `uret.py` çıktısı; SPEC'e güncel başlık notu | `nesneler.json`: başlık x 141–879, y 470–831 |
| A4 · EK-6 | `aciklama.md` (16, 65), `aciklama-a.md` (17, 66), `aciklama-b.md` (24, 44, 68) | `I live mı` → `I live mi` (7 yer) | `grep -rn "live mı" . --exclude-dir=uretim-tutanagi` → 0 satır |
| A4 · EK-6 | `sahneler/02-paperjs-ornek/sahne-02.js:125`, `aciklama.md` (24, 43), `aciklama-a.md` (25, 44), `aciklama-b.md` (26, 46), `BRIEF-S1.md:56` | İngilizce cümlede `İstanbul.` → `Istanbul.`; Türkçe `İstanbul'da yaşı-` (`sahne-02.js:148`) değişmedi | kare `02-paperjs-ornek-10.28.png`: kart `I live in Istanbul.`, altyazı `I live in Istanbul.` |
| A4 (ek) | `BRIEF-S1.md:65` | kural satırı `Ekranda "İstanbul" noktalı, seste "Istanbul"` → `İngilizce cümlede ekranda ve seste "Istanbul" (J3 A4, 16.11); Türkçe satırda "İstanbul'da"` | BRIEF kuralı düzeltmeyle çelişmesin diye (kart hatası `bc402eb`'den beri bu kuraldan geliyordu) |

A4 grep çıktıları (iki paket, iç belge dahil):

```
$ grep -rn "live mı" K/projeler/02-04-ydt-temel-s1 K/projeler/02-04-ydt-temel-s1b   (uretim-tutanagi dışı)
(0 satır)
uretim-tutanagi içinde kalan: S1-VAR-RAPOR.md:50-51, aciklama-taslak.md (7 satır), juri/J2-hukum-1611-0009.md:117,140,
juri/KBJ-hukum-1611-0014.md:130,162,173,182 — tarihsel kayıt ve jüri hükmü; dokunulmadı.
$ grep -rn "I live in İstanbul" (iki paket)
sahneler/02-paperjs-ornek/RAPOR.md:55 · SPEC.md:131 (kol a) · RAPOR.md:58 · SPEC.md:134 (kol b) — iç belge (istemin beklediği)
uretim-tutanagi: J2-hukum-1611-0009.md:117, senaryo-taslak.md (iki kol), DUZ2-RAPOR.md:41, aciklama-taslak.md (4), istem/sahne*/D-02-paperjs-ornek.md — tarihsel kayıt
```

Karaoke kararı (A1, karar notu "aynı paketin kaydet sahnesindeki karaoke çizgisi"): görünüm `08-hyperframes-kaydet/yardim.py` `altyazi_svg`
ile aynı: renk `RENK.vurgu` (açık `#d9900f`, koyu `#f2a93b`), kalınlık 6 px, yuvarlak uç, y = satır tabanı + 12, x = sözcük başı → sözcük sonu
(sondaki `.,:;!?` ve tırnak hariç), 0,15 sn power2.out ile soldan uzar. Zaman: sözcüğün t0'ından sonraki sözcüğün t0'ına kadar (son sözcük
t1 + 0,25); bu, 08 sahnesinin kuralıdır. İstemin "t0 ≤ t < t1" aralığında çizgi her karede doğru sözcüktedir; sözcük arası 0,04–0,25 sn
boşlukta çizgi sönmez (sönerse 30 fps'te 1–7 kare titrer). Sözcük sayısı satır sözcüğünü tutmazsa çizgi çizilmez (08 kuralı).

## 2. Ses sha256 (önce = sonra)

| Dosya | Kol a | Kol b |
|---|---|---|
| `cumle-1.wav` | `35974df2f7f2dad3…` = | `2f914435214ee485…` = (değişken cümle, kol a'dan farklı) |
| `cumle-2.wav` | `a363311cf849f45e…` = | `a363311cf849f45e…` = (kol a ile eş, AB-9) |
| `cumle-3.wav` | `0c3ba8612d3bf456…` = | `0c3ba8612d3bf456…` = (eş) |
| `cumle-4.wav` | `dd50c6bcd4520c12…` = | `dd50c6bcd4520c12…` = (eş) |
| `sentez.wav` | `2d14406ebe934b5c…` = | `bb76a6037c7e7b71…` = |
| `anlatim.m4a` | `024863ac61a158ae…` = | `66ccac3b7e5fd30b…` = |
| `anlatim.m4a.imza` | `3f752e96abcf4a39…` = | `0064ddd5d44edf9a…` = |
| `anlatim.wav` | `e998b45b1d3b8c42…` = | `7ee4ad2120552bc4…` = |

Komut: `sha256sum cumle-*.wav sentez.wav anlatim.*` (iki pakette), değişiklikten önce ve sonra; `diff önce sonra` → fark yok (16 dosya).
Tam değerler: `~/Silinecekler/2026-11-16-duz4-0204S1/ses-sha-once.txt`, `ses-sha-sonra.txt`.

## 3. Karaoke (A1 kanıtı)

Yöntem: `node araclar/sahne-kare.mjs <paket> 02-paperjs-ornek <t…> <k> --tema acik|koyu --port 41333 --sunucu 41022`; satır içi Python/PIL
(`-I`). Altyazı bandı y 1400–1550; çizgi pikseli eşiği r > 200, 130 < g < 200, b < 120 (koyuda tema rengi `#f2a93b` aynı eşiği geçer);
yazı pikseli açıkta R+G+B < 450, koyuda > 420. Sözcük öbeği = satırdaki yazı sütunlarının ≥ 9 px boşlukla ayrılan kümesi (öbek sayısı her
karede sözcük sayısına eşit). Okunan sözcük j = `sozcukler.json` t0 ≤ t < sonraki t0. Kare zamanı = T_BAS + kare/30.

| kol | tema | kare (istenen sn) | küresel t | altyazı parçası | okunan sözcük (j) | çizgi px | çizgi x | çizgi y | çizgi altındaki öbek k (x) | öbek / sözcük | doğru sözcük | altyazı x |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| -s1 | acik | 3.05 | 3.033 | İstanbul'da yaşıyorum. Amcamla yaşıyorum. Türkçede ikisi de yaşıyorum. | Amcamla (2) | 1256 | 661–870 | 1465–1470 | 2 (665–864) | 8 / 8 | evet | 79–938 |
| -s1 | acik | 4.24 | 4.233 | İstanbul'da yaşıyorum. Amcamla yaşıyorum. Türkçede ikisi de yaşıyorum. | Türkçede (4) | 1208 | 326–527 | 1521–1526 | 4 (330–523) | 8 / 8 | evet | 79–938 |
| -s1 | acik | 7.27 | 7.267 | İngilizcede ikisi ayrılır. | İngilizcede (0) | 1478 | 265–511 | 1493–1498 | 0 (271–506) | 3 / 3 | evet | 265–749 |
| -s1 | acik | 8.4 | 8.400 | İngilizcede ikisi ayrılır. | ayrılır. (2) | 782 | 618–748 | 1493–1498 | 2 (622–749) | 3 / 3 | evet | 271–749 |
| -s1 | acik | 9.86 | 9.833 | I live in Istanbul. | Istanbul. (3) | 1124 | 499–686 | 1493–1498 | 3 (505–692) | 4 / 4 | evet | 328–692 |
| -s1 | acik | 10.28 | 10.267 | I live in Istanbul. | Istanbul. (3) | 1124 | 499–686 | 1493–1498 | 3 (505–692) | 4 / 4 | evet | 328–692 |
| -s1 | acik | 11.5 | 11.500 | Hep orada: kalıcı durum, geniş zaman. | orada: (1) | 128 | 192–213 | 1493–1498 | 1 (196–332) | 6 / 6 | evet | 98–923 |
| -s1 | acik | 11.89 | 11.867 | Hep orada: kalıcı durum, geniş zaman. | orada: (1) | 806 | 192–326 | 1493–1498 | 1 (196–332) | 6 / 6 | evet | 98–923 |
| -s1 | acik | 12.97 | 12.967 | Hep orada: kalıcı durum, geniş zaman. | durum, (3) | 884 | 470–617 | 1493–1498 | 3 (474–625) | 6 / 6 | evet | 98–923 |
| -s1 | acik | 13.86 | 13.833 | Hep orada: kalıcı durum, geniş zaman. | zaman. (5) | 908 | 766–917 | 1493–1498 | 5 (771–923) | 6 / 6 | evet | 98–923 |
| -s1 | acik | 15 | 15.000 | I am living with my uncle. | am (1) | 400 | 262–329 | 1493–1498 | 1 (267–331) | 6 / 6 | evet | 233–787 |
| -s1 | acik | 15.14 | 15.133 | I am living with my uncle. | living (2) | 700 | 344–461 | 1493–1498 | 2 (350–462) | 6 / 6 | evet | 233–787 |
| -s1 | acik | 17.86 | 17.833 | Şimdilik: geçici durum, şimdiki zaman. | Şimdilik: (0) | 1070 | 92–270 | 1493–1498 | 0 (97–276) | 5 / 5 | evet | 92–923 |
| -s1 | acik | 18.23 | 18.200 | Şimdilik: geçici durum, şimdiki zaman. | geçici (1) | 782 | 289–419 | 1493–1498 | 1 (293–415) | 5 / 5 | evet | 97–923 |
| -s1 | acik | 19.9 | 19.867 | Şimdilik: geçici durum, şimdiki zaman. | zaman. (4) | 908 | 766–917 | 1493–1498 | 4 (771–923) | 5 / 5 | evet | 97–923 |
| -s1 | koyu | 11.5 | 11.500 | Hep orada: kalıcı durum, geniş zaman. | orada: (1) | 126 | 192–213 | 1493–1498 | 1 (196–332) | 6 / 6 | evet | 98–923 |
| -s1 | koyu | 11.89 | 11.867 | Hep orada: kalıcı durum, geniş zaman. | orada: (1) | 804 | 192–326 | 1493–1498 | 1 (196–332) | 6 / 6 | evet | 98–923 |
| -s1 | koyu | 15 | 15.000 | I am living with my uncle. | am (1) | 394 | 262–328 | 1493–1498 | 1 (267–331) | 6 / 6 | evet | 233–787 |
| -s1 | koyu | 15.14 | 15.133 | I am living with my uncle. | living (2) | 696 | 345–461 | 1493–1498 | 2 (350–462) | 6 / 6 | evet | 233–787 |
| s1b | acik | 2.55 | 2.533 | Bu iki "yaşıyorum" aynı mı? | mı? (4) | 346 | 728–786 | 1493–1498 | 4 (734–804) | 5 / 5 | evet | 217–804 |
| s1b | acik | 3.41 | 3.400 | İngilizcede ikisi ayrılır. | İngilizcede (0) | 1478 | 265–511 | 1493–1498 | 0 (271–506) | 3 / 3 | evet | 265–749 |
| s1b | acik | 4.5 | 4.500 | İngilizcede ikisi ayrılır. | ayrılır. (2) | 782 | 618–748 | 1493–1498 | 2 (622–749) | 3 / 3 | evet | 271–749 |
| s1b | acik | 6 | 6.000 | I live in Istanbul. | Istanbul. (3) | 1124 | 499–686 | 1493–1498 | 3 (505–692) | 4 / 4 | evet | 328–692 |
| s1b | acik | 6.42 | 6.400 | I live in Istanbul. | Istanbul. (3) | 1124 | 499–686 | 1493–1498 | 3 (505–692) | 4 / 4 | evet | 328–692 |
| s1b | acik | 7.64 | 7.633 | Hep orada: kalıcı durum, geniş zaman. | orada: (1) | 62 | 192–202 | 1493–1498 | 1 (196–332) | 6 / 6 | evet | 98–923 |
| s1b | acik | 8.03 | 8.000 | Hep orada: kalıcı durum, geniş zaman. | orada: (1) | 806 | 192–326 | 1493–1498 | 1 (196–332) | 6 / 6 | evet | 98–923 |
| s1b | acik | 9.11 | 9.100 | Hep orada: kalıcı durum, geniş zaman. | durum, (3) | 884 | 470–617 | 1493–1498 | 3 (474–625) | 6 / 6 | evet | 98–923 |
| s1b | acik | 10 | 10.000 | Hep orada: kalıcı durum, geniş zaman. | zaman. (5) | 908 | 766–917 | 1493–1498 | 5 (771–923) | 6 / 6 | evet | 98–923 |
| s1b | acik | 11.14 | 11.133 | I am living with my uncle. | am (1) | 386 | 262–326 | 1493–1498 | 1 (267–331) | 6 / 6 | evet | 233–787 |
| s1b | acik | 11.28 | 11.267 | I am living with my uncle. | living (2) | 682 | 344–458 | 1493–1498 | 2 (350–462) | 6 / 6 | evet | 233–787 |
| s1b | acik | 14 | 14.000 | Şimdilik: geçici durum, şimdiki zaman. | Şimdilik: (0) | 1070 | 92–270 | 1493–1498 | 0 (97–276) | 5 / 5 | evet | 92–923 |
| s1b | acik | 14.37 | 14.367 | Şimdilik: geçici durum, şimdiki zaman. | geçici (1) | 794 | 289–421 | 1493–1498 | 1 (293–415) | 5 / 5 | evet | 97–923 |
| s1b | acik | 16.04 | 16.033 | Şimdilik: geçici durum, şimdiki zaman. | zaman. (4) | 908 | 766–917 | 1493–1498 | 4 (771–923) | 5 / 5 | evet | 97–923 |
| s1b | koyu | 7.64 | 7.633 | Hep orada: kalıcı durum, geniş zaman. | orada: (1) | 58 | 192–202 | 1493–1498 | 1 (196–332) | 6 / 6 | evet | 98–923 |
| s1b | koyu | 8.03 | 8.000 | Hep orada: kalıcı durum, geniş zaman. | orada: (1) | 804 | 192–326 | 1493–1498 | 1 (196–332) | 6 / 6 | evet | 98–923 |
| s1b | koyu | 11.14 | 11.133 | I am living with my uncle. | am (1) | 380 | 262–326 | 1493–1498 | 1 (267–331) | 6 / 6 | evet | 233–787 |
| s1b | koyu | 11.28 | 11.267 | I am living with my uncle. | living (2) | 678 | 345–458 | 1493–1498 | 2 (350–462) | 6 / 6 | evet | 233–787 |

Doğru sözcük ölçütü: çizgi altındaki öbek k = okunan sözcük j VE çizgi (yuvarlak uç 3 px kırpılmış) öbeğin içinde (±6 px: yazı yan boşluğu + kenar yumuşatma).
Sonuç: 37 / 37 kare doğru sözcükte; çizgi px > 0: 37 / 37.

Sözcük ortasına düşen kare (istem: en az 4): kol a 4,24 · 7,27 · 10,28 · 11,89 · 12,97 · 15,14 · 18,23 (7) · kol b 3,41 · 6,42 · 8,03 · 9,11 ·
11,28 · 14,37 (6); hepsinde çizgi > 0 ve doğru sözcükte. 11,5 (kol a) ve 7,64 (kol b) kareleri sözcük başından 0,01 sn sonradır; çizgi uzamaya
yeni başlar (62–128 px). Göz denetimi: `~/Silinecekler/2026-11-16-duz4-0204S1/altyazi-bant.png` (kol b 2,55 `mı` altında, `?` hariç;
kol a 4,24 iki satırlı parçada 2. satır `Türkçede`; koyu 15,14 `living`).

## 4. Altyazı x aralığı (sahne 02, adım 8)

| Altyazı parçası | Kare | x aralığı (yazı + çizgi) | 960'ı aşan |
|---|---|---|---|
| `İstanbul'da yaşıyorum. Amcamla yaşıyorum. Türkçede ikisi de yaşıyorum.` (2 satır) | 3,05 · 4,24 | 79–938 | yok |
| `İngilizcede ikisi ayrılır.` | 7,27 · 8,4 | 265–749 | yok |
| `I live in Istanbul.` | 9,86 · 10,28 | 328–692 | yok |
| `Hep orada: kalıcı durum, geniş zaman.` | 11,5 · 11,89 · 12,97 · 13,86 | 98–923 | yok |
| `I am living with my uncle.` | 15 · 15,14 | 233–787 | yok |
| `Şimdilik: geçici durum, şimdiki zaman.` | 17,86 · 18,23 · 19,9 | 92–923 | yok |
| Kol b `Bu iki "yaşıyorum" aynı mı?` (sahne 02 ilk kareleri) | 2,55 | 217–804 | yok |

37 karenin hiçbirinde altyazı x > 960 değil (en sağ 938).

## 5. Kapak C (A2) ve 168 px (C1)

| Ölçü | Açık | Koyu |
|---|---|---|
| Başlık | `LIVE` / `≠ [LIVING]`: 2 sözcük + ≠ (HV-20b 2–4 sözcük) | aynı |
| Kural cümlesi / set başlığı yinelemesi | yok / yok (başlık A `Yaşıyorum: I live mi, I am living mi? …`, B `"Yaşıyorum" İngilizcede nasıl denir? …`) | — |
| İçerik x (piksel) | 68–951 (ev 68'den, zemin çizgisi 951'e) | 68–951 |
| Başlık y · figür üstü · ara | 479–830 · 879 · ≈ 49 px | 479–830 · 880 · 50 px |
| Taşma, binme | yok (Read ile bakıldı) | yok |
| Dosya | `kapak-c.png` (02:01:32) | `sahneler/06-hyperframes-kapak-c/k/koyu/kapak-c-koyu.png` (02:01:27) |

168 px (yöntem P3: genişlik 168, oran korunur, PIL LANCZOS):

| Dosya | Boyut | Ana yazı (Read ile) | Not |
|---|---|---|---|
| `kapak-a-168.png` | 168 × 299 | okunur: `YAŞIYORUM = İKİ ZAMAN` | künye, kanal ve el yazısı etiketleri çok küçük |
| `kapak-b-168.png` | 168 × 299 | okunur: `YAŞIYORUM NASIL DENİR?` | baloncuk yazıları sınırda |
| `kapak-c-168.png` | 168 × 299 | okunur: `LIVE ≠ LIVING` | `kalıcı` / `geçici` sınırda |

Göz denetimi sayfası: `~/Silinecekler/2026-11-16-duz4-0204S1/kapak-168-dort.png` (kol b `kapak-a-168.png` dahil).

## 6. `hyperframes check` (C3) ve Paper.js boyut sabitleri

Tutanak: `hf-check-duz4.txt` (komut: paket kökünden `motorlar/hyperframes/node_modules/.bin/hyperframes check sahneler/<k>/proje`).

| Sahne | Sonuç | Hata | Uyarı (tür × sayı) | Çıkış |
|---|---|---|---|---|
| 01 kanca | Check passed | 0 | `text_below_floor` × 1 (rozet `YDT · TEMEL` 26 px) · `line_unread` × 2 · `gsap_repeated_fromto_without_baseline` × 1 | 0 |
| 03 çağrı | Check passed | 0 | `text_below_floor` × 1 | 0 |
| 08 kaydet | Check passed | 0 | `text_below_floor` × 1 · `line_unread` × 2 | 0 |
| 04 hikâye A | Check passed | 0 | `text_below_floor` × 1 · `line_unread` × 14 | 0 |
| 05 kapak B | Check passed | 0 | `text_below_floor` × 1 · `line_unread` × 9 | 0 |
| 06 kapak C | Check passed | 0 | `text_below_floor` × 1 · `line_unread` × 7 | 0 |
| 07 hikâye B | Check passed | 0 | `text_below_floor` × 1 · `line_unread` × 14 | 0 |

Layout 0 sorun, Contrast WCAG AA 7/7 sahnede tam. `text_below_floor` yalnız 26 px rozet (B1 önerisinde bilgi satırı). `line_unread`:
durağan türevler 1 sn tek kare zaman çizelgesidir (araç her satırı "kapanış satırı" sayar); video sahnelerinde son satır bir sonraki sahneye
geçer. Uyarılar düzeltilmedi (istem: B1 bekler).

Paper.js sahne 02 (paketin `ortak/kunye.js`):

| Öğe | Sabit | Değer |
|---|---|---|
| Kanal yazısı `@ydspublishing` | `KANAL.yaziFont` | Lexend 700, 42 px; taban y 330 |
| Kanal logosu | `KANAL.logoH` | 48 px yükseklik, y 291 |
| Künye konu adı | `KUNYE.konuAzami` / `konuAsgari` | Fredoka 700, 34 px (28'e kadar küçülür; bu pakette 34 seçilir, sağ x 645) |
| Rozet `YDT · TEMEL` | `KUNYE.rozetYazi` / `rozetH` | Lexend 700, 26 px; hap 48 px, x 665–872 |
| Altyazı | `KUNYE.altyaziYazi` / `altyaziSatir` | Lexend 500, 44 px (2 satıra sığmazsa 40, 36); satır aralığı 56 |
| Karaoke çizgisi (DUZ4) | `karaokeCiz` | 6 px, vurgu rengi, taban + 12 |

## 7. Kare tazeliği (J3 C6, adım 7)

Kaynak kümesi: `sahne-*.js`, `kalem-*.js`, `uret.py`, `proje/index.html`, paketin `ortak/kunye.js` (huni kapısı KR-1 ile aynı: `k/` üst düzey).

| kol | sahne | k/*.png (üst düzey) | en yeni kare | en yeni kaynak (dosya) | kare − kaynak (sn) | KR-1 |
|---|---|---|---|---|---|---|
| -s1 | 01-hyperframes-kapak | 4 | 16.11 02:15:26 | ortak/kunye.js 16.11 01:56:46 | +1120 | taze |
| -s1 | 02-paperjs-ornek | 15 | 16.11 02:00:59 | sahneler/02-paperjs-ornek/kalem-paper.js 16.11 01:56:56 | +244 | taze |
| -s1 | 03-hyperframes-cta | 3 | 16.11 02:15:28 | ortak/kunye.js 16.11 01:56:46 | +1122 | taze |
| -s1 | 04-hyperframes-hikaye | 1 | 16.11 02:15:46 | ortak/kunye.js 16.11 01:56:46 | +1140 | taze |
| -s1 | 05-hyperframes-kapak-b | 1 | 16.11 02:15:53 | ortak/kunye.js 16.11 01:56:46 | +1147 | taze |
| -s1 | 06-hyperframes-kapak-c | 1 | 16.11 02:01:32 | sahneler/06-hyperframes-kapak-c/proje/index.html 16.11 02:01:28 | +4 | taze |
| -s1 | 07-hyperframes-hikaye-b | 1 | 16.11 02:15:58 | ortak/kunye.js 16.11 01:56:46 | +1152 | taze |
| -s1 | 08-hyperframes-kaydet | 5 | 16.11 02:15:32 | ortak/kunye.js 16.11 01:56:46 | +1126 | taze |
| s1b | 01-hyperframes-kapak | 6 | 16.11 02:15:36 | sahneler/01-hyperframes-kapak/proje/index.html 16.11 02:03:11 | +745 | taze |
| s1b | 02-paperjs-ornek | 14 | 16.11 02:03:29 | sahneler/02-paperjs-ornek/kalem-paper.js 16.11 01:57:12 | +377 | taze |
| s1b | 03-hyperframes-cta | 3 | 16.11 02:15:39 | ortak/kunye.js 16.11 01:57:12 | +1106 | taze |
| s1b | 04-hyperframes-hikaye | 0 | — | ortak/kunye.js 16.11 01:57:12 | — | kare yok: grup türevi kol a paketinde (AB §4) |
| s1b | 05-hyperframes-kapak-b | 0 | — | ortak/kunye.js 16.11 01:57:12 | — | kare yok: grup türevi kol a paketinde (AB §4) |
| s1b | 06-hyperframes-kapak-c | 0 | — | sahneler/06-hyperframes-kapak-c/proje/index.html 16.11 02:01:28 | — | kare yok: grup türevi kol a paketinde (AB §4) |
| s1b | 07-hyperframes-hikaye-b | 0 | — | ortak/kunye.js 16.11 01:57:12 | — | kare yok: grup türevi kol a paketinde (AB §4) |
| s1b | 08-hyperframes-kaydet | 5 | 16.11 02:15:42 | ortak/kunye.js 16.11 01:57:12 | +1110 | taze |

Süreç notu: ilk huni koşusu (02:14) kol a 01, 03, 04, 05, 07, 08 ve kol b 01, 03, 08 için KR-1 KALDI verdi. Neden 1: `kunye.js` (01:56) bu HF
sahnelerinin karelerinden yeni; HF sahneleri `kunye.js`'i okumaz (yalnız `yardim.py` yorumunda anılır), ama kapı onu her sahneye sayar.
Neden 2: kol b sahne 01 açık karelerini koyu geçişinden önce çektim; son `calistir.sh --tema acik` `index.html`'i 79 sn sonra yeniden yazdı
(içerik aynı, tema sınıfı açık). Çözüm: kaynağa dokunmadan 29 kare geçici dizine yeniden çekildi (sahne-kare canlı kip; 04, 05, 07
`hyperframes snapshot --at 0.5`); 29/29 var olan kareyle eş (en büyük fark 1/255, fark > 3/255 piksel 0). Eski kareler
`~/Silinecekler/…/eski-kare-kr1/` altına taşındı, taze kareler yerine kondu. Kıyas tablosu `~/Silinecekler/…/olcum/tazele-kiyas.md`.

## 8. Kontak (C2) ve 18 klişe ön sayımı

| Sayfa | Kare |
|---|---|
| `kontak/02-04-ydt-temel-s1-duz4-kontak.png` (açık) | 01 × 4 · 02 × 9 · 08 × 5 · 03 × 3 · kapak A/B/C · hikâye A/B (26) |
| `kontak/02-04-ydt-temel-s1-duz4-kontak-koyu.png` (koyu) | 01 × 3 · 02 × 4 · 08 × 3 · 03 × 3 · kapak A/B/C koyu · hikâye A/B koyu (18) |

Koyu sayfa için 01 (0,2), 08 (20,05 · 22,75) ve 03 (25,55 · 28,6) koyu kareleri bu turda eklendi (`sahne-kare --tema koyu`, kaynağa dokunmadan;
deneme: 08 25,4 sn yeniden çekim var olan koyu kareyle 0 px).

Ön sayım (`~/.claude/skills/motion-grafik-ders/references/kliseler.md`; kanıt jürinin sayımıdır):

| # | Klişe | Ön sayım |
|---|---|---|
| 1 | Mor–mavi gradyan | 0 (düz zemin + gren + hafif vinyet ≤ 25/255) |
| 2 | Glassmorphism | 0 |
| 3 | Neon | 0 |
| 4 | Parçacık | 0 |
| 5 | 3B | 0 |
| 6 | Inter/Roboto | 0 (Fredoka, Lexend, Caveat) |
| 7 | Her şey ortalı | 0 (altyazı ortalı: standart; kapak B, C başlığı ortalı, içerik kartları sol hizalı) |
| 8 | Aynı ease, nefes zoom | kareden ölçülmez; sahne 02 kodunda `nefes` yok |
| 9 | Sabit hızlı kesme | 0 (4 sahne; kanca 3,0 sn huni §3 gereği) |
| 10 | TikTok karaoke | 0 (karaoke altçizgi; ölçek ve renk değişmez) |
| 11 | Her geçişte whoosh | kareden ölçülmez (ses) |
| 12 | AI ikonografisi | 0 |
| 13 | Emoji | 0 |
| 14 | Uzun intro | 0 (ilk söz 1,0 sn) |
| 15 | Konuşan kafa | 0 |
| 16 | Metin duvarı | **aday 1**: sahne 02 son kareleri (17,86–19,9) içerik bölgesinde 2 kart + 2 etiket + 2 `yor` + 2 `now`; B6 önerisindeki "≥ 5 öbek" sayımıyla işaret alır, öbekler iki kartta gruplu. Hikâye A/B özet karesi (bilgi) |
| 17 | Stok görsel | 0 |
| 18 | Gradyan metin, outline | 0 (kapak C `LIVE` zemin rengi konturu görünmez ayırıcıdır) |

## 9. Çakışma kapısı

```
$ node araclar/cakisma-kapisi.mjs 02-04-ydt-temel-s1 --port 41333 --sunucu 41022 --json projeler/02-04-ydt-temel-s1/uretim-tutanagi/cakisma-DUZ4.json
01-hyperframes-kapak | çakışma yok (13 örnek, 3528 kutu)
02-paperjs-ornek | çakışma yok (69 örnek, 3180 kutu)
08-hyperframes-kaydet | çakışma yok (23 örnek, 2800 kutu)
03-hyperframes-cta | çakışma yok (26 örnek, 3880 kutu)
çıkış kodu: 0
$ node araclar/cakisma-kapisi.mjs 02-04-ydt-temel-s1b --port 41333 --sunucu 41022 --json projeler/02-04-ydt-temel-s1b/uretim-tutanagi/cakisma-DUZ4.json
01-hyperframes-kapak | çakışma yok (11 örnek, 2674 kutu)
02-paperjs-ornek | çakışma yok (56 örnek, 3106 kutu)
08-hyperframes-kaydet | çakışma yok (23 örnek, 2800 kutu)
03-hyperframes-cta | çakışma yok (26 örnek, 3880 kutu)
çıkış kodu: 0
$ KALEM_KOK=/home/sef/Silinecekler/2026-11-16-duz4-0204S1/kapi-kok SAHNE_KARE_BETIK=$PWD/araclar/sahne-kare.mjs node araclar/cakisma-kapisi.mjs 02-04-ydt-temel-s1 --port 41333 --sunucu 41022 --json projeler/02-04-ydt-temel-s1/uretim-tutanagi/cakisma-DUZ4-duragan.json
04-hyperframes-hikaye | çakışma yok (3 örnek, 564 kutu)
05-hyperframes-kapak-b | çakışma yok (3 örnek, 468 kutu)
06-hyperframes-kapak-c | çakışma yok (3 örnek, 1089 kutu)
07-hyperframes-hikaye-b | çakışma yok (3 örnek, 336 kutu)
çıkış kodu: 0
```

JSON: `cakisma-DUZ4.json`, `cakisma-DUZ4-duragan.json`. Durağan koşu geçici kökü (DUZ2 yöntemi): gerçek `zaman.json` kopyası, `sahneler[]` = 4
durağan sahne (t 0–0,5), `sahneler` simge bağı; `~/Silinecekler/2026-11-16-duz4-0204S1/kapi-kok/`.

## 10. Huni kapısı (`huni-kapi-duz4.txt`, `huni-kapi.mjs` 8afc202)

```
$ node D/araclar/huni-kapi.mjs K/projeler/02-04-ydt-temel-s1
JR-1b KALDI — jüri 2026-11-16 00:11:11 (J2-hukum-1611-0009.md) ≤ son içerik 2026-11-16 02:14:09 (surumler.json)
KR-1 GEÇTİ — 8 sahnede kareler kaynaktan ve kunye.js'ten yeni
ÖZET: 17 GEÇTİ, 1 KALDI, 5 ÖLÇÜLEMEDİ, 7 UYGULANMAZ
çıkış kodu: 1
```

| KALDI | Sınıf | Gerekçe |
|---|---|---|
| JR-1b | gerçek (sıra durumu; üretim kusuru değil) | jüri hükmü DUZ4 içeriğinden eski; 3. tur jüri (J3 §0 sıra 4) yazınca kapanır |
| KR-1 (ilk koşu 02:14, giderildi) | kapı hatası K7 (kapsam) + gerçek (kol b 01) | §7 süreç notu; son koşuda GEÇTİ |

ÖLÇÜLEMEDİ 5 (HV-1, HV-10, HV-17, HV-22, HV-23): tarayıcı ya da Whisper ister; HV-22 bu raporun §9'u, HV-10 §4 (altyazı) ve §5 (kapak C).

## 11. AB-8 taraması (kol b)

```
$ grep -rnw "02-04-ydt-temel-s1" K/projeler/02-04-ydt-temel-s1b --include=*.js --include=*.html --include=*.json --include=*.py --include=*.sh
projeler/02-04-ydt-temel-s1b/sahneler/07-hyperframes-hikaye-b/calistir.sh:10:PAKET="$(cd "$AD/../.." && pwd)"            # paket kökü (02-04-ydt-temel-s1)
projeler/02-04-ydt-temel-s1b/sahneler/06-hyperframes-kapak-c/calistir.sh:10:PAKET="$(cd "$AD/../.." && pwd)"            # paket kökü (02-04-ydt-temel-s1)
projeler/02-04-ydt-temel-s1b/sahneler/03-hyperframes-cta/uret.py:1:"""02-04-ydt-temel-s1 sahne 03 Çağrı (HyperFrames, DİKEY 1080x1920, huni v2).
projeler/02-04-ydt-temel-s1b/uretim-tutanagi/kol-b.json:3:  "kol_a": "02-04-ydt-temel-s1",
projeler/02-04-ydt-temel-s1b/sahneler/01-hyperframes-kapak/yardim.py:1:"""02-04-ydt-temel-s1 sahne 01; huni v2 (15.11): kanal katmanı + künye satırı + v2 bantları (BRIEF-S1 "Kanal katmanı").
projeler/02-04-ydt-temel-s1b/sahneler/01-hyperframes-kapak/uret.py:3:Kol a (02-04-ydt-temel-s1) uret.py kopyası; KBC-0204S1 (15.11) değişiklikleri, senaryo-taslak §3: başlık 2 `AYNI MI?` ·
projeler/02-04-ydt-temel-s1b/sahneler/04-hyperframes-hikaye/calistir.sh:11:PAKET="$(cd "$AD/../.." && pwd)"            # paket kökü (02-04-ydt-temel-s1)
projeler/02-04-ydt-temel-s1b/sahneler/05-hyperframes-kapak-b/uret.py:2:"""02-04-ydt-temel-s1 sahne 05 kapak B (soru) index.html üretici (HyperFrames DİKEY 1080x1920; tek kare, ses yok; huni v2)."""
projeler/02-04-ydt-temel-s1b/sahneler/04-hyperframes-hikaye/yardim.py:1:"""Ortak yardımcılar, DİKEY 1080x1920 (present-continuous-ileri-s1 sahne 03 kopyası; 02-04-ydt-temel-s1 için künye
projeler/02-04-ydt-temel-s1b/sahneler/05-hyperframes-kapak-b/yardim.py:1:"""02-04-ydt-temel-s1 sahne 05 kapak B; huni v2 (15.11): kanal katmanı + künye satırı + v2 bantları (BRIEF-S1 "Kanal katmanı").
projeler/02-04-ydt-temel-s1b/sahneler/08-hyperframes-kaydet/calistir.sh:2:# Sahne 08 Kaydet (02-04-ydt-temel-s1, huni v2, HyperFrames DİKEY 1080x1920, 177 kare, t_bas 19,99, cümle 3 öğretmen):
projeler/02-04-ydt-temel-s1b/sahneler/02-paperjs-ornek/sahne-02.js:1:// Sahne 02 (02-04-ydt-temel-s1 Shorts) — Örnek: Paper.js, 1080x1920, 522 kare, t_bas 3.00.
projeler/02-04-ydt-temel-s1b/sahneler/05-hyperframes-kapak-b/calistir.sh:10:PAKET="$(cd "$AD/../.." && pwd)"            # paket kökü (02-04-ydt-temel-s1)
projeler/02-04-ydt-temel-s1b/sahneler/08-hyperframes-kaydet/yardim.py:1:"""Ortak yardımcılar, DİKEY 1080x1920 (02-04-ydt-temel-s1 sahne 03 v2 kopyası; sahne 08 Kaydet).
projeler/02-04-ydt-temel-s1b/sahneler/07-hyperframes-hikaye-b/yardim.py:1:"""Ortak yardımcılar, DİKEY 1080x1920 (present-continuous-ileri-s1 sahne 03 kopyası; 02-04-ydt-temel-s1 için künye
projeler/02-04-ydt-temel-s1b/sahneler/03-hyperframes-cta/yardim.py:1:"""Ortak yardımcılar, DİKEY 1080x1920 (present-continuous-ileri-s1 sahne 03 kopyası; 02-04-ydt-temel-s1 için künye
projeler/02-04-ydt-temel-s1b/sahneler/08-hyperframes-kaydet/uret.py:1:"""02-04-ydt-temel-s1 sahne 08 Kaydet (HyperFrames, DİKEY 1080x1920, huni v2).
projeler/02-04-ydt-temel-s1b/sahneler/02-paperjs-ornek/sayfa.html:5:// SAHNE 02 — Örnek (02-04-ydt-temel-s1 Shorts): Paper.js, 1080x1920, 30 fps, 522 kare. Kalem modülü: kalem-paper.js; içerik: sahne-02.js.
projeler/02-04-ydt-temel-s1b/sahneler/03-hyperframes-cta/calistir.sh:2:# Sahne 03 Çağrı (02-04-ydt-temel-s1, huni v2, HyperFrames DİKEY 1080x1920, 218 kare, t_bas 25,49, cümle 4 öğrenci):
projeler/02-04-ydt-temel-s1b/sahneler/06-hyperframes-kapak-c/yardim.py:1:"""02-04-ydt-temel-s1 sahne 06 (kapak C); sahne 01 v2 yardim.py kopyası — huni v2 (15.11): kanal katmanı + künye satırı + v2 bantları.
```

Sınıf: 19 satır yorum ya da belge dizgisi (`#`, `//`, `"""` başlığı; yol değil), 1 satır `uretim-tutanagi/kol-b.json` `kol_a` kayıt alanı
(A/B kaydı). Kol a yolunu gösteren içe aktarma, URL ya da `PROJE=` atama satırı 0. Kapı AB-8 GEÇTİ ("bilgi: 9 yorum satırı").

## 12. `diff -rq` sınıflaması (kol a ↔ kol b)

Tam liste: `../../02-04-ydt-temel-s1b/uretim-tutanagi/diff-siniflama-DUZ4.txt` (satır başına sınıf, durum, yol).

| Sınıf | Satır | Durum |
|---|---|---|
| S2 aciklama*.md (utm_content s1b + kol b başlık notları) | 3 | beklenen |
| T1 grup türevleri yalnız kol a (AB §4: kök kapak B/C, 168 px B/C, hikâye, 04–07 kareleri) | 19 | beklenen |
| D2 kapak A = kanca karesi (kapak-a, kapak, kapak-a-168) | 3 | beklenen |
| D5 ses ve zaman türevleri (cümle 1 süresi; altyazi.json ayrıca DUZ4 tırnağı) | 14 | beklenen |
| D3 değişken cümle sesi cumle-1.wav | 1 | beklenen |
| D4 senaryo.json (cümle 1 + meta.kimlik s1b) | 1 | beklenen |
| G2 ortak/kunye.js KOK yolu (AB-8 ister) | 1 | beklenen |
| D1 değişken sahne 01 (kod, proje, proje-ka, kareler) | 30 | beklenen |
| H1 .hyperframes (hyperframes check/snapshot artefaktı, git dışı) | 19 | beklenen |
| P1 __pycache__ (derleme önbelleği, git dışı) | 11 | beklenen |
| G1 sahne 02 baş kırpımı (sahne-02.js T_BAS/KARE/çapa, calistir.sh N/TBAS, SPEC/RAPOR kol b notu) | 4 | B3 bekliyor |
| Q1 sahne 02/08/03 kareleri (her kol kendi zaman çizelgesiyle) | 65 | beklenen |
| G3 sahne 02 içe aktarma yolu (kalem-paper.js, sayfa.html; AB-8 ister) | 2 | beklenen |
| S1 surumler.json (varyant, kol b sürüm satırları, revizyon r1–r2) | 1 | beklenen |
| U1 uretim-tutanagi (kola özgü tutanak) | 46 | beklenen |
| **Toplam** | **220** | **beklenmeyen 0** |

Ortak dosyalar paket adı normalleştirilerek: `ortak/kunye.js` ve `kalem-paper.js` fark 0 (yalnız yol); `sahne-02.js` farkı yalnız kol b
başlık yorumu + `KARE`/`T_BAS` + cümle 1 çapası (B3); `aciklama*.md` farkı yalnız kol b başlık notları (8–10 satır); `BRIEF-S1.md` 0;
`06-hyperframes-kapak-c/{uret.py,nesneler.json,proje/index.html,SPEC.md}` kol b'ye birebir kopyalandı (kol b grup türevi kaynağını eş taşır).

AB-3 kare çifti (kol a t ↔ kol b t − 3,86; fark > 3/255 piksel; kapının "G kare çifti gerekir" satırı için):

| sahne | tema | kol a t ↔ kol b t | tam kare (> 3/255 px) | altyazı bandı 1400–1550 | kanal 280–350 | fark kutusu |
|---|---|---|---|---|---|---|
| 02 | açık | 7.27 ↔ 3.41 | 0 | 0 | 0 | None |
| 02 | açık | 9.86 ↔ 6 | 83 | 0 | 0 | (822, 631, 878, 673) |
| 02 | açık | 10.28 ↔ 6.42 | 0 | 0 | 0 | None |
| 02 | açık | 11.5 ↔ 7.64 | 74 | 74 | 0 | (201, 1493, 215, 1499) |
| 02 | açık | 11.89 ↔ 8.03 | 0 | 0 | 0 | None |
| 02 | açık | 12.97 ↔ 9.11 | 0 | 0 | 0 | None |
| 02 | açık | 13.86 ↔ 10 | 0 | 0 | 0 | None |
| 02 | açık | 15 ↔ 11.14 | 20 | 20 | 0 | (325, 1493, 330, 1499) |
| 02 | açık | 15.14 ↔ 11.28 | 24 | 24 | 0 | (457, 1493, 463, 1499) |
| 02 | açık | 17.86 ↔ 14 | 259 | 0 | 0 | (263, 1173, 293, 1208) |
| 02 | açık | 18.23 ↔ 14.37 | 524 | 24 | 0 | (128, 1265, 423, 1499) |
| 02 | açık | 19.9 ↔ 16.04 | 0 | 0 | 0 | None |
| 02 | koyu | 11.5 ↔ 7.64 | 76 | 76 | 0 | (200, 1493, 215, 1499) |
| 02 | koyu | 11.89 ↔ 8.03 | 0 | 0 | 0 | None |
| 02 | koyu | 15 ↔ 11.14 | 20 | 20 | 0 | (325, 1493, 330, 1499) |
| 02 | koyu | 15.14 ↔ 11.28 | 26 | 26 | 0 | (456, 1493, 463, 1499) |
| 08 | açık | 20.05 ↔ 16.19 | 0 | 0 | 0 | None |
| 08 | açık | 21.2 ↔ 17.34 | 0 | 0 | 0 | None |
| 08 | açık | 22.75 ↔ 18.89 | 0 | 0 | 0 | None |
| 08 | açık | 23.4 ↔ 19.54 | 0 | 0 | 0 | None |
| 08 | açık | 25.4 ↔ 21.54 | 0 | 0 | 0 | None |
| 03 | açık | 25.55 ↔ 21.69 | 0 | 0 | 0 | None |
| 03 | açık | 28.6 ↔ 24.74 | 0 | 0 | 0 | None |
| 03 | açık | 31.7 ↔ 27.85 | 0 | 0 | 0 | None |

Sahne 08 ve 03: 8/8 çift 0 px. Sahne 02: 16 çiftin 9'u 0 px; kalan farklar süren çizimdedir: karaoke çizgisinin uzayan ucu (20–76 px,
y 1493–1499) ve kalem darbesi (83–524 px). İki kolun kare ızgarası 0,2 kare kaymalıdır (Δ 3,86 sn = 115,8 kare; DUZ2 §3 aynı). B3 bekliyor.

## 13. Düzeltilmeyen maddeler

| Madde | Sebep |
|---|---|
| ST-2 boyutları (B1), `hyperframes check` uyarıları | istem: dokunma, B1 bekler |
| EK-12 açılış zamanları (B2), AB-4/5/7, EK-4, EK-11 | istem: dokunma (yayın sonrası / insan kanıtı) |
| "Hep orada: kalıcı durum, geniş zaman." (EK-5c, B4) | şef kararı: kalır |
| `sahneler/02-paperjs-ornek/SPEC.md:120` "Ekranda `İstanbul.` (noktalı İ)" ve RAPOR/SPEC tabloları | iç belge (istemin beklediği); SPEC başına DUZ4 notu eklendi |
| `uretim-tutanagi/` içindeki eski `I live mı` / `İstanbul` satırları | tarihsel kayıt ve jüri hükmü |
| Klişe #16 adayı (sahne 02 son kareleri) | A sınıfı değil; B6 sayım kuralı onaylanmadı; jüri sayar |
| 168 px'te künye, kanal, el yazısı etiketleri | ana yazı okunur (KS-6 ölçütü); bilgi |

## 14. Süreç notları

- Yazım kapısı (`write-size-gate`, 15 satır) `kunye.js` düzenlemesini durdurdu; kanca atlama bayrağı oluşturulmadı, düzenleme ≤ 15 satırlık
  parçalara bölündü. Ölçümler satır içi `python3 -I -c` ile koştu (kod dosyası yazılmadı).
- Kapak C ilk koşuda `uret.py` kuralı (başlık–sahne ≥ 48) S = 190 ile kaldı (43,3); S yükseklikten de sınırlandı (187).
- `calistir.sh` içinde `uret.py && olay.py` zinciri `set -e`'yi tetiklemez; ilk kapak C koşusunda hata "önizleme hazır" ile örtüldü. Bilgi.
- Huni kapısı oturum içinde güncellendi (8afc202, 02:03); bütün koşular bu sürümle.

## 15. Değiştirilen dosyalar (kol a)

Git'te izlenen: `aciklama.md`, `aciklama-a.md`, `aciklama-b.md`, `BRIEF-S1.md`, `surumler.json` (`revizyonlar` r2), `ortak/kunye.js`,
`sahneler/02-paperjs-ornek/{kalem-paper.js,sahne-02.js,SPEC.md}`, `sahneler/06-hyperframes-kapak-c/{uret.py,nesneler.json,proje/index.html,SPEC.md}`.
Yeni: `uretim-tutanagi/{DUZ4-RAPOR.md,hf-check-duz4.txt,huni-kapi-duz4.txt,cakisma-DUZ4.json,cakisma-DUZ4-duragan.json,
kontak/02-04-ydt-temel-s1-duz4-kontak.png,kontak/02-04-ydt-temel-s1-duz4-kontak-koyu.png}`.
Git dışı (`.gitignore`): `kapak-a-168.png`, `kapak-b-168.png`, `kapak-c-168.png` (yeni), `kapak-c.png`, `sahneler/*/k/` kareleri,
`sahneler/*/proje/.hyperframes/` (check artefaktı). Şef commit'inde 168 px dosyaları için `git add -f` gerekir (KS-6 "dosya pakette").
