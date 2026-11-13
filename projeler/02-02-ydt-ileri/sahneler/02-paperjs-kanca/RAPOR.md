# Sahne 02-paperjs-kanca (Paper.js, 520 kare, t_bas 3.0) — 02-02-ydt-ileri

Tema: acik (son önizleme hazırlığı açık; koyu da koştu)

Durum: yazıldı, önizleme hazırlığı tamam. Kapı ve sahne-kare KOŞULMADI (şef EK 13.11 12:40). Render yok.

## İçerik
- Kare 0: cümle 1 (Sizi karı koca ilan ediyorum.) sahne 01'den gelen büyük yazı, kare 12'ye dek durgun; kare 12–24'te sol üste küçülür (söz yok, cümle 1 3,08'de bitti: sapma notu).
- c2: EN kart (Fredoka 80, sözcük zamanlı), pronounce sarı daire, iki halka (husband, wife; kalem elipsi).
- c3: alt satır ediyorum ↔ EN pronounce oku, ≠, -ing ve ikincil çarpı, şimdiki zaman el yazısı, ediyorum altı çizgi, ediyorum→ing yayı; küçük TR cümlede ediyorum sarı daire. 15,2–15,55 sn solar.
- c4: SIMPLE PRESENT kutuda, künyeye uçar (formülü), ajanda Rule ve Roots sarı çizgi (künye kutusunun altı), 3 sarı halka (1,2,3) + 1 ikincil boş halka (tuzak), parıltı. Kırmızı yok.

## Olay ↔ sözcük t0 (parantez = bağlı sözcük; yerel kare = round((t − t_bas) × 30), sözcük zamanları sozcukler.json'dan okundu, sapma ≤ 0,03 sn; istisnalar altta)
| Olay | Kare | Küresel sn |
|---|---|---|
| TR cümle küçülür (cümle 1 bitti 3,08; ilk 12 kare durgun) | 12 | 3.40 |
| cümle 2 başı (I) | 19 | 3.63 |
| kart kutusu | 19 | 3.63 |
| pronounce daire | 39 | 4.30 |
| halka 1 (husband) | 62 | 5.07 |
| halka 2 (wife) | 89 | 5.97 |
| ediyorum (alt satır) | 139 | 7.63 |
| ediyorum daire (küçük cümle) | 139 | 7.63 |
| şimdiki zaman etiketi (şimdiki) | 172 | 8.73 |
| ediyorum ↔ pronounce oku (İngilizcede) | 206 | 9.87 |
| -ing (ing) | 230 | 10.67 |
| ≠ işareti (ing) | 230 | 10.67 |
| -ing çarpı (yok.) | 241 | 11.03 |
| ediyorum altı çizgi (güvenirsen) | 273 | 12.10 |
| ediyorum → ing yayı (seni) | 314 | 13.47 |
| parıltı (götürür) | 346 | 14.53 |
| başlık kutusu (Bu) | 381 | 15.70 |
| SIMPLE (derste) | 389 | 15.97 |
| PRESENT (derste) | 393 | 16.10 |
| başlık künyeye uçar (formülü) | 402 | 16.40 |
| ajanda Rule (formülü) | 406 | 16.53 |
| ajanda Roots (kökünü) | 443 | 17.77 |
| kök halkası 1 (üç) | 424 | 17.13 |
| kök halkası 2 (sınav) | 431 | 17.37 |
| kök halkası 3 (kökünü) | 443 | 17.77 |
| tuzak halkası (bir) | 467 | 18.57 |
| parıltı (görüyoruz) | 484 | 19.13 |

## Kanıt
- `ONIZLE_YALNIZ=1 bash calistir.sh --tema koyu` ve `--tema acik` → "önizleme hazır" (son koşu AÇIK).
- `node --check sahne-*.js` temiz.
- Taklit koşu (Node, sahte DOM/Paper; scratchpad p2-ydt-ileri/harness.mjs): 520 karenin tamamı hatasız; olaylar son 12 karede yok. Gerçek Paper geometrisi taklitte YOK: göz kontrolü QA şeridinde (düzen sayıları gerçek Fredoka/Caveat ölçüsüyle fontTools'tan hesaplandı).

## Sapma / dikkat
- sozcukler.json yolu kalem-paper.js'te doğrudan /projeler/02-02-ydt-ileri/ortak/anlatim (kunye.js KOK düzeltilmeden önce yanlıştı; artık aynı yer).
- Künye: SIMPLE PRESENT · YDT ADVANCED, ajanda Hook · Rule · Roots, çip bölüm kuralına göre.
- Kare yolları: `k/` boş (sahne-kare koşulmadı). calistir.sh denetim kareleri GLOBAL_SN satırında.


## QA 13.11
Kapı: çakışma yok (69 örnek, 393 kutu). Kareler: k/02-paperjs-kanca-{4.5,8.5,12.5,18.7}.png (açık), -11.png (koyu; bakılmadı). Göz: 12,5 sn'de ediyorum/pronounce/≠ -ing düzeni temiz, boşluk yeterli. 4. boş halka: 18,57 sn'de anlatımda 'bir tuzağı' geçiyor (taslakta halka yok ama söz var) → kalsın. 3,40 sn küçülme ve 08 alt çizgi sapması şef kararıyla kabul. Düzeltme yok. Kalan: gerçek Paper geometrisi göze iyi; sorun yok.

QA 13.11 ek: Koyu kare: k/koyu/02-paperjs-kanca-11.png bakıldı, renk hatası yok, yazı/halka okunur.

QA 13.11 ek 2: Halka kuralı: 'pronounce' (now/you'ya değiyordu) ve küçük cümledeki 'ediyorum' (ilan'a değiyordu) halkaları vurgu renginde el altçizgisine çevrildi (sahne-02.js alt()); sözcük göründükten ~10 kare sonra başlar. Değmeyen halkalar (husband/wife, 1-2-3, tuzak) kaldı. Sunucuda kapı: çakışma yok (69 örnek, 393 kutu); k/02-paperjs-kanca-12.5.png temiz.
