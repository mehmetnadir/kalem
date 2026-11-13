# Sahne 04 — Örnek 2 (düz canvas, 783 kare, t_bas 44,37, cümle 10–14) — 02-02-ydt-temel

Tema: acik (son önizleme hazırlığı açık; koyu da koştu)

Durum: yazıldı, önizleme hazırlığı tamam. Kapı ve sahne-kare KOŞULMADI (EK). Render yok.

## İçerik
- c10: sarı daire içinde 2. c11: kök 2 satır (Fredoka 56; 7+5 sözcük), `gets`, `swims` sarı halka, `every morning` sarı alt çizgi.
- c12: Türkçe çeviri (Caveat 48, y 500); sağda erkek figür (Open Peeps standing-3; K22: ses öğretmen, özne he) + kalemle havuz (U gövde, iki dalga).
- c13: `every morning` sarı daire; alt satır `every morning → rutin`.
- c14: `He` halka; alt satır `he → get|s · swim|s (+s)`: `s` yukarıdan kayıp oturur, sarı el kutusu çevreler (ek_ayir).

## Olay ↔ sözcük t0 (küresel sn; yerel kare = (t − 44,37) × 30)
| Olay | Küresel sn | Sözcük (t0) | Sapma |
|---|---|---|---|
| daire 2 | 44,95 | İkinci (44,92) | 0,03 |
| cümle başı | 46,43 | He (46,43) | 0 |
| gets halka | 46,75 | gets (46,71) | 0,04 |
| every morning altı çizgi | 47,72 | every (47,71) | 0,01 |
| swims halka | 48,87 | swims (48,83) | 0,04 |
| çeviri + figür | 50,50 | O (50,50) | 0 |
| havuz | 52,58 | havuzda (52,58) | 0 |
| every morning daire | 55,78 | every (55,78) | 0 |
| satır every morning | 58,99 | Bu (58,99) | 0 |
| rutin | 59,23 | rutin. (59,23) | 0 |
| He halka + satır he | 61,63 | he. (61,63) | 0 |
| ok | 63,72 | özneye (63,72) | 0 |
| get (+ s 65,45) | 65,17 | gets (65,17) | 0 |
| swim (+ s 66,80) | 66,47 | swims. (66,47) | 0 |
| (+s) | 69,36 | se (69,36) | 0 |

## Kanıt
- `ONIZLE_YALNIZ=1 bash calistir.sh --tema acik|koyu|acik` → "önizleme hazır" (son AÇIK). `node --check sahne.js` temiz.
- Taklit koşu (Node, sahte DOM, ölçü = 0,55 em tahmini): 783 kare hatasız; 28 olay (kare 17–750). Yerleşim: çakışma yalnız halka-sözcük (beklenen) ve karaoke altçizgisi; taşan 0. İlk görünme karesi 17 (≥12), `figur` SVG taklitte boş.

## Sapma / dikkat
- `sahne-ortak.js` kopyası: `cumle` artık sayı ya da dizi (sahne 5 cümle taşır); başka değişiklik yok.
- Havuz tek `cizim` kutusu olarak kayda geçer (çakışma kapısı çizgileri tek nesne görür).

## Kare yolları
`k/` boş (EK). calistir.sh denetim kareleri: 48,2 / 55,9 / 66,5 sn + son durgun kare.

## QA 13.11
- Kapı: "çakışma yok (104 örnek, 2769 kutu)".
- Kareler: k/04-canvas-ornek2-46.6, -52.8, -60, -68.5 (açık) · -55.9 (koyu).
- Göz: kök cümle, halkalar, çeviri, figür ve havuz (dalgalar) yerinde; ek_ayir (get|s, swim|s) okunuyor; koyu tema doğru. Taşma/binme yok.
- Düzeltme: yok.
- Kalan (küçük): "2" dairesi mürekkep renginde, sahne 03'teki "1" dairesi sarı; tutarsızlık. Dokunulmadı (kapsam dışı, kozmetik).
- QA 13.11 (2. tur, sunucu): "2" dairesi sarıya çevrildi (sahne-ortak.js daireSayi `renk: RT.vurgu`; tüm örnek numaraları sarı). Kapı yeniden: çakışma yok (104 örnek, 2769 kutu). Kareler k/04-…-46.6, -60, -68.5, k/koyu -55.9: temiz.

- Halka kuralı: DEĞİŞTİ: gets, swims, He halkaları (sahne-ortak.js halka() altçizgiye çevrildi) ve `every morning` (altçizgi morning 56,18 sonrası). BIRAKILDI: sayı dairesi "2". Kapı: çakışma yok (104 örnek, 2819 kutu); kare k/…-57.2, -62.3.

- zaman eşitleme 13.11: KARE 783→768, ICERIK 771→756, TBAS 44.37→44.45 (calistir.sh dahil). 21 sabit zaman, eski sözcük t0 → yeni t0 parçalı doğrusal eşlemeyle taşındı (cümle 10–13 +0,08; cümle 14 sonu −0,42 → "(+s)" 68,94). Kapı temiz (102 örnek, 2747 kutu); kareler k/…-68.7 (öncesi yok), -69.4 (sonrası var).
