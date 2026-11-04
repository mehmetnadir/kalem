# Sahne 01 giriş (dikey 1080x1920, HyperFrames)

- Kare: 102 (ffprobe yuv420p, 30 fps, acik + koyu ikisi de; video-acik.mp4, video-koyu.mp4, video.mp4 = son koşu koyu)
- Olay: 52 kayıt (olaylar.json, kare aralığında)
- Kapı 1 (editör, başsız, konsol): dikey t=1.5 ve t=8: durum() slot hazir:true goster:true (t=1.5 slot 0, t=8 slot 1); konsol 4x 404 = projenin surumler.json dosyası yok (dikey proje kökü; sahne dosyası değil)
- Kapı 2 (kareler): k/36.png, k/59.png (kapak karesi), k/87.png, k/telefon-01.png (360x640 kontak), kontrol.png; logo HUD sol üst 96, ders adı 56 (uçuş sonu), rozet 72, çip Hook 80, başlık 190 px, cümle Caveat 80 iki satır, figür 420 px, altyazı bandı cümle 1
- Neden yeniden: ilk koşuda GRAMMAR rozeti uçuştan sonra kalıyor ve çip dolgusu canvas künyesinden 16 px dardı (HUD sahneler arası tutarsız): rozet uçuşta solar, cipDolgu 64 yapıldı, iki tema yeniden koşuldu
- Açık sorular: HUD'da tek rozet var (canvas künye); GRAMMAR yalnız kapakta
