# Sahne 05 DİKEY — Örnek 3 (düz canvas) — RAPOR

Tema: koyu

05.11.2026 · 517 kare · t_bas 45,98 · cümle 5 · 1080×1920 yuv420p 30 fps (ffprobe: 517/517 her iki tema).

## Yapılan
- `sahne.js`, `sahne-ortak.js` (D1 iskeleti + dikey kunye.js + altyazı + halka ölçeği), `sayfa.html`, `calistir.sh`.
- Yerleşim: çip `Example 3 / 3`; kart 48,372 984×316 (`Look!` kırmızı Fredoka 110 + cümle Fredoka 72, sözcük zamanlı);
  TR Caveat 64 (y 756); sol ağaç 460 px + kedi 150 px (tırmanış), sağ sütun etiket kutuları Caveat 64
  (`Look!` `Listen!` `Watch out!`) + `= şimdi` Caveat 84 sarı; alt `is + climb-ing` Fredoka 110 (taban 1364);
  `be + V-ing` Caveat 72. Altyazı 1400–1536. Platform bandı boş.
- Altyazı: uzun parça (cümle 5 TR, 99 karakter) `kunye.js altyaziCiz` ile 3 satıra taşıp 2 satıra yapışıyordu;
  `sahne-ortak.js` parçayı sözcük zamanıyla ≤ 2 satırlık dilimlere böler (ortak/ dosyasına dokunulmadı).
- Daire içinde `3` sayısı yok (BRIEF-DIKEY §4 çip ile verir). Sarı ok → NOW noktası yerine `= şimdi` + alt çizgi.

## Zamanlama (yerel kare)
| Olay | Kare |
|---|---|
| kart kutusu | 16 |
| Look! pop + vurus | 39; ünlem 46, 54 |
| cümle sözcükleri | 60 – 108 |
| ağaç | 40–79; parıltı 80 |
| kedi çizimi / tırmanış | 73 / 96–136 |
| TR çeviri | 130 |
| etiketler Look! / Listen! / Watch out! | 207 / 229 / 256 (yazı +7) |
| `= şimdi` | 334 |
| halka is / climbing | 402 / 411 |
| formül `is + climb-ing` | 421 |
| `be + V-ing` | 455 |

## Kapılar
- olaylar.json: 27 olay, en büyük kare 455 (< 517); ilk görünen kare 16 (ilk 12 kare boş), son 12 kare durgun.
- Editör: `?surum=dikey-tam&tema=acik&t=64` -> `{"no":5,"hazir":true,"goster":true,"op":1}` (slot no 0 tabanlı: 5 = sahne 06; sahne 05 t=50 için `{"no":4,"hazir":true,"goster":true,"op":1}`).
- Kare: `k/0151.png` `k/0271.png` `k/0466.png` (2 tema, son koşu koyu), `kontrol.png`, `k/telefon-01..03.png` Read ile açıldı:
  HUD okunuyor, kart + sol/sağ çizim + formül bandı 372–1392 dolu, yazı ≥ 64 px, ağaç 460 px, altyazı var, platform boş, çakışma yok.

## Neden yeniden
1. Tur 1: `be + V-ing` `= şimdi` alt çizgisiyle çakıştı (V-i kesik); cümle `…the / tree.` yetim satırdı. Etiket sütunu 95 px aralığa sıkıldı, `= şimdi` 1170'e, `be + V-ing` 1255'e alındı, cümle maxGen 740 (`The cat is climbing / the tree.`).
2. 2. koşu yük 393 yüzünden `ZAMAN AŞIMI` verdi (kod hatası değil); yük düşünce aynı kodla yeniden koşuldu.

## Açık sorular
- `ortak/kunye.js altyaziCiz` 2 satırdan uzun parçada üçüncü satırı ikinciye ekleyip taşırıyor (genişlik 984 aşılır); ortak dosya, ben dilimleme ile aştım. Diğer dikey sahneler aynı hataya düşebilir.
- Etiket sütununun sağında 915–1032 px boş (≈ %11 genişlik).
- Editör konsolunda 404 satırları var: kaynak başka sahneler (`01-hyperframes-giris/sayfa.html` 404 — HF sahnesi `proje/index.html` kullanıyor; bu iki sahnenin tüm istekleri 200).
