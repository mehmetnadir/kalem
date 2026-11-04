# Present Perfect Continuous — kalem paketi (YDT temel, Doğan Hoca destesi unit-1_sunum-5) · `projeler/present-perfect-cont-temel`

Amaç: ana örnek paketin (`../present-continuous/BRIEF.md`) görsel dilini bu konuya uygulamak. Çıktı `cikti.mp4`
(1920×1080, 30 fps, ≈83 sn). Anlatım hazır: `ortak/anlatim/anlatim.wav` (soğuk açılış: ilk söz 1,00 sn).
Metin ve zamanlar: `ortak/anlatim/METIN.md`, sözcük zamanları `ortak/anlatim/sozcukler.json` (küresel sn).
Kod `ING-YDT-GR-02-09-T`, rozet `YDT · BASIC`, ders adı `PRESENT PERFECT CONTINUOUS`. HUD'a sığmazsa ders adı `PRES. PERFECT CONT.`
olur (`ortak/kunye.js` `ders` alanı; sığma ölçülmedi, sahne ajanı kareye bakıp karar verir).
Seviye kuralı (temel): tümevarım — 3 günlük örnek → kalıp; EN yalnız örnek; Türkçe -dir … -yor köprüsü.

## 0. Nadir'in istekleri (kaynak: 03–04.11 konuşmaları; hepsi bu videoda görünür olmalı)

| # | İstek | Bu videoda |
|---|---|---|
| 1 | Gerçek YDS Publishing logosu | `ortak/logo/yds-publishing-seffaf.svg` (sarı "yds" + beyaz "publishing"); başka logo YOK |
| 2 | Logodan sonra içerik başlıkları ekranda | Giriş: Hook · Examples · Form listesi |
| 3 | Başlıklar animasyonla şablon köşelerine kayar | Giriş 2,2–3,0 sn uçuş → künye (bkz §3) |
| 4 | Giriş = YouTube kapak biçimi | Sol sütun: rozet hapları + 2 satır büyük başlık (beyaz/sarı, kalın kontur); sağ sütun: kalem eskizi; logo alt sol |
| 5 | İngilizce ders → şablonda Türkçe yok | Künye, etiketler, formül kartı İngilizce. Anlatım ve Türkçe çeviri İÇERİKTİR, serbest |
| 6 | Anlatılan şey hep ekranda; zoom ile kaybolmaz; 4 köşe sabit | Künye kamera dışında, her karede; kamera hareketi yok ya da küçük (≤ %6) |
| 7 | Kalem ile çizme etkisine en yakın çizim; minik çizimler | `cizgi()` kalem darbesi geometrisi (uçta incelme, titrek merkez, ilerleyen dolgu) — bkz §2.3 |
| 8 | Fosforlu kalem belirteçleri (altını çiz, daire, ok) | Konuşulan sözcüğün altında sarı belirteç; have/has been + -ing daire; oklar kalemle |
| 9 | Ekran düz kalmasın, öğrenci 3 dk'da sıkılmasın | Her 4 sn içinde en az bir hareket (çizim, belirteç, figür); boş kare yok |
| 10 | Kalem simgesi gerekmez | Ekranda kalem/el YOK; çizgi kendini çizer |
| 11 | Karaoke/altyazı bandı YOK | Sözcük vurgusu yalnız cümlenin kendi üstünde |
| 12 | Öğrenci sorusu (balon) | Sahne 06 ilk 3,36 sn |
| 13 | Ses tasarımı | Olay → Tone.js efekt (kalem hışırtısı, tık, sayfa) — `olaylar.json` |

Kapalı kararlar: DUR kartı yok · video ortasında soru kartı yok · QR bu prototipte yok (adres kararı bekliyor).


Konu notu: bu pakette 6 sahne ve 7 cümle ana paketle aynı sırada. Cümle 1 kanca (`İki saattir çalışıyorum.`), cümle 6 öğrenci sorusu (`Hocam, üçünde de been var. Neden hep been?`). Çizim listesi yalnız `ortak/cizim/` içinde VAR OLAN dosyalardan kurulur (bkz. §4: sitting/standing figürleri, tabler ve coco nesneleri).

## 1. Teknik çerçeve

- `zaman.json`: 6 sahne, `gecis_kare` N = 12. Sahne i yerel kare f ↔ küresel kare `ofs_i + f`, `ofs_i = Σ(kare_j − N)`.
  Yani yerel f ↔ küresel saniye `t_bas + f/30`. Sahne i>0'ın ilk N karesi ve i<son'un son N karesi geçiş altında
  (BookFlip / fade) görünür: bu karelerde içerik DURGUN olmalı (giriş: künye hazır, tuval boş; çıkış: her şey yerleşmiş).
- Kare sayıları zaman.json'daki `kare` ile BİREBİR (birlestir uyarır, kayma olur). İçerik `icerik_kare`'ye kadar biter.
- Zaman yalnız kare numarasından gelir; `Math.random` / `Date` YOK (iki koşu aynı kareyi verir; ornek tohumlu `hash`).
- Çıktı her sahnede: `video.mp4` (libx264 crf 16 yuv420p, tam kare sayısı) + `olaylar.json` + `kontrol.png` (6 kare, yatay)
  + `k/<kare>.png` (en az 3 tam boy denetim karesi) + `RAPOR.md`.

| Sahne | Klasör | Motor | Kare | Küresel sn | Anlatım |
|---|---|---|---|---|---|
| 1 | 01-hyperframes-giris | HyperFrames | 102 | 0,00–3,00 | cümle 1 (1,00–2,84) |
| 2 | 02-paperjs-kanca | Paper.js | 436 | 3,00–17,13 | cümle 2 |
| 3 | 03-paperjs-ornek1 | Paper.js | 467 | 17,13–32,28 | cümle 3 |
| 4 | 04-canvas-ornek2 | Düz canvas | 462 | 32,28–47,27 | cümle 4 |
| 5 | 05-canvas-ornek3 | Düz canvas | 439 | 47,27–61,51 | cümle 5 |
| 6 | 06-hyperframes-form | HyperFrames | 681 | 61,51–83,22 | cümle 6 (öğrenci) + 7 |

Cümle başları (sn): 1: 1,00 · 2: 3,39 · 3: 17,68 · 4: 32,83 · 5: 47,82 · 6: 62,06 · 7: 65,97. Anlatım biter 82,22; t_son = bitiş + 1,0. Sınır kuralı: sahne sınırı = sonraki cümle başı − 0,55 (spec §3.4).

## 2. Görsel dil (stil anayasası — bütün sahneler aynı)

### 2.1 Renk (yalnız bunlar)
**Render varsayılanı AÇIK tema (K19, 04.11)**; koyu kullanıcı seçimidir: `calistir.sh --tema koyu`, `birlestir.py --tema koyu` (`cikti-koyu.mp4`).
Açık palet: zemin `#f7f3ea` · mürekkep `#1b2440` · ikincil `#5a6275` · vurgu `#d9900f` · kırmızı `#d6453a`; logo `yds-publishing-lacivert.svg`. Aşağıdaki hex değerleri KOYU temadır.
zemin `#1b1a17` · mürekkep (krem) `#f3efe6` · ikincil `#c9c2b3` · vurgu sarı `#f2a93b` · logo sarısı `#fece00`
(yalnız logo ve giriş başlığı 2. satır) · kırmızı `#e0473b` (yalnız "Look!").
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
| Sol üst | `PRESENT PERFECT CONTINUOUS` + ` · YDT BASIC` | x 56, taban y 72; Fredoka 700 30 px; Lexend 500 22 px, 14 px boşluk | krem / ikincil |
| Sağ üst | bölüm adı: `Hook` · `Example 1 / 3` · `Example 2 / 3` · `Example 3 / 3` · `Question` → `Form` | sağ kenar x 1864, taban 72; Lexend 700 24 px | vurgu |
| Sol alt | logo svg | x 56, yükseklik 34 px (en ≈ 137), alt kenar y 1036 | logonun kendi renkleri |
| Sağ alt | ajanda `Hook  Examples  Form`, etkin olan sarı + 4 px nokta solunda | sağ kenar 1864, taban 1030; Lexend 500 20 px, 36 px aralık | ikincil / vurgu |

Canvas: `ortak/kunye.js` → `kunyeHazirla()`, `zeminCiz(ctx, f, K)`, `kunyeCiz(ctx, {bolum, etkin, logo})`.
HyperFrames: aynı sayılar CSS'te; sahne 01'in uçuş hedefleri bu tablodur (bitişte piksel piksel aynı görünmeli).


Ders adı sığması: `PRESENT PERFECT CONTINUOUS` Fredoka 700 30 px ≈ 500 px (sol üst boşluk > 800 px): sığar. Dikeyde 56 px ≈ 900 px < 984: sınırda; sığmazsa `PRES. PERFECT CONT.`.

## 4. Sahne sözleşmeleri (küresel saniye; yerel kare = round((t − t_bas) × 30); sınırlar cümle başı − 0,55; hiçbir tablo eski çerçeve kaydırması taşımaz)

### 01 Giriş — soğuk açılış (HyperFrames, 102 kare, t 0,00–3,00; cümle 1)

Karar (Nadir 04.11, K23): giriş 3 sn, ilk söz ≤ 1 sn, kalem sesi 0. kareden, geri sayım / tik tak YOK. İçerik 3,0 sn (kare 0–90).
| sn | Hareket |
|---|---|
| 0,00–0,40 | Logo damgası sol sütun altında (110 px, x 96, y ≈ 880): ölçek 1,18→1,0 + dönme −2°→0, alfa 0→1 (vurus kare 3) |
| 0,30–0,90 | Rozet hapları: `YDT · BASIC`, `GRAMMAR` (stagger 0,1) |
| 0,00–2,20 | Başlık kalemle çizilir (soldan açılan kırpma): `PRESENT PERFECT` 0,0–1,1, `CONTINUOUS` 1,0–2,2; Fredoka 700 112 (en ≤ 1100; 15 harflik satır 140'a sığmaz). Kalem sesi kare 0 (cizgi + hisirti) |
| 0,20–2,30 | Sağ sütun: oturan figür (sitting-5) + dizüstü (laptop) + saat (clock), stroke-dash, cizgi olayları |
| 1,00–2,84 | Başlığın altında (x 96, y 650) Caveat 700 64: `İki saattir çalışıyorum.` sözcük sözcük (`sozcukler.json`) |
| 2,20–3,00 | UÇUŞ: başlık → sol üst künye; logo → sol alt 34 px; eskiz solar (parilti); künye metinleri son 0,25 sn'de belirir; ajanda burada belirir |
| 3,00 | Künye yerleşik; cümle yerinde; son 12 kare BookFlip altında durgun |

### 02 Kanca (Paper.js, 436 kare, t 3,00–17,13; cümle 2)

| sn | Hareket |
|---|---|
| 3,00–3,40 | Cümle 1 yazısı hazır sayılır: Caveat 64 (x 140, y 300) `İki saattir çalışıyorum.`; sağda eskiz: figür + dizüstü + saat |
| 4,91–5,43 | `saat-tir` içindeki `-dir` sarı daire; Caveat not `-dir → süre` (ok) |
| 6,91–7,95 | `çalış-ıyor-um` içindeki `-yor` sarı daire; Caveat not `-yor → iş sürüyor`; alt çizgi: zaman çizgisi (el çizgisi): `2 saat önce` noktası → `now`, aradaki bant sarı |
| 8,10–10,66 | Altına Fredoka 56 (y 520): `I have been working for two hours.`; `have been` ve `-ing` sarı daire; iki yönlü kalem oku `-dir … -yor ⇄ have been … -ing` |
| 10,73–17,13 | Alt sağ el çizimi kutu, 3 madde tik zamanlı: `form` (formunu) · `time expressions` (ikinci `süre`) · `result clue` (sonuç); küçük saat `6 min` (dakikada) |

### 03 Örnek 1 (Paper.js, 467 kare, t 17,13–32,28; cümle 3)

| sn | Hareket |
|---|---|
| 17,68–18,64 | Büyük el çizimi daire içinde `1` (x 140, y 200) |
| 18,89–21,93 | Fredoka 64: `I have been waiting for the bus for twenty minutes.` sözcük sözcük (x 140, y 320, en ≤ 980, 2 satır) + sarı alt çizgi kayar |
| 18,89–21,93 | Sağ: bekleyen figür (sitting-4) + otobüs (bus, 460 px) + küçük saat (clock) |
| 20,41–21,93 | `for twenty minutes` altına sarı yay; Caveat `20 dk` |
| 22,10–24,26 | Caveat 48: `Yirmi dakikadır otobüs bekliyorum.` (y 470) |
| 24,30–25,62 | Zaman çizgisi (el çizgisi, y 620): `20 dk önce` noktası, `now` nabız atar; arada dalgalı `in progress` bandı sarı |
| 25,87–28,28 | `for` Fredoka 110 sarı (vurus) + Caveat `süre uzunluğu` |
| 28,84–32,28 | Formül kartı (el kutusu, alt): `have been  +  V-ing`; `have been` (ikinci `have`) ve `waiting` sarı daire; altında `wait-ing` (-ing sarı) |

### 04 Örnek 2 (düz canvas, 462 kare, t 32,28–47,27; cümle 4)

| sn | Hareket |
|---|---|
| 32,83–33,87 | Daire içinde `2` |
| 34,12–37,48 | Fredoka 64: `My brother has been playing the guitar since this morning.` sözcük sözcük + sarı alt çizgi |
| 34,12–37,48 | Sağ: kardeş (sitting-2) gitarda (guitar, 440 px); notalar (music) 3 adet teker teker (parilti) |
| 35,96–37,48 | Zaman çizgisi: sol uçta güneş (sun) `this morning` → kalem oku → `now` |
| 37,73–40,37 | Caveat 48: `Kardeşim sabahtan beri gitar çalıyor.` |
| 40,62–42,22 | `since` Fredoka 110 sarı + Caveat `başlangıç noktası`; soluk Caveat (ikincil) `for = süre uzunluğu` |
| 44,23–47,27 | Formül kartı: `has been  +  V-ing` → `has` sarı daire (`has been` anında) / `play-ing` |

### 05 Örnek 3 (düz canvas, 439 kare, t 47,27–61,51; cümle 5; çıkış fade)

| sn | Hareket |
|---|---|
| 47,82–48,86 | Daire içinde `3` |
| 49,11–49,75 | `Look!` Fredoka 110 kırmızı, ölçek 0,6→1 taşmalı (vurus) + kalem ünlem çizgisi |
| 49,83–52,87 | Fredoka 64: `The street is wet. It has been raining.` sözcük sözcük (Look! ayrı, üstte) |
| 49,83–52,87 | Sağ: yağmur bulutu (rain, 520 px) kalemle; `wet` anında sokak çizgisi + 3 su birikintisi çizgisi; şemsiye (umbrella, 260 px) `It` anında |
| 53,12–56,40 | Caveat 48: `Bak, sokak ıslak.` sonra `Yağmur bir süredir yağıyor.` |
| 56,56–57,76 | Sarı ok ıslak sokağa; Caveat vurgu `izi şimdi görünüyor` (sonuç ipucu) |
| 57,91–61,51 | Formül kartı: `has been  +  V-ing` → `has been` (ikinci `has`) sarı daire / `rain-ing` |

### 06 Soru + Form (HyperFrames, 681 kare, t 61,51–83,22; cümle 6 öğrenci, cümle 7 öğretmen)

| sn | Hareket |
|---|---|
| 62,06–63,66 | Künye sağ üst `Question`. Sol: öğrenci BAŞI (peeps-kit ogrenci-bas.svg, 0,4 sn; K22 kadın ses = kadın çizim) + el çizimi konuşma balonu; Fredoka 600 44 sözcük sözcük: `Hocam, üçünde de been var. Neden hep been?` Sağ: `have been waiting` · `has been playing` · `has been raining` dikey, `been` sarı (tik) |
| 65,97–68,33 | Künye `Form`. Üç `been` tek büyük `been`'e toplanır (Fredoka 160 sarı, sağ orta; vurus); altında `past → now` kalem oku (`have` geçmişi bugüne bağlar); balon ve baş küçülüp yukarı kayar (alfa 0,45) |
| 68,61–71,17 | `been` kutusu + `-ing` sarı; Caveat `in progress →` bandı |
| 71,32–74,36 | Sol sütun: `-dir … -yor` Fredoka 96, çift yönlü ok, `have been … -ing` (sarı eşleşme) |
| 74,53–76,93 | Fredoka 64: `I have been working for two hours.` sözcük sözcük |
| 77,10–79,10 | Altında Caveat 56: `saat-tir  çalış-ıyor-um`; `-dir`/`-yor` sarı ↔ `for two hours`/`have been … -ing` kalem bağı |
| 79,14–82,30 | Formül kartı el kutusunda toplanır: `have / has been  +  V-ing` (tik); sağ altta ajandanın üstünde küçük `Next lesson →` Lexend 24 ikincil |
| 82,30–83,22 | Durgun (1 sn kuyruk) |
## 5. Çalıştırma (her sahne kendi `calistir.sh`; paket kökünden)
- Canvas/Paper.js: `python3 ortak/yakala.py projeler/present-perfect-cont-temel/sahneler/<klasor>/sayfa.html "$KARE"` →
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
| Harita | `/p/present-perfect-cont-temel/harita.html?ac=02,02-09,02-09-ydt-temel&sec=<kimlik>` |
| Editör | `/p/present-perfect-cont-temel/onizle.html?surum=ana-yatay&t=0&tema=acik&yan=1&yol=02,02-09,02-09-ydt-temel` |
| API | `/api/present-perfect-cont-temel/{gorevler,surumler,yorumlar,konum}` |
| Eski adres | `/projeler/present-perfect-cont-temel/{harita,onizle}.html` → 302, sorgu korunur |
