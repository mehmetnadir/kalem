# İleri dikey sahne 05 (Örnek 3) — RAPOR (05.11.2026)

Tema: acik + koyu (ikisi de koşuldu; video-acik.mp4 + video-koyu.mp4; video.mp4 = son koşu).

## Yapılan
- Sıfırdan 9:16: kart Fredoka 64 (3 satır), TR Caveat 64, orta bantta yolcu 420+ px + otobüs + takvim, sağ sütunda yarın→PLAN, bilet ✓, saat ✓; alt formül are + tak-ing / am + pack-ing Fredoka 96; altyazı bandı dolu; platform bandı boş.

## Sayılar
- Kare: 372 (ffprobe yuv420p 1080x1920, 30 fps; zaman.json ile birebir).
- Olay: 34 (olaylar.json, en çok kare 355 < kare sayısı).
- Editör kapısı: `window.EDITOR.durum()` t=48 → slot no 4 hazir:true goster:true; t=70 → slot no 5 hazir:true goster:true (yatay ana-yatay, dikey dikey-tam); `cdpilot console` boş (hata 0).

## Bakılan kareler (Read ile)
k/0118.png, 0238.png, 0355.png, kontrol.png, k/telefon-01.png, telefon-02.png (360x640 kontak)

## Neden yeniden
Tur 1: calistir.sh ls hatası (sed) düzeltildi; takvim otobüs çatısına değiyordu → yukarı alındı; formül satırları zemin çizgisine/birbirine değiyordu → Fredoka 96, B1 1190; alt çizgi y+16.

## Açık sorular
- Tabler bus yalnız otobüs gövdesi; "bag" için çizim yok (cümlede yalnız yazı).
