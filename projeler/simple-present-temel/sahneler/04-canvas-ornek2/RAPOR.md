# Sahne 04 — Örnek 2 (YATAY, düz canvas) · simple-present-temel

Tema: acik + koyu (ikisi de koşuldu; `video.mp4` = koyu).

| Ölçüt | Sonuç |
|---|---|
| Kare | 482 (ffprobe: 1920×1080 yuv420p 30 fps, iki tema) |
| Olay | 32 (`olaylar.json`, son olay kare 455) |
| Kaynak | Present Continuous 04 şablonu (`sahne-ortak.js` kopya, künye yolu simple-present-temel, etkin alanı `this.etkin`) |

Zamanlama: daire 2 28,24 · cümle 29,53 (My…bus.) · usually halkası 30,55 · figür 29,6 · otobüs 31,3 · TR 32,74 ·
etiketler 35,53 / 36,73 / 37,45 (tik +0,55) · gün kutuları 37,9+ · goes halkası 40,96 · formül `he + go → go-es` 41,35–42,6.

Kontrol: `kontrol.png`, `k/0114,0279,0453.png` (koyu), `k/acik-0200.png`, `k/acik-0469.png` (acik).
Bakılan: acik-0469: künye tam, cümle iki satır, çakışma 0, formül kartı sağ altta.
Editör kapısı: `onizle.html?surum=ana-yatay&tema=acik&t=35` → slot no 3 `hazir:true, goster:true`, konsol boş.

Yeniden koşu nedeni: ilk koşuda `S.dizi("My", 29.53, 9)` 9. sözcük olarak "Kardeşim"i cümleye kattı;
8'e indirildi, iki tema yeniden koşuldu. Sonradan `canliKip` koruması (CIZIM/OLAYLAR /log POST, canlıda 405) eklendi.
Açık sorular: yok.
