# simple-present-temel-s3 · kapak taslağı — 3 sürüm (1080×1920 PNG)

Durum: TASLAK (istem P0202-S3-A, 15.11.2026). Görsel üretim ve render YOK. S3-C (15.11): jüri düzeltmeleri işlendi (`S3-duzeltme.md`).
Sahne klasörleri huni v2 numarasıyla (S3-C): A = `01-hyperframes-kanca`, B = `06-hyperframes-kapak-b`, C = `07-hyperframes-kapak-c`.
Kural: `huni-v2-standart.md` §6 (A = kanca karesi; B ve C ayrı tasarım; en az biri karakter taşır; altyazı yok; kanal katmanı var),
§2 (yerleşim); `dikey-senaryo-kalibi.md` §4 (başlık, can alıcı, görsel, rozet, yasaklar). Emsal biçim: `02-04-ydt-temel-s2` `kapak-taslak.md`.
Dosyalar (emsal S2-C kalıbı): A = sahne 01 karesi `kapak-a.png` + kopyası `kapak.png`; B = durağan sahne `05-hyperframes-kapak-b` →
`kapak-b.png`; C = durağan sahne `06-hyperframes-kapak-c` → `kapak-c.png`.
Ana ders kapak metni `GİDER = GOES` (olumlu cümlede s). Üç kısa kapağı bu metni yinelemez; üçü de olumsuz ve soru cümlesindeki tuzağı taşır.

## 1. Sürümler bir bakışta

| | A — kanca karesi | B — soru / merak | C — kural kartı + karşıt çift |
|---|---|---|---|
| Başlık satır 1 | `BU CÜMLE` | `GOES mu,` | `DOES VARSA` |
| Başlık satır 2 | `YANLIŞ` (sarı hap) | `GO mu?` | `FİİL YALIN` |
| Sözcük sayısı | 3 | 4 | 4 |
| Can alıcı | tek kaynak ana cümle 7 parça 4 ("Olumsuzda ve soruda does girer, s ona geçer."): yanlış yeri gösterir; neden sorusu açık kalır | aynı kaynak, soru biçiminde: does varken fiil s alır mı? | aynı kaynak, kural kodu olarak: `does → fiil yalın` |
| Görsel | kart `He doesn't goes.` (sol) + karakter (sağ, sola, karta işaret eder) | kart `He doesn't ____.` / `Does she ____?` + iki şık hapı `go` · `goes` + büyük `?`; figür yok | iki kart üst üste: `He doesn't goes.` (soluk, kırmızı ✗) · `He doesn't go.` (mürekkep, ✓); figür yok |
| Karakter | VAR: ana `ortak/kapak/karakter.png` | yok | yok |
| Tek vurgu (sarı) | `YANLIŞ` hapı | `?` işareti | doğru kartta `go` altında el altçizgisi |
| Kırmızı | yok | yok | yanlış kartta üstü çizili `es` eki + `✗` |
| Kalem hareketi | video içinde 0,3–0,8 sn: hap çerçevesi kalemle | durağan | durağan |
| Seste karşılık | cümle 1 (kanca: `He doesn't goes.` · `Hata nerede?`) | cümle 2 EN parça `He doesn't go. Does she go?` | cümle 2 `Fiile s gelmez.` + cümle 3 `Does varsa fiil yalın.` |
| Dosya | `kapak-a.png` + kopyası `kapak.png` (sahne 01 karesi) | `kapak-b.png` (sahne 06, durağan) | `kapak-c.png` (sahne 07, durağan) |

Fark ilkesi: A yanlışı gösterir ve nedeni videoya bırakır. B iki seçenek sorar ve cevabı videoya bırakır. C kuralı ve karşıt çifti verir;
kaydedilecek kapaktır. Başlıklar ayrı sözcüklerdir; üçünde de `GİDER` yok.

## 2. Ortak öğeler (üç sürüm)

| Öğe | Değer | Kural |
|---|---|---|
| Zemin | açık kâğıt `#f7f3ea`, mürekkep `#1b2440` (video kareleriyle aynı) | K19 |
| y 0–280 | yalnız zemin | standart §2 (platform arayüzü) |
| Kanal katmanı y 280–350 | `yds-publishing-lacivert.svg` (ana `ortak/logo/`), yükseklik ≈ 48 px, x 60'tan + `@ydspublishing` Lexend 700 42 px, mürekkep | standart §1 kural 1, §2 |
| Künye y 360–450 | konu `Simple Present` (Fredoka 700, x 60, taban 420, boy ≤ 34) + rozet hapı `YDT · BASIC` | standart §2; rozet emsal 02-04-ydt-temel-s1 (istem S3-C) |
| Başlık y 470–800 | Fredoka 700, 2 satır aynı boy, kalın kontur (zemin rengi 10 px, `paint-order: stroke fill`); 900 px genişliğe (x 60–960) sığan en büyük değer, üst sınır 190 px; motor ölçer, elle boy yazılmaz | kalıp §4 |
| İçerik y 820–1380 | x 60–960 | standart §2 |
| y 1400–1550 | boş (altyazı yok) | standart §6 |
| y 1570–1920 | yalnız zemin | standart §2 |
| Hap | dolgu `#ffe066`, yazı `#1b2440` | emsal S2 §2 |
| Kırmızı | `#d6453a`, yalnız yanlış işaretinde | ana BRIEF §2.1 açık palet |
| Yazı tabanı | kart yazısı en az 64 px; künye en az 36 px | küçük yazı yasak |
| Yasak | üçüncü başlık satırı, emoji (`✗`, `✓`, `?` SVG kalem çizimidir, emoji değil), kalabalık sahne, standart §1 kural 4–5 sözleri | kalıp §4; standart §1 |

Karakter dosyası: `../../simple-present-temel/ortak/kapak/karakter.png` (şeffaf PNG; genç erkek, iri kıvırcık saç, yuvarlak gözlük,
koyu ceket, bel üstü, sola işaret eder, "buldum" ifadesi; `KAYNAK.json` üretim `d97e66af…`, nano-banana-2). Kâğıt zeminde arkasına sarı
daire (`#fece00`) ve 10 px krem kenar (kapak-standardi §2 çıkartma kenarı) gelir: krem ceket ve saç ayrıntısı zeminde kaybolmaz.

## 3. Sürüm A — kanca karesi

```
0 ─────── 280   yalnız zemin
280 ───── 350   kanal katmanı: logo + @ydspublishing
360 ───── 450   künye: Simple Present · YDT · BASIC
470 ───── 800   başlık: BU CÜMLE / YANLIŞ (sarı hap)
840 ──── 1000   kart (sol, x 60–640): He doesn't goes.   (Fredoka 80)
880 ──── 1380   karakter (sağ, x 600–950), sola işaret eder → kart; arkasında sarı daire
1400 ─── 1550   boş (altyazı yok)
1570 ─── 1920   yalnız zemin
```

- Kanca karesi = sahne 01'in t 0,90 karesi (kare 27): başlık tam, hap çerçevesi çizilmiş, karaoke ve kırmızı `?` henüz yok.
- **DİKKAT:** başlık ve kart 0. karede tamdır; ses 1,00'da başlar. "Ekran metni sesten önce gelmez" kuralının kapak istisnası
  (kalıp §5 "Kapak = ilk kare"; emsal S1, S2).
- Karede düzeltme yok (merak). Yanlış biçimi `YANLIŞ` hapı etiketler; kırmızı yok.
- Karakter ana ders kapağında da var: kısanın ilk karesinde ve çağrı sahnesindeki ana kapakta aynı yüz görünür (döngü).
- Kaba boy: satır 1 `BU CÜMLE` 8 karakter → ≈ 190 px üst sınırına yakın (0,55 em/karakter, ölçülmedi).

## 4. Sürüm B — soru / merak

```
0 ─────── 280   yalnız zemin
280 ───── 350   kanal katmanı
360 ───── 450   künye
470 ───── 800   başlık: GOES mu, / GO mu?
860 ──── 1120   kart: He doesn't ____.  /  Does she ____?   (Fredoka 72; boşluk kalemle çizilmiş çizgi)
1160 ─── 1300   iki hap: go · goes (mürekkep çerçeve, dolgusuz)  ·  sağda büyük sarı ?
1400 ─── 1550   boş
1570 ─── 1920   yalnız zemin
```

- Soru eki küçük harf (kapak-standardi §3 izin verir). Ünlü uyumu: *goes* /goʊz/ → `mu`; *go* → `mu`.
- İki şık aynı biçimde; hiçbiri vurgulanmaz. Gerekçe: vurgu cevabı verir. Tek sarı öğe `?`.
- Cevap videoda: cümle 2 EN parça `He doesn't go. Does she go?` + cümle 3 `Does varsa fiil yalın.`
- Başlık sesteki hiçbir tümceyi yinelemez.

## 5. Sürüm C — kural kartı + karşıt çift

```
0 ─────── 280   yalnız zemin
280 ───── 350   kanal katmanı
360 ───── 450   künye
470 ───── 800   başlık: DOES VARSA / FİİL YALIN   (mürekkep, hap yok)
840 ──── 1060   kart 1 (soluk): He doesn't goes.   goes'un es eki kırmızı üstü çizili (go + çizili es) · sağda kırmızı ✗
1100 ─── 1320   kart 2: He doesn't go.   sağda ✓ (mürekkep) · go altında sarı el altçizgisi
1400 ─── 1550   boş
1570 ─── 1920   yalnız zemin
```

- Başlık kaydet sahnesindeki kural cümlesidir (`Does varsa fiil yalın.`). C, kaydedilip geri dönülecek kapaktır.
- Büyük harf Türkçe kuralla: `FİİL` (İ noktalı). `DOES` İngilizcedir.
- Tek vurgu `go`: göz yalın fiile gider. Başlık hapsız: kartta tek sarı öğe kalır.
- En uzun kart satırı `He doesn't goes.` 16 karakter; Fredoka 72'de ≈ 640 px (kaba).
- **DİKKAT:** kalıp §4 "Görsel: figür + nesne" maddesinden sapma (B ve C'de figür yok; emsal S2 C ile aynı). Standart §6 "en az biri
  karakter taşır" A ile karşılanır.

## 6. `senaryo.json` alanları (huni-plan §2 veri kaynağı)

`senaryo.json` yalnız A'yı taşır. B ve C durağan kare sahneleri 06 ve 07'dir; değerleri o sahnelerin istemine girer (emsal S2-C).
Kart ve karakter sahne 01 kodunda çizilir; yeni şema alanı açılmaz.

```json
"giris": {
  "logo": "varlik/logo/yds-publishing.svg",
  "satir1": "BU CÜMLE",
  "satir2": "YANLIŞ",
  "rozetler": ["YDT · BASIC"]
},
"meta": {
  "kapak": {
    "satir1": "BU CÜMLE",
    "satir2": "YANLIŞ",
    "canAlici": ""
  }
}
```

| Sürüm | `satir1` | `satir2` | `meta.kapak.canAlici` | Görsel |
|---|---|---|---|---|
| B | `GOES mu,` | `GO mu?` | boş (tek kaynak ana cümle 7 parça 4) | kart + iki hap + `?`, sahne 06 kodunda |
| C | `DOES VARSA` | `FİİL YALIN` | boş (tek kaynak ana cümle 7 parça 4) | iki kart, sahne 07 kodunda |

- `meta.kapak.canAlici` alanına `canAlici` listesinden birebir madde yazılır (emsal kuralı). Ana paket listesinde S3'ün maddesi
  (does → yalın fiil) yok; `[3]` S3'ün bilgisi değil (jüri kaynak 2). Alan boş kalır; tek kaynak ana cümle 7 parça 4. Şef ana listeye
  "Olumsuzda ve soruda does girer, s ona geçer" maddesini eklerse alan o maddeyi birebir alır (`S3-duzeltme.md`).
  `02-02-ydt-temel` `canAlici[1]` kullanılmaz (jüri kaynak, açık nokta 1).
- `rozetler` ana pakette `["YDT · BASIC", "GRAMMAR"]`; standart §2 `YDT · TEMEL` der. S3-C emsal künyesini alır: `["YDT · BASIC"]`
  (istem S3-C "Rozet emsaldeki gibi"; emsal 02-04-ydt-temel-s1).

## 7. Karar notu

- Videonun ilk karesi A. B ve C platform kapağı olarak yüklenir (PNG).
- Kullanılmayan seçenek: A için `HATA` / `NEREDE?`. Neden: sesteki soruyu yineler; B de soru olunca A ile B ayrışmaz. A ifade, B soru kalır.
- Kullanılmayan seçenek: C için `İKİ S` / `OLMAZ`. Neden: kökü s ile biten fiilde (*miss*, *pass*) yanlış okunur; `FİİL YALIN` kesindir.
