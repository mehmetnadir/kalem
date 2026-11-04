# Present Continuous — İLERİ seviye (YDT, tümdengelim: formül → 3 sınav kökü → 1 tuzak) · `projeler/present-continuous-ileri`

Amaç: temel sürümle AYNI kapsam, farklı derinlik. Ana görsel dil `../present-continuous/BRIEF.md` (prototip 4 "kalem") ile aynıdır;
bu BRIEF yalnız §0 (içerik özeti), §1 (sahne tablosu) ve §4 (sahne sözleşmeleri) değiştirir. Çıktı `cikti.mp4`
(1920×1080, 30 fps, 84.96 sn) + `kontrol.png`. Anlatım hazır: `ortak/anlatim/anlatim.wav` (soğuk açılış: ilk söz 1,00 sn).
Metin ve zamanlar: `ortak/anlatim/METIN.md`, sözcük zamanları `ortak/anlatim/sozcukler.json` (küresel sn), altyazı parçaları
`ortak/anlatim/altyazi.json` (21 parça). Senaryo: `ortak/anlatim/senaryo.json` (kaynak: `dijital-anlatim/pilot/grammar-tenses-01-ileri/`).

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


### İleri sürüm içerik özeti (bu videoda temelden FARKLI olan)
| Eksen | Temel | İleri (bu video) |
|---|---|---|
| Yön | 3 örnek → kural (tümevarım) | kural/formül önce, sonra 3 YDT kökü, sonra 1 tuzak (tümdengelim) |
| Örnek türü | günlük kısa cümle | uzun, bağlaçlı sınav kökü (while, because, so) |
| Tuzak | yok | durum fiilleri (know, believe, own, belong) -ing almaz; `always + V-ing` = şikâyet |
| Dil payı | TR anlatım, EN yalnız örnek | EN sözcük payı ≈ %42 (örnek + kısa EN kural cümleleri) |
| Öğrenci cümlesi | merak: "neden hep -ing?" | yanlış kavram: "I am knowing the answer olmaz mıydı?" |
| Rozet / künye | `YDT · BASIC` | `YDT · ADVANCED` (`PRESENT CONTINUOUS`) |
Sahne başına cümle: 01 → c1 · 02 → c2 · 03 → c3 · 04 → c4 · 05 → c5 · 06 → c6 (öğrenci) + c7.
Kırmızı bu videoda yalnız: tuzak ünlemi (sahne 02), yanlış cümlenin üstüne çarpı (sahne 06). Başka yerde kırmızı YOK.

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
| 1 | 01-hyperframes-giris | HyperFrames | 102 | 0.00–3.00 | cümle 1 (1,00–3,16) |
| 2 | 02-paperjs-kanca | Paper.js | 380 | 3.00–15.25 | cümle 2 (3,71–15,25) |
| 3 | 03-paperjs-ornek1 | Paper.js | 442 | 15.25–29.58 | cümle 3 (15,80–29,58) |
| 4 | 04-canvas-ornek2 | Düz canvas | 387 | 29.58–42.07 | cümle 4 (30,13–42,07) |
| 5 | 05-canvas-ornek3 | Düz canvas | 372 | 42.07–54.08 | cümle 5 (42,62–54,08) |
| 6 | 06-hyperframes-form | HyperFrames | 956 | 54.08–84.96 | cümle 6 (öğrenci, 54,63–59,85) + cümle 7 (60,40–83,96) |

Sahne sınırı = bir önceki cümlenin bitişi (= sonraki cümle başı − 0,55); son sahne = son söz + 1,0 sn. Cümle 1 sesi 3,16 sn'ye kadar sürer (sahne 01 içeriği 3,0 sn): `düşme.` sözcüğü 2,52'de başlar, yazı 3,0'dan önce yerinde olmalı.

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
| Sol üst | `PRESENT CONTINUOUS` + ` · YDT ADVANCED` | x 56, taban y 72; Fredoka 700 30 px; Lexend 500 22 px, 14 px boşluk | krem / ikincil |
| Sağ üst | bölüm adı: `Hook` · `Example 1 / 3` · `Example 2 / 3` · `Example 3 / 3` · `Question` → `Form` | sağ kenar x 1864, taban 72; Lexend 700 24 px | vurgu |
| Sol alt | logo svg | x 56, yükseklik 34 px (en ≈ 137), alt kenar y 1036 | logonun kendi renkleri |
| Sağ alt | ajanda `Hook  Examples  Form`, etkin olan sarı + 4 px nokta solunda | sağ kenar 1864, taban 1030; Lexend 500 20 px, 36 px aralık | ikincil / vurgu |

Canvas: `ortak/kunye.js` → `kunyeHazirla()`, `zeminCiz(ctx, f, K)`, `kunyeCiz(ctx, {bolum, etkin, logo})`.
HyperFrames: aynı sayılar CSS'te; sahne 01'in uçuş hedefleri bu tablodur (bitişte piksel piksel aynı görünmeli).


## 4. Sahne sözleşmeleri (yerel kare = round((t − t_bas) × 30); tablolardaki sn KÜRESELDİR)

Çizim kaynakları yalnız `ortak/cizim/` altındaki mevcut dosyalar: `tabler/` (phone, bus, home, calendar, clock, ...), `coco/` (rain, letter, ...),
`open-peeps/` (sitting-1..7, standing-1..6), `peeps-kit/ogrenci-bas.svg`. Çip adları: `Hook` · `Example 1 / 3` · `Example 2 / 3` ·
`Example 3 / 3` · `Question` → `Form`.

### 01 Giriş — soğuk açılış (HyperFrames, 102 kare, t 0–3,0; cümle 1 burada konuşulur; kapak kalıbı)
Temel sürümün sahne 01 kalıbı aynen (logo damgası, rozet hapları, başlık kalemle, uçuş, künye). Farklar:
| sn | Hareket |
|---|---|
| 0,3–0,9 | Rozet hapları `YDT · ADVANCED`, `GRAMMAR` |
| 0,0–2,2 | Başlık `PRESENT` / `CONTINUOUS` kalemle (temeldeki gibi) |
| 0,2–2,3 | Sağ sütun: ayakta figür (standing-3) 0,2–2,0 + telefon (phone) 1,6–2,2 |
| 1,00–3,0 | Başlığın altında Caveat 64 krem: `YDT'nin -ing tuzağına düşme.` sözcük zamanlı: `YDT'nin` 1,00 · `-ing` 1,80 (sarı daire) · `tuzağına` 2,04 · `düşme.` 2,52 |
| 2,2–3,0 | UÇUŞ: başlık → sol üst künye; logo → sol alt; eskiz solar; ajanda belirir. Cümle yazısı sahne 02'ye hazır geçer |

### 02 Kanca + formül (Paper.js, 380 kare, t_bas 3,00; cümle 2)
| sn | Hareket |
|---|---|
| 3,00–3,71 | Cümle 1 yazısı yerinde (Caveat 64 krem, x 140, y 300); `-ing` sarı daire titrer |
| 3,71–5,07 | `Formül tek satır.` Caveat 48 `FORMÜL` etiketi; el kutusu çizilir (x 140–1280, y 420–660) |
| 5,32–10,68 | Kutu içinde sırayla: `Subject` (5,32, Caveat 64 `özne`) · `+` · `am` (6,84) `is` (7,68) `are` (8,32) Fredoka 110 · `+` (9,00) · `V-ing` (9,40, sarı daire). Sözcük zamanlı belirir |
| 10,93–12,57 | Altı dakika: saat (clock, 260 px, x 1450 y 300) kalemle; Caveat `6 min` |
| 12,57–14,05 | `üç sınav kökünü`: kutunun altında üç küçük el kutusu `1` `2` `3` (12,57 / 13,09 / 13,65), her biri tik |
| 14,05–15,25 | `bir tuzağı`: dördüncü kutu, kırmızı ünlem `!` ve Caveat `1 tuzak` (kırmızı yalnız burada); son 12 kare durgun |

### 03 Örnek 1 (Paper.js, 442 kare, t_bas 15,25; cümle 3) — çip `Example 1 / 3`
| sn | Hareket |
|---|---|
| 15,80–16,68 | Büyük el çizimi daire içinde `1` (x 140, y 200) |
| 16,93–22,05 | Fredoka 56, 3 satır, sözcük zamanlı (x 140, y 300, en ≤ 980): `Please be quiet! The baby is sleeping in the next room while I am talking on the phone.` `is sleeping` (18,69–19,01) ve `am talking` (20,40–20,49) sarı daire; `while` (20,13) sarı kutu |
| 16,9–20,0 | Sağ: telefonda konuşan figür (sitting-4) + telefon (phone, 300 px); ortada el çizimi duvar çizgisi; duvarın ardında küçük uyuyan figür (sitting-6) + Caveat `z z z` |
| 22,30–25,14 | Caveat 48 ikincil: `Bebek uyuyor, ben telefonda konuşuyorum.` (y 620) |
| 25,14–27,66 | Zaman çizgisi (y 760): `now` noktası nabız atar; üstünde iki paralel dalgalı sarı bant `is sleeping` / `am talking`; Caveat `iki iş de sürüyor` |
| 27,66–29,58 | `While` (27,66) sarı kutu → ok → `NOW`; formül kartı `be + V-ing` → `is sleep-ing` / `am talk-ing` (-ing sarı). Durgun son 12 kare |

### 04 Örnek 2 (düz canvas, 387 kare, t_bas 29,58; cümle 4) — çip `Example 2 / 3`
| sn | Hareket |
|---|---|
| 30,13–31,09 | Daire içinde `2` |
| 31,34–35,50 | Fredoka 56, 3 satır: `Because the roof is leaking, we are staying at my uncle's house this week.` `Because` (31,34) sarı alt çizgi; `is leaking` (32,14) ve `are staying` (33,02) sarı daire; `this week` (34,38–34,70) sarı köşeli ayraç |
| 31,3–35,0 | Sağ: ev (home, 420 px), çatısından 3 damla (rain, 150 px) kalemle; ok → ikinci küçük ev (home, 240 px) + Caveat `uncle's`; figür (sitting-7) küçük evin önünde |
| 35,75–38,87 | Caveat 48: `Çatı aktığı için bu hafta amcamlarda kalıyoruz.` (y 600) |
| 38,87–40,27 | `Geçici bir durum.`: takvim (calendar) şeridi 7 kutu, sarı ayraç `this week`, Caveat `geçici`; ok → `eve dönüş` |
| 40,27–42,07 | `This week bunu söyler.`: `this week` sarı daire; formül kartı `be + V-ing` → `is leak-ing` / `are stay-ing`. Durgun son 12 kare |

### 05 Örnek 3 (düz canvas, 372 kare, t_bas 42,07; cümle 5; çıkış fade) — çip `Example 3 / 3`
| sn | Hareket |
|---|---|
| 42,62–43,58 | Daire içinde `3` |
| 43,83–48,79 | Fredoka 56, 3 satır: `We are taking the bus to Izmir tomorrow morning, so I am packing my bag tonight.` `are taking` (43,99) ve `am packing` (46,98) sarı daire; `tomorrow morning` (45,43–45,83) sarı alt çizgi; `tonight` (47,83) sarı daire |
| 43,9–47,0 | Sağ: otobüs (bus, 460 px) kalemle, yanında yolcu figürü (standing-4); üstte takvim (calendar, 200 px) |
| 49,04–51,12 | Caveat 48: `Yarın sabah İzmir'e gidiyoruz.` |
| 51,12–52,20 | `Planlı gelecek.`: takvimde `yarın` sarı daire; ok → Caveat `PLAN` sarı |
| 52,20–54,08 | `Bilet alınmış, saat belli.`: el kutusu `bilet ✓` (52,40 tik) + saat (clock, 200 px) (53,04 tik); formül kartı `be + V-ing` → `are tak-ing` / `am pack-ing`. Durgun son 12 kare |

### 06 Soru + tuzak + kural (HyperFrames, 956 kare, t_bas 54,08; cümle 6 öğrenci, cümle 7 öğretmen)
| sn | Hareket |
|---|---|
| 54,63–59,85 | Künye sağ üst `Question`. Sol: öğrenci BAŞI (peeps-kit ogrenci-bas.svg; kadın ses = kadın çizim) + el çizimi konuşma balonu; Fredoka 600 44 sözcük zamanlı: `Hocam, bilmek de sürüyor. I am knowing the answer olmaz mıydı?` `I am knowing` (56,96–57,36) sarı alt çizgi |
| 60,40–61,60 | `Olmaz.`: balondaki `I am knowing the answer` üstüne kırmızı kalem çarpısı (kırmızı yalnız burada); künye `Form` |
| 61,60–66,04 | Sol sütun dikey liste Fredoka 96: `know` (61,60) · `believe` (62,32) · `own` (63,20) · `belong` (63,84); sağda el kutusu Caveat 64 `durum fiili` (64,64); `-ing` (65,80) sarı yazılır, üstüne kalemle çizgi/çarpı (`almaz`, 66,04) |
| 66,81–68,33 | Fredoka 64: `I know the answer.` (`know` sarı daire 66,97) |
| 68,58–73,14 | Köprü: Caveat 56 `biliyor-um` (69,22; `-yor` sarı) ↔ `I know` (70,26 ama) ; `know-ing` üstü çizili (`-ing` 71,38); Caveat `Türkçede -yor var, İngilizcede -ing yok` |
| 73,39–75,87 | Fredoka 64: `He is always losing his keys.` `always` (73,79) sarı alt çizgi, `losing` (74,27) daire; sağda figür (standing-5) ve el çizimi ünlem (sinir) |
| 76,12–79,92 | Caveat 56: `always + V-ing = şikâyet` (`Always` 76,12, `-ing` 77,32 sarı, `şikâyettir` 77,80 el altı çizgisi); `Sınavda ikisi de çıkar` (78,96): iki küçük kutu yan yana: `know / believe / own / belong` ve `always + V-ing` |
| 80,72–83,96 | `Kod:` (80,72) → Fredoka 150: `olay = -ing` (`olay` 81,48, `-ing` 81,88 sarı) alt satır `durum ≠ -ing` (`durum` 82,92, `almaz` 83,32); `=` ve `≠` kalemle çizilir |
| 83,96–84,96 | Formül kartı el kutusunda toplanır: `am / is / are + V-ing` (tik); sağ alt ajanda üstünde `Next lesson →` Lexend 24 ikincil; 1 sn durgun kuyruk |

## 5. Çalıştırma (her sahne kendi `calistir.sh`; paket kökünden)
- Canvas/Paper.js: `python3 ortak/yakala.py projeler/present-continuous-ileri/sahneler/<klasor>/sayfa.html "$KARE"` →
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

