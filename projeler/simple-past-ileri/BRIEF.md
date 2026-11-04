# Simple Past — ileri seviye "kalem" paketi (YDT ADVANCED, Doğan Hoca destesi unit-1_sunum-6)

Amaç: Nadir'in konuşmalar boyunca istediği görsel dili kalem motorlarıyla Simple Past konusunda GÖSTERMEK (Present Continuous prototipinin aynı dili). Çıktı `cikti.mp4`
(1920×1080, 30 fps, ≈92 sn) + `kontrol.png`. Anlatım hazır: `ortak/anlatim/anlatim.wav` (soğuk açılış: ilk söz 1,00 sn).
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
| 8 | Fosforlu kalem belirteçleri (altını çiz, daire, ok) | Konuşulan sözcüğün altında sarı belirteç; ago / yet / used to daire; oklar kalemle |
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
| 1 | 01-hyperframes-giris | HyperFrames | 102 | 0,00–3,00 | cümle 1 (1,00–3,16) |
| 2 | 02-paperjs-kanca | Paper.js | 326 | 3,00–13,47 | cümle 2 (3,71–12,92) |
| 3 | 03-paperjs-ornek1 | Paper.js | 602 | 13,47–33,15 | cümle 3 (13,47–32,60) |
| 4 | 04-canvas-ornek2 | Düz canvas | 487 | 33,15–48,99 | cümle 4 (33,15–48,44) |
| 5 | 05-canvas-ornek3 | Düz canvas | 528 | 48,99–66,19 | cümle 5 (48,99–65,64) |
| 6 | 06-hyperframes-form | HyperFrames | 791 | 66,19–91,54 | cümle 6 öğrenci (66,19–70,51) + cümle 7 (71,06–90,54) |

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
| Sol üst | `SIMPLE PAST` + ` · YDT ADVANCED` | x 56, taban y 72; Fredoka 700 30 px; Lexend 500 22 px, 14 px boşluk | krem / ikincil |
| Sağ üst | bölüm adı: `Hook` · `Example 1 / 3` · `Example 2 / 3` · `Example 3 / 3` · `Question` → `Form` | sağ kenar x 1864, taban 72; Lexend 700 24 px | vurgu |
| Sol alt | logo svg | x 56, yükseklik 34 px (en ≈ 137), alt kenar y 1036 | logonun kendi renkleri |
| Sağ alt | ajanda `Hook  Examples  Form`, etkin olan sarı + 4 px nokta solunda | sağ kenar 1864, taban 1030; Lexend 500 20 px, 36 px aralık | ikincil / vurgu |

Canvas: `ortak/kunye.js` → `kunyeHazirla()`, `zeminCiz(ctx, f, K)`, `kunyeCiz(ctx, {bolum, etkin, logo})`.
HyperFrames: aynı sayılar CSS'te; sahne 01'in uçuş hedefleri bu tablodur (bitişte piksel piksel aynı görünmeli).

## 4. Sahne sözleşmeleri (yerel kare = round((t − t_bas) × 30); tüm tablolar KÜRESEL saniye, sahne kodu `t_bas`'ı çıkarır)

### 01 Giriş — soğuk açılış (HyperFrames, 102 kare, t 0–3,0; cümle 1 = 1,00–3,16 (son sözcüğün kuyruğu 0,16 sn sahne 02'ye taşar); kapak kalıbı)
Karar (Nadir 04,11, K23): giriş 3 sn, ilk söz ≤ 1 sn, kalem sesi 0. kareden, geri sayım / tik tak YOK.
İçerik 3,0 sn (kare 0–90); son 12 kare BookFlip altında durgun.
| sn | Hareket |
|---|---|
| 0,0–0,4 | Logo damgası sol sütun altında (110 px, x 96, y ≈ 880): ölçek 1,18→1,0 + dönme −2°→0, alfa 0→1 (vurus kare 3) |
| 0,3–0,9 | Rozet hapları: `YDT · ADVANCED`, `GRAMMAR` (stagger 0,1) |
| 0,0–2,2 | Başlık kalemle çizilir: `SIMPLE` 0,0–1,1, `PAST` 1,0–2,2; Fredoka 700 140. Kalem sesi kare 0 |
| 0,2–2,3 | Sağ sütun: ayakta figür (standing-3) 0,2–2,0, saat (clock) 1,6–2,2 (stroke-dash) |
| 1,00–3,16 | Başlığın altında (x 96, y 650) Caveat 700 64: `Ago varsa Perfect yok.` sözcük sözcük (Ago 1,00 · varsa 1,48 · Perfect 2,12 · yok 2,64); `Perfect` üstüne kırmızı çizgi 2,64'te |
| 2,2–3,0 | UÇUŞ: başlık → sol üst künye; logo → sol alt 34 px; eskiz solar; ajanda belirir |

### 02 Kanca (Paper.js, 326 kare, t 3,00–13,47; cümle 2 = 3,71–12,92). Yerel kare = (t − 3,00) × 30
| sn | Hareket |
|---|---|
| kare 0–9 | (cümle 1 yazısı hazır sayılır) Caveat 64 sol (x 140, y 300): `Ago varsa Perfect yok.`; `Perfect` kırmızı çizili. Sağda eskiz: takvim (calendar, 260 px) + saat (clock) |
| 3,71–9,07 | El çizimi kutu, 3 madde tik: `rule` (kuralını 5,55) · `time words` (belirteçlerini 6,99) · `traps` (tuzaklarını 8,51); küçük saat `6 min` 4,03 |
| 9,72–12,76 | Fredoka 56 iki satır (y 520): `A finished action at a definite time in the past.` sözcük sözcük (A 9,72 · finished 9,88 · definite 11,24 · past 12,44); `finished` sarı daire; `definite time` sarı alt çizgi (11,24–12,12) |
| 11,5–12,9 | Altta zaman çizgisi: kapalı kutu + `now` noktası; kutu sarı |
| 12,92–13,47 | Yerleşik; son 12 kare durgun |

### 03 Örnek 1 — kök 1 (Paper.js, 602 kare, t 13,47–33,15; cümle 3). Yerel kare = (t − 13,47) × 30
| sn | Hareket |
|---|---|
| 13,47–14,51 | Daire içinde `1` (x 140, y 200) |
| 14,68–19,92 | Fredoka 56 iki satır (en ≤ 1000, y 320): `Marie Curie won her second Nobel Prize in 1911, three years before the war began.` sözcük sözcük; `won` (15,56) ve `began` (19,60) sarı kutu; `1911` (17,24) sarı daire |
| 14,7–16,6 | Sağ: oturan figür (sitting-2) + kitap (book, 380 px) + kalem (pencil) |
| 20,85–23,97 | Zaman çizgisi (y 650): 1911 noktası ve `war` noktası, aralarında `3 years` köprüsü; `In 1911` (20,85) → `belirli zaman` (22,21); sağda `Simple Past` kutusu (23,65) |
| 25,05–26,69 | İki satır Fredoka 72: `win → won` (25,05) · `begin → began` (25,65); Caveat `düzensiz` (26,37) sarı |
| 27,40–32,20 | Tuzak: Caveat `Tuzak:` kırmızı (27,40); satır `begin · began · begun` (28,52 · 29,04 · 29,92); `began` sarı daire, `begun` (31,32) kırmızı çizili |
| 32,20–33,15 | Durgun |

### 04 Örnek 2 — kök 2 (düz canvas, 487 kare, t 33,15–48,99; cümle 4). Yerel kare = (t − 33,15) × 30
| sn | Hareket |
|---|---|
| 33,15–34,19 | Daire içinde `2` |
| 34,36–37,80 | Fredoka 56 iki satır: `We used to live in a village, and we would walk to school every morning.` sözcük sözcük; `used to` (34,52–35,08) ve `would` (36,12) farklı el çizimi kutu |
| 34,5–37,8 | Sağ: ev (home, 320 px) ile okul (school, 320 px) arasında kalemle yol; figür (standing-4) yolda yürür |
| 39,01–41,73 | İki etiket Caveat 48: `durum` (durumu 39,81) + `alışkanlık` (40,93); ok → takvim, üstü çizili `artık yok` |
| 42,44–47,72 | İki kutu: `would + walk` ✓ (45,44–46,04) ve `would + live` ✗ (46,92–47,72, kırmızı çizgi); Caveat `durum fiili → used to` |
| 47,72–48,99 | Durgun |

### 05 Örnek 3 — kök 3, asıl tuzak (düz canvas, 528 kare, t 48,99–66,19; çıkış fade). Yerel kare = (t − 48,99) × 30
| sn | Hareket |
|---|---|
| 48,99–50,0 | Daire içinde `3`; `TRAP` Fredoka 110 kırmızı, ölçek 0,6→1 taşmalı (vurus 50,51) |
| 51,32–55,64 | Fredoka 56 iki satır: `The manager resigned two weeks ago, and the board has not found a replacement yet.` sözcük sözcük; `ago` (52,92) ve `yet` (55,32) sarı alt çizgi |
| 56,45–59,81 | Sol çizim: takvim (calendar) + kapalı nokta `two weeks ago`; `resigned` (56,45) sarı daire; `ago` (57,65); etiket `Simple Past` (59,49) |
| 60,84–65,32 | Sağ çizim: saat (clock) + `now`'a uzanan ok; `has not found` (60,84) sarı daire; `yet` (62,60); etiket `Present Perfect` (64,76) |
| 65,32–66,19 | Durgun |

### 06 Soru + Form (HyperFrames, 791 kare, t 66,19–91,54; cümle 6 öğrenci = 66,19–70,51, cümle 7 öğretmen = 71,06–90,54)
| sn | Hareket |
|---|---|
| 66,19–70,51 | Künye `Question`. Sol: öğrenci BAŞI (peeps-kit ogrenci-bas.svg) + el çizimi balon; Fredoka 600 44: `Hocam, ago varken has resigned yazsam olmaz mıydı?` Sağda `has resigned + ago` (68,43) üstüne kırmızı çarpı (69,47) |
| 71,06–71,9 | Künye `Form`. `Olmaz.` Fredoka 160 kırmızı vurgu (vurus 71,06); balon ve baş küçülüp yukarı kayar (alfa 0,45) |
| 72,11–75,15 | Fredoka 56 kart: `A definite time word blocks the present perfect.` sözcük sözcük; `blocks` (73,47) sarı |
| 75,56–79,88 | Sol sütun etiketler: `ago` (75,56) · `last year` (76,44) · `in 1911` (77,72), her biri tik; Caveat `belirli zaman` (79,16) sarı |
| 80,44–83,12 | Sağ sütun: `for` (81,40) · `since` (81,96) · `yet` (82,52) → kutu `Present Perfect` (80,44) |
| 83,97–85,2 | Fredoka 72: `Did not resign.` (Did 83,97 · resign 84,53); `Did` sarı |
| 85,90–90,54 | Kod kartı el kutusunda: `ago → Past` (ago 86,86 · Past 87,90) ve `since → Perfect` (since 88,86 · Perfect 89,82), oklar kalemle |
| 90,54 | Formül kartı toplanır: `V2 · did + V1` (tik); 90,9 sağ alt ajandanın üstünde `Next lesson →` Lexend 24 ikincil |
| 90,54–91,54 | Durgun (1 sn kuyruk) |

## 5. Çalıştırma (her sahne kendi `calistir.sh`; paket kökünden)
- Canvas/Paper.js: `python3 ortak/yakala.py projeler/simple-past-ileri/sahneler/<klasor>/sayfa.html "$KARE"` →
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
| Harita | `/p/simple-past-ileri/harita.html?ac=02,02-10,02-10-ydt-ileri&sec=<kimlik>` |
| Editör | `/p/simple-past-ileri/onizle.html?surum=ana-yatay&t=0&tema=acik&yan=1&yol=02,02-10,02-10-ydt-ileri` |
| API | `/api/simple-past-ileri/{gorevler,surumler,yorumlar,konum}` |
| Eski adres | `/projeler/simple-past-ileri/{harita,onizle}.html` → 302, sorgu korunur |
