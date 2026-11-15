# RAPOR — 02-04-ydt-temel-s3 · sahne 05-hyperframes-kapak-b (kapak B, soru) · huni v2 · 15.11.2026

Tema: acik

| Kapı | Sonuç |
|---|---|
| Tek kare açık | `P/kapak-b.png` 1080×1920 (ffprobe `png,1080,1920`) |
| Tek kare koyu | `D/k/koyu/kapak-b-koyu.png` 1080×1920 |
| Kanal katmanı | açık + koyu: logo ve `@ydspublishing` görünür; logo görünür sol kenar x 60, y 296–339 içinde |
| Metin taraması (`tam ders`, `dakika`, `D/proje`) | sonuç yok (grep çıkış 1) |
| Çakışma kapısı | çıkış 2 (sahne `sahneler[]` dışında; araç sınırı, aşağıda aynen) |
| uret.py iç denetimleri | 13 blok, kesişim 0, boşluklar, hex kümesi, yasak sözler: geçti |
| Bakılan PNG | açık + koyu (tek kare: ilk = orta = son) |

P = `K/projeler/02-04-ydt-temel-s3/`, D = `P/sahneler/05-hyperframes-kapak-b/`. Yol: SPEC.md (şef) → uret.py (agy) → şef okuma + 1 küçük düzeltme.

## Öğe listesi

| Öğe | Kimlik | y bandı (px) | Yazı boyu |
|---|---|---|---|
| Kanal: logo (tema logosu) | `#kunye > #kanal > #logoimg` | 291–339 (resim x 53,15, w 193,49) | — |
| Kanal: `@ydspublishing` | `#kanal-ad` | taban 330, x 263 | Lexend 700 42 |
| Rozet `YDT · BASIC` (yalnız rozet, kapak A son konumu) | `#rz0` | 386–434, x 664,6–868,2 | Lexend 700 26 |
| Başlık `NEDEN -ING` | `#bs-1` | taban 590,8 (blok 470–) | Fredoka 700 164 |
| Başlık `YOK?` sarı hapta | `#bk-hap`, `#bs-2` | hap 617–781, x 261–758 | Fredoka 700 164 |
| Saat (akrep 7, yelkovan 12, rakamsız) | `#saat` | 874–994 | — |
| El çizimi sarı `?` (kabin üstü) | `#soru` | 874–991 | — |
| Tren + duman + ray | `#tren` | 984–1178, x 64–520 | — |
| Karakter görseli (krem çıkartma kenarı 10 px) | `#karakter` (`<img>`) | görünür 820–1227, x 578–948; kenarla 810–1237, x 568–958 | — |
| Krem daire (yalnız açık tema) | `#daire` (`<div>`) | 802–1095, x 622–915, r 146,3 | — |
| Kart `The train leaves …` | `#kart`, `#kart-yazi` | 1254–1378, x 60–753 | Fredoka 700 72 |
| `leaves` sarı altçizgi | `#alti` | 1350–1369 | — |
| Altyazı | yok (standart §6) | — | — |

Başlık boyu: `900 px'e sığan en büyük, üst sınır 170` → S = 164 (satır 1 genişliği 896,6). Karakter ölçeği: dosya kutusu 520 px
(896×1200 → 388×520; `SK = 520/1200`); kırpılmış görünür kutu 370,1×406,5. Kırıntı temizliği alfa ≤ 64 + 3×3 açılış (90-kapak kalıbı).

## Kanal katmanı ölçümü (PNG piksel taraması, mürekkep/doygun piksel kutusu)

| Tema | Logo görünür kutu (x0, y0, x1, y1) | Yazı görünür kutu | 0–280 | x 962+ | y 1380+ |
|---|---|---|---|---|---|
| açık | 60, 298, 239, 330 | 265, 296, 595, 339 | boş | boş | boş |
| koyu | 60, 298, 239, 330 | 265, 296, 595, 339 | boş | boş | boş |

İçerik görünür kutusu: açık x 60–950, y 476–1377 · koyu x 60–956, y 476–1377 (koyuda krem kenar görünür). Karakter (kenar dahil,
koyu) x 566–956, y 808–1235; kart y 1254–1377 → ara 19 px. Başlık alt 780 → karakter kenarı 808 → ara 28 px.

## Kapı (son satırlar, aynen)

```
$ node araclar/cakisma-kapisi.mjs 02-04-ydt-temel-s3 --sahne 05-hyperframes-kapak-b --port 41333 --sunucu 41022
HATA sahne bulunamadı: 05-hyperframes-kapak-b
çıkış=2
```

## Bakılan kareler ve bulgu

| Kare | Bulgu |
|---|---|
| `P/kapak-b.png` (açık) | taşma yok; kesik yazı yok; üst üste binme yok; 0–280 boş; içerik x ≤ 960; altyazı yok; hap `#ffe066` + yazı `#1b2440`; `?` ve altçizgi `#d9900f` |
| `D/k/koyu/kapak-b-koyu.png` (koyu) | aynı yerleşim; daire yok; krem çıkartma kenarı karakterin siyah çizgisini zeminden ayırır; logo şeffaf sürüm |

Düzeltme turu: 1 (render öncesi). agy satır 623'e `#root.tema-acik #daire` yazdı (SPEC'in ilk sürümü bu kalıbı veriyordu);
`hf_tema.py` bu dizgeyi "tema CSS'i var" sayar, açık tema koyu çıkardı. Şef `.tema-acik #daire` yaptı ve assert ekledi. Render sonrası düzeltme yok.
`calistir.sh`: `uret.py && olay.py` zinciri iki satıra ayrıldı (sözleşme: `set -e` zincirde uret.py hatasını yutar). Yeniden koşu: iki PNG md5 aynı.

## agy koşu özeti
`/home/sef/.claude/canavar/agy-filo/20261115-191206/ozet.md` — rol `kod`, gemini-3.8-flash-high, 360 sn, başarılı; yazılan dosya `D/uret.py`.
Özetin "değişen" listesindeki `.claude/docs/sozlesme.md` ve `projeler/02-03-ydt-temel/sahneler/90-hyperframes-kapak/*` eş oturumların izidir
(çalışma ağacı farkı); ajan raporu yalnız `uret.py` yazdığını söyler.

## Açık noktalar
- Krem daire (`#f3efe6`) açık zeminde (`#f7f3ea`) çok soluk görünür; `kapak-standardi.md` sarı zemin için yazıldı. Kural aynen uygulandı; renk kararı Nadir'de.
- Karakter `<img>` olarak `#sahne` svg'sinin dışındadır: `araclar/hf-kutu.mjs` onu ölçmez. Çakışma uret.py blok denetimi ve PNG piksel ölçümüyle sınandı.
- "yükseklik ≈ 520" dosya kutusu olarak okundu (görünür 406,5). Görünür 520 seçilirse karakter 475 px genişler ve kartla çakışır.
- Ana ders `02-04-ydt-temel` ve S1 paketi okundu, değişmedi. `P/ortak/kapak/karakter.png` ana ders kopyası (`cmp` eşit).
