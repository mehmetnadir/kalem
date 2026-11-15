# Sahne 01 · kanca — A/B kol b (`kanca` = `soru`; HyperFrames DİKEY 1080×1920, 109 kare, 0,00–3,24 sn + 12 kare geçiş payı)

| Ölçüm | Değer |
|---|---|
| Durum | yazıldı (istem KBC-0202S3, 15.11.2026, srv21). Önizleme hazırlığı `ONIZLE_YALNIZ=1`. mp4 yok, commit yok |
| Kaynak | kol a `simple-present-temel-s3/sahneler/01-hyperframes-kanca/` kopyası; `uret.py`, `zamanlar.json`, `olay.py`, `calistir.sh` değişti |
| qa-yerel | çıkış 0 · `01-hyperframes-kanca \| çakışma yok (14 örnek, 781 kutu)` |
| Kapak A | `kapak-a.png` = `kapak.png` (md5 `a7b1535b…`), `k/koyu/kapak-a-koyu.png` (`02c931eb…`); t 0,90; altyazısız |
| Son kare | kol a son karesiyle (3,90 ↔ 3,24) kanal, künye, içerik, boş bantlar fark 0 piksel; kart: `es` glif kenarında 183 piksel (en çok 60/255) |
| `devir.json` | kol a ile aynı; yalnız `t` 3,89 → 3,24 |

## İçerik (kol a farkı)
- Söz: `Olumsuzda s nereye gider?` (tek TR parça). Altyazı 4 sözcük, sözcük zamanlı karaoke.
- Başlık `S NEREYE` / `GİDER?` (sarı hap). B = 133 (kol a ile aynı; görsel ağırlık eşit). Satır tabanları kol a ile aynı
  (T1 596,69 · T2 753,86). Hap alt payı kol a ile aynı; üst pay ona eşit, İ noktası üst payın içinde (hap y 622,19–792,43,
  x 264,22–755,78; İ üstü 631,37).
- `GİDER?` iki `<text>` parçası (`Gİ` + `DER?`), konumu tek yazıyla aynı. Sebep: İ noktası tek kutuyu köşeye dek yükseltir;
  0,50 sn'de yarım çizilmiş çerçevenin köşe yayı o kutu köşesini keser (kapı ilk koşu: `kesişim 22x13 px`). Mürekkepte kesişme yok.
- Kapak kartı `He goes.` kartta ortalı (He x 249,08, goes. x 362,68). Kart çerçevesi kol a ile aynı (x 60–737, y 840–1000).
- "Olumsuzda" (1,00–1,72): şapka `‸` (SVG, mürekkep, tabanın altında, x 353,28) 1,00–1,20 kalemle; `He` ve `goes.` 1,00–1,30 kol a
  yerlerine kayar (power2.inOut); `doesn't` 1,30–1,62 soldan sağa kırpmayla açılır; şapka 1,62–1,72 söner. Kart 1,62'de kol a kartıdır.
- "s" (2,04–2,20): `goes` içindeki `es` altında sarı kalem çizgisi (0,10 sn çizim, 2,20'de kapanır).
- "nereye" (2,28): kırmızı `?` kol a yerinde, 2,28–2,72.
- Çıkış C0 = 2,7333: kural "son söz sonu − 0,50"; `gider?` sözcük sonu (3,32) ses bitişini (3,24) aştığı için sınır içerik sonu (3,2333, kare 97).

## Taslaktan sapma
| Taslak (`senaryo-taslak.md` §2) | Uygulama | Sebep |
|---|---|---|
| kayma 1,00–1,40, açılma 1,20–1,60 | kayma 1,00–1,30, açılma 1,30–1,62 | açılan `doesn't` kayan `He` ile kesişmesin (kapı kırpmayı ölçer) |
| çapalar tahmin (s 1,94, nereye 2,29, çıkış 2,98) | ölçülmüş: s 2,04, nereye 2,28, çıkış 2,73 | sentez sonrası `sozcukler.json` |

## Bakılan kareler (Read)
| Kare (sn) | Bulgu |
|---|---|
| 0 · 0,90 | kapak: başlık, hap (0,90'da çerçeveli), `He goes.`, karakter; altyazı yok |
| 1,15 · 1,40 · 1,65 | şapka, sözcükler ayrılıyor; `do…` açılıyor; `He doesn't goes.` tam, şapka sönüyor |
| 2,12 · 2,50 · 2,80 | `es` sarı çizgi; kırmızı `?`; çıkış başı (başlık ve `?` soluyor) |
| 3,00 · 3,23 | kart yukarı kayıyor, karakter çıkıyor; son kare kart y 480 |
| koyu 2,12 | okunur; kart açık zeminde, hap turuncu |
Taşma, kesik yazı, üst üste binme, okunmaz kontrast yok. Kanal katmanı her karede aynı yerde. Emoji yok.

Komut: `bash araclar/qa-yerel.sh simple-present-temel-s3b 01-hyperframes-kanca 0.00,0.90,1.15,1.40,1.65,2.12,2.50,2.80,3.00,3.23 2.12 --hazirla`.
Kapak A yöntemi kol a ile aynı (`ONIZLE_YALNIZ=1 bash calistir.sh --tema <t>` → `proje-ka[-koyu]` kopyası + `#altyazi{display:none}` →
`hyperframes snapshot . --at 0.9`); koyu kopyada logo `33189e5b`, açıkta `316d8df3`.
