# S1 Shorts — "GO mu, GOES mu?" (simple-present-temel-s1, YDT TEMEL) · huni v2

Çıktı: önizleme (mp4 yok, standart §1 kural 9; 1080×1920, 30 fps, 24,00 sn, anlatım 24,00 sn hazır) + `kapak-a|b|c.png` (`kapak.png` = A)
+ `hikaye-a|b.png` (`hikaye.png` = A). Bağlayıcı standart: `D/.claude/docs/huni-v2-standart.md` (15.11; bu belge onunla çelişirse standart geçer).
Biçim emsali: `../02-04-ydt-temel-s1/` (v2 pilot). Öğe kimliği `02-02-ydt-temel`; ana ders `../simple-present-temel/`.
Stil, kalem darbesi, olay sesi kuralları `../simple-present-temel/BRIEF.md` ile aynı (palet; kırmızı yalnız `s` yuvası çizgisi, satır 159); ≥ 64 px içerik yazısı
`../present-continuous-dikey/BRIEF-DIKEY.md` §3.
Kaynaklar: ses `ortak/anlatim/` (cümle başları 1,00 · 4,67 · 15,18 · 18,29; toplam 24,00), senaryo `ortak/anlatim/senaryo.json`
(kaynak: `uretim-tutanagi/senaryo-taslak.md`, jüri `uretim-tutanagi/juri/s1.dil.md` + `s1.kaynak-kural.md`, düzeltme `uretim-tutanagi/S1-duzeltme.md`,
ses ve zaman `uretim-tutanagi/S1-C-RAPOR.md`).

Kapak başlığı (2 satır, 4 sözcük): `GO mu,` / `GOES mu?`. Can alıcı: "Gider = goes; ama yalnız he, she, it ile. I, you, we, they ile go." (`canAlici[0]`).
Ses: cümle 1–3 öğretmen (`gsJ9nrlXYbPztJxC4fwc`, ana ders `sesler.ogretmen`), cümle 4 (çağrı) öğrenci (`kadro.ogrenci`, `oPC5I9GKjMReiaM29gjY`).
Konuşan figür yok (ana derste `kadro.ogretmen` yok). Kanca görseli: kalem çizimi genç figür `ortak/cizim/open-peeps/standing-2.svg` + otobüs `ortak/cizim/coco/bus.svg`.
Kural özeti (kaydet kartı ve hikâye kareleri, tek cümle): `He, she, it: s gelir;` / `I, you, we, they: s yok.`

## Yerleşim (px) — huni v2 §2
| Bölge | y | İçerik |
|---|---|---|
| Üst boş | 0–280 | yalnız zemin; çip YOK |
| Kanal katmanı | 280–350 | aşağıdaki tablo; kalıcı |
| Künye | 360–450 | konu `Simple Present` (Fredoka 700, x 60, taban 420; boy ≤ 34, rozetle x 960'a sığan en büyük, alt sınır 28) + rozet `YDT · TEMEL` (hap y 386–434, Lexend 700 26, dolgu `vurguDolgu`, yazı `pilMetin`, konu sonu + 20) |
| İçerik | 460–1380 | x 60–960 |
| Altyazı + karaoke | 1400–1550 | en çok 2 satır (kapak ve hikâye karelerinde yok) |
| Alt boş | 1570–1920 | yalnız zemin |

Kanal katmanı (bütün sahnelerde AYNI piksel; tek kaynak bu tablo — canvas `ortak/kunye.js` (v2, `KANAL` + `kanalCiz`), HyperFrames sahne başına `yardim.py`):

| Öğe | Değer |
|---|---|
| Logo | `ortak/logo/` (açık `yds-publishing-lacivert.svg`, koyu `yds-publishing-seffaf.svg`); yükseklik 48, genişlik 193,5 (48 × 1920 / 476,3); resim x 53,2 (SVG iç boşluğu 68/1920 düşülür, görünür sol kenar x 60), y 291–339 |
| Yazı | `@ydspublishing`, Lexend 700 42 px, renk `murekkep`, x 263, taban y 330 |
| Davranış | 0. kareden son kareye; opaklık 1; giriş/çıkış animasyonu yok; uçuş ve geçiş dokunmaz; kimlik `kanal`; `__kalemKutu` türü `kunye`, ad `kunye:kanal` |

## Sahneler (zaman.json ile birebir)
| # | Klasör | Motor | Küresel sn | Kare | Ses |
|---|---|---|---|---|---|
| 1 Kanca | 01-hyperframes-kanca | HyperFrames | 0,00–3,00 | 102 | öğretmen |
| 2 Değer | 02-paperjs-deger | Paper.js | 3,00–14,63 | 361 | öğretmen |
| 3 Kaydet | 03-hyperframes-kaydet | HyperFrames | 14,63–17,74 | 105 | öğretmen |
| 4 Çağrı | 04-hyperframes-cagri | HyperFrames | 17,74–24,00 | 218 | öğrenci |
| — | 05-hyperframes-hikaye-a · 06-…-kapak-b · 07-…-kapak-c · 08-…-hikaye-b | HyperFrames | zaman çizelgesi dışı | 1 | — |

Sahne sınırı = bir sonraki cümle başı − 0,55; son sahne = son söz + 1,0 sn. Sahne 01 → 02 sınırı 3,00 (giriş ≤ 3 sn; cümle 1'in sonu 02'de).
Durağan kareler `zaman.json` → `hikaye` (05) ve `duragan[]` (06–08) alanındadır, `sahneler[]` dışında: `birlestir.py` ve `kur.py` yalnız `sahneler[]` okur.
Kod tabanı: paket yeni, sahne kodu yok. Yapı ve v2 yerleşimi emsalden (`../02-04-ydt-temel-s1/sahneler/`), içerik eski S1'den
(`~/Silinecekler/2026-11-15-huni-v2/simple-present-temel-s1-eski/sahneler/`) ve ana dersten (`../simple-present-temel/sahneler/04-canvas-ornek2`, `06-hyperframes-form`).

## Sahne içeriği (tablodaki sn KÜRESELDİR; yerel kare = round((t − t_bas) × 30))
Zaman sözcük çapasından okunur (`ortak/anlatim/sozcukler.json`), sabit saniyeden değil. Ekran metni sesten önce gelmez; tek istisna kapak başlığı.

| sn | Hareket |
|---|---|
| 0,00 | Kapak tam görünür (ilk kare = kapak A, kanal katmanı dahil): künye satırında yalnız rozet `YDT · TEMEL`; başlık `GO mu,` / `GOES mu?` (900 px'e sığan en büyük boy, üst sınır 190; satır 2 sarı hap, dolgu `#ffe066`, yazı `#1b2440`); altında solda genç figür (`standing-2`, kalem), sağda otobüs (`coco/bus.svg`, sola gider); etiket yok |
| 0,30–0,80 | Başlıktaki `?` kalemle çizilir (tek kalem hareketi) |
| 1,00–2,24 | Cümle 1 altyazıda sözcük zamanlı (`Kardeşim` 1,00 · `gider:` 1,56); ekranda yeni yazı yok |
| 1,90–2,45 | Uçuş: başlık künye konu adına (`Simple Present`, y 360–450) döner; figür + otobüs küçülür (yükseklik ≤ 140), içerik bandının sağ üstüne (x 700–960, y 460–600). Kanal katmanı yerinde |
| 2,45 | Caveat 700 72 `Kardeşim gider:` (mürekkep, x 60, taban y 560); söylendikten sonra |
| 2,52 | Kart `go` (Fredoka 700 ≥ 96; x 60–440, y 620–820; `go` çapası). Sahne 01 3,00'te biter; bu durum sahne 02 kare 0'dır |
| 3,40 | Sahne 02: kart `goes` (x 580–960, y 620–820; `goes` çapası) |
| 3,80 | İki kart arasında kalem `?` (x 450–570; `mu?` çapası) |
| 4,67–6,83 | EN kart `My brother goes` / `to school by bus.` (Fredoka 700 ≥ 64, karaoke; `My` 4,67 · `goes` 5,23 · `bus.` 6,19). `Kardeşim gider:` aynı yerde soluk Caveat'e döner (ikincil renk, seslendirilmez, sahne sonuna dek kalır; jüri K2). Figür ve küçük otobüs solar; otobüs EN kartın yanında kalemle çizilir 4,67–6,19 (ana ders `04-canvas-ornek2`) |
| 5,23 | Kanca kartı `goes` cümledeki *goes*'a uçar, sarı alt çizgi alır; kart `go` soluk, sağ kenarda bekler (kaybolmaz) |
| 7,08–8,28 | `My brother` altında Caveat `= he` + kalem oku (`He,` 7,08) · çipler `he` 7,08 · `she` 7,64 · `it` 8,12 |
| 9,25 | `goes` → `go-es`, `es` sarı daire (`s` çapası); sarı belirteç en çok 2 (alt çizgi + daire) |
| 10,62–13,02 | İkinci satır çipler `I` 10,62 · `you` 11,42 · `we` 12,14 · `they` 12,86 |
| 13,59 | `gelmez.` çapası: soluk `go` kartı ikinci satırın yanına döner; `s` yuvası üstünden kırmızı kalem çizgisi (ana ders BRIEF satır 159) |
| 13,59–14,63 | Son durum iki satır: `he · she · it → goes` / `I · you · we · they → go`; hiçbir öğe sahne bitmeden kaybolmaz; x 60–960, y 460–1380 |
| 15,18–15,63 | Sahne 03: kural özeti kartı tek hareketle girer (ölçek 0,96 → 1 + saydamlık, ≤ 0,45 sn; `Sınavdan` 15,18): `He, she, it: s gelir;` / `I, you, we, they: s yok.` Fredoka 700 ≥ 64, kâğıt kart + kalem kenarı, x 60–960, y ≈ 600–980; 15,63'ten sahne sonuna sabit (2,11 sn ≥ 2) |
| 17,10–17,40 | `Kaydet.` çapası (17,10): yer imi simgesi (SVG yol, emoji değil) kalemle ≤ 0,3 sn + `Kaydet` sarı hap (Fredoka 700 64); kartın altında, y ≈ 1020–1140 |
| 17,74–18,29 | Sahne 04: ana dersin kapağı 16:9 kart (900×506, x 60–960, y 620–1126; standart ≈ 920×518, x 960 sınırı için 900) tek hareketle girer (ölçek 0,94 → 1 + saydamlık) |
| 18,29–19,33 | `Gerisi bizde.` Fredoka 700 (≈ 96; `Gerisi` 18,29), kartın üstünde (y ≈ 470–590); öğrenci sesi |
| 20,76–23,08 | `@ydspublishing · YouTube` Lexend 700 ≈ 56 (`YDS` 20,76), kartın altında (y ≈ 1160–1240); `@ydspublishing` sarı hapta |
| 23,00–24,00 | Durgun kuyruk (son söz + 1,0 sn) |

`@ydspublishing` ekranda; seste "YDS Publishing" (ses metni `YeDeSe`). Yasak sözler (seste, ekranda, açıklamada): standart §1 kural 4 (eski kapanış
sözü) ve kural 5 (süre sözü). QR yok, emoji yok, "izle" düğmesi taklidi yok, YouTube logosu taklidi yok.

## Kapak (`kapak-a.png` = `kapak.png`, 1080×1920)
A: sahne 01'in kanca karesi t 0,90 (kare 27; başlık tam, `?` çizilmiş, ilk söz ve altyazı yok; `kapak-taslak.md` §3), altyazı katmanı gizli
(S1-KAPAK-A yöntemi: `proje` kopyasında CSS `#altyazi{display:none}`, `hyperframes snapshot --at 0.90`; emsal `../02-04-ydt-temel-s1/uretim-tutanagi/S1-VAR-RAPOR.md`
satır 101), açık + koyu. B (`06-hyperframes-kapak-b`, `kapak-b.png`): `FİİLE -S` / `HANGİ ÖZNEYLE?` (jüri K1; satır 2 siyah kutuda krem), sarı zemin
`#fece00`, yazı ve logo `#141414` (ana kapağın tek renk çözümü), karakter `ortak/kapak/karakter.png` (10 px krem çıkartma kenarı + krem daire) ve küçük
`ortak/kapak/nesne.png`. C (`07-hyperframes-kapak-c`, `kapak-c.png`): `HE GO[ES]` / `I GO` (`ES` sarı hap), otobüs kalem çizimi, figürsüz.
Üçünde kanal katmanı var, altyazı yok, künye satırında yalnız rozet. Tarif: `uretim-tutanagi/kapak-taslak.md`.

## Hikâye kareleri (`hikaye-a.png` = `hikaye.png`, `hikaye-b.png`; 1080×1920)
Durağan; ses yok; kanal katmanı + künye + kural özeti + `Kaydet` (yer imi simgesi). İçerik y 460–1140; y 1150–1380 boş zemin (bağ çıkartması
elle konur; boş kutu çizilmez); 1400–1920 boş. A (`05-hyperframes-hikaye-a`): kural kartı düzeni (kural özeti · `he · she · it → goes` ·
`I · you · we · they → go` · Caveat `My brother = he` + küçük otobüs · `Kaydet`). B (`08-hyperframes-hikaye-b`): soru kartı (`Hangisi doğru?` ·
`My parents ____` / `to work by bus.` · `A) go` yeşil çerçeve + kalem tik, `B) goes` soluk · kural özeti · `Kaydet`). Tek sarı öğe `Kaydet` hapı.
Tarif: `uretim-tutanagi/hikaye-taslak.md` §3–§5.

## Çalıştırma
Her sahne `calistir.sh --tema acik` (önizleme: `ONIZLE_YALNIZ=1`); birleştirme `python3 birlestir.py projeler/simple-present-temel-s1 --tema acik
--gecis BookFlip --efekt hisirti` (mp4 takvimi gelince). Durağan kareler ayrı: `sahneler/<klasör>/calistir.sh --tema acik|koyu` → paket kökü PNG.
Ses yeniden kurulumu (sentez yok): `ortak/anlatim/` içinde `sozcuk_uret.py` → `zaman_uret.py` → `kur.py` →
`araclar/ses-paketle.py --yaz --paket simple-present-temel-s1` → `araclar/altyazi_uret.py projeler/simple-present-temel-s1` → `metin_uret.py`.
Sahne istemleri: `uretim-tutanagi/istem/sahne/D-<klasör>.md` (8 dosya).
