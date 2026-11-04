# Simple Present — paket 05.11 "kalem" (YDT temel, Doğan Hoca anlatımı)

Amaç: Nadir'in konuşmalar boyunca istediği görsel dili kalem motorlarıyla GÖSTERMEK. Çıktı `cikti.mp4` (1920×1080, 30 fps, ≈90 sn) + `kontrol.png`. Anlatım hazır: `ortak/anlatim/anlatim.wav` (soğuk açılış: ilk söz 1,00 sn).
(1920×1080, 30 fps, ≈88 sn) + `kontrol.png`. Anlatım hazır: `ortak/anlatim/anlatim.wav` (soğuk açılış: ilk söz 1,00 sn).
Metin ve zamanlar: `ortak/anlatim/METIN.md`, sözcük zamanları `ortak/anlatim/sozcukler.json` (küresel sn).

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
| 8 | Fosforlu kalem belirteçleri (altını çiz, daire, ok) | Konuşulan sözcüğün altında sarı belirteç; am/is + -ing daire; oklar kalemle |
| 9 | Ekran düz kalmasın, öğrenci 3 dk'da sıkılmasın | Her 4 sn içinde en az bir hareket (çizim, belirteç, figür); boş kare yok |
| 10 | Kalem simgesi gerekmez | Ekranda kalem/el YOK; çizgi kendini çizer |
| 11 | Karaoke/altyazı bandı YOK | Sözcük vurgusu yalnız cümlenin kendi üstünde |
| 12 | Öğrenci sorusu (balon) | Sahne 06 başı (cümle 6) |
| 13 | Ses tasarımı | Olay → Tone.js efekt (kalem hışırtısı, tık, sayfa) — `olaylar.json` |

Kapalı kararlar: DUR kartı yok · video ortasında soru kartı yok · QR bu prototipte yok (adres kararı bekliyor).

## 1. Teknik çerçeve

- `zaman.json`: 6 sahne, `gecis_kare` N = 12. Sahne i yerel kare f ↔ küresel kare `ofs_i + f`, `ofs_i = Σ(kare_j − N)`; yerel f ↔ küresel saniye `t_bas + f/30`. Sahne sınırı = sonraki cümle başı − 0,55 (yani önceki cümlenin bitişi; geçiş sessizlikte olur). İlk/son N kare geçiş altında: içerik DURGUN.
- Kare sayıları zaman.json `kare` ile BİREBİR. İçerik `icerik_kare`'ye kadar biter.
- Zaman yalnız kare numarasından gelir; `Math.random` / `Date` YOK.
- Çıktı her sahnede: `video.mp4` (libx264 crf 16 yuv420p) + `olaylar.json` + `kontrol.png` + `k/<kare>.png` + `RAPOR.md`.
- Metin ve zamanlar: `ortak/anlatim/METIN.md`; sözcük zamanları `sozcukler.json`; altyazı parçaları `altyazi.json`.

| Sahne | Klasör | Motor | Kare | Küresel sn | Anlatım |
|---|---|---|---|---|---|
| 1 | 01-hyperframes-giris | HyperFrames | 102 | 0,00–3,00 | cümle 1 (1.00–3.00) |
| 2 | 02-paperjs-kanca | Paper.js | 451 | 3,00–17,65 | cümle 2 |
| 3 | 03-paperjs-ornek1 | Paper.js | 456 | 17,65–32,45 | cümle 3 |
| 4 | 04-canvas-ornek2 | düz canvas | 487 | 32,45–48,29 | cümle 4 |
| 5 | 05-canvas-ornek3 | düz canvas | 406 | 48,29–61,41 | cümle 5 |
| 6 | 06-hyperframes-form | HyperFrames | 901 | 61,41–90,43 | cümle 6 (öğrenci) + 7 |

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
`ortak/cizim/open-peeps/*.svg` (CC0; sitting-1..7, standing-1..6), `ortak/cizim/tabler/*.svg` (MIT; camera, piano,
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
| Sol üst | `SIMPLE PRESENT` + ` · YDT ADVANCED` | x 56, taban y 72; Fredoka 700 30 px; Lexend 500 22 px, 14 px boşluk | krem / ikincil |
| Sağ üst | bölüm adı: `Hook` · `Example 1 / 3` · `Example 2 / 3` · `Example 3 / 3` · `Question` → `Form` | sağ kenar x 1864, taban 72; Lexend 700 24 px | vurgu |
| Sol alt | logo svg | x 56, yükseklik 34 px (en ≈ 137), alt kenar y 1036 | logonun kendi renkleri |
| Sağ alt | ajanda `Hook  Examples  Form`, etkin olan sarı + 4 px nokta solunda | sağ kenar 1864, taban 1030; Lexend 500 20 px, 36 px aralık | ikincil / vurgu |

Canvas: `ortak/kunye.js` → `kunyeHazirla()`, `zeminCiz(ctx, f, K)`, `kunyeCiz(ctx, {bolum, etkin, logo})`.
HyperFrames: aynı sayılar CSS'te; sahne 01'in uçuş hedefleri bu tablodur (bitişte piksel piksel aynı görünmeli).

## 4. Sahne sözleşmeleri (küresel saniye; yerel kare = round((t − t_bas) × 30); satır zamanı sözcük başlangıcından)

### 01 Giriş — soğuk açılış (HyperFrames, 102 kare, t 0,00–3,00; kapak kalıbı, cümle 1 burada konuşulur)
| küresel sn | Hareket |
|---|---|
| 0,00–0,40 | Logo damgası sol sütun altında (110 px, x 96, y ≈ 880): ölçek 1,18→1,0 + dönme −2°→0 |
| 0,30–0,90 | Rozet hapları: `YDT · ADVANCED`, `GRAMMAR` |
| 0,00–2,20 | Başlık kalemle çizilir: `SIMPLE` 0,0–1,1, `PRESENT` 1,0–2,2; Fredoka 700 140 |
| 0,20–2,30 | Sağ sütun: ayakta figür `open-peeps/standing-3.svg`, uçak `coco/plane.svg` 1,6–2,2 |
| 1,00–3,00 | Caveat 700 64: `Uçak yarın dokuzda kalkıyor.` sözcük sözcük; `kalkıyor` sarı daire |
| 2,20–3,00 | UÇUŞ: başlık → sol üst künye; logo → sol alt; eskiz solar; ajanda belirir |

### 02 Kanca (Paper.js, 451 kare, t 3,00–17,65)
| küresel sn | Hareket |
|---|---|
| 3,00–7,24 | Cümle 1 yazısı hazır. Caveat `?` büyük, sarı; altında iki kutu `will` ve `Simple Present` (el çizimi, soru işareti arası) |
| 7,24–10,60 | Kural satırı Fredoka 56: `he · she · it  →  V-s` (`takes` 9,16'de sarı) |
| 10,60–13,97 | İkinci satır: `does + base verb` (olumsuz + soru); `does` sarı daire (12,28) |
| 13,97–17,65 | Alt sağ kutu 3 madde tik: `form` · `time expressions` · `3 YDT roots` (16,05); küçük saat `6 min` |

### 03 Örnek 1 (Paper.js, 456 kare, t 17,65–32,45)
| küresel sn | Hareket |
|---|---|
| 18,20–19,41 | Daire içinde `1` |
| 19,41–23,17 | Fredoka 56 (3 satır): `Although the sun looks small from here, it gives plants the energy they need.` sözcük sözcük; `Although` kırmızı değil, mürekkep; `gives` sarı alt çizgi |
| 19,41–23,77 | Sağ: güneş `coco/sun.svg` (360 px) + ağaç `coco/tree.svg` (360 px) kalemle |
| 24,30–27,34 | Caveat 48: `Güneş küçük görünse de bitkilere gereken enerjiyi verir.` |
| 28,93–32,45 | `Although` kutuya alınır; ok `zaman değişmez` → `gives` sarı daire; formül `it gives` (V-s) |

### 04 Örnek 2 (düz canvas, 487 kare, t 32,45–48,29)
| küresel sn | Hareket |
|---|---|
| 33,00–34,13 | Daire içinde `2` |
| 34,13–39,17 | Fredoka 56 (3 satır): `Mike owns two cars, but he usually takes the bus because parking costs so much.`; `owns` + `costs` turuncu daire, `usually` sarı alt çizgi |
| 34,13–39,77 | Sağ: araba `coco/car.svg` (300 px) üstü çizgili ✗ değil (sahip) + otobüs `coco/bus.svg` (300 px) |
| 39,90–42,94 | Caveat 48: `Mike'ın iki arabası var, ama genellikle otobüse biner.` |
| 46,05–48,29 | Kutu `durum fiili: own · cost · know` ; `ing` kırmızı çizgiyle silinir (`owns` ✗ `is owning`) |

### 05 Örnek 3 (düz canvas, 406 kare, t 48,29–61,41, çıkış fade)
| küresel sn | Hareket |
|---|---|
| 48,84–50,05 | Daire içinde `3` |
| 50,05–54,21 | Fredoka 56 (3 satır): `Our flight takes off at eleven tomorrow morning, so we have to leave home at nine.`; `tomorrow` kırmızı daire (tuzak), `takes off` sarı |
| 50,05–54,81 | Sağ: uçak `coco/plane.svg` (400 px) + takvim `tabler/calendar.svg` + saat `coco/clock.svg` `11:00` |
| 54,94–56,38 | Caveat 48: `Uçuşumuz yarın sabah on birde kalkıyor.` |
| 57,41–61,41 | El çizimi tarife tablosu `11:00  takes off`; `tomorrow` kırmızı çizgi `≠ will`; çıkış fade |

### 06 Soru + Form (HyperFrames, 901 kare, t 61,41–90,43)
| küresel sn | Hareket |
|---|---|
| 61,96–65,88 | Künye `Question`. Sol: öğrenci başı `peeps-kit/ogrenci-bas.svg` + balon; Fredoka 600 44: `Hocam, yarın dediği için will take off olmaz mıydı?` Sağ: `will take off` ? |
| 66,43–71,24 | Künye `Form`. Balon ve baş küçülür; büyük kırmızı `✗ will` ; yeşil yerine mürekkep `takes off ✓` |
| 71,24–75,01 | Fredoka 72: `Will` = `predictions · sudden decisions` (iki etiket); `tarife · program · takvim` Simple Present kutusunda |
| 75,01–84,87 | Durum fiilleri: `know` `own` `cost` el kutusu; `I know the answer.` ✓ / `I am knowing.` ✗ (kırmızı çizgi, 83,70) |
| 84,87–90,43 | Alt: Fredoka 110 `tarife → Simple Present` / `tahmin → will` (iki satır, sarı); sağ alt `Next lesson →`; son 1 sn durgun |

## 5. Çalıştırma (her sahne kendi `calistir.sh`; paket kökünden)
- Canvas/Paper.js: `python3 ortak/yakala.py projeler/simple-present-ileri/sahneler/<klasor>/sayfa.html "$KARE"` →
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
| Harita | `/p/simple-present-ileri/harita.html?ac=02,02-04,02-04-ydt-ileri&sec=<kimlik>` |
| Editör | `/p/simple-present-ileri/onizle.html?surum=ana-yatay&t=0&tema=acik&yan=1&yol=02,02-04,02-04-ydt-ileri` |
| API | `/api/simple-present-ileri/{gorevler,surumler,yorumlar,konum}` |
| Eski adres | `/projeler/simple-present-ileri/{harita,onizle}.html` → 302, sorgu korunur |
