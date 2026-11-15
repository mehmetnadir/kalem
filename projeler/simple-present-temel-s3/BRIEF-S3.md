# S3 Shorts — "BU CÜMLE YANLIŞ" (simple-present-temel-s3, YDT TEMEL) · huni v2

**DUZ2 (16.11, J2-OZET A1–A3, A7; rapor `uretim-tutanagi/DUZ2-RAPOR.md`):** rozet `YDT · TEMEL`; cümle 2 "He, she, it ile olumsuzda ve soruda
does girer; s ona geçer. Fiile s gelmez. He doesn't go. Does she go?" (yalnız cümle 2 yeniden sentez); karakter kadın öğrenci (ana paket
`ortak/kapak/karakter.png`, sha256 `5a902b40…`; ana kapak da yeni); kanca `?`, sahne 02 `✗` ve üstü çizgi, kapak C ve hikâye A işaretleri
kırmızı değil mürekkep (çizilen `es` soluk tona geçer); sahne 02 kapsam etiketi `he, she, it` (soluk el yazısı, "He, … it" anında).
Yeni zamanlar: cümle başları 1,00 · 4,44 · 15,64 · 20,90; son söz 26,33; toplam 27,33 sn; sahne 02 3,89–15,09 (348 kare), 03 15,09–20,35,
04 20,35–27,33. Aşağıdaki zaman tablosu DUZ2 öncesidir: 4,44 sonrası her an +2,25 sn kayar; `does` 8,05, `s` 9,17, `gelmez.` 11,40, `He` 12,61.

Çıktı: önizleme (mp4 yok, standart §1 kural 9; 1080×1920, 30 fps, 27,33 sn, anlatım 27,33 sn hazır; DUZ2 öncesi 25,08) + `kapak-a|b|c.png` (`kapak.png` = A)
+ `hikaye-a|b.png` (`hikaye.png` = A). Bağlayıcı standart: `D/.claude/docs/huni-v2-standart.md` (15.11; bu belge onunla çelişirse standart geçer).
Biçim emsali: `../02-04-ydt-temel-s1/BRIEF-S1.md` (v2). Stil, kalem darbesi, olay sesi kuralları `../simple-present-temel/BRIEF.md` ile aynı.
Öğe `02-02-ydt-temel`; ana paket `../simple-present-temel/` (kadro, ses kimlikleri, ana kapak). Biçim: yanlış–doğru (standart §5).
Kaynaklar: ses `ortak/anlatim/` (cümle başları 1,00 · 4,44 · 13,39 · 18,65; son söz 24,08; toplam 25,08), senaryo `ortak/anlatim/senaryo.json`
(kaynak: `uretim-tutanagi/senaryo-taslak.md`, jüri `uretim-tutanagi/juri/`, düzeltme `uretim-tutanagi/S3-duzeltme.md`, rapor `uretim-tutanagi/S3-C-RAPOR.md`).

Kapak başlığı (2 satır, 3 sözcük): `BU CÜMLE` / `YANLIŞ` (sarı hap). Can alıcı: ana `senaryo.json` cümle 7 parça 4 "Olumsuzda ve soruda does
girer, s ona geçer." (`meta.kapak.canAlici` boş; ana listede madde yok, `S3-duzeltme.md` madde 5). Ses: cümle 1–3 öğretmen Atakan
(`gsJ9nrlXYbPztJxC4fwc`), cümle 4 (çağrı) öğrenci (`kadro.ogrenci`, `oPC5I9GKjMReiaM29gjY`). Figür çizilmez; karakter görseli
`ortak/kapak/karakter.png` (ana ders kopyası; ana kapaktaki karakterle aynı).
Kural özeti (kaydet kartı, hikâye kareleri, kapak C; tek cümle): `Does varsa` / `fiil yalın.`

## Yerleşim (px) — huni v2 §2
| Bölge | y | İçerik |
|---|---|---|
| Üst boş | 0–280 | yalnız zemin; çip YOK |
| Kanal katmanı | 280–350 | aşağıdaki tablo; kalıcı |
| Künye | 360–450 | konu `Simple Present` (Fredoka 700, x 60, taban 420; boy ≤ 34, rozetle x 960'a sığan en büyük, alt sınır 28) + rozet `YDT · TEMEL` (hap y 386–434, Lexend 700 26, dolgu `vurguDolgu`, yazı `pilMetin`, konu sonu + 20) |
| İçerik | 460–1380 | x 60–960 |
| Altyazı + karaoke | 1400–1550 | en çok 2 satır (kapak ve hikâye karelerinde yok) |
| Alt boş | 1570–1920 | yalnız zemin |

Kanal katmanı (bütün sahnelerde AYNI piksel; değerler emsal BRIEF-S1 tablosundan AYNEN; ortak modül yok: canvas `ortak/kunye.js`,
HyperFrames sahne başına `yardim.py`):

| Öğe | Değer |
|---|---|
| Logo | `ortak/logo/` (açık `yds-publishing-lacivert.svg`, koyu `yds-publishing-seffaf.svg`); yükseklik 48, genişlik 193,5 (48 × 1920 / 476,3); resim x 53,2 (SVG iç boşluğu 68/1920 düşülür, görünür sol kenar x 60), y 291–339 |
| Yazı | `@ydspublishing`, Lexend 700 42 px, renk `murekkep`, x 263, taban y 330 |
| Davranış | 0. kareden son kareye; opaklık 1; giriş/çıkış animasyonu yok; uçuş ve geçiş dokunmaz; kimlik `kanal`; `__kalemKutu` türü `kunye`, ad `kunye:kanal` |

Renk (açık tema, ana BRIEF §2.1): zemin `#f7f3ea`, mürekkep `#1b2440`, vurgu dolgu `#ffe066`, yazı `pilMetin` `#1b2440`, doğru yeşil,
kırmızı `#d6453a` YALNIZ yanlış işaretinde (üstü çizili `es`, `✗`, `?`). Koyu tema çifti zorunlu.

## Sahneler (zaman.json ile birebir)
| # | Klasör | Motor | Küresel sn | Kare | Ses |
|---|---|---|---|---|---|
| 1 Kanca | 01-hyperframes-kanca | HyperFrames | 0,00–3,89 | 129 | öğretmen |
| 2 Değer | 02-paperjs-deger | Paper.js | 3,89–12,84 | 281 | öğretmen |
| 3 Kaydet | 03-hyperframes-kaydet | HyperFrames | 12,84–18,10 | 170 | öğretmen |
| 4 Çağrı | 04-hyperframes-cagri | HyperFrames | 18,10–25,08 | 239 | öğrenci |
| — | 05-hyperframes-hikaye-a · 06-…-kapak-b · 07-…-kapak-c · 08-…-hikaye-b | HyperFrames | zaman çizelgesi dışı | 1 | — |

Sahne sınırı = bir sonraki cümle başı − 0,55 (= cümle bitişi); son sahne = son söz + 1,0 sn. Kanca sınırı: huni v2 §3 "0–4 sn"
(`zaman_uret.py` `GIRIS_SN = 4.0`; cümle 1 3,89'da biter, tamamı sahne 01'de). Kare = içerik + 12 geçiş (son sahne + 30).
Durağan kareler `zaman.json` → `hikaye` (05) ve `duragan[]` (06–08) alanındadır, `sahneler[]` dışında: `birlestir.py` ve `kur.py` yalnız
`sahneler[]` okur.

## Sahne içeriği (tablodaki sn KÜRESELDİR; yerel kare = round((t − t_bas) × 30))
Zaman sözcük çapasından okunur (`ortak/anlatim/sozcukler.json`), sabit saniyeden değil. Ekran metni sesten önce gelmez; kapak A istisnadır.

| sn | Hareket |
|---|---|
| 0,00 | Kapak tam görünür (ilk kare = kapak, kanal katmanı + künye dahil): başlık `BU CÜMLE` (900 px'e sığan en büyük boy, üst sınır 190) / `YANLIŞ` sarı hapta; kart `He doesn't goes.` (Fredoka 80, sol, x 60–640, y ≈ 840–1000); karakter sağda (`ortak/kapak/karakter.png`, x ≈ 600–950, y ≈ 880–1380, sola karta işaret eder; arkasında sarı daire, 10 px krem çıkartma kenarı) |
| 0,30–0,80 | `YANLIŞ` hap çerçevesi kalemle çizilir |
| 0,90 | Kapak A karesi (başlık tam, hap çizili; karaoke ve kırmızı `?` yok) |
| 1,00–2,44 | Kart karaoke: `He` 1,00 · `doesn't` 1,32 · `goes.` 1,72 |
| 2,69–3,15 | `Hata` 2,69: kartın sağ üstüne kırmızı kalem `?`; altyazı `Hata nerede?` (`nerede?` 3,09) |
| 3,39–3,89 | Başlık söner, karakter sağa kayıp çıkar, kart içerik bandının üstüne (y ≈ 480) kayar; kanal katmanı ve künye yerinde |
| 3,89–4,44 | Sahne 02 kare 0: kart `He doesn't goes.` y ≈ 480'de (sahne 01 son karesiyle aynı konum) |
| 4,44–8,36 | Altyazı karaoke `Olumsuzda ve soruda does girer, s ona geçer.`; `does` 6,28: karttaki `doesn't` içinde `does` sarı kalem dairesi; `s` 7,24: `goes`'un `es` ekinden `does`'a kavisli kalem oku (`go-es` → `do-es`) |
| 8,51–10,11 | Altyazı `Fiile s gelmez.`; `s` 8,99: `goes`'un `es` eki birlikte kırmızı üstü çizilir (`go` + çizili `es`); `gelmez.` 9,23: kartın sağında kırmızı kalem `✗` (SVG); `does` dairesi mürekkebe döner |
| 10,36–12,84 | `He` 10,36: çizili `es` düşer ve solar, `✗` silinir; kart 1 `He doesn't go.` (Fredoka 72) + soluk TR `O gitmez.` (Caveat 52); `go.` 11,16 altında sarı kalem altçizgisi. `Does` 11,96: kart 2 `Does she go?` + soluk TR `O gider mi?` (Caveat 52); `go?` 12,36 altçizgi. Kart karaoke EN parçada |
| 12,84–15,31 | Sahne 03: kural özeti kartı (kâğıt kart, kalem çerçeve 0,4 sn) `Does varsa` / `fiil yalın.` (Fredoka 88), karaoke `Does` 13,39 · `yalın.` 14,75; kart 15,31'de tam |
| 15,31–18,10 | Kart sabit (2,79 sn, standart "≥ 2 sn"). `Bir` 15,46: yer imi simgesi (SVG yol, emoji değil) kalemle ≤ 0,4 sn + `Kaydet` sarı hap; `gönder;` 16,26: kâğıt uçak simgesi (SVG) + `Gönder` (Lexend 700 ≥ 50). İkisi kartın altında, y ≈ 1020–1140. Altyazı karaoke |
| 18,10–20,41 | Sahne 04: `Bu sadece başlangıç.` Fredoka 700 64, y 470–590, sözcük zamanlı (`Bu` 18,65 · `sadece` 18,89 · `başlangıç.` 19,45); öğrenci sesi |
| 20,56 | `Dersin`: ana dersin kapağı 16:9 kart 900×506, x 60–960, y 620–1126 (`ortak/kapak/ana-kapak.png`, koyu temada `ana-kapak-koyu.png`); kalem çerçeve, içi 0,3 sn'de belirir |
| 21,84 | `YDS`: `@ydspublishing` sarı hap, y 1180–1260 |
| 22,96 | `YouTube`: hapın yanında `· YouTube` (Lexend 700) |
| 24,08–25,08 | Durgun kuyruk (son söz + 1,0 sn) |

Altyazı bandı (1400–1550): TR parçalar karaoke; çağrı cümlesi konuşma balonu biçiminde (ses değişimi gözle görünür). Seste
"YeDeSe Publishing", ekranda `@ydspublishing`. Yasak sözler (seste, ekranda, açıklamada): "Tam ders", süre ("dakika"). QR yok, emoji yok,
"izle" düğmesi taklidi yok. Yazı tabanı ≥ 64 (kanal, künye ve altyazı hariç; ikincil satır ve etiket ≥ 50).

## Kapak (`kapak-a.png` = `kapak.png`, 1080×1920)
A: sahne 01'in kanca karesi (t 0,90), altyazı katmanı gizli (S1-KAPAK-A yöntemi: `proje` kopyasında CSS `#altyazi{display:none}`,
`hyperframes snapshot --at <t>`), açık + koyu. B (`06`, `kapak-b.png`): `GOES mu,` / `GO mu?`; kart `He doesn't ____.` / `Does she ____?`
+ iki eş hap `go` · `goes` (dolgusuz) + büyük sarı `?`; figür yok. C (`07`, `kapak-c.png`): `DOES VARSA` / `FİİL YALIN` (hapsız);
kart 1 soluk `He doesn't goes.` (`es` kırmızı üstü çizili + `✗`), kart 2 `He doesn't go.` (`✓`, `go` altında sarı altçizgi); figür yok.
Üçünde de kanal katmanı + künye var, altyazı yok; karakter A'da. Tarif: `uretim-tutanagi/kapak-taslak.md`.

## Hikâye kareleri (`hikaye-a.png` = `hikaye.png`, `hikaye-b.png`; 1080×1920)
Durağan; ses yok; kanal katmanı + künye + kural özeti + `Kaydet` (yer imi simgesi). İçerik y 460–1140; y 1150–1380 boş zemin (bağ
çıkartması elle konur; boş kutu çizilmez); 1400–1920 boş.
A (`05`): etiket `Sınav tuzağı` · kural kartı `Does varsa` / `fiil yalın.` · yanlış satır `He doesn't goes.` (soluk, `es` çizili, `✗`) ·
doğru `He doesn't go.` / `Does she go?` (`✓`) · `Kaydet` hapı.
B (`08`): `Hangisi doğru?` · kök `Does she ____` / `to school?` · şıklar `A) go` / `B) goes` (sarı yok) · kural özeti `Does varsa fiil yalın.`
+ `Kaydet` hapı. Cevap karede yok (doğru: A). Tarif: `uretim-tutanagi/hikaye-taslak.md` §3–§4.

## Çalıştırma
Her sahne `calistir.sh --tema acik` (önizleme: `ONIZLE_YALNIZ=1`); birleştirme `python3 birlestir.py projeler/simple-present-temel-s3 --tema acik
--gecis BookFlip --efekt hisirti` (mp4 takvimi gelince). Durağan kareler ayrı: `sahneler/<klasör>/calistir.sh --tema acik|koyu` → paket kökü PNG.
Ses yeniden kurulumu (sentez yok): `ortak/anlatim/` içinde `sozcuk_uret.py` → `zaman_uret.py` → `kur.py` →
`araclar/ses-paketle.py --yaz --paket simple-present-temel-s3` → `araclar/altyazi_uret.py projeler/simple-present-temel-s3` → `metin_uret.py`.
Sahne istemleri: `uretim-tutanagi/istem/sahne/D-<klasör>.md` (8 istem).
