# Sahne 04 — Örnek 2 (düz canvas) — RAPOR

Tema: acik

04.11.2026 · 487 kare · t_bas 36,15 · cümle 4 · `calistir.sh` ile üretildi (yakala → olaylar.json → video.mp4 → kontrol.png → k/).

## Yapılan
- `ortak/kalem-canvas.js`: kalem darbesi (Paper.js'siz). `sahne-ortak.js`: Sahne sınıfı (zaman, olay, cümle belirmesi, öğeler). `sahne.js`: içerik.
- Zemin ve künye `zeminCiz` / `kunyeCiz` ile; künye `Example 2 / 3`, etkin 1; kare 0'dan sabit.
- İlk 12 kare boş (yalnız künye), son 12 kare durgun (nefes ve nota salınımı `icerik_kare`'de donar).

## Zamanlama (BRIEF satırı → gerçek kare)
| BRIEF | Beklenen kare | Gerçek kare |
|---|---|---|
| Daire içinde 2 | 0–32 | 12–28 daire, sayı pop 21–32 (ilk 12 kare boş kuralı) |
| Cümle sözcükleri | 38 (My) – 108 (semester.) | 39 – 108, sozcukler.json t0 ile birebir |
| Kız kardeş çizimi | 44–99 | 44–98 (1,8 sn, 22 darbe) |
| Piyano | 44–99 | 71–98 (0,9 sn, 5 darbe) |
| Notalar teker teker | 86–138 | 86 / 103 / 119 (+parıltı 99 / 116 / 132) |
| Türkçe çeviri | 142–159 | 142–159 (soldan maske 0,55 sn) |
| Takvim şeridi 5 kutu | 218–… | 218, 225, 231, 238, 244 |
| now noktası / not at this moment | 255 / 263 | 255 / 263 |
| this semester + köşeli ayraç | 281 | 281 / 282 |
| → these days | 300 | 296 ok, 300 yazı |
| is / taking daire | 344 / 353 | 344 / 353 |
| Formül kartı | 386–431 | 386 kutu+be, 397 is, 415 +, 422 V-ing, 430 tak-ing |

## Kontrol anları
Kontrol.png: 0, 97, 194, 292, 389, 474. Tam boy `k/`: 0101 (39,5 sn), 0281 (45,5 sn), 0439 (50,8 sn).

## Sayılar
- video.mp4: 487 kare, 1920×1080, yuv420p, 30 fps.
- Darbe: 78 (kız 22, piyano 5, nota 3×4, kutu 20, halka 2, kart 4, ok 3, ayraç 1, daire 1, alt çizgi 8). Olay: 34 (cizgi 24, tik 6, parilti 3, vurus 1); aynı karede en çok 2.
- Yakalama süresi ≈ 41 sn (yük düşükken).

## Görsel denetim bulguları ve düzeltmeler
1. Tur 1: Peeps yüz çizgileri eksikti (eşik %2 çok yüksek) → kız figürü için eşik %0,4 (22 darbe, yüz görünüyor).
2. Tur 1: sarı halkalar komşu harflere değiyordu → sözcük aralığı +10 px, halka payı 6 px, kalınlık 6.
3. Tur 1: formül kartında satırlar alt kenara yapışıktı → kart yüksekliği 156 px, satır aralığı artırıldı.
4. Son kontrol: çakışma yok (yazı × çizim × künye), güvenli alan içinde, künye tam; en uzun cümle satırı x ≈ 1117'de biter, nota alanı (y ≥ 395) ile çakışmaz.

## Açık sorular
- Kız figürünün piyanoya göre konumu: Peeps `sitting-2` piyanoya bakmıyor, yanında oturuyor gibi duruyor. Başka poz ya da yatay çevirme istenir mi?
- Dolgu yolları (Peeps) yalnız kontur olarak çiziliyor; saç ve ceket dolgusuz (kalem eskizi görünümü).
- `now` noktası dolu disk olarak çiziliyor (kalem darbesi değil); nabız halkası süs efekti.

## Çalışmayan / eksik
Eksik madde yok. Ses olayları kalem darbelerinin başında; ses tasarımı çıktısını bu sahne üretmez (olaylar.json yeterli).
