# Sahne 06 — Soru anı 1 (HyperFrames, 589 kare, t_bas 68,56; cümle 6 öğrenci + 7 öğretmen)

Durum: P2 yazıldı, önizleme hazırlığı (ONIZLE_YALNIZ=1, son koşu açık tema) tamam. Render, kapı ve sahne-kare YOK (12:40 şef notu; QA şeridi koşar).
Dosyalar: `uret.py` · `olay.py` · `yardim.py` (ileri kök1 ile aynı) · `calistir.sh` · `proje/index.html` · `olaylar.json` (32 olay).

## İçerik
- Kare 0: örnek 3 kartı (It is getting harder and harder … nowadays.) statik; `harder and harder` sarı belirteç, `nowadays.` sarı halka (sahne 05'ten devam).
- Soru anı 1: öğrenci başı (`ogrenci-bas.svg`) + el balonu, soru sözcük sözcük; `-ing?` sarı belirteç; sarı nokta balonu kartın `harder and harder` satırına bağlar. 0,75 sn duraklama ses dosyasında (73,35 → 74,02): bu aralıkta olay yok.
- Cevap (74,02, soru bitişinden 0,67 sn sonra): balon söner; kalemle yükselen ok; `CHANGING → mostly -ing` kartı; üç örnek kartı sağ köşede küçülüp üst üste durur (PLAN · PERIOD · CHANGING); fiillerde (leaving · going · getting) sarı halka.
- Künye: `PRESENT CONTINUOUS vs SIMPLE PRESENT · YDT BASIC` (kunye.js ile aynı), sağ üst `Question`, ajanda etkin Examples.
- yanılgı: değişen durum (`harder and harder`) genel gerçek sanılır. Soru 9 sözcük (≤ 12). Kırmızı yok.

## Olay ↔ sözcük t0 (küresel sn)
| Olay | Sözcük (cümle.i) | Sözcük t0 | Olay t | Sapma |
|---|---|---|---|---|
| balon + baş çizimi (ilk 12 kare durgun) | Hocam, (6.0) | 69.11 | 68.99 | -0.12 |
| soru sözcükleri tek tek (ör. 'Hocam,') | Hocam, (6.0) | 69.11 | 69.11 | +0.00 |
| sarı nokta (zorlaşmak) | zorlaşmak (6.1) | 69.91 | 69.91 | +0.00 |
| -ing? sarı belirteç | -ing? (6.8) | 72.87 | 72.87 | +0.00 |
| balon + baş söner (cevap başı) | Durum (7.0) | 74.02 | 74.02 | +0.00 |
| yükselen ok (değişiyor.) | değişiyor. (7.2) | 74.90 | 74.90 | +0.00 |
| sarı halka (değişimde.) | değişimde. (7.5) | 77.14 | 77.14 | +0.00 |
| cevap kutusu çizimi (sözcükten önce) | değişimde. (7.5) | 77.14 | 77.44 | +0.30 |
| CHANGING (Değişen) | Değişen (7.6) | 78.18 | 78.18 | +0.00 |
| ok (çoğunlukla) | çoğunlukla (7.8) | 78.98 | 78.98 | +0.00 |
| mostly (çoğunlukla) | çoğunlukla (7.8) | 78.98 | 79.10 | +0.12 |
| -ing (şimdiki) | şimdiki (7.9) | 79.70 | 79.70 | +0.00 |
| -ing belirteç (zamanla) | zamanla (7.10) | 80.10 | 80.10 | +0.00 |
| büyük kart küçülür (Üç) | Üç (7.12) | 81.30 | 81.30 | +0.00 |
| PLAN çipi (plan,) | plan, (7.18) | 83.34 | 83.34 | +0.00 |
| PERIOD çipi (dönem,) | dönem, (7.19) | 83.94 | 83.94 | +0.00 |
| CHANGING çipi (değişim.) | değişim. (7.20) | 84.66 | 84.66 | +0.00 |
| fiillerde halka (şimdiki) | şimdiki (7.22) | 86.26 | 86.26 | +0.00 |

Not: kutu çizimi, kayma ve mini kart gelişleri (81,75 · 82,15 · 82,35 · 82,60) sözcüğe bağlı değil, dolgu zamanı; `Üç örnekte de bir ipucu var` (81,30–83,14) süresince yığın kurulur.
Kontrol: tüm komut zamanları ilk 12 kare ve son 12 kare dışında (ihlal yok); `node --check` JS tamam; kapı ve kare görüntüsü QA şeridine kaldı (`k/` boş).
Kare yolları: `k/` (QA şeridi dolduracak).

## QA 13.11
- Kapı: HyperFrames, ölçülmez. Kareler `k/06-hyperframes-soru1-{69.5,73,80,87.2}.png`, koyu `k/koyu/` (sunucuda alındı).
- Düzeltme: son karedeki üç fiil halkası (`uret.py`) are/is yazısını örtüyordu; halka yalnız fiile daraltıldı (`wv/2+5`, +2 kaydırma). Yeniden karede are/is serbest, halka yalnız leaving/going/getting üstünde. `leaving` halkası l harfine hafif değiyor, okunurluk bozulmadı.
- Göz: soru anı balonu, bağlantı noktası, CHANGING kartı doğru; koyu tema doğru. Kalan sorun yok.
- QA 13.11 ek (halka kuralı): üç fiil halkası el altçizgisine çevrildi (`uret.py`), kare `k/06-hyperframes-soru1-87.2.png` doğrulandı; are/is serbest, halka kalmadı.
- zaman eşitleme 13.11: yeni zaman.json/sozcukler.json (t_bas 68,56 → son −0,08). HyperFrames: zaman uret.py içinde sözcükten okunur; `--hazirla` ile sunucuda yeniden kuruldu, kareler `k/06-hyperframes-soru1-{72.9,77.3,81.6,86.4}.png` alındı.
- QA 13.11 ek (halka/kutu taraması): büyük karttaki nowadays halkası altçizgi oldu; harder and harder halkası zaten altı çizili olduğundan kaldırıldı (çift çizgi kalabalıktı). Kare `k/06-hyperframes-soru1-77.5.png` doğrulandı.
