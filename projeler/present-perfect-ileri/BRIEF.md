# Present Perfect — prototip kalem (YDT ileri, Doğan Hoca anlatımı) · `projeler/present-perfect-ileri`

Çıktı `cikti.mp4` (1920×1080, 30 fps, ≈94 sn) + `kontrol.png`. Anlatım hazır: `ortak/anlatim/anlatim.wav` (soğuk açılış: ilk söz 1,00 sn).
Metin ve zamanlar: `ortak/anlatim/METIN.md`, sözcük zamanları `ortak/anlatim/sozcukler.json` (küresel sn), altyazı parçaları `altyazi.json`.
Kod `ING-YDT-GR-02-06-I`; kimlik `02-06-ydt-ileri`. Yaklaşım: tümdengelim: formül önce, 3 YDT kökü (since+Simple Past, for, ago tuzağı), EN payı ≈ %40, öğrenci yanlış kavramı.
Stil, kalem darbesi, künye ve ses olayları `../present-continuous/BRIEF.md` ile AYNI (aşağıdaki §2, §3, §5–§7 oradan kopyadır);
bu dosyada konuya özel olanlar: §1 sahne tablosu, §4 sahne sözleşmeleri, §3'te künye metinleri.

## 0. Nadir'in istekleri (kaynak: 03–04.11 konuşmaları; hepsi bu videoda görünür olmalı)

| # | İstek | Bu videoda |
|---|---|---|
| 1 | Gerçek YDS Publishing logosu | `ortak/logo/yds-publishing-seffaf.svg` (sarı "yds" + beyaz "publishing"); başka logo YOK |
| 2 | Logodan sonra içerik başlıkları ekranda | Giriş: Hook · Examples · Form listesi |
| 3 | Başlıklar animasyonla şablon köşelerine kayar | Giriş 5,0–6,4 sn uçuş → künye (bkz §3) |
| 4 | Giriş = YouTube kapak biçimi | Sol sütun: rozet hapları + 2 satır büyük başlık (beyaz/sarı, kalın kontur); sağ sütun: kalem eskizi; logo alt sol |
| 5 | İngilizce ders → şablonda Türkçe yok | Künye, etiketler, formül kartı İngilizce. Anlatım ve Türkçe çeviri İÇERİKTİR, serbest |
| 6 | Anlatılan şey hep ekranda; zoom ile kaybolmaz; 4 köşe sabit | Künye kamera dışında, her karede; kamera hareketi yok ya da küçük (≤ %6) |
| 7 | Kalem ile çizme etkisine en yakın çizim; minik çizimler | `cizgi()` kalem darbesi geometrisi (uçta incelme, titrek merkez, ilerleyen dolgu) — bkz §2.3 |
| 8 | Fosforlu kalem belirteçleri (altını çiz, daire, ok) | Konuşulan sözcüğün altında sarı belirteç; have/has + V3 daire; oklar kalemle |
| 9 | Ekran düz kalmasın, öğrenci 3 dk'da sıkılmasın | Her 4 sn içinde en az bir hareket (çizim, belirteç, figür); boş kare yok |
| 10 | Kalem simgesi gerekmez | Ekranda kalem/el YOK; çizgi kendini çizer |
| 11 | Karaoke/altyazı bandı YOK | Sözcük vurgusu yalnız cümlenin kendi üstünde |
| 12 | Öğrenci sorusu (balon) | Sahne 06 ilk 3,4 sn |
| 13 | Ses tasarımı | Olay → Tone.js efekt (kalem hışırtısı, tık, sayfa) — `olaylar.json` |

Kapalı kararlar: DUR kartı yok · video ortasında soru kartı yok · QR bu prototipte yok (adres kararı bekliyor).

## 1. Teknik çerçeve

- `zaman.json`: 6 sahne, `gecis_kare` N = 12. Sahne i yerel kare f ↔ küresel kare `ofs_i + f`, `ofs_i = Σ(kare_j − N)`.
  Sahne sınırı = bir önceki cümlenin bitişi (cümle başı − 0,55): geçiş sessizlik payında olur. Yerel f ↔ küresel saniye `t_bas + f/30`.
  Sahne i>0'ın ilk N karesi ve i<son'un son N karesi geçiş altında (BookFlip / fade) görünür: bu karelerde içerik DURGUN olmalı.
- Kare sayıları zaman.json'daki `kare` ile BİREBİR. İçerik `icerik_kare`'ye kadar biter.
- Zaman yalnız kare numarasından gelir; `Math.random` / `Date` YOK (ornek tohumlu `hash`).
- Çıktı her sahnede: `video.mp4` (libx264 crf 16 yuv420p) + `olaylar.json` + `kontrol.png` + `k/<kare>.png` (en az 3) + `RAPOR.md`.

| Sahne | Klasör | Motor | Kare | Küresel sn | Anlatım |
|---|---|---|---|---|---|
| 1 | 01-hyperframes-giris | HyperFrames | 102 | 0.00–3.00 | cümle 1 (1,00–3,48) |
| 2 | 02-paperjs-kanca | Paper.js | 461 | 3.00–17.97 | cümle 2 |
| 3 | 03-paperjs-ornek1 | Paper.js | 490 | 17.97–33.89 | cümle 3 |
| 4 | 04-canvas-ornek2 | Düz canvas | 533 | 33.89–51.25 | cümle 4 |
| 5 | 05-canvas-ornek3 | Düz canvas | 532 | 51.25–68.60 | cümle 5 |
| 6 | 06-hyperframes-form | HyperFrames | 785 | 68.60–93.77 | cümle 6 (öğrenci) + 7 |

Çip adları (sağ üst): `Hook` · `Rule` · `Exam Q 1 / 3` · `Exam Q 2 / 3` · `Trap 3 / 3` · `Question` → `Rule`. Ajanda (sağ alt): `Hook  Rule  Exam`.
Çizim kaynağı (YALNIZ `ortak/cizim/` içinde VAR olanlar): `coco/` (home, phone, guitar, plane, calendar, clock, music, laptop, book …), `tabler/` (home, phone, plane, calendar, clock, music, book, device-laptop; gitar yalnız coco/guitar.svg), `open-peeps/` (sitting-1,2,4..7 · standing-1..6), `peeps-kit/ogrenci-bas.svg`. Anahtar, banka, grafik simgesi YOK: el çizgisiyle (`cizgi()`) çizilir.

## 2. Görsel dil (stil anayasası — bütün sahneler aynı)

### 2.1 Renk (yalnız bunlar)
**Render varsayılanı AÇIK tema (K19, 04.11)**; koyu kullanıcı seçimidir: `calistir.sh --tema koyu`, `birlestir.py --tema koyu` (`cikti-koyu.mp4`).
Açık palet: zemin `#f7f3ea` · mürekkep `#1b2440` · ikincil `#5a6275` · vurgu `#d9900f` · kırmızı `#d6453a`; logo `yds-publishing-lacivert.svg`. Aşağıdaki hex değerleri KOYU temadır.
zemin `#1b1a17` · mürekkep (krem) `#f3efe6` · ikincil `#c9c2b3` · vurgu sarı `#f2a93b` · logo sarısı `#fece00`
(yalnız logo ve giriş başlığı 2. satır) · kırmızı `#e0473b` (yalnız "Look!" ve "past: was/were" çizgisi).
Zemin: düz + yaşayan gren (opaklık 0,045) + kenar vinyet (0,38). Canvas sahneleri `zeminCiz()` çağırır;
HyperFrames sahneleri aynı görünümü CSS (feTurbulence gren + radial-gradient vinyet) ile verir.

### 2.2 Yazı
| Rol | Yazı tipi | Boy |
|---|---|---|
| İngilizce örnek cümle | Fredoka 700 | 64 px (2 satıra sığmazsa 56) |
| Büyük başlık (giriş) | Fredoka 700 | 150 px, kontur 10 px zemin rengi (`paint-order: stroke fill`) |
| Formül / anahtar sözcük | Fredoka 700 | 60–160 px |
| Türkçe çeviri, el notları, oklar üstü etiket | Caveat 700 | 44–64 px, renk ikincil ya da vurgu |
| Etiket, künye, rozet | Lexend 500/700 | 20–40 px |
Dosyalar: `ortak/font/*.woff2` (+css). Canvas sahneleri `kunyeHazirla()` ile yükler; HyperFrames proje dizinine kopyalar.

### 2.3 Kalem darbesi (çizimlerin tamamı)
Kaynak geometri: `ornek/ucan-makine/sahneler/01-paperjs/sayfa.html` → `cizgi(pts, o)`, `cokgen(c, t)`, `tarama`.
Kurallar: merkez çizgisi 2 frekanslı gürültüyle sapar (amp 1,1) · uçlarda kalınlık kısılır (uc0 16 / uc1 34 px) ·
kalınlık ±%18 titrer · ilerleme t ile kapalı çokgen dolgu (kendini çizen kalem) · her darbe `cizgi` olayı yazar.
Renk krem; figür ve nesne kalınlığı w 3,2–4,0; belirteç (altını çizme, daire, ok) sarı w 6–9, alfa 0,85, hafif
eğik elips/çizgi (mükemmel geometri YASAK). Düz canvas sahneleri aynı geometriyi `ortak/kalem-canvas.js`'e taşır
(A3 yazar: polyline örnekleme + normal sapma + kalınlık → dolgu çokgen; Paper.js'siz).

### 2.4 Figür ve nesne (hazır çizimler, kalemle çizilir)
`ortak/cizim/open-peeps/*.svg` (CC0; sitting-1..7, standing-1..6), `ortak/cizim/tabler/*.svg` (MIT; phone, guitar, plane,
cat, tree, home, calendar, clock, music …). SVG dosyası METİN olarak okunur (fetch + DOMParser); `<path d>` yolları
örneklenir (Paper.js: `new paper.Path(d)` / `importSVG`; canvas: gizli `<svg><path>` `getPointAtLength`) ve `cizgi()`
ile çizilir. `fill="none"` dışı dolgu yolları kontur olur; Peeps'te %2'den kısa yollar atlanır (sade). Bütçe: figür
≤ 60 darbe, nesne ≤ 25 darbe, çizim süresi figür 1,2–2,0 sn, nesne 0,6–1,0 sn. Figürler tam kadraj değil, sahnenin
sağ sütununda (x 1000–1860) ya da BRIEF'in söylediği yerde. Çizim bitince figür durmaz: 6 sn'de bir mikro hareket
(ölçek 1,00→1,012 nefes, ya da nesnede küçük parıltı). Yüz çizgileri korunur.

### 2.5 Metin belirme
İngilizce cümle sözcük sözcük, tam `sozcukler.json` zamanında belirir (soldan maske, 120 ms); konuşulan sözcüğün
altında sarı kalem alt çizgisi kayar (karaoke bandı değil, cümlenin kendi altında). Caveat notlar soldan sağa yazılır
gibi maske ile 0,4–0,6 sn. Formül/anahtar sözcük: ölçek 0,92→1,0 + alfa, 0,35 sn, ease-out cubic.

### 2.6 Hareket kuralları
ease-out cubic giriş · ≤ 4 sn durağanlık · çakışma 0 px (yazı × çizim, yazı × künye) · güvenli alan 56 px ·
künye asla örtülmez · kamera: yok ya da ≤ %6 yavaş kayma · hiçbir öğe sahne bitmeden kaybolmaz (anlatılan şey ekranda kalır),
yalnız yer açmak için küçülüp köşeye toplanır · ses olayı görsel anla aynı kare.

## 3. Künye (HUD) — her sahnede aynı px (sahne 01 uçuşla kurar, 02–06 kare 0'dan sabit)

| Köşe | İçerik | Konum / boy | Renk |
|---|---|---|---|
| Sol üst | `PRESENT PERFECT` + ` · YDT ADVANCED` | x 56, taban y 72; Fredoka 700 30 px; Lexend 500 22 px, 14 px boşluk | krem / ikincil |
| Sağ üst | bölüm adı: `Hook` · `Rule` · `Exam Q 1 / 3` · `Exam Q 2 / 3` · `Trap 3 / 3` · `Question` → `Rule` | sağ kenar x 1864, taban 72; Lexend 700 24 px | vurgu |
| Sol alt | logo svg | x 56, yükseklik 34 px (en ≈ 137), alt kenar y 1036 | logonun kendi renkleri |
| Sağ alt | ajanda `Hook  Rule  Exam`, etkin olan sarı + 4 px nokta solunda | sağ kenar 1864, taban 1030; Lexend 500 20 px, 36 px aralık | ikincil / vurgu |

Canvas: `ortak/kunye.js` → `kunyeHazirla()`, `zeminCiz(ctx, f, K)`, `kunyeCiz(ctx, {bolum, etkin, logo})`.
HyperFrames: aynı sayılar CSS'te; sahne 01'in uçuş hedefleri bu tablodur (bitişte piksel piksel aynı görünmeli).

## 4. Sahne sözleşmeleri (yerel kare = round((t − t_bas) × 30); tablolardaki sn KÜRESEL saniyedir, sahne kodu t_bas çıkarır)

### 01 Giriş — soğuk açılış (HyperFrames, 102 kare, t 0–3,0; cümle 1: 1,00–3,48, son 0,48 sn sahne 02'ye taşar)
Kapak kalıbı; içerik kare 0–90, son 12 kare BookFlip altında durgun.
| sn | Hareket |
|---|---|
| 0,0–0,4 | Logo damgası (110 px, x 96, y ≈ 880): ölçek 1,18→1,0 + dönme −2°→0 |
| 0,3–0,9 | Rozet hapları: `YDT · ADVANCED`, `GRAMMAR` |
| 0,0–2,2 | Başlık kalemle çizilir: `PRESENT` 0,0–1,1, `PERFECT` 1,0–2,2; Fredoka 700 140. Kalem sesi kare 0 |
| 0,2–2,3 | Sağ sütun: uçak (plane) 0,2–1,6, saat (clock) 1,6–2,2 (stroke-dash) |
| 1,0–3,48 | Başlığın altında (x 96, y 650) Caveat 700 64: `Ago varsa Present Perfect yok.` sözcük zamanlı; `Ago` (1,00) kırmızı alt çizgi |
| 2,2–3,0 | UÇUŞ: başlık → sol üst künye; logo → sol alt 34 px; eskiz solar; ajanda belirir |

### 02 Kural (Paper.js, 461 kare, t 3,00–17,97; cümle 2: parçalar 4,03–9,71 · 9,96–15,32 · 15,57–17,97)
| sn | Hareket |
|---|---|
| 3,0–4,0 | Cümle 1 yazısı hazır; `ago` kırmızı alt çizgi kalır (kırmızı: yalnız `ago`, `Simple Past` tuzağı) |
| 4,03–9,71 | Sol el kutusu, 3 madde tik zamanlı: `formula` (4,91) · `since / for` (6,19) · `Simple Past trap` (7,79); küçük saat `6 min` |
| 9,96–15,32 | Formül kartı (el kutusu, orta): `S + have / has + V3` Fredoka 110; EN sözcük sözcük `The formula: subject plus have or has plus past participle.`; `have` (12,28) / `has` (13,12) / `past participle` (13,80) sarı daire; altında Caveat `V3 = past participle` |
| 15,57–17,97 | Üç mini kutu `1 · 2 · 3` (exam roots) teker teker belirir; son 12 kare durgun |

### 03 Kök 1 (Paper.js, 490 kare, t 17,97–33,89; cümle 3; çip `Exam Q 1 / 3`)
| sn | Hareket |
|---|---|
| 18,52–19,3 | Daire içinde `1` |
| 19,65–23,8 | Fredoka 56 (2 satır, en ≤ 1000): `Ever since the company launched its new app, the number of users has doubled.` sözcük sözcük; `since` (20,01) ve `launched` (20,69) sarı daire |
| 20,0–23,5 | Sağ: telefon (phone, 380 px) + yukarı çıkan 3 basamaklı el çizimi sütun grafik (sayı ikiye katlanır) |
| 24,46–29,58 | Caveat 48: TR çeviri (2 satır) |
| 29,73–33,89 | İki kutu + ok: `since + Simple Past` → `Present Perfect (has doubled)`; `launched` ve `has doubled` sarı daire (30,77 / 32,85) |

### 04 Kök 2 (düz canvas, 533 kare, t 33,89–51,25; cümle 4; çip `Exam Q 2 / 3`)
| sn | Hareket |
|---|---|
| 34,44–35,3 | Daire içinde `2` |
| 35,57–39,9 | Fredoka 56: `Selim has worked at this bank for thirty years, so he knows every customer.` sözcük sözcük; `for thirty years` (37,13–37,73) sarı daire |
| 36,0–39,0 | Sağ: oturan figür (sitting-5) + dizüstü (laptop, 360 px) |
| 40,70–45,74 | Caveat 48 TR çeviri; takvim şeridi `30 years` sarı köşeli ayraç, sağ uçta `now` |
| 45,89–51,25 | İki kutu: `for + süre` (47,17) / `since + başlangıç` (50,29), ok `since 1995` Caveat ikincil; `has worked` daire |

### 05 Kök 3 — tuzak (düz canvas, 532 kare, t 51,25–68,60; cümle 5; çip `Trap 3 / 3`; çıkış fade)
| sn | Hareket |
|---|---|
| 51,80–52,6 | Daire içinde `3`; 53,00 Caveat kırmızı `TUZAK` |
| 54,21–58,05 | Fredoka 56: `The plane took off two hours ago, but it hasn't landed yet.` sözcük sözcük; `two hours ago` (55,09–55,65) kırmızı alt çizgi; `hasn't landed yet` (56,61–57,25) sarı daire |
| 54,3–58,0 | Sağ: uçak (plane, 440 px) soldan sağa kalkış eğrisi, yanında saat |
| 58,30–61,5 | Caveat 48 TR çeviri; zaman çizgisi iki bölge: sol `finished`, sağ `unfinished`, ortada `now` |
| 61,65–65,33 | Kırmızı etiket `ago → Simple Past` (took off) |
| 65,48–68,60 | Sarı etiket `yet → Present Perfect` (hasn't landed) |

### 06 Soru + Kural (HyperFrames, 785 kare, t 68,60–93,77; cümle 6 öğrenci, cümle 7 öğretmen)
| sn | Hareket |
|---|---|
| 69,15–73,07 | Künye sağ üst `Question`. Sol: öğrenci BAŞI (`peeps-kit/ogrenci-bas.svg`) + el balonu; Fredoka 600 44: `Hocam, ago varken de has landed diyemez miyiz?` sözcük sözcük; sağda `has landed` üstüne kırmızı çarpı (71,15–71,99) |
| 73,62–78,10 | Künye `Rule`. Balon küçülür; `Hayır.` Caveat; `Bitmiş zaman` sarı bant |
| 78,35–81,47 | Üç kırmızı etiket el kutusunda: `ago` (78,35) · `yesterday` (79,27) · `last year` (80,27) üzerlerinde yasak çizgisi |
| 81,72–86,84 | İki sütun: `Finished → Simple Past` (82,12) / `Unfinished → Present Perfect` (84,68), Fredoka 60 |
| 87,09–92,77 | Kod kartı el kutusunda toplanır: `ago → Simple Past` (kırmızı) / `yet → Present Perfect` (sarı); sağ alt ajandanın üstünde `Next lesson →` |
| 92,77–93,77 | Durgun (1 sn kuyruk) |

## 5. Çalıştırma (her sahne kendi `calistir.sh`; paket kökünden)
- Canvas/Paper.js: `python3 ortak/yakala.py projeler/present-perfect-ileri/sahneler/<klasor>/sayfa.html "$KARE"` →
  log'dan `OLAYLAR` satırı → `olaylar.json`; kare sayısı denetimi; ffmpeg → `video.mp4`; `kontrol.png` (6 kare: 0, %20, %40,
  %60, %80, son−13) + `k/*.png`. Örnek: `ornek/ucan-makine/sahneler/01-paperjs/calistir.sh`. Sayfa `/ortak/surucu.js`'i
  kullanır (Fell/Garamond yükler; bizim fontları `kunyeHazirla()` yükler). Paper.js: `/motorlar/paperjs/node_modules/paper/dist/paper-core.js`.
- HyperFrames: `motorlar/hyperframes/node_modules/.bin/hyperframes render . -o renders/cikti.mp4 --fps 30 --workers 1`;
  örnek `ornek/ucan-makine/sahneler/02-hyperframes/calistir.sh` (+ `olay.py` ile olaylar). gsap `lib/gsap.min.js` kopyası.
- Yük: ağır komut `perl -e 'alarm 480; exec @ARGV' <komut>` ile; aynı anda yalnız KENDİ sahnen; koşudan önce `uptime`
  1 dk yük > 24 ise 60 sn bekle (en çok 5 dk). Değişiklik yokken yeniden koşma (hesaplamadan önce 3 soru).
- Denetim: `kontrol.png` ve `k/*.png` dosyalarını GÖRSEL olarak incele (Read); en az 2 tur (koş → bak → düzelt → koş).
  Bakılacaklar: çakışma, taşma, künye örtülmesi, yazı okunurluğu, zamanlama (sözcük anında belirme).

## 6. Ses olayları (`olaylar.json`: `[{kare, tur, guc}]`, yerel kare)
`cizgi` her kalem darbesi başı (güç 0,4–0,7; uzun darbe 0,7) · `tik` etiket/madde/sözcük grubu belirmesi (0,4–0,6) ·
`vurus` damga, pop, toplanma (0,8–0,9) · `parilti` nota, ışıltı, uçuş (0,5) · `sayfa` birlestir ekler · `hisirti`
istenirse uzun yazı maskesi. Sahne başına 20–80 olay; aynı karede ≤ 3. Birleştirme varsayılanı `--efekt hisirti`: yalnız `cizgi` çalar (04.11 karar).

## 7. Kabul (sahne)
1. `video.mp4` kare sayısı = zaman.json `kare`; ffprobe yuv420p 1920×1080 30 fps.
2. `olaylar.json` geçerli JSON, kare aralığında.
3. kontrol + 3 tam kare: çakışma 0, güvenli alan içinde, künye tam, yazı okunur, renk/yazı tipi §2.
4. Zamanlama: tablo satırları ±3 kare.
5. `RAPOR.md`: yapılan, zamanlama tablosu gerçek kareyle, kontrol anları, olay sayısı, açık sorular, ne çalışmadı.

---
Şef: Claude (Fable), 04.11.2026. Kararlar: `~/01dev/dijital-anlatim/.claude/docs/video-format-kararlari.md`.

## Harita/editör

Kod ortaktır: `ortak/editor/{harita,onizle}.{html,js,css}`, `harita-model.js`, `yol.js`. Proje dizininde yalnız veri kalır.
Sunucu: `node ortak/onizle-sunucu.mjs --port 3012` (sunucu kodu değişince yeniden başlat).

| Sayfa | Adres |
|---|---|
| Harita | `/p/present-perfect-ileri/harita.html?ac=02,02-06,02-06-ydt-ileri&sec=<kimlik>` |
| Editör | `/p/present-perfect-ileri/onizle.html?surum=ana-yatay&t=0&tema=acik&yan=1&yol=02,02-06,02-06-ydt-ileri` |
| API | `/api/present-perfect-ileri/{gorevler,surumler,yorumlar,konum}` |
| Eski adres | `/projeler/present-perfect-ileri/{harita,onizle}.html` → 302, sorgu korunur |
