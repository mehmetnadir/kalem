# S2 Shorts — "GENEL ≠ ŞU AN" (02-04-ydt-temel-s2, YDT TEMEL)

Çıktı: `cikti.mp4` (1080×1920, 30 fps, 27.98 sn, anlatım 27.98 sn hazır) + `kapak-a.png` (+ kopyası `kapak.png`) + `kapak-b.png` +
`kapak-c.png` + `hikaye-a.png` (+ kopyası `hikaye.png`) + `hikaye-b.png` + `kontrol.png`.
Ana BRIEF biçimi dikeye uyarlandı; stil, kalem darbesi, olay sesi kuralları `../02-04-ydt-temel/BRIEF.md` ile aynı; dikey v2 ölçekleri
`../present-continuous-dikey/BRIEF-DIKEY.md` §2–§3 (HUD, ders adı 56, rozet 36, ≥ 64 px yazı). Biçim örneği: `../02-04-ydt-temel-s1/BRIEF-S1.md`.
Kaynaklar: ses `ortak/anlatim/` (cümle başları 1,00 · 3,39 · 17,96; toplam 27.98), senaryo `ortak/anlatim/senaryo.json`
(kaynak: `uretim-tutanagi/senaryo-taslak.md`, jüri düzeltmeleri `uretim-tutanagi/S2-duzeltme.md`). `ortak/kunye.js` = S1 kopyası
(ders adı 2 satır `SIMPLE PRESENT vs` / `PRESENT CONTINUOUS`, tek rozet `YDT · BASIC`); çip sağ üst `KUNYE.cipler[<klasör>]` (7 klasör).

Kapak A başlığı (2 satır, 3 sözcük): `GENEL` / `≠ ŞU AN`. Can alıcı: "Önce anlama bak: genel mi, şu an mı? Kalıcı mı, geçici mi? Tarife mi,
plan mı?" (`canAlici[0]`, ilk soru). Ses öğretmen Atakan (`gsJ9nrlXYbPztJxC4fwc`), figür öğretmen erkek (`kadro.ogretmen`:
ShirtPantsWB / Smile / Short). Soru anı yok, öğrenci sesi yok.

## Dikey yerleşim (px) — dikey v2 bantları
Yerleşim ve ölçek: ../present-continuous-s1/BRIEF-S1.md '05.11 düzeltme' bölümü + ../present-continuous-dikey/BRIEF-DIKEY.md §2–§3
(tek kaynak, 05.11 karar 6b). HUD 0–320 · içerik 352–1392 · altyazı 1400–1536 · platform 1536–1920 BOŞ.

## Sahneler (zaman.json ile birebir)
| # | Klasör | Motor | Küresel sn | Kare | Çıktı |
|---|---|---|---|---|---|
| 01 | 01-hyperframes-kapak | HyperFrames | 0.00–2.84 | 97 | video + `kapak-a.png` (+ `kapak.png`) |
| 02 | 02-paperjs-ornek | Paper.js | 2.84–17.41 | 449 | video |
| 03 | 03-hyperframes-cta | HyperFrames | 17.41–27.98 | 347 | video |
| — | 04-hyperframes-hikaye | HyperFrames | zaman çizelgesi dışı | 1 | `hikaye-a.png` (+ `hikaye.png`) |
| — | 05-hyperframes-kapak-b | HyperFrames | zaman çizelgesi dışı | 1 | `kapak-b.png` |
| — | 06-hyperframes-kapak-c | HyperFrames | zaman çizelgesi dışı | 1 | `kapak-c.png` |
| — | 07-hyperframes-hikaye-b | HyperFrames | zaman çizelgesi dışı | 1 | `hikaye-b.png` |

Sahne sınırı = bir sonraki cümle başı − 0,55; son sahne = son söz + 1,0 sn. Sahne 01 = cümle 1 (1,00–2,84; K23 giriş ≤ 3 sn).
Durağan kareler `zaman.json` → `hikaye` (04) ve `duragan` (05, 06, 07) alanlarındadır, `sahneler[]` dışında: `birlestir.py` ve
`kur.py` yalnız `sahneler[]` okur, `cikti.mp4`'e girmez.

## Sahne içeriği (tablodaki sn KÜRESELDİR; yerel kare = round((t − t_bas) × 30))
Zaman sözcük çapasından okunur (`ortak/anlatim/sozcukler.json`), sabit saniyeden değil. Tek istisna 8,37–11,17 parçası (aşağıdaki DİKKAT).

| sn | Hareket |
|---|---|
| 0,00 | Kapak A tam görünür (ilk kare = kapak): rozet `YDT · BASIC`; başlık `GENEL` (952 px'e sığan en büyük boy, üst sınır 190 px) / `≠ ŞU AN` sarı hapta (dolgu `#ffe066`, yazı `#1b2440`); solda askıda mont (`coat`), ortada işaret eden öğretmen figürü, sağda askıda pembe tişört (`t-shirt`); etiketler mont altında `wears`, tişört altında `is wearing` (Caveat ≥ 72) |
| 0,30–0,80 | `≠` işareti hapın içinde kalemle çizilir (tek kalem hareketi) |
| 0,90 | Kapak karesi (kare 27): başlık tam, `≠` bitmiş, altyazı henüz yok → `kapak-a.png` |
| 1,00–2,84 | Cümle 1 altyazı bandında sözcük zamanlı: `Genel mi,` (`Genel` 1,00) · `şu an mı?` (`şu` 2,12 · `mı?` 2,52) |
| 2,24–2,84 | Uçuş: başlık üst bant ders adına, figür ve iki nesne solar; soru satırı `Genel mi, şu an mı?` (Caveat) içerik bandının üstüne kalemle yazılır ve sahne 02 boyunca soru başlığı olarak durur (konumu sahne 02 kare 0 ile aynı) |
| 3,39–5,31 | Sahne 02. Kart 1 `She wears her coat` / `in the winter.` Fredoka 64 karaoke (`She` 3,39 · `wears` 3,67 · `coat` 4,27 · `winter.` 4,67); `coat` çapasında mont kalemle (ana ders `sahne-03.js` MONT dizisi); `in` (4,47) çapasında `in the winter` altına `odak` |
| 5,56–8,12 | `GENERAL` Caveat (`Genel` 5,56) · `Simple Present` ince yazı (`geniş` 6,68) · kart 1 altında `zaman_cizgisi`: uzun çizgide tekrar eden kısa kış bantları (küçük kar tanesi), now noktası bantların dışında |
| 8,37–11,17 | Kart 2 `She is wearing her` / `pink T-shirt today.` karaoke (`She` 8,37 · `is` 8,61 · `wearing` 8,77 · `pink` 9,45 · `T-shirt` 9,65 · `today.` 10,13); `T-shirt` çapasında pembe tişört kalemle (TISORT dizisi); `today` çapasında `odak` |
| 11,42–15,10 | `Today` (11,42): kart 2'deki `today` sarı daire (`isaret`) · `anlam` (14,14): `MEANING` sarı hap kart 2'nin sağında; üst soru satırı `Genel mi, şu an mı?` mürekkep altçizgi alır; `today` dairesi mürekkebe döner (o anda tek sarı `MEANING`). `Simple Present` etiketine ok YOK, kart 1'e bağ YOK |
| 15,25–17,41 | `RIGHT NOW` Caveat (`Konuşma` 15,25) · `Present Continuous` ince yazı (`şimdiki` 16,49) · `today` dairesinden `RIGHT NOW`'a tek ince kalem oku · kart 2 altında `zaman_cizgisi`: today gün bandı, now noktası bandın içinde nabız (ana ders sahne 08 görseli) |
| 17,96–20,04 | Sahne 03 (CTA): `üç farktan biri` Lexend (`üç` 18,44) |
| 20,19–24,27 | `Tam ders:` Caveat (`Tam` 20,19) · ders bandı Fredoka `Simple Present` (`Simple` 21,39) / `vs Present Continuous` (`vs` = sesteki `ve` çapası 22,19; `Present` 22,67) |
| 24,42–26,98 | `üç farkın hepsi` Lexend (`Üç` 24,42) · saat (clock) + `dört buçuk dakikada` (`dört` 25,78 · `dakikada.` 26,26) · `@ydspublishing` sarı hap (dolgu `#ffe066`, yazı `#1b2440`) son sözle (`dakikada.` 26,26–26,98) |
| 26,98–27,98 | Durgun kuyruk; son karede mont ve tişört ikonu bandın iki yanında küçük → kapak karesine döngü (kalıp §1 kural 5) |

**DİKKAT:** 8,37–11,17 parçasının sözcükleri `sozcukler.json`'da YOK. Neden: el.py `T-shirt`'ü sese `T shirt` gönderir; sözcük sayısı
ekranla tutmaz, el.py o parçaya sözcük zamanı yazmaz (ana derste cümle 3 ve 9'da da aynı). Yukarıdaki çapalar ElevenLabs önbellek
hizalamasından türetildi (`~/.local/share/elevenlabs-onbellek/3e7a9af33838d05cd9a8083c218a882a935c6edf.hiz.json`, `T` + `shirt`
birleşik; parça başı 8,37 `sureler.json`'dan). Sahne kodu bu parça için çapaları bu tablodan sabit dizi olarak alır; kaynağı yorumda yazar.
`altyazi.json` bu kaymadan etkilenmez: paket içi `ortak/anlatim/altyazi_uret.py` parça sınırını `sureler.json` `parcalar` alanından okur.

Ekranda `T-shirt` tireli, seste `T shirt`. `@ydspublishing` sesle okunmaz. "kanal" sözü yok, QR yok, emoji yok. `METIN.md` başlığındaki
"sahne 01 3 sn" S1 betiğinden kalma sabit metindir; sahne 01 2,84 sn (`zaman.json`).

## Kapak A (`kapak-a.png` + kopyası `kapak.png`, 1080×1920)
Sahne 01'in uçuş öncesi karesi: t 0,90 (kare 27), tema açık, çip yok, altyazı yok. `calistir.sh` render dalı `video.mp4`'ten
`select=eq(n\,27)` ile paket köküne `kapak-a.png` yazar ve `kapak.png` olarak kopyalar (S1 `01-hyperframes-kapak/calistir.sh` kalıbı).
Karede: rozet, 2 satır başlık (`≠` bitmiş), mont + işaret eden figür + tişört, etiketler `wears` / `is wearing`. Logo sol alt y ≈ 1478.
Tarif: `uretim-tutanagi/kapak-taslak.md` §1–§3.

## Kapak B (`kapak-b.png`) ve Kapak C (`kapak-c.png`), 1080×1920, durağan
Sahne 05 ve 06 tek kare üretir (S1 `05-hyperframes-kapak-b`, `06-hyperframes-kapak-c` kalıbı); ses yok; altyazı bandı boş.

| Bant (y px) | B — soru (sahne 05) | C — karşıt çift (sahne 06) |
|---|---|---|
| 0–288 HUD | rozet `YDT · BASIC` | rozet `YDT · BASIC` |
| 288–768 başlık | `TODAY VARSA` / `HANGİ ZAMAN?` (mürekkep, hapsız; ≈ 144 px, motor ölçer) | `AYNI FİİL,` / `İKİ ZAMAN` (mürekkep, hapsız) |
| 864–1344 sahne | düşünen öğretmen (el çenede), elinde `today` yazan takvim yaprağı; sağda büyük sarı `?` (tek vurgu) | kart 1 `She wears her coat` / `in the winter.` (köşede küçük mont) · kart 2 `She is wearing her` / `pink T-shirt today.` (köşede küçük tişört; `is wearing` altında sarı el altçizgisi, tek vurgu); figür yok |
| 1344–1536 | boş · logo sol alt y ≈ 1478 | boş · logo sol alt y ≈ 1478 |
| 1536–1920 | boş (platform arayüzü) | boş (platform arayüzü) |

Tarif: `uretim-tutanagi/kapak-taslak.md` §4 (B), §5 (C), §6 tablo (satir1, satir2, can alıcı).

## Hikâye A (`hikaye-a.png` + kopyası `hikaye.png`) ve Hikâye B (`hikaye-b.png`), 1080×1920, durağan
Anlatımdan bağımsız durağan kare; ses yok; süre yazmaz. Sahne 04 (A) ve 07 (B) tek kare üretir. Tarif: `uretim-tutanagi/hikaye-taslak.md` §3, §4.

| Bant (y px) | A — bilgi kartı (sahne 04) | B — soru kartı (sahne 07) |
|---|---|---|
| 0–288 HUD | rozet `YDT · BASIC` · ders adı (2 satır, 56 px) | aynı |
| 300–440 | `Genel mi, şu an mı?` (Lexend 64) | `Hangisi doğru?` (Fredoka 96) |
| 430–1000 | kart 1 `She wears her coat` / `in the winter.` · `GENERAL` · küçük mont + kış bantları · kart 2 `She is wearing her` / `pink T-shirt today.` · `RIGHT NOW` · küçük tişört + today bandı | kök `Look! She ____ her` / `pink T-shirt today.` (Fredoka 72; boşluk kalem çizgisi; köşede küçük tişört) · şık `A) wears` · şık `B) is wearing` (kart, Fredoka 72) |
| 1010–1300 | `today` (sarı hap, tek vurgu) · `iki zamanda da geçebilir` · `Farkı anlam yapar.` (Lexend 64) | ipucu `Genel mi, şu an mı?` (Caveat 64; cevap değil) |
| 1344–1536 | `Tam ders:` / `profildeki bağlantı` (Caveat 72) · `@ydspublishing` sarı hap · logo sol alt y ≈ 1478 | `Cevap ve neden:` / `tam derste` (Caveat 72) · `@ydspublishing` sarı hap · logo sol alt |
| 1536–1920 | boş (platform arayüzü) | boş |

Hikâye B'de cevap karede YOK ve sarı vurgu yok (şık vurgusu cevabı verir). Doğru şık B; yalnız `hikaye-taslak.md` §4 ve açıklama notunda.

## Çalıştırma
Her video sahnesi `calistir.sh --tema acik`; sonra paket kökünden
`python3 birlestir.py projeler/02-04-ydt-temel-s2 --tema acik --gecis BookFlip --efekt hisirti`.
Durağan kareler ayrı: `sahneler/0{4,5,6,7}-…/calistir.sh --tema acik` → paket kökünde PNG (birleştirmeye girmez).
Ses yeniden kurulumu (sentez yok): `ortak/anlatim/` içinde `sozcuk_uret.py` → `zaman_uret.py` → `kur.py` →
`araclar/ses-paketle.py --yaz --paket 02-04-ydt-temel-s2` → `ortak/anlatim/altyazi_uret.py projeler/02-04-ydt-temel-s2` (paket kopyası;
`araclar/altyazi_uret.py` bu pakette kayar) → `metin_uret.py`.
Sahne istemleri: `uretim-tutanagi/istem/sahne/D-<klasör>.md` (7 dosya).
