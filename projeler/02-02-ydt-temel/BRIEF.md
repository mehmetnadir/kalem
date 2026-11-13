# Simple Present — TEMEL seviye (YDT, tümevarım: 3 örnek → kural → karşıt çift → tuzak) · `projeler/02-02-ydt-temel`

Durum: P1 (anlatım + paket iskeleti) tamam; sahneler P2'de yazılır. Render yok (yalnız Nadir panelde işaretlerse).
Ana görsel dil ve stil anayasası: `../present-continuous/BRIEF.md` (kalem hattı) + skill `motion-grafik-ders`
(`references/stil-anayasasi.md`, `kalem-hatti.md`). Bu BRIEF yalnız künye, iskelet ve sahne planını tanımlar.
Senaryo kaynağı (jüri GEÇTİ 3/3, D-0204/D-0205): `/Users/nadir/01dev/kalem/_is/senaryo-taslak/02-02-ydt-temel.md`
(her satırın "görsel fikir" sütunu P2'nin sahne girdisidir; satır no `ortak/anlatim/satirlar.json` ile cümle no'ya bağlanır).

## 0. Künye

| Alan | Değer |
|---|---|
| Kimlik | `02-02-ydt-temel` |
| Kod | `ING-YDT-GR-02-02-T` (katalog GR-02-02, "02 - tenses - 02") |
| Konu | Simple Present (geniş zaman) — Present Forms, ikinci video |
| Kitle / seviye | YDT / temel |
| Biçim | yatay 16:9, 1920×1080, 30 fps, tema açık (K19) |
| Künye metni | ders `SIMPLE PRESENT` · seviye `YDT BASIC` · ajanda Hook · Examples · Form |
| Sesler | öğretmen Atakan Arisoy `gsJ9nrlXYbPztJxC4fwc` · öğrenci Gökçe Deniz `oPC5I9GKjMReiaM29gjY` · eleven_v4 · hız tr 1,0, en 0,9 |
| Anlatım | `ortak/anlatim/anlatim.m4a` (soğuk açılış: ilk söz 1,00 sn, K23) |
| Süre iddiası | yok (ne seste ne ekranda) |

## 1. Kaynak

| Kaynak | Yol / kimlik |
|---|---|
| pptx | `/Users/nadir/01dev/dijital-anlatim/varlik/grammar/kaynak-pptx/YEDEK/Tenses/unit-1_sunum-2a uygun.pptx` (36 slayt; animasyon adımları aynı içeriği tekrarlar) |
| Eski ders döküm | Vimeo 863572777, LMS "02 - tenses - 02" · `/Users/nadir/01dev/dijital-anlatim/varlik/grammar/transkript-whisper/863572777.md` (Whisper hataları: I,U,V,D = I, you, we, they; "Kaş" → cash) |
| Senaryo taslağı | `_is/senaryo-taslak/02-02-ydt-temel.md` + jüri `02-02-ydt-temel.juri.md` |
| Prototip (yalnız bakmak için) | `projeler/simple-present-temel/` (90 sn kalem prototipi, DEĞİŞTİRME) |

Kapsam kesintisi (jüri onaylı): slayt 1 (menü), 13–35 (ileri videoda); slayt 4'teki uzun kalıp listesi 6.3'e üç kalıpla girdi.

## 2. İskelet (hedef 360 sn; taslak tahmini 361 sn)

| Bölüm | Süre (hedef sn) | Ekran metni (özet) | Görsel notu |
|---|---|---|---|
| Kanca | 15 | Her sabah yedide kalkıyorum. · I get up at seven every morning. · -yor ≠ -ing ? · SIMPLE PRESENT | soğuk açılış 0. kareden; kinetik başlık, clock çizimi, yor ↔ ing bağı; başlık künyeye uçar, ajanda Hook · Examples · Form |
| Örnekler | 90 | Example 1/3: I go to Kaş every summer… · Example 2/3: He gets up… · Example 3/3: The Moon completes… | her örnek: kart + odak daireleri + TR çeviri + tek çizim; sinyal sözcüğü altı çizgi; `ek_ayir` get\|s, swim\|s, complete\|s |
| Kural kartı | 45 | I · you · we · they → V · he · she · it → V + s · + don't / doesn't + V · Do / Does + özne + V ? | öğrenci balonu (soru 1), `tanim` üç blok kademeli, `ek_ayir`, kısa örnek kartları |
| Karşıt çift | 60 | She eats fish every day. / She is eating fish now. · rutin → geniş zaman, şu an → şimdiki zaman · kanca cümlesi geri gelir | bölünmüş ekran, `zaman_cizgisi` iki yan, `fark_tablosu`, kancadaki çarpı → tik |
| Tuzak | 60 | She doesn't eats fish. ✗ · Does she eats fish? ✗ · does = do + s · olumlu: eats / olumsuz, soru: does + eat | kırmızı yalnız burada; öğrenci balonu (soru 2); `ek_ayir` s eats'ten does'a kayar; `fark_tablosu`; kanca fiiliyle doğrulama |
| Ara özet | 20 | rutin · kalıcı durum · genel gerçek · he/she/it → s · always 100 % → never 0 % | `ozet` kademeli; yatay sıklık ölçeği; tekrar sayısı kalıpları ayrı etiket |
| Mini soru | 55 | Every morning, my brother ____ the dog… A) take B) takes C) taking D) is taking E) to take | `soru` + sayaç halkası; öğrenci yanlış cevap A; `dogru` B yeşil; `sik_not` A, C, D, E; 3 adım yöntem |
| Kapanış | 15 | SIMPLE PRESENT · özne + V · he/she/it + V-s | `baslik` + formül kartı; logo; tek kare durgun |

Öğrenci sesi: soru 1 (kural kartı, "fiil her özneyle aynı kalır"), soru 2 (tuzak, "she var, doesn't eats"), yanlış cevap (mini soru, A şıkkı take).

## 3. Sahne planı (P2 bunu uygular; klasör `sahneler/NN-<motor>-<ad>/`, şimdilik OLUŞTURULMADI)

Motor seçimi `kalem-hatti.md` tablosuna göre: Paper.js = kendini çizen kalem darbesi (kanca, ilk örnek) · Düz canvas = figür + nesne çizimi ·
HyperFrames = yazı / kart / tablo / sayaç. Cümle no = `senaryo.json` sırası; satır no = taslak tablosu (`satirlar.json`).

| No | Klasör | Motor | Bölüm | Taslak satırları | Cümle no | Sahne önerisi |
|---|---|---|---|---|---|---|
| 1 | `01-paperjs-kanca` | Paper.js | Kanca | 1.1–1.4 | 1–4 | kinetik başlık, kalemle clock (07:00), yor ↔ ing bağı + soru işareti, başlık künyeye uçar |
| 2 | `02-paperjs-ornek1` | Paper.js | Örnekler | 2.1–2.5 | 5–9 | Example 1/3 çipi, kart, go ve have daireleri, every summer çizgisi, yazlık + güneş çizimi |
| 3 | `03-canvas-ornek2` | Düz canvas | Örnekler | 2.6–2.10 | 10–14 | Example 2/3, kart, gets ve swims, peeps figürü + havuz çizgisi, `ek_ayir` get\|s swim\|s |
| 4 | `04-canvas-ornek3` | Düz canvas | Örnekler | 2.11–2.15 | 15–19 | Example 3/3, Moon kartı, güneş + yörünge elipsi + Ay, genel gerçek etiketi, `ek_ayir` complete\|s |
| 5 | `05-hyperframes-kural` | HyperFrames | Kural kartı | 3.1–3.8 | 20–27 | öğrenci balonu (soru 1), `tanim` üç blok (V / V+s, don't·doesn't, Do·Does), `ek_ayir` get\|s go\|es stud\|ies, örnek kartlar |
| 6 | `06-canvas-karsit` | Düz canvas | Karşıt çift | 4.1–4.11 | 28–38 | bölünmüş ekran, her gün / şu an `zaman_cizgisi`, `fark_tablosu`, kanca kartı geri gelir, çarpı → tik |
| 7 | `07-hyperframes-tuzak` | HyperFrames | Tuzak | 5.1–5.12 | 39–50 | kırmızı çarpılı iki yanlış kart, öğrenci balonu (soru 2), s harfi eats'ten does'a kayar, `fark_tablosu`, doğru kartlar |
| 8 | `08-hyperframes-ozet` | HyperFrames | Ara özet | 6.1–6.3 | 51–53 | `ozet` üç + iki madde, always → never yatay ölçek, tekrar sayısı kalıp etiketleri |
| 9 | `09-hyperframes-soru` | HyperFrames | Mini soru | 7.1–7.6 | 54–59 | `soru` kartı + 5 şık, sayaç halkası (2,0 sn sessizlik), A işareti (öğrenci), B yeşil, `sik_not`, üç adım yöntem |
| 10 | `10-hyperframes-kapanis` | HyperFrames | Kapanış | 8.1–8.2 | 60–61 | `baslik` + formül kartı, logo, son kare durgun |

Notlar (P2 için): kırmızı yalnız sahne 7'de yanlış cümlelerde · öğrenci figürü `kadro.ogrenci` (kadın, K22) · çizimler `ortak/cizim/` (Open Peeps/Doodles, Tabler; balık
çizimi için Open Doodles taranır) · her sahne sonunda içerik durgun (geçiş 12 kare) · metin tabanı yatay 30 mantıksal px ·
sözcük zamanları `ortak/anlatim/sozcukler.json` (küresel sn; yerel kare = round((t − t_bas) × 30)) · altyazı parçaları `altyazi.json`.


## Şef notu 13.11 — sahne planı güncellendi

Seri tutarlılığı ve K23 için 3,00 sn'lik `01-hyperframes-giris` (soğuk açılış kapağı, künye uçuşu) eklendi; kanca `02-paperjs-kanca` 3,00–16,27; öteki sahneler bir numara kaydı. Geçerli liste `zaman.json` (yukarıdaki tablodaki klasör numaraları eski).
