# Simple Present — paket 05.11 "kalem" (YDT temel, Doğan Hoca anlatımı)

Amaç: Nadir'in konuşmalar boyunca istediği görsel dili kalem motorlarıyla GÖSTERMEK. Çıktı `cikti.mp4` (1920×1080, 30 fps, ≈93 sn) + `kontrol.png`. Anlatım hazır: `ortak/anlatim/anlatim.wav` (soğuk açılış: ilk söz 1,00 sn).
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
| 1 | 01-hyperframes-giris | HyperFrames | 102 | 0,00–3,00 | cümle 1 (1.00–2.76) |
| 2 | 02-paperjs-kanca | Paper.js | 386 | 3,00–15,45 | cümle 2 |
| 3 | 03-paperjs-ornek1 | Paper.js | 379 | 15,45–27,69 | cümle 3 |
| 4 | 04-canvas-ornek2 | düz canvas | 482 | 27,69–43,36 | cümle 4 |
| 5 | 05-canvas-ornek3 | düz canvas | 525 | 43,36–60,47 | cümle 5 |
| 6 | 06-hyperframes-form | HyperFrames | 1020 | 60,47–93,47 | cümle 6 (öğrenci) + 7 |

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
| Sol üst | `SIMPLE PRESENT` + ` · YDT BASIC` | x 56, taban y 72; Fredoka 700 30 px; Lexend 500 22 px, 14 px boşluk | krem / ikincil |
| Sağ üst | bölüm adı: `Hook` · `Example 1 / 3` · `Example 2 / 3` · `Example 3 / 3` · `Question` → `Form` | sağ kenar x 1864, taban 72; Lexend 700 24 px | vurgu |
| Sol alt | logo svg | x 56, yükseklik 34 px (en ≈ 137), alt kenar y 1036 | logonun kendi renkleri |
| Sağ alt | ajanda `Hook  Examples  Form`, etkin olan sarı + 4 px nokta solunda | sağ kenar 1864, taban 1030; Lexend 500 20 px, 36 px aralık | ikincil / vurgu |

Canvas: `ortak/kunye.js` → `kunyeHazirla()`, `zeminCiz(ctx, f, K)`, `kunyeCiz(ctx, {bolum, etkin, logo})`.
HyperFrames: aynı sayılar CSS'te; sahne 01'in uçuş hedefleri bu tablodur (bitişte piksel piksel aynı görünmeli).

## 4. Sahne sözleşmeleri (küresel saniye; yerel kare = round((t − t_bas) × 30); satır zamanı sözcük başlangıcından)

### 01 Giriş — soğuk açılış (HyperFrames, 102 kare, t 0,00–3,00; kapak kalıbı, cümle 1 burada konuşulur)
| küresel sn | Hareket |
|---|---|
| 0,00–0,40 | Logo damgası sol sütun altında (110 px, x 96, y ≈ 880): ölçek 1,18→1,0 + dönme −2°→0 (vurus kare 3) |
| 0,30–0,90 | Rozet hapları: `YDT · BASIC`, `GRAMMAR` (stagger 0,1) |
| 0,00–2,20 | Başlık kalemle çizilir: `SIMPLE` 0,0–1,1, `PRESENT` 1,0–2,2; Fredoka 700 140. Kalem sesi kare 0 |
| 0,20–2,30 | Sağ sütun: ayakta figür `open-peeps/standing-3.svg` 0,2–2,0, saat `tabler/clock.svg` 1,6–2,2 |
| 1,00–2,76 | Başlığın altında (x 96, y 650) Caveat 700 64: `Her sabah yedide kalkarım.` sözcük sözcük (`sozcukler.json`) |
| 2,20–3,00 | UÇUŞ: başlık → sol üst künye; logo → sol alt; eskiz solar; ajanda belirir |

### 02 Kanca (Paper.js, 386 kare, t 3,00–15,45)
| küresel sn | Hareket |
|---|---|
| 3,00–3,71 | Cümle 1 yazısı hazır (Caveat 64, x 140, y 300). Sağda eskiz: yatak `coco/bed.svg` (300 px) + saat `coco/clock.svg` + ayakta figür `open-peeps/standing-1.svg` |
| 5,71–7,77 | `kalkar` · `gider` · `yapar` sırayla sarı daire; Caveat not `geniş zaman` (ok → saat) |
| 9,30–10,42 | Altına Fredoka 56: `Simple Present` yazılır; iki yönlü kalem oku `geniş zaman ⇄ Simple Present` |
| 10,65–15,45 | Alt sağ el çizimi kutu, 3 madde tik zamanlı: `form` 11,61 · `time expressions` 12,41 · `uses` 13,77; küçük saat `tabler/clock.svg` `6 min` |

### 03 Örnek 1 (Paper.js, 379 kare, t 15,45–27,69)
| küresel sn | Hareket |
|---|---|
| 16,00–17,21 | Daire içinde `1` (x 140, y 200) |
| 17,21–18,65 | Fredoka 64: `The sun rises in the east.` sözcük sözcük (x 140, y 320, 2 satır) + sarı alt çizgi kayar |
| 17,21–19,45 | Sağ: güneş `coco/sun.svg` (420 px) ufuk çizgisinin üstünde; ok `east` (Caveat) kalemle |
| 19,86–21,94 | Caveat 48: `Güneş doğudan doğar.`; etiket `doğa kanunu` el kutusunda |
| 24,93–27,01 | `rises` sarı daire; sonundaki `s` ayrı sarı daire |
| 27,01–27,69 | Formül kartı (el kutusu): `it + V-s` → `rise-s`; durgun |

### 04 Örnek 2 (düz canvas, 482 kare, t 27,69–43,36)
| küresel sn | Hareket |
|---|---|
| 28,24–29,53 | Daire içinde `2` |
| 29,53–32,01 | Fredoka 64: `My brother usually goes to school by bus.` sözcük sözcük + sarı alt çizgi; `usually` ayrıca sarı |
| 29,53–32,81 | Sağ: oturan figür `open-peeps/sitting-4.svg` + otobüs `coco/bus.svg` (420 px) |
| 32,74–38,53 | Caveat 48: `Kardeşim genellikle okula otobüsle gider.` |
| 35,53–41,36 | Etiketler el kutusunda tik: `usually` · `always` · `every day`; altında 5 küçük gün kutusu (el çizimi) |
| 40,96–43,36 | `goes` sarı daire; formül kartı: `he + go` → `go-es` |

### 05 Örnek 3 (düz canvas, 525 kare, t 43,36–60,47, çıkış fade)
| küresel sn | Hareket |
|---|---|
| 43,91–45,20 | Daire içinde `3` |
| 45,20–46,48 | Fredoka 64: `Our plane takes off at nine tomorrow.` sözcük sözcük + sarı alt çizgi |
| 45,20–47,60 | Sağ: uçak `coco/plane.svg` (440 px) kalkış yayı; takvim `tabler/calendar.svg` + Caveat `tomorrow` |
| 48,01–52,01 | Caveat 48: `Uçağımız yarın dokuzda kalkar.` |
| 52,88–56,32 | Tarife tablosu (el çizimi kutu): `09:00  takes off`; etiketler `tarife` · `program` · `takvim` tik |
| 57,99–60,47 | `takes off` sarı daire; formül kartı `it + V-s`; çıkış fade |

### 06 Soru + Form (HyperFrames, 1020 kare, t 60,47–93,47)
| küresel sn | Hareket |
|---|---|
| 61,02–65,18 | Künye sağ üst `Question`. Sol: öğrenci başı `peeps-kit/ogrenci-bas.svg` + el çizimi konuşma balonu; Fredoka 600 44: `Hocam, üçünde de fiilin sonunda s var. Neden hep s?` Sağ: `rise-s` · `go-es` · `take-s` dikey, `s` sarı (cümle 6 sonunda) |
| 65,73–68,46 | Künye `Form`. Üç `s` tek büyük `s`'e toplanır (Fredoka 160 sarı); balon ve baş küçülür, yukarı kayar |
| 68,46–72,55 | `he · she · it` Fredoka 96 (sözcük zamanlı) + `+ V-s` |
| 72,55–77,74 | `I · you · we · they + go` (s YOK) altında soluk; kırmızı çizgi `s` üstünden |
| 77,74–85,60 | Kart: `He does not go.` / `Does he go?` — `does` sarı; `s` oka bağlanıp does'a geçer |
| 85,60–87,75 | Alt: Caveat 56 `git-er  =  go-es`, `er` ve `es` sarı; `=` kalemle çizilir |
| 87,75–93,47 | Formül kartı toplanır: `always · usually · every day → Simple Present` (tik); sağ alt `Next lesson →`; son 1 sn durgun |

## 5. Çalıştırma (her sahne kendi `calistir.sh`; paket kökünden)
- Canvas/Paper.js: `python3 ortak/yakala.py projeler/simple-present-temel/sahneler/<klasor>/sayfa.html "$KARE"` →
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
| Harita | `/p/simple-present-temel/harita.html?ac=02,02-04,02-04-ydt-temel&sec=<kimlik>` |
| Editör | `/p/simple-present-temel/onizle.html?surum=ana-yatay&t=0&tema=acik&yan=1&yol=02,02-04,02-04-ydt-temel` |
| API | `/api/simple-present-temel/{gorevler,surumler,yorumlar,konum}` |
| Eski adres | `/projeler/simple-present-temel/{harita,onizle}.html` → 302, sorgu korunur |
