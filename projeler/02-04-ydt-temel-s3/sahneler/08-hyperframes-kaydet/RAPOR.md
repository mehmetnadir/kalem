# RAPOR — 02-04-ydt-temel-s3 sahne 08 Kaydet (HyperFrames, huni v2) · 15.11.2026

| Kapı | Sonuç |
|---|---|
| qa-yerel (`15.99,18.66,21.3` açık, `19.6` koyu, `--hazirla`) | çıkış 0 (2. tur) |
| Çakışma kapısı (`--port 41333 --sunucu 41022`) | `çakışma yok (23 örnek, 4936 kutu)`, RC 0 |
| Kanal katmanı (4 kare) | aynı konum, opaklık 1 |
| Metin taraması (`tam ders`, `dakika`) | sonuç yok (grep rc 1) |
| mp4 render | YOK (`ONIZLE_YALNIZ=1`) |

## Dosyalar
- `uret.py`: agy-filo (`kod`, gemini-3.8-flash-high, 308 sn) SPEC'ten yazdı; şef 3 küçük Edit yaptı (aşağıda).
- `yardim.py`, `olay.py`: S1 sahne 08 kopyası (v2 kanal katmanı `Y.kunye_svg()`); `calistir.sh`: kopya, `KARE=172`, denetim kareleri.
- `SPEC.md`: şef. agy koşu özeti: `/home/sef/.claude/canavar/agy-filo/20261115-192822`.

## Olay listesi (cümle 4, öğretmen; yerel = küresel − 15,99)
| olay | küresel sn | kare | sözcük | hareket |
|---|---|---|---|---|
| kart_ciz | 16,54 | 16 | `Bu,` | çerçeve kalemle 0,40 sn |
| satir1 | 16,60 | 18 | `Bu,` | tren darbesi + `Tarife → leaves,` (`leaves` sarı hap) |
| satir2 | 16,70 | 21 | `Bu,` | bilet darbesi + `plan → am going.` |
| gonder_ciz | 18,77 | 83 | `Bir` | gönder simgesi (SVG) kalemle 0,40 sn |
| imi_ciz | 18,87 | 86 | `Bir` | yer imi (SVG) kalemle 0,40 sn + `Kaydet` |
| arkadasina | 19,01 | 91 | `arkadaşına` | `Arkadaşına` gelir |
| gonder_yaz | 19,53 | 106 | `gönder;` | `gönder` gelir |
| sari_gecis | 19,53 | 106 | `gönder;` | gönder simgesi sarı dolar; `leaves` hapı söner, mürekkep altçizgi çizilir |
| kuyruk_durgun | 21,32 | 160 | sahne sonu | hareket yok (son 12 kare geçiş) |

Ses olayları: 0,55 `cizgi` · 2,78 `cizgi` · 3,54 `tik` (`olaylar.json` 3 satır).
Kart 17,00'de (yerel 1,01) tamamlanır; 17,00–21,33 arası (≈ 4,3 sn) konumu ve boyu değişmez.
Altyazı: `altyazi.json` cümle 4, iki parça; ikinci parça 21,33'te kapanır (`Y.altyazi_svg(T_BAS, 5.34, ALT)`).

## Kanal katmanı ölçümü (PNG, zeminden ayrışan piksel)
| Kare | x | y |
|---|---|---|
| 15,99 açık | 60–596 | 296–339 |
| 18,66 açık | 60–596 | 296–339 |
| 21,30 açık | 60–596 | 296–339 |
| 19,60 koyu | 60–596 | 296–339 |

Görünür sol kenar x 60; resim kutusu y 291–339 (logonun üst iç boşluğu 5 px). Boş bantlar dört karede de boş:
0–280 → 0 piksel, 1570–1920 → 0, sağ şerit x 964–1080 (y 460–1560) → 0.

## Bakılan kareler ve bulgu
| Kare | Bulgu |
|---|---|
| 15,99 | yalnız kanal + künye; içerik bandı boş zemin ✓ |
| 18,66 | kart tam (tren, bilet, iki satır, oklar), `leaves` sarı hapta; altyazı `Bu, üç farktan yalnız biri.` ✓ |
| 21,30 | kart (`leaves,` mürekkep altçizgili) + sarı gönder simgesi + `Arkadaşına gönder` + yer imi + `Kaydet`; altyazı ikinci parça ✓ |
| 19,60 koyu | `sari_gecis` ortası (hap sönüyor, `gönder` geliyor); renkler koyu temada doğru, kontrast yeterli ✓ |

Taşma, kesik yazı, üst üste binme yok. İçerik x 60–960 içinde. Altyazı satırı x 77–943, taban ≈ 1484 (1400–1550 içinde).
Simgeler SVG yolu (Tabler `send`, `bookmark`; MIT), emoji değil.

## Düzeltme turları
1. Tur 1: kapı 1 uyarı (`leaves-hap:text0 × s1:text1`, 16,74–19,49): hap yazısı alttaki mürekkep kopyayla üst üste.
   Son karede virgül kopuk (`leaves ,`); çerçevenin sol üst bindirme izi kusur gibi görünüyordu.
   Düzeltme (şef, Edit): mürekkep yazı `leaves,` (virgül bitişik), opaklık 0 ile başlar, hap söndükten 0,10 sn sonra gelir;
   hap dönemi virgülü hapla birlikte söner; çerçeve yolu sonu `L114 562`.
2. Tur 2: kapı 0, qa 0.

## Açık noktalar
- Şef notu (19:00) istemdeki "ekranda yalnız `Kaydet`; paylaş simgesi yok" maddesinin yerine uygulandı: büyük `Arkadaşına gönder`
  (Fredoka 80, gönder simgesi) + küçük `Kaydet` (Fredoka 64, yer imi). `Kaydet`'in "yanında" durması 900 px'e sığmaz
  (685 + 208 + simgeler); iki satır alt alta.
- Sarı dolgu `gönder;` çapasında yer imine değil gönder simgesine gider: söylenen eylem gönderdir, ekran sesle çelişmesin.
  İstemin eski maddesi (yer imi sarıyla dolar) şef notuyla çelişiyordu; yer imi mürekkep çizgide kalır. Nadir isterse tek satırlık değişiklik.
- İkon yerleşimi istemdeki gibi iki ikon da satır başında (BRIEF "sağda bilet" diyor; hikâye A'da bilet sağda).
- Standart §3 kaydet sahnesi tanımı ("yer imi + Kaydet") bu kısada gönder satırı ile genişledi; standart belgesine dokunulmadı.
