# Sahne 03 — Örnek 1 (Paper.js, 855 kare, t_bas 16,27, cümle 5–9) — 02-02-ydt-temel

Tema: acik (son önizleme hazırlığı açık; koyu da koştu)

Durum: yazıldı, önizleme hazırlığı tamam. Kapı ve sahne-kare KOŞULMADI (EK). Render yok.

## İçerik
- c5: sarı daire içinde 1. c6: kök cümle 2 satır (Fredoka 56, satır aralığı 90), sözcük zamanlı + sarı alt çizgi kayar; `go`, `have` sarı daire; `every summer` altı çizgi.
- c7: Türkçe çeviri (Caveat 48, y 500, sözcük pencereli); sağda kalemle güneş (yaz) + yazlık (home). 32,70–33,00 çeviri solar (yer açılır).
- c8: `every summer` sarı daire → ok → `tekrar` (Caveat, sarı).
- c9: satır 1 `go → rutin`, satır 2 `have → kalıcı durum`; ikisini birleştiren sarı ayraç + parıltı; kökteki iki `I` daire; formül satırı `I + go / have` (yakın çekim yerine).

## Olay ↔ sözcük t0 (yerel kare = round((t − 16,27) × 30))
| Olay | Kare | Küresel sn | Sözcük (t0) | Sapma |
|---|---|---|---|---|
| daire 1 | 17 | 16,84 | Birinci (16,82) | 0,02 |
| cümle başı | 64 | 18,40 | I (18,41) | 0,01 |
| go daire | 74 | 18,74 | go (18,65) | 0,09 |
| every summer altı çizgi | 94 | 19,40 | every (19,37) | 0,03 |
| have daire | 137 | 20,83 | have (20,77) | 0,06 |
| Türkçe çeviri | 186 | 22,47 | Her (22,48) | 0,01 |
| güneş | 195 | 22,77 | yaz (22,76) | 0,01 |
| yazlık | 251 | 24,64 | yazlığım (24,64) | 0 |
| every summer daire | 359 | 28,24 | every (28,24) | 0 |
| ok → tekrar | 451 | 31,30 | tekrar (31,45), ok 0,15 önce | 0,15 |
| go satırı | 503 | 33,03 | Gitmek (33,04) | 0,01 |
| rutin | 527 | 33,84 | rutin. (33,84) | 0 |
| have satırı | 556 | 34,80 | Yazlığın (34,80) | 0 |
| kalıcı durum | 590 | 35,94 | kalıcı (35,92) | 0,02 |
| ayraç | 628 | 37,20 | İkisi (37,20) | 0 |
| I daire 1 + formül I | 703 | 39,70 | I. (39,69) | 0,01 |
| formül go + parıltı | 792 | 42,67 | go (42,67) | 0 |
| formül have | 824 | 43,73 | have. (43,73) | 0 |

## Kanıt
- `ONIZLE_YALNIZ=1 bash calistir.sh --tema acik|koyu|acik` → "önizleme hazır" (son AÇIK). `node --check sahne-03.js` temiz.
- Taklit koşu (Node, sahte DOM + sahte Paper): 855 kare hatasız; 37 olay (kare 17–824), son 12 karede olay yok. SVG çizimleri (güneş, home) taklitte boş: yerleşim QA'da görülecek.

## Sapma / dikkat
- Taslak `yakin_cekim` (go, have): kökte yer değişmeden dim yapılamadığı için altta `I + go / have` formül satırı + parıltı ile verildi.
- `every summer` ilk vurgusu altı çizgi (taslak), ikincisi daire (isaret); aynı kutuya iki kez dokunma karaoke altçizgisiyle çakışmasın diye çizgi y+24 (satır aralığı 90).
- `kalem-paper.js`: örnek paketin en yeni sürümü (03, `?canli=1` günlük atlama), yalnız paket yolu değişti.

## Kare yolları
`k/` boş (EK). calistir.sh denetim kareleri: 20,5 / 25,0 / 36,2 sn + son durgun kare.

## QA 13.11
- Kapı: ilk koşu CDP zaman aşımı; düzeltme sonrası "çakışma yok (114 örnek, 3664 kutu)".
- Kareler: k/03-paperjs-ornek1-17.9, -20.5, -25, -36.2, -37.5, -43.5 (açık) · -28.3 (koyu).
- Göz: gerçek Paper geometrisi, güneş ve yazlık SVG'si, çeviri, ok/etiketler, formül satırı doğru; koyu tema renkleri doğru.
- Düzeltme: sarı "1" dairesi (y 190) ilk satırdaki `go` dairesine ve kök cümleye değiyordu → daire y 172 / r 58, rakam y 208 (sahne-03.js). `ONIZLE_YALNIZ=1 bash calistir.sh` (son koşu açık), kapı + kareler yeniden: temiz.
- Kalan: yok. Not: ayraç `}` 37,5 sn karesinde yarım çiziliyor (animasyon ortası), 43,5 sn karesinde tam.

- Halka kuralı: DEĞİŞTİ: go, have, I (×2) halkaları ve `every summer` halkası → altçizgi (tek(); every summer, summer göründükten sonra 28,56). BIRAKILDI: sayı dairesi "1" (harfe değmiyor, 29.6 karesinde görüldü). Kapı: çakışma yok (114 örnek, 3671 kutu).

- zaman eşitleme 13.11: KARE 855→857 (calistir.sh N dahil), T_BAS 16.27 aynı; cümle 9 içi düzensiz kayma (−0,24…+0,16) için 15 sabit zaman sözcük çapasıyla eşlendi. Kapı temiz (114 örnek, 3675 kutu); kareler k/…-28.3…37.5 (işaretler sözcükten sonra).
