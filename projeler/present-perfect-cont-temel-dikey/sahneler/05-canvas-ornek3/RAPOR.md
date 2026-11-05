# Sahne 05 DİKEY — Örnek 3 (PPC temel, düz canvas) — RAPOR

Tema: acik + koyu (video-acik.mp4, video-koyu.mp4) · 05.11.2026 · 1080×1920

## Yapılan
- Şablon: present-continuous-dikey/05 (iyi örnek); sahne-ortak.js yerel kopya (ppc yolları, ortak kunye.js `altyaziMetin/altyaziCiz` — yamalı küçülme kullanılıyor, yerel dilimleme YOK).
- Yerleşim (BRIEF-DIKEY §4): çip "Example 3 / 3"; kart 48,372 984×300 (Look! kırmızı Fredoka 110 + 2 satır Fredoka 72, "has been" halka); Caveat 64 çeviri iki satır (y 730/794); orta: umbrella 420 px (sol), cloud-rain 420 kutu (orta), sokak çizgisi + 3 su birikintisi (y 1250); sağ üstte Caveat 64 "izi şimdi / görünüyor" + sarı ok sokağa; alt: has been + V-ing Fredoka 110 (taban 1364). Altyazı bandı 1400–1536 dolu, platform bandı boş.
- Zamanlar yatayla aynı (küresel sn → yerel kare, TBAS 47,27).

## Sayılar
- 439 kare, 1080×1920 yuv420p (iki tema, ffprobe). olaylar.json 25 olay, ilk 16, son 406. Son 12 kare durgun.

## Kapılar
- Editör kapısı (başsız, ortak-tarayici + cdpilot context): t=52 → slot {"no":4,"hazir":true,"goster":true,"op":1} (sahne 05); t=72 ve t=80 → {"no":5,"hazir":true,"goster":true,"op":1} (sahne 06). Konsol: yalnız t=52 sayfasında 2 × "405 Method Not Allowed" (canvas sahnesinin /log POST çağrısı: önizleme sunucusu /log kabul etmez, görüntüyü etkilemez; t=72/80 sayfalarında konsol temiz).
- Kare: k/0097.png, k/0247.png, k/0382.png (tam boy), kontrol.png, k/telefon-01..03.png (360×640 kontak) Read ile açıldı: HUD okunuyor, içerik bandı 372–1364 dolu, yazı ≥ 64 px, umbrella 420 px, altyazı var, platform boş, çakışma yok.

## Neden yeniden
1. Tur 1: formül "has been + V-ing" su birikintisine değiyordu, çizimler küçük (280 px) ve ortada boşluk vardı → sokak y 1250, umbrella 420 px sola, bulut orta, not sağ üste; kart 316→300 px, Look! 10 px yukarı.
2. Tur 1: bulut Coco damlasıydı → tabler/cloud-rain.
3. dikey 05 koyu: yük yüzünden "ZAMAN AŞIMI 60 sn" (kod hatası değil) → aynı kodla bir kez yeniden koşuldu.

## Açık sorular
- cloud-rain çizimi umbrella'dan küçük görünüyor (ikonun iç boşluğu; kutu 420, çizim ≈ 357×230).
- Daire içinde 3 yok (BRIEF-DIKEY §4 çip ile verir).
