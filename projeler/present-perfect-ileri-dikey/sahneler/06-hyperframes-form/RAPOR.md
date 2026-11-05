# PRESENT PERFECT İLERİ dikey · sahne 06 Soru + Kural (HyperFrames, 1080x1920) — RAPOR (05.11.2026)

Tema: acik + koyu (ikisi de koşuldu; `video-acik.mp4` + `video-koyu.mp4`; `video.mp4` = son koşu).

## Yapılan
- `uret.py` (+ `olay.py`, `yardim.py`, `zamanlar.json`, `calistir.sh`; şablon present-continuous-ileri-dikey 06, yerleşim sıfırdan):
  öğrenci başı + balon Caveat 76, 2 satır (küçülünce 57 px; `ago` sarı belirteç, `has landed` kırmızı çarpı) → çip `Question` → `Rule` (73,62) →
  `Hayır.` + sarı bantlı `Bitmiş zaman` (Caveat) + `Present Perfect` kırmızı çizgi + `yasak` → hand-kutu 3 kırmızı etiket `ago` `yesterday` `last year` (ink yasak çizgisi) →
  tablo 2 satır: `Finished → Simple Past` / `Unfinished → Present Perfect` Fredoka 68 → kod kartı `ago → Simple Past` (kırmızı) / `yet → Present Perfect` (sarı), Fredoka 72 + `Next lesson →`.
  Tablo iskeleti erken: etiket kutusu 70,0 · tablo satırları 70,35 / 70,6 · kod kartı 70,85; hücreler konuşma anında dolar.
  Altyazı `div` (HF, `altyazi_svg`: 44 → 40 → 36 küçülür, sonra 3 satır; her parça `tl.set` ile açılıp kapanır). Kök `data-width="1080" data-height="1920"`.

## Sayılar
- Kare 785 (ffprobe h264 yuv420p 1080x1920 30 fps, ikisi de tema). `olaylar.json` 43 olay (cizgi 22, tik 18, vurus 3), son olay kare 729, aynı karede en çok 3.
- Son 30 kare durgun: kare 755 ↔ 784 PSNR 62,8 dB.

## Kapılar
- Editör: `dikey-tam&tema=acik&t=75` ve `t=92` → `slot no 5 hazir:true goster:true op:1`; konsol hata satırı yok.
- Baktığım kareler (Read): `k/72.png`, `k/642.png` (+ `k/177.png`, `k/327.png`, `k/432.png`, `k/507.png`), `kontrol.png`, `k/telefon-03.png` (360x640 kontak, koyu): HUD okunur, bant dolu, balon yazısı ≥ 44 px ve 2 satır, ≥ 64 px içerik yazısı.

## Neden yeniden
- Tur 1 → 2: (1) `Bitmiş` `ş` Fredoka 700 alt kümesinde yok → Caveat; (2) tablo satırı kimliği `t2`, ortak `hf_tema.py` kuralı `#root.tema-acik #t2{fill}` ile turuncuya dolmuştu → `tbl1`/`tbl2`;
  (3) `Hayır.` öğrenci başının altına değiyordu → A satırları 704 / 800'e indi; (4) kod kartı `Next lesson`a değiyordu → kart 168 px, satırlar sıkıldı.

## Açık sorular / sapma
- Tablo yazısı 68 px (BRIEF 80): `Unfinished → Present Perfect` 80 px'te 984 px'e sığmıyor.
- Kod kartı yazısı 72 px (BRIEF 110): `yet → Present Perfect` 110 px'te sığmıyor.
- `ortak/hf_tema.py`: kalıntı `#t2` kuralı (rapor yatay 06'da da var).
