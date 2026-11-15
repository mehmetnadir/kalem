# DUZ3-0201T — ders içeriği düzeltmesi (present-continuous + present-continuous-dikey)

Tarih 16.11.2026 · kaynak `uretim-hatti/raporlar/YV-DUZ-1511.md` §4 (jüri sınıfı c) ve satır 13/17.
Bu rapor iki paketi birlikte anlatır; dikey pakette aynı adla bir kopyası vardır.

| Ölçü | Değer |
|---|---|
| Düzeltilen cümle parçası | 4 (jüri 2 + kendi 2) |
| Düzeltilen ekran yazısı | 6 yer (yatay 02, 06; dikey 02, 06; senaryo bağ etiketi 2) + rozet + kapak |
| Yeniden sentezlenen cümle | 2 (c2, c7; 9 parça, 448 karakter) |
| Süre | 87,33 sn → 94,61 sn (+7,28) |
| En düşük Whisper | 0,96 (c7 p4) |
| Yeniden üretilen sahne | yatay 6 (01–06) + kapak · dikey 6 (01–06) + kapak |
| Tutarlılık kapısı | çıkış 1; bu iki pakette 0 sorun (6 sorun simple-present-ileri{,-dikey}) |
| Çakışma kapısı | yeni hata 0; çıkış 1 olan sahnelerin hepsi HEAD'de de 1 (aşağıda) |

## 1. Cümleler (önce → sonra)

| # | Yer | Önce | Sonra | Gerekçe | Sınıf |
|---|---|---|---|---|---|
| 1 | c2 p2 | İngilizce de aynısını yapar. | İngilizce de planlı gelecek için aynısını yapar. | Kısmi denklik: İngilizcede şimdiki zaman yalnız planlı/ayarlanmış gelecekte gelir (I'm going tonight); tahmin ve ani kararda will gelir. "Aynısını" tek başına tam denklik söyler. Jüri önerisi "planlanmış" → "planlı" (aynı anlam, sahne ve `surumler.json` ile aynı sözcük). | jüri |
| 2 | c7 p4 (+p5, p6) | -ing ekini Türkçedeki -yor gibi düşün: koşu-yor, runn-ing. | -ing çoğu zaman Türkçedeki -yor'a denk gelir: koşuyor, running. / Ama her -yor -ing olmaz: biliyorum, / I know. | Yanlış denklik: biliyorum ≠ \*I am knowing. Jüri önerisinin ikinci yarısı ("know gibi durum fiillerinde …") kısaltıldı: "durum fiili" terimi bu temel derste tanıtılmaz (ileri dersin konusu); örnek aynı. | jüri |
| 3 | c2 p3 | … zaman ifadelerini ve altı kullanımını görüyoruz. | … zaman ifadelerini ve üç kullanımını görüyoruz. | Ders üç kullanım gösterir: şu an (sahne 03, Look! sahne 05), bu dönem (sahne 04), planlı gelecek (sahne 02). "Altı" dersin hiçbir yerinde karşılanmaz. | kendi |
| 4 | c7 p1 | Çünkü -ing devam eden işi gösterir. | Çünkü burada -ing devam eden işi gösterir. | Mutlak iddia: aynı ders c2'de -ing'i planlı gelecek için kullanır; "burada" iddiayı form sahnesindeki üç örnekle sınırlar. | kendi |

Aynı iddianın geçtiği bütün yerler:

| Yer | Önce → sonra | Dosya |
|---|---|---|
| Senaryo | 4 parça + `metin` | `ortak/anlatim/senaryo.json` (meta.canAlici bu eski senaryoda yok) |
| Senaryo bağ etiketi | c2 "−ing ↔ −yor" → "planlı gelecek"; c7 "aynı iş" → "çoğu zaman" | `senaryo.json` |
| Metin | yeniden üretildi (tablo, parçalar, sözcük zamanları) | `ortak/anlatim/METIN.md` |
| Altyazı | 24 → 26 parça; değişmeyen 17 satır tam +0 / +1,04 kaydı | `ortak/anlatim/altyazi.json` |
| Yatay 02 ekran | `-yor ⇄ -ing` → `tonight → planlı gelecek`; `6 uses` → `3 uses` | `sahneler/02-paperjs-kanca/sahne-02.js` |
| Dikey 02 ekran | `-yor ⇄ -ing` → `tonight → planlı gelecek`; `6 kullanım` → `3 kullanım` | dikey `sahne-02.js` |
| Yatay 06 ekran | `koşu-yor = runn-ing` → 2×2 kart `koşuyor → running` · `biliyorum → I know` | `sahneler/06-hyperframes-form/uret.py`, `zamanlar.json` |
| Dikey 06 ekran | `-ing = -yor` (Fredoka 150) ve `koşu-yor = runn-ing` kalktı → aynı 2×2 kart | dikey `06-hyperframes-form/uret.py` |
| surumler.json | amaç 3 "üç kullanımı ayırt etmek (şu an, bu dönem, planlı gelecek)"; amaç 4 "… köprü kurmak ve sınırını görmek"; canAlici 1–2 yeni cümlelerle | `surumler.json` (dikey bağ) |
| Rozet (HV-24) | `YDT · BASIC` → `YDT · TEMEL`, kaynakta | `ortak/kunye.js`, 01/06/90 `yardim.py`, 01 `uret.py`, `nesneler.json`, BRIEF (iki paket, 12 dosya) |
| BRIEF | yatay satır 136/137/185, dikey satır 53/65/69 yeni tasarıma uyduruldu | `BRIEF.md`, `BRIEF-DIKEY.md` |
| youtube.json / youtube-aciklama.md | metinde yanlış iddia yok; yalnız zaman değişti (§5) | iki paket |

## 2. Ses

Komut: `HIZ_EN=0.8 timeout 1500 bash araclar/ses-sunucu.sh --kok ~/is/uretim-0204/duz3-0201T/kok present-continuous`
(geçici senaryoda yalnız c2 + c7; önbellek anahtarı cümle içi komşu metni içerir → cümlenin bütün parçaları yeniden).
Değişmeyen c1, c3–c6 eski `anlatim.wav`'dan örnek-tam kesildi; sha eşitliği doğrulandı. `kur.py` → `anlatim.wav`
(94,61 sn, sha d5e8d95d…), `ses-paketle.py --yaz` → `anlatim.m4a` 1.105.444 B. Dikey `ortak/anlatim` yatayın sembolik bağıdır (aynı dosya).

| Cümle | Parça | Whisper duyulan | Benzerlik |
|---|---|---|---|
| c2 | p1 | Türkçe'de şimdiki zamanla geleceği anlatırız. | 1,00 |
| c2 | p2 | İngilizce de planlı gelecek için aynısını yapar. | 1,00 |
| c2 | p3 | Bu derste … üç kullanımını görüyoruz. | 1,00 |
| c7 | p1 | Çünkü burada ING devam eden işi gösterir. … | 1,00 |
| c7 | p2 | Bir fiili ise zamanı taşır. Am, is, are … | 0,97 |
| c7 | p3 | Past olsaydı was, were derdik. | 1,00 |
| c7 | p4 | İng çoğu zaman Türkçedeki yor'a denk gelir. Koşuyor. Rumming. | 0,96 |
| c7 | p5 | Ama her yor ing olmaz. Biliyorum. | 1,00 |
| c7 | p6 (en) | I know. | 1,00 |

| Cümle | Süre önce → sonra | Başlangıç önce → sonra |
|---|---|---|
| c2 | 10,94 → 12,54 | 3,39 → 3,39 |
| c3 | 14,16 | 15,44 → 16,48 |
| c4 | 15,28 | 30,15 → 31,19 |
| c5 | 16,28 | 45,98 → 47,02 |
| c6 | 3,36 | 62,81 → 63,85 |
| c7 | 19,01 → 25,25 | 66,72 → 67,76 (son 87,33 → 94,61) |

Not: eski düzende c2 → c3 arası 1,11 sn idi; yeni zincir öteki bütün geçişler gibi "önceki bitiş + 0,55" (`sozcuk_uret.py` BASLAR).

## 3. Sahneler ve kareler

| Sahne | Yatay | Dikey | Değişiklik |
|---|---|---|---|
| 01 giriş | yeniden üretildi | yeniden üretildi | rozet TEMEL |
| 02 kanca | KARE 385 → 416, yeni zamanlar, olaylar/zamanlar.json (31 olay, geçici log sunucusu), nesneler.json | aynı (dikey nesneler.json boş) | iki ekran yazısı + c2 zamanları |
| 03–05 | KAYMA 6,00 → 4,96 (186/186 sözcük karesi aynı); nesneler +1,04 | küresel sabitler +1,04 (03: 29, 04: 25, 05: 28) | yalnız zaman |
| 06 form | KARE 953, zamanlar.json yeni, index.html (31,767 sn), olaylar.json 43 | aynı, 41 olay | 2×2 kart, c7 zamanları |
| 90 kapak | açık + koyu | açık + koyu | §4 |

Kareler (`sahneler/<sahne>/k/duz3/<sahne>-<t>.png`; koyu: `k/duz3/koyu/`):

| Sahne | Yatay t (sn) | Dikey t (sn) |
|---|---|---|
| 01 | 1,2 · 2,9 | 1,2 · 2,9 |
| 02 | 6,0 · 8,3 · 9,4 · 15,5 · 16,4 (koyu 16,4) | 9,4 · 16,4 (koyu 16,4) |
| 03 | 22,0 · 30,9 | 22,0 · 30,9 |
| 04 | 36,0 · 46,8 | 36,0 · 46,8 |
| 05 | 52,5 · 63,5 | 52,5 · 63,5 |
| 06 | 65,5 · 70,5 · 78,0 · 84,0 · 88,5 · 92,5 · 94,5 (koyu 94,5) | 65,5 · 84,0 · 88,5 · 92,5 · 94,5 (koyu 94,5) |

Kontak sayfaları: `~/is/uretim-0204/duz3-0201T/kontak-{yatay-01-05,dikey-01-05,dikey-06,koyu,kapak,dikey-168}.png`;
önceki kareler `~/is/uretim-0204/duz3-0201T/once/`. Bakış: taşma ve üst üste binme yok, künye "YDT · TEMEL",
yazılar sözcük zamanında, dikey altyazı yeni cümleleri gösterir.

## 4. Kapak

| | Önce | Sonra |
|---|---|---|
| Satır 1 | GİDİYORUM | GİDİYORUM |
| Satır 2 | = AM GOING | = I AM GOING |
| Küçük satır | -yor → -ing | kalktı |

Gerekçe: rapor satır 13 ve §4 "ses düzelince kapak …"; yeni c7 her -yor'un -ing olmadığını söyler, kapak aynı iddiayı taşır.
Karakter, saat ve renkler değişmedi. Üretici: `sahneler/90-hyperframes-kapak/uret.py` (yatay S 154, T1 500; dikey S 148),
`calistir.sh --tema acik|koyu`; assert'ler iki temada geçti. Dosyalar: `kapak.png`, `kapak-koyu.png` (iki paket),
`uretim-tutanagi/kapak-168.png` (yatay 168×94), dikey `uretim-tutanagi/kapak-168.png` + `kapak-koyu-168.png` (94×168).
168 px'te iki satır okunur. Eski kapaklar `~/Silinecekler/2026-11-16-duz3-0201T/` altında.

## 5. Yayın verisi

| Alan | Önce | Sonra |
|---|---|---|
| bolumler[].t | 0 · 15,44 · 30,15 · 45,98 · 62,81 | 0 · 16,48 · 31,19 · 47,02 · 63,85 |
| bildirimler[].t | 30,15 | 31,19 (c4 başı; ilk 30 sn ve son 20 sn dışında) |
| açıklama damgaları | 00:00 · 00:15 · 00:30 · 00:46 · 01:03 | 00:00 · 00:16 · 00:31 · 00:47 · 01:04 |

Bölüm süreleri 16,48 / 14,71 / 15,83 / 16,83 / 30,76 sn (≥ 10). Dikey `youtube.json` yatayla bayt eşit (`cmp`);
dikey açıklama yalnız `utm_content=dikey-tam` satırında ayrılır.

Tutarlılık kapısı: `cd K && /usr/bin/python3 uretim-hatti/betikler/yv-tutarlilik.py --kilitli simple-present-temel,simple-present-temel-dikey,02-04-ydt-temel-dikey`
→ **çıkış 1**, "toplam sorun: 6 · kilitli pakette: 0". 6 sorunun hepsi öteki ders: `simple-present-ileri` ve `-dikey`
bölüm 3/4/5 (t 32,45 / 48,29 / 61,41) zaman.json sahne başı değil. Bu iki pakette sorun yok.

## 6. Çakışma kapısı

Komut (sahne başına, ön planda): `node araclar/cakisma-kapisi.mjs <paket> --sahne <s> --json
projeler/<paket>/uretim-tutanagi/duz3-kareler/cakisma/<s>.json --port 41333 --sunucu 41022`.
Taban: aynı komut HEAD kopyasında (`git archive HEAD` + izlenmeyen lib/font/cizim/motorlar bağları,
`KALEM_KOK=~/is/uretim-0204/duz3-0201T/taban SAHNE_KARE_BETIK=K/araclar/sahne-kare.mjs`, geçici sunucu 41023).

| Sahne | Yatay çıkış (HEAD) | Dikey çıkış (HEAD) | Fark |
|---|---|---|---|
| 01 | 0 (0) | 0 (—) | yatay 1 uyarı t1×t2 10×7 px, HEAD'de aynı |
| 02 | 0 | 0 | çakışma yok |
| 03 | 0 | 0 | çakışma yok |
| 04 | 0 | 1 (1) | dikey 6 hata + 4 uyarı, HEAD'de aynı (+1,04 sn) |
| 05 | 0 | 1 (1) | dikey 1 hata `agac × is + climb-ing`, HEAD'de aynı |
| 06 | 1 (1) | 1 (1) | hatalar HEAD'de aynı (yatay 6, dikey 4: toplanma okları, kırmızı çizgi × was/were, dikey halka × V); yeni yalnız uyarı: aynı sözcüğün parçaları `koşu+yor`, `bili+yor+um` 7–13 px (yatay 2, dikey 3) |

Yeni hata 0. Çıktılar `uretim-tutanagi/duz3-kareler/cakisma/<sahne>.{json,log}`; taban `~/is/uretim-0204/duz3-0201T/taban/cakisma/`.

## 7. Kısa video (`present-continuous-s1`) — yalnız rapor, dokunulmadı

| Yer | Bulgu |
|---|---|
| Anlatım | jüri cümlesi YOK ("İki dilde de şimdiki zaman, ama gelecek demek." doğru) |
| Kapak/çip | "BU AKŞAM = I AM GOING" (`01-hyperframes-kapak/uret.py`, `02-paperjs-ornek/sahne-02.js`, `senaryo.json` satir2): "bu akşam" ≠ "I am going"; ana kapaktaki gibi "GİDİYORUM = I AM GOING" önerilir |
| surumler.json | amaç "altı kullanımı ayırt etmek" (ana dersteki eski iddia) |
| Rozet | `YDT · BASIC` (`yardim.py`, `senaryo.json`, BRIEF-S1) |

## 8. Düzeltilmeyenler

- mp4 dosyaları ve `uretim-tutanagi/art.json` (render sonrası ASR, mp4 sha'sına bağlı) bayat: render bu işte yasak.
- c7 p4 "Rumming" (0,96) ve c7 p2 "/biː/" okunuşu: Whisper eşiği geçti; c3/c4'teki eski Türkçe "be" okunuşuyla kulak farkı (EK-11) kaldı.
- c4 "bu günlerde" (TDK: bugünlerde), c4 "piyanonun başında değil", c5 "Look … söyler": ses değişmesin diye dokunulmadı (doğru ya da yazım düzeyinde).
- `surumler.json` kodu `ING-YDT-GR-01-PC`: kapsam dışı (rapor satır 18).
- Sahne RAPOR.md'leri, `huni-konu.*`, `on.json`, eski RAPOR.md: geçmiş tutanağı, eski tasarımı anlatır; değişmedi.
- Sözleşme ve Kovan: yazma alanı iki paketle sınırlı; şef yazar.
- YVJ ve kapak jürisi yeniden koşmalı (yeni kapak ve cümleler).
- Yazma boyutu kapısı 06 `uret.py` için 21 satırlık düzenlemeyi reddetti; atlama bayrağı açılmadı, aynı değişiklik 13 satırlık döngüyle yazıldı.

## 9. surumler.json

`revizyonlar` ana-yatay r2 ve dikey-tam r2 (DUZ3 notu, 2026-11-16T01:30:00Z, `cikti: null`); dikey-tam adı "… 95 sn".
