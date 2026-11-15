# Sahne 03 Kaydet — huni v2 (simple-present-temel-s1, HyperFrames DİKEY 1080×1920, 105 kare, t_bas 14,63; cümle 3 öğretmen)

| Kapı | Sonuç |
|---|---|
| `qa-yerel.sh … 14.70,16.20,17.65 17.65 --hazirla` | çıkış 0 · `kapı çıkış kodu: 0` |
| `cakisma-kapisi.mjs --sahne 03-hyperframes-kaydet --port 41333 --sunucu 41022` | çıkış 0 · `03-hyperframes-kaydet \| çakışma yok (14 örnek, 1542 kutu)` · 0 uyarı |
| `grep -rniE 'tam ders\|dakika'` (html/js/py) | boş (grep çıkış 1) |
| Kanal katmanı (piksel ölçümü, 4 kare) | 4 karede aynı: logo mürekkebi x 60–239, y 298–330 (resim kutusu 53,2–246,7 × 291–339) · `@ydspublishing` x 264–595, y 296–339 (taban 330) · künye x 60–512, y 386–433 |
| Boş bölgeler (piksel ölçümü, 4 kare) | 0–280 boş · 1570–1920 boş · sağ 963–1080 (y 280–1570) içerik yok |

Durum: yazıldı, önizleme hazır (`ONIZLE_YALNIZ=1`, son hazırlık AÇIK tema). Render yok. Commit yok.
Tema: acik (koyu kare canlı tema geçişiyle çekildi).

## Dosyalar
- `SPEC.md` (şef) → `uret.py` (agy, tek koşu; şef okudu, düzeltme gerekmedi).
- `yardim.py`: `../../../02-04-ydt-temel-s1/sahneler/03-hyperframes-cta/yardim.py` (huni v2) `cp -p` kopyası; şef Edit: belge dizgesi + `KONU = "Simple Present"`.
- `olay.py`: aynı emsalden `cp -p`, değişiklik yok.
- `calistir.sh`: aynı emsalden `cp -p`; şef Edit: başlık, `KARE=105`, ana kapak kopyası çıkarıldı, denetim kareleri (yerel 0,6 / 1,6 / 2,6 / 3,0).
- Üretilen: `proje/index.html`, `zamanlar.json`, `olaylar.json` (3 ses olayı), `k/*.png`, `k/koyu/*.png`.
- Emsal 08 kaydet (`02-04-ydt-temel-s1/sahneler/08-hyperframes-kaydet/`) 19:1x'te yarımdı (RAPOR ve `uret.py` yok); onun `SPEC.md`'si tasarım tabanı oldu, kod tabanı v2 olan 03-cta.

## Yerleşim
| Öğe | Yazı · boy | Konum |
|---|---|---|
| Kanal | logo + `@ydspublishing` Lexend 700 42 | BRIEF tablosu; `#kunye > #kanal`, opaklık 1, animasyon yok |
| Künye | konu `Simple Present` Fredoka 700 34 + rozet `YDT · BASIC` Lexend 700 26 | taban 420; hap 386–434, x 310–513 |
| Kural kartı | kâğıt + kalem kenarı (tek yol, sabit kaydırma dizisi) | x 60–960, y 600–980 |
| `He, she, it: s gelir;` / `I, you, we, they: s yok.` | Fredoka 700 80 (21 · 24 karakter) | x 110, taban 763 / 869; satır 2 sonu ≈ 886 |
| Yer imi (Tabler `bookmark` yolu, ölçek 5, çizgi 7) + `Kaydet` hapı | Fredoka 700 64 | grup 510'a ortalı: ikon x ≈ 321–388, hap x ≈ 412–700, y 1036–1124 |
| Altyazı + karaoke | Lexend 500 44 | 1400–1550, orta x 510; iki cümle sırayla (tek satır) |

## Olay listesi (yerel sn = küresel − 14,63; zaman `sozcukler.json` çapasından, `T(i, bas)` assert'li)
| Olay | Kare · yerel (küresel) | Cümle 3 sözcüğü |
|---|---|---|
| kart girer (ölçek 0,96→1 + opaklık, 0,45 sn, `power3.out`) | 16 · 0,55 (15,18) | Sınavdan |
| kart sabit (sahne sonuna kadar tween yok) | 30 · 1,00 (15,63) | — (17,74'e 2,11 sn) |
| yer imi kalemle çizilir (`strokeDashoffset`, 0,30 sn, `sine.inOut`) | 74 · 2,47 (17,10) | Kaydet. |
| `Kaydet` hapı girer (ölçek 0,9→1 + opaklık, 0,20 sn, `back.out(1.6)`) | 77 · 2,57 (17,20) → 17,40'ta tam | Kaydet. |
| durgun kuyruk | 83 · 2,77 (17,40) → 105 | — |
Ses olayları (`olaylar.json`): kare 16 vurus 0,5 · 74 cizgi 0,6 · 77 tik 0,5.
Altyazı: yalnız cümle 3; `altyazi.json` ham parça 1, `Y.altyazi_svg` onu `Sınavdan önce lazım olacak.` (0,50–2,42) ve `Kaydet.` (2,42–3,50) olarak böler.

## Bakılan kareler
| Kare | Bulgu |
|---|---|
| `k/03-hyperframes-kaydet-14.7.png` | yalnız kanal + künye (kart 15,18'de girer); içerik ve altyazı bandı boş. Doğru. |
| `k/03-hyperframes-kaydet-16.2.png` | kart tam; iki satır kartın içinde, taşma yok; altyazı tek satır `Sınavdan önce lazım olacak.` (x 203–816). |
| `k/03-hyperframes-kaydet-17.65.png` | kart + yer imi + `Kaydet` hapı (açık temada `#ffe066` dolgu, `#1b2440` yazı); altyazı `Kaydet.` altında karaoke çizgisi. Üst üste binme yok. |
| `k/koyu/03-hyperframes-kaydet-17.65.png` | koyu zemin; kâğıt `#fff9e6`, yazı ve kalem kenarı koyu; yer imi krem; hap `#f2a93b`. Kontrast okunur. |

## agy koşu özeti
- uret.py: `/home/sef/.claude/canavar/agy-filo/20261115-192103` (gemini-3.8-flash-high, başarılı, 138 sn).
- Not: özetin "değişen" listesinde başka sahne/paket dosyaları var; o dosyalar aynı çalışma ağacındaki paralel oturumlarındır, bu koşu yazmadı.

## Açık noktalar
- Kartta sarı yok; sahnedeki sarılar: `Kaydet` hapı (tek içerik vurgusu), künye rozeti (kanal katmanı) ve ortak altyazı karaoke çizgisi (açık temada amber `#d9900f`).
- `Kaydet.` sözcüğü 17,82'de biter, sahne 17,74'te (içerik) / 18,13'te (geçiş payıyla) kapanır; altyazı sahne sonunda (yerel 3,50) kapanır. mp4 birleştirmede sahne 04 girişiyle bakılmalı.
- Kural satırları sola hizalı (x 110); satır 1 sağında ≈ 150 px boşluk kalır. Ortalı düzen istenirse tek değişiklik `text-anchor`.
- İlk 12 kare (14,63–15,03) yalnız kanal + künye: geçiş bu aralığı örter.
