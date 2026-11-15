# RAPOR — 02-04-ydt-temel-s3 · sahne 02-hyperframes-ornek (değer, HyperFrames 1080×1920, 402 kare) · huni v2 · 15.11.2026

| Alan | Durum |
|---|---|
| QA (`qa-yerel.sh … 3.0,9.5,15.96 13.5 --hazirla`) | **çıkış 0** (3 koşu; son koşu son kodla) |
| Çakışma kapısı | `02-hyperframes-ornek \| çakışma yok (53 örnek, 27834 kutu)` → 0 uyarı |
| `uret.py` / `olay.py` | çıkış 0; `Y.kontrol` geçti; 86 komut, 34 ses olayı (18 cizgi); SPEC §6 bekçileri (7 grup) geçti |
| Kanal katmanı | 4 karede görünür, konum aynı (§3) |
| Metin taraması `tam ders\|dakika` (`proje/`) | sonuç yok |
| Render | YOK (`ONIZLE_YALNIZ=1`) |
| Kod yolu | şef `SPEC.md` (v2) → `agy-filo tek --rol kod` (`uret.py`) → şef okudu + 3 düzeltme turu (Edit, §5) |

## 1. Değişen dosyalar (yalnız bu sahne dizini)

| Dosya | Değişiklik |
|---|---|
| `SPEC.md` | v2 tasarımı (şef); v1 yedeği `~/Silinecekler/2026-11-15-huni-v2/…/sahneler-v1/02-hyperframes-ornek/` |
| `uret.py` | agy (SPEC v2) + şef Edit'leri: v2 yerleşim sabitleri, `kunye_v2()`, kanal katmanı (`#logo > #kanal`), `altyazi_v2_svg()` (x 510, ≤ 900), bekçiler |
| `yardim.py` | `altyazi_dilimleri(cumleler, gen=None)`: satır genişliği parametresi (şef, 2 satır) |
| `calistir.sh` | yalnız açıklama satırı (yerleşim kaynağı huni v2) |
| `RAPOR.md` | bu belge |

## 2. Olay listesi (küresel sn = yerel + 3,00; çapa `sozcukler.json`, zamanlar v1 ile aynı)

| Küresel sn | Sözcük çapası | Olay |
|---|---|---|
| 3,00 | — | kare 0: kanal + künye + kart 1 (`The train to İzmir` / `leaves at 7`) + tren köşede + altyazı dilimi 0 |
| 3,40 · 3,52 | `p.m.` 3,00 · `today.` 3,40 | `pm`, `today.` (ilk 12 kare geçiş altında; `pm` 3,40'a kayar) |
| 3,52–4,45 | `today.` | eksen 72→948 (y 848), now (120), `7 pm` çentik + nokta (320), now → `7 pm` kalem oku, `7 pm` sarı daire (`isaret`) 4,10, `gelecek · V-s` 4,15 |
| 4,15–5,93 | `I` 4,45 … `tonight.` 5,93 | kart 2 çerçevesi (966–1220); `I am going to the` / `movie theater tonight.` sözcük sözcük; bilet `movie` 5,29 |
| 5,93–6,40 | `tonight.` 5,93 | `tonight` noktası (732) + etiket + `gelecek · am + V-ing` |
| 6,50 · 6,58 | `Hocam,` − 0,50 / − 0,42 | zaman çizgisi söner; kart 2 −132 (834–1088) |
| 6,90–10,33 | `Hocam,` 7,00 … `yok?` 10,33 | öğrenci başı, balon (256–954 × 1112–1372), soru sözcük sözcük (3 satır, Fredoka 600 64) |
| 9,72 · 9,86 | `Neden` 9,72 | sarı nokta balon üstünde (767, 1112) → sarı bağ kart 1 `leaves` altına (x 767 koridoru, y 704) |
| 10,76–11,51 | — | DURAKLAMA (olay yok) |
| 11,51 · 11,55 | `Planı` 11,51 | balon + baş söner; öğretmen kalemle (72–155 × 1110–1376) |
| 12,07 · 12,47 | `bir` 12,07 | sarı ok el → `am going` sütunu; `am going` sarı altçizgi (y 961) |
| 12,31 · 12,51 | `kişi` · `yapar.` | `person` → `plan` (x 300, taban 1172) |
| 13,43 | `Tren` 13,43 | önceki sarılar griye; sarı tren bağı (819,5; 594,5) → `leaves` altına |
| 13,53 · 13,83 | `Tren` · `tarifeye` 13,83 | `train` → `timetable` (kart 1 altı, taban 792) |
| 15,19 | `geniş` 15,19 | tren bağı griye; `leaves` sarı altçizgi (odak, y 684). Son hareket 15,49; durgun kuyruk |

Aynı anda tek sarı içerik kümesi: `7 pm` dairesi → bağ `cn` → ok + `am going` → tren bağı → `leaves` (geçişte 0,25 sn çapraz solma).

## 3. Kanal katmanı konumu

| Ölçüm | Değer |
|---|---|
| DOM | `image#logoimg` x 53,2 · y 291 · 193,5 × 48 (görünür sol kenar 60) · `text#kanal-ad` `@ydspublishing` Lexend 700 42, x 263, taban 330; ikisi `#logo > #kanal` içinde, hareket komutu yok |
| Piksel (açık 3,00 · 9,50 · 15,96) | üçünde de aynı kutu: x 107–596, y 290–340 (açık temada sarı `yds` harfleri ölçüm eşiğinin altında; logo görünür) |
| Piksel (koyu 13,50) | x 61–596, y 286–344 (bulanık zemin kestirimi ±4 px) |
| Boş bantlar (4 kare) | y 0–280 boş · y 1570–1920 boş · x > 960 (y 452–1392) boş |
| Diğer bantlar | künye y 396–439 (açık) · içerik x 59–958, y 461–1377 · altyazı y 1426–1529, x 84–936 |

İçerik sol ucu x 59: kart çerçevesi taşması (kutu titreşimi + çizgi + kenar yumuşatma 1 px).

## 4. Kart 1 devir karşılaştırması (sahne 01 → 02)

İş sırasında sahne 01 `devir.json` v1'di (12:58); değerler önce sahne 01 `SPEC.md` v2'sine (18:54) çekildi. Sahne 01 `devir.json`
v2'yi 19:01'de yazdı; son karşılaştırma onunla:

| Öğe | Sahne 01 `devir.json` v2 (19:01) | Sahne 02 kare 0 | Sonuç |
|---|---|---|---|
| Kart 1 satırları | Fredoka 700 64, kerning none, sol 97, taban [568, 666], görünen `The train to İzmir` / `leaves at 7` | aynı | eşit |
| Kart 1 çerçevesi | x 71, y 472, w 878, h 254, tohum 71, çizgi 4 | `kutu(71, 472, 878, 254, 71)`, çizgi 4 | eşit |
| Tren | kutu [712, 494, 927, 586] (tam sayı), ölçek 0,5 | `translate(717 506.5) scale(0.5)` → [712, 494,5, 927, 585,5] | eşit (yuvarlama) |
| Künye | konu 34, taban 420, rozet [664,6; 386; 203,6; 48] | aynı (rozet x 664,6, w 203,6) | eşit |
| Altyazı | x 510, boy 44, taban [1490] | aynı | eşit |
| Kanal | logo [53,15; 291; 193,49; 48], yazı x 263, taban 330, Lexend 700 42 | logo [53,2; 291; 193,5; 48], aynı yazı | 0,05 px fark (istem değeri 53,2) |

## 5. Bakılan kareler ve bulgu

| Kare | Bulgu | Sonuç |
|---|---|---|
| `k/…-3.png` (kare 0) | kanal, künye (34 px + rozet), kart 1 iki satır, tren köşede, altyazı tek satır; taşma yok | geçti |
| `/tmp/…/qa-ek/…-6.4.png` (ek) | ilk koşuda iki alt etiket arası 28 px: `gelecek · V-s gelecek · am + V-ing` tek satır gibi okunuyordu | DÜZELTİLDİ: noktalar 130/350/726 → 120/320/732, ara ≈ 65 px; `V-ing` kuyruğu x ≈ 950 |
| `k/…-9.5.png` | kart 2 yukarıda, balon 2 satır, baş; balon sağ ucu ≈ 955 | geçti |
| `/tmp/…/qa-ek/…-10.5.png` (ek) | sarı bağ `tonight.` ile bilet arasından (≈ 13 px) geçer, ucu `leaves` altında | geçti |
| `k/…-15.96.png` | son düzen: `leaves` sarı, griler, iki etiket, öğretmen; altyazı 2 satır bantta | geçti |
| `k/koyu/…-13.5.png` | koyu temada kontrast okunur; tren bağı başlarken eski sarılar söner (0,25 sn) | geçti |

Şef düzeltmeleri (Edit): kart 1 / tren / altyazı tabanı / künye ayrıntısı sahne 01 SPEC v2'ye eşlendi · tren dönüşümü `:g` biçimi (506,5 yuvarlanmasın) ·
bekçi 1 sınırları sabitlerden · zaman çizgisi noktaları (yukarıdaki satır).

## 6. agy koşu özeti

`/home/sef/.claude/canavar/agy-filo/20261115-185256/ozet.md` — rol kod, gemini-3.8-flash-high, başarılı, 224 sn; girdi 1.436.606 / çıktı 141.038 token.
Özetin "değişen" listesi bütün çalışma ağacını tarar (paralel oturumların dosyaları); agy yalnız `uret.py`'yi yazdı (mtime 18:56).

## 7. Açık noktalar

1. Kare 0 sahne 01 `devir.json` v2 (19:01) ile eşit; sahne 01 kendi QA'sında devri değiştirirse yeniden karşılaştır. Logo x 53,2 ↔ 53,15 (0,05 px).
2. `k/` içinde v1'den kalan 6 kare var (4 · 6,6 · 9,95 · 10,9 · 12,2 · 15,9): `qa-yerel.sh` `~/qa-kare/<paket>/<sahne>/` dizininin tamamını kopyalar. Silme yok; güncel kareler 3 · 9,5 · 15,96 · koyu 13,5.
3. Faz C'de öğretmen 266 px (v1 380): kart 2 B altı ile 1380 arasına sığan boy. Sağ alt (x 650–960, y 1100–1380) boş kalır.
4. Bilet ölçeği 0,55 → 0,40: sarı bağ koridoru (x 767) `tonight.` sonu ile bilet arasında ≥ 13 px açıklık ister.
5. Rozet iç boşluğu (20 + 20) ve yazı tabanı (419,4) standartta yok; sahne 01 SPEC'iyle aynı seçildi.
6. Karaoke: v1 kararı sürer (alt bantta düz altyazı; okunan sözcük kartta sözcük sözcük yazımla verilir).
