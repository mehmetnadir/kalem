# RAPOR — 02-04-ydt-temel-dikey · 02-paperjs-kanca (Paper.js, 1080×1920, 529 kare, 3,00–20,22 sn) · 15.11.2026

Tema: koyu

| Konu | Durum |
|---|---|
| Kod | `kalem-paper.js` (575 satır, agy) · `sahne-02.js` (567 satır, agy) · `calistir.sh`, `sayfa.html` (şef) · tasarım `SPEC.md` |
| Kapı | `qa-yerel.sh … 5.6,14.6,20.1 17.8 --hazirla` → **çıkış 0** (hata 0, uyarı 18: yalnız geçici yazı × yazı) |
| Kareler | `k/` (açık 5,6 · 14,6 · 20,1; koyu 17,8) + `k/ek/` (3,6 · 6,7 · 8,2 · 11,9 · 16,3 · 16,85 · 18,4; koyu 20,1) |
| Render | yok (`ONIZLE_YALNIZ=1`); `olaylar.json` / `zamanlar.json` render koşusunda üretilir |
| Tema | açık + koyu (künye `ortak/kunye.js`) |

## Olay listesi (küresel sn → yerel kare)

| sn | kare | Olay | Cümle sözcüğü |
|---|---|---|---|
| 3,00 | 0 | Kare 0 = 01 son düzeni: `İstanbul'da` / `yaşı-yor-um.` (*yor* sarı kutu) / `Amcamla`, Fredoka 128, x 96, taban 560 / 740 / 960; künyede logo + `Hook` | cümle 1 (01'de) |
| 3,40 | 12 | 4. satır `yaşı-yor-um.` taban 1140 (geçiş sonrası ilk kare); 3,60 *yor* kutusu | `yaşıyorum` 3,08 |
| 4,84 / 5,24 | 55 / 67 | sarı `=` üst / alt çizgi, sağ koridor (x 872–972), iki *yor* satırının ortası | `ikisi` / `de` |
| 6,50–6,90 | 105–117 | dört satır üst şeride toplanır (Fredoka 64): satır 1 sağa hizalı (x ≈ 328–1032), satır 2 sola hizalı (x 48–703); *yor* kutuları birlikte küçülür; `=` söner | `yaşıyorum` sonu |
| 6,87 / 6,91–7,55 | 116 / 117–137 | kart A çerçevesi y 600–740; `I live in İstanbul.` Fredoka 72 sağa hizalı, sözcük zamanlı + karaoke (8,50'de söner) | `I live in Istanbul` |
| 8,60 | 168 | bağ oku 1: şerit 1. *yor* → *live* (şerit 2'nin sağından dolanır) | `Biri` |
| 9,08 / 9,40 | 182 / 192 | `SIMPLE` / `PRESENT` Fredoka 64, kart A altı, taban 825, sağa hizalı | `geniş` / `zaman` |
| 10,57 / 10,69–11,73 | 227 / 231–262 | kart B çerçevesi y 880–1020; `I am living with my uncle.` x 88, sözcük zamanlı + karaoke (kuyruklu sözcükte taban + 0,48 em); ok 1 `ikincil`e döner | `I am living with my uncle` |
| 12,86 | 296 | bağ oku 2: şerit 2. *yor* → *am living* (kart A'nın boş sol yarısından geçer) | `Öteki` |
| 13,50 / 13,94 | 315 / 328 | `PRESENT` / `CONTINUOUS` kart B altı, taban 1105, x 88 | `şimdiki` / `zaman` |
| 15,82 | 385 | `vs` etiket A satırının sonunda (`SIMPLE PRESENT vs`) | `iki` |
| 16,07–16,67 | 392–410 | üç parça künyeye uçar: `SIMPLE PRESENT vs` ders satır 1, `PRESENT CONTINUOUS` satır 2 (Fredoka 56, x 48, taban 212 / 276) | `zamanın` 15,98 |
| 16,67–16,97 | 410–419 | rozet `YDT · BASIC` soldan sağa açılır | — |
| 17,26 | 428 | iki uçlu sarı fark oku, sağ kenar x 960, kart A altı ↔ kart B üstü; ok 2 `ikincil` | `farkını` |
| 19,26 / 19,58 | 488 / 497 | `MEANING` Fredoka 140 taban 1310 ortalı; sarı belirteç alt yarıda, 19,58'de biter; fark oku `ikincil` | `anlam` / `belirler` |
| 20,20 | 516 | son 12 kare durgun | — |

Sarı sayımı: her an en çok 3 belirteç (2 *yor* kutusu + o anki tek belirteç); eski oklar `ikincil`e döner (SPEC §B10).

## Kapı sonucu (son satırlar)

```
02-paperjs-kanca | 6.75-6.75 sn | yaşı- × İstanbul'da | kesişim 196x38 px | uyari
02-paperjs-kanca | 16.25-16.25 sn | PRESENT × living | kesişim 110x58 px | uyari
02-paperjs-kanca | 16.50-16.50 sn | CONTINUOUS × yaşı- | kesişim 6x58 px | uyari
== KARE (açık) 5.6 · 14.6 · 20.1   == KARE (koyu) 17.8
kapı çıkış kodu: 0
```
18 uyarının hepsi şeride toplanma (6,75) ve künyeye uçuş (16,25–16,50) anındaki geçici yazı × yazı kesişimidir; hata 0.

## Bakılan kareler ve bulgu

| Kare | Bulgu |
|---|---|
| 5,6 açık | dört satır + iki *yor* kutusu + `=`; HUD yalnız logo + çip; altyazı cümle 1; taşma yok |
| 14,6 açık | şerit iki satır, iki kart, dört etiket; ok 1 `ikincil`, ok 2 sarı; oklar yazıya değmez; HUD'da ders yok |
| 20,1 açık | künyede ders 2 satır + rozet; fark oku ve oklar `ikincil`; MEANING + belirteç; altyazı `belirler.`; platform bandı boş |
| 17,8 koyu | *yor* yazısı (`pilMetin`) turuncu kutuda okunur; fark oku çiziliyor (uçları 18,0'da biter) |
| ek 3,6 · 6,7 · 8,2 · 11,9 | 4. satır yazılıyor; toplanma ortası düzgün; karaoke A `İstanbul.` altında, B `uncle.` altında, kuyruğa değmez |
| ek 16,3 · 16,85 · 18,4 | uçuş ortası (geçici bindirme); rozet açılıyor; fark oku tam, iki uçlu |
| ek koyu 20,1 | MEANING açık yazı + turuncu belirteç okunur |

Taşma, kesik yazı, okunmaz kontrast, boş kare, altyazı bandına giren öğe: yok.

## agy koşuları

| Dosya | Model | Süre | Özet yolu |
|---|---|---|---|
| `kalem-paper.js` (§A) | gemini-3.8-flash-high | 200 sn | `~/.claude/canavar/agy-filo/20261115-120310` |
| `sahne-02.js` (§B) | gemini-3.8-flash-high | 228 sn | `~/.claude/canavar/agy-filo/20261115-120312` |

Şef düzeltmeleri (Edit, 2 satır): karaoke altçizgisi kuyruklu sözcükte 0,48 em (sözleşme 14.11 s11; agy SPEC'in önceki
hâlini okudu) · uçuş matrisi FL0'dan önce `null` değil birim matris (geri sarmada yazı yerine döner).

## Açık noktalar

1. **`=` yorumu.** BRIEF "iki *yor* kutusunu sağdan bağlayan iki kısa çizgi" der. İki *yor* satırı arasında `Amcamla` durduğu
   için `=` sağ koridora, iki satırın ortasına kondu. `Amcamla =` diye okunabilir; Nadir köşeli ayraç (`]` + `=`) isterse
   değişiklik küçüktür.
2. **Zikzak yerleşim.** Şerit satırı 1 + kart A + etiket A sağa, şerit satırı 2 + kart B + etiket B sola hizalı. Sebep: bağ
   oklarının yazının üstünden geçmemesi (sola hizalı şeritte ok 1 şerit 2'yi keser). Ok 2 kart A'nın boş sol yarısından geçer.
3. **Kart B 26 karakter.** BRIEF §3 satır 2 tek satırı açıkça ister (812 px); §2.6'daki ≤ 24 kuralına istisna.
4. **01 sürekliliği.** Sahne 01 henüz yazılmadı; kare 0 BRIEF §3 satır 1 ölçüleriyle kuruldu (*yor* kutusu kalem bandı,
   `pilMetin` yazı). 01'in kutu biçimi farklı çıkarsa BookFlip geçişi farkı örter; yine de 01 bitince karşılaştırılmalı.
5. **Fark oku kısa.** Kartlar tam genişlik (984) ve kart A yazısı sağa dayalı olduğu için ok yalnız kart arası boşlukta
   (124 px). Telefonda ≈ 45 CSS px.
6. **Altyazı dilimi.** 12,9–19 sn arasında dilim, söylenmemiş sözcükleri de gösterir (`ortak/kunye.js` dilimleme; bu sahnenin
   kapsamı dışı).
7. `git status`'ta paketin tamamı izlenmiyor (`??`); commit bu istemin kapsamı dışı.

**W-02-düzelt (15.11):** Ders adı uçuşu kalktı: 5 etiket FL0→FL1 (392→410) yerinde solar, ders adı künyede belirir (opaklık 0→1, 16 px aşağıdan yerine; aynı kareler, rozet FL1'de); künye son hâli sahne 03 ile piksel farkı ≤ 1. 6,75 sn şerit toplanması sıralandı: İstanbul'da 8, Amcamla 9 karede yerleşir; 2. parçalar (yaşı-yor-um ×2, yor kutusu) önce 6 karede yana kayıp küçülür, 12 karede yükselir (`topla` sx/sy, `kucul` fy0/fy1; kalem-paper.js'e yazı `alfa`, künye `dersAlfa/dersDy`).
- Kapı (`cakisma-kapisi.mjs … --sahne 02-paperjs-kanca`): önce 18 uyarı → sonra `çakışma yok (70 örnek, 1951 kutu)`, 0 uyarı; `--sikilik 30` ile `çakışma yok (517 örnek, 14433 kutu)`.
- Bakılan kareler (qa-yerel, açık): 6.75 · 16.0 · 16.25 · 16.5 · 17.0 · 20.1, koyu 16.5 — taşma yok, kesişme yok, künye yerinde (2 satır + rozet).
