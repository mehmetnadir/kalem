# S1 Shorts — "YAŞIYORUM = İKİ ZAMAN" (02-04-ydt-temel-s1, YDT TEMEL) · huni v2

Çıktı: önizleme (mp4 yok, standart §1 kural 9; 1080×1920, 30 fps, 31,75 sn, anlatım 31,75 sn hazır) + `kapak-a|b|c.png` (`kapak.png` = A)
+ `hikaye-a|b.png` (`hikaye.png` = A). Bağlayıcı standart: `D/.claude/docs/huni-v2-standart.md` (15.11; bu belge onunla çelişirse standart geçer).
Stil, kalem darbesi, olay sesi kuralları `../02-04-ydt-temel/BRIEF.md` ile aynı; ≥ 64 px içerik yazısı `../present-continuous-dikey/BRIEF-DIKEY.md` §3.
Kaynaklar: ses `ortak/anlatim/` (cümle başları 1,00 · 6,91 · 20,54 · 26,04; toplam 31,75), senaryo `ortak/anlatim/senaryo.json`
(kaynak: `uretim-tutanagi/senaryo-taslak.md`, jüri `uretim-tutanagi/S1-duzeltme.md`, v2 çevirisi `uretim-tutanagi/V2-C-RAPOR.md`).

Kapak başlığı (2 satır, 3 sözcük): `YAŞIYORUM` / `= İKİ ZAMAN`. Can alıcı: "Türkçe yaşıyorum iki zamana karşılık gelir: I live (kalıcı),
I am living (geçici)" (`canAlici[4]`). Ses: cümle 1–3 öğretmen Atakan (`gsJ9nrlXYbPztJxC4fwc`), cümle 4 (çağrı) öğrenci
(`kadro.ogrenci`, `oPC5I9GKjMReiaM29gjY`; ana dersten). Figür öğretmen erkek (`kadro.ogretmen`: ShirtPantsWB / Smile / Short).
Kural özeti (kaydet kartı ve hikâye kareleri, tek cümle): `Live, work fiillerinde:` / `kalıcıysa geniş zaman,` / `geçiciyse şimdiki zaman.` (DUZ2 15.11)

**DİKKAT:** toplam 31,75 sn; standart §3 hedefi ≈ 22–26 sn. Değer cümlesi (13,08 sn) eski metinle aynı; karar şefte (`V2-C-RAPOR.md`).

## Yerleşim (px) — huni v2 §2
| Bölge | y | İçerik |
|---|---|---|
| Üst boş | 0–280 | yalnız zemin; çip YOK (eski sağ üst çip kalktı) |
| Kanal katmanı | 280–350 | aşağıdaki tablo; kalıcı |
| Künye | 360–450 | konu `Simple Present vs Present Continuous` (Fredoka 700, x 60, taban 420; boy ≤ 34, rozetle x 960'a sığan en büyük, alt sınır 28) + rozet `YDT · TEMEL` (hap y 386–434, Lexend 700 26, dolgu `vurguDolgu`, yazı `pilMetin`, konu sonu + 20) |
| İçerik | 460–1380 | x 60–960 |
| Altyazı + karaoke | 1400–1550 | en çok 2 satır (kapak ve hikâye karelerinde yok) |
| Alt boş | 1570–1920 | yalnız zemin |

Kanal katmanı (bütün sahnelerde AYNI piksel; tek kaynak bu tablo — ortak modül yok: canvas `ortak/kunye.js`, HyperFrames sahne başına `yardim.py`):

| Öğe | Değer |
|---|---|
| Logo | `ortak/logo/` (açık `yds-publishing-lacivert.svg`, koyu `yds-publishing-seffaf.svg`); yükseklik 48, genişlik 193,5 (48 × 1920 / 476,3); resim x 53,2 (SVG iç boşluğu 68/1920 düşülür, görünür sol kenar x 60), y 291–339 |
| Yazı | `@ydspublishing`, Lexend 700 42 px, renk `murekkep`, x 263, taban y 330 |
| Davranış | 0. kareden son kareye; opaklık 1; giriş/çıkış animasyonu yok; uçuş ve geçiş dokunmaz; kimlik `kanal`; `__kalemKutu` türü `kunye`, ad `kunye:kanal` |

## Sahneler (zaman.json ile birebir)
| # | Klasör | Motor | Küresel sn | Kare | Ses |
|---|---|---|---|---|---|
| 1 Kanca | 01-hyperframes-kapak | HyperFrames | 0,00–3,00 | 102 | öğretmen |
| 2 Değer | 02-paperjs-ornek | Paper.js | 3,00–19,99 | 522 | öğretmen |
| 3 Kaydet | 08-hyperframes-kaydet (YENİ) | HyperFrames | 19,99–25,49 | 177 | öğretmen |
| 4 Çağrı | 03-hyperframes-cta | HyperFrames | 25,49–31,75 | 218 | öğrenci |
| — | 04-hyperframes-hikaye · 05-…-kapak-b · 06-…-kapak-c · 07-…-hikaye-b | HyperFrames | zaman çizelgesi dışı | 1 | — |

Sahne sınırı = bir sonraki cümle başı − 0,55; son sahne = son söz + 1,0 sn. Sahne 01 → 02 sınırı 3,00 (giriş ≤ 3 sn).
Durağan kareler `zaman.json` → `hikaye` ve `duragan[]` alanındadır, `sahneler[]` dışında: `birlestir.py` ve `kur.py` yalnız `sahneler[]` okur.

## Sahne içeriği (tablodaki sn KÜRESELDİR; yerel kare = round((t − t_bas) × 30))
Zaman sözcük çapasından okunur (`ortak/anlatim/sozcukler.json`), sabit saniyeden değil. 01 ve 02'nin içeriği aynı kalır; yalnız yerleşim v2'ye çekilir.

| sn | Hareket |
|---|---|
| 0,00 | Kapak tam görünür (ilk kare = kapak, kanal katmanı dahil): başlık `YAŞIYORUM` (900 px'e sığan en büyük boy, üst sınır 190 px) / `= İKİ ZAMAN` sarı hapta (dolgu `#ffe066`, yazı `#1b2440`); solda ev (house), sağda elinde bavul (suitcase) tutan öğretmen figürü; etiketler `I live` / `I am living` (Caveat ≥ 72) |
| 0,30–0,80 | `YOR` altına sarı el altçizgisi (`alti`) |
| 1,00–2,10 | Cümle 1 sözcük zamanlı: `İstanbul'da yaşı-yor-um.` (`İstanbul'da` 1,00 · `yaşıyorum.` 1,64) |
| 2,0–3,0 | Uçuş: başlık künye satırına (y 360–450), figür ve ev solar; cümle satırları içerik bandının üstüne (y ≥ 460). Kanal katmanı yerinde |
| 2,52 | İkinci satır `Amcamla yaşı-yor-um.` (`Amcamla` 2,52); sahne 01 iki satır taşır |
| 3,08–19,99 | Sahne 02: eski akış aynen (`ek_ayir` 3,96–6,36 · `İngilizcede ikisi ayrılır.` 6,91 · kart 1 `I live in Istanbul.` 9,08 + `Hep orada.` / `PERMANENT` / uzun bant · kart 2 `I am living` / `with my uncle.` 14,70 + `Şimdilik.` / `TEMPORARY` / kısa bant 19,03); x 60–960, y 460–1380 |
| 20,54–22,62 | Sahne 08: `üç farktan biri` Lexend (`üç` 21,02), kartın üstünde küçük |
| 20,54–21,00 | Kural özeti kartı girer (tek hareket ≤ 0,45 sn); `Live, work fiillerinde:` / `kalıcıysa geniş zaman,` / `geçiciyse şimdiki zaman.` (DUZ2 15.11) Fredoka 700 ≥ 64; 21,00'den sahne sonuna sabit (≥ 2 sn) |
| 24,89–25,49 | `Kaydet.` çapası (24,89): yer imi simgesi (SVG yol, emoji değil) kalemle çizilir + `Kaydet` sarı hap; kartın altında |
| 25,49–26,04 | Sahne 03: ana dersin kapağı 16:9 kart (900×506, x 60–960, y 620–1126; standart ≈ 920×518, x 960 sınırı için 900) girer |
| 26,04–27,08 | `Gerisi bizde.` Fredoka 700 (`Gerisi` 26,04), kartın üstünde (y ≈ 470–590); öğrenci sesi |
| 28,51–30,83 | `@ydspublishing · YouTube` Lexend 700 (`YDS` 28,51), kartın altında (y ≈ 1160–1240) |
| 30,83–31,75 | Durgun kuyruk (son söz + 1,0 sn) |

İngilizce cümlede ekranda ve seste "Istanbul" (J3 A4, 16.11); Türkçe satırda "İstanbul'da". `@ydspublishing` ekranda; seste "YDS Publishing". Yasak sözler (seste, ekranda,
açıklamada): "Tam ders", süre ("dakika"). QR yok, emoji yok, "izle" düğmesi taklidi yok.

## Kapak (`kapak-a.png` = `kapak.png`, 1080×1920)
A: sahne 01'in uçuş öncesi kanca karesi (≈ t 1,97), altyazı katmanı gizli (S1-KAPAK-A yöntemi: `proje` kopyasında CSS `#altyazi{display:none}`,
`hyperframes snapshot --at <t>`; `S1-VAR-RAPOR.md` son satırlar), açık + koyu. B (`05`, `kapak-b.png`) ve C (`06`, `kapak-c.png`): kanal katmanı,
altyazı yok; B öğrenci karakter görselini taşır (`ortak/kapak/karakter.png`, krem çıkartma kenarı). Tarif: `uretim-tutanagi/kapak-taslak.md`.

## Hikâye kareleri (`hikaye-a.png` = `hikaye.png`, `hikaye-b.png`; 1080×1920)
Durağan; ses yok; kanal katmanı + künye + kural özeti + `Kaydet` (yer imi simgesi). İçerik y 460–1140; y 1150–1380 boş zemin (bağ çıkartması
elle konur; boş kutu çizilmez); 1400–1920 boş. A (`04`): kural kartı düzeni (`YAŞI-YOR-UM` + `I live` PERMANENT / `I am living` TEMPORARY).
B (`07`): soru–cevap düzeni (`Şimdilik amcamla yaşıyorum.` → doğru `I am living with my uncle.` yeşil, soluk `I live with my uncle.`).
Eski `Tam ders:` / `profildeki bağlantı` satırı kalkar. Tarif: `uretim-tutanagi/hikaye-taslak.md` + `istem/sahne-v2/D-04…`, `D-07…`.

## Çalıştırma
Her sahne `calistir.sh --tema acik` (önizleme: `ONIZLE_YALNIZ=1`); birleştirme `python3 birlestir.py projeler/02-04-ydt-temel-s1 --tema acik
--gecis BookFlip --efekt hisirti` (mp4 takvimi gelince). Durağan kareler ayrı: `sahneler/<klasör>/calistir.sh --tema acik|koyu` → paket kökü PNG.
Ses yeniden kurulumu (sentez yok): `ortak/anlatim/` içinde `sozcuk_uret.py` → `zaman_uret.py` → `kur.py` →
`araclar/ses-paketle.py --yaz --paket 02-04-ydt-temel-s1` → `araclar/altyazi_uret.py projeler/02-04-ydt-temel-s1` → `metin_uret.py`.
Sahne istemleri: v2 `uretim-tutanagi/istem/sahne-v2/D-<klasör>.md` (eski `istem/sahne/` arşiv).
