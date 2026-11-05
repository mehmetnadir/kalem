# Sahne 05 — Örnek 3 (PPC temel, YATAY, düz canvas) — RAPOR

Tema: acik + koyu (video-acik.mp4, video-koyu.mp4; video.mp4 = son koşu) · 05.11.2026

## Yapılan
- Şablon: present-continuous/05 (sahne.js, sahne-ortak.js, sayfa.html, calistir.sh); yol sabitleri ppc, kayma 0, TBAS 47,27, KARE 439, ICERIK 427.
- İçerik BRIEF §4 sahne 05: daire 3 · Look! kırmızı pop (49,11) + kalem ünlem · iki satır cümle (The street is wet. / It has been raining., sözcük zamanlı) · sağda tabler cloud-rain (520 px) + sokak çizgisi (wet, 50,51) + 3 su birikintisi + coco umbrella (It, 51,23) · Caveat çeviri (53,12 / 54,88) · sarı ok + "izi şimdi görünüyor" (56,56) · formül kartı has been + V-ing / rain-ing (57,91) · halka "has been" (59,51) ve raining (60,79).
- Dosyalar: sahne.js, sahne-ortak.js, sayfa.html, calistir.sh (alarm 1500), olaylar.json, kontrol.png, k/.

## Sayılar
- video-acik.mp4 / video-koyu.mp4: 1920×1080 yuv420p, 439 kare (ffprobe nb_read_frames).
- olaylar.json: 26 olay, ilk kare 16, son kare 406 (< 439). İlk 12 kare boş, son 12 kare durgun (içerik 427'de biter).

## Kapılar
- Editör kapısı (başsız, ortak-tarayici + cdpilot context): t=52 → slot {"no":4,"hazir":true,"goster":true,"op":1} (sahne 05); t=72 ve t=80 → {"no":5,"hazir":true,"goster":true,"op":1} (sahne 06). Konsol: yalnız t=52 sayfasında 2 × "405 Method Not Allowed" (canvas sahnesinin /log POST çağrısı: önizleme sunucusu /log kabul etmez, görüntüyü etkilemez; t=72/80 sayfalarında konsol temiz).
- Kare (kendi gözümle): k/0097.png, k/0247.png, k/0382.png (tam boy), kontrol.png. Künye tam, çakışma yok, güvenli alan içinde, kart logoya 20 px uzak, yazı okunur.

## Neden yeniden
1. Tur 1: Coco rain.svg tek yağmur damlasıydı (bulut değil) → tabler/cloud-rain.svg.
2. Tur 1: cümle "has / been" farklı satıra düşüyordu (halka bölünüyordu) → iki cümle ayrı satırda iki cumleYaz.
3. Tur 1: kart logoya 6 px yakındı → kart y 836 → 820.

## Açık sorular / sapma
- Coco'da yağmur bulutu yok; tabler cloud-rain kullanıldı (çizim yalnız ortak/cizim içinden).
- Öncelik: son 12 kare durgunluğu salınım donduruldu (ICERIK), gren her karede canlı kalır.
