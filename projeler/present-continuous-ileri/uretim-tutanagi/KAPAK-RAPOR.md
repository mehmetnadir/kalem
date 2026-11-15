# KAPAK-RAPOR — present-continuous-ileri ana ders kapakları · 15.11.2026 (istem KAPAK-0201I)
| Dosya (`file`) | Boyut | Tema |
|---|---|---|
| `present-continuous-ileri/kapak.png` · `kapak-koyu.png` | 1920 × 1080 | açık · koyu |
| `present-continuous-ileri-dikey/kapak.png` · `kapak-koyu.png` | 1080 × 1920 | açık · koyu |
| `present-continuous-ileri/uretim-tutanagi/kapak-168.png` | 168 × 94 | açık |

Yöntem: simple-present-temel `90-hyperframes-kapak` kopyası (`uret.py`, `yardim.py`, `calistir.sh`; dikey `calistir.sh` `SAHNE=` ile ana betiği çağırır, görseller `-dikey/ortak/kapak` göreli bağından). `zaman.json`, `surumler.json`, sahne kodu değişmedi. Emsalden farklar: (1) metin `KNOWING?` · kutu `OLMAZ!` · `know · believe · own` (ok yok) · `YDT · İLERİ`; (2) `KNOWING?` uzun → satır 1 boyu 180, vurgu 200 (yatay; dikey 180/190), 02-04 gibi vurgu büyük; (3) karakter yatay 0,93, dikey 0,66 (avuç sola uzanır, gövde sağ alt boş bölgeye yaklaşır); tabela yatayda avucun solunda altta, dikeyde başın solunda; (4) yeni kural: alt kesik kapak dışında kalır; (5) kopyada 02-04 kırıntı temizliği (alfa ≤ 64 + 3×3 açılış; 432 + 192 adacık → 0); (6) eski kök PNG Silinecekler'e taşınır.

| Kapı (§5) | Sonuç | Bakılan |
|---|---|---|
| Boyut | 4/4 §1 ile aynı | `file` |
| 168 px | `KNOWING?` / `OLMAZ!` okunur, yüz seçilir; küçük satır okunmaz (beklenen) | `kapak-168.png` (Read) |
| Glif | ana yazıda İ/Ş/Ğ yok; her harf Fredoka cmap `assert`; rozet `İ` Lexend latin-ext (emsal rozet yazı tipi) | 4 PNG |
| Çakışma | yazı ↔ görsel ≥ 34 px, daire ↔ yazı ≥ 24 px (`assert`) + göz | 4 PNG (Read) |
| Sağ alt %15×%8 | zemin dışı piksel 0 / 25.056 (açık, koyu) | numpy |
| Dikey üst/alt %20 | 0 / 414.720 her bölge, iki tema | numpy |
| Turlar | 1. çekim: avuç/tabela kenarında kırıntı pürüzü, dikeyde tabela daireye değiyor → 2. çekimde giderildi | yakın kesit (Read) |

**Açık kalan:** (a) KAYNAK GÖRSEL KUSURU: `karakter.png` kol ile gövde arasında opak beyaz üçgen (x 601–714, y 862–1093; arka plan temizleyici kapalı bölgeyi bırakmış); 4 kapakta görünür, görsel yeniden temizlenmeli (düzeltmedim). (b) Satır 1 yatayda %16,7 (sol %55 sınırı), standart %18–24. (c) Dikey yazı y 492–904 (emsal gibi bandın üstünde); baş ortadan 191 px sağda. Commit yok.
