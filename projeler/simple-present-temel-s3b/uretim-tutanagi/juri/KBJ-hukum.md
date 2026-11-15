# KBJ-hukum — simple-present-temel-s3b (A/B kol b, değişken `kanca`) çıktı jürisi · 15.11.2026 23:39 (istem KBJ-0202S3)

`juri_model`: Claude Sonnet 5.5 (`claude-sonnet-5-5`) · `uretici_model`: Claude Opus 5.5 (`claude-opus-5-5`; KBC-RAPOR.md son tablo). **İki model FARKLI** (juri-olcutleri §1e sağlandı; aynı aile, ayrı sürüm: ortak kör nokta riski kalır).
Jüri zamanı 23:39; paketin son içerik değişikliği 23:27 (`aciklama-a.md`), çakışma kapısı çıktısı 23:29 → jüri paketten yeni (§1b sağlandı).
Üretim dosyalarına dokunulmadı; tek yazılan dosya bu hükümdür.

## Özet

| Sonuç | Sayı | Maddeler |
|---|---|---|
| Geçti | 40 | HV 24 · EK/DK/ST 10 · AB 6 |
| **Kaldı** | **10** | hayır 5: HV-24, ST-1, EK-5b, EK-6, AB-8 · kanıt yok 5: HV-13, ST-2, EK-3, EK-8, EK-11 |
| Uygulanmaz | 7 | HV-21, DK-2, DK-3, K23, AB-4, AB-5, AB-7 |

**Hüküm: KALDI.** Teslim kapısı (EK-4, D-0338) açılmaz; önizleme adresi Nadir'e ve karta yazılmadan önce aşağıdaki 10 madde kapanmalı, jüri yeniden koşmalı.

Ölçüm kaynakları: `senaryo.json`, `sentez.wav.rapor.json`, `METIN.md`, `sozcukler.json`, `zaman.json`, `surumler.json`, `aciklama*.md`, `kapi-cikti.txt`; kareler: `~/qa-kare/simple-present-temel-s3b/kanal-b/` (0 · 7,75 · 24,42), `sahneler/01-hyperframes-kanca/k/` (açık 0,9 · 1,4 · 2,5 · 3,23; koyu 2,12), `kapak-a.png`, `k/koyu/kapak-a-koyu.png`, `sahneler/02..04/k/` (açık + koyu). Piksel ölçümü PIL ile jüri tarafından yeniden koşuldu.

## Tek değişken: `diff -rq` (jüri kendi koştu)

`diff -rq simple-present-temel-s3 simple-present-temel-s3b` = 74 satır (16'sı `uretim-tutanagi/`, 58 paket). Üreticinin sınıflaması (beklenmeyen 0) DOĞRULANDI: 58 satır şu sınıflara iniyor.

| Sınıf | Dosya | Beklenen mi (AB §4) |
|---|---|---|
| Sahne `01-hyperframes-kanca` (`uret.py`, `zamanlar.json`, `olay.py`, `olaylar.json`, `devir.json`, `calistir.sh`, `proje/index.html`, `RAPOR.md`, `SPEC.md`, `__pycache__`, `k/`, `proje-ka[-koyu]/`) | 34 | evet (değişen sahne) |
| `ortak/anlatim/senaryo.json` | 1 | evet; JSON farkı yalnız `cumleler[0]`, `giris`, `meta.kapak` |
| Ses ve türevleri (`cumle-1.wav`, `sentez.wav`+rapor, `anlatim.wav/m4a/.imza`, `sozcukler`, `sureler`, `baslar`, `altyazi`, `METIN`) + `zaman.json` | 12 | evet |
| `surumler.json` | 1 | evet |
| `aciklama.md`, `aciklama-a.md`, `aciklama-b.md` | 3 | evet (yalnız `utm_content`; ama bkz. EK-6) |
| `kapak.png`, `kapak-a.png` | 2 | evet (kanca karesi; md5 `a7b1535b…` iki dosyada aynı) |
| Kol a'da kalan grup türevleri (`kapak-b/c`, `hikaye*.png`) | 5 | evet (AB §4) |

Sahne 02/03/04, `ortak/` (anlatım dışı), `BRIEF-S3.md`, `gorevler.json` bayt aynı. `cumle-2/3/4.wav` sha256 kol a ile aynı (6cbf7b4efbd3 · 569e61237aa4 · 6a9927c66d00); `cumle-1.wav` farklı (132a1a31… ↔ 5ff70552…) ve yeni.

## Madde tablosu — §2a kısa video (huni v2)

| Kimlik | Hüküm | Kanıt | Not |
|---|---|---|---|
| HV-1 | evet | kanal-b/01-0 · 02-7,75 · 04-24,42: `ydspublishing` + `@ydspublishing`, y 296–339, x≈60 | kol a karelerinin kanal+künye bölgesi (y 280–450) kol b ile 0 piksel farklı (PIL) |
| HV-2 | evet | `senaryo.json` cümle 4 `ses: ogrenci`; `sentez.wav.rapor.json` | Whisper 1,00 |
| HV-3 | evet | `senaryo.json` cümle 4; `METIN.md` | ses metni "YeDeSe Publishing" beklenen (HV-17) |
| HV-4 | evet | `grep` senaryo, METIN, altyazı, açıklama, `surumler.json`, sahne HTML/JS, `ortak/kunye.js`: "tam ders" 0 | `BRIEF-S3.md:76` yasak listesi, yüzey değil |
| HV-5 | evet | aynı tarama, "dakika" / `dk` 0 | `calistir.sh` yorumundaki "1 dk yük" yüzey değil |
| HV-6 | evet | 03 Kaydet sahnesi + `aciklama*.md` satır 1: "Sınav günü bakmak için kaydet. …" | |
| HV-7 | evet | kanal-b/04-24,42: ana kapak x 60–960, y 620–1125 | açık + koyu (k/koyu/04-25) |
| HV-8 | evet | `senaryo.json` | 6 sorunun 6'sı evet (bkz. EK-5b: kural kapsamı ayrı madde) |
| HV-9 | evet | `find -name '*.mp4'` boş | |
| HV-10 | evet | üst 0–280 ve alt 1570–1920 yalnız zemin vinyeti (gri 218–243; mürekkep yok) 0 · 7,75 · 24,42 karelerinde | |
| HV-11 | evet | `zaman.json`: 4 sahne; 24,43 sn | hedef 22–26 |
| HV-12 | evet | `sureler.json` ilk söz 1,00; kanca 0–3,24 | |
| HV-13 | **kanıt yok** | kol b'nin kendi 03 karesi yok; paketteki `03-…-16.6` / `-18` kol a'dan kopya ve aralıkları 1,4 sn | Kural: 2 kare, aralık 2 sn, kart bölgesi farkı 0 px. 16,6 ↔ 18 farkı 0 px ama aralık 1,4 sn; 12,9 ↔ 16,6 farklı (kart giriş animasyonu). Yer imi SVG + "Kaydet" gözle var. |
| HV-14 | evet | kare 04-20,68 / 24,42: kart konumu, giriş sözü Fredoka 700 (gözle), `@ydspublishing · YouTube` | `hyperframes check` çıktısı yok (bkz. ST-2) |
| HV-15 | evet | "Bu sadece başlangıç." listede; senaryoda 1 kez | |
| HV-16 | evet | "Bir arkadaşına gönder; o da karıştırıyor." Kaydet listesinde; 1 kez | |
| HV-17 | evet | rapor: ses metni "YeDeSe Publishing YouTube kanalında."; Whisper en düşük 0,93 | `/dʌz/` ("döz") 0,96 ve 0,93: beklenen |
| HV-18 | evet | `aciklama-a/b.md` satır 1 sabit; Reels bloğunda bağ yok ("profildeki bağlantı") | |
| HV-19 | evet | 90 bağ satırı (6 kardeş paket, `aciklama*.md`): tek `utm_campaign=ING-YDT-GR-02-02-T`; kol b `utm_content=s3b-a` / `s3b-b` | büyük harf, biçim tutarlı |
| HV-20 | evet | `surumler.json` `s3b-kapak-a` → `kapak-a.png`, 1080×1920, altyazı yok, kanal katmanı + karakter var | kol b'de kapak B/C, hikâye, `s3b` dışı türev yok: AB §4 gereği |
| HV-20a | evet | kapak-a: 1080×1920; kanal y 296–339, künye 360–450, içerik 460+, sağ kenar ≤ 960; zemin orta (244,241,232), köşe (222,218,210) fark ≤ 25 (vinyet); koyu orta (27,26,23) = `#1b1a17` | koyu: `k/koyu/kapak-a-koyu.png` |
| HV-20b | evet | kapak "S NEREYE GİDER?" = 3 sözcük; kapak A = kanca karesi (0,9 sn) | |
| HV-21 | uygulanmaz | kol b'de hikâye yok (AB §4) | |
| HV-22 | evet | `kapi-cikti.txt`: 4 sahne "çakışma yok", çıkış 0; zaman 23:29 ≥ son içerik 23:27 | jüri kapıyı yeniden koşmadı (sunucu gerekir); tutanak kanıtı |
| HV-23 | evet | çağrı parçaları 1,00 / 1,00 | |
| HV-24 | **hayır** | künye `YDT · BASIC` her karede (kanal-b/01, 02, 04; kapak-a; koyu kareler); `senaryo.json` `giris.rozetler: ["YDT · BASIC"]`; kare 04'te ana kapak içinde `YDT · TEMEL`: aynı karede iki rozet metni | standart §9 `YDT · TEMEL` ister; KBC-RAPOR §6.10 kendisi bildirmiş |
| HV-25 | evet | kareler: en çok 2 satır (7,75 karesi 2 satır, y 1420–1520) | bilgi: 1 satır ≤ 41 karakter, 2 satır 44 karakter (N kararı Nadir'de) |

## Madde tablosu — §2b kısa jüriye giren maddeler

| Kimlik | Hüküm | Kanıt | Not |
|---|---|---|---|
| DK-1 | evet | `sozcukler.json` 40 sözcük = `senaryo.json` 40 sözcük; kareler 0,9 → 25 sn karaoke altı çizgisi ilerliyor | kanca sahnesinde zorunlu değil, var |
| DK-2 | uygulanmaz | kısada HV-25 | |
| DK-3 | uygulanmaz | kısa jüriye girmeyen madde | |
| K23 | uygulanmaz | HV-12 kapsıyor | |
| ST-1 | **hayır** | kanal-b/01-2,5 ve 01-3,0: sarı hap + kırmızı `?` halkası aynı karede; kural: kırmızı ✗ ve üstü çizgi ikinci vurgu sayılır | kol a'da da var (`?` kırmızı); ana dersle ortak desen. Vinyet köşe-orta 22 ≤ 25: gradyan sayılmadı |
| ST-2 | **kanıt yok** | tutanakta `hyperframes check` çıktısı yok (yalnız çakışma kapısı); künye 34 px, rozet 26 px (BRIEF) yazı tabanı 50'nin altında | font ailesi gözle Fredoka/Lexend uygun; taban ölçümü yok |
| EK-1 | evet | ses metni: YDT okunmuyor; "YDS" yalnız marka sözlüğüyle "YeDeSe" | |
| EK-2 | evet | kareler emoji yok; yüzey taraması 0 (`sahne-02.js` `✗` yalnız yorum/hata metni) | |
| EK-3 | **kanıt yok** | kol b'nin kendi render karesi olmayan hücreler: 02 koyu, 03 açık + koyu, 04 koyu (paketteki kareler kol a kopyası; sahne bayt aynı ama `KOK` kol a'ya bağlı, bkz. AB-8) | dolu: 01 açık+koyu, 02 açık (7,75), 04 açık (24,42), kapak-a açık+koyu. Yön: yalnız dikey |
| EK-4 | evet | KBC-RAPOR §6.11: Kovan kaydı yok, adres gitmedi | bu hükümle de gitmez |
| EK-5a | evet | kanca kartı `He doesn't goes.` gerçekten hatalı, kırmızı `?` ile işaretli; üstü çizili cümle yok | `He goes.` → `He doesn't goes.` geçişi doğru anlatılıyor |
| EK-5b | **hayır** | (1) cümle 2 "Olumsuzda ve soruda does girer, s ona geçer." ve "Fiile s gelmez.": kapsam sınırı yazılı değil; kural yalnız üçüncü tekil kişide (he/she/it) geçerli, `I/you/we/they` `do` alır, `be` ve modallarda `does` girmez. (2) `senaryo.json` `meta.canAlici[0]` ve `surumler.json` `video.canAlici[0]`: "Türkçedeki geniş zaman eki = İngilizcedeki s: gider = goes" YANLIŞ (Türkçe `-r/-ir` kip/zaman eki, İngilizce `-s` üçüncü tekil uyum eki) | iki hata kol a ve ana derste de var (§1c). Doğru olanlar: `Does varsa fiil yalın.`, `He doesn't go.`, `Does she go?`, kapak "GİDER = GOES · he·she·it → -s", başlık "Does varsa fiil yalın: He doesn't go" |
| EK-5c | evet | "her zaman / hep / always" yok | "Fiile s gelmez." öncesi cümlenin kapsamına bağlı; sınır eksikliği EK-5b'de |
| EK-6 | **hayır** | `aciklama-a.md` satır 1: başlık `simple-present-temel-s3`; satır 4 `s3-aciklama-a`; satır 6 `25,08 sn` (kol b 24,43 sn); satır 35, 58 kol b'de olmayan `kapak-c.png`, `hikaye-a.png`'ye gönderme. `aciklama.md` ≡ `aciklama-a.md` (aynı bayatlık) | kol a'dan kalma şablon cümleleri. Tür/İ-I/noktalama hatası yok |
| EK-7 | evet | koyu kareler okunuyor: 01-2,12 · kapak-a-koyu · 02-8,4 · 03-16,6 · 04-25 | |
| EK-8 | **kanıt yok** | pakette kontak sayfası yok (`find -iname '*kontak*'` boş) | işaret sayısı ölçülemedi |
| EK-9 | evet | kanca sorusu "Olumsuzda s nereye gider?" = 4 sözcük, 1 soru | "Does she go?" örnek cümle, soru anı değil |
| EK-10 | evet | ses metni `Olumsuzda ve, soruda /dʌz/ girer…`, `/dʌz/ varsa…` | |
| EK-11 | **kanıt yok** | yeni parça `s` / `gider?` dinleme kaydı yok; Whisper `S` yazdı (1,00) | Nadir kulak kararı bekliyor (KBC §6.1) |
| EK-12 | evet | kanca (0–4 sn) istisna; 02–04: cümle başı − sahne başı kol a ile aynı (cümle 2: 3,79 − 3,24 = 4,44 − 3,89 = 0,55) | `?` 2,28 = "nereye" 2,28 |

## Madde tablosu — §2d A/B kolu

| Kimlik | Hüküm | Kanıt | Not |
|---|---|---|---|
| AB-1 | evet | kol a satırı `s3` `varyant {grup s3, kol a, degisken kanca, deger yanlis-cumle}`; kol b `s3b` `{s3, b, kanca, soru}` | atama s3 → kanca |
| AB-2 | evet | yukarıdaki `diff -rq` tablosu: beklenmeyen 0 | süre farkı (25,08 ↔ 24,43) cümle 1'in kısalmasından; kaçınılmaz |
| AB-3 | evet | sahne 02–04 bayt aynı; kanal+künye bölgesi 3 karede 0 px; `sesler`, `kadro`, cümle 2–4 `senaryo.json`'da aynı | |
| AB-4 | uygulanmaz | yayın sonrası | |
| AB-5 | uygulanmaz | yayın sonrası | |
| AB-6 | evet | `surumler.json` `s3b.varyant`; `utm_content=s3b-a/b` | `deger` `[a-z0-9-]` |
| AB-7 | uygulanmaz | yayın sonrası | |
| AB-8 | **hayır** | `ortak/kunye.js:7` `KOK = "/projeler/simple-present-temel-s3/ortak"`; `sahneler/02-paperjs-deger/sahne-02.js:4` `import … from "/projeler/simple-present-temel-s3/sahneler/02-paperjs-deger/kalem-paper.js"`; `sayfa.html` ve `kalem-paper.js` da kol a yolu içeriyor | kol a panelde yoksa kol b kırılır; kol b altyazı ve sözcük verisini kol a'dan çeker (sahne 02–04 renderı kol a'ya bağlı) |
| AB-9 | evet | cümle 2, 3, 4 `cumle-N.wav` sha256 aynı (yukarıda) | |

## İki kol yan yana (değişken dışında fark)

| Yüzey | Kol a (`yanlis-cumle`) | Kol b (`soru`) | Fark meşru mu |
|---|---|---|---|
| Ses cümle 1 | "He doesn't goes. Hata nerede?" | "Olumsuzda s nereye gider?" | evet (değişken) |
| Kanca ekranı | `BU CÜMLE / YANLIŞ` + kart | `S NEREYE / GİDER?` + kart `He goes.` → `He doesn't goes.` | evet |
| Kanca sonu | kart `He doesn't goes.` + `?` | aynı kart + `?`; `?` bekleme ≈ 0 sn (kol a'da 0,26 sn) | evet; estetik not: `?` çizimi 2,72'de biter, çıkış 2,73'te başlar |
| Değer, kaydet, çağrı sahneleri; kanal katmanı; çekirdek cümle; kadro | — | aynı | evet |
| Kapak A | `BU CÜMLE YANLIŞ` karesi | `S NEREYE GİDER?` karesi | evet (AB §4) |
| Açıklama metni | `utm_content=s3-*` | `s3b-*`; gövde bayt aynı, bayat başlık/süre satırları | utm evet; bayat satırlar EK-6 |
| Künye rozeti | `YDT · BASIC` | `YDT · BASIC` | iki kolda aynı (HV-24 ikisinde birlikte düzelmeli) |

## Kaldı maddeleri için düzeltme önerisi (tek cümle)

| Madde | Öneri |
|---|---|
| HV-13 | Kol b için sahne 03'ten ≥ 2 sn arayla iki kare çek (ör. 14,0 ve 16,0 sn), kart bölgesi farkını 0 px ölç. |
| HV-24 | `giris.rozetler`, `ortak/kunye.js`, sahne 01–04 `yardim.py`/HTML ve kapak karelerinde `YDT · BASIC` → `YDT · TEMEL`; kol a ile birlikte (tek değişken bozulmasın). |
| ST-1 | Kanca `?` halkasını vurgu rengine çevir ya da standartta "kanca hatası işareti" istisnasını yaz (iki kolda ve ana derste ortak karar). |
| ST-2 | Sahne 01–04 için `hyperframes check` çıktısını tutanağa yaz; künye 34/26 px ile taban 50 çelişkisini standartta çöz. |
| EK-3 | Kol b'nin kendi render'ından 02 koyu, 03 açık + koyu, 04 koyu kareleri çek; matrisi tabloya yaz. |
| EK-5b | Kural cümlesine "üçüncü tekil kişide (he/she/it)" sınırı ekle; `meta.canAlici[0]` ve `video.canAlici[0]` satırını sil ya da "gider = goes; he/she/it fiile s alır" yap. |
| EK-6 | Kol b `aciklama*.md` başlık, sürüm, süre (`24,43 sn`) ve kol a'ya ait dosya göndermelerini kol b'ye göre düzelt (`aciklama.md` ≡ `aciklama-a.md` kalsın). |
| EK-8 | Kol b için kontak sayfası üret ve klişe işaretlerini say. |
| EK-11 | Nadir `s` / `gider?` telaffuzunu dinlesin; kayıt tutanağa girsin. |
| AB-8 | `kunye.js` `KOK` ve `sahne-02.js` içe aktarımını kol b yoluna çevir (`sayfa.html`, `kalem-paper.js` dahil), sonra sahne 02–04 karelerini kol b'den yeniden çek (EK-3 ve HV-13 ile aynı koşu). |

## Ana derse (`simple-present-temel`) geri besleme

1. `meta.canAlici[0]` hatası ("geniş zaman eki = s") ana ders ve bütün kardeş kısalarda aynı; hepsi temizlenmeli (SP-s1 hatasının yinelemesi).
2. Kural cümlesi "does girer, s ona geçer" üçüncü tekil sınırı olmadan yayınlanıyor; kapaktaki "he·she·it" sınırı yalnız son karede görünüyor.
3. `YDT · BASIC` rozeti 6 kısada hâlâ duruyor (huni v2 §9 açık işi); kol b'de kapak içindeki `YDT · TEMEL` ile aynı karede çakışıyor.
4. ST-1 kırmızı `?` deseni ders sahnelerinde de olabilir; standart "hata işareti" rengini açıkça tanımlamalı.
5. Kol b paketleri (s1b, s2b, s3b) `KOK` bağını kol a'ya taşıyor; kopya paket sözleşmesi (AB §4) kunye.js ve sahne 02 içe aktarmasını da kapsamalı; `juri-olcutleri.md` AB-8 tarama komutuna `sahne-02.js`, `sayfa.html`, `kalem-paper.js` eklenmeli.
