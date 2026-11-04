# Present Continuous — prototip 4 "kalem" (YDT temel, Doğan Hoca anlatımı)

Amaç: Nadir'in konuşmalar boyunca istediği görsel dili kalem motorlarıyla GÖSTERMEK. Çıktı `cikti.mp4`
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
| 12 | Öğrenci sorusu (balon) | Sahne 06 ilk 3,4 sn |
| 13 | Ses tasarımı | Olay → Tone.js efekt (kalem hışırtısı, tık, sayfa) — `olaylar.json` |

Kapalı kararlar: DUR kartı yok · video ortasında soru kartı yok · QR bu prototipte yok (adres kararı bekliyor).

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
| 1 | 01-hyperframes-giris | HyperFrames | 102 | 0,00–3,40 | cümle 1 (1,00–2,84) |
| 2 | 02-paperjs-kanca | Paper.js | 385 | 3,00–15,83 | cümle 2 (cümle 1 yazısı hazır belirir) |
| 3 | 03-paperjs-ornek1 | Paper.js | 453 | 15,44–30,54 | cümle 3 |
| 4 | 04-canvas-ornek2 | düz canvas | 487 | 30,15–46,38 | cümle 4 |
| 5 | 05-canvas-ornek3 | düz canvas | 517 | 45,98–63,21 | cümle 5 |
| 6 | 06-hyperframes-form | HyperFrames | 766 | 62,81–88,33 | cümle 6 (öğrenci) + 7 |

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
| Sol üst | `PRESENT CONTINUOUS` + ` · YDT BASIC` | x 56, taban y 72; Fredoka 700 30 px; Lexend 500 22 px, 14 px boşluk | krem / ikincil |
| Sağ üst | bölüm adı: `Hook` · `Example 1 / 3` · `Example 2 / 3` · `Example 3 / 3` · `Question` → `Form` | sağ kenar x 1864, taban 72; Lexend 700 24 px | vurgu |
| Sol alt | logo svg | x 56, yükseklik 34 px (en ≈ 137), alt kenar y 1036 | logonun kendi renkleri |
| Sağ alt | ajanda `Hook  Examples  Form`, etkin olan sarı + 4 px nokta solunda | sağ kenar 1864, taban 1030; Lexend 500 20 px, 36 px aralık | ikincil / vurgu |

Canvas: `ortak/kunye.js` → `kunyeHazirla()`, `zeminCiz(ctx, f, K)`, `kunyeCiz(ctx, {bolum, etkin, logo})`.
HyperFrames: aynı sayılar CSS'te; sahne 01'in uçuş hedefleri bu tablodur (bitişte piksel piksel aynı görünmeli).

## 4. Sahne sözleşmeleri (yerel kare = round((t − t_bas) × 30); 02–06 tabloları 04.11 öncesi küresel saniyeyle yazılı, gerçek t_bas 4,0 sn geri (03–06: 6,0 sn), sahne kodu KAYMA ile çevirir)

### 01 Giriş — soğuk açılış (HyperFrames, 102 kare, t 0–3,4; cümle 1 burada konuşulur; kapak kalıbı)
Karar (Nadir 04.11, K23): giriş 3 sn, ilk söz ≤ 1 sn, kalem sesi 0. kareden, geri sayım / tik tak YOK.
İçerik 3,0 sn (kare 0–90); son 12 kare BookFlip altında durgun (künye hazır, cümle yerinde).
| sn | Hareket |
|---|---|
| 0,0–0,4 | Logo damgası sol sütun altında (110 px, x 96, y ≈ 880): ölçek 1,18→1,0 + dönme −2°→0, alfa 0→1 (vurus kare 3) |
| 0,3–0,9 | Rozet hapları: `YDT · BASIC`, `GRAMMAR` (stagger 0,1) |
| 0,0–2,2 | Başlık kalemle çizilir (soldan açılan kırpma): `PRESENT` 0,0–1,1, `CONTINUOUS` 1,0–2,2; Fredoka 700 140. Kalem sesi kare 0 (cizgi + hisirti) |
| 0,2–2,3 | Sağ sütun: ayakta figür (standing-3) 0,2–2,0, kamera 1,6–2,2 (stroke-dash, cizgi olayları) |
| 1,0–2,92 | Başlığın altında (x 96, y 650) Caveat 700 64 krem: `Bu akşam amcamlara gidiyorum.` cümle 1 ile sözcük sözcük yazılır (`sozcukler.json`) |
| 2,2–3,0 | UÇUŞ: başlık → sol üst künye; logo → sol alt 34 px; eskiz solar (parilti); künye metinleri son 0,25 sn'de belirir; ajanda burada belirir |
| 3,0–3,4 | Künye yerleşik; cümle yerinde; kare 90–101 BookFlip altında |

### 02 Kanca (Paper.js, 385 kare, t_bas 3,00; cümle 2). Tablo eski çerçevede (t − 7,00) × 30; cümle 2'den sonraki satırlar gerçekte 2,0 sn (60 kare) öne alındı: yerel kare = (t − 7,00) × 30 − 60
| sn | Hareket |
|---|---|
| 0–0,4 sn (kare 0–9) | (cümle 1 sesi sahne 01'de; yazı hazır sayılır, çizilmeden hızlı belirir) Caveat 64 krem, sol (x 140, y 300): `Bu akşam amcamlara gidiyorum.` sözcük zamanında yazılır. Sağda eskiz: ev (home, 260 px, x≈1450 y≈300) + ona yürüyen figür (standing-2) + hilal (el elipsi) |
| 9,39–12,35 | `gidiyorum` sarı daire; Caveat not `-yor → şimdiki zaman`; ok → küçük takvim (calendar) + Caveat `bu akşam → gelecek` |
| 12,50–14,58 | Altına Fredoka 56 krem: `I'm going to my uncle's tonight.` (y 520); `going` sarı daire; iki yönlü kalem oku `-yor ⇄ -ing` |
| 14,73–20,89 | Alt sağ: el çizimi kutu, 3 madde tik zamanlı: `form` (16,97) · `time expressions` (17,65) · `6 uses` (19,29); küçük saat (clock) `6 min` 14,73 |
| 20,89–21,83 | Her şey yerleşik; son 12 kare durgun |

### 03 Örnek 1 (Paper.js, 453 kare, t_bas 15,44; tablo eski çerçevede: yerel kare = (t − 21,44) × 30)
| sn | Hareket |
|---|---|
| 21,44–22,48 | Büyük el çizimi daire içinde `1` (x 140, y 200) |
| 22,73–24,65 | Fredoka 64: `I am sitting in front of the camera now.` sözcük sözcük (x 140, y 320, en ≤ 980, 2 satır) + sarı alt çizgi kayar |
| 22,5–24,6 | Sağ: oturan figür (sitting-4) kameraya bakar; kamera (camera) + üç ayaklı sehpa (3 el çizgisi) 23,8–24,6 |
| 24,65 | `now` sarı daire + Caveat etiket `NOW` |
| 25,30–25,78 | Caveat 48 ikincil: `Şu anda oturuyorum.` (y 470) |
| 26,78–28,26 | Zaman çizgisi (el çizgisi, y 620): `now` noktası nabız atar; üstünde dalgalı `in progress` bandı sarı |
| 29,29–31,85 | `am` (30,73) ve `sitting` (31,85) sarı daire |
| 33,04–35,60 | Formül kartı (el kutusu, alt): `be  +  V-ing` Fredoka 60; altında `am` / `sitt-ing` (-ing sarı) |
| 35,60–36,54 | Durgun |

### 04 Örnek 2 (düz canvas, 487 kare, t_bas 30,15; tablo eski çerçevede: yerel kare = (t − 36,15) × 30)
| sn | Hareket |
|---|---|
| 36,15–37,19 | Daire içinde `2` |
| 37,44–39,76 | Fredoka 64: `My sister is taking piano lessons this semester.` sözcük sözcük + sarı alt çizgi |
| 37,6–39,6 | Sağ: kız kardeş (sitting-2) piyanoda (piano büyük, 420 px); notalar (music) 3 adet 39,0–40,6 teker teker (parilti) |
| 40,89–42,65 | Caveat 48: `Kardeşim bu dönem piyano dersi alıyor.` |
| 43,41–46,65 | Takvim şeridi (el çizimi 5 kutu) `this semester`; sarı köşeli ayraç hepsini kapsar; ortada `now` noktası; Caveat `not at this moment → these days` |
| 47,12–47,92 | `is`, `taking` sarı daire |
| 49,03–50,63 | Formül kartı: `be + V-ing` → `is` / `tak-ing` |
| 50,63–52,38 | Durgun |

### 05 Örnek 3 (düz canvas, 517 kare, t_bas 45,98; tablo eski çerçevede: yerel kare = (t − 51,98) × 30; çıkış fade)
| sn | Hareket |
|---|---|
| 51,98–53,02 | Daire içinde `3` |
| 53,27 | `Look!` Fredoka 110 kırmızı, ölçek 0,6→1 taşmalı (vurus 0,9) + kalem ünlem çizgisi |
| 53,99–55,59 | Fredoka 64: `The cat is climbing the tree.` sözcük sözcük (Look! ayrı, üstte) |
| 53,3–54,6 | Sağ: ağaç (tree, 520 px) kalemle; 54,4–56,5 kedi (cat, 150 px) gövde boyunca aşağıdan ortaya tırmanır (yol + hafif salınım), başlangıçta 3 toz çizgisi |
| 56,32–57,60 | Caveat 48: `Bak, kedi ağaca tırmanıyor.` |
| 58,88–63,96 | Etiketler el kutusunda: `Look!` (58,88) · `Listen!` (59,60) · `Watch out!` (60,52), her biri tik; 62,80–63,96 sarı ok → el çizimi `NOW` noktası |
| 65,37–65,69 | `is`, `climbing` sarı daire |
| 67,14–67,51 | Formül kartı: `be + V-ing` → `is` / `climb-ing` |
| 67,51–69,21 | Durgun |

### 06 Soru + Form (HyperFrames, 766 kare, t_bas 62,81; tablo eski çerçevede (+6 sn); cümle 6 öğrenci, cümle 7 öğretmen)
| sn | Hareket |
|---|---|
| 68,81–72,17 | Künye sağ üst `Question`. Sol: oturan öğrenci figürü (sitting-6, SVG stroke-dash) + el çizimi konuşma balonu; Fredoka 600 44 krem sözcük sözcük: `Hocam, üçünde de -ing var. Neden hep -ing?` Sağ: `sitt-ing` · `tak-ing` · `climb-ing` dikey, -ing sarı (69,5 / 70,2 / 70,9, tik) |
| 72,72–77,28 | Künye `Form`. Üç `-ing` tek büyük `-ing`'e toplanır (Fredoka 160 sarı, sağ orta; vurus); altında el çizimi `in progress →` bandı; balon solar, figür küçülür sol alta (künyeye değmez) |
| 77,43–83,19 | Sol sütun `be` kolonu: `am` · `is` · `are` Fredoka 72 krem, sözcük zamanlarında; Caveat `now` sarı yanında |
| 83,34–87,10 | Altında soluk `was · were` ikincil + Caveat `past`, kırmızı tek çizgi üstünden |
| 87,25–91,73 | Alt: Caveat 56 `koşu-yor  =  runn-ing`, `-yor` ve `-ing` sarı; `=` kalemle çizilir |
| 91,73–93,33 | Formül kartı el kutusunda toplanır: `am / is / are  +  V-ing` (tik); 92,5 sağ alt ajandanın üstünde küçük `Next lesson →` Lexend 24 ikincil |
| 93,33–94,33 | Durgun (1 sn kuyruk) |

## 5. Çalıştırma (her sahne kendi `calistir.sh`; paket kökünden)
- Canvas/Paper.js: `python3 ortak/yakala.py projeler/present-continuous/sahneler/<klasor>/sayfa.html "$KARE"` →
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
istenirse uzun yazı maskesi. Sahne başına 20–80 olay; aynı karede ≤ 3.

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
| Harita | `/p/present-continuous/harita.html?ac=02,02-01,02-01-ydt-temel&sec=<kimlik>` |
| Editör | `/p/present-continuous/onizle.html?surum=ana-yatay&t=0&tema=acik&yan=1&yol=02,02-01,02-01-ydt-temel` |
| API | `/api/present-continuous/{gorevler,surumler,yorumlar,konum}` |
| Eski adres | `/projeler/present-continuous/{harita,onizle}.html` → 302, sorgu korunur |
