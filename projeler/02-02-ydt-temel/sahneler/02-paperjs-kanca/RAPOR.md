# Sahne 02 — Kanca (Paper.js, 410 kare, t_bas 3,00, cümle 2–4) — 02-02-ydt-temel

Tema: acik (son önizleme hazırlığı açık; koyu da koştu)

Durum: yazıldı, önizleme hazırlığı tamam. Kapı ve sahne-kare KOŞULMADI (şef EK 13.11 12:40, makine yükü). Render yok.

## İçerik
- c2 (3,39–5,63): el kutusu içinde İngilizce cümle (Fredoka 68, sözcük zamanlı). `get up` ve `every morning` sarı altı çizgi. Sağda kalemle saat (07:00: akrep 7'de sarı, yelkovan 12'de) + "07:00" + güneş.
- c3 (6,10–11,48): `-yor` (kalkıyorum) · `-ing` sarı daire · çift başlı kalem oku · sarı `?`. Hepsi 11,55–11,90 sn arasında solar.
- c4 (12,03–16,35): el kutusu içinde SIMPLE / PRESENT sözcük sözcük (Fredoka 140); "formunu" anında 30 px'e küçülüp künyedeki SIMPLE PRESENT'in üstüne uçar; ajanda: formunu → Rule, kullanımını → Examples (künye kutusunun ALTINDA, y 1046, sarı çizgi — künye kutusuna değmez); "iki kullanım" = iki numaralı el kutusu (1, 2); parıltı.

## Olay ↔ sözcük t0 (yerel kare = round((t − 3,00) × 30))
| Olay | Kare | Küresel sn | Sözcük (t0) | Sapma |
|---|---|---|---|---|
| cümle başı + kart kutusu | 12 | 3,40 | I (3,39) | 0,01 |
| get up altı çizgi | 19 | 3,63 | get (3,63) | 0 |
| saat çemberi | 33 | 4,10 | seven (4,11) | 0,01 |
| every morning altı çizgi | 48 | 4,60 | every (4,59) | 0,01 |
| güneş | 57 | 4,90 | morning. (4,91) | 0,01 |
| `-yor` | 123 | 7,10 | kalkıyorum (6,82–7,46; yor hecesi) | — |
| `-ing` | 185 | 9,17 | ing (9,15) | 0,02 |
| yor ↔ ing oku | 204 | 9,80 | yok. (9,80) | 0 |
| `?` | 229 | 10,63 | Neden? (10,64) | 0,01 |
| başlık kutusu | 273 | 12,10 | Bu derste (12,03 / 12,31) | — |
| SIMPLE | 297 | 12,90 | geniş (12,91) | 0,01 |
| PRESENT | 307 | 13,23 | zamanın (13,23) | 0 |
| başlık künyeye uçar | 321 | 13,70 | formunu (13,71) | 0,01 |
| ajanda Rule çizgisi | 341 | 14,37 | ve (14,35) (formunu bitti 14,27) | 0,02 |
| ajanda Examples + kutu 1 | 357 | 14,90 | kullanımını (14,91) | 0,01 |
| kutu 2 | 371 | 15,37 | kullanımını bitişi (15,47) | — |

## Kanıt
- `ONIZLE_YALNIZ=1 bash calistir.sh --tema acik|koyu|acik` → "önizleme hazır" (3 koşu; son AÇIK).
- `node --check sahne-02.js` temiz.
- Taklit koşu (Node, sahte DOM + sahte Paper; `scratchpad/p2-ydt/harness.mjs`): 410 karenin tamamı hatasız çizildi; 23 olay (kare 12–379); olay yok son 12 karede. Paper geometrisi (gerçek sınır kutusu) taklitte YOK: göz kontrolü QA şeridinde.

## Sapma / dikkat
- Taslak ajanda "Hook · Examples · Form" diyor; künye.js ajandası Hook · Examples · Rule · Trap (şef). Form = Rule eşlendi.
- Künye kutusuna çizgi bindirilmedi (kapı riski); ajanda vurgusu kutunun altında (y 1046).
- Başlık uçuşu `dinamik` + grup matrisi ile (sahne grubu kapı toplayıcısında etiketsiz); uçuş künye üstünde biter, son 6 karede solar.

## Kare yolları
`k/` boş (EK: sahne-kare koşulmadı). calistir.sh denetim kareleri: 4,8 / 9,5 / 13,9 sn + son durgun kare.

## QA 13.11
- Kapı: "çakışma yok (54 örnek, 952 kutu)". Yanlış alarm yok.
- Kareler (açık): k/02-paperjs-kanca-9.5, -11.2, -13.6, -13.9 (uçuş ortası), -15.77 · koyu: k/02-paperjs-kanca-4.8 (açık 4.8 karesinin üstüne yazıldı; açık hâl 9.5 ve sonrası karelerde).
- Göz: kart, saat, güneş, -yor / -ing, başlık kutusu (başlık kutu içinde ortalı), 1-2 kutuları, ajanda çizgileri temiz; koyu tema doğru. 13.9 karesindeki kutu dışı başlık = künye uçuşu ortası, hata değil.
- Düzeltme: yok. Kalan sorun: yok.

- Halka kuralı: DEĞİŞTİ: `-ing` halkası (g kuyruğuna değiyordu) → altçizgi (sahne-02.js). BIRAKILDI: yok. Kapı: çakışma yok (54 örnek, 951 kutu); kare k/…-10.3, -11.0.

- zaman eşitleme 13.11: kayma yok (cümle 2–4 değişmedi). Kapı temiz (54 örnek, 951 kutu).
