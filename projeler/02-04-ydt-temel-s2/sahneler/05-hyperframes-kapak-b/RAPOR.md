# Sahne 05 — Kapak B (soru) · 02-04-ydt-temel-s2 · HyperFrames DİKEY 1080×1920 · tek kare, ses yok · 15.11.2026

Tema: acik (teslim) + koyu (kopya)

| Alan | Durum |
|---|---|
| Teslim | `P/kapak-b.png` (açık, 1080×1920) · `k/koyu/kapak-b-koyu.png` (koyu, 1080×1920) |
| Önizleme | `ONIZLE_YALNIZ=1 bash calistir.sh` → "önizleme hazır", rc 0 (`S=132 TT=100 fs=0.43522`) |
| Tek kare | `bash calistir.sh --tema acik` rc 0 · `--tema koyu` rc 0; ffprobe `png,1080,1920` (iki dosya) |
| Kapı | qa-yerel / çakışma kapısı koşulmadı (sahne `zaman.json` → `duragan`; araç `sahneler[]` dışını görmez). Kapı = `uret.py` iç assert'leri (SPEC §6: blok kesişimi, boşluklar, yazı boyu, hex beyaz listesi, yasak sözcükler) — geçti |
| Üretim yolu | şef `SPEC.md` → `agy-filo tek --rol kod` (gemini-3.8-flash-high, 294 sn) `uret.py` yazdı → şef baştan sona okudu, SPEC'e uyuyor; düzeltme 0 |
| agy özeti | `/home/sef/.claude/canavar/agy-filo/20261115-125443/ozet.md` (1/1 başarılı; "değişen 58" listesi bütün ağacı tarar, paralel oturumların dosyaları) |
| Düzeltme turu | 0 / 4 |
| Dosyalar | `uret.py` (agy) · `SPEC.md` · `cizim/ogretmen-dusunen.json`, `cizim/question-mark.svg`, `cizim/KAYNAK.md` (şef) · `calistir.sh`, `olay.py`, `zamanlar.json`, `yardim.py` (S1 sahne 05 kopyası; calistir.sh paket adı, yardim.py docstring) · `nesneler.json`, `olaylar.json` (üretilen) |

## Olay listesi
Durağan kare; olay yok (`olaylar.json` = `[]`). Çizelge 1,0 sn, yakalama 0,5 sn (`zamanlar.json`). Ses ve sözcük zamanı kullanılmaz.

| Öğe | Yer (px) | Not |
|---|---|---|
| logo | x 48, y 48, h 96 | HUD sol üst (aşağıda açık nokta 1) |
| rozet `YDT · BASIC` | x 48, y 216, h 72 | künye hapı (vurgu dolgusu, açıkta `#ffe066`) |
| başlık `TODAY VARSA` / `HANGİ ZAMAN?` | taban 495 / 661; x 85–995 / 65–1015 | Fredoka 700 S = 132 (952'ye sığan en büyük; g2 950); mürekkep + zemin kontur 12; hapsız; `İ` noktalı |
| takvim yaprağı | ≈ x 386–713, y 757–1116; +4° | Tabler `calendar` (rakam yolları yok), 300 × 300; sol alt köşe yumruğun arkasında |
| `today` | Caveat 700 100, takvim gövdesinde | küçük harf, mürekkep |
| öğretmen (büst) | x 64–455, y 864–1344 (480 px) | peeps-kit `PointingUp` + `Short` + `Smile`, dolgu çizimi; el çene hizasında, parmak yukarıda, yaprağı tutar |
| `?` | ≈ x 758–1000, y 890–1294 | Tabler `question-mark`, q 27, çizgi 26 px, round uç; TEK vurgu (`stroke` vurgu → açıkta `#d9900f`) |
| zemin çizgisi | y 1344, x 64–1016 | masa kenarı; büst alt kenarı burada |
| 1344–1536 · 1536–1920 | boş | altyazı yok (ses yok), platform boş |

## Bakılan kareler ve bulgu
| Kare | Bakılan | Bulgu |
|---|---|---|
| `k/at-0.5s.png` = `P/kapak-b.png` (açık) | taşma, kesik yazı, üst üste binme, kontrast, boş kare, alt bant | sorun yok. Başlık iki satır aynı boy, kenar payı ≥ 64; takvim ile baş arası ≈ 50 px; takvim ile `?` arası ≈ 45 px; 1344 altı boş |
| `k/koyu/kapak-b-koyu.png` (koyu) | aynı | sorun yok; figür ters baskı (krem dolgu), `.dz` örtücü dolgu koyu zeminde de doğru |
| yakın kırpım (x 330–720, y 960–1180), iki tema | yumruk–yaprak kesişimi | parmak ve yumruk yaprağın sol kenarını ve alt köşesini örter; çizgi elin içinden geçmez (tutma okunur) |

## Açık noktalar
1. **Logo yeri:** BRIEF-S2 ve `kapak-taslak.md` §4 "logo sol alt y ≈ 1478" der; BRIEF-DIKEY §0 (Nadir bulgusu) "logo HUD sol üst, alt bantta logo yok"
   der. Nadir bulgusu uygulandı (S1 kapak B, S2 kapak C ve `sozlesme.md` 02-04-s3 kapak B satırı ile aynı).
2. **"El çenede" pozu yok:** react-peeps kitinde 51 gövde tarandı, el-çene gövdesi yok; Open Peeps `standing-4..6` el çenede ama kadın görünümlü
   (K22: ses erkek). Seçilen `PointingUp`: el çene hizasında, işaret parmağı yukarıda; yaprağı bu el tutar. "Düşünme" işareti `?` ile verilir.
   Kadro farkı: gövde `ShirtPantsWB` değil `PointingUp`; saç (`Short`) ve yüz (`Smile`) kadroyla aynı. Gerçek el-çene pozu yeni kaynak ister (Higsfield IMAGE_RULE).
3. **Çizim tekniği:** figür S1 sahnelerindeki kontur yerine DOLGU ile çizildi (konturda kazak desenleri çift çizgi verir). Örtücü beyaz yollar
   `class="dz"` + `#root .dz{fill:var(--zemin,#1b1a17)}`: `hf_tema.py`'de path `fill` zemin eşlemesi yok.
4. **`?` rengi:** açık temada vurgu çizgisi `#d9900f` (temanın vurgu rengi); `#ffe066` yalnız hap dolgusudur, kâğıtta çizgi olarak okunmaz.
5. `__pycache__/` (yardim içe aktarımı) dizinde duruyor; silme yok kuralı gereği bırakıldı.
