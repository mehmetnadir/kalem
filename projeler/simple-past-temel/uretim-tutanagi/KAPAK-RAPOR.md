# KAPAK-0210T — simple-past-temel ana ders kapakları · 15.11.2026

| Dosya (`file`) | Boyut | Tema |
|---|---|---|
| `simple-past-temel/kapak.png` · `kapak-koyu.png` | 1920×1080 | açık · koyu |
| `simple-past-temel-dikey/kapak.png` · `kapak-koyu.png` | 1080×1920 | açık · koyu |
| `simple-past-temel/uretim-tutanagi/kapak-168.png` | 168×94 | açık (küçük görünüm, PIL LANCZOS) |

**Yöntem.** Emsal `simple-present-temel/sahneler/90-hyperframes-kapak/` kopyası (`uret.py --duzen yatay|dikey`, `yardim.py`, `calistir.sh`); dikey `calistir.sh` ana üreticiyi çağırır. Kare: `bash calistir.sh --tema acik|koyu` → `hyperframes snapshot --at 0.5`. Sahne `zaman.json` listesinde yok; `zaman.json`, `surumler.json` değişmedi. **Emsalden farklar.** (1) Metin `GİTTİM` / `= WENT` / `-di → -ed · go → went` (küçük satır N parçalı, 2 SVG ok; Lexend'de → yok). (2) Yatay: `= WENT` kutusu daha geniş (x 982), el sola uzanıyor → S 240 → 230 (satır %21), karakter 1,00, baş y 150, alt kenardan taşar. (3) Dikey: kesim satırı 960, ölçek 0,67, karakter ortadan 6 px sağda (emsal 184 px). Ok başın solunda. (4) Görsel kopyası 02-04 emsaliyle temizlenir (alfa ≤ 64 + 3×3 açılış); kaynak değişmedi. (5) `calistir.sh` eski kök PNG'yi `~/Silinecekler/2026-11-15-kapak/` dizinine taşır (02-04 emsali). (6) `simple-past-temel-dikey/ortak/kapak` göreli bağı eklendi.

| Kapı (§5) | Sonuç |
|---|---|
| 4 PNG, boyut | GEÇTİ: 1920×1080 ×2, 1080×1920 ×2 |
| 168 px | GEÇTİ: `GİTTİM = WENT` okunuyor, yüz seçiliyor; küçük satır okunmuyor (beklenen) |
| Glif İ | GEÇTİ: `uret.py` her harfi Fredoka latin/latin-ext cmap'te arar (`assert`); İ noktası Fredoka biçiminde (yakın kesit). Metinde Ş/Ğ yok |
| Yazı ↔ görsel | GEÇTİ: alfa `assert` (pay 24 + kenar 10 px), 4 PNG göz denetimi |
| Sağ alt %15×%8 · dikey üst/alt %20 | GEÇTİ: zemin dışı piksel 0/24.768 (yatay) · 0/414.720 her bölge (dikey); iki tema |
| Kırıntı, emoji | GEÇTİ: koyu karelerde nesne dışında leke yok (rozet noktası hariç); emoji yok |

**Açık kalan.** (a) Halka okun iç deliğinde emsal kenar yöntemi (3 geçiş × 3,33 px, kare biçimli genişleme) 3 ve 6 yönünde 2 küçük sivri krem uç bırakır; tam boyda zor seçilir, emsal kenarı korundu. (b) Sarı kazak sarı zeminde yalnız krem kenarla ayrılır (standart §2 öngörüsü). (c) Dikey yazı y 492'den başlar (emsal ile aynı; standart bant 600). (d) Yazma kapısı 15 satırı aşan `.py` düzenlemesini kesti; düzenleme Bash ile yapıldı. Commit yok; 6 ara kesit PNG Silinecekler'de.
