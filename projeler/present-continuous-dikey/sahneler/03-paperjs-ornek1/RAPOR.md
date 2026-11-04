# Sahne 03 DİKEY — Örnek 1 (Paper.js)

Tema: koyu (son koşu; acik da koşuldu)

- Kare: 453 (video-acik.mp4, video-koyu.mp4: 1080x1920 yuv420p 30 fps, ffprobe 453/453). t_bas 15,44.
- Olay: 26 (olaylar.json, en büyük kare 438, aynı karede en çok 3).
- Dosyalar: sahne-03.js, kalem-paper.js (D1 kopyası, dikey kunye v2 + altyazı), sayfa.html, calistir.sh.
- Yerleşim: kart 372–~620 (Fredoka 72, 2 satır, sözcük zamanlı) · TR `Şu anda oturuyorum.` Caveat 64 +
  `in progress` bandı · figür 428 px + kamera/sehpa (y 722–1150) · formül `am + sitt-ing` ↓ `be + V-ing`
  Fredoka 110 (y 1268/1378) · altyazı 1400–1536.
- Editör kapısı: `?surum=dikey-tam&tema=acik&t=20` → `{"slot":[{"no":2,"hazir":true,"goster":true,"op":1},...]}`;
  `t=38` → no 3 (sahne 04). Sahne sayfası `?canli=1` konsol hatası 0. Editör konsolunda 7 adet 404
  (kaynak bulunamadı: resource timing boş; favicon.ico 404 dönüyor, sahne 03/04 sayfaları 200).
- Bakılan kareler: k/0077 k/0191 k/0407 k/0440 (acik ve koyu), kontrol.png, k/telefon-01.png, k/telefon-02.png.
  HUD okunur, kart/figür/formül ≥ 64 px, altyazı var, platform bandı boş, çakışma yok; 12 geçiş karesi durgun.
- Neden yeniden: (1) ilk koşuda sehpa ayakları formül satırına değiyordu → fAlt 1190→1150; (2) daire halkaları
  komşu sözcüğü örtüyordu → ry 46→40; (3) `sitt -ing` arası boşluk → bitişik; (4) ok A→B 27 px kalıyordu → sol sütuna;
  (5) altyazı son 12 karede sonraki sahnenin parçasını gösteriyordu → SON−2'ye sabitlendi; (6) çok cümleli altyazı
  parçası → cümle cümle gösterim (altyaziSec).
- Açık sorular: `ortak/kunye.js` `altyaziCiz` 2 satırı aşan metni (cümle 4, 34,89–40,97 sn parçası) yatay taşırıyor;
  burada sahne içinde çözüldü, ortak dosya düzeltilmeli. Editör konsolundaki 404'ün kaynağı (benim sahnelerim değil).
