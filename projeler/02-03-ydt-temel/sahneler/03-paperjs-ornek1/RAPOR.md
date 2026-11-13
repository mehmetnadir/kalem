# 03-paperjs-ornek1 — RAPOR (13.11, P2; render yok)

Motor: Paper.js · 1920×1080 · 30 fps · 543 kare · t_bas 15.31. Tema: açık/koyu hazırlık koştu (son koşu açık).

## Olay ↔ sözcük t0 (yerel kare = round((t − t_bas) × 30); sapma 0)

| Cümle:sözcük | t0 (sn) | Kare | Olay |
|---|---|---|---|
| 3:0 Birinci | 15.86 | 16 | daire içinde 1 |
| 3:1 örnek. | 16.34 | 31 | tek kart kutusu |
| 3:2 We | 17.07 | 53 | kök sözcük sözcük (We) |
| 3:7 airport | 17.95 | 79 | uçak simgesi |
| 3:8 at | 18.43 | 94 | `at 9.` sarı daire |
| 3:10 Saat | 19.72 | 132 | Türkçe çeviri |
| 3:14 Plan | 22.52 | 216 | PLAN etiketi |
| 3:16 saat | 23.56 | 247 | saat simgesi |
| 3:18 Planı | 24.6 | 279 | `We` sarı daire |
| 3:26 şimdiki | 27.8 | 375 | `are leaving` sarı daire |
| 3:29 Yapı | 29.48 | 425 | formül kartı |
| 3:31 yapı: | 30.52 | 456 | V-ing |
| 3:32 are | 31.2 | 477 | `are` yakın çekim kutusu + satır 2 |
| 3:33 artı | 31.72 | 492 | + |
| 3:34 leaving. | 32.36 | 511 | leav-ing |

## Kapı ve göz

- Çakışma kapısı ve sahne-kare: ŞEF NOTU (13.11 12:40) gereği KOŞULMADI; QA şeridi koşar. Kare görüntüsü yok (`k/` boş).
- `node --check` JS: geçti. `ONIZLE_YALNIZ=1 bash calistir.sh` (koyu, sonra açık): "önizleme hazır".
- Kapı notu: dekoratif çizgiler `isaret`; yazı kartın içinde; simgeler yazıyla örtüşmeyecek konumda (elle hesap).

## QA 13.11
- Önce `ONIZLE_YALNIZ=1 bash calistir.sh` (açık tema) koşuldu. Kapı: çakışma yok (72 örnek, 3209 kutu). Kareler `k/03-paperjs-ornek1-{16.5,19,26,32.5}.png`, koyu `kk/03-paperjs-ornek1-28.png`.
- Göz: soru metni 2 satır, uçak ve saat simgeleri anlamlı (uçak = airport, saat = at 9), PLAN etiketi, formül kartı künyeye taşmıyor; koyu temada renkler doğru. Düzeltme yok. Kalan sorun yok.
- QA 13.11 ek (halka/kutu taraması): at 9 ve We/are leaving halkaları, formül kartındaki are kutusu el altçizgisine çevrildi (`sahne-03.js`). Kapı: çakışma yok (72 örnek, 3189 kutu). Kare `k/03-paperjs-ornek1-31.7.png` doğrulandı.
