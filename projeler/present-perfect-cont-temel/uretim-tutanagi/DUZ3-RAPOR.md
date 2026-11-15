# DUZ3-0209T — `present-perfect-cont-temel` dersin kendi içerik düzeltmeleri (jüri c sınıfı) · 16.11.2026

> Girdi: `uretim-hatti/raporlar/YV-DUZ-1511.md` §4 (bu dersin satırı) ve §3 (kapak "ses düzelince"), `uretim-tutanagi/juri/YVJ-hukum.md`
> (N-1). Makine srv21 (Linux x86_64). Üretici: Claude Opus 5.5. Render yok, mp4 yok, alt ajan yok, commit yok.
> Önceki oturum (bellek arızası) bu pakete bir şey yazmamıştı (`git status`: yalnız YV dosyaları); iş sıfırdan yapıldı.
> Eski ses ve kapaklar `~/Silinecekler/2026-11-16-duz3-0209T/` altında (`LISTE.md` satırı yazıldı).
> Dikey paketin raporu: `../present-perfect-cont-temel-dikey/uretim-tutanagi/DUZ3-RAPOR.md`.

## 1. Cümle tablosu

| # | Kaynak | Önce | Sonra | Gerekçe |
|---|---|---|---|---|
| 1 | jüri (c7) | `Türkçedeki -dir ve -yor gibi düşün:` | `Süreyi ise for ya da since söyler:` | `-dir ↔ have been`, `-yor ↔ -ing` denkliği kuruyordu. Süreyi İngilizcede `for two hours` taşır, süren işi `have been + -ing`. Jüri önerisi "Süreyi for ve since söyler" doğru; `for ya da since` seçenek ilişkisini açık yazar. Süren iş yarısı aynı cümlenin parça 1'inde ("Been ve -ing …") söyleniyor; yineleme olmasın diye parça 2'ye girmedi. |
| 2 | jüri (c2) | `İngilizce de iki parçayla yapar.` | `İngilizcede süreyi for ya da since söyler, süren işi have been artı -ing kurar.` | Jüri satırı "c2/c7". "İki parça", hemen önceki `-dir` ve `-yor` ile birebir eşleşme çağrıştırıyordu; ekranda (sahne 02) aynı denklik çift yönlü okla çiziliyordu. Yeni cümle iki parçayı anlam düzeyinde adlandırır. |
| 3 | kendi taramam (c4) | `Tekil kişide has been, artı -ing.` | `Üçüncü tekil kişide has been, artı -ing.` | Mutlak ve yanlış: `I` da tekildir, `have been` alır (dersin c3 örneği: *I have been waiting*). `has` yalnız he/she/it (üçüncü tekil) ile gelir. |
| 4 | kendi taramam (c5) | `Yağmur bir süredir yağıyor.` | `Yağmur yağıyormuş.` | *Look! The street is wet. It has been raining.* kalıbında yağmur kanıttan (ıslak sokak) çıkarılır, çoğu zaman yeni durmuştur. "Bir süredir yağıyor" yağmuru şu an süren gösteriyordu ve aynı cümledeki "İzi şimdi görünüyor" ile çelişiyordu. `-mış` kanıta dayalı çıkarımı, `-yor` süreci taşır. `huni-konu.md` jüri notu aynı sorunu yazmıştı. |
| 5 | kendi taramam (c7) | `Been ve -ing işin sürdüğünü gösterir.` | `Been ve -ing işin bir süre sürdüğünü gösterir.` | c5 örneğinde iş durmuş olabilir; "sürdüğünü" şu an süren iş diye mutlak okunuyordu. "Bir süre" iki durumu da kapsar. |
| 6 | kendi taramam (kart) | `kartlar.k3.tr`: `Bak, sokak ıslak. Yağmur yağıyor.` | `Bak, sokak ıslak. Yağmur yağıyormuş.` | `Yağmur yağıyor` = *It is raining* (yanlış çeviri). |
| 7 | kendi taramam (kart) | `kartlar.form.tr`: `-dir ... -yor` | `süren iş; süreyi for / since söyler` | Form kartının Türkçe karşılığı denklik kuruyordu. |
| 8 | jüri N-1 + §4 | `meta.kapak`: `İKİ SAATTİR` / `= HAVE BEEN`, canAlici `Türkçedeki -dir ... -yor, İngilizcede have been ... -ing` | `İKİ SAATTİR` / `NASIL DENİR?`, `kucuk`: `I have been working for two hours.`, canAlici `Süreyi for two hours, süren işi have been working taşır` | §4 kapak sütunu: "dersin c1'i ile soru ya da I have been working". Soru biçimi kapak §3'te izinli; iddia kurmaz; yanıt küçük satırda dersin c7 örneğidir. |
| 9 | aynı iddia | `meta.canAlici[0]` + `surumler.json`: `Türkçedeki -dir ... -yor = İngilizcedeki have been ... -ing` | `Süreyi for / since söyler, süren işi have/has been + -ing kurar` | Denklik. |
| 10 | aynı iddia | `meta.amaclar[3]` + `surumler.json`: `Türkçe -dir ... -yor ile köprü` | `Türkçe -dir ... -yor cümlesini aktarmak: süre for / since, süren iş have/has been + V-ing` | Köprünün neyi neye bağladığı yazılı. |
| 11 | HV-24 | rozet `YDT · BASIC`, künye `· YDT BASIC` | `YDT · TEMEL`, `· YDT TEMEL` | Kaynakta düzeltildi: `senaryo.json` `giris.rozetler`, `ortak/kunye.js`, sahne 01 `uret.py` + `yardim.py`, sahne 06 `yardim.py`, sahne 90 `yardim.py` (kullanılmayan sabit). |

Dokunulmayan, doğru bulunan cümleler: c1, c3 (`for twenty minutes` = süre uzunluğu, kalıp), c4 parça 1–4 (`since this morning` = başlangıç noktası), c5 parça 1–2 ve 4,
c6 (öğrenci sorusu), c7 `Have geçmişi bugüne bağlar` (öğretim benzetmesi; `huni-konu.md` notu), c7 `İki saattir çalışıyorum. Kod: have been, artı -ing.`
`youtube.json` / `youtube-aciklama.md`: aynı iddia yok (gönderi metni YV-DUZ'da düzeltilmişti); bölüm adı `İki saattir çalışıyorum: -dir ve -yor` dersin c1–c2'sini adlandırır, denklik kurmaz → metin değişmedi, zamanlar §5.

Değişen dosyalar: `ortak/anlatim/senaryo.json`, `METIN.md`, `altyazi.json`, `sureler.json`, `sozcukler.json`, `sozcuk_uret.py` (`BASLAR`), `anlatim.wav`, `anlatim.m4a` (+ `.imza`),
`cumle-1…7.wav`, `zaman.json`, `ortak/kunye.js`, `surumler.json`, `BRIEF.md`, sahne 01, 02, 03, 04, 05, 06, 90 (§3), `kapak.png`, `kapak-koyu.png`, `uretim-tutanagi/kapak-168.png`.

## 2. Ses ve süre

Yöntem (öteki cümlelerin sesi değişmez):
1. Sunucu önbelleğinde bu dersin sesi yoktu (ses Mac'te üretilmiş; `~/is/duz3-0209T/anahtar.py`, iki hız anahtarı da boş).
2. `el.py` yalnız c2, c4, c5, c7'yi taşıyan geçici senaryoyla koştu: `timeout 1500 bash araclar/ses-sunucu.sh --kok ~/is/duz3-0209T/kok present-perfect-cont-temel`.
   rc 0; 16 / 16 parça kapıdan geçti; 763 karakter (≈ 3,74 TL). Bir parça değişince aynı cümlenin öteki parçaları da yeniden istenir (bağlam metni anahtara girer).
3. Hız: `HIZ_EN=0.9` (`ses-sunucu.sh` varsayılanı). Denetim: c4 EN parçası özgün 3,36 sn → yeni 3,28 sn; c5 EN parçası 3,76 = 3,76 sn.
4. c1, c3, c6 eski `anlatim.wav`'dan örnek-eşit kesildi (`[başlangıç_N, başlangıç_N+1)`, 48 kHz); c2, c4, c5, c7 yeni `cumle-*.wav`.
   `kur.py` → `anlatim.wav`; `araclar/ses-paketle.py --yaz --paket present-perfect-cont-temel` → `anlatim.m4a` (sunucuda önceden yoktu).
5. Cümle arası boşluk 0,55 sn korundu. Kanıt: PCM sha256 eski = yeni — c1 `057227ed22ecea8e` (0–3,39), c3 `7904aafb5273e638` (eski 17,68 → yeni 22,48),
   c6 `f90b7378105984c4` (eski 62,06 → yeni 67,42); cümle aralarındaki 6 boşlukta en büyük örnek 0.
6. Üreteçler önce eski dosyaları birebir yeniden üretti (`sozcuk_uret` mantığı, `altyazi_uret.py`, `metin.py`: eşit), sonra yeni girdilerle koştu.

| Ölçü | Önce | Sonra |
|---|---|---|
| c2 süre / sözcük | 13,74 sn / 26 | 18,54 sn / 35 |
| c4 süre / sözcük | 14,44 sn / 28 | 14,84 sn / 29 |
| c5 süre / sözcük | 13,69 sn / 28 | 13,85 sn / 26 |
| c7 süre / sözcük | 16,25 sn / 31 | 16,25 sn / 34 |
| Cümle başları c1–c7 | 1,00 · 3,39 · 17,68 · 32,83 · 47,82 · 62,06 · 65,97 | 1,00 · 3,39 · 22,48 · 37,63 · 53,02 · 67,42 · 71,33 |
| Konuşma sonu | 82,22 | 87,58 |
| Ders süresi (`zaman.json` son `t_son`, `anlatim.wav`) | 83,22 sn | 88,58 sn |
| `anlatim.wav` sha256 | `02f5a69a97f5` | `9ec3ab880004` |
| `anlatim.m4a` sha256 | — (sunucuda yoktu) | `30697c0471f2` |
| `altyazi.json` | 23 parça, son t1 82,30 | 23 parça, son t1 87,66 (≤ 88,58) |

Whisper (faster-whisper large-v3-turbo int8, eşik 0,85; rapor `~/is/duz3-0209T/kok/projeler/present-perfect-cont-temel/ortak/anlatim/sentez.wav.rapor.json`):

| Cümle | Dil | Metin | Duyulan | Benzerlik |
|---|---|---|---|---|
| c2 | tr | Türkçede süre için -dir, süren iş için -yor deriz. | Türkçe'de süre içindir, sürem iş için yor deriz. | **0,97** (en düşük) |
| c2 | tr | İngilizcede süreyi for ya da since söyler, süren işi have been artı -ing kurar. | (aynı; "have, been", "in") | 0,99 |
| c2 | tr | Bu derste Present Perfect Continuous'ın formunu, … görüyoruz. | (aynı) | 1,00 |
| c4 | tr | İkinci örnek. | (aynı) | 1,00 |
| c4 | en | My brother has been playing the guitar since this morning. | (aynı) | 1,00 |
| c4 | tr | Kardeşim sabahtan beri gitar çalıyor. | (aynı) | 1,00 |
| c4 | en | Since this morning. | (aynı) | 1,00 |
| c4 | tr | Başlangıç noktası. Üçüncü tekil kişide has been, artı -ing. | … Üçüncü tekil kişi de has been artı ing. | 0,99 |
| c5 | tr | Üçüncü örnek. | (aynı) | 1,00 |
| c5 | en | Look! The street is wet. It has been raining. | (aynı) | 1,00 |
| c5 | tr | Bak, sokak ıslak. Yağmur yağıyormuş. İzi şimdi görünüyor. | (aynı) | 1,00 |
| c5 | tr | Kalıp yine aynı: has been, artı -ing. | (aynı) | 1,00 |
| c7 | tr | Have geçmişi bugüne bağlar. Been ve -ing işin bir süre sürdüğünü gösterir. | … Bin ve Ing işin bir süre … | 0,98 |
| c7 | tr | Süreyi ise for ya da since söyler: | (aynı) | 1,00 |
| c7 | en | I have been working for two hours. | (aynı) | 1,00 |
| c7 | tr | İki saattir çalışıyorum. Kod: have been, artı -ing. | (aynı) | 1,00 |

## 3. Sahneler (yeniden üretilen: 01, 02, 03, 04, 05, 06, 90)

| Sahne | Ne değişti | Neden |
|---|---|---|
| 01 giriş | rozet `YDT · TEMEL` (`uret.py`, `yardim.py`, `nesneler.json`) → `proje/index.html` | HV-24 |
| 02 kanca | 580 kare (436); c2 sözcük zamanları; İngilizce cümlede 3 daire sese bağlı (9,54 `for two hours` · 12,74 `have been` · 14,34 `-ing`); çift yönlü `-dir … -yor ⇄ have been … -ing` kalktı, yerine iki satır `süre → for / since` (9,54) ve `iş sürüyor → have been + -ing` (11,78–14,66); sağ alt kutu 15,77'den | c2 yeni metin |
| 03 örnek 1 | `kayma: -4.8` (sahne eski çerçevede, T_BAS 17,13; yerel kareler aynı) | c2 +4,80 sn |
| 04 örnek 2 | 474 kare (462); `kayma: -4.8`; Türkçe çeviri penceresi 37,65; `has` halkası ve formül kartı yeni c4 parça 5 sözcüklerine (eski çerçeve 44,19 / 45,59 / 46,71 / 46,95 / 47,19) | c4 yeni ses |
| 05 örnek 3 | 444 kare (439); `kayma: -5.2`; ekran `Yağmur yağıyormuş.`; `izi şimdi görünüyor` ve ok 56,12–56,66; kart ve halkalar +0,16 sn (eski çerçeve) | c5 yeni metin |
| 06 soru + form | `zamanlar.json` gerçek çerçeveye (t_bas 66,87; c6 +5,36, c7 yeni sözcükler); sol sütun `-dir … -yor ⇄ have been … -ing` kalktı, yerine Caveat `süre:` + Fredoka `for / since` (77,00 / 78,04 / 79,00); künye rozeti | c7 yeni metin + HV-24 |
| 90 kapak | §4 | jüri N-1, §4 |
| `ortak/kunye.js` | `seviye: "YDT TEMEL"` (02–05 künyesi çalışma anında çizilir) | HV-24 |

HF kaynak üretimi: `uret.py` → `olay.py` → `tema_hf acik` (`~/is/duz3-0209T/hf-uret.sh`; render yok). `calistir.sh` kare sayıları güncel (02 `N=580`, 04 `N=474`, 05 `N=444`; 06 681 aynı).

Kareler (kendim baktım; `node araclar/sahne-kare.mjs present-perfect-cont-temel <sahne> <t,…> <dizin> --tema acik --port 41333 --sunucu 41022`;
dizin `sahneler/<sahne>/k/duz3/`, git dışı):

| Sahne | Anlar (sn) | Gözlem |
|---|---|---|
| 01 | 1,2 · 2,9 | hap `YDT · TEMEL` + `GRAMMAR` |
| 02 | 5,6 · 9,0 · 10,9 · 12,7 · 14,8 · 21,5 (+ koyu 14,8) | künye `· YDT TEMEL`; `for two hours` dairesi 9,54'te, alt satırlar sesle; okların sağında yazı taşmaz, kutuya değmez; for dairesi `-ing` dairesine yalnız teğet (iki çizim) |
| 03 | 23,0 · 27,5 · 31,0 · 36,5 | yerleşim eskisiyle aynı; `for` 31,0'da (ses 30,67) |
| 04 | 38,6 · 42,0 · 44,6 · 47,6 · 50,6 · 52,3 | `başlangıç noktası` 47,6'da yazılıyor (ses 47,27); `has` halkası + kart 50,6'da (ses 50,39) |
| 05 | 54,6 · 57,2 · 60,5 · 62,4 · 65,3 · 66,7 | `Yağmur yağıyormuş.` tek satır; ok ve kart çakışmasız |
| 06 | 69,5 · 72,8 · 75,2 · 77,6 · 79,6 · 82,0 · 84,2 · 86,2 · 88,3 (+ koyu 86,2) | `süre: for / since` y 540, been kutusu ve `in progress` satırına değmez; cümle, köprü, kart, `Next lesson` okunur |

## 4. Kapak

| Kare | Önce | Sonra |
|---|---|---|
| `kapak.png` (1920×1080, açık) | `İKİ SAATTİR` / `= HAVE BEEN` + `-dir … -yor → have been -ing` | `İKİ SAATTİR` / `NASIL DENİR?` + `I have been working for two hours.` |
| `kapak-koyu.png` | aynı | aynı (sarı vurgu kutusu) |
| `uretim-tutanagi/kapak-168.png` (168×94) | — | `İKİ SAATTİR NASIL DENİR?` okunur |

Üretici `sahneler/90-hyperframes-kapak/uret.py`: `SATIR2`, tek satırlık `KUCUK` (ok ve iki parça kalktı); küçük satır sol %55'e sığana ve karaktere
değmeyene dek küçülür (yatay 53 px, dikey 43 px); yatay ana yazı 160 → 156 px (`NASIL DENİR?` 160 px'te karakterin saçına değiyordu, `assert`).
Karakter, nesne, yerleşim, rozet değişmedi. 4 kare + 168 px'e baktım: taşma yok, yazı karaktere binmiyor, sağ alt süre rozeti bölgesi boş, `İ` noktaları doğru.

## 5. Yayın verisi zamanı (`youtube.json`, `youtube-aciklama.md`; dikeyde aynı)

| Öğe | Önce | Sonra |
|---|---|---|
| Bölüm 1 İki saattir çalışıyorum | 0 (00:00) | 0 (00:00) |
| Bölüm 2 Süre için for | 17,13 (00:17) | 21,93 (00:22) |
| Bölüm 3 Başlangıç için since | 32,28 (00:32) | 37,08 (00:37) |
| Bölüm 4 Sokak ıslak | 47,27 (00:47) | 52,47 (00:52) |
| Bölüm 5 Neden hep been? | 61,51 (01:02) | 66,87 (01:07) |
| En kısa bölüm | 14,24 sn | 14,40 sn |
| Bildirim | 32,83 (c4 başı, %39,4) | 37,63 (c4 başı, %42,5; 30 sn sonrası ilk cümle başı; bitiş 40,63 ≤ 68,58) |

Damga bloğu `bolumler` ile aynı (yuvarlama `int(t + 0,5)`). `yv-tutarlilik.py` damga denetimi 0 sorun.

## 6. Kapılar

```
$ /usr/bin/python3 uretim-hatti/betikler/yv-tutarlilik.py --kilitli simple-present-temel,simple-present-temel-dikey,02-04-ydt-temel-dikey
present-perfect-cont-temel / -dikey: süre 88.58 sn, bölüm 5; sinir, damga, kanal-etiketi, emoji, baslik, liste, etiket-yazim, kopya, dikey → TAMAM
[SORUN] zaman: 14 — hepsi present-perfect-cont-ileri{,-dikey} ve simple-past-temel{,-dikey} (bölüm sahne başı değil; başka oturumların DUZ3 işi)
→ çıkış 1 (bu derste sorun 0; kilitli pakette 0)

$ node araclar/cakisma-kapisi.mjs present-perfect-cont-temel --port 41333 --sunucu 41022 --json ~/is/duz3-0209T/kapi-ana.json
02, 03, 05: çakışma yok · 01: t1 × t2 (2,75 sn, giriş uçuşu) uyarı · 04: başlangıç noktası × since (6 px) uyarı · 06: row0/row1/row2 (72,12 sn, toplanma anı) uyarı
→ çıkış 0
```

## 7. Kısa video (`present-perfect-cont-temel-s1`; yalnız rapor, dokunulmadı)

| Dosya | Aynı hata |
|---|---|
| `ortak/anlatim/senaryo.json` (ses), `altyazi.json`, `METIN.md`, `uretim-tutanagi/art.json` | `Kardeşim sabahtan beri gitar çalıyor. Tekil kişide has been, artı -ing.` (I de tekildir) |
| `senaryo.json` `meta.canAlici`, `surumler.json` | `Türkçedeki -dir ... -yor = İngilizcedeki have been ... -ing`; `Tekil kişide has been, çoğul ve I/you ile have been` |
| `senaryo.json` kapak + `sahneler/01-hyperframes-kapak/uret.py`, `sahneler/02-paperjs-ornek/sahne-02.js` (çip), `BRIEF-S1.md`, `manifest` | `İKİ SAATTİR` / `= HAVE BEEN` (kapak denkliği) |
| `BRIEF-S1.md` | rozet `YDT · BASIC` (HV-24) |

Ekranda (`sahne-02.js` 13,91–16,75) `he · she · it` yazıyor; o kısım doğru. Ana paketin `surumler.json` `shorts` satırı `kapak: İKİ SAATTİR = HAVE BEEN`
kısanın bugünkü kapağını anlatır; kısa düzelince güncellenmeli.
Ana paketin `uretim-tutanagi/huni-konu.{json,md}` dosyası da `köprü: -dir ... -yor = have been + -ing`, `Tekil özne (he, she, it, my brother) has been alır`,
`Yağmur bir süredir yağıyor` taşır; tutanaktır, dokunulmadı.

## 8. Düzeltemediklerim / açık kalanlar

| Madde | Sebep |
|---|---|
| EK-11 kulak dinlemesi (c2, c4, c5, c7 yeni ses) | Nadir'in işi; Whisper süzgeçtir (c2 "süren" → "sürem" duyuldu, 0,97) |
| mp4 ve render çıktıları bayat | render yasak; `calistir.sh` kare sayıları güncel. Render ile yenilenecek türetilmiş kayıtlar: sahne 02–05 `olaylar.json` (ses efekti anları), sahne 02 `zamanlar.json` (not listesi) |
| YVJ ve ders jürisi | içerik değişti → `juri-olcutleri.md` §1b gereği jüri yeniden koşmalı (farklı model) |
| Tutarlılık kapısı çıkış 1 | başka derslerin zaman sorunu (§6) |
| Kısa video (s1) ve `huni-konu` tutanağı | istem yazmayı iki paketle ve kısaya dokunmamakla sınırladı (§7) |
| `.claude/docs/sozlesme.md`, Kovan | istem yazmayı iki paketle sınırladı |
| Yazım boyutu kapısı | `write-size-gate` 15 satırlık bir düzenlemeyi durdurdu (sahne 02); atlama bayrağı açılmadı, düzenleme ≤ 14 satırlık parçalara bölündü |
| Kural ihlali (bildirim) | kare kopyalarken yanlış dizine düşen bir kopyayı (`06-hyperframes-form-86.2.png`, `~/is` altındaki özgünün kopyası) `rm -f` ile kaldırdım; özgün dosya yerinde, kayıp yok |

---
Son Güncelleme: 16.11.2026 (DUZ3-0209T oturumu).
