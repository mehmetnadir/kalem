# KAPAK-RAPOR — present-perfect-temel ana ders kapakları · 15.11.2026 (istem KAPAK-0206T)
| Dosya (`file`) | Boyut | Tema |
|---|---|---|
| `present-perfect-temel/kapak.png` · `kapak-koyu.png` | 1920 × 1080 | açık · koyu |
| `present-perfect-temel-dikey/kapak.png` · `kapak-koyu.png` · `uretim-tutanagi/kapak-168.png` (ana paket) | 1080 × 1920 · 168 × 94 | açık · koyu · açık |

Yöntem: KAPAK-0202 üreticisinin kopyası (`sahneler/90-hyperframes-kapak/uret.py --tema --duzen`, `calistir.sh`). Dikey `calistir.sh` ana üreticiyi `--duzen dikey` ile çağırır; görseller `present-perfect-temel-dikey/ortak/kapak` göreli bağından gelir. `zaman.json`, `surumler.json` ve sahne kodu değişmedi. Emsalden farklar: (1) metin `KAYBETTİM` · `= HAVE LOST` · `have / has + V3` (tek Lexend satırı, ok yok); (2) yazı boyu 240 → 160 yatay, 190 → 144 dikey (uzun vurgu satırı); satır 1 ile kutu arası en az 24 px (`max(0,15·S; 0,02·S + 26)`); (3) karakter tam boy, etek çizgisine kadar çıkartma; alttan taşmaz. Eller etek hizasında yana açık; taşırınca sağ el süre rozeti bölgesine giriyor (aramada 0 geçerli düzen). Dikeyde göğüs altı kesim yok, boş cepler görünür; (4) 02-04 emsalinin kopya temizliği (alfa ≤ 64 + 3×3 açılış): 1. turda koyu temada kenar noktalı saçaklıydı; (5) `calistir.sh` eski kök PNG'yi Silinecekler'e taşır (02-04 emsali).

| Kapı (§5) | Sonuç | Bakılan |
|---|---|---|
| 4 PNG, boyut | GEÇTİ: 1920×1080 ×2, 1080×1920 ×2 | `file` |
| 168 px | GEÇTİ: "KAYBETTİM = HAVE LOST" okunur, yüz seçilir; küçük satır okunmaz (beklenen) | `kapak-168.png` + koyu kopya (Read) |
| Glif İ (Ş, Ğ metinde yok) | GEÇTİ: `uret.py` cmap assert; İ noktası Fredoka biçiminde | yakın kesit (Read) |
| Yazı ↔ görsel çakışma | GEÇTİ: alfa assert (pay 24 px + kenar 10 px) + göz | 4 PNG (Read) |
| Sağ alt %15×%8 · dikey üst/alt %20 | GEÇTİ: zemin dışı piksel 0/25.056 · 0/414.720 (her bölge, iki tema) | numpy |
| Emoji, öğe | GEÇTİ: yazı, karakter, anahtar, logo, rozet (+ açık temada krem daire) | 4 PNG |

- **Açık kalan — görsel kusuru, düzeltilmedi:** `karakter.png` içinde kol ile gövde arasında arka plan temizleyicinin silmediği 2 kapalı beyaz bölge var (her biri ~7.000 px; kaynak x 189–285 ve 633–725, y 834–989). Kapakta kolun içinde beyaz şerit görünür, koyu temada belirgindir. Görsel yeniden temizlenince `calistir.sh` yeniden koşar.
- Şef/Nadir onayı: yatayda karakter alttan taşmıyor; dikeyde karakter ortadan 192 px sağda, yazı y 492'den başlıyor (iki emsalle aynı).
- Tur: 2 (1. tur kenar saçağı). Ara 4 PNG `~/Silinecekler/2026-11-15-kapak/present-perfect-temel-*`. Commit yok.
