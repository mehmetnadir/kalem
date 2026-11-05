# Sahne 03 — Örnek 1 (YATAY, Paper.js) · simple-present-temel

Tema: acik + koyu (ikisi de koşuldu; `video-acik.mp4`, `video-koyu.mp4`, `video.mp4` = son koşu = koyu).

| Ölçüt | Sonuç |
|---|---|
| Kare | 379 (ffprobe: 1920×1080 yuv420p 30 fps, iki tema) |
| Olay | 24 (`olaylar.json`, son olay kare 359; kare 366 sonrası durgun) |
| Kaynak | Present Continuous 03 şablonu; `kalem-paper.js` kopya (künye yolu simple-present-temel) |

Zamanlama (yerel kare; t_bas 15,45): daire 1 → 17 · cümle başı The → 53 · güneş çizimi → 58 · ok east → 96 ·
TR çeviri → 132 · doğa kanunu kutusu → 188 · rises daire → 284 · s daire → 336 · formül kartı → 344–363.

Kontrol: `kontrol.png` (6 kare, koyu), `k/0137,0272,0347,0366.png` (koyu), `k/acik-*.png` (acik).
Bakılan: acik-0366 (son kare): künye tam, çakışma 0, yazı okunur, formül `it + V-s → rise-s` durgun.
Editör kapısı: `onizle.html?surum=ana-yatay&tema=acik&t=20` → slot no 2 `hazir:true, goster:true`, konsol boş.

Yeniden koşu nedeni: ilk koşu sonrası değişiklik yok (sahne). Sonradan yalnız `canliKip` koruması eklendi
(canlı editörde /log POST 405 hatasını önler); render çıktısı etkilenmez.
Açık sorular: yok.
