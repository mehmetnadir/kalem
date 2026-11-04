# Sahne 04 DİKEY — Örnek 2 (düz canvas)

Tema: koyu (son koşu; acik da koşuldu)

- Kare: 487 (video-acik.mp4, video-koyu.mp4: 1080x1920 yuv420p 30 fps, ffprobe 487/487). t_bas 30,15.
- Olay: 33 (en büyük kare 434, aynı karede en çok 3).
- Dosyalar: sahne.js, sahne-ortak.js (D1 kopyası, dikey kunye/kalem-canvas + altyazı), sayfa.html, calistir.sh.
- Yerleşim: kart 372–~605 (Fredoka 72, 2 satır) · TR Caveat 64 · not `şu anda değil → bu günlerde` (Caveat 64, kalem oku)
  · kız kardeş 425 px + piyano + 3 nota (y 755–1180) · formül `is + tak-ing` ↓ `be + V-ing` Fredoka 110 · altyazı.
- Editör kapısı: bkz. sahne 03 RAPOR (t=38 → slot no 3 `hazir:true, goster:true`). Sahne sayfası `?canli=1`
  konsol hatası 0 (son sürüm).
- Bakılan kareler: k/0086 k/0251 k/0431 k/0474 (acik ve koyu), kontrol.png, k/telefon-01.png, k/telefon-02.png.
- Neden yeniden: (1) ilk koşu 480 sn alarmına takıldı (makine yükü 350) → alarm 1200 sn; (2) altyazı 3 cümleli
  parça yatay taşıyordu → cümle cümle (altyaziSec); (3) figür 362 px idi (≥ 420 gerek) → kart/TR/not sıkıştırıldı,
  figür 425 px; (4) piyano/figür altına formül yaklaştı → yA 1274, yB 1382.
- Son düzenleme (yalnız günlük): `fetch("/log")` çağrıları canlı kipte 405 veriyordu → kaldırıldı/korumaya alındı;
  görüntü değişmez, videolar bu düzenlemeden önceki koşudan.
- Açık soru: `ortak/kunye.js` altyaziCiz uzun parçada taşma (bkz. sahne 03).
