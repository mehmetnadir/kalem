# Present Perfect Continuous — kalem paketi (YDT ileri, Doğan Hoca destesi unit-1_sunum-5) · `projeler/present-perfect-cont-ileri`

Amaç: ana örnek paketin (`../present-continuous/BRIEF.md`) görsel dilini bu konuya uygulamak. Çıktı `cikti.mp4`
(1920×1080, 30 fps, ≈86 sn). Anlatım hazır: `ortak/anlatim/anlatim.wav` (soğuk açılış: ilk söz 1,00 sn).
Metin ve zamanlar: `ortak/anlatim/METIN.md`, sözcük zamanları `ortak/anlatim/sozcukler.json` (küresel sn).
Kod `ING-YDT-GR-02-09-I`, rozet `YDT · ADVANCED`, ders adı `PRESENT PERFECT CONTINUOUS`. HUD'a sığmazsa ders adı `PRES. PERFECT CONT.`
olur (`ortak/kunye.js` `ders` alanı; sığma ölçülmedi, sahne ajanı kareye bakıp karar verir).
Seviye kuralı (ileri): tümdengelim — kural önce, sonra sınav kökü örnekleri, 1 tuzak (durum fiili); EN payı ≈ %40; öğrenci yanlış kavram sorar.

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
| 12 | Öğrenci sorusu (balon) | Sahne 06 ilk 3,78 sn |
| 13 | Ses tasarımı | Olay → Tone.js efekt (kalem hışırtısı, tık, sayfa) — `olaylar.json` |

Kapalı kararlar: DUR kartı yok · video ortasında soru kartı yok · QR bu prototipte yok (adres kararı bekliyor).


Konu notu: bu pakette 6 sahne ve 7 cümle ana paketle aynı sırada. Cümle 1 kanca (`Süreç mi, sonuç mu?`), cümle 6 öğrenci sorusu (`Hocam, have been knowing, olmaz mıydı?`). Çizim listesi yalnız `ortak/cizim/` içinde VAR OLAN dosyalardan kurulur (bkz. §4: sitting/standing figürleri, tabler ve coco nesneleri).

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
| 2 | 02-paperjs-kanca | Paper.js | 440 | 3,00–17,25 | cümle 2 |
| 3 | 03-paperjs-ornek1 | Paper.js | 505 | 17,25–33,68 | cümle 3 |
| 4 | 04-canvas-ornek2 | Düz canvas | 478 | 33,68–49,20 | cümle 4 |
| 5 | 05-canvas-ornek3 | Düz canvas | 392 | 49,20–61,87 | cümle 5 |
| 6 | 06-hyperframes-form | HyperFrames | 752 | 61,87–85,93 | cümle 6 (öğrenci) + 7 |

Cümle başları (sn): 1: 1,00 · 2: 3,39 · 3: 17,80 · 4: 34,23 · 5: 49,75 · 6: 62,42 · 7: 66,75. Anlatım biter 84,93; t_son = bitiş + 1,0. Sınır kuralı: sahne sınırı = sonraki cümle başı − 0,55 (spec §3.4).

## 2. Görsel dil (stil anayasası — bütün sahneler aynı)

### 2.1 Renk (yalnız bunlar)
**Render varsayılanı AÇIK tema (K19, 04.11)**; koyu kullanıcı seçimidir: `calistir.sh --tema koyu`, `birlestir.py --tema koyu` (`cikti-koyu.mp4`).
Açık palet: zemin `#f7f3ea` · mürekkep `#1b2440` · ikincil `#5a6275` · vurgu `#d9900f` · kırmızı `#d6453a`; logo `yds-publishing-lacivert.svg`. Aşağıdaki hex değerleri KOYU temadır.
zemin `#1b1a17` · mürekkep (krem) `#f3efe6` · ikincil `#c9c2b3` · vurgu sarı `#f2a93b` · logo sarısı `#fece00`
(yalnız logo ve giriş başlığı 2. satır) · kırmızı `#e0473b` (yalnız `know-ing` ve `have been knowing` üstü çizgisi).
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
| Sol üst | `PRESENT PERFECT CONTINUOUS` + ` · YDT ADVANCED` | x 56, taban y 72; Fredoka 700 30 px; Lexend 500 22 px, 14 px boşluk | krem / ikincil |
| Sağ üst | bölüm adı: `Hook` · `Example 1 / 3` · `Example 2 / 3` · `Example 3 / 3` · `Question` → `Form` | sağ kenar x 1864, taban 72; Lexend 700 24 px | vurgu |
| Sol alt | logo svg | x 56, yükseklik 34 px (en ≈ 137), alt kenar y 1036 | logonun kendi renkleri |
| Sağ alt | ajanda `Hook  Examples  Form`, etkin olan sarı + 4 px nokta solunda | sağ kenar 1864, taban 1030; Lexend 500 20 px, 36 px aralık | ikincil / vurgu |

Canvas: `ortak/kunye.js` → `kunyeHazirla()`, `zeminCiz(ctx, f, K)`, `kunyeCiz(ctx, {bolum, etkin, logo})`.
HyperFrames: aynı sayılar CSS'te; sahne 01'in uçuş hedefleri bu tablodur (bitişte piksel piksel aynı görünmeli).


Ders adı sığması: `PRESENT PERFECT CONTINUOUS` Fredoka 700 30 px ≈ 500 px (sol üst boşluk > 800 px): sığar. Dikeyde 56 px ≈ 900 px < 984: sınırda; sığmazsa `PRES. PERFECT CONT.`.

## 4. Sahne sözleşmeleri (küresel saniye; yerel kare = round((t − t_bas) × 30); sınırlar cümle başı − 0,55; hiçbir tablo eski çerçeve kaydırması taşımaz)

### 01 Giriş — soğuk açılış (HyperFrames, 102 kare, t 0,00–3,00; cümle 1)

Karar (Nadir 04.11, K23): giriş 3 sn, ilk söz ≤ 1 sn, kalem sesi 0. kareden. İçerik 3,0 sn (kare 0–90). Kanca kısa tutuldu (`Süreç mi, sonuç mu?`) ki giriş 3 sn içinde bitsin.
| sn | Hareket |
|---|---|
| 0,00–0,40 | Logo damgası sol sütun altında (110 px, x 96, y ≈ 880): ölçek 1,18→1,0 + dönme −2°→0, alfa 0→1 (vurus kare 3) |
| 0,30–0,90 | Rozet hapları: `YDT · ADVANCED`, `GRAMMAR` (stagger 0,1) |
| 0,00–2,20 | Başlık kalemle çizilir (soldan açılan kırpma): `PRESENT PERFECT` 0,0–1,1, `CONTINUOUS` 1,0–2,2; Fredoka 700 112 (en ≤ 1100; 15 harflik satır 140'a sığmaz). Kalem sesi kare 0 (cizgi + hisirti) |
| 0,20–2,30 | Sağ sütun: terazi yerine iki nesne: yarım okunmuş kitap (book) + saat (clock), stroke-dash |
| 1,00–2,92 | Başlığın altında (x 96, y 650) Caveat 700 64: `Süreç mi, sonuç mu?` sözcük sözcük |
| 2,20–3,00 | UÇUŞ: başlık → sol üst künye; logo → sol alt 34 px; eskiz solar (parilti); künye metinleri son 0,25 sn'de belirir; ajanda burada belirir |
| 3,00 | Künye yerleşik; cümle yerinde; son 12 kare BookFlip altında durgun |

### 02 Kural (Paper.js, 440 kare, t 3,00–17,25; cümle 2)

| sn | Hareket |
|---|---|
| 3,00–3,40 | Cümle 1 yazısı hazır: Caveat 64 sol üst `Süreç mi, sonuç mu?` |
| 3,39–5,79 | Merkezde el çizimi kural kartı (Fredoka 96, tümdengelim: kural önce); Caveat not `sınav bunu sorar` |
| 6,04–10,76 | Kart sözcük zamanında dolar: `have / has` (Have or has) · `+ been` (been) · `+ -ing` (-ing); üç parça farklı sarı daire sırayla |
| 10,69–16,85 | Alt sağ el çizimi kutu, 3 madde tik zamanlı: `form` (formunu) · `time clues` (ipuçlarını) · `2 traps` (tuzağı); küçük saat + süre etiketi (zaman.json) |

### 03 Örnek 1 — since + geçmiş yan cümle (Paper.js, 505 kare, t 17,25–33,68; cümle 3)

| sn | Hareket |
|---|---|
| 17,80–18,84 | Daire içinde `1` |
| 19,09–23,41 | Fredoka 64: `Since the school changed the timetable, students have been complaining.` sözcük sözcük (x 140, y 320, en ≤ 980, 3 satır) + sarı alt çizgi |
| 19,09–23,41 | Sağ: okul (school, 440 px) + öğrenci figürü (sitting-6) + takvim (calendar) kalemle |
| 19,89–20,21 | `Since … changed` sarı köşeli ayraç; Caveat `geçmiş yan cümle` |
| 21,81–23,41 | `have been complaining` ikinci sarı daire; Caveat `ana cümle` |
| 23,66–26,86 | Caveat 48: `Program değişeli beri öğrenciler yakınıyor.` |
| 27,11–30,07 | Zaman çizgisi (y 620): `changed` noktası → ok → `now` nabız; üstte `since` yayı |
| 30,32–33,68 | Kural kartı (alt): `since + past simple, have been + V-ing` tik |

### 04 Örnek 2 — süreç ve sonuç (düz canvas, 478 kare, t 33,68–49,20; cümle 4)

| sn | Hareket |
|---|---|
| 34,23–35,27 | Daire içinde `2` |
| 35,52–40,24 | Fredoka 56: `I have been reading this novel all week, but I have only finished two chapters.` sözcük sözcük (3 satır) |
| 35,52–40,24 | Sağ: roman (book, 440 px) + okuyan figür (sitting-1); `all week` altı sarı çizgi |
| 35,84–37,95 | `have been reading` sarı daire; kalem oku → Caveat `process` |
| 38,56–40,24 | `have only finished two chapters` ikinci daire (tik); Caveat `result` |
| 40,41–44,57 | Caveat 48: `Bütün hafta okuyorum, ama yalnızca iki bölümü bitirdim.` |
| 44,72–49,20 | İki sütunlu el kartı: `PROCESS  been reading` · `RESULT  have finished + sayı`; sözcük zamanında dolar |

### 05 Örnek 3 — tuzak: durum fiili (düz canvas, 392 kare, t 49,20–61,87; cümle 5; çıkış fade)

| sn | Hareket |
|---|---|
| 49,75–50,79 | Daire içinde `3` + sarı Caveat etiket `TRAP` |
| 51,04–54,16 | Fredoka 56: `We have known each other since we were at primary school.` sözcük sözcük (3 satır) |
| 51,04–54,16 | Sağ: iki figür (sitting-2, sitting-7) + okul (school, 380 px) |
| 51,44–51,60 | `known` sarı daire; Caveat `have known`, `have been knowing` değil |
| 54,33–56,97 | Caveat 48: `İlkokuldan beri birbirimizi tanıyoruz.` |
| 57,22–59,38 | Kart `STATE VERB` el kutusunda; `know-ing` yazılır ve kırmızı tek çizgiyle üstü çizilir (kırmızı: bu çizgi) |
| 59,63–61,87 | Caveat `durum fiili: -ing yok`; `Present Perfect` etiketi tik |

### 06 Soru + Özet (HyperFrames, 752 kare, t 61,87–85,93; cümle 6 öğrenci, cümle 7 öğretmen)

| sn | Hareket |
|---|---|
| 62,42–66,20 | Künye sağ üst `Question`. Sol: öğrenci BAŞI + konuşma balonu; Fredoka 600 44: `Hocam, have been knowing olmaz mıydı?` Sağ: `have been knowing` yazılı |
| 66,75–69,79 | Künye `Form`. `have been knowing` kırmızı tek çizgiyle silinir; yanında `have known` tik; balon ve baş küçülür |
| 70,04–76,45 | İki sütunlu el kartı: `PROCESS  have / has been + V-ing` · `RESULT  have / has + V3`, sözcük zamanında dolar |
| 76,70–79,82 | Altında Caveat 56: `-yor → süreç`, `-di → sonuç` sarı oklar kartın iki sütununa |
| 79,97–85,01 | Kod kartı el kutusunda: `süreç varsa been var` · `sonuç varsa been yok` (tik, vurus); sağ altta küçük `Next lesson →` Lexend 24 ikincil |
| 85,01–85,93 | Durgun (1 sn kuyruk) |
## 5. Çalıştırma (her sahne kendi `calistir.sh`; paket kökünden)
- Canvas/Paper.js: `python3 ortak/yakala.py projeler/present-perfect-cont-ileri/sahneler/<klasor>/sayfa.html "$KARE"` →
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
| Harita | `/p/present-perfect-cont-ileri/harita.html?ac=02,02-09,02-09-ydt-ileri&sec=<kimlik>` |
| Editör | `/p/present-perfect-cont-ileri/onizle.html?surum=ana-yatay&t=0&tema=acik&yan=1&yol=02,02-09,02-09-ydt-ileri` |
| API | `/api/present-perfect-cont-ileri/{gorevler,surumler,yorumlar,konum}` |
| Eski adres | `/projeler/present-perfect-cont-ileri/{harita,onizle}.html` → 302, sorgu korunur |
