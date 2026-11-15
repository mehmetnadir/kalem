uretici_model: claude-opus-5-5 (üretim oturumu fd389160) + ajan yok
# DUZ4-0204S1 raporu — 02-04-ydt-temel-s1b (A/B kol b, değişken `kanca`) · J3 A düzeltmeleri ve üretilebilir kanıtlar · 16.11.2026

İstem: `uretim-hatti/raporlar/J3-OZET-1611.md` §5 satır `DUZ4-0204S1`. Hüküm: `juri/KBJ-hukum-1611-0014.md`. Kol a raporu (yöntem, kod
ayrıntısı, ortak tablolar): `../../02-04-ydt-temel-s1/uretim-tutanagi/DUZ4-RAPOR.md`. Ses sentezi, mp4, commit, alt ajan, agy-filo YOK.
Silinen dosya yok; taşınanlar `~/Silinecekler/2026-11-16-duz4-0204S1/` (`LISTE.md`).

| Ölçüm | Değer |
|---|---|
| Düzeltilen kusur | A1 (DK-1) · A4 (EK-6: `I live mi`, kart `Istanbul.`, altyazı tırnağı) |
| Üretilen kanıt | C1 (KS-6: `kapak-a-168.png`) · C2 (EK-8: kontak) · C3 (ST-2: `hyperframes check` + `kunye.js` boyutları) |
| Ses | değişmedi: `cumle-1…4.wav`, `sentez.wav`, `anlatim.*` sha256 önce = sonra; cümle 2–4 kol a ile eş (AB-9) |
| Karaoke | kol b 18 karenin 18'inde çizgi okunan sözcüğün altında (kol a ile birlikte 37/37) |
| Altyazı x | en sağ 923 (kol b sahne 02), tırnaklı kanca altyazısı 217–804 |
| Kare tazeliği | 4 video sahnesi taze; 04–07 kol b'de kare taşımaz (AB §4) |
| Çakışma kapısı | çıkış **0** (4 sahne, 0 uyarı) |
| Huni kapısı | 22 GEÇTİ, 1 KALDI (JR-1b, sıra durumu), 7 ÖLÇÜLEMEDİ, çıkış 1; AB-2 GEÇTİ (0 beklenmeyen), AB-8 GEÇTİ, KS-6f GEÇTİ, AB-9 GEÇTİ |
| `diff -rq` kol a ↔ kol b | 220 satır, beklenmeyen **0**, B3 bekliyor 4 |

## 1. Düzeltmeler

| J3 · jüri madde | Dosya | Önce → sonra | Kanıt |
|---|---|---|---|
| A1 · DK-1 | `ortak/kunye.js`, `sahneler/02-paperjs-ornek/kalem-paper.js` | kol a dosyası kopyalandı, yalnız `KOK` ve içe aktarma yolu `02-04-ydt-temel-s1b`'ye geri yazıldı | paket adı normalleştirilmiş `diff` → 0 satır (iki dosya); kareler `sahneler/02-paperjs-ornek/k/*.png` |
| A4 · EK-6 | `aciklama.md` (16, 65), `aciklama-a.md` (17, 66), `aciklama-b.md` (24, 44, 68) | `I live mı` → `I live mi` (7 yer; kol a ile aynı satırlar) | `grep -rn "live mı"` (uretim-tutanagi dışı) → 0 |
| A4 · EK-6 | `sahneler/02-paperjs-ornek/sahne-02.js:123` (kol a :125), `aciklama.md` (24, 43), `aciklama-a.md` (25, 44), `aciklama-b.md` (26, 46), `BRIEF-S1.md:56`, `:65` | İngilizce cümlede `İstanbul.` → `Istanbul.`; `İstanbul'da yaşı-` (`:146`) değişmedi | kare `02-paperjs-ornek-6.42.png` (kart + altyazı `Istanbul.`) |
| A4 · EK-6 (yalnız kol b) | `ortak/anlatim/altyazi.json` cümle 1 | `Bu iki yaşıyorum aynı mı?` → `Bu iki "yaşıyorum" aynı mı?`; ses metni (`senaryo.json`, `METIN.md`, `sentez.wav.rapor.json`) ve `cumle-1.wav` değişmedi | `json.load` geçti; kareler `sahneler/01-hyperframes-kapak/k/01-…-0.9 · 1.3 · 1.75 · 2.2 · 2.45.png`, `k/koyu/01-…-0.9 · 1.75 · 2.2.png`; sahne 02 ilk kare `02-…-2.55.png` |
| A4 (kaynak türevi) | `sahneler/01-hyperframes-kapak/proje/index.html`, `proje-ka/index.html` | `calistir.sh` (ONIZLE_YALNIZ) `uret.py`'yi koşturdu; tek fark altyazı metni (eski yedekle `diff`: yalnız satır 133). `proje-ka` = `proje` + `#altyazi{display:none}` | kapak A açık md5 `bf26cabd7f0b…` (eskiyle aynı; altyazı gizli) · koyu md5 `08b5522b816d…` (eskiyle aynı) |
| A2 grup kaynağı | `sahneler/06-hyperframes-kapak-c/{uret.py,nesneler.json,proje/index.html,SPEC.md}` | kol a dosyaları birebir kopyalandı (kol b kapak C PNG üretmez; grup türevi kaynağını kol a ile eş taşır, DUZ2 kalıbı) | `diff -rq` 06: yalnız kol a `k/` ve `.hyperframes`; kapı AB-2 0 beklenmeyen |

Tırnak göz denetimi: `~/Silinecekler/2026-11-16-duz4-0204S1/altyazi-bant.png` — açık 1,3 ve koyu 2,2 sn'de `Bu iki "yaşıyorum" aynı mı?`
(Lexend düz tırnak); sahne 02 2,55 sn'de karaoke `mı` altında (`?` hariç). Sahne 01 kancadır: karaoke beklenmez (DK-1 kısada kanca değil).

**UYARI:** `araclar/altyazi_uret.py` `altyazi.json`'u `senaryo.json` parçalarından yeniden üretir. Ses yeniden sentezlenir ya da betik koşarsa
tırnak kaybolur (ses metni tırnaksızdır). Bu tur betiğe dokunmadı (`K/araclar` kapsam dışı).

## 2. Ses sha256

Kol a raporu §2 tablosu (iki kol). Kol b: `cumle-1.wav` `2f914435214e…` (değişken), `cumle-2/3/4.wav` kol a ile eş, `sentez.wav`
`bb76a6037c7e…`, `anlatim.m4a` `66ccac3b7e5f…`, `anlatim.m4a.imza` `0064ddd5d44e…`, `anlatim.wav` `7ee4ad212055…`; önce = sonra.

## 3. Karaoke (A1) ve altyazı x

Yöntem ve eşikler kol a raporu §3. Tablo (iki kol):

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

Kol b sözcük ortası kareleri: 3,41 · 6,42 · 8,03 · 9,11 · 11,28 · 14,37 (+ koyu 8,03 · 11,28). Altyazı x: en sol 92, en sağ 923; 960'ı aşan 0.

## 4. Kapak A ve 168 px (C1)

| Dosya | Boyut | Ana yazı (Read ile) |
|---|---|---|
| `kapak-a.png` = `kapak.png` | 1080 × 1920 | yeniden çekim (proje-ka, `hyperframes snapshot --at 1.75`); md5 eskiyle aynı |
| `kapak-a-168.png` | 168 × 299 | okunur: `YAŞIYORUM AYNI MI?`; el yazısı satırları ve künye çok küçük |

## 5. `hyperframes check` (C3)

Tutanak `hf-check-duz4.txt`. 01 kanca: Check passed, 0 hata, `text_below_floor` × 1 (rozet 26 px), `line_unread` × 1 · 03 çağrı: 0 hata,
`text_below_floor` × 1 · 08 kaydet: 0 hata, `text_below_floor` × 1, `line_unread` × 2. Üç sahnede Layout 0 sorun, WCAG AA tam, çıkış 0.
Paper.js boyut sabitleri kol a ile aynı (`ortak/kunye.js` fark 0): kanal 42 px, logo 48, künye 34 (asgari 28), rozet 26, altyazı 44 / satır 56.

## 6. Kare tazeliği

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

Kol b sahne 01 açık kareleri ilk koşuda `proje/index.html`'den 79 sn eskiydi (son tema geçişi dosyayı yeniden yazdı; içerik aynı). 6 kare
kaynağa dokunmadan yeniden çekildi; 6/6 var olanla piksel eş (kol a raporu §7). Kol b 03 ve 08: `kunye.js` kaynaklı aynı işlem, 8/8 eş.

## 7. Kontak (C2) ve klişe ön sayımı

| Sayfa | Kare |
|---|---|
| `kontak/02-04-ydt-temel-s1b-duz4-kontak.png` (açık) | 01 × 6 · 02 × 8 · 08 × 5 · 03 × 3 · kapak A (23) |
| `kontak/02-04-ydt-temel-s1b-duz4-kontak-koyu.png` (koyu) | 01 × 3 · 02 × 4 · 08 × 3 · 03 × 3 · kapak A koyu (14) |

Ön sayım kol a raporu §8 ile aynı (sahne 02, 08, 03 iki kolda eş içerik): 18 maddenin 15'i 0, 2'si kareden ölçülmez (#8, #11), #16 aday 1
(sahne 02 son kareleri 14–16,04 sn). Kol b'ye özgü: kanca sahnesi 2,5 sn, ilk söz 0,5 sn (#14 0).

## 8. Çakışma kapısı

```
$ node araclar/cakisma-kapisi.mjs 02-04-ydt-temel-s1b --port 41333 --sunucu 41022 --json projeler/02-04-ydt-temel-s1b/uretim-tutanagi/cakisma-DUZ4.json
01-hyperframes-kapak | çakışma yok (11 örnek, 2674 kutu)
02-paperjs-ornek | çakışma yok (56 örnek, 3106 kutu)
08-hyperframes-kaydet | çakışma yok (23 örnek, 2800 kutu)
03-hyperframes-cta | çakışma yok (26 örnek, 3880 kutu)
çıkış kodu: 0
```

## 9. Huni kapısı (`huni-kapi-duz4.txt`, `huni-kapi.mjs` 8afc202)

```
$ node D/araclar/huni-kapi.mjs K/projeler/02-04-ydt-temel-s1b --kol-a K/projeler/02-04-ydt-temel-s1
JR-1b KALDI — jüri 2026-11-16 00:16:26 (KBJ-hukum-1611-0014.md) ≤ son içerik 2026-11-16 02:14:09 (surumler.json)
KR-1 ÖLÇÜLEMEDİ — k/ kare dizini yok ya da boş: 04-hyperframes-hikaye, 05-hyperframes-kapak-b, 06-hyperframes-kapak-c, 07-hyperframes-hikaye-b; 4 sahne taze
AB-8 GEÇTİ · AB-2 GEÇTİ — kanca: 31 beklenen fark, 0 beklenmeyen; zaman kayması (Δ=-3.860 sn): 2 dosya · AB-3 ÖLÇÜLEMEDİ — G kare çifti gerekir
KS-6f GEÇTİ · AB-9 GEÇTİ · AB-1 GEÇTİ · AB-6 GEÇTİ
ÖZET: 22 GEÇTİ, 1 KALDI, 7 ÖLÇÜLEMEDİ, 3 UYGULANMAZ
çıkış kodu: 1
```

| Satır | Sınıf | Gerekçe |
|---|---|---|
| JR-1b KALDI | gerçek (sıra durumu; üretim kusuru değil) | jüri hükmü DUZ4 içeriğinden eski; 3. tur jüri kapatır |
| KR-1 ÖLÇÜLEMEDİ (04–07) | kapı hatası K7 (kapsam) | kol b grup türevi sahneleri kare taşımaz (AB §4); kapı bunları "k/ yok" sayar. 4 video sahnesi taze |
| AB-2 KALDI (ilk koşu 02:14, giderildi) | gerçek (eksik kopya) | kapak C kaynağı kol b'ye kopyalanmamıştı; kopyalandı, son koşuda 0 beklenmeyen |
| AB-3 ÖLÇÜLEMEDİ | B3 bekliyor | kare çifti tablosu §10 |

## 10. AB-8, `diff -rq`, AB-3 kare çifti

AB-8 taraması:

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

Sınıf: 19 yorum ya da belge dizgisi, 1 `uretim-tutanagi/kol-b.json` `kol_a` kayıt alanı; yol başvurusu 0. Bu turda eklenen satır 0
(`kalem-paper.js` kopyası yol satırlarını `-s1b`'ye geri yazdı).

`diff -rq K/projeler/02-04-ydt-temel-s1 K/projeler/02-04-ydt-temel-s1b` (tam liste `diff-siniflama-DUZ4.txt`):

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

"B3 bekliyor" 4 satır: `sahneler/02-paperjs-ornek/{sahne-02.js,calistir.sh,SPEC.md,RAPOR.md}` (kol b `T_BAS 2.5`, `KARE 421`, `N=421`,
`TBAS=2.50`, cümle 1 çapası yok; SPEC/RAPOR kol b notu). Değişmeyen sahnelerin `zamanlar.json` kayması (03, 08) D5 sınıfında; kapı bunları
"zaman kayması (beklenen, Δ = −3,860 sn)" sayar.

AB-3 kare çifti (kol a t ↔ kol b t − 3,86):

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

Sahne 08 ve 03: 8/8 çift 0 px. Sahne 02: 16 çiftin 9'u 0 px; farklar süren çizimde (karaoke ucu 20–76 px, kalem darbesi 83–524 px); kare
ızgarası iki kolda 0,2 kare kaymalı (Δ 3,86 sn = 115,8 kare). B3 bekliyor.

## 11. Düzeltilmeyen maddeler

| Madde | Sebep |
|---|---|
| Sahne 02 `T_BAS` / kare / yol farkı (AB-2, AB-3) | B3 kararı bekler; kod yazılmadı |
| "Hep orada" (EK-5c) | B4: kalır |
| ST-2 (B1), EK-12 (B2), AB-4/5/7, EK-11 | istem: dokunma |
| `sahneler/01-hyperframes-kapak/RAPOR.md:6,16` ve `uretim-tutanagi/*` içinde tırnaksız `Bu iki yaşıyorum aynı mı?` | iç belge ve tarihsel kayıt (ses metni de tırnaksızdır) |
| `altyazi_uret.py` tırnağı korumaz | `K/araclar` kapsam dışı; şef kararı (altyazı metni için ayrı alan) |

## 12. Değiştirilen dosyalar (kol b)

Git'te izlenen: `aciklama.md`, `aciklama-a.md`, `aciklama-b.md`, `BRIEF-S1.md`, `surumler.json` (`revizyonlar` r2), `ortak/kunye.js`,
`ortak/anlatim/altyazi.json`, `sahneler/01-hyperframes-kapak/{proje/index.html,proje-ka/index.html}`,
`sahneler/02-paperjs-ornek/{kalem-paper.js,sahne-02.js,SPEC.md}`, `sahneler/06-hyperframes-kapak-c/{uret.py,nesneler.json,proje/index.html,SPEC.md}`.
Yeni: `uretim-tutanagi/{DUZ4-RAPOR.md,hf-check-duz4.txt,huni-kapi-duz4.txt,cakisma-DUZ4.json,diff-siniflama-DUZ4.txt,
kontak/02-04-ydt-temel-s1b-duz4-kontak.png,kontak/02-04-ydt-temel-s1b-duz4-kontak-koyu.png}`.
Git dışı (`.gitignore`): `kapak-a-168.png` (yeni; commit için `git add -f`), `kapak-a.png`, `kapak.png`, `sahneler/*/k/` kareleri,
`sahneler/*/proje/.hyperframes/`.
