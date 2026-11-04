# Sahne 01 DİKEY — Giriş (HyperFrames 1080x1920, 102 kare)

Tema: koyu (ikisi de koştu: `video-acik.mp4` + `video-koyu.mp4`; `video.mp4` = son koşu = koyu)

## Sonuç
- ffprobe: h264 yuv420p 1080x1920 30 fps, 102 kare (zaman.json ile birebir), her iki tema.
- `olaylar.json`: 52 olay (cizgi 44, tik 3, hisirti 3, vurus 1, parilti 1), son olay kare 89 (< 90).
- Konsol: sahne sayfası tek başına (`proje/index.html?canli=1&tema=acik`) hata 0. Editör
  (`onizle.html?surum=dikey-tam&tema=acik`) t=1,5: slot 0 `hazir:true, goster:true`; t=8: slot 1 `hazir:true, goster:true`
  (editör konsolunda 7 adet 404 var; kaynağı bu sahne değil, çünkü sahne sayfaları tek başına temiz; muhtemelen
  henüz yapılmamış 03–06 iframe'leri ya da editör kaynakları).

## Yerleşim (BRIEF-DIKEY)
Logo 387x96 sol üst (damga 0,0–0,4) · rozet hapı y236 h72 + GRAMMAR hapı (uçuşta söner) · PRESENT 200 px taban 520,
CONTINUOUS 156 px taban 690 (kalemle, 0,65–1,45) · cümle 1 Caveat 80 iki satır (815/900), sözcük zamanlı (1,00 → 2,92) ·
figür standing-3 430 px + ev 360 px (y 950–1380) · uçuş 2,0–3,0: başlık HUD ders adına 56 px, cümle taban 440/525'e kayar
(sahne 02'nin cümle 1 yeriyle aynı), "Hook" çipi + ders adı belirir · altyazı Lexend 500 44, cümle 1 (0,95 → son).

## Kapı: gözle bakılan kareler
`k/36.png`, `k/60.png`, `k/87.png` (koyu), `k/87-acik.png`, `k/telefon-01.png` (koyu 4 kare), `k/telefon-acik.png` (açık, 6 kare:
0, 9, 20, 45, 70, 101), `kontrol.png`. HUD okunur, altyazı bandında metin, platform bandı (1536+) boş, çakışma yok;
kare 90–101 durgun (son kare = kare 87 görüntüsü).

## Neden yeniden
1. İlk render: bitişte (kare 87) alt yarı (y 560–1400) boştu, çünkü eskiz (figür + ev) uçuşta soluyordu → eskiz solması
   kaldırıldı, figür + ev bitişte kalır (içerik bandı doldu). BRIEF "figür solar" der; "alt yarı boş olmayacak"
   kuralı öncelikli seçildi.
2. İlk koşu makine yükü 232 iken hyperframes 480 sn zaman aşımına düştü (kare 10'da takıldı); `alarm` 900 sn yapıldı.

## Sapmalar / açık sorular
- Başlık 190 px DEĞİL: `CONTINUOUS` 190 px'te 1175 px tutar, 984'e sığmaz → CONTINUOUS 156 px (966 px), PRESENT 200 px.
- Bitiş karesinde yatay orta boşluk var (y 560–950); figür + ev tek bant (950–1380) ve cümle üstte. İsterseniz figür
  yukarı alınabilir.
- Eskiz uçuşta solmadığı için kare 90–101'de figür + ev sahne 02'nin ilk karesiyle (boş zemin) geçişte çapraz görünür.
