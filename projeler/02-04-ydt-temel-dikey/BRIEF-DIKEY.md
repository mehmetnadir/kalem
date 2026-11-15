# 02-04 · Simple Present vs Present Continuous — DİKEY tam ders (9:16, YDT temel) · `projeler/02-04-ydt-temel-dikey`

Nadir 04.11 (ONAYLI): dikey sürüm = yatayla AYNI anlatım ve AYNI ses. Sahne düzeni dikey için SIFIRDAN tasarlanır.
Yatay öğelerin döndürülmüş ya da responsive hâli YASAK. Nadir 15.11: "bu video için burada görünenlerin hepsini istiyorum"
→ dikey tam ders, açık + koyu tema. İzleyici telefondan bakar: 1080 px genişlik ekranda ≈ 390 CSS px olur (ölçek 1/2,77).
Bu BRIEF, yatay `../02-04-ydt-temel/BRIEF.md` üstüne gelir: içerik, senaryo, ses olayları, ekran metni oradan aynen;
görsel dil `../present-continuous/BRIEF.md` (kalem prototipi); yerleşim ve ölçek burada.

## 0. Bulgular — bunlar düzeltilmiş olmalı

Nadir'in dikey bulguları: `../present-continuous-dikey/BRIEF-DIKEY.md` §0 (tek kaynak, 05.11 karar 6b). Özeti: içerik bandı
DOLU (alt yarı boş değil) · logo HUD sol üst 96 px · ders adı 56, rozet 36, çip 40 · içerik yazısı ≥ 64 · figür/nesne 420–560 px
bant ortasında · altyazı bandında konuşulan parça.

Yatay 02-04 raporlarındaki açık noktalar (`../02-04-ydt-temel/sahneler/*/RAPOR.md`). Dikeyde TEKRAR ETME:

| Yatay bulgu (sahne) | Dikey kural |
|---|---|
| Boş kart/bant çerçevesi 9+ sn bekledi (05 sağ kart 12 sn, 11 kart 2 9,5 sn, 12 bant 3 9 sn, 07 başlık satırı 10 sn) | çerçeve içeriğinin ilk sözcüğünden en çok 0,6 sn önce çizilir; boş çerçeve hiçbir yerde 4 sn'den uzun beklemez |
| Figürde işaret pozu yok, ok başından çıktı (06) | ok figürün elinden ya da gövdesinin yanından çıkar; baştan çıkmaz |
| Figür cinsiyeti belirsiz (06, `standing-1`) | öğretmen figürü erkek sesle (K22) uyumlu `open-peeps/standing-*` pozu |
| Ajandada Question/Contrast yok, yanlış bölüm yandı (06, 08, 09) | dikey HUD ajanda çizmez; çip sahnenin kendi bölümünü yazar: `KUNYE.cipler[klasör]` (§2) |
| Açık temada sarı dolgu üstünde zemin rengi yazı okunmadı (13, 02 koyu orta) | sarı dolgu (`vurguDolgu`) üstünde yazı ve tik `pilMetin` (iki temada koyu) |
| Karaoke altçizgisi g/y kuyruğuna değdi (03, 04, 11, 13) | altçizgi taban + 0,28 em; kuyruklu sözcükte kuyruğun altından geçer |
| Son karede 5 sarı altçizgi (11) | aynı anda en çok 3 sarı belirteç; eskisi söner (kaybolmaz, `ikincil` çizgiye döner) |
| 08 ↔ 09 süreklilik ölçülmedi (09 08'i görmeden yazıldı) | 08 ve 09 ortak ölçüleri §3'te sabit; 09 kare 0 = 08 son düzen |
| Sözcük zamanı eksik: `She is wearing her pink T-shirt today.` (cümle 3 parça 4, cümle 9 EN parçası) | yeniden ölçme YOK: 03 yatay `sahne-03.js` `EN2`, 08 yatay `sahne.js` `EN` değerleri kullanılır |
| `ortak/cizim`'de mont, tişört, bavul, tren, bilet yok (03, 05) | tek kaynak yatay sahne kodu: mont/tişört `03-paperjs-ornek1/sahne-03.js` (`MONT`, `TISORT`), bavul `04-canvas-ornek2/sahne.js`, tren/saat/bilet `05-canvas-ornek3/sahne.js`; ev = `tabler/home.svg` |
| QA zamanı "sahne içi" yazılmıştı | `qa-yerel.sh` t = KÜRESEL anlatım saniyesi (istem şablonu düzeltildi) |

## 1. Teknik çerçeve

| Konu | Değer |
|---|---|
| Paket | `K/projeler/02-04-ydt-temel-dikey/` (K = `/home/sef/01dev/_worktrees/kalem-0204`) |
| Zaman | `zaman.json`: 14 sahne, yatayla AYNI `t_bas`/`t_son`/`kare`/`gecis`; 1080×1920, 30 fps, `gecis_kare` 12; 13 → 14 `fade`, 14 geçişsiz |
| Kare ↔ saniye | yerel kare f ↔ küresel `t_bas + f/30`; ilk ve son 12 kare geçiş altında DURGUN |
| Ses | `ortak/anlatim` → `../../02-04-ydt-temel/ortak/anlatim` (aynı ses): `anlatim.m4a`, `cumle-1..18.wav`, `senaryo.json`, `sozcukler.json`, `baslar.json`, `altyazi.json` (47 parça), `METIN.md`. Bu dizine YAZILMAZ |
| Kare yakalama | `K/ortak/yakala.py … 1080 1920` |
| HyperFrames kökü | `data-width="1080" data-height="1920"` |
| Ortak dosyalar | `ortak/kunye.js` (dikey v2 + 02-04 ekleri, §2), `ortak/kalem-canvas.js`, `ortak/tema.sh`, `ortak/tema_damga.py` (simple-present-temel-dikey kopyası); `ortak/{cizim,font,hf_tema.py,logo}` → `../../present-continuous/ortak/` |
| El yazısı (K26) | `../present-continuous-dikey/BRIEF-DIKEY.md` §6; veri `K/ortak/tegaki/caveat-tr/`; dikey ek: boy ≥ 56, sağ uç ≤ 1032 px |
| QA | `cd K && bash araclar/qa-yerel.sh 02-04-ydt-temel-dikey <klasör> <açık t1,t2,t3> <koyu t> --hazirla` (t küresel) |
| Editör | `http://127.0.0.1:3012/p/02-04-ydt-temel-dikey/onizle.html?surum=dikey-tam&tema=acik&t=<sn>` |
| Örnek sahne kodu | `../present-continuous-dikey/sahneler/*` (motor kurulumu, calistir.sh, yakala, olaylar); yerleşim bu BRIEF'ten |

Motor ve klasör adları yatayla aynı kaldı. Dağılım: HyperFrames 7 (01, 06, 07, 10, 12, 13, 14), Paper.js 2 (02, 03),
düz canvas 5 (04, 05, 08, 09, 11). Gerekçe: hiçbir sahnede dikey düzen motor değişikliği istemez; aynı ad editör ve birleştirme
eşlemesini korur.

## 2. Bantlar, HUD ve ortak kurallar (px, 1080×1920)

```
y    0 ┌──────────────────────────────────────┐
       │ [logo 387×96]           [çip 80]      │  logo sol üst (48,48) · çip sağ üst y48 h80 (Lexend 700 40)
       │ SIMPLE PRESENT vs                      │  ders satır 1: Fredoka 700 56, taban y212
       │ PRESENT CONTINUOUS  (YDT · BASIC)      │  ders satır 2: taban y276 · rozet hapı x668 y216 h72 (Lexend 700 36)
  320  ├──────────────────────────────────────┤
       │          İÇERİK 352–1392               │  tek sütun, kenar 48, genişlik 984; kart + çizim + not üst üste
       │      (1040 px, DOLU kullanılır)        │
 1392  ├──────────────────────────────────────┤
 1400  │   ALTYAZI 1400–1536 (≤ 2 satır)        │  konuşulan dilim, Lexend 500 44, satır 56, ortalı, mürekkep
 1536  ├──────────────────────────────────────┤
       │   PLATFORM 1536–1920  BOŞ              │  hiçbir öğe girmez (Shorts/Reels arayüzü)
 1920  └──────────────────────────────────────┘
```

1. **Ders adı 2 satır.** `SIMPLE PRESENT vs PRESENT CONTINUOUS` 56 px'te 1119 px ölçüldü; 984 px'e sığmaz. 56 px kuralı
   küçültmeye izin vermez. Bu yüzden 2 satır: `SIMPLE PRESENT vs` (510 px) / `PRESENT CONTINUOUS` (596 px), satır aralığı 64.
   Rozet `YDT · BASIC` 2. satırın sağında: x = 48 + 596 + 24 = 668. Ölçülen kutular (15.11, başsız tarayıcı): logo 48,48,387,96 ·
   ders 48,156,596,126 · rozet 668,216,281,72 · çip (`Example 1 / 3`) 684,48,348,80. Çakışma yok, HUD 320'de biter.
   Paper.js/canvas sahneleri `kunyeCiz(ctx, {bolum: KUNYE.cipler[klasör], logo})` çağırır; HyperFrames sahneleri aynı sayıları
   CSS ile uygular (logo `<img>`, iki ders satırı, rozet hapı `vurguDolgu` + `pilMetin`, çip `vurgu` çerçeve 4 px).
   `KUNYE.ders` artık dizidir; sahne kodu onu dize gibi kullanmaz.
2. **Ders adı ne zaman görünür.** Ders adı cümle 2'de söylenir. Sahne 01 HUD'da yalnız logo + çip çizer. Ders adı + rozet
   sahne 02'de 15,98'de (`zamanın`) iner (§3 satır 2). 03–14 HUD'u kare 0'dan tam çizer.
3. **Çip metinleri** (`KUNYE.cipler`): 01–02 `Hook` · 03 `Example 1 / 3` · 04 `Example 2 / 3` · 05 `Example 3 / 3` ·
   06 `Question` · 07 `Rule` · 08 `Contrast 1 / 2` · 09 `Contrast 2 / 2` · 10 `Trap` · 11 `Trap · answer` · 12 `Recap` ·
   13 `Mini question` · 14 `Next lesson`. Kaynak: yatay sahnelerin çip metinleri. Yatay ajanda (`Hook · Examples · Rule · Trap`)
   `KUNYE.ajanda`'da kayıtlıdır; dikey HUD onu çizmez.
4. **Altyazı dilimi.** `altyazi.json`'da 13 parça 2 satıra sığmaz (en uzunu 226 karakter, cümle 8). `kunyeHazirla()` uzun parçayı
   `sozcukler.json` sözcük zamanıyla ≤ 2 satırlık (Lexend 500 44, 984 px) dilimlere böler (47 parça → 64 dilim); sözcük sayısı
   tutmazsa (cümle 3 ve 9 TR parçası) zaman karakter oranıyla bulunur. `altyaziCiz(ctx, altyaziMetin(K.altyazi, t))` değişmedi.
   HyperFrames sahneleri aynı kuralı Python'da uygular (kalıp: `../present-continuous-dikey/sahneler/06-hyperframes-form/uret.py`
   `altyazi_dilimleri()`; genişlik 984, boy 44, en çok 2 satır). Altyazı sessiz izleme içindir; her sahnede zorunlu.
5. **Çift kart kuralı.** Çok satırlı örnek kartı ve büyük çizim varsa ekranda en çok 1 örnek kartı tam boydadır. İkinci kart
   gelince birinci kart üst şeride (y 352–472) küçülür: tek satır özet (anahtar fiil → etiket, Fredoka 64 / Caveat 64) + çizimin
   ≥ 96 px simgesi. Kart kaybolmaz. İstisna: tek satırlık karşıt çift (02 kanca, 11 tuzak cevabı) iki satır kartı üst üste durur;
   orada büyük çizim yok, yer yeter.
6. **Kart.** Genişlik 984 (x 48–1032), kenar 4 px kalem çizgisi, iç boşluk 40. İngilizce cümle Fredoka 700 72 (satır 86); satır
   ≤ 24 karakterde sözcük sınırından kırılır; 3 satıra sığmazsa 64. Türkçe çeviri Caveat 700 64, `murekkep`.
7. **Zaman çizgisi** (04, 05, 08, 09, 11): eksen x 96–984, sağ ok; bant `vurguDolgu` %45 + iki uç çentiği; now noktası `vurgu`,
   nabız; etiketler Caveat 64. `→` ve `≠` el yazısı glif setinde yok: kalemle çizilir.
8. **Öğrenci** (06, 10, 11, 13): `ortak/cizim/peeps-kit/ogrenci-bas.svg`, baş 160 px; balon metni Caveat 64, ≤ 24 karakter/satır,
   sözcük sözcük. Soru anından sonra 0,75 sn duraklama olaysız; cevap 2 sn içinde başlar.
9. **Renk.** Tek vurgu sarı (`vurgu` / `vurguDolgu`, temaya göre). Kırmızı yok, emoji yok. Doğru şık (13) vurgu dolgusu +
   `pilMetin` tik; ham yeşil yok (yatay BRIEF §3, 13.11 QA).
10. **Hareket.** ease-out; ≤ 4 sn durağanlık; çakışma 0 px; yer açmak için öğe yukarı toplanır ve küçülür, küçülünce de ≥ 48 px
    kalır. Bandın ≥ %85'i sahne bitiminde dolu. y değerleri §3'te yaklaşıktır; ölçek kuralı (§2.6, `present-continuous-dikey` §3)
    önceliklidir.

Ölçek tablosu: `../present-continuous-dikey/BRIEF-DIKEY.md` §3 (İngilizce cümle 72 · çeviri/kanca Caveat 64–80 · el notu Caveat 64 ·
formül 110–160 · figür/nesne 420–560 px, kalınlık 4,0–4,8 · belirteç w 9–12). Satır ≤ 24 karakter. Güvenli alan: kenar 48.

## 3. Sahne planı (küresel sn; içerik ve olay sırası yatay BRIEF §3 + raporlar; yerleşim dikey)

| No | Klasör | Motor | Küresel sn | Kare | Dikeyde ekranda NE var (içerik bandı 352–1392, üstten alta; altyazı alt bantta) |
|---|---|---|---|---|---|
| 1 | `01-hyperframes-giris` | HyperFrames | 0,00–3,00 | 102 | Soğuk açılış, cümle 1 başı. 0,00–0,40 logo damgası bant ortasında, 0,50–0,95 HUD sol üste (387×96) uçar; çip `Hook` 0,70–0,95. Ders adı ve rozet bu sahnede YOK (02'de iner). Türkçe satırlar Fredoka 700 128, sola hizalı x 96, sözcük sözcük (`kinetik_baslik`): `İstanbul'da` taban y 560 (1,00) → `yaşıyorum.` taban y 740 (1,64, bitişik) → `ek_ayir`: *yor* sarı kutuyla kayar 1,94–2,30, yazı 2,14'te `pilMetin`, tireler 2,22 → `yaşı-yor-um.` (740 px) → `Amcamla` taban y 960 (2,52). Arkasındaki `yaşıyorum` 3,08'de söylenir: 4. satır yuvası (y 1140) boş kalır, sahne 02 çizer. Hareket 2,74'te biter; son 12 kare geçiş altında durgun. Altyazı: cümle 1 |
| 2 | `02-paperjs-kanca` | Paper.js | 3,00–20,22 | 529 | Kare 0 = 01 son düzeni. 3,08 `yaşı-yor-um.` 4. satır (taban y 1140) + 2. *yor* sarı kutu. 4,84 / 5,24 sarı kalem `=`: iki *yor* kutusunu sağdan bağlayan iki kısa çizgi. 6,50'de dört satır üst şeride toplanır (y 352–560, Fredoka 64: `İstanbul'da yaşı-yor-um.` / `Amcamla yaşı-yor-um.`, *yor* kutuları kalır). Kanca çifti (tek satırlık, §2.5 istisna): kart A y 600–740 `I live in İstanbul.` Fredoka 72 sözcük zamanlı (6,91), karaoke altı; 8,60 `bag` oku üst şeritteki 1. *yor* → *live*; etiket `SIMPLE` (9,08) `PRESENT` (9,40) Fredoka 64 kart altında y 770–840. Kart B y 880–1020 `I am living with my uncle.` (10,69, 812 px tek satır); 12,86 `bag` 2. *yor* → *am living*; `PRESENT` (13,50) `CONTINUOUS` (13,94) y 1050–1120. 15,82 `vs` iki etiket arasında. 15,98 (`zamanın`) üç parça HUD'a uçar: `SIMPLE PRESENT vs` ders satır 1, `PRESENT CONTINUOUS` satır 2; iniş bitince rozet açılır (≈ 16,7). 17,26 sağ kenarda iki uçlu sarı fark oku (kart A ↔ kart B). 19,26 `MEANING` Fredoka 140 y 1180–1340 + 19,58'de biten sarı belirteç (yazının alt yarısı). Altyazı: cümle 1 sonu, cümle 2 dilimleri |
| 3 | `03-paperjs-ornek1` | Paper.js | 20,22–43,85 | 721 | Çip `Example 1 / 3`. Kart A çerçevesi 20,77 (`Birinci`), y 380–720: `She wears her coat / in the winter.` Fredoka 72 sözcük zamanlı 24,22–25,78, karaoke altı; TR `Kışın montunu giyer.` Caveat 64 el yazısı 26,79 (kart içinde, y ≈ 680). Mont çizimi (yatay `MONT`) y 750–1190, 440 px, 25,02 (`coat`). 28,55 `odak` *in the winter*. `GENERAL` Caveat 80 el yazısı 30,31, y 1230–1320; altı 31,35. 32,41'de çift kart kuralı: kart A + mont üst şeride (`wears → GENERAL` + mont simgesi). Kart B y 490–830: `She is wearing her / pink T-shirt today.` sözcük zamanı yatay `EN2` (32,41–34,13); TR `Bugün pembe tişörtünü giyiyor.` Caveat 64 (35,37, 665 px). Tişört (yatay `TISORT`) y 860–1260, 400–420 px, 33,63. 38,17 `odak` *today*. `RIGHT NOW` Caveat 80 39,05, y 1280–1370; altı 41,45. 42,81 *is* altı, 43,05 *-ing* altı. Altyazı: cümle 3 dilimleri |
| 4 | `04-canvas-ornek2` | Düz canvas | 43,85–68,84 | 762 | Çip `Example 2 / 3`. 44,40 daire içinde 2 (sol üst köşe, 96 px). `live` Fredoka 140 pop 47,20 (y 380–520) + sarı altı 47,55. Kart A çerçevesi 47,70, y 540–770: `I live in İstanbul / with my family.` 72, sözcük zamanlı 48,09–49,61. Ev (`tabler/home.svg`) y 790–1210, 420 px, 50,82 (`Ailemle`). Zaman çizgisi A y 1230–1390: eksen 52,90, now 53,15 + `now`, uzun bant 53,30 (`hep`), `PERMANENT` Caveat 72 bandın üstünde 54,58. 55,54 `odak` *live*. 56,64'te çift kart kuralı: şerit `live → PERMANENT` + ev simgesi. Kart B y 490–830: `My parents are out of / town, so I am living / with my uncle.` 72 (3 satır), sözcük zamanlı 56,99–59,95. Bavul (yatay `sahne.js` çizimi) y 845–1265, 62,28. Zaman çizgisi B y 1270–1390: eksen 65,00, now 65,25, kısa bant 65,60–66,12 (uç çizgileri 66,00 / 66,12), `TEMPORARY` 66,84. 67,88 `odak` *am living*. Türkçe çeviri yok (yatayda yok). Altyazı: cümle 4 dilimleri |
| 5 | `05-canvas-ornek3` | Düz canvas | 68,84–93,35 | 747 | Çip `Example 3 / 3`. Zaman çizgisi sahne boyunca altta kalır, y 1230–1390: eksen + now + nabız 71,55 (`geleceği`), gelecek yarısı dolgu 72,03. Kart A çerçevesi 72,60, y 380–620: `The train to İzmir / leaves at 7 pm today.` 72, sözcük zamanlı 73,00'dan. Tren y 640–1060 (420 px) 73,16; saat (akrep 7, vurgu) trenin sağında 74,76. 77,81 zaman çizgisinde 7 pm çentiği + nokta + etiket; 78,53 now → 7 pm kalem yayı. `TIMETABLE` Caveat 72 el yazısı 80,37, y 1080–1160; altı 81,93. 83,17 `odak` *leaves*. 84,60'ta çift kart kuralı: şerit `leaves → TIMETABLE` + tren simgesi (sağ kart 12 sn boş beklemez). Kart B y 490–730: `I am going to the / movie theater tonight.` sözcük zamanlı 84,94'ten. Bilet y 750–1150, 85,82. 87,75 tonight çentiği + etiket; 88,63 now → tonight yayı. `ARRANGEMENT` 89,63, y 1160–1220; altı 91,07. 92,43 `odak` *am going*. Altyazı: cümle 5 dilimleri |
| 6 | `06-hyperframes-soru1` | HyperFrames | 93,35–113,37 | 613 | Çip `Question`. Kare 0: 05'in iki cümlesi üst şeritte, y 352–500, Fredoka 64 iki satır: `The train … leaves at 7 pm today.` · `I am going … tonight.`; *leaves* ve *am going* sarı altlı. SORU ANI 1: öğrenci başı + balon y 540–960, `Hocam, tren de plana / göre kalkmıyor mu? / Neden -ing yok?` sözcük sözcük 93,90–97,66; 94,62 (`tren`) sarı nokta balon → *leaves*; 96,98 *-ing* altı. 97,66–98,41 olaysız duraklama. 98,41 balon söner, baş küçülüp alt sağa iner (x 870–1030, y 1230–1390). Cevap 1 y 520–950: öğretmen figürü (`open-peeps/standing-*`, erkek, 420 px) solda, 99,05; sağında Caveat 64 zincir `person` (99,05) `↳ plan` (99,33) `↳ am / is / are + V-ing` (101,45); 100,17 sarı ok figürün elinden/yanından *am going*'e. Cevap 2 y 970–1390: tren (yatay çizimi) 102,57 + `train` / `↳ timetable` (103,93) / `↳ V1 / V-s` (106,89); 104,49 sarı ok tren → *leaves*; 104,95 öğrenci 1 sn baş sallar; 105,21 TIMETABLE nabzı (şeritte). 109,53 *The train* altı; 111,49 tren nabzı; 112,21 uçak (`tabler/plane.svg`), 112,97 kitap (`tabler/book.svg`) trenin yanında, 140 px. Altyazı: cümle 6 (öğrenci) + cümle 7 dilimleri |
| 7 | `07-hyperframes-kural` | HyperFrames | 113,37–130,40 | 523 | Çip `Rule`. Kural tablosu tek sütunda bir öğe; satırlar 2 hücreli (sol/sağ, ayraç x 540), çünkü anlatım "soldakiler / sağdakiler" der. Boş başlık satırı ve boş tablo YOK: her satır söylenince çizilir. Satır 1 y 380–560: [mont] `general` (117,44) ‖ `right now` [tişört] (118,24). Satır 2 y 570–750: [ev] `permanent` (119,44) ‖ `temporary` [bavul] (120,48). Satır 3 y 760–940: [tren] `timetable` (121,52) + `(future)` (122,04) ‖ `arrangement` (122,80) + `(future)` (123,44) [bilet]. Terimler Caveat 64; simgeler 120–140 px (03–05 çizimleri); hücre → simge kısa kalem çizgisi. Ad satırı y 960–1250: sol `SIMPLE / PRESENT` Fredoka 64 (124,32) + `V1 / V-s` (124,96); sağ `PRESENT / CONTINUOUS` (126,00) + `am / is / are` / `+ V-ing` (126,72). Alt y 1270–1390: `MEANING` (128,08) `FIRST` (128,56) Fredoka 110 kinetik; 129,52 (`anlamına`) sarı belirteç. Altyazı: cümle 8 dilimleri |
| 8 | `08-canvas-karsit1` | Düz canvas | 130,40–145,29 | 459 | Çip `Contrast 1 / 2`. 08–09 ORTAK ÖLÇÜLER: kart y 490–760 · not satırı y 790–880 · zaman çizgisi ekseni y 1180 (x 96–984) · today bandı x 200–880, y 1040–1180 · now x 360 · `now` etiketi y 1240. 134,95 (`today.`) `today` Caveat 80 notu y 380–470 + kart çerçevesi (kart 130,95'te çizilmez: 4,7 sn boş kalırdı). Kart: `She is wearing her / pink T-shirt today.` 72, sözcük zamanı yatay 08 `EN` (135,61–137,69); kartın sağ iç köşesinde tişört simgesi 220 px, 136,87. 138,57 eksen. 139,21 / 139,29 çoklu `odak`: *today* kartta + notta. 139,93 today gün bandı + çentikler; 140,05 ok; `this day only` Caveat 72 not satırında 140,29–140,89 (`today → this day only`). 141,77 tişört çevresine sarı halka. 142,57 now noktası + nabız; 143,05 `now`. 144,37 `odak` *is wearing*. Altyazı: cümle 9 dilimleri |
| 9 | `09-canvas-karsit2` | Düz canvas | 145,29–162,33 | 523 | Çip `Contrast 2 / 2`. Kare 0 = 08 son düzeni (ortak ölçüler §3 satır 8). 145,72'de 08 kartı + notu üst şeride küçülür (y 352–470: `is wearing … today → this day only` + tişört simgesi); bant, now ve `now` yerinde kalır. Kart y 490–760: `The train to İzmir / leaves at 7 pm today.` 72, sözcük zamanlı 145,84–148,80; kartın sağ iç köşesinde tren simgesi 146,00. 149,69 not `today`; 150,57 `odak` *7 pm* (dar öbek → `alti`); 151,05 not `+ 7 pm`; 151,85 zaman çizgisinde 7 pm çentiği + nokta (x 780, today bandının içinde); 152,25 `7 pm` etiketi; 153,45 now → 7 pm kalem yayı; 154,93 not oku + `timetable` (not satırı: `today + 7 pm → timetable`). 156,09 `odak` *leaves*. 157,21 çoklu `odak`: iki *today* (şerit + kart). Alt y 1290–1390: 159,05 `≠` (kalem, 3 darbe, x ≈ 570); 160,57 `RIGHT NOW` Caveat 64 now altında; 161,61 `TIMETABLE` 7 pm altında. Altyazı: cümle 10 dilimleri |
| 10 | `10-hyperframes-tuzak` | HyperFrames | 162,33–183,79 | 656 | Çip `Trap`. 162,88 (`Tuzak.`) `TRAP` Fredoka 96 etiketi + tam genişlik kart, `yaklas` (0,93 → 1); kart önce bant ortasında (y 600–1040). 163,84 `TR` etiketi. EN `I live in İstanbul / with my family.` 72 sözcük sözcük 166,09–167,83. TR `Ailemle İstanbul'da / yaşıyorum.` Fredoka 600 72 (168,66 / 169,54, bitişik); 171,30 `ek_ayir` *yor* sarı kutu → `yaşı-yor-um.` (01 kalıbı ve QA payları). 172,74 `bag` *yor* → *live* (dikey kol, ok ucu *live*'da); 174,26 yanında sarı `?`; 176,26 *live* sarı fosfor (yazı `pilMetin`). 177,40'ta kart yukarı toplanır (y 380–820). SORU ANI 2 (177,65): öğrenci başı + balon y 860–1380, `Hocam, Türkçesi / yaşıyorum. I am living / in İstanbul olmaz mı?` Caveat 64 sözcük sözcük 177,85–183,64; 179,37 sarı nokta balon → *yor*; 181,36 *living* sarı altı. Duraklama ve cevap sahne 11'de. Altyazı: cümle 11 dilimleri + cümle 12 (öğrenci) |
| 11 | `11-canvas-tuzak-cevap` | Düz canvas | 183,79–205,30 | 657 | Çip `Trap · answer`. Tek satırlık karşıt çift (§2.5 istisna). 184,20 öğrenci başı alt sağda (x 870–1030, y 1220–1380). Kart 1 çerçevesi 184,54, y 380–500. 185,90 `≠` sarı kalem + 186,22–186,82 `meaning` el yazısı, orta satırda y 720–850 (çarpı yok; iki cümle de doğru). Kart 1: `I am living in İstanbul.` 72 sözcük zamanlı 187,11–188,95; not `→ for now (temporary)` Caveat 64 y 520–590 (189,12; `(temporary)` 191,55–192,30); zaman çizgisi 1 y 600–700: eksen 189,68, now 190,00, kısa bant 190,24. Kart 2 çerçevesi 192,48 (`Ailenle`; 185,42'de çizilmez), y 880–1000; zaman çizgisi 2 y 1100–1200: eksen 192,48, now 192,90 (now x iki çizgide aynı), uzun bant 193,36–194,21; not `→ always (permanent)` y 1020–1090 (193,12; `(permanent)` 193,95). Kart 2 cümlesi `I live in İstanbul.` 194,89–196,65. 197,70 / 197,78 çoklu `odak` *am living* + *live*; 201,30 *meaning* altı ve fiil altları `ikincil`e döner (en çok 3 sarı); 202,30–203,30 öğrenci 1 sn baş sallar; 202,74 `(permanent)` altı; 203,46 `(temporary)` altı. Altyazı: cümle 13 dilimleri |
| 12 | `12-hyperframes-ozet` | HyperFrames | 205,30–220,33 | 463 | Çip `Recap`. Perde yok. Üç madde bloğu üst üste; her blok sözü gelince çizilir (soluk boş bant YOK). Blok 1 y 380–680: `general · permanent ·` / `timetable` Caveat 64, terim söylenince belirteçle (206,89 / 207,85 / 208,89); altında mont, ev, tren simgeleri 110 px (207,29 / 208,05 / 209,09); 210,17 kalem oku + hap `V1 / V-s` (Fredoka 64, `vurguDolgu` + `pilMetin`). Blok 2 y 700–1000: `right now · temporary ·` / `arrangement` (211,29 / 212,41 / 213,37); tişört, bavul, bilet (211,77 / 212,61 / 213,57); 214,77 hap `am / is / are + V-ing`. Blok 3 y 1020–1240: `time word · Turkish -yor` (216,01 / 217,21) → hap `clue` (217,93); `MEANING` (219,45) → hap `decision` (219,85). Alt y 1260–1390: `MEANING FIRST` Fredoka 96 + sarı belirteç (218,97–219,45; 07 belirtecinin dönüşü). 219,87–220,29 geçiş çizgisi. Altyazı: cümle 14 dilimleri |
| 13 | `13-hyperframes-mini-soru` | HyperFrames | 220,33–251,27 | 940 | Çip `Mini question`. 220,88 soru kartı + `MINI QUESTION` (Lexend 700 56), kart y 380–700. Kök `My brother lives in / Ankara, but this month / he ____ with us.` Fredoka 72 sözcük sözcük 221,93'ten; 224,71 boşluk çizgisi (susma anında); 227,40 boşluk vurgu çizgisi. 229,33 (`Beş`) sayaç halkası + 5 kartın sağ üst köşesinde; şıklar y 730–1170, 0,18 sn arayla, Fredoka 64: `A) lives` · `B) is living` · `C) live` · `D) to live` · `E) are living` (ses şıkları okumaz, D-0205). Öğrenci başı + balon y 1190–1390, `Bence A şıkkı. / Yaşamak kalıcı bir durum.` Caveat 64 (230,58'den); 231,40 A soluk sarı çerçeve. 235,03 balon söner (baş kalır); 235,13 `odak` *lives in Ankara*; 238,55 `odak` *this month*; 241,43 A pili `this month → temporary`, A soluklaşır. 243,43 doğru B: `vurguDolgu` + `pilMetin` yazı, 243,63 `pilMetin` tik (ham yeşil yok; istem şablonundaki "doğru şık yeşil" bu sahnede uygulanmaz). 244,95 boşluğa *is living* (g kuyruğu çizgiye değmez). 246,07 / 246,95 C, E imleci; 247,67 / 248,15 pilleri `he ↔ live`, `he ↔ are`; 249,11 D imleci, 249,83 pili `to live: no tense`. Piller şık satırının sağında (x ≥ 420). Çıkış fade; son 12 kare durgun. Altyazı: cümle 15, 16 (öğrenci), 17 dilimleri |
| 14 | `14-hyperframes-kapanis` | HyperFrames | 251,27–264,64 | 431 | Çip `Next lesson`. `MEANING` (251,82) `FIRST` (252,14) Fredoka 120 kinetik, y 400–540; 252,62 sarı altı. 253,58 numara halkaları 1 · 2 · 3 (0,12 sn arayla). Üç soru satırı Caveat 88, sola hizalı, y 600–1060 (satır 150): `general or now?` (254,78 / 255,18 / 255,66) · `permanent or temporary?` (256,54 / 257,02 / 257,42) · `timetable or plan?` (258,30 / 258,86 / 259,26); her parça söylenince yazılır, `or` `ikincil`. Sonraki ders kartı y 1100–1380: el kutusu 260,30, `Next lesson` Lexend 500 56 `ikincil` (260,70), `Stative Verbs` Fredoka 96 (261,18 / 262,06), sarı ok 262,50. Kare 401'den sonrası durgun son düzen; geçiş yok. Altyazı: cümle 18 dilimleri |

## 4. Çalıştırma ve kabul (sahne başına)

1. Sahne istemi: `uretim-tutanagi/istem/sahne/D-<klasör>.md` (şablon `uretim-tutanagi/istem/D-dikey-sablon.md`).
2. Sahne klasörü örnekle aynı dosya düzeni (`calistir.sh` → `. "$D/../../ortak/tema.sh" "$@"`, `KAREYI_TUT`, yük bekçisi,
   `RAPOR.md`, `olaylar.json`). Yol sabitleri `/projeler/02-04-ydt-temel-dikey/...`. Render YOK; önizleme `ONIZLE_YALNIZ=1`.
3. Kapı: `qa-yerel.sh` çıkış 0 + kareler ajanın kendi gözüyle (taşma, kesik yazı, üst üste binme, kontrast, boş kare, alt bant).
   Ölçüt: HUD okunur, içerik bandı dolu, ≥ 64 px içerik yazısı, figür/nesne ≥ 420 px, altyazı bandında metin, platform bandı boş.
4. RAPOR.md: olay listesi, kapı sonucu, bakılan kareler, açık noktalar.

---
Son Güncelleme: 15.11.2026 — P1-dikey (iskelet + BRIEF + 14 sahne istemi). Rapor: `uretim-tutanagi/P1-DIKEY-RAPOR.md`.
