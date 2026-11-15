# RAPOR — sahne 08 Kaydet (02-04-ydt-temel-s1, huni v2, HyperFrames DİKEY) · 15.11.2026

| Ölçüm | Değer |
|---|---|
| Sahne | 19,99–25,49 (içerik 165 + geçiş 12 = 177 kare, 5,9 sn); cümle 3, öğretmen |
| Kod yolu | şef `SPEC.md` → `agy-filo tek --rol kod` → `uret.py` (340 satır, 1 tur, düzeltme yok) |
| Kopya | `calistir.sh`, `olay.py`, `yardim.py` ← `03-hyperframes-cta` (v2); Edit: başlık, `KARE=177`, ana kapak kopyası çıktı, denetim kare saniyeleri |
| QA (`qa-yerel.sh … --hazirla`) | çıkış 0 · `çakışma yok (23 örnek, 2780 kutu)` · `kapı çıkış kodu: 0` |
| Çakışma kapısı (ayrı koşu, 41333/41022) | çıkış 0 · `08-hyperframes-kaydet | çakışma yok (23 örnek, 2780 kutu)` · 0 uyarı |
| Metin taraması (`tam ders|dakika`, html/js/py) | boş (grep rc 1) |
| Kanal katmanı (4 karede piksel) | logo görünür kutu x 60–239, y 298–330 · `@ydspublishing` x 265–595, y 296–339; 4 karede aynı; 03 sahnesiyle kıyas: koyu fark 0, açık en çok 1 (gren) |
| Boş bantlar | 0–280, 1570–1920, sağ 962–1080 (y 440–1570): 4 karede mürekkep pikseli yok |
| agy koşusu | `/home/sef/.claude/canavar/agy-filo/20261115-191649` (gemini-3.8-flash-high, 270 sn, başarılı) |

## Olay listesi
| olay | kare | yerel sn | küresel sn | sözcük | hareket |
|---|---|---|---|---|---|
| `kart_giris` | 16 | 0,55 | 20,54 | `Bu,` | kart ölçek 0,96 → 1 + opaklık, 0,45 sn `power3.out`; 21,00'den sabit (4,49 sn) |
| `uc_giris` | 31 | 1,03 | 21,02 | `üç` | `üç farktan biri` (Lexend 700 48, mürekkep %70) opaklık + y 16 → 0, 0,30 sn |
| `imi_ciz` | 147 | 4,90 | 24,89 | `Kaydet.` | yer imi (Tabler `bookmark` yolu, sahne içinde) kalem darbesi 0,30 sn `sine.inOut` |
| `hap_giris` | 150 | 5,00 | 24,99 | `Kaydet.` | `Kaydet` sarı hap (Fredoka 700 64) ölçek 0,9 → 1 + opaklık, 0,30 sn `back.out(1.6)` |
| `kuyruk_durgun` | 165 | 5,50 | 25,49 | sahne sonu | hareket yok (son 12 kare) |

Ses olayları (`olaylar.json`): kare 16 `vurus` 0,5 · 147 `cizgi` 0,6 · 150 `tik` 0,5.
Yerleşim: `üç farktan biri` taban 528 (y ≈ 492–538) · kâğıt kart x 60–960, y 600–980 (kalem kenarı x 74–946, y 614–966) ·
kural satırları Fredoka 700 73, x 110, taban 765 / 861 · yer imi + hap y 1031–1129, yatay orta 510 · altyazı 1400–1550.

## Bakılan kareler
| Kare | Yol | Bulgu |
|---|---|---|
| 20,05 açık | `k/08-hyperframes-kaydet-20.05.png` | yalnız kanal + künye; içerik bandı boş (kart 20,54'te girer; ilk 12 kare geçiş payı) |
| 22,75 açık | `k/08-hyperframes-kaydet-22.75.png` | `üç farktan biri` + kart + altyazı `Sınavdan önce lazım olacak.`; taşma, kesik, bindirme yok |
| 25,40 açık | `k/08-hyperframes-kaydet-25.4.png` | + yer imi + `Kaydet` hapı (dolgu `#ffe066`, yazı `#1b2440`), altyazı `Kaydet.` karaoke çizgili |
| 25,40 koyu | `k/koyu/08-hyperframes-kaydet-25.4.png` | kâğıt kart koyu zeminde okunur; hap `#f2a93b` + koyu yazı; yer imi krem |
| 20,75 / 25,05 açık (ara) | `/tmp/qa08-ara/` (geçici) | kart girişte küçük + saydam; yer imi yarı çizili, hap belirmekte |

## Açık noktalar
1. `üç farktan biri` 48 px: genel taban 64'ün altında; istem "Bu sahneye özel" maddesi 48'i açıkça istiyor. Karar şefte.
2. 20,05 karesinde içerik bandı boş (0,55 sn; 0,40 sn geçiş payı + 0,15 sn). Kart `Bu,` çapasına bağlı; öne alınırsa söz öncesi hareket olur.
3. `üç farktan biri` sahne sonuna kadar kalır (BRIEF satırı 20,54–22,62 aralığını yazar; çıkış hareketi eklenmedi, kart sabitliği bozulmasın diye).
4. Kâğıt rengi tema paletinde yok: koyu `#fff9e6` (stil anayasası kart rengi), açık `#fffdf8` (`.tema-acik #kagit`). Ortak bir `kagit` değeri yok.
5. Kalem kenarı düz parçalı (L) çizgi, ±2,2 px sabit kaydırma; eğri (Q) değil. Gözle el çizimi okunuyor.
6. agy SPEC'teki "test yok" sözüne karşın `uret.py` + `olay.py` koştu (zararsız: `calistir.sh` dosyayı temayla yeniden üretti).
7. Altyazı `Kaydet.` ile hap `Kaydet` aynı anda ekranda (altyazı zorunlu; çift metin bilinçli).
