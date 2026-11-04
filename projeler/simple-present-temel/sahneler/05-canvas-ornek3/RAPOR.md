# Sahne 05 (yatay) — Simple Present Örnek 3

Tema: acik + koyu (ikisi de koşuldu; video-acik.mp4, video-koyu.mp4; video.mp4 son koşu = koyu değil, tema_bitir kopyası)

Kare: 525 (zaman.json ile aynı), 1920x1080 yuv420p 30 fps. olaylar.json: 33 olay, son kare 477.
Bakılan kareler: k/0109.png, k/0334.png, k/0484.png, kontrol.png.
Neden yeniden: (1) uçak sola bakıyordu, kalkış sağa-yukarı → SVG yatay çevrildi, dönme -0,5 → -0,3; (2) pist takvimin üstünden geçiyordu → pist 1500'de bitti; (3) etiket tikleri yazıya biniyordu → kutu genişledi; (4) formül kartı logoya 5 px yaklaşıyordu → y 816, h 152; (5) 'takes off' halkası alt satıra değiyordu → ry 46.
Zamanlar: daire 3 → 43,91; cümle 45,20; takvim 46,80; TR 48,01; tarife 52,88; takes off halkası 57,99; kart 59,27.
Kapı: editör başsız (ana-yatay) t=50 → slot 4 hazir:true goster:true; t=70 → slot 5 hazir:true goster:true; t=90 slot 5 aynı. Konsol: yalnız POST /log 405 (sahne-ortak CIZIM günlüğü, canlı kipte sunucu reddeder; Present Continuous sahneleriyle aynı), başka hata 0.
