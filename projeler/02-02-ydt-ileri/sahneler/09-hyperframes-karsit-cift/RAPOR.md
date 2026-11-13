# Sahne 09 — Karşıt çift Mike (HyperFrames, 844 kare, t_bas 196,44, cümle 28–33)

Durum: P2 yazıldı. `ONIZLE_YALNIZ=1 bash calistir.sh --tema koyu`, sonra açık (son koşu AÇIK) tamam; id çakışması 0, GSAP hedefleri tam, `node --check` OK, assert'ler (kart/tablo sığması) geçti. Kapı ve sahne-kare KOŞULMADI (EK 13.11 12:40).
Künye: SIMPLE PRESENT · YDT ADVANCED, bölüm Contrast, ajanda Hook Rule Roots (etkin Roots). İlk olay 197,79; son 223,74 (içerik sonu 224,17).

## İçerik
Perde KARŞIT ÇİFT · sol kart Mike live|s and work|s / in Birmingham. (s kutuları) · uzun kalıcı bant + ok · home · TR soluk italik · kalıcı · live/work altı çizgi · sağ kart Mike is staying in / a hotel [this week]. (sarı köşeli ayraç) · kısa bant · bed · TR · geçici · yor altı çizgileri · fark tablosu (kalıcı → geniş zaman, geçici → şimdiki zaman).

## Olay ↔ sözcük t0
| Olay | Küresel sn | Sözcük (t0) |
|---|---|---|
| KARŞIT / ÇİFT perdesi | 197,79 / 198,27 | karşıt / çift. |
| Sol kart çizilir; Mike | 199,33 / 199,38 | Mike (199,38) |
| live + s kutusu | 199,86 / 200,04 | lives (199,86) |
| work + s kutusu | 200,58 / 200,76 | works (200,58) |
| Birmingham; zaman çizgisi, kalıcı bant | 201,22 / 201,27 / 201,67 | Birmingham. (201,22) |
| home ikonu + TR çeviri | 202,49 | Mike (202,49) |
| «kalıcı» + altı çizgi | 205,37 / 205,77 | Kalıcı / bir |
| live altı · work altı | 206,58 · 207,48 | Live · work |
| bant ok ucu | 208,21 | süreklilik |
| Sağ kart; zaman çizgisi | 210,04 / 210,88 | Mike / in |
| this köşeli ayraç · week. ayraç + kısa bant | 211,60 · 211,80 / 211,90 | this · week. |
| bed ikonu + TR | 212,83 | Mike (212,83) |
| «geçici» | 214,99 | Geçici |
| yor altı çizgileri (3) | 217,70 / 217,82 / 217,94 | yor (217,70) |
| Tablo çerçevesi | 218,74 | Fark (218,74) |
| kalıcı → geniş zaman | 220,42 / 221,22 / 221,62 | Kalıcı: / geniş / zaman. |
| geçici → şimdiki zaman | 222,34 / 223,22 / 223,62 | Geçici: / şimdiki / zaman. |

## Açık notlar
- Perde metni KARŞIT ÇİFT taslakta yok ("—", perde); süs sayılırsa `uret.py` C28 bloğu silinir.
- 4 sn'den uzun hareketsiz aralık yok (en uzun başlangıç aralığı < 4 sn, betikle ölçüldü).


## QA 13.11
Kapı: bu motor için ölçülmedi. Kareler: k/09-hyperframes-karsit-cift-{199.2,207,214.7,223.7}.png (açık), k/koyu/…-210.9.png (koyu). Göz: iki kart + bant + tablo, taşma/binme yok, koyu tema doğru. 223,7 karesinde tablonun son sözcüğü 'zaman' daha yazılıyor: tasarım gereği son olay 223,74 (içerik sonu 224,17), son 12 kare durgun. Düzeltme yok. Kalan: perde 'KARŞIT ÇİFT' taslakta yok (P2 notu); karar şefte.

zaman eşitleme 13.11: cümle 30 +0,38 sn. HyperFrames `--hazirla` ile sunucuda yeniden kuruldu (yeni sozcukler.json; cümle 30 sahne içinde, işaretler sözcük çapalı). Kareler 207,4 / 215,1 / 224,0: kalıcı/geçici etiketi, yor altçizgileri, tablo 'geniş zaman' (221,6) ve 'şimdiki' (223,6) sözcükten sonra geliyor.

QA 13.11 ek 3: simge–etiket/cümle taraması: çizimler cümleyle uyumlu (kod ve kareler üzerinden); uyuşmazlık yok.
