# Sahne 07 — Karşıt çift (düz canvas, 1845 kare, t_bas 157,88, cümle 28–38)

Durum: P2 yazıldı, önizleme hazırlığı koşuldu (açık tema son). Render, kapı (çakışma) ve kare görüntüsü YOK (şef EK 13.11 12:40: QA şeridi koşar).
Tema: açık (K19). Künye: ortak/kunye.js (SIMPLE PRESENT · YDT BASIC · Hook Examples Rule Trap), bölüm "Contrast pair", etkin 2 (Rule).

## İçerik (ekran metni taslak §4 satır 4.1–4.11, değişmedi)
- 28 bölünmüş ekran: dikey ayraç. 29–30 sol kart (She eats fish every day) + takvim noktaları + TR çeviri + her gün → rutin.
- 31–32 sağ kart (She is eating fish now) + now noktası (nabız) + TR çeviri + şu anda → olay sürüyor.
- 33 fark tablosu: every day · always · usually → geniş zaman | now · look (çoğunlukla) → şimdiki zaman.
- 34 -yor ↔ -ing bağı, çarpı; rutin → geniş zaman; şu an → şimdiki zaman (soluk).
- 35–37 kanca cümlesi geri gelir (kartın içine yazılır), every morning halkası, I am getting up çarpılı → yeşil tik, -ing yok, am yok.
- 38 ek değil, anlam; kartta every morning parlar.

## Olay ↔ sözcük t0
| Olay | Küresel sn | Sözcük (t0) |
|---|---|---|
| Ayraç çizgisi | 159,23 | karşıt (159,23) |
| Takvim ekseni + 7 nokta | 162,34 / 162,60+ | day. (162,34) |
| Sol TR çeviri yazılır | 163,37 | Her (163,37) |
| every day halkası + «her gün» | 166,34 | Every (166,34) |
| «→ rutin» | 167,55 | rutin (167,55) |
| Sağ eksen + now noktası | 170,34 / 170,70 | now. (170,34) |
| Sağ TR çeviri | 171,37 | Şu (171,37) |
| now halkası + «şu anda → olay sürüyor» | 175,46 | Now (175,46) |
| İki fish halkası (soluk) | 179,86 | balık (179,86) |
| every day · always · usually | 183,07 · 184,19 · 185,23 | Every · always, · usually: |
| → geniş zaman | 186,44 | geniş (186,44) |
| now · look · çoğunlukla · → şimdiki zaman | 188,05 · 189,19 · 189,84 · 190,72 | Now · look · çoğunlukla · şimdiki |
| -yor çipi | 195,75 | yor, (195,75) |
| rutin (sarı) | 197,11 | rutin. (197,11) |
| -ing çipi + bağ okları | 197,99 / 198,30 | İngilizcede (197,99) |
| Bağ üstüne çarpı | 198,95 | o (198,95) |
| → geniş zaman | 199,67 | geniş (199,67) |
| Kanca kartı geri gelir | 201,34 | Kanca (201,34) |
| Kartta cümle yazılır | 203,33 | I (203,33) |
| every morning halkası | 204,53 | every (204,53) |
| Yeşil tik (çarpı söner) | 209,92 | I (209,82; tik +0,10) |
| -ing çarpılı · am çarpılı | 211,35 · 212,81 | Ing · am |
| ek değil, | 215,93 | ekine (215,93) |
| Çizgi, parıltı, anlam | 216,25 · 216,89 · 218,17 | değil, · zaman · anlama |

Sapma: elle yazılan zaman yok; her `tb` `T(sözcük, yakın)` ile sozcukler.json'dan okunur (bulunamazsa sahne yüklenmez). Kasıtlı ofsetler: kartlar sözcükten 0,37 sn önce çizilir; kalıcı alt çizgiler kayan çizgi söndükten sonra (163,50 · 171,55).

## Yapılan doğrulama (kapı yerine)
- `node --check sahne.js` ve `sahne-ortak.js`: tamam.
- Sahte tarayıcıyla (mock canvas) kur() + 47 örnek kare (ilk 12, son 12 dahil): 0 hata; ilk görünme karesi 40 (≥ 12); içerik karesi 1833 ile 1844 aynı çizim sayısı (son 12 kare durgun).
- Sahne içi sönme: gerçek alfa çarpanı (globalAlpha yazımı çarpılır; 02-03 ileri'deki `solar` darbe/metinPop alfasını ezdiği için o kalıp kullanılmadı).

## Kapı çıktısı
Koşulmadı (EK 13.11 12:40). Kare görüntüsü yok; `k/` boş. QA şeridi şunlara bakmalı: sol/sağ kart altı (TR çeviri ile formül satırı y 650 yakınlığı), tablo sütunları (y 560–830), 34'te -yor/-ing çipleri ve çarpı, kanca kartı sağındaki I am getting up çarpısı ile yeşil tik.

## Açık notlar
- Yeşil tik/doğru rengi `#167A4A` (soru sahnesiyle aynı); kunye TEMALAR'da yeşil yok. Şef istemezse sarı tike çevrilir (sahne.js `YESIL`).
- Kırmızı kullanılmadı (BRIEF: kırmızı yalnız tuzak sahnesinde).
- 34'teki «şu an → şimdiki zaman» satırı taslak ekran metninde var ama anlatımda söylenmiyor; soluk yazıldı.

## QA 13.11
- Düzeltme (sahne.js): YESIL `#167A4A` → `RT.vurgu`; 34'teki "şu an → şimdiki zaman" satırı (anlatımda yok) kaldırıldı. `ONIZLE_YALNIZ=1 bash calistir.sh` koşuldu (açık). Yedek: scratchpad/sahne-07.js.yedek.
- Kapı/kare: ALINAMADI (CDP zaman aşımı; sunucu-qa 30 dk takıldı, öldürüldü). Kontrol edilecek: TR çeviri (y 470–535) ile formül satırı (y 650) aralığı, tablo, kanca kartı tik.
- 2. tur (sunucu): kapı çakışma yok (246 örnek, 3633 kutu). Kareler k/07-…-160.5, -170, -190, -200, -213, k/koyu -205. TR çeviri (y 470–535) ile formül satırı (y 650) arası yeterli, sıkışma yok; tablo sütunları ve tik/çarpı okunur. Yeşil artık vurgu. Kalan yok.

- Halka kuralı: DEĞİŞTİ: `every day`, `Now`, iki `fish` (soluk), kanca `every morning` halkaları → altçizgi (halka() altçizgi; every day day 166,74 sonrası, every morning 204,85 sonrası). BIRAKILDI: takvim ve now noktaları (satır dışı, metne değmiyor). Kapı: çakışma yok (249 örnek, 3866 kutu); kare k/…-176.3, -206.

- zaman eşitleme 13.11: KARE 1845→1871, ICERIK 1833→1859, TBAS 157.88→157.54. 70 sabit zaman eşlendi (başta −0,34; cümle 37–38 +0,54; SON dizisi dahil). T() çapaları yeni sözcüğe uyuyor. Kapı temiz (249 örnek, 3914 kutu); kareler k/…-166.6 (her gün çıktıktan sonra), -210.4 (tik), -217.2 (ek değil).
