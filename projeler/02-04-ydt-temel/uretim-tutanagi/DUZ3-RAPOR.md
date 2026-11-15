# DUZ3-0204T — `02-04-ydt-temel`: dersin kendi içerik düzeltmeleri (jüri (c) sınıfı) · 16.11.2026

Girdi: `uretim-tutanagi/juri/DJ-hukum-1611-0019.md` (en son hüküm) · `juri-olcutleri.md` §1, §2b, §2c, §2f · `kapak-standardi.md` ·
`youtube-yayin-verisi-sozlesme.md` §2 · skill `motion-grafik-ders`. Önceki oturum bellek arızasıyla kesilmişti: başlangıçta senaryo ve
ses dokunulmamıştı (yalnız DUZ2 rozet farkları vardı); iş baştan yapıldı. Dikey eş: `../02-04-ydt-temel-dikey/uretim-tutanagi/DUZ3-RAPOR.md`.

| Ölçüm | Sonuç |
|---|---|
| Düzeltilen cümle / ekran metni | jüri 3 cümle + 1 ekran (s11) · kendi bulduğum 3 cümle + 1 ekran (s12) + kapak yazısı |
| Yeniden sentezlenen cümle | 5 (4, 7, 13, 14, 18) = 13 parça; öteki 13 cümle önbellekten, `cumle-N.wav` sha256 aynı (13/13) |
| Süre | 264,64 → 267,04 sn (+2,40) |
| Whisper | değişen 13 parçada en düşük 0,95 (13-2 "I'm living"); bütün ders 47/47 ≥ 0,85, en düşük 0,95 |
| Yeniden üretilen sahne | metin/süre: 04, 06, 11, 12, 14 · yalnız kayma: 05, 07, 08, 09, 10, 13 (yerel zaman aynı; HyperFrames çıktısı farksız) |
| Kapak | değişti: `KALICI mı / GEÇİCİ mi?` (açık + koyu, 168 px önizleme) |
| Çakışma kapısı | 11 sahne (04–14), hepsi çıkış **0** |
| Tutarlılık kapısı | çıkış **1**; 14 sorunun 14'ü `present-continuous*` (başka ders, başka oturum 16.11 01:02'de değiştirdi); 02-04: 0 sorun |
| Kısa video | `02-04-ydt-temel-s1` ve `-s1b` aynı "Hep orada" cümlesini taşıyor (§9; dokunulmadı) |
| Render | yok (mp4 yasak); `k/` kareleri yeniden çekildi |

## 1. Cümleler (önce → sonra)

| # | Yer | Önce | Sonra | Gerekçe | Kaynak |
|---|---|---|---|---|---|
| 1 | cümle 4 (ses + altyazı) | Ailemle İstanbul'da yaşıyorum. **Orada hep yaşıyorum.** Kalıcı durum: geniş zaman. | Ailemle İstanbul'da yaşıyorum. **Burası bizim evimiz.** Kalıcı durum: geniş zaman. | "hep" geniş zamanı "her zaman" ile eşitler (EK-5c). Jüri önerisi "uzun süredir yaşıyorum" da sorunlu: İngilizcede bu anlam present perfect ister (*I have lived here for a long time*); birebir denklik doğar. "Evimiz burada" kalıcı durumu mutlak sözcüksüz anlatır. Sözcük sayısı aynı (49), sahne 04 sözcük sırası bozulmaz. | jüri |
| 2 | cümle 7 | Tarife ya da program varsa **geniş zaman kullanırız.** | Tarife ya da program varsa **çoğunlukla** geniş zaman kullanırız. | Kapsamsız kural (EK-5b): *The train is leaving at seven tonight* da doğrudur. Jüri "genelde" önerdi; sonraki cümlede "genelde" zaten var, tekrar olmasın diye "çoğunlukla". | jüri |
| 3 | cümle 7 | **Planı bir kişi yapar:** ben, biz, arkadaşım. | **Planı insanlar yapar:** ben, biz, arkadaşım. | "bir kişi" ile "biz" çelişir. | kendim |
| 4 | cümle 13 | Geçici. **Ailenle hep orada yaşıyorsan:** I live in Istanbul. | Geçici. **Ailenle kalıcı olarak yaşıyorsan:** I live in Istanbul. | "hep" (EK-5c). Jüri "uzun süreli orada" önerdi; "kalıcı olarak" dersin kendi sorusuna ("Kalıcı mı, geçici mi?") bağlanır ve 4 sözcükte kalır. | jüri |
| 5 | sahne 11 ekranı | `I live in İstanbul. → always (permanent)` | `I live in İstanbul. → long-term (permanent)` | "always" = SP-s2 hatası (EK-5c); jüri önerisi alındı. | jüri |
| 6 | cümle 14 | Zaman sözcüğü **ve Türkçe ek ipucu verir.** Kararı anlam verir. | Zaman sözcüğü ipucu verir. **Türkçe ek yanıltabilir.** Kararı anlam verir. | Dersin tuzak bölümü (cümle 11–13) -yor ekinin iki zamanı da anlattığını, yanılttığını söyler; özet tersini diyordu (jüri "gerilimli" not düştü). Sözcük sayısı aynı (29). | kendim |
| 7 | sahne 12 ekranı | `time word · Turkish -yor → clue` | `time word → clue · -yor → trap` | Cümle 6 ile aynı iddia; "trap" dersin tuzak bölümünün adı. | kendim |
| 8 | cümle 18 | Sonraki derste **-ing almayan fiilleri** görüyoruz. | Sonraki derste **durum bildiren fiilleri** görüyoruz. | "-ing almaz" mutlak kural (istem; EK-5b): durum fiilleri eylem anlamında -ing alır (*I'm thinking about it*, *She's having lunch*). "durum bildiren" = Stative; kart "Stative" artık "durum" sözcüğüyle gelir. Whisper'ın "-ing"i yanlış duyduğu yer (eski "İENG'ye") de kalktı. | kendim |
| 9 | kapak | `HER ZAMAN mı / ŞİMDİ mi?` | `KALICI mı / GEÇİCİ mi?` | KS-4 kaldı (5 sözcük); yazı geniş zamanı "her zaman" diye çerçeveliyordu (EK-5c'nin kapaktaki izi). Yeni yazı dersin kilit sorusu (cümle 13, 18), 4 sözcük; kısa kapaklarla çakışmaz (s2 `GENEL / ŞU AN`). | jüri + kendim |

Taradım, doğru buldum (dokunmadım): cümle 1–3, 5, 6, 8–12, 15–17; sahne 06/07 zinciri `timetable → V1 / V-s` (özet kartı; sesi
"çoğunlukla" ile sınırlı); `surumler.json` amaçlar ve `canAlici` (mutlak iddia yok); `youtube.json` gönderi ve sabit yorum;
`youtube-aciklama.md` metni (bölüm adlarında iddia yok). Cümle 15'te A şıkkı (*this month he lives with us*) dil bilgisi olarak
kurulabilir; ders 17. cümlede anlamla eler (jüri kabul etti).

Aynı ifadenin düzeldiği dosyalar: `ortak/anlatim/senaryo.json` (parça + metin; bu pakette `meta.canAlici` alanı yok), `METIN.md`,
`altyazi.json`, `sozcukler.json`, `sureler.json`, `baslar.json`, `sentez.wav.rapor.json` · sahne 04 `sahne.js` (yorumlar) · 06 `uret.py`
(`T7("insanlar")`) · 11 `sahne.js` · 12 `uret.py` · 14 `uret.py` (`T(22, "durum")`) · 90 `uret.py` · `BRIEF.md` (satır 29, 40, 41, 65, 66 +
DUZ3 notu) · `SPEC.md` (04, 06, 90; DUZ3 notu) · `surumler.json` (r2). `youtube.json` ve `youtube-aciklama.md`'de aynı iddia yok;
yalnız zamanlar değişti (§6).

## 2. Ses

Komut (ön planda): `timeout 1500 bash araclar/ses-sunucu.sh --kok /home/sef/01dev/_worktrees/kalem-0204 02-04-ydt-temel` (kayıt
vekili; anahtar süreçten çıkmaz; `HIZ_EN=0.9`, `eleven_v4`). Önbellek anahtarı denetimi: eski 47 parçanın 47'si `HIZ_EN=0,9` anahtarıyla
önbellekte (0,8 ile 0). Çıktı: "kapı önbelleği 35 / 47 parça · 1116 karakter (≈ 5,47 TL) · 47 / 47 parça kapıdan geçti". Değişen
cümlenin bütün parçaları yeniden istenir (önceki/sonraki bağlamı değişir): cümle 4 (5 parça), 13 (5), 7, 14, 18 (1'er) = 13 parça.
"sözcük zamanı eksik parça 2" = cümle 3 ve 9 (önceden de eksikti; değişmedi).

Zincir: `sozcuk_uret.py` → `zaman_uret.py` → `kur.py` (anlatim.wav 267,04 sn) → `araclar/ses-paketle.py --yaz --paket 02-04-ydt-temel`
(m4a + imza) → `araclar/altyazi_uret.py` (47 parça; cümle 3 ve 9 uyarısı eskiden beri) → `metin_uret.py`. Eski dosyalar:
`/home/sef/Silinecekler/2026-11-16-duz3-0204T/once/` (sha256 listesi `sha256-once.txt`).

## 3. Süre, Whisper ve sahne zamanları

| Cümle | Parça | Dil | Metin | Duyulan (Whisper) | Benzerlik | Tohum |
|---|---|---|---|---|---|---|
| 4 | 1 | tr | İkinci örnek. Kancadaki fiil: live. | İkinci örnek, kancadaki fiil, live. | 1.00 | 0 |
| 4 | 2 | en | I live in Istanbul with my family. | I live in Istanbul with my family. | 1.00 | 0 |
| 4 | 3 | tr | Ailemle İstanbul'da yaşıyorum. Burası bizim evimiz. Kalıcı durum: geniş zaman. | Ailemle İstanbul'da yaşıyorum. Burası bizim evimiz. Kalıcı durum, geniş zaman. | 1.00 | 0 |
| 4 | 4 | en | My parents are out of town, so I am living with my uncle. | My parents are out of town, so I am living with my uncle. | 1.00 | 0 |
| 4 | 5 | tr | Ailem şehir dışında, bu yüzden amcamla yaşıyorum. Bu yalnız şimdilik. Geçici durum: şimdiki zaman. | Ailem şehir dışında, bu yüzden amcamla yaşıyorum. Bu yalnız şimdilik. Geçici durum, şimdiki zaman. | 1.00 | 0 |
| 7 | 1 | tr | Planı insanlar yapar: ben, biz, arkadaşım. Tren plan yapmaz, tarifeye uyar. Tarife ya da program varsa çoğunlukla geniş zaman kullanırız. Tarife cümlelerinde özne genelde cansızdır: tren, uçak, ders. | Planı insanlar yapar. Ben, biz, arkadaşım. Tren plan yapmaz. Tarifeye uyar. Tarife ya da program varsa çoğunlukla geniş zaman kullanırız. Tarife cümlelerinde özne genelde cansızdır. Tren, uçak, ders. | 1.00 | 0 |
| 13 | 1 | tr | Olur, ama anlam değişir. | Olur ama anlam değişir. | 1.00 | 0 |
| 13 | 2 | en | I am living in Istanbul. | I'm living in Istanbul. | 0.95 | 0 |
| 13 | 3 | tr | Şimdilik İstanbul'da yaşıyorum demek. Geçici. Ailenle kalıcı olarak yaşıyorsan: | Şimdilik İstanbul'da yaşıyorum demek. Geçici. Ailenle kalıcı olarak yaşıyorsan… | 1.00 | 0 |
| 13 | 4 | en | I live in Istanbul. | I live in Istanbul. | 1.00 | 0 |
| 13 | 5 | tr | Türkçede yor eki iki durumu da anlatır. İngilizcede ikisi ayrılır. Kalıcı mı, geçici mi? Önce bunu sor. | Türkçe'de yor eki iki durumu da anlatır. İngilizce'de ikisi ayrılır. Kalıcı mı, geçici mi? Önce bunu sor. | 1.00 | 0 |
| 14 | 1 | tr | Özet. Genel durum, kalıcı durum ve tarifeli gelecek: geniş zaman. Konuşma anı, geçici durum ve planlanmış gelecek: şimdiki zaman. Zaman sözcüğü ipucu verir. Türkçe ek yanıltabilir. Kararı anlam verir. | Özet. Genel durum, kalıcı durum ve tarifeli gelecek geniş zaman. Konuşma anı, geçici durum ve planlanmış gelecek şimdiki zaman. Zaman sözcüğü ipucu verir. Türkçe ek yanıltabilir. Kararı anlam verir. | 1.00 | 0 |
| 18 | 1 | tr | Dil sınavında boşluğu görünce üç soru sor. Genel mi, şu an mı? Kalıcı mı, geçici mi? Tarife mi, plan mı? Sonraki derste durum bildiren fiilleri görüyoruz. Görüşürüz. | Dil sınavında boşluğu görünce 3 soru sor. Genel mi? Şu an mı? Kalıcı mı? Geçici mi? Tarife mi? Plan mı? Sonraki derste durum bildiren fiilleri görüyoruz. Görüşürüz. | 1.00 | 0 |

| Cümle | Süre önce (sn) | Süre sonra (sn) | Fark |
|---|---|---|---|
| 4 | 24.44 | 25.00 | +0.56 |
| 7 | 14.96 | 16.08 | +1.12 |
| 13 | 20.76 | 20.28 | -0.48 |
| 14 | 14.48 | 15.60 | +1.12 |
| 18 | 12.32 | 12.40 | +0.08 |

Değişen 5 cümle: 13 parça yeniden sentezlendi; tüm ders en düşük benzerlik 0.95; 47/47 ≥ 0,85.

| Sahne | t_bas önce → sonra (sn) | Δ | kare önce → sonra | Değişiklik |
|---|---|---|---|---|
| 01-hyperframes-giris | 0.00 → 0.00 | +0.00 | 102 → 102 | yok |
| 02-paperjs-kanca | 3.00 → 3.00 | +0.00 | 529 → 529 | yok |
| 03-paperjs-ornek1 | 20.22 → 20.22 | +0.00 | 721 → 721 | yok |
| 04-canvas-ornek2 | 43.85 → 43.85 | +0.00 | 762 → 779 | metin + süre |
| 05-canvas-ornek3 | 68.84 → 69.40 | +0.56 | 747 → 747 | yalnız kayma |
| 06-hyperframes-soru1 | 93.35 → 93.91 | +0.56 | 613 → 646 | metin + süre |
| 07-hyperframes-kural | 113.37 → 115.05 | +1.68 | 523 → 523 | yalnız kayma |
| 08-canvas-karsit1 | 130.40 → 132.08 | +1.68 | 459 → 459 | yalnız kayma |
| 09-canvas-karsit2 | 145.29 → 146.97 | +1.68 | 523 → 523 | yalnız kayma |
| 10-hyperframes-tuzak | 162.33 → 164.01 | +1.68 | 656 → 656 | yalnız kayma |
| 11-canvas-tuzak-cevap | 183.79 → 185.47 | +1.68 | 657 → 643 | metin + ekran + süre |
| 12-hyperframes-ozet | 205.30 → 206.50 | +1.20 | 463 → 497 | metin + ekran + süre |
| 13-hyperframes-mini-soru | 220.33 → 222.65 | +2.32 | 940 → 940 | yalnız kayma |
| 14-hyperframes-kapanis | 251.27 → 253.59 | +2.32 | 431 → 434 | metin + süre |

Toplam süre: 264.64 → 267.04 sn.

## 4. Sahneler

| Sahne | Ne yaptım |
|---|---|
| 04 kanvas | `KARE 762 → 779`, `ICERIK 750 → 767`; sözcükler sıra ile (`t(i)`), sayısı aynı (49); "hep" yorumları; `calistir.sh` `N` ve `GLOBAL_SN` (sözcüğe göre: 56,52 · 63,74 · 69,2) |
| 05, 08, 09 kanvas | süre aynı, yalnız kayma: `KAYMA = −0,56 / −1,68`, `kayma: KAYMA` (sahne-ortak'ın var olan düzeni). `TBAS` ve sabit zamanlar eski çerçevede kalır; çakışma kutu sayısı DUZ2 ile birebir (1.981 · 676 · 1.972) |
| 06 HyperFrames | `T7("kişi") → T7("insanlar")` (figür + "person" zinciri); `KARE 613 → 646`; `ONIZLE_YALNIZ=1 bash calistir.sh --tema acik` |
| 07, 10, 13 HyperFrames | yeniden üretildi; `index.html` ve `olaylar.json` farkı yalnız DUZ2 rozeti (yerel zaman aynı) |
| 11 kanvas | `KARE 657 → 643`, `KAYMA −1,68`; not `always → long-term`; cümle içi sabit zamanlar sözcüğe bağlandı (now `İstanbul'da + 0,32`, `Ailenle + 0,42`, `(permanent)` `yaşıyorsan: + 0,35`, baş sallama `Kalıcı − 0,44`); `calistir.sh` `N`, `GLOBAL_SN` |
| 12 HyperFrames | madde 3 `time word → clue · -yor → trap` (iki ok kısa: `AU3 = u(64)`, satır 931 ≤ sınır 946); `KARE 463 → 497` |
| 14 HyperFrames | kart "Stative" `T(22, "durum")`; `KARE 431 → 434` |
| 90 kapak | `SATIR1/2`; dikey için yazı tavanı 140 px ve "nesne sığmıyor" kuralı (bkz. §7); yatay `index.html` iki koşuda aynı |

Rozet `YDT · BASIC` hiçbir karede yok; künye bütün karelerde `YDT · TEMEL` (HV-24 kaynakta DUZ2'de düzelmişti; bu iş kareleri tazeledi).
Depodaki HyperFrames `index.html` tema durumu HEAD ile aynı (yatay açık, kapak koyu).

## 5. Kareler (kendi bakışım)

Araç: `bash araclar/qa-yerel.sh <paket> <sahne> <açık_t…> <koyu_t> --kapisiz` (sahne sahne; `sahne-kare.mjs`, ortak Chrome 41333,
önizleme 41022). Eski `k/` içeriği (14.11 render kareleri, BASIC rozetli) `/home/sef/Silinecekler/2026-11-16-duz3-0204T/k-eski/`
altında. Zamanlar eski kare adlarından sözcük hizasıyla çevrildi.

Kontak sayfaları: `uretim-tutanagi/duz3-kareler/kontak-yatay-acik-degisen.png` (04, 06, 11, 12, 14) ·
`kontak-yatay-koyu.png` (14 sahne) · `kontak-kapak.png`.

Bakış: taşma, çakışma, okunmayan yazı yok. 11'de `long-term (permanent)` kart içinde, sarı çizgi `(permanent)` altında; 12'de madde 3
bandın içinde, `clue` hapı ile `· -yor` arası 8 px nefes payıyla ayrık (ilk çekimde sıkışıktı, düzelttim, yeniden çektim); 14'te kart
`Next lesson · Stative Verbs`. Yatay sahnelerde altyazı yok (tasarım).

Yeni kareler (`sahneler/<sahne>/k/` açık, `k/koyu/` koyu):

| Sahne | Açık (t, sn) | Koyu |
|---|---|---|
| 01-hyperframes-giris | 1.25, 2.45, 2.9 | 2.9 |
| 02-paperjs-kanca | 14.6, 16.9, 20.1, 5.8, 9.9 | 14.6 |
| 03-paperjs-ornek1 | 32.2, 37.6, 43.6 | 43.6 |
| 04-canvas-ornek2 | 56.52, 63.74, 69.2 | 69.2 |
| 05-canvas-ornek3 | 79.96, 84.76, 93.86 | 93.86 |
| 06-hyperframes-soru1 | 107.52, 114.82, 98.16 | 109.48 |
| 07-hyperframes-kural | 121.08, 125.78, 130.58, 131.98 | 129.28 |
| 08-canvas-karsit1 | 139.98, 142.78, 146.68 | 145.58 |
| 09-canvas-karsit2 | 148.08, 156.18, 159.38, 163.88 | 163.88 |
| 10-hyperframes-tuzak | 174.21, 179.01, 185.41 | 185.41 |
| 11-canvas-tuzak-cevap | 194.05, 199.32, 204.08, 205.5 | 200.76 |
| 12-hyperframes-ozet | 212.18, 217.02, 222.6 | 222.6 |
| 13-hyperframes-mini-soru | 228.32, 232.22, 236.52, 241.32, 248.22, 253.32 | 236.52 |
| 14-hyperframes-kapanis | 258.48, 262.66, 265.92 | 265.26 |

## 6. Çakışma kapısı

Komut (sahne başına, ön planda): `timeout 280 node araclar/cakisma-kapisi.mjs 02-04-ydt-temel --sahne <s> --json uretim-tutanagi/duz3-kareler/cakisma/<s>.json --port 41333 --sunucu 41022`. Sahne 01–03 değişmedi (DUZ2'de 0).

| Sahne | Çıkış | Örnek | Kutu |
|---|---|---|---|
| 04-canvas-ornek2 | 0 | 104 | 2179 |
| 05-canvas-ornek3 | 0 | 99 | 1981 |
| 06-hyperframes-soru1 | 0 | 86 | 61612 |
| 07-hyperframes-kural | 0 | 69 | 43884 |
| 08-canvas-karsit1 | 0 | 61 | 676 |
| 09-canvas-karsit2 | 0 | 69 | 1972 |
| 10-hyperframes-tuzak | 0 | 87 | 32229 |
| 11-canvas-tuzak-cevap | 0 | 85 | 1594 |
| 12-hyperframes-ozet | 0 | 66 | 43175 |
| 13-hyperframes-mini-soru | 0 | 125 | 39812 |
| 14-hyperframes-kapanis | 0 | 55 | 5811 |

## 7. Kapak

Komut (sırayla, tek tarayıcı): `bash sahneler/90-hyperframes-kapak/calistir.sh --tema acik|koyu` iki pakette (paketin kendi üreticisi;
`hyperframes snapshot`, mp4 yok). Eski kapaklar betik tarafından `~/Silinecekler/2026-11-16-kapak/` altına taşındı.

| Dosya | Ölçü | Yazı | Not |
|---|---|---|---|
| `kapak.png` · `kapak-koyu.png` | 1920 × 1080 | `KALICI mı` / kutulu `GEÇİCİ mi?` | S1 170 · S2 188 · karakter ölçeği 0,99 |
| `../02-04-ydt-temel-dikey/kapak.png` · `kapak-koyu.png` | 1080 × 1920 | aynı | S1 140 · S2 168 · karakter ölçeği 0,66 (eski 0,67) |
| `uretim-tutanagi/kapak-168.png` | 168 × 94 | okunur | eskisi `Silinecekler/…/once/kapak-168-yatay-eski.png` |

Karakter ve nesne aynı. `GEÇİCİ` İ/Ç doğru çizili. Üretici değişikliği (iki pakette aynı dosya): dikeyde kısa satır 1 yazıyı 170 px'e
büyütüyor, nesneye yer kalmayınca `ValueError` ile duruyordu; şimdi (a) dikey yazı tavanı 140 px, (b) avuç üstüne hedef boyun
%60'ından küçük sığan nesne adayı kapıda reddedilir, arama sürer.

## 8. Yayın verisi zamanı

`youtube.json` `bolumler[].t` = sahne `t_bas` (ders zamanı), `bildirimler[].t` = cümle başı; `youtube-aciklama.md` damga bloğu
`int(t + 0,5)` ile (kapının yöntemi). Dikey `youtube.json` yatayla bayt bayt aynı; dikey açıklama yalnız `utm_content` farklı.

| Bölüm | t önce → sonra (sn) | Damga önce → sonra |
|---|---|---|
| Yaşıyorum: I live mi, I am living mi? | 0.0 → 0.0 | 00:00 → 00:00 |
| Genel durum ve konuşma anı: wear | 20.22 → 20.22 | 00:20 → 00:20 |
| Kalıcı ve geçici durum: live | 43.85 → 43.85 | 00:44 → 00:44 |
| Tarifeli ve planlanmış gelecek | 68.84 → 69.4 | 01:09 → 01:09 |
| Tren örneği: tarife mi, plan mı? | 93.35 → 93.91 | 01:33 → 01:34 |
| Üç fark tek kartta | 113.37 → 115.05 | 01:53 → 01:55 |
| Aynı sözcük today: konuşma anı | 130.4 → 132.08 | 02:10 → 02:12 |
| Saatle gelen today: tarife | 145.29 → 146.97 | 02:25 → 02:27 |
| Tuzak: Türkçedeki -yor eki | 162.33 → 164.01 | 02:42 → 02:44 |
| I live ve I am living: anlam farkı | 183.79 → 185.47 | 03:04 → 03:05 |
| Özet: hangi durumda hangi zaman? | 205.3 → 206.5 | 03:25 → 03:27 |
| Mini soru: boşluğa hangi şık? | 220.33 → 222.65 | 03:40 → 03:43 |
| Sınavda soracağın üç soru | 251.27 → 253.59 | 04:11 → 04:14 |

En kısa bölüm 13.45 sn (≥ 10). Bildirimler: 69.39 → 69.95, 184.54 → 186.22 (cümle 5 ve 13 başı; ilk 30 sn ve son 20 sn dışında).

Tutarlılık kapısı: `python3 uretim-hatti/betikler/yv-tutarlilik.py --kilitli simple-present-temel,simple-present-temel-dikey,02-04-ydt-temel-dikey`
→ **çıkış 1**. 02-04 satırları: yatay ve dikey `başlık 52 kr · açıklama 972 B · etiket 133 · bölüm 13 · süre 267.04 sn`; `zaman`
ölçütündeki 14 sorunun hepsi başka derste: `present-continuous`, `-dikey`, `-ileri`, `-ileri-dikey` bölüm 2–5 "zaman.json sahne başı
değil" (o paketlerin `zaman.json`'ı 16.11 01:02'de başka bir oturumda değişti). Öteki 9 ölçüt `[TAMAM] 0`. Yalnız raporlanır.

## 9. Kısa video (yalnız rapor, dokunulmadı)

`02-04-ydt-temel-s1` ve `02-04-ydt-temel-s1b` aynı EK-5c hatasını taşıyor: **"Hep orada: kalıcı durum, geniş zaman."**

| Dosya | Yer |
|---|---|
| `02-04-ydt-temel-s1/ortak/anlatim/senaryo.json` | satır 55 (parça), 67 (metin) |
| `02-04-ydt-temel-s1/ortak/anlatim/altyazi.json` | satır 31 |
| `02-04-ydt-temel-s1/sahneler/02-paperjs-ornek/sahne-02.js` | satır 63, 341–348 (ekranda soluk TR satırı "Hep orada.") |
| `02-04-ydt-temel-s1b/…` | aynı üç dosya (senaryo 55/67, altyazı 31, sahne-02.js 61, 331–338) |

s2, s2b, s3, s3b: aynı yanlış cümle yok (s3'te "Planı bir kişi yapar" DUZ2'de düzelmişti).

## 10. Dokunulmayan maddeler (ölçüt hatası / insan kanıtı / render yasağı)

| Kimlik | Durum | Neden |
|---|---|---|
| KS-4 | kapak 4 sözcüğe indi, ama ölçüt çelişkisi sürer | `kapak-standardi.md` §3 örneği 5 sözcüklü; madde "2–4", istem "2–5" diyor. Standart notu şefin kararı. |
| HV-24 (mp4) | `k/` tazelendi; mp4 eski | render yasağı: `cikti.mp4`, `cikti-koyu.mp4`, sahne `video*.mp4`, `kontrol*.png`, `_is/` eski ses, eski metin ve BASIC rozeti taşır. Yayından önce şef derlemesi gerekir. |
| EK-11 | kanıt yok | dinleme insan işi. Yeni 13 parça dinlenmeli: "Burası bizim evimiz", "çoğunlukla", "insanlar", "kalıcı olarak", "yanıltabilir", "durum bildiren"; eski not "wear" ve cümle 6 "-ing" sürer. |
| DK-1, DK-3, ST-2, EK-3, EK-12 | kanıt yok | render ya da `hyperframes check` / `huni-kapi.mjs` çıktısı gerekir (render yasağı). |
| EK-4 | kanıt yok | görsel jüri adres kaydı şefin işi. |
| Kanvas `olaylar.json` (04, 11) | eski | ses olayı listesi render yakalamasının yan ürünü (`yakala.py`); süresi değişen 04 ve 11'de render ile tazelenir. HyperFrames `olaylar.json` (06, 12, 14) tazelendi. |

## 11. Açık kalanlar

- mp4 derlemesi (şef; render yasağı).
- Kısa video s1/s1b "Hep orada" düzeltmesi (ayrı istem).
- `BRIEF.md` tablo saniyeleri 15.11 zamanlarıdır (belgeye not düşüldü; geçerli olan `zaman.json`).
- Tarihî kayıtlar (`sahneler/*/RAPOR.md`, `uretim-tutanagi/*`) eski metni anlatır; dokunulmadı.
- git commit yok (şef atar). Yeni dosyalar: bu rapor, `uretim-tutanagi/duz3-kareler/` (kontak sayfaları + `cakisma/*.json,log`).
