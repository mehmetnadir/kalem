# Sahne 08-paperjs-kok3-soz (Paper.js, 1177 kare, t_bas 157.59) — 02-02-ydt-ileri

Tema: acik (son önizleme hazırlığı açık; koyu da koştu)

Durum: yazıldı, önizleme hazırlığı tamam. Kapı ve sahne-kare KOŞULMADI (şef EK 13.11 12:40). Render yok.

## İçerik
- c24: 'Kök 3' + 'Söz ve durum fiilleri' sözcük sözcük; kanca cümlesi (I now pronounce you husband and wife.) küçük kartta, pronounce sarı daire. 164,2–164,55 solar.
- c25–26: kök kartı (3 satır), think ve promise daireleri, pencil + clock çizimi, TR çeviri soluk el yazısı, düşünüyoruz ve veriyorum'da yor altı çizgi (yor hecesi kelime penceresinde orantılı: sapma >0,15 sn). 176,35–176,7 solar.
- c27: söz fiili kutusu (promise, pronounce + daire, accept, deny, inform; söylemek = yapmak), durum fiili kutusu (think, hope, iki sarı tik), alt şerit -yor ↔ -ing, -ing ikincil çarpı. Bölüm çipi Root 3 / 3.

## Olay ↔ sözcük t0 (parantez = bağlı sözcük; yerel kare = round((t − t_bas) × 30), sözcük zamanları sozcukler.json'dan okundu, sapma ≤ 0,03 sn; istisnalar altta)
| Olay | Kare | Küresel sn |
|---|---|---|
| Kök 3 (Üçüncü) | 16 | 158.12 |
| Kök 3 altı çizgi (kök:) | 31 | 158.62 |
| Söz (söz) | 55 | 159.42 |
| ve (ve) | 84 | 160.39 |
| durum (durum) | 91 | 160.62 |
| fiilleri (fiilleri.) | 100 | 160.92 |
| kanca kartı kutusu (Açılıştaki) | 132 | 161.99 |
| kanca cümlesi (tören) | 151 | 162.62 |
| pronounce daire (burada.) | 177 | 163.49 |
| kök kartı kutusu (We) | 211 | 164.62 |
| think daire | 221 | 164.96 |
| promise daire | 316 | 168.12 |
| pencil çizimi (report) | 344 | 169.06 |
| clock çizimi (tonight.) | 353 | 169.36 |
| yor altı çizgi (düşünüyoruz;) | 454 | 172.72 |
| yor altı çizgi (veriyorum.) | 549 | 175.89 |
| TR çeviri (İşin) | 385 | 170.42 |
| söz fiili kutusu (Promise) | 575 | 176.76 |
| promise (Promise) | 583 | 177.02 |
| söz fiili başlığı (söz) | 604 | 177.72 |
| söylemek (söylemek) | 638 | 178.86 |
| = yapmak (yapmak) | 659 | 179.56 |
| pronounce + daire (Pronounce) | 707 | 181.16 |
| accept (accept,) | 739 | 182.22 |
| deny (deny,) | 767 | 183.16 |
| inform (inform) | 800 | 184.26 |
| durum fiili kutusu (Think) | 864 | 186.39 |
| think (Think) | 872 | 186.66 |
| hope (hope) | 898 | 187.52 |
| durum fiili başlığı (durum) | 918 | 188.19 |
| tikler (alır) | 988 | 190.52 |
| -yor (yor) | 1033 | 192.02 |
| yor ↔ ing oku (İngilizcesi) | 1088 | 193.86 |
| -ing (ing) | 1117 | 194.82 |
| -ing çarpı (almaz) | 1134 | 195.39 |

## Kanıt
- `ONIZLE_YALNIZ=1 bash calistir.sh --tema koyu` ve `--tema acik` → "önizleme hazır" (son koşu AÇIK).
- `node --check sahne-*.js` temiz.
- Taklit koşu (Node, sahte DOM/Paper; scratchpad p2-ydt-ileri/harness.mjs): 1177 karenin tamamı hatasız; olaylar son 12 karede yok. Gerçek Paper geometrisi taklitte YOK: göz kontrolü QA şeridinde (düzen sayıları gerçek Fredoka/Caveat ölçüsüyle fontTools'tan hesaplandı).

## Sapma / dikkat
- sozcukler.json yolu kalem-paper.js'te doğrudan /projeler/02-02-ydt-ileri/ortak/anlatim (kunye.js KOK düzeltilmeden önce yanlıştı; artık aynı yer).
- Künye: SIMPLE PRESENT · YDT ADVANCED, ajanda Hook · Rule · Roots, çip bölüm kuralına göre.
- Kare yolları: `k/` boş (sahne-kare koşulmadı). calistir.sh denetim kareleri GLOBAL_SN satırında.


## QA 13.11
Kapı (sunucu): çakışma yok (157 örnek, 1430 kutu). Kareler: k/08-paperjs-kok3-soz-{161.5,172.4,183.2,195.9}.png (açık), k/koyu/…-177.8.png (koyu). Göz (gerçek Paper): yerleşim temiz, taşma yok, tik/çarpı/≠ okunur. Düzeltme: promise ve pronounce halkaları birbirine biniyordu (ry 44, satır aralığı 70) → ry 34 (sahne-08.js, iki daire çağrısı); yeniden koşu 183,2 karesi temiz. Kalan: yok.

QA 13.11 ek 2: Halka kuralı: think, promise (cümle), kanca kartı pronounce ve kök kartı listesindeki promise/pronounce halkaları altçizgiye çevrildi. Kapı: çakışma yok (157 örnek, 1427 kutu); k/08-paperjs-kok3-soz-172.4.png ve -183.2.png temiz.

QA 13.11 ek 3: simge–etiket/cümle taraması: çizimler cümleyle uyumlu (kod ve kareler üzerinden); uyuşmazlık yok.
