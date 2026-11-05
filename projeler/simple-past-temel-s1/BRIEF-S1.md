# S1 Shorts — "-Dİ = -ED" (simple-past-temel-s1)

Çıktı: `cikti.mp4` (1080×1920, 30 fps, 21,72 sn anlatım hazır + 1 sn kuyruk) + `kapak.png` (t = 1,97 sn karesi) + `kontrol.png`.
Ana BRIEF biçimi dikeye uyarlandı; stil, kalem darbesi, olay sesi kuralları `../simple-past-temel/BRIEF.md` ile aynı.
Kaynaklar: ses `ortak/anlatim/` (cümle başları 1,00 · 8,10 · 15,29; toplam 21,72), kalıp `dikey-senaryo-kalibi.md` §4–5, senaryo `pilot/grammar-tenses-05-simple-past-temel-s1/senaryo.json`.
Kod `ING-YDT-GR-02-10-T-S1`; HUD sayıları dikey v2 (`ortak/kunye.js`).

## Dikey yerleşim (px)
Yerleşim ve ölçek: ../present-continuous-s1/BRIEF-S1.md '05.11 düzeltme' bölümü +
../present-continuous-dikey/BRIEF-DIKEY.md §2–§3
(tek kaynak, 05.11 karar 6b); 04.11 tablosu geçersiz.

## Sahneler (zaman.json ile birebir)
| # | Klasör | Motor | Küresel sn | Kare |
|---|---|---|---|---|
| 01 | 01-hyperframes-kapak | HyperFrames | 0,00–3,00 (+12 geçiş) | 102 |
| 02 | 02-paperjs-ornek | Paper.js | 3,00–15,29 (+12) | 381 |
| 03 | 03-hyperframes-cta | HyperFrames | 15,29–21,72 (+1 sn kuyruk) | 223 |

Kapak: başlık `-Dİ` / `= -ED` 0,65–1,45; Türkçe cümle `Dün akşam amcamlara gittim.` 1,00'dan sözcük zamanlı (Dün 1,00 · akşam 1,24 · amcamlara 1,64 · gittim 2,20); uçuş 2,0–3,0 (başlık → çip, cümleler yukarı, eskiz solar).
Örnek: `Türkçede biten işe -di ekleriz` (2,91'den) — `-di` (4,35) sarı kutu; `İngilizce de -ed ekler` — `-ed` (6,59) sarı kutu, ok `-di ⇄ -ed`; kart `I watched a movie last night.` 8,10'dan sözcük zamanlı (I 8,10 · watched 8,38 · movie 8,82 · last 9,10 · night 9,30); figür + televizyon 8,3'ten; TR `Dün gece film izledim.` 10,03; `watch + -ed` 12,02–12,98 (Fiile 11,54 · -ed 12,02); `last night` (13,86 / 14,38) sarı belirteç.
CTA: `Tam ders:` 15,29 (Tam 15,29 · ders 15,61) · `Simple Past` bant 16,41 / 16,81 · saat + `Tam ders kanalda · 6 dk` (6 17,69 · kanalda 19,68) · 1 sn durgun kuyruk.

## Çalıştırma
Her sahne `calistir.sh --tema acik`; sonra paket kökünden
`python3 birlestir.py projeler/simple-past-temel-s1 --tema acik --gecis BookFlip --efekt hisirti`.
