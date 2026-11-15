# KAPAK-0206I — present-perfect-ileri ana ders kapakları · 15.11.2026

| Dosya (`file`) | Boyut | Tema |
|---|---|---|
| `present-perfect-ileri/kapak.png` · `kapak-koyu.png` | 1920×1080 | açık · koyu |
| `present-perfect-ileri-dikey/kapak.png` · `kapak-koyu.png` | 1080×1920 | açık · koyu |
| `present-perfect-ileri/uretim-tutanagi/kapak-168.png` | 168×94 | açık |

**Yöntem.** Emsal `simple-present-temel/sahneler/90-hyperframes-kapak/` kopyası (`uret.py`, `yardim.py`, `calistir.sh`; dikey `calistir.sh` ana üreticiyi `--duzen dikey` ile çağırır). Dikey görseller `present-perfect-ileri-dikey/ortak/kapak` göreli bağından gelir. Kare: `hyperframes snapshot --at 0.5`. `zaman.json`, `surumler.json` ve öteki sahneler değişmedi.

**Emsalden farklar.** (1) Metin: `AGO VARSA` · vurgu `PERFECT YOK` · `ago → Simple Past` · `YDT · İLERİ`. (2) Vurgu kutusu 6,8 em uzun. Yazı boyu yatayda 240 → 150, dikeyde 190 → 136. Yatay karakter 1,05 → 0,94, sağa kaydı (sağ alt boş bölge sınırı). Dikey karakter 0,64 → 0,76, kesim satırı 1000 aynı. (3) Takvim: yatayda karakterin sol altında, dikeyde karakterin solunda. Krem daire yazıdan ≥ 24 px uzakta. (4) Küçük S için satır 1 ile kutu arası en az 31 px. Satır 1 üstü en yüksek glife göre ölçülür. Küçük satır kutusu "i" noktasını ve "p" uzantısını kapsar. (5) Kırıntı temizliği `02-04-ydt-temel` kapak yöntemiyle eklendi: kopyada alfa ≤ 64 sıfırlanır, sonra 3×3 açılış uygulanır. (6) `calistir.sh` eski kök kapağı `~/Silinecekler/2026-11-15-kapak/` dizinine taşır.

| Kapı (§5) | Sonuç | Bakılan |
|---|---|---|
| 4 PNG, boyut | GEÇTİ: 1920×1080 ×2, 1080×1920 ×2 | `file` |
| 168 px küçük görünüm | GEÇTİ: `AGO VARSA / PERFECT YOK` okunur, yüz seçilir (koyu 168 kopyası da) | Read |
| Glif (İ/Ş/Ğ) | GEÇTİ: ana yazıda İ/Ş/Ğ yok. Rozetteki `İ` Lexend latin-ext; `uret.py` her harfi `assert` ile denetler | rozet kesiti |
| Yazı ↔ karakter | GEÇTİ: `assert` (kenar 10 + pay 24 px) ve göz denetimi | 4 PNG |
| Sağ alt %15×%8 | GEÇTİ: zeminden farklı piksel 0 / 25.056 (iki tema) | numpy |
| Dikey üst/alt %20 | GEÇTİ: 0 / 414.720 (her bölge, iki tema). İçerik y 400–1520 | numpy |

**Kusur turu (1).** Kaynak PNG'lerde kenar dışında 1–2 px'lik ayrık kırıntı vardı (karakter 328, takvim 328). Kenar gölgesi kırıntıları büyütüyordu, kenar pürüzlü görünüyordu. Kopya temizlendi, 4 kare yeniden çekildi. Karakter artık tek parça, takvimde 7 parça kaldı (hız çizgileri ve yapraklar). Kaynak `ortak/kapak/` değişmedi. İlk 4 kare Silinecekler'de.

**Açık kalan (şef kararı).** (a) Yatay yazı boyu 150 px = kapağın %14'ü; standart %18–24 der. Sebep: vurgu satırı uzun. Daha büyük yazı için karakter küçülmeli ya da metin kısalmalı. (b) Dikey düzende karakter ortadan 160 px sağda. Takvimle birlikte ortalı (orta 557). (c) Takvimin ince hız çizgilerinde krem kenar 3× büyütmede hafif tırtıklı görünür; 1× boyutta seçilmez. (d) Açık temada logo tek renk `#141414` (emsal kararı).
