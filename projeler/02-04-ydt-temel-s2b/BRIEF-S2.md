# S2 Shorts — "GENEL ≠ ŞU AN" (02-04-ydt-temel-s2, YDT TEMEL) · huni v2

Çıktı: `cikti.mp4` (1080×1920, 30 fps, 29.41 sn, anlatım 29.41 sn hazır) + `kapak-a.png` (+ kopyası `kapak.png`) + `kapak-b.png` +
`kapak-c.png` + `hikaye-a.png` (+ kopyası `hikaye.png`) + `hikaye-b.png` + `kontrol.png`. mp4 bugün üretilmez (huni v2 §1 kural 9).
Bağlayıcı standart: `D/.claude/docs/huni-v2-standart.md` (V2-S2-C, 15.11). Stil, kalem darbesi, olay sesi kuralları `../02-04-ydt-temel/BRIEF.md`
ile aynı; yazı tabanı ≥ 64 px. Biçim örneği: `../02-04-ydt-temel-s1/BRIEF-S1.md`. v1 BRIEF yedeği: `~/Silinecekler/2026-11-15-huni-v2/02-04-ydt-temel-s2/`.
Kaynaklar: ses `ortak/anlatim/` (cümle başları 1,00 · 3,39 · 17,96 · 23,30; toplam 29.41), senaryo `ortak/anlatim/senaryo.json`
(kaynak: `uretim-tutanagi/senaryo-taslak.md`, jüri düzeltmeleri `uretim-tutanagi/S2-duzeltme.md`; v2 değişikliği `uretim-tutanagi/V2-C-RAPOR.md`).

Kapak A başlığı (2 satır, 3 sözcük): `GENEL` / `≠ ŞU AN`. Can alıcı: "Önce anlama bak: genel mi, şu an mı? Kalıcı mı, geçici mi? Tarife mi,
plan mı?" (`canAlici[0]`, ilk soru). Ses: cümle 1–3 öğretmen Atakan (`gsJ9nrlXYbPztJxC4fwc`, figür `kadro.ogretmen`: ShirtPantsWB / Smile /
Short); cümle 4 (çağrı) öğrenci (`oPC5I9GKjMReiaM29gjY`, `kadro.ogrenci`; ana dersten kopya). Soru anı yok.

## Yerleşim (px) — huni v2 §2
Platform arayüzü üst 0–250, alt 1580–1920 ve sağ 960–1080 bölgesini kapatır. Çip (sağ üst bölüm etiketi) yok.

| Bölge | y | İçerik |
|---|---|---|
| Üst boş | 0–280 | yalnız zemin |
| Kanal katmanı | 280–350 | logo resmi x 53,2 (SVG iç boşluğu 68/1920 düşülür, görünür sol kenar x 60), y 291–339, yükseklik 48, genişlik 193,5 (en-boy 1920/476,3; açık `ortak/logo/yds-publishing-lacivert.svg`, koyu `yds-publishing-seffaf.svg`) + `@ydspublishing` Lexend 700 42 px, x 263, taban y 330, tema mürekkebi. İlk kareden son kareye, alfa 1, giriş/çıkış animasyonu yok; kimlik `kanal`, `__kalemKutu` türü `kunye`, ad `kunye:kanal`. Değerler S1 ile aynı (`../02-04-ydt-temel-s1/BRIEF-S1.md`) |
| Künye | 360–450 | konu `Simple Present vs Present Continuous` Fredoka 700, x 60, taban y 420, boy ≤ 34 (rozetle x 960'a sığan en büyük, alt sınır 28) · rozet hapı `YDT · TEMEL` Lexend 700 26 px, y 386–434, konu sonu + 20 |
| İçerik | 460–1380 | kart, çizim, kural; x 60–960 |
| Altyazı + karaoke | 1400–1550 | en çok 2 satır (`ortak/kunye.js` `altyaziCiz` bandı 1400–1536) |
| Alt boş | 1570–1920 | yalnız zemin |

Kanal katmanı tek ortak dosyadan gelmez: Paper.js sahnesi `ortak/kunye.js` kullanır (v1 HUD: logo y 48, ders adı y 212, rozet y 216, çip);
HyperFrames sahneleri her biri kendi `yardim.py` `kunye_svg` kopyasını taşır (6 farklı dosya). Bu yüzden değerler burada ve her sahne isteminde
aynı yazılır; sahne kendi dosyasında çizer. HyperFrames'te logo `<image>` kimliği `logoimg` kalır (`ortak/hf_tema.py` tema değişiminde logoyu değiştirir).

## Sahneler (zaman.json ile birebir)
| # | Klasör | Motor | Küresel sn | Kare | Çıktı |
|---|---|---|---|---|---|
| 01 | 01-hyperframes-kapak | HyperFrames | 0.00–2.84 | 97 | video + `kapak-a.png` (+ `kapak.png`) — kanca |
| 02 | 02-paperjs-ornek | Paper.js | 2.84–17.41 | 449 | video — değer |
| 03 | 08-hyperframes-kaydet | HyperFrames | 17.41–22.75 | 172 | video — kaydet (YENİ) |
| 04 | 03-hyperframes-cta | HyperFrames | 22.75–29.41 | 230 | video — çağrı (öğrenci sesi, ana ders kapağı) |
| — | 04-hyperframes-hikaye | HyperFrames | zaman çizelgesi dışı | 1 | `hikaye-a.png` (+ `hikaye.png`) |
| — | 05-hyperframes-kapak-b | HyperFrames | zaman çizelgesi dışı | 1 | `kapak-b.png` |
| — | 06-hyperframes-kapak-c | HyperFrames | zaman çizelgesi dışı | 1 | `kapak-c.png` |
| — | 07-hyperframes-hikaye-b | HyperFrames | zaman çizelgesi dışı | 1 | `hikaye-b.png` |

Sahne sınırı = bir sonraki cümle başı − 0,55; son sahne = son söz + 1,0 sn. Sahne 01 = cümle 1 (1,00–2,84; K23 giriş ≤ 3 sn).
Klasör adı ile sıra ayrıdır: `08-hyperframes-kaydet` zaman çizelgesinde 3. sırada. Durağan kareler `zaman.json` → `hikaye` (04) ve `duragan`
(05, 06, 07) alanlarındadır, `sahneler[]` dışında: `birlestir.py` ve `kur.py` yalnız `sahneler[]` okur, `cikti.mp4`'e girmez.

## Sahne içeriği (tablodaki sn KÜRESELDİR; yerel kare = round((t − t_bas) × 30))
Zaman sözcük çapasından okunur (`ortak/anlatim/sozcukler.json`), sabit saniyeden değil. Tek istisna 8,37–11,17 parçası (aşağıdaki DİKKAT).
01 ve 02'nin içeriği v1 ile aynıdır; yalnız yerleşim yukarıdaki bölgelere çekilir.

| sn | Hareket |
|---|---|
| 0,00 | Kapak A tam görünür (ilk kare = kapak): kanal katmanı; künye satırında yalnız rozet `YDT · TEMEL`; başlık `GENEL` (900 px'e sığan en büyük boy, üst sınır 190 px) / `≠ ŞU AN` sarı hapta (dolgu `#ffe066`, yazı `#1b2440`); solda askıda mont (`coat`), ortada işaret eden öğretmen figürü, sağda askıda pembe tişört (`t-shirt`); etiketler mont altında `wears`, tişört altında `is wearing` (Caveat ≥ 72); hepsi 460–1380 içinde |
| 0,30–0,80 | `≠` işareti hapın içinde kalemle çizilir (tek kalem hareketi) |
| 0,90 | Kapak karesi (kare 27): başlık tam, `≠` bitmiş, altyazı katmanı gizli → `kapak-a.png` |
| 1,00–2,84 | Cümle 1 altyazı bandında sözcük zamanlı: `Genel mi,` (`Genel` 1,00) · `şu an mı?` (`şu` 2,12 · `mı?` 2,52) |
| 2,24–2,84 | Uçuş: başlık küçülerek künye satırındaki konu adına iner (360–450); figür ve iki nesne solar; soru satırı `Genel mi, şu an mı?` (Caveat) içerik bandının üstüne (≈ 470–550) kalemle yazılır ve sahne 02 boyunca soru başlığı olarak durur (konumu sahne 02 kare 0 ile aynı) |
| 3,39–5,31 | Sahne 02. Kart 1 `She wears her coat` / `in the winter.` Fredoka 64 karaoke (`She` 3,39 · `wears` 3,67 · `coat` 4,27 · `winter.` 4,67); `coat` çapasında mont kalemle (ana ders `sahne-03.js` MONT dizisi); `in` (4,47) çapasında `in the winter` altına `odak` |
| 5,56–8,12 | `GENERAL` Caveat (`Genel` 5,56) · `Simple Present` ince yazı (`geniş` 6,68) · kart 1 altında `zaman_cizgisi`: uzun çizgide tekrar eden kısa kış bantları (küçük kar tanesi), now noktası bantların dışında |
| 8,37–11,17 | Kart 2 `She is wearing her` / `pink T-shirt today.` karaoke (`She` 8,37 · `is` 8,61 · `wearing` 8,77 · `pink` 9,45 · `T-shirt` 9,65 · `today.` 10,13); `T-shirt` çapasında pembe tişört kalemle (TISORT dizisi); `today` çapasında `odak` |
| 11,42–15,10 | `Today` (11,42): kart 2'deki `today` sarı daire (`isaret`) · `anlam` (14,14): `MEANING` sarı hap kart 2'nin sağında; üst soru satırı mürekkep altçizgi alır; `today` dairesi mürekkebe döner (o anda tek sarı `MEANING`). `Simple Present` etiketine ok YOK, kart 1'e bağ YOK |
| 15,25–17,41 | `RIGHT NOW` Caveat (`Konuşma` 15,25) · `Present Continuous` ince yazı (`şimdiki` 16,49) · `today` dairesinden `RIGHT NOW`'a tek ince kalem oku · kart 2 altında `zaman_cizgisi`: today gün bandı, now noktası bandın içinde nabız. İçerik 1380'de biter (sığmazsa aralık ve zaman çizgisi küçülür, yazı 64 altına inmez) |
| 17,41 | Sahne 08 (kaydet) kare 0: kanal katmanı + künye; içerik boş |
| 17,96–18,36 | `Bu,` (17,96): kural özeti kartı gelir (yumuşak ölçek 0,96 → 1 + opaklık), x 60–960, y ≈ 560–1000. Tek cümle, Fredoka 72, 3 satır: `Today iki zamanda` / `da geçebilir;` / `farkı anlam yapar.`; `Today` sarı hapta (tek vurgu) |
| 18,52 | `üç` (18,52): kartın altında üç küçük nokta (y ≈ 1040), birincisi dolu, ikisi boş halka (mürekkep; "üç farktan biri"); yazı yok |
| 18,36–22,75 | Kart sabit (hareket yok; en az 2 sn kuralı) |
| 20,47 | `kuralı` (20,47): yer imi simgesi (SVG, kalem çizgisi; emoji değil) kartın altında (y ≈ 1120–1260) kalemle çizilir (0,5 sn) |
| 22,15–22,75 | `Kaydet.` (22,15): `Kaydet` Fredoka 96 yer iminin sağında gelir, yer imi sarı dolgu alır (0,3 sn); aynı anda `Today` hapı mürekkep çerçeveye döner (tek sarı = yer imi) |
| 22,75 | Sahne 03 (çağrı) kare 0: kanal katmanı + künye; içerik boş |
| 23,30–24,74 | `Bitmedi,` (23,30): giriş sözü `Bitmedi, gel.` Fredoka 700 ≈ 96 px, y ≈ 480–600, sözcük zamanlı (`gel.` 24,26) |
| 24,89–26,17 | `Dersin` (24,89): ana dersin kapağı 16:9 kart, 900×506, x 60–960, y 627–1133 (standart "≈ 920×518"; sağ 960–1080 platform arayüzü altında kaldığı için 900); ince mürekkep çerçeve, köşe 24; açık tema `ortak/kapak/ana-kapak.png`, koyu `ortak/kapak/ana-kapak-koyu.png` |
| 26,17–28,41 | `YDS` (26,17): kartın altında (y ≈ 1170–1250) `@ydspublishing` sarı hap (tek vurgu) + ` · YouTube` Lexend 700 mürekkep. Oynat düğmesi, "izle" düğmesi taklidi, YouTube logosu yok |
| 28,41–29,41 | Durgun kuyruk: kapak kartı ve satırlar yerinde |

Altyazı `ortak/anlatim/altyazi.json` (10 parça; cümle 3: 17,96–20,12 · 20,27–22,75; cümle 4: 23,30–24,74 · 24,89–28,41, `konusan` `ogrenci`).

**DİKKAT:** 8,37–11,17 parçasının sözcükleri `sozcukler.json`'da YOK. Neden: el.py `T-shirt`'ü sese `T shirt` gönderir; sözcük sayısı
ekranla tutmaz, el.py o parçaya sözcük zamanı yazmaz (ana derste cümle 3 ve 9'da da aynı). Yukarıdaki çapalar ElevenLabs önbellek
hizalamasından türetildi (`~/.local/share/elevenlabs-onbellek/3e7a9af33838d05cd9a8083c218a882a935c6edf.hiz.json`, `T` + `shirt`
birleşik; parça başı 8,37 `sureler.json`'dan). Sahne kodu bu parça için çapaları bu tablodan sabit dizi olarak alır; kaynağı yorumda yazar.
`altyazi.json` bu kaymadan etkilenmez: paket içi `ortak/anlatim/altyazi_uret.py` parça sınırını `sureler.json` `parcalar` alanından okur.

Ekranda `T-shirt` tireli, seste `T shirt`. Ekranda ve seste `Tam ders` sözü, süre sözü ("dakika", "dk"), QR ve emoji yok. Seste "kanal" sözü
yalnız çağrı çekirdeğinde; ekranda `@ydspublishing · YouTube`. `METIN.md` başlığındaki "sahne 01 3 sn" S1 betiğinden kalma sabit metindir;
sahne 01 2,84 sn (`zaman.json`).

## Kapak A (`kapak-a.png` + kopyası `kapak.png`, 1080×1920)
Sahne 01'in uçuş öncesi karesi: t 0,90 (kare 27), tema açık, altyazı katmanı gizli. Yöntem S1-KAPAK-A (`../02-04-ydt-temel-s1/uretim-tutanagi/S1-VAR-RAPOR.md`
son 3 satır): sahne `proje` kopyasında yalnız CSS `#altyazi{display:none}`, `hyperframes snapshot --at 0.9`; koyu tema `sahneler/01-hyperframes-kapak/k/koyu/kapak-a-koyu.png`.
Karede: kanal katmanı, rozet, 2 satır başlık (`≠` bitmiş), mont + işaret eden figür + tişört, etiketler `wears` / `is wearing`. Tarif: `uretim-tutanagi/kapak-taslak.md` §1–§3.

## Kapak B (`kapak-b.png`) ve Kapak C (`kapak-c.png`), 1080×1920, durağan
Sahne 05 ve 06 tek kare üretir; ses yok; altyazı yok. Kanal katmanı ve künye yukarıdaki değerlerle.

| Bölge (y px) | B — soru (sahne 05) | C — karşıt çift (sahne 06) |
|---|---|---|
| 280–450 | kanal katmanı + künye | kanal katmanı + künye |
| 460–800 başlık | `TODAY VARSA` / `HANGİ ZAMAN?` (mürekkep, hapsız; motor ölçer, en geniş satır ≤ 900) | `AYNI FİİL,` / `İKİ ZAMAN` (mürekkep, hapsız) |
| 820–1380 sahne | kapak görseli `ortak/kapak/karakter.png` (öğrenci, iki avuç açık "hangisi?"; krem çıkartma kenarı) elinde ya da yanında `today` yazan takvim yaprağı; sağda büyük sarı `?` (tek vurgu) | kart 1 `She wears her coat` / `in the winter.` (köşede küçük mont) · kart 2 `She is wearing her` / `pink T-shirt today.` (köşede küçük tişört; `is wearing` altında sarı el altçizgisi, tek vurgu); figür yok |
| 1400–1920 | boş | boş |

`ortak/kapak/karakter.png` = `../02-04-ydt-temel/ortak/kapak/karakter.png` kopyası (md5 `3d846e4b…`, V2-S2-C). Tarif: `uretim-tutanagi/kapak-taslak.md` §4 (B), §5 (C).

## Hikâye A (`hikaye-a.png` + kopyası `hikaye.png`) ve Hikâye B (`hikaye-b.png`), 1080×1920, durağan
Anlatımdan bağımsız durağan kare; ses yok; süre yazmaz. Huni v2 §6: kanal katmanı + kural özeti + "Kaydet"; iki düzen farklı.
y 1150–1380 bağ çıkartması için boş zemin (boş kutu çizilmez); 1400–1920 boş.

| Bölge (y px) | A — kural kartı (sahne 04) | B — soru kartı (sahne 07) |
|---|---|---|
| 280–450 | kanal katmanı + künye | kanal katmanı + künye |
| 460–560 | `Genel mi, şu an mı?` (Caveat 72) | `Hangisi doğru?` (Fredoka 88) |
| 570–1000 | kural kartı (tek cümle, Fredoka 72): `Today iki zamanda` / `da geçebilir;` / `farkı anlam yapar.` (`Today` sarı hap, tek vurgu) · altında `wears → GENERAL` / `is wearing → RIGHT NOW` (Caveat 64) | kök `Look! She ____ her` / `pink T-shirt today.` (Fredoka 64; boşluk kalem çizgisi; köşede küçük tişört) · şık `A) wears` · şık `B) is wearing` (kart, Fredoka 64) · ipucu `Genel mi, şu an mı?` (Caveat 64; cevap değil) |
| 1010–1140 | yer imi (mürekkep çizgi) + `Kaydet` (Fredoka 88), sağa yaslı | yer imi (sarı dolgu, tek vurgu) + `Kaydet` (Fredoka 88), sola yaslı |

Hikâye B'de cevap karede YOK; şıklarda vurgu yok. Doğru şık B; yalnız `hikaye-taslak.md` §4 ve açıklama notunda. Tarif: `uretim-tutanagi/hikaye-taslak.md` §3, §4.

## Çalıştırma
Sahne istemleri: `uretim-tutanagi/istem/sahne-v2/D-<klasör>.md` (8 dosya; v1 istemleri `istem/sahne/` yerinde). Her video sahnesi
`calistir.sh --tema acik`; sonra paket kökünden `python3 birlestir.py projeler/02-04-ydt-temel-s2 --tema acik --gecis BookFlip --efekt hisirti`.
Durağan kareler ayrı: `sahneler/0{4,5,6,7}-…/calistir.sh --tema acik` → paket kökünde PNG (birleştirmeye girmez).
Ses yeniden kurulumu (sentez yok): `ortak/anlatim/` içinde `sozcuk_uret.py` → `zaman_uret.py` → `kur.py` →
`araclar/ses-paketle.py --yaz --paket 02-04-ydt-temel-s2` → `ortak/anlatim/altyazi_uret.py projeler/02-04-ydt-temel-s2` (paket kopyası;
`araclar/altyazi_uret.py` bu pakette kayar) → `metin_uret.py`. Sentez: `cd K && bash araclar/ses-sunucu.sh 02-04-ydt-temel-s2`.
