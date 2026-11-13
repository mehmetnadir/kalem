# Sahne 05-paperjs-kok1-haber (Paper.js, 515 kare, t_bas 74.89) — 02-02-ydt-ileri

Tema: acik (son önizleme hazırlığı açık; koyu da koştu)

Durum: yazıldı, önizleme hazırlığı tamam. Kapı ve sahne-kare KOŞULMADI (şef EK 13.11 12:40). Render yok.

## İçerik
- c11: 'Kök 1 · Özet' (Özet sarı, altı çizgi); haber başlığı / film / spor yorumu el yazısı, sözcük anında. 80,30–80,65 solar.
- c12: gazete çerçevesi (çift çizgi), 2 satır Fredoka 84 başlık, blocks sarı daire, üç sütun kuralı.
- c13: car çizimi, TR çeviri soluk el yazısı, 'haber sunumu → geniş zaman' (geniş zaman sarı), parıltı. Bölüm çipi Root 1 / 3.

## Olay ↔ sözcük t0 (parantez = bağlı sözcük; yerel kare = round((t − t_bas) × 30), sözcük zamanları sozcukler.json'dan okundu, sapma ≤ 0,03 sn; istisnalar altta)
| Olay | Kare | Küresel sn |
|---|---|---|
| Kök 1 (Birinci) | 16 | 75.42 |
| · Özet (özet.) | 50 | 76.56 |
| Özet altı çizgi | 53 | 76.66 |
| haber başlığı (Haber) | 79 | 77.52 |
| film (film) | 115 | 78.72 |
| spor yorumu (spor) | 135 | 79.39 |
| gazete çerçevesi (Truck) | 177 | 80.79 |
| başlık yazısı (Truck) | 177 | 80.79 |
| blocks daire | 208 | 81.82 |
| gazete kuralları (hours.) | 261 | 83.59 |
| car çizimi (Kamyon) | 301 | 84.92 |
| TR çeviri (Kamyon) | 301 | 84.92 |
| haber sunumu (Haber) | 405 | 88.39 |
| ok (olay) | 450 | 89.89 |
| geniş (geniş) | 462 | 90.29 |
| zaman (zamanla) | 472 | 90.62 |
| parıltı (zamanla) | 476 | 90.76 |

## Kanıt
- `ONIZLE_YALNIZ=1 bash calistir.sh --tema koyu` ve `--tema acik` → "önizleme hazır" (son koşu AÇIK).
- `node --check sahne-*.js` temiz.
- Taklit koşu (Node, sahte DOM/Paper; scratchpad p2-ydt-ileri/harness.mjs): 515 karenin tamamı hatasız; olaylar son 12 karede yok. Gerçek Paper geometrisi taklitte YOK: göz kontrolü QA şeridinde (düzen sayıları gerçek Fredoka/Caveat ölçüsüyle fontTools'tan hesaplandı).

## Sapma / dikkat
- sozcukler.json yolu kalem-paper.js'te doğrudan /projeler/02-02-ydt-ileri/ortak/anlatim (kunye.js KOK düzeltilmeden önce yanlıştı; artık aynı yer).
- Künye: SIMPLE PRESENT · YDT ADVANCED, ajanda Hook · Rule · Roots, çip bölüm kuralına göre.
- Kare yolları: `k/` boş (sahne-kare koşulmadı). calistir.sh denetim kareleri GLOBAL_SN satırında.


## QA 13.11
Kapı: çakışma yok (68 örnek, 2082 kutu). Kareler: k/05-paperjs-kok1-haber-{76.6,81.3,86,91.2}.png (açık), -83.6.png (koyu; bakılmadı). Göz: gazete kutusu, halka, çeviri, geniş zaman satırı çakışmıyor. Küçük not: 'Kamyon' çevirisi yanında çizim binek araba (tabler car); anlam kaybı yok, değiştirilmedi. Düzeltme yok.

QA 13.11 ek: Koyu kare: k/koyu/05-paperjs-kok1-haber-83.6.png bakıldı, renk hatası yok. Şef kararı 3: 'Kamyon' çevirisinin yanındaki binek araba çizimi kamyonla değiştirildi (kamyon.svg sahne klasöründe, Tabler truck çizgi stili; svgCiz yolu ../../sahneler/05-paperjs-kok1-haber/kamyon.svg; sahne-05.js). Sunucuda kapı: çakışma yok (68 örnek, 2083 kutu); k/05-paperjs-kok1-haber-91.2.png karesinde kamyon çiziliyor, temiz.

QA 13.11 ek 2: Halka kuralı: 'blocks' halkası (accident/traffic'e değiyordu) altçizgiye çevrildi. Kapı: çakışma yok (68 örnek, 2082 kutu); k/05-paperjs-kok1-haber-91.2.png temiz.

QA 13.11 ek 3: simge–etiket/cümle taraması: çizimler cümleyle uyumlu (kod ve kareler üzerinden); uyuşmazlık yok.
