# Sahne 13 — Mini soru (HyperFrames, 916 kare, t_bas 242,28; cümle 16 soru + 17 öğrenci + 18 öğretmen)

Durum: P2 yazıldı, önizleme hazırlığı (ONIZLE_YALNIZ=1, son koşu açık tema) tamam. Render, kapı ve sahne-kare YOK (12:40 şef notu; QA şeridi koşar).
Dosyalar: `uret.py` · `olay.py` · `yardim.py` · `calistir.sh` · `proje/index.html` · `olaylar.json` (34 olay).
Kalıp: ileri `11-hyperframes-mini-soru` (kök kartı + 5 şıklı panel + sayaç + pil); 05-kok1 ile aynı yerleşim (kart 96,164 · panel y 470 adım 96 · pil x 1010).

## İçerik
- Kök kartı `I ____ this postcard now.` (kaynak boşluk 1; `now` taslakta eklenmiş sinyal). Şıklar taslak: A write · B am writing · C writes · D wrote · E is writing.
- Sayaç halkası «Beş şık var» (5) → şıklar sırayla gelir. Öğrenci yanlış cevabı A: balon (3 satır) + `ogrenci-bas.svg`, A satırı soluk sarı çerçeve; 0,75 sn duraklama ses dosyasında (255,75 → 256,42).
- Cevap: balon + çerçeve söner; `now` sarı belirteç; doğru B yeşil `#167A4A` (taslaktan birebir) + onay işareti + boşlukta yeşil çizgi; `am writing` boşluğa yazılır, sarı halka; A soluklaşır; `sik_not` pilleri: A `now ↔ write ✗`, D `now ↔ wrote ✗`, C `I ↔ writes ✗`, E `I ↔ is ✗`. Çarpılar sarı (kırmızı yok).
- Künye: `· YDT BASIC`, sağ üst `Mini question`, ajanda etkin Trap. Çıkış fade geçiş katmanında (sahne 13'ten sonra fade).

## Olay ↔ sözcük t0 (küresel sn)
| Olay | Sözcük (cümle.i) | Sözcük t0 | Olay t | Sapma |
|---|---|---|---|---|
| soru kartı (Mini) | Mini (16.0) | 242.83 | 242.83 | +0.00 |
| I yazılır | I (16.5) | 245.72 | 245.72 | +0.00 |
| this | this (16.6) | 246.63 | 246.63 | +0.00 |
| postcard | postcard (16.7) | 246.95 | 246.95 | +0.00 |
| now. | now. (16.8) | 247.59 | 247.59 | +0.00 |
| sayaç + şık satırları (Beş) | Beş (16.11) | 250.32 | 250.32 | +0.00 |
| öğrenci balonu + baş | Bence (17.0) | 251.75 | 251.57 | -0.18 |
| balon sözcük sözcük (Bence) | Bence (17.0) | 251.75 | 251.75 | +0.00 |
| A çerçevesi (A) | A (17.1) | 252.31 | 252.31 | +0.00 |
| balon söner (Hayır.) | Hayır. (18.0) | 256.42 | 256.42 | +0.00 |
| now. belirteç (Now) | Now (18.1) | 256.98 | 256.98 | +0.00 |
| A imleci (Now) | Now (18.1) | 256.98 | 256.98 | +0.00 |
| A pili now ↔ write ✗ (alışkanlığı) | alışkanlığı (18.5) | 259.50 | 259.50 | +0.00 |
| doğru B yeşil (B) | B (18.9) | 261.46 | 261.46 | +0.00 |
| boşlukta am writing (am) | am (18.12) | 262.98 | 262.98 | +0.00 |
| sarı halka (writing.) | writing. (18.13) | 263.22 | 263.32 | +0.10 |
| D imleci (D) | D (18.15) | 264.98 | 264.98 | +0.00 |
| D pili now ↔ wrote ✗ (now) | now (18.17) | 266.02 | 266.02 | +0.00 |
| C imleci (C) | C (18.22) | 268.66 | 268.66 | +0.00 |
| E imleci (E) | E (18.25) | 269.54 | 269.54 | +0.00 |
| C pili I ↔ writes ✗ (özne) | özne (18.27) | 270.50 | 270.50 | +0.00 |
| E pili I ↔ is ✗ (I) | I (18.28) | 271.06 | 271.06 | +0.00 |

Not: `Beş şık var` parçası 250,32–251,28; şıklar 0,18 sn aralıkla gelir (son satır 251,04). Cevap, öğrenciden 0,67 sn sonra başlar (≤ 2 sn).
Kontrol: tüm komut zamanları ilk 12 kare ve son 12 kare dışında (ihlal yok); `node --check` JS tamam; pil ve şık metni genişlik doğrulamaları (assert) geçti; kapı ve kare görüntüsü QA şeridine kaldı (`k/` boş).
Kare yolları: `k/` (QA şeridi dolduracak).

## QA 13.11
- Kapı: HyperFrames, ölçülmez. Kareler `k/13-hyperframes-mini-soru-{243,252,262,271.5}.png`, koyu `k/koyu/`.
- Düzeltme: doğru şık yeşil #167A4A ham rengi kaldırıldı (renk kuralı); B şık satırı vurgu çerçeveli + saydam vurgu dolgu, tik vurgu, yazı mürekkep (`uret.py`). Açık temada beyazlaşan yazı sorunu çıktı, yazı rengi tweeni kaldırılarak giderildi. Açık ve koyu karede doğrulandı.
- Göz: kök boşluğu halkası I ve this harflerine hafif değiyor; çeldirici notları (A, C, D, E) doğru. Kalan sorun yok.
- QA 13.11 ek (halka kuralı): kök boşluğu halkası el altçizgisine çevrildi (boşluk çizgisinin altında ikinci vurgu çizgisi), kare `k/13-hyperframes-mini-soru-271.5.png` doğrulandı; I ve this'e değen halka kalmadı.
- QA 13.11 ek 2: eklenen vurgu altçizgisi (fm0) kaldırıldı, yalnız boşluk çizgisi kaldı; sunucuda --hazirla ile kare alındı, `k/13-hyperframes-mini-soru-271.5.png` doğrulandı (tek çizgi).
- zaman eşitleme 13.11: yeniden kuruldu (t_bas 240,36, kare 911). Doğru şık: "B" 259,62 sn; 259,9 karesinde B satırı yanık, tik çiziliyor (`k/13-hyperframes-mini-soru-259.9.png`). Kareler 244,2–269,7 alındı.
