# 02-paperjs-kanca — RAPOR (13.11, P2; render yok)

Motor: Paper.js · 1920×1080 · 30 fps · 381 kare · t_bas 3. Tema: açık/koyu hazırlık koştu (son koşu açık).

## Olay ↔ sözcük t0 (yerel kare = round((t − t_bas) × 30); sapma 0)

| Cümle:sözcük | t0 (sn) | Kare | Olay |
|---|---|---|---|
| 1:5 sinyal | 3.72 | 22 | SIGNAL yazısı + sarı belirteç başlar |
| 1:6 sözcüğünde. | 4.16 | 35 | WORD yazısı |
| 2:2 şimdiki | 6.83 | 115 | sol çip (PRESENT CONTINUOUS) kutu + yazı |
| 2:3 zamanı | 7.31 | 129 | sol çip sarı daire |
| 2:5 geniş | 8.11 | 153 | sağ çip (SIMPLE PRESENT) |
| 2:6 zamanı | 8.43 | 163 | sağ çip sarı daire |
| 2:12 ikisini | 11.15 | 245 | iki çipin altında sarı ayraç |
| 2:13 yan | 11.67 | 260 | `vs` kalemle |
| 2:16 Alıştırma | 12.99 | 300 | kalem simgesi |
| 2:18 farkı | 14.19 | 336 | iki uçlu fark oku |
| 2:19 yakalıyoruz. | 14.51 | 345 | parıltı |

Kartlar (`goes` üstte, `is going` altta; 01 ile aynı yer) kare 12'de (3,40 sn) yeniden çizilir; kelime bağlı değil (ilk 12 kare durgun).

## Kapı ve göz

- Çakışma kapısı ve sahne-kare: ŞEF NOTU (13.11 12:40) gereği KOŞULMADI; QA şeridi koşar. Kare görüntüsü yok (`k/` boş).
- `node --check` JS: geçti. `ONIZLE_YALNIZ=1 bash calistir.sh` (koyu, sonra açık): "önizleme hazır".
- Kapı notu: dekoratif çizgiler `isaret`; yazı kartın içinde; simgeler yazıyla örtüşmeyecek konumda (elle hesap).

## QA 13.11
- Kapı: çakışma yok (51 örnek, 1041 kutu). Kareler `k/02-paperjs-kanca-{3.72,3.76,3.9,4.3,8.6,12,14.8}.png`, koyu `kk/02-paperjs-kanca-12.png`.
- Düzeltme (şef maddesi 2): `SIGNAL WORD` sarı belirteci t0'da (3,72 sn = kare 22) görünmüyordu (çizim kare 22'de başlıyor, ilk karede 0 px). `sahne-02.js` belirteç `bas` 5 kare erken (fr−5) → 3,72 karesinde belirteç görünür (kareyle doğrulandı). `ONIZLE_YALNIZ=1` koşuldu (son koşu açık), kapı yeniden temiz.
- Göz: açık/koyu temada taşma yok, yazı ≥ 40 px, kartlar doğru yerde. Künye ajandası Hook · Examples · Rule · Trap doğru, etiket "Hook". Kalan sorun yok.
