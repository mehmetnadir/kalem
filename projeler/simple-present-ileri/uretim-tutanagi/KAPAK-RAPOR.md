# KAPAK-0202I — simple-present-ileri ana ders kapakları · 15.11.2026
| Dosya (`file`) | Boyut | Tema |
|---|---|---|
| `simple-present-ileri/kapak.png` · `kapak-koyu.png` | 1920×1080 | açık · koyu |
| `simple-present-ileri-dikey/kapak.png` · `kapak-koyu.png` | 1080×1920 | açık · koyu |
| `simple-present-ileri/uretim-tutanagi/kapak-168.png` | 168×94 | açık |

Yöntem: `simple-present-temel/sahneler/90-hyperframes-kapak/` kopyası (`uret.py`, `yardim.py`, `calistir.sh`); dikey `calistir.sh` ana betiği `SAHNE=` ile çağırır; `simple-present-ileri-dikey/ortak/kapak` → ana paket `ortak/kapak` göreli bağ. Kare `hyperframes snapshot --at 0.5`. Sahne kodu, `zaman.json`, `surumler.json` değişmedi.
**Emsalden farklar.** (1) Metin `YARIN ama` (S1 170) · vurgu `WILL YOK` (184 yatay, 190 dikey) · Lexend `The flight takes off at nine.` (56/44, ok yok) · `YDT · İLERİ`. Satır 1 vurgudan küçük (02-04 emsali gibi; 190'da sol %55'i aşar). (2) Yatay: karakterin düz alt kesiği kapak alt kenarında (1080), mürekkep sağı 1798, ölçek 0,97 (sağ dirsek süre rozeti bölgesine girmesin); uçak 0,28, biletin üstünde. Dikey: kesik satır 1000 (saatli elin altı), ölçek 0,70; uçak sol üstte, biletin üstünde. (3) Kaynak saç ve uçak kenarında beyaz kırıntı (507 + 433 px) kenar gölgesini pürüzlü gösterdi → 02-04 yöntemi: kopyada alfa ≤ 64 + 3×3 açılış; çakışma denetimi de temiz alfayla; kaynak değişmedi. (4) `calistir.sh` kökteki eski kapağı Silinecekler'e taşır (02-04 emsali).

| Kapı (§5) | Sonuç |
|---|---|
| 1. 4 PNG, boyut | GEÇTİ — 1920×1080 ×2, 1080×1920 ×2 |
| 2. 168 px | GEÇTİ — `YARIN ama` / `WILL YOK` okunur, yüz ve bilet seçilir; küçük satır okunmaz (beklenen) |
| 3. Glif | GEÇTİ — ana yazıda İ/Ş/Ğ yok; her harf Fredoka/Lexend cmap `assert`'inden geçti; rozet İ Lexend latin-ext (yakın kesit) |
| 4. Çakışma, sağ alt %15×%8, dikey üst/alt %20 | GEÇTİ — alfa `assert` (pay 24 + kenar 10 px) + göz; zemin dışı piksel 0/24.768 ve 0/414.720 (iki tema) |
| 5. Emoji, beklenmeyen yazı, kesik kenar | GEÇTİ — görselde yazı yok; kırıntı 2. turda giderildi (3× yakın kesit) |

Turlar: 1 yerleşim turu (dirsek boş bölgede → karakter alt kenara), 1 kusur turu (kırıntı). 1. tur PNG'leri ve kesitler `~/Silinecekler/2026-11-15-kapak/`.
**Açık kalan.** (a) Ana yazı 170/184 px = kapağın %16–17'si (standart %18–24): "YARIN ama" uzun, bilet yazıya yakın; büyütme karakteri küçültür. (b) Dikey yazı y 480–899 (standart bant 600–1320 üst yarısı; temel emsali gibi). (c) Açık temada logo tek renk `#141414` (emsal kararı). (d) Commit yok; iki sahne ve `ortak/kapak` bağı izlenmeyen dosya.
