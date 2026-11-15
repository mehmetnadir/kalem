# S1 Shorts — "YAŞIYORUM = İKİ ZAMAN" (02-04-ydt-temel-s1, YDT TEMEL)

Çıktı: `cikti.mp4` (1080×1920, 30 fps, 30.56 sn, anlatım 30.56 sn hazır) + `kapak.png` + `hikaye.png` + `kontrol.png`.
Ana BRIEF biçimi dikeye uyarlandı; stil, kalem darbesi, olay sesi kuralları `../02-04-ydt-temel/BRIEF.md` ile aynı; dikey v2 ölçekleri
`../present-continuous-dikey/BRIEF-DIKEY.md` §2–§3 (HUD, ders adı 56, rozet 36, ≥ 64 px yazı). Kaynaklar: ses `ortak/anlatim/`
(cümle başları 1,00 · 6,91 · 20,54; toplam 30.56), senaryo `ortak/anlatim/senaryo.json`
(kaynak: `uretim-tutanagi/senaryo-taslak.md`, jüri düzeltmeleri `uretim-tutanagi/S1-duzeltme.md`). `ortak/kunye.js` dikey v2 tabanlıdır
(`02-04-ydt-temel-dikey/ortak/kunye.js` kopyası: ders adı 2 satır `SIMPLE PRESENT vs` / `PRESENT CONTINUOUS`, tek rozet `YDT · BASIC`
2. satırın sağında; `GRAMMAR` rozeti yok); çip sağ üst `KUNYE.cipler[<klasör>]`.

Kapak başlığı (2 satır, 3 sözcük): `YAŞIYORUM` / `= İKİ ZAMAN`. Can alıcı: "Türkçe yaşıyorum iki zamana karşılık gelir: I live (kalıcı),
I am living (geçici)" (`canAlici[4]`, ana ders kancası). Ses öğretmen Atakan (`gsJ9nrlXYbPztJxC4fwc`), figür öğretmen erkek
(`kadro.ogretmen`: ShirtPantsWB / Smile / Short). Soru anı yok, öğrenci sesi yok.

**DİKKAT:** toplam 30,56 sn; kalıp §5 aralığı (15–30 sn) 0,56 sn aşılır. Karar şefte (`uretim-tutanagi/S1-C-RAPOR.md` açık nokta 1).

## Dikey yerleşim (px) — dikey v2 bantları
Yerleşim ve ölçek: ../present-continuous-s1/BRIEF-S1.md '05.11 düzeltme' bölümü +
../present-continuous-dikey/BRIEF-DIKEY.md §2–§3
(tek kaynak, 05.11 karar 6b). HUD 0–320 · içerik 352–1392 · altyazı 1400–1536 · platform 1536–1920 BOŞ.

## Sahneler (zaman.json ile birebir)
| # | Klasör | Motor | Küresel sn | Kare |
|---|---|---|---|---|
| 01 | 01-hyperframes-kapak | HyperFrames | 0.00–3.00 | 102 |
| 02 | 02-paperjs-ornek | Paper.js | 3.00–19.99 | 522 |
| 03 | 03-hyperframes-cta | HyperFrames | 19.99–30.56 | 347 |
| — | 04-hyperframes-hikaye | HyperFrames | zaman çizelgesi dışı | 1 (`hikaye.png`) |

Sahne sınırı = bir sonraki cümle başı − 0,55; son sahne = son söz + 1,0 sn. Sahne 01 → 02 sınırı 3,00 (K23 giriş ≤ 3 sn).
Hikâye karesi `zaman.json` → `hikaye` alanındadır, `sahneler[]` dışında: `birlestir.py` ve `kur.py` yalnız `sahneler[]` okur,
`cikti.mp4`'e girmez.

## Sahne içeriği (tablodaki sn KÜRESELDİR; yerel kare = round((t − t_bas) × 30))
Zaman sözcük çapasından okunur (`ortak/anlatim/sozcukler.json`), sabit saniyeden değil.

| sn | Hareket |
|---|---|
| 0,00 | Kapak tam görünür (ilk kare = kapak): rozet `YDT · BASIC`; başlık `YAŞIYORUM` (952 px'e sığan en büyük boy, üst sınır 190 px) / `= İKİ ZAMAN` sarı hapta (dolgu `#ffe066`, yazı `#1b2440`); solda ev (house), sağda elinde bavul (suitcase) tutan öğretmen figürü; etiketler ev yanında `I live`, bavul yanında `I am living` (Caveat ≥ 72) |
| 0,30–0,80 | `YOR` altına sarı el altçizgisi (`alti`) |
| 1,00–2,10 | Cümle 1 sözcük zamanlı: `İstanbul'da yaşı-yor-um.` (`İstanbul'da` 1,00 · `yaşıyorum.` 1,64) |
| 2,0–3,0 | Uçuş: başlık üst bant ders adına, figür ve ev solar (present-continuous-ileri-s1 kalıbı); cümle satırları içerik bandının üstüne |
| 2,52 | İkinci satır `Amcamla yaşı-yor-um.` (`Amcamla` 2,52); sahne 01 iki satır taşır |
| 3,08 | Sahne 02: iki satır yerinde sürer; `yaşıyorum.` karaokesi (3,08) |
| 3,96–6,36 | `Türkçede ikisi de yaşıyorum.` (`Türkçede` 3,96 · `ikisi` 4,84 · `yaşıyorum.` 5,56): `ek_ayir`, iki satırda *yor* sarı kutuda kayar (ana ders sahne 01 ile aynı) |
| 6,91–8,83 | `İngilizcede ikisi ayrılır.` (`ayrılır.` 8,19): TR satırlar yukarı solar, iki *yor* kutusu kalır |
| 9,08–10,92 | Kart 1 `I live in İstanbul.` Fredoka 64 sözcük zamanlı (`I` 9,08 · `live` 9,32 `odak` · `Istanbul.` 9,64); `bag`: üst *yor* kutusundan karta kalem çizgisi; ev ikonu kart köşesinde küçük |
| 11,17–14,45 | Kart 1 altında soluk TR `Hep orada.` (11,17) · `PERMANENT` etiketi (`kalıcı` 12,37) · `zaman_cizgisi` uzun bant (`geniş` 13,25), now noktası bandın içinde |
| 14,70–16,78 | Kart 2 `I am living` / `with my uncle.` (`I` 14,70 · `am` 14,90 · `living` 15,02 `odak` · `uncle.` 15,74); `bag`: alt *yor* kutusundan karta; bavul ikonu kart köşesinde küçük |
| 17,03–19,99 | Kart 2 altında soluk TR `Şimdilik.` (17,03) · `TEMPORARY` etiketi (`geçici` 18,07) · kısa bant, now noktası bandın içinde (`şimdiki` 19,03) |
| 20,54–22,62 | Sahne 03 (CTA): `üç farktan biri` Lexend (`üç` 21,02) |
| 22,77–26,85 | `Tam ders:` Caveat (22,77) · ders bandı Fredoka `Simple Present` (23,97) / `vs Present Continuous` (`vs` = `ve` çapası 24,77; `Present` 25,25) |
| 27,00–29,56 | `üç farkın hepsi` Lexend (`Üç` 27,00) · saat (clock) + `dört buçuk dakikada` (`dört` 28,36 · `dakikada.` 28,84) · `@ydspublishing` sarı hap (dolgu `#ffe066`, yazı `#1b2440`) son sözle (`dakikada.` 28,84–29,64) |
| 29,56–30,56 | Durgun kuyruk; son karede ev ve bavul ikonu bandın iki yanında küçük → kapak karesine döngü (kalıp §1 kural 5) |

Ekranda "İstanbul" noktalı, seste "Istanbul" (EN parça). `@ydspublishing` sesle okunmaz. "kanal" sözü yok, QR yok, emoji yok.

## Kapak (`kapak.png`, 1080×1920)
Sahne 01'in uçuş öncesi karesi: t 1,97 (kare 59), tema açık, çip yok. `calistir.sh` örnekteki gibi `video.mp4`'ten
`select=eq(n\,59)` ile paket köküne `kapak.png` yazar (present-continuous-ileri-s1 `01-hyperframes-kapak/calistir.sh` satır 34–36).
Karede: rozet, 2 satır başlık (`YOR` altçizgisi bitmiş), ev + bavullu figür, etiketler `I live` / `I am living`, cümle satırı
`İstanbul'da yaşı-yor-um.`, altyazı bandında cümle 1'in ilk dilimi (`kunye.js` altyaziDilimle). Logo sol alt y ≈ 1478. Tarif: `uretim-tutanagi/kapak-taslak.md`.

## Hikâye karesi (`hikaye.png`, 1080×1920)
Anlatımdan bağımsız durağan kare; ses yok; süre yazmaz. Sahne `04-hyperframes-hikaye` tek kare üretir, paket köküne `hikaye.png`
(açık) yazar. Tarif: `uretim-tutanagi/hikaye-taslak.md` §3.

| Bant (y px) | Metin |
|---|---|
| 0–288 HUD | rozet `YDT · BASIC` · ders adı `Simple Present vs Present Continuous` (2 satır, 56 px) |
| 300–420 | `Türkçede tek sözcük` (Lexend 64) |
| 440–700 | `YAŞI-YOR-UM` (Fredoka; `YOR` sarı kutuda, `ek_ayir` görünümü; 952 px'e sığan en büyük boy) |
| 720–1180 | kart 1 `I live` · `PERMANENT` · ev ikonu + uzun bant · kart 2 `I am living` · `TEMPORARY` · bavul ikonu + kısa bant |
| 1190–1300 | `İngilizcede iki zaman` (Lexend 64) |
| 1344–1536 | `Tam ders:` / `profildeki bağlantı` (Caveat 72) · `@ydspublishing` sarı hap · logo sol alt y ≈ 1478 |
| 1536–1920 | boş (platform arayüzü) |

## Çalıştırma
Her sahne `calistir.sh --tema acik`; sonra paket kökünden
`python3 birlestir.py projeler/02-04-ydt-temel-s1 --tema acik --gecis BookFlip --efekt hisirti`.
Hikâye karesi ayrı: `sahneler/04-hyperframes-hikaye/calistir.sh --tema acik` → `hikaye.png` (birleştirmeye girmez).
Ses yeniden kurulumu (sentez yok): `ortak/anlatim/` içinde `sozcuk_uret.py` → `zaman_uret.py` → `kur.py` →
`araclar/ses-paketle.py --yaz --paket 02-04-ydt-temel-s1` → `araclar/altyazi_uret.py projeler/02-04-ydt-temel-s1` → `metin_uret.py`.
Sahne istemleri: `uretim-tutanagi/istem/sahne/D-<klasör>.md`.
