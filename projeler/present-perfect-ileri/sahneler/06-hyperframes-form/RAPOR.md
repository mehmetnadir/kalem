# PRESENT PERFECT İLERİ yatay · sahne 06 Soru + Kural (HyperFrames) — RAPOR (05.11.2026)

Tema: acik + koyu (ikisi de koşuldu; `video-acik.mp4` + `video-koyu.mp4`; `video.mp4` = son koşu).

## Yapılan
- `uret.py` (+ `olay.py`, `yardim.py`, `zamanlar.json`, `calistir.sh`; şablon present-continuous-ileri 06): öğrenci başı + balon Fredoka 600 44 (2 satır; `ago` sarı belirteç 69,95; `has landed` kırmızı çarpı 71,15–71,99) ·
  künye `Question` → `Rule` (73,62; ajanda Exam → Rule) · balon köşeye küçülür (73,30) · `Hayır.` + sarı bantlı `Bitmiş zaman` + `Present Perfect` kırmızı çizgi + `yasak` (74,58–77,42) ·
  el kutusunda 3 kırmızı etiket `ago` / `yesterday` / `last year` + yasak işareti (78,35 / 79,27 / 80,27) ·
  iki sütun `Finished → Simple Past` / `Unfinished → Present Perfect` Fredoka 60–72 (81,72 / 84,16) · kod kartı `ago → Simple Past` (kırmızı) / `yet → Present Perfect` (sarı) + tik + `Next lesson →` (87,09–92,3).
  Çerçeveler (etiket kutusu, iki sütun, kod kartı) 70,2–71,1'de erken çizilir. Ok işaretleri kalem yolu.

## Sayılar
- Kare 785 (ffprobe h264 yuv420p 1920x1080 30 fps, ikisi de tema). `olaylar.json` 46 olay (cizgi 25, tik 18, vurus 3), son olay kare 729, aynı karede en çok 3.
- Son 30 kare durgun: kare 755 ↔ 784 PSNR 62,1 dB (yalnız gren).
- Zamanlama (yerel kare = (t − 68,60) × 30): balon çizgisi 17 · çarpı 77 · künye geçişi ve `Hayır.` 151 · ago 292 · yesterday 320 · last year 350 · Finished 394 · Unfinished 467 · kod `ago` 605 · `yet` 665.

## Kapılar
- Editör: `ana-yatay&tema=acik&t=75` ve `t=92` → `slot no 5 hazir:true goster:true op:1`; konsol hata satırı yok.
- Baktığım kareler (Read): `k/72.png`, `k/327.png`, `k/507.png`, `k/642.png` (+ `k/177.png`, `k/432.png`, `kontrol.png`).

## Neden yeniden
- Tur 1 → 2: `Bitmiş` sözcüğündeki `ş`, Fredoka 700 yazı tipi alt kümesinde yok (fontTools cmap: ş ğ İ yok) → tarayıcı yedek yazıyla çizdi, genişlik 0 sayıldı, `zaman` üst üste bindi.
  Çözüm: `Bitmiş zaman` Caveat 700 (Türkçe glif var).
- Çerçeveler konuşmadan önce çizilsin diye (alt yarı boş kalmasın) zamanları 70,2–71,1'e çekildi.

## Açık sorular
- `ortak/` dosyalarında: `yardim.py`'deki yazı tipi alt kümesi U+2192 (→) ve Fredoka'da ş ğ İ içermiyor; HF sahnelerde Türkçe yazı Caveat ya da Lexend ile yazılmalı.
- `ortak/hf_tema.py` CSS'inde kalıntı kural: `#root.tema-acik #t2{fill}` — HF sahnede kimlik `t2` kullanılırsa sarıya boyanır (dikey sahnede yakaladım).
