# KAPAK-RAPOR — simple-past-ileri ana ders kapakları · 15.11.2026 (istem KAPAK-0210I)
| Dosya (`file`) | Boyut | Tema |
|---|---|---|
| `simple-past-ileri/kapak.png` · `kapak-koyu.png` | 1920 × 1080 | açık · koyu |
| `simple-past-ileri-dikey/kapak.png` · `kapak-koyu.png` | 1080 × 1920 | açık · koyu |
| `simple-past-ileri/uretim-tutanagi/kapak-168.png` | 168 × 94 | açık (PIL LANCZOS) |
Yöntem: emsal `simple-present-temel/sahneler/90-hyperframes-kapak/` kopyası (`uret.py --duzen yatay|dikey`, `yardim.py`, `calistir.sh`); dikey `calistir.sh` ana üreticiyi çağırır, görsel `simple-past-ileri-dikey/ortak/kapak` göreli bağından. Kare `hyperframes snapshot --at 0.5`.
Emsalden farklar: (1) metin `USED TO mu` / `WOULD mu?` / `durum: yalnız used to` / `YDT · İLERİ`; küçük satır düz yazı (ok yok). (2) S 240 → 155 (yatay ve dikey): iki satır 10 ve 9 harf, sol %55'e sığar. (3) satır 1 ile vurgu kutusu arası en az 0,02·S + 26 px (S < 185'te emsal oranı denetim payının altına iner). (4) Karakter düşünce balonuyla geniş: yatay ölçek 1,05 → 1,0, sol 940; daire r 390 → 350 (yatay), 295 → 280 (dikey). (5) Görsel kopyasında alfa ≤ 64 ve 3×3 açılış (02-04 emsal yöntemi): karakterde 410, nesnede 253 kırıntı (≤ 3 px) silindi; kaynak PNG değişmedi.

| Kapı (§5) | Sonuç | Bakılan |
|---|---|---|
| Boyut | 4/4 standart §1 ile aynı | `file` |
| 168 px'te ana yazı | okunur: `USED TO mu` / `WOULD mu?`, yüz seçilir; küçük satır okunmaz (beklenen) | `kapak-168.png` + koyu kopya (Read) |
| Glif | ana yazıda İ/Ş/Ğ yok, 11 harf Fredoka latin; rozet `İ` Lexend latin-ext, Lexend biçiminde | cmap + rozet yakın kesit (Read) |
| Yazı–karakter üst üste | binmiyor: alfa denetimi (kenar 10 + pay 24 px, `assert`) + göz | 4 PNG (Read) |
| Sağ alt %15×%8 | boş: zemin dışı piksel 0/25.056 (açık, koyu) | numpy |
| Dikey üst ve alt %20 | yalnız zemin: 0/414.720 her bölge (açık, koyu) | numpy |
| Emoji, beklenmeyen öğe | yok; balon boş, saat kadranında rakam yok; kenar 3 geçiş, basamak görülmedi | balon/saat/saç yakın kesit (Read) |

Açık kalan: yatay yazı boyu 155 (kapağın %14'ü; standart %18–24, 02-04 emsalinde de altında) · dikeyde karakter gövdesi ortadan ~210 px sağda (balon sağ kenara yaslı; 02-04'te de açık madde) · açık temada logo tek renk `#141414` (emsal kararı). Kökte eski kapak yoktu, Silinecekler'e taşınan dosya yok; commit yok.
