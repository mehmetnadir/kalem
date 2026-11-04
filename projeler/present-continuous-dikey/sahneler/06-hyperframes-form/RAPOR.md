# Sahne 06 DİKEY — Soru + Form (HyperFrames 1080×1920) — RAPOR

Tema: acik + koyu (ikisi de koştu; video-acik.mp4, video-koyu.mp4, video.mp4 = son koşu)

05.11.2026 · 766 kare (ffprobe h264 1080×1920 yuv420p 30/1, nb_read_frames 766, iki tema) · t_bas 62,81 · cümle 6 (öğrenci) + 7.

## Yapılan
- `uret.py`, `olay.py`, `yardim.py` (D1 kopyası + dikey v2 künye: logo 387×96, ders 56, rozet 72, çip 80), `zamanlar.json`, `calistir.sh`.
- Üst: öğrenci başı 160 px (peeps-kit `ogrenci-bas.svg`, `#bas`, 3 yol) + balon + Caveat 72 metin (`-ing` sarı + belirteç).
  Balon 66,72'den sonra alfa 0,55.
- Orta (62,81–66,72): `sitt-ing / tak-ing / climb-ing` Fredoka 112; 66,72 çip `Question` → `Form`, -ing parçaları oklarla büyük `-ing`'e (190 px) + `in progress →`.
- 71,43: sütun solar, `be` başlığı; büyük `-ing` `V-ing` yuvasına küçülür; `I am / He is / We are` Fredoka 96 (zamanlı),
  `now` ayracı (kıvrık ayraç + Caveat 80 sarı); `was · were` + `past` + kırmızı çizgi (80,18).
- Alt: `-ing = -yor` Fredoka 130 (81,25, `V-ing` halkalı) + `koşu-yor = runn-ing` Caveat 72 (82,93 / 84,21 / 85,09). Son 1 sn durgun.
- Altyazı `div` 1400–1536 (5 dilim, opaklık `tl.set`); sözcükler `white-space:nowrap` (tire kırılması düzeltildi).
- Seçiciler `#id` önekli; balon başı görünür (k/75.png, k/110.png).

## Zamanlama
Kaynak zamanlar.json (yerel sn = t − 62,81): balon sözcükleri 0–2,8 sn; satırlar 0,69/1,39/2,09; form 3,91; be 8,62;
am/is/are 11,02/11,74/12,38; now 12,94; past 14,53; was/were 15,81/16,69; kırmızı çizgi 17,37; halka 18,44; yor 20,12; eşit 21,40; runn 22,28.
Olay: 39 (cizgi 19), en büyük kare 668 (< 766).

## Kapılar
- Editör: `t=82` -> `{"no":5,"hazir":true,"goster":true,"op":1}`; `t=64` aynı; sayfa 200. Ekran: `k/editor-t82.png` (altyazı, kare 576/766 doğru).
- Kare: `k/51.png` (64,5 sn) `k/216.png` (70,0) `k/696.png` (86,0) `k/30.png` `k/75.png` `k/110.png`, `kontrol.png`, `k/telefon-01..04.png` Read ile açıldı:
  HUD okunuyor, yazı ≥ 64 px (en küçük Caveat 72 / Lexend 44 altyazı), altyazı var, platform boş, çakışma yok, balon başı görünür.

## Neden yeniden
1. Tur 1: altyazı dilimi tire noktasında kırıldı (`koşu-/yor`); yatay taştı (flex içinde boşluk kayboldu); alt %30 boş kalıyordu.
   Satır/tablo aralıkları büyütüldü (satırlar 950/1080/1210, tablo 830/960/1090, `-ing` 190), altyazı iç `span` + `nowrap`.
2. `V-ing` halkası V harfine değiyordu → rx 16 pay.

## Açık sorular
- 71,43–73,83 arasında tablo yalnız `be` + `V-ing` (≈ 2,4 sn durgun); sözcük zamanları sabit.
- Sahne 06'da ana sürümdeki "Next lesson →" ve `am / is / are + V-ing` formül kartı yok (BRIEF-DIKEY §4 listelemiyor); tablo formülü taşıyor.
- Aşama 66,72'de büyük sol sütun (sitt/tak/climb) solarak yer açar: "hiçbir öğe kaybolmaz" kuralından bilinçli sapma (yer açma, kök `V` olarak tabloda kalır).
