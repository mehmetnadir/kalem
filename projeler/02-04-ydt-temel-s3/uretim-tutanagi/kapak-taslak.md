# 02-04-ydt-temel-s3 · kapak taslağı (3 sürüm, 1080×1920 PNG)

Durum: TASLAK (istem S3-A, 15.11.2026). Görsel üretim ve render YOK.
Kural: `dijital-anlatim/.claude/docs/dikey-senaryo-kalibi.md` §4 ve "Uygulandı (04.11)" bant tablosu. Emsal: S1 `kapak-taslak.md`.
Sürüm A = Shorts'un ilk karesi (kalıp §5). B ve C ayrı PNG; videoya girmez. Çıktı adları (öneri): `kapak-a.png`, `kapak-b.png`, `kapak-c.png`.

## 1. Ortak öğeler (üç sürümde aynı)

| Öğe | Değer | Kaynak |
|---|---|---|
| Zemin | açık: kâğıt `#f7f3ea`, mürekkep `#1b2440` | K19, kalıp §4 |
| Rozet | `YDT · BASIC` (tek rozet; S1 ile aynı) | ders + seviye |
| Sarı hap | dolgu `#ffe066` (`RENK.vurguDolgu`), yazı `#1b2440` (`RENK.pilMetin`) | `../../02-04-ydt-temel-s1/ortak/kunye.js` satır 11–12 (`acik`) |
| Logo | `dijital-anlatim/varlik/logo/yds-publishing.svg`, alt sol (y ≈ 1478) | kalıp §4 |
| Başlık boyu | iki satır aynı boy; 952 px'e (1080 − 2 × 64) sığan en büyük değer, üst sınır 190 px; motor ölçer, elle boy yazılmaz | S1 §2 |
| Etiket yazısı | Caveat, en az 72 px; dikey taban 64 px | S1 §1–§2 |
| Çizimler | tren, saat (kollar yedide, rakamsız), sinema bileti: ana ders sahne 05 (`trenParcalari`, `saatParcalari`, `biletParcalari`) | ana ders `05-canvas-ornek3/sahne.js` |
| Yasak | üçüncü satır, küçük yazı, emoji, kalabalık sahne | kalıp §4 |

- `-ING` Latin büyük I ile yazılır. Başlık metni elle büyük harf yazılır; `text-transform` kullanılmaz (Türkçe yerelde `-İNG` olur).
- `TARİFE`, `İKİ ÖRNEK`, `İKİ ZAMAN` Türkçe İ ile yazılır.

## 2. Sürümler

| Öğe | A — can alıcı kod (S1 kalıbı) | B — soru / merak | C — karşıt çift |
|---|---|---|---|
| Başlık satır 1 | `TARİFE` · altında sarı el altçizgisi | `NEDEN -ING` | `İKİ ÖRNEK` |
| Başlık satır 2 | `≠ PLAN` (sarı hap) | `YOK?` (sarı hap) | `İKİ ZAMAN` (sarı hap) |
| Sözcük sayısı | 2 | 3 | 4 |
| Can alıcı | kısa kod `tarife → leaves · plan → am going` (`canAlici[1]`, `[2]`); başlık + etiketlerle okunur | `canAlici[1]` (tarifeli gelecek: V1 / V-s); kısa kod `leaves`: kartta sarı altçizgili sözcük. Başlık soruyu sorar, kart can alıcı öğeyi gösterir; cevabı videoda (S3-C, kaynak jürisi madde 2) | `canAlici[1]` + `[2]`; kısa kod `leaves` (V-s) ↔ `am going` (am + V-ing): iki kart (S3-C, kaynak jürisi madde 2) |
| Görsel | solda tren + saat, etiket `leaves`; sağda elinde sinema bileti tutan öğretmen figürü, etiket `am going`; figür hafif gülümser, başı trene dönük | ortada tren + saat; trenin üstünde el çizimi sarı `?`; altında tek kart `The train leaves …` (Fredoka 72), `leaves` altında sarı altçizgi; sağda öğretmen figürü trene işaret eder | iki kart üst üste, aynı boy: `The train leaves …` (solda tren ikonu) / `I am going …` (solda bilet ikonu). Tek vurgu: `leaves` sarı hapta. Sağ altta küçük öğretmen figürü (kalıp §4 "figür + nesne"; S3-C, kaynak jürisi madde 2) |
| Vurgu mantığı | `≠` iki kavramı ayırır | soru öğrencinin ağzından; `?` sarı | `leaves` şaşırtan öğe (gelecek, ama -ing yok); `am going` beklenen biçim, vurgusuz |
| Rozet | `YDT · BASIC` | `YDT · BASIC` | `YDT · BASIC` |
| Kalem hareketi | yalnız video karesinde: `TARİFE` altçizgisi 0,3–0,8 sn (başlık 0. karede tam) | yok (durağan PNG) | yok (durağan PNG) |
| Yeni metin | `TARİFE ≠ PLAN`: ana derste yok; S3-B dil ve kaynak jürisi geçti | `NEDEN -ING YOK?`: ana ders cümle 6'dan birebir kesit | `İKİ ÖRNEK` / `İKİ ZAMAN`: S3-B dil jürisinin önerdiği metin (madde 1); `İKİSİ DE GELECEK` "gelir" diye okunuyordu |
| Uzunluk (karakter) | 6 / 6 | 10 / 4 | 9 / 9 |

- Kart satırı kısaltması (B, C): `The train leaves …`, `I am going …`. S1 kapak etiketleri (`I live` / `I am living`) gibi özne + fiil.
  Kapakta tam cümle yok (2 kart × 2 satır kalabalık olur). Rakam yok.
- `≠` glifi: ana ders sahne 09 ve 11 ekranda kullandı. Fredoka'da glif yoksa kalemle çizilir; sahne kodu ölçer.

## 3. Yerleşim (dikey v2 bantları, y px)

```
0 ─────── 288   HUD: rozet YDT · BASIC
288 ───── 768   başlık 2 satır (y 346–768)            A: TARİFE / ≠ PLAN · B: NEDEN -ING / YOK? · C: İKİ ÖRNEK / İKİ ZAMAN
864 ──── 1344   sahne                                 A: tren+saat (sol) · bilet tutan figür (sağ) · leaves / am going
                                                      B: tren+saat + sarı ? · kart The train leaves … · figür (sağ)
                                                      C: kart The train leaves … / kart I am going … · ikonlar solda · küçük figür sağ alt
1344 ─── 1536   boş (Shorts'ta altyazı bandı) · logo sol alt y ≈ 1478
1536 ─── 1920   platform arayüzü: BOŞ
```

## 4. Platformda kullanım

| Platform | Kapak | Sürüm |
|---|---|---|
| YouTube Shorts | yalnız Studio'da seçilir, akışta görünmez (huni-plan §5) | A, B, C elle denenebilir |
| TikTok | "API karesi veya Studio" (huni-plan §5) | kare seçiliyorsa yalnız A (videonun içinde); B, C için yükleme yolu doğrulanmadı |
| Instagram | kapak alanı doğrulanmadı (huni-plan §5) | A ilk kare; B, C elle yükleme doğrulanmadı |

## 5. `senaryo.json` alanları (yalnız A; video ilk karesi)

```json
"giris": {
  "logo": "varlik/logo/yds-publishing.svg",
  "satir1": "TARİFE",
  "satir2": "≠ PLAN",
  "rozetler": ["YDT · BASIC"],
  "sahne": [
    {"ad": "train", "x": 28, "y": 58, "olcek": 0.6},
    {"ad": "clock", "x": 28, "y": 44, "olcek": 0.3},
    {"figur": "ogretmen", "x": 70, "y": 58, "olcek": 0.8},
    {"ad": "ticket", "x": 82, "y": 64, "olcek": 0.3}
  ]
},
"meta": {
  "kapak": {
    "satir1": "TARİFE",
    "satir2": "≠ PLAN",
    "canAlici": "tarife → leaves · plan → am going"
  }
}
```

Ad değerleri (`train`, `clock`, `ticket`) öneridir; ana ders sahne 05 çizimleri birincildir, yoksa Open Doodles / Tabler taranır.
x, y, olcek başlangıç önerisidir; sahne kodu yazılırken kontak sayfasında düzeltilir. B ve C kayıt alanı şefte (rapor açık nokta 12).
