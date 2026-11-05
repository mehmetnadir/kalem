# Sahne 03 YATAY — Örnek 1 (PPC temel, Paper.js)

Tema: acik ve koyu ikisi de koşuldu (video-acik.mp4, video-koyu.mp4; video.mp4 son koşu).

- Kare: 467 (ffprobe 467/467, 1920x1080 yuv420p 30 fps, iki tema). t_bas 17,13. Olay: 30 (en büyük kare 443).
- Dosyalar: sahne-03.js, kalem-paper.js (ana PPC 02 kopyası), sayfa.html, calistir.sh.
- İçerik: BRIEF §4 sahne 03 satırlarının hepsi (1 dairesi, cümle, figür sitting-4 + otobüs + saat, for twenty minutes yayı + 20 dk, TR çeviri, zaman çizgisi + in progress, for + süre uzunluğu, have been / waiting daireleri, formül kartı have been + V-ing / wait-ing).
- Editör kapısı (başsız, ortak-tarayici): `?surum=<ana-yatay|dikey-tam>&tema=acik&t=22` → slot no 2 `hazir:true, goster:true, op:1`; `t=38` → slot no 3 `hazir:true, goster:true, op:1`. Editör konsolundaki 404 (3 adet) başka ajanların henüz yazılmamış sahnelerinden; kendi sahne sayfam `?canli=1` konsol hatası 0.
- Bakılan kareler: k/0101 k/0230 k/0440 k/0454 (acik ve koyu), kontrol.png. Çakışma yok, künye tam, yazı okunur.
- Neden yeniden: (1) ilk koşuda sarı yay Türkçe çevirinin üstüne biniyordu → yay y+24, çeviri y 505, zaman çizgisi y 640; (2) wait-ing satırı kart sağ kenarına taşıyordu → x 200; (3) "20 dk" figürün bacağına değiyordu → yayın altına, sağa.
- Açık soru: yok.
