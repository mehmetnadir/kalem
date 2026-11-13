# 02-03 · Present Continuous ve Simple Present: ayrım alıştırması — YDT temel · `projeler/02-03-ydt-temel`

Durum: P1 tamam (anlatım + paket iskeleti). Sahneler P2'de yazılır. Render YOK (yalnız Nadir panelde işaretlerse).
Görsel dil: `../present-continuous/BRIEF.md` (kalem prototipi) ve `../present-continuous-ileri/BRIEF.md` §2–§4 ile aynı; bu BRIEF yalnız içerik, iskelet ve sahne planını verir.
Senaryo (jüri GEÇTİ, D-0204/D-0205): `/Users/nadir/01dev/kalem/_is/senaryo-taslak/02-03-ydt-temel.md` (+ `.juri.md`, `juri/02-03-ydt-temel.*.md`).

## 0. Künye

| Alan | Değer |
|---|---|
| Kimlik / kod | `02-03-ydt-temel` · `ING-YDT-GR-02-03-T` |
| Ders | GR-02-03 · Tenses (02) · Present Continuous ve Simple Present: ayrım alıştırması |
| Kitle / seviye | YDT · temel |
| Format | yatay 16:9, 1920×1080, 30 fps, tema açık (render varsayılanı) |
| Sesler | öğretmen Atakan `gsJ9nrlXYbPztJxC4fwc` · öğrenci Gökçe Deniz `oPC5I9GKjMReiaM29gjY` · eleven_v4 · HIZ_EN 0,9 |
| Kadro | öğrenci: kadın, genç, Sitting / Smile / LongBangs / GlassRound (ogrenci-bas.svg) |
| Süre iddiası | YOK (12.11 kararı); anlatım süresi `zaman.json` son sahne t_son |

## 1. Kaynak

| Kaynak | Yol |
|---|---|
| pptx (slayt 2, 3, 4) | `/Users/nadir/01dev/dijital-anlatim/varlik/grammar/kaynak-pptx/YEDEK/Tenses/unit-1_sunum-2b uygun.pptx` |
| Döküm (Whisper; Vimeo 863572892) | `/Users/nadir/01dev/dijital-anlatim/varlik/grammar/transkript-whisper/863572892.md` |

Kaynak yalnız soru slaytlarını taşır (4 cümle + 9 boşluklu kartpostal); cevaplar ve nedenler dökümden gelir. Kaynakta olmayan kural eklenmedi.
D-0205 notu: believe/think için kategori etiketi YOK; "performative" yalnız recommend/promise/agree. these days / nowadays mutlak değil ("genellikle şimdiki zamanı çağırır").

## 2. İskelet (gerçekleşen süreler anlatım sesinden; ses 1,00 sn'de başlar)

| Bölüm | Cümleler | Hedef sn | Gerçek sn | Ekran metni | Görsel notu |
|---|---|---|---|---|---|
| 1 Kanca | 1–2 | 15 | 14,3 | ONE VERB · TWO TENSES / SIGNAL WORD; PRESENT CONTINUOUS vs SIMPLE PRESENT | Soğuk açılış (K23): `goes` ve `is going` iki kart, `SIGNAL WORD` sarı belirteç; başlık künyeye uçar; `vs` kalemle |
| 2 Örnekler (3) | 3–7 | 90 | 71,9 | 3 örnek cümle (leaving at 9 · these days · harder and harder nowadays); PLAN · CHANGING; soru anı 1 balonu | Tek kart/örnek; uçak, takvim ikonu; `harder and harder` sarı belirteç; öğrenci balonu + 0,75 sn duraklama; cevap 2 sn içinde |
| 3 Kural kartı | 8 | 45 | 21,3 | NOW → am/is/are + V-ing · THESE DAYS · NOWADAYS · PLAN → usually V-ing (temporary / changing) · USUALLY · GENERAL → V1 / V-s | `tanim` 3 satır kademeli; sinyal sözcükleri örnek kartlarına ince çizgiyle bağlı |
| 4 Karşıt çift | 9–11 | 60 | 57,4 | Nancy usually spends… / is meeting… now; I am staying ≠ package includes; offers ≠ are enjoying | `bag` okları, zaman çizgisi (alışkanlık noktaları / now nabzı); sol-sağ kartlar; TEMPORARY / GENERAL / RIGHT NOW |
| 5 Tuzak | 12–14 | 60 | 58,3 | We believe this situation is temporary · TRAP; soru anı 2; believe · think · have (own) → simple present · performative: promise · agree · recommend → NO -ing | `yaklas`, `believe` sarı daire, `-ing` üstü çarpı (sarı); `has` ve `recommend` kartları alt alta |
| 6 Ara özet | 15 | 20 | 15,3 | NOW · THESE DAYS / NOWADAYS → usually -ing · USUALLY / GENERAL → V1 · believe, have: no -ing | `ozet` 3 madde kademeli, bölüm perdesi yok |
| 7 Mini soru | 16–18 | 55 | 29,6 | I ____ this postcard now. A write · B am writing · C writes · D wrote · E is writing | `soru` kök + 5 şık, sayaç; yanlış cevap A (soluk sarı çerçeve); doğru B yeşil; `sik_not` pilleri |
| 8 Kapanış | 19 | 15 | 8,7 | SIGNAL → VERB · Next lesson | kalemle ok; sonraki ders kartı |
| Toplam | 1–19 | 360 | 281,7 (ses bitişi) | | zaman.json son t_son 282,19 |

Not: hedef altında kalma kabul (jüri onaylı); dolgu eklenmedi. Soru anı: 2 (cümle 6, cümle 13); yanlış cevap mini soru içinde (cümle 17).

## 3. Sahne planı (P2 uygular; klasör `sahneler/NN-<motor>-<ad>`; geçiş: BookFlip, 13'ten sonra fade, son sahne geçişsiz)

Motor seçimi `references/kalem-hatti.md`: HyperFrames = yazı/kart/künye; Paper.js = kendini çizen kalem darbesi; Düz canvas = figür + nesne.

| No | Klasör | Motor | t_bas–t_son (sn) | Cümle | Öneri |
|---|---|---|---|---|---|
| 1 | `01-hyperframes-giris` | HyperFrames | 0,00–3,00 | 1 (başı) | Soğuk açılış kapak kalıbı; ilk söz 1,00 sn; kinetik başlık, iki kart, künye uçuşu. Cümle 1 sesi 5,00'e kadar sürer; yazı 3,00'dan önce yerinde, sahne 02'ye hazır geçer |
| 2 | `02-paperjs-kanca` | Paper.js | 3,00–15,31 | 1 (sonu), 2 | `goes` / `is going` kartları, `vs` çipi; sol/sağ çip sarı daire ses sırasıyla |
| 3 | `03-paperjs-ornek1` | Paper.js | 15,31–33,00 | 3 | Örnek 1/3: uçak ikonu kalemle, `are` yakın çekim, `at 9` sarı, `PLAN` |
| 4 | `04-canvas-ornek2` | Düz canvas | 33,00–51,57 | 4 | Örnek 2/3: takvim ikonu, `these days` sarı belirteç, `is going` daire |
| 5 | `05-canvas-ornek3` | Düz canvas | 51,57–68,56 | 5 | Örnek 3/3: `harder and harder` belirteç + yükselen ok, `nowadays` daire, `CHANGING` |
| 6 | `06-hyperframes-soru1` | HyperFrames | 68,56–87,78 | 6 (öğrenci), 7 | SORU ANI 1: balon + ogrenci-bas.svg sözcük sözcük; 0,75 sn duraklama; cevap kartı `CHANGING → mostly -ing`; üç örnek köşede küçülür |
| 7 | `07-hyperframes-kural` | HyperFrames | 87,78–109,61 | 8 | Kural kartı 3 satır kademeli (NOW / THESE DAYS·NOWADAYS·PLAN / USUALLY·GENERAL) |
| 8 | `08-canvas-karsit1` | Düz canvas | 109,61–130,74 | 9 | Nancy cümlesi, iki ok (`usually`→`spends`, `now`→`is meeting`), alt zaman çizgisi |
| 9 | `09-canvas-karsit2` | Düz canvas | 130,74–167,60 | 10, 11 | İki sol/sağ kart çifti (staying ≠ includes; offers ≠ are enjoying); sahil çizgisi + figür (standing) |
| 10 | `10-hyperframes-tuzak` | HyperFrames | 167,60–188,50 | 12, 13 | TRAP kartı `We believe…`; SORU ANI 2 balonu (cümle 13, sözcük sözcük, 0,75 sn duraklama) |
| 11 | `11-canvas-tuzak-fiiller` | Düz canvas | 188,50–226,45 | 14 | `believe` + `-ing` üstü sarı çarpı; `has` kutusu; `recommend` daire; köşe listesi; `performative` etiketi yalnız promise·agree·recommend |
| 12 | `12-hyperframes-ozet` | HyperFrames | 226,45–242,28 | 15 | `ozet` 3 madde; geçiş çizgisi (perde yok) |
| 13 | `13-hyperframes-mini-soru` | HyperFrames | 242,28–272,42 | 16, 17, 18 | `soru` kök + 5 şık + sayaç ("Beş şık var"); yanlış cevap A balonu; doğru B yeşil, `sik_not` pilleri; çıkış fade |
| 14 | `14-hyperframes-kapanis` | HyperFrames | 272,42–282,19 | 19 | `SIGNAL → VERB` kalemle ok; sonraki ders kartı; son sahne +0,5 sn kuyruk |

Sahne dizinleri P1'de OLUŞTURULMADI. Sahne zamanları `zaman.json` ile birebir; `ortak/anlatim/zaman_uret.py` yeniden üretir.
Künye: sol üst `PRESENT CONTINUOUS vs SIMPLE PRESENT · YDT BASIC`; sağ üst bölüm çipi; tek vurgu sarı, doğru şık yeşil, kırmızı yok.

## 4. Ses dosyaları (`ortak/anlatim/`)

`senaryo.json` (19 cümle) → `sentez.wav` + `cumle-N.wav` + `sureler.json` (el.py) → `sozcuk_uret.py` → `sozcukler.json` + `baslar.json` → `zaman_uret.py` → `../../zaman.json` → `kur.py` → `anlatim.wav` → `ses-paketle.py` → `anlatim.m4a` → `altyazi_uret.py` → `altyazi.json`; `metin_uret.py` → `METIN.md`.
Cümle başları sabit dizi değil: ilk cümle 1,00 sn; sonrası önceki bitiş + 0,55 sn (öğrenciden sonra 0,75 sn).
