# S1 Shorts — "BU AKŞAM = I AM GOING" (present-continuous-s1)

Çıktı: `cikti.mp4` (1080×1920, 30 fps, 26,4 sn, anlatım 25,39 sn hazır) + `kapak.png` (t = 1,97 sn karesi) + `kontrol.png`.
Ana BRIEF biçimi dikeye uyarlandı; stil, kalem darbesi, olay sesi kuralları `../present-continuous/BRIEF.md` ile aynı.
Kaynaklar: ses `ortak/anlatim/` (cümle başları 1,00 · 8,21 · 18,52; toplam 25,39), kalıp `dikey-senaryo-kalibi.md` §4–5.

## Dikey yerleşim (px)
| Bant | y | İçerik |
|---|---|---|
| HUD | 0–288 | ders adı sol üst, rozetler `YDT · BASIC` + `GRAMMAR`, çip sağ üst |
| İçerik | 288–1344 | kapak / örnek / CTA |
| Altyazı | 1344–1536 | boş (bu sürümde altyazı bandı yok; cümleler ekranda yazılı) |
| Logo | 1440–1536 sol | y 1464, yükseklik 48 |
| Platform | 1536–1920 | BOŞ |

## Sahneler (zaman.json ile birebir)
| # | Klasör | Motor | Küresel sn | Kare |
|---|---|---|---|---|
| 01 | 01-hyperframes-kapak | HyperFrames | 0,00–3,00 (+12 geçiş) | 102 |
| 02 | 02-paperjs-ornek | Paper.js | 3,00–18,52 (+12) | 478 |
| 03 | 03-hyperframes-cta | HyperFrames | 18,52–25,39 (+1 sn kuyruk) | 236 |

Kapak: başlık 0,65–1,45; Türkçe cümle 1,00'dan sözcük zamanlı; uçuş 2,0–3,0 (başlık → çip, cümleler yukarı, eskiz solar).
Örnek: `going` altı çizgi, `şimdiki` / `gelecek` belirteç, figür + ev + hilal 8,3'ten, kart 8,0'dan, `go + -ing` 12,77–13,73, `am · is · are` 15,41 / 16,05 / 17,09.
CTA: `Tam ders:` 0,45 · `Present Continuous` bant 1,0 / 1,44 · saat + `@ydspublishing · 6 dk` (karar A 05.11) 2,4 / 3,51 · 1 sn durgun kuyruk.

## Çalıştırma
Her sahne `calistir.sh --tema acik`; sonra paket kökünden
`python3 birlestir.py projeler/present-continuous-s1 --tema acik --gecis BookFlip --efekt hisirti`.

## 05.11 düzeltme (telefon ölçeği; kural kaynağı `../present-continuous-dikey/BRIEF-DIKEY.md` §0, §2, §3)
Nadir şef kare incelemesi (360×640): logo 48 px yüzüyor, ders adı/rozet/çip 9-13 CSS px, Caveat 56-64 gri, içerik üst %55, altyazı bandı boş.
Yukarıdaki "Dikey yerleşim" tablosu bu bölümle DEĞİŞTİ (eski satırlar tarih için kalır).
| Bant | y | İçerik |
|---|---|---|
| HUD | 0-320 | logo sol üst (48,48) 387×96 · ders adı Fredoka 56 taban y212 · rozetler `YDT · BASIC` + `GRAMMAR` Lexend 36, hap y236 h72 · çip sağ üst y48 h80 Lexend 40 (çip metni logo ile çakışmasın diye iç boşluk 48) |
| İçerik | 352-1392 | DOLU; yazı ≥ 64 px; figür ≥ 420 px |
| Altyazı | 1400-1536 | Lexend 500 44, ≤ 2 satır, ortalı (`ortak/anlatim/altyazi.json`, 8 parça; `altyazi_uret.py`) |
| Platform | 1536-1920 | BOŞ |
Sahne 01: `BU AKŞAM` 180 / `= I AM GOING` 160 (190 px'te 1136 px, 984'e sığmaz) ortalı, Caveat 80 TR (y765) + EN (y855), eskiz figür 480 + ev + zemin y 900-1384; uçuşta eskiz solmaz; çip uçuş bitene kadar gizli; kapak = kare 59 (t 1,97, açık tema).
Sahne 02: kare 0 = sahne 01 son hali (cümleler y440/530); not Caveat 64 2 satır; 8,0'da cümle 1 + not solar; kart y372-704 Fredoka 72; `go + -ing` Fredoka 110 y735-885; 14,45'te eskiz solar; `am · is · are` Fredoka 96 kutuları y1110-1310.
Sahne 03: `Tam ders:` Caveat 72 y460, bant y510-1070 Fredoka 150, saat + `@ydspublishing · 6 dk` (karar A 05.11) Lexend 64 y1240.
Çıktı: `cikti.mp4` + `cikti-koyu.mp4` (792 kare, 26,4 sn), `kapak.png`, `kontrol.png`, `kontrol-koyu.png`; telefon kontak `k/telefon-*.png`.
Çalıştırma: her sahne `calistir.sh --tema acik` sonra `--tema koyu`; `birlestir.py ... --tema acik|koyu --gecis BookFlip --efekt hisirti`.
> TEK KAYNAK (05.11 karar 6b): öteki 9 paketin kopyası buraya işaret eder;
> kuralı yalnız burada değiştir.

## El yazısı (K26, 05.11)

Caveat yazılar kalemle yazılır (`02-paperjs-ornek`: `S.elYazisi(str, {x, y (taban), boyut, renk, bas | sozcukler,
sure})`; veri kök `ortak/tegaki/caveat-tr/`). Kural kaynağı `../present-continuous-dikey/BRIEF-DIKEY.md` §6: hız
kuralı, nib noktaları, glif kapsam kapısı, sağ uç ≤ 1032 px, boyut ≥ 56, 3 kare kanıt. HyperFrames (01 kapak,
03 CTA) ayrı karar.
