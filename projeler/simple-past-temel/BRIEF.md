# Simple Past — temel seviye "kalem" paketi (YDT BASIC, Doğan Hoca destesi unit-1_sunum-6)

Amaç: Nadir'in konuşmalar boyunca istediği görsel dili kalem motorlarıyla Simple Past konusunda GÖSTERMEK (Present Continuous prototipinin aynı dili). Çıktı `cikti.mp4`
(1920×1080, 30 fps, ≈94 sn) + `kontrol.png`. Anlatım hazır: `ortak/anlatim/anlatim.wav` (soğuk açılış: ilk söz 1,00 sn).
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
| 8 | Fosforlu kalem belirteçleri (altını çiz, daire, ok) | Konuşulan sözcüğün altında sarı belirteç; -ed / went / did daire; oklar kalemle |
| 9 | Ekran düz kalmasın, öğrenci 3 dk'da sıkılmasın | Her 4 sn içinde en az bir hareket (çizim, belirteç, figür); boş kare yok |
| 10 | Kalem simgesi gerekmez | Ekranda kalem/el YOK; çizgi kendini çizer |
| 11 | Karaoke/altyazı bandı YOK | Sözcük vurgusu yalnız cümlenin kendi üstünde |
| 12 | Öğrenci sorusu (balon) | Sahne 06 ilk 4 sn |
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
| 1 | 01-hyperframes-giris | HyperFrames | 102 | 0,00–3,00 | cümle 1 (1,00–2,84) |
| 2 | 02-paperjs-kanca | Paper.js | 366 | 3,00–14,80 | cümle 2 (3,39–14,25) |
| 3 | 03-paperjs-ornek1 | Paper.js | 448 | 14,80–29,35 | cümle 3 (14,80–28,80) |
| 4 | 04-canvas-ornek2 | Düz canvas | 566 | 29,35–47,82 | cümle 4 (29,35–47,27) |
| 5 | 05-canvas-ornek3 | Düz canvas | 521 | 47,82–64,78 | cümle 5 (47,82–64,23) |
| 6 | 06-hyperframes-form | HyperFrames | 901 | 64,78–93,81 | cümle 6 öğrenci (64,78–68,78) + cümle 7 (69,33–92,81) |

## 2. Görsel dil (stil anayasası — bütün sahneler aynı)

### 2.1 Renk (yalnız bunlar)
**Render varsayılanı AÇIK tema (K19, 04.11)**; koyu kullanıcı seçimidir: `calistir.sh --tema koyu`, `birlestir.py --tema koyu` (`cikti-koyu.mp4`).
Açık palet: zemin `#f7f3ea` · mürekkep `#1b2440` · ikincil `#5a6275` · vurgu `#d9900f` · kırmızı `#d6453a`; logo `yds-publishing-lacivert.svg`. Aşağıdaki hex değerleri KOYU temadır.
zemin `#1b1a17` · mürekkep (krem) `#f3efe6` · ikincil `#c9c2b3` · vurgu sarı `#f2a93b` · logo sarısı `#fece00`
(yalnız logo ve giriş başlığı 2. satır) · kırmızı `#e0473b` (yalnız yanlış biçim ve tuzak çizgisi).
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
| Sol üst | `SIMPLE PAST` + ` · YDT BASIC` | x 56, taban y 72; Fredoka 700 30 px; Lexend 500 22 px, 14 px boşluk | krem / ikincil |
| Sağ üst | bölüm adı: `Hook` · `Example 1 / 3` · `Example 2 / 3` · `Example 3 / 3` · `Question` → `Form` | sağ kenar x 1864, taban 72; Lexend 700 24 px | vurgu |
| Sol alt | logo svg | x 56, yükseklik 34 px (en ≈ 137), alt kenar y 1036 | logonun kendi renkleri |
| Sağ alt | ajanda `Hook  Examples  Form`, etkin olan sarı + 4 px nokta solunda | sağ kenar 1864, taban 1030; Lexend 500 20 px, 36 px aralık | ikincil / vurgu |

Canvas: `ortak/kunye.js` → `kunyeHazirla()`, `zeminCiz(ctx, f, K)`, `kunyeCiz(ctx, {bolum, etkin, logo})`.
HyperFrames: aynı sayılar CSS'te; sahne 01'in uçuş hedefleri bu tablodur (bitişte piksel piksel aynı görünmeli).

## 4. Sahne sözleşmeleri (yerel kare = round((t − t_bas) × 30); tüm tablolar KÜRESEL saniye, sahne kodu `t_bas`'ı çıkarır)

### 01 Giriş — soğuk açılış (HyperFrames, 102 kare, t 0–3,0; cümle 1 burada konuşulur; kapak kalıbı)
Karar (Nadir 04,11, K23): giriş 3 sn, ilk söz ≤ 1 sn, kalem sesi 0. kareden, geri sayım / tik tak YOK.
İçerik 3,0 sn (kare 0–90); son 12 kare BookFlip altında durgun (künye hazır, cümle yerinde).
| sn | Hareket |
|---|---|
| 0,0–0,4 | Logo damgası sol sütun altında (110 px, x 96, y ≈ 880): ölçek 1,18→1,0 + dönme −2°→0, alfa 0→1 (vurus kare 3) |
| 0,3–0,9 | Rozet hapları: `YDT · BASIC`, `GRAMMAR` (stagger 0,1) |
| 0,0–2,2 | Başlık kalemle çizilir: `SIMPLE` 0,0–1,1, `PAST` 1,0–2,2; Fredoka 700 140. Kalem sesi kare 0 |
| 0,2–2,3 | Sağ sütun: ayakta figür (standing-3) 0,2–2,0, televizyon (device-tv) 1,6–2,2 (stroke-dash) |
| 1,00–2,84 | Başlığın altında (x 96, y 650) Caveat 700 64: `Dün akşam amcamlara gittim.` sözcük sözcük (Dün 1,00 · akşam 1,24 · amcamlara 1,64 · gittim 2,24) |
| 2,2–3,0 | UÇUŞ: başlık → sol üst künye; logo → sol alt 34 px; eskiz solar; künye metinleri son 0,25 sn'de belirir; ajanda belirir |

### 02 Kanca (Paper.js, 366 kare, t 3,00–14,80; cümle 2 = 3,39–14,25). Yerel kare = (t − 3,00) × 30
| sn | Hareket |
|---|---|
| kare 0–9 | (cümle 1 sahne 01'de söylendi; yazı hazır sayılır) Caveat 64 sol (x 140, y 300): `Dün akşam amcamlara gittim.` Sağda eskiz: ev (home, 260 px) + ona yürüyen figür (standing-2) + hilal (el elipsi) |
| 3,39–5,87 | `gittim` sarı daire (kare 0'dan); Caveat not `-di → biten iş`, `-di` (4,83) sarı kutu; ok → takvim (calendar) + Caveat `dün` |
| 6,02–8,10 | Altına Fredoka 56 (y 520): `I visited my uncle last night.`; `visited`'ın `-ed`'i (6,90) sarı daire; iki yönlü kalem oku `-di ⇄ -ed` |
| 8,25–14,25 | Alt sağ: el çizimi kutu, 3 madde tik: `form` (10,17) · `time expressions` (11,29) · `irregular verbs` (13,01); küçük saat (clock) `6 min` 8,57 |
| 14,25–14,80 | Her şey yerleşik; son 12 kare durgun |

### 03 Örnek 1 (Paper.js, 448 kare, t 14,80–29,35; cümle 3). Yerel kare = (t − 14,80) × 30
| sn | Hareket |
|---|---|
| 14,80–15,84 | Büyük el çizimi daire içinde `1` (x 140, y 200) |
| 16,09–18,09 | Fredoka 64: `I watched a movie last night.` sözcük sözcük (I 16,09 · watched 16,25 · a 16,57 · movie 16,65 · last 16,97 · night 17,37) + sarı alt çizgi kayar |
| 16,1–18,0 | Sağ: oturan figür (sitting-4) + televizyon (device-tv, 420 px) kalemle; ekranda 3 parıltı çizgisi |
| 17,37–18,09 | `last night` sarı daire + Caveat etiket `LAST NIGHT` |
| 18,34–20,0 | Caveat 48 ikincil: `Dün gece bir film izledim.` (y 470) |
| 20,22–22,90 | Zaman çizgisi (el çizgisi, y 620): solda dolu nokta `last night` (22,50), sağda `now`; aradaki bant kapalı kutu `bitti` (bitti 20,63) ; `belli` (21,78) tik |
| 23,85–26,89 | `watch` (25,21) ve `-ed` (26,17) sarı daire |
| 27,04–28,80 | Formül kartı (el kutusu, alt): `V + -ed`; altında `watch` → `watch-ed` (-ed sarı), Caveat `izle-di` |
| 28,80–29,35 | Durgun |

### 04 Örnek 2 (düz canvas, 566 kare, t 29,35–47,82; cümle 4). Yerel kare = (t − 29,35) × 30
| sn | Hareket |
|---|---|
| 29,35–30,39 | Daire içinde `2` |
| 30,64–33,60 | Fredoka 64: `My uncle went to London two years ago.` sözcük sözcük + sarı alt çizgi (went 31,32) |
| 30,8–33,0 | Sağ: ayakta figür (standing-5) + uçak (plane, 420 px); uçağın arkasında 3 hız çizgisi |
| 32,64 | `ago` sarı daire |
| 33,85–35,57 | Caveat 48: `Amcam iki yıl önce Londra'ya gitti.` |
| 36,73–39,13 | Takvim şeridi (el çizimi 4 kutu) `two years ago`; sola giden ok `ago = önce` (yani 37,49 · önce 38,01); sağda `now` noktası; `zaman belli` (39,13) tik |
| 40,08–42,24 | `-ed` (40,56) üstü kırmızı kalem çizgisi (yok); `go` (41,84) sarı daire |
| 43,51–44,71 | `go` → kalem oku → `went` Fredoka 110 (went 44,71 sarı) |
| 45,59–46,39 | Caveat `ezberle` + küçük kitap (book) ; `go → went` kutuya alınır |
| 46,39–47,82 | Durgun |

### 05 Örnek 3 (düz canvas, 521 kare, t 47,82–64,78; çıkış fade). Yerel kare = (t − 47,82) × 30
| sn | Hareket |
|---|---|
| 47,82–48,86 | Daire içinde `3` |
| 49,11–50,27 | Fredoka 64: `We didn't play football yesterday.` sözcük sözcük; `didn't` (49,27) sarı alt çizgi |
| 49,2–51,0 | Sağ: ayakta figür (standing-6) + futbol topu (ball-football, 360 px); topun üstüne kalemle büyük çarpı |
| 51,52–53,0 | Caveat 48: `Dün futbol oynamadık.` |
| 53,44–54,80 | `didn't` sarı daire; alt formül kartı: `did + not + V1` |
| 55,51–59,43 | `Did` (55,51) küçük geçmiş bayrağı çizer; `play` (59,43) sarı daire; yanında `played` kırmızı çizili |
| 60,30–61,74 | Soruda `Did` başa: kalem oku cümle başına |
| 62,87–64,23 | Fredoka 64: `Did you play football?` sözcük sözcük, `Did` sarı |
| 64,23–64,78 | Durgun |

### 06 Soru + Form (HyperFrames, 901 kare, t 64,78–93,81; cümle 6 öğrenci = 64,78–68,78, cümle 7 öğretmen = 69,33–92,81)
| sn | Hareket |
|---|---|
| 64,78–68,78 | Künye sağ üst `Question`. Sol: öğrenci BAŞI (peeps-kit ogrenci-bas.svg, 3 yol stroke-dash, 0,4 sn, balonla birlikte; kadın ses = kadın çizim) + el çizimi konuşma balonu; Fredoka 600 44 sözcük sözcük: `Hocam, birinde -ed var, ikisinde yok. Neden?` Sağ: `watch-ed` (-ed 66,14 sarı) · `went` (67,02) · `didn't play` (67,58) |
| 69,33–75,81 | Künye `Form`. İki kolon: `düzenli → + -ed` (Düzenli 71,01) ve `düzensiz → V2` (Düzensiz 73,25); örnekler `watch → watched`, `go → went`; balon ve baş küçülür, yukarı kayar, soluklaşır (alfa 0,45) |
| 75,96–79,72 | Kutu: `didn't + V1` ve `Did + özne + V1?` Fredoka 72 (did 77,32 · fiil yalın 78,20); `V1` sarı |
| 79,87–84,19 | Alt: Caveat 56 `izle-di  =  watch-ed` (izle-di 82,03 · watch-ed 83,07), `-di` ve `-ed` sarı, `=` kalemle çizilir |
| 84,34–89,62 | Zaman ifadeleri el kutularında: `yesterday` (84,34) · `ago` (85,46) · `last year` (86,10), her biri tik; sarı ok → `Simple Past` (88,86) |
| 89,77–92,81 | Formül kartı toplanır: `V-ed / V2  ·  did + V1` (tik); `Biten iş, belli zaman` (89,77); 92,0 sağ alt ajandanın üstünde küçük `Next lesson →` Lexend 24 ikincil |
| 92,81–93,81 | Durgun (1 sn kuyruk) |

## 5. Çalıştırma (her sahne kendi `calistir.sh`; paket kökünden)
- Canvas/Paper.js: `python3 ortak/yakala.py projeler/simple-past-temel/sahneler/<klasor>/sayfa.html "$KARE"` →
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
Şablon şef: Claude (Fable), 04.11.2026; bu konu: senaryo-sp ajanı, 05.11.2026. Kararlar: `~/01dev/dijital-anlatim/.claude/docs/video-format-kararlari.md`.

## Harita/editör

Kod ortaktır: `ortak/editor/{harita,onizle}.{html,js,css}`, `harita-model.js`, `yol.js`. Proje dizininde yalnız veri kalır.
Sunucu: `node ortak/onizle-sunucu.mjs --port 3012` (sunucu kodu değişince yeniden başlat).

| Sayfa | Adres |
|---|---|
| Harita | `/p/simple-past-temel/harita.html?ac=02,02-10,02-10-ydt-temel&sec=<kimlik>` |
| Editör | `/p/simple-past-temel/onizle.html?surum=ana-yatay&t=0&tema=acik&yan=1&yol=02,02-10,02-10-ydt-temel` |
| API | `/api/simple-past-temel/{gorevler,surumler,yorumlar,konum}` |
| Eski adres | `/projeler/simple-past-temel/{harita,onizle}.html` → 302, sorgu korunur |
