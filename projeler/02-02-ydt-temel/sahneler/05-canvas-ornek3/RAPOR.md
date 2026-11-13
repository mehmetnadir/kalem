# Sahne 05 — Örnek 3 (düz canvas, 809 kare, t_bas 70,08, cümle 15–19) — 02-02-ydt-temel

Tema: acik (son önizleme hazırlığı açık; koyu da koştu)

Durum: yazıldı, önizleme hazırlığı tamam. Kapı ve sahne-kare KOŞULMADI (EK). Render yok.

## İçerik
- c15: sarı daire içinde 3. c16: kök 2 satır (5+6 sözcük; seste "twenty seven", ekranda `27` tek sözcük, pencere 74,86–75,50), `completes` ve `27 days` sarı halka.
- c17: Türkçe çeviri (Caveat 48, y 500; "yirmi yedi" → `27`); sağda kalemle Dünya + yörünge elipsi + Ay: Ay "Ay," anında, Dünya "Dünya", yörünge "çevresindeki"; Ay "turunu" anında bir tur atar (65 kare), sonra aynı hızda dönmeye devam eder (içerik sonunda donar).
- c18: `genel gerçek` (Caveat sarı) + iki yönlü ok (dün de, yarın da) + sarı tik (geniş zaman alır).
- c19: `The Moon` halka; alt satır `it → complete|s (+s)` (ek_ayir: `s` kayar, sarı kutu).

## Olay ↔ sözcük t0 (küresel sn; yerel kare = (t − 70,08) × 30)
| Olay | Küresel sn | Sözcük (t0) | Sapma |
|---|---|---|---|
| daire 3 | 70,70 | Üçüncü (70,63) | 0,07 |
| cümle başı | 72,22 | The (72,22) | 0 |
| completes halka | 72,75 | completes (72,70) | 0,05 |
| 27 days halka | 74,90 | twenty (74,86) | 0,04 |
| Ay çizilir | 76,77 | Ay, (76,77) | 0 |
| Dünya | 77,49 | Dünya (77,49) | 0 |
| yörünge | 77,89 | çevresindeki (77,89) | 0 |
| Ay turu başlar | 78,53 | turunu (78,53) | 0 |
| genel gerçek | 81,56 | genel (81,56) | 0 |
| iki yönlü ok | 83,10 | böyleydi (83,12) | 0,02 |
| tik | 88,36 | alır. (88,36) | 0 |
| The Moon halka | 90,04 | the (90,04) | 0 |
| it | 91,90 | it. (91,90) | 0 |
| complete (+ s 94,75) | 93,68 | completes. (93,68) | 0 |
| (+s) | 95,93 | se (95,93) | 0 |

## Kanıt
- `ONIZLE_YALNIZ=1 bash calistir.sh --tema acik|koyu|acik` → "önizleme hazır" (son AÇIK). `node --check sahne.js` temiz.
- Taklit koşu (Node, sahte DOM, ölçü = 0,55 em tahmini): 809 kare hatasız; 24 olay (kare 19–776). Çakışma yalnız halka-sözcük (beklenen) ve karaoke altçizgisi; taşan 0. Dünya/yörünge/Ay tek `cizim` kutusu (x 1309–1831, y 261–539). Ay açısı `min(f, 797)`: son 12 kare durgun.

## Sapma / dikkat
- Taslak "sun + yörünge elipsi" diyor; cümle Ay'ın DÜNYA çevresindeki turunu anlattığı için merkeze Dünya çizildi (Güneş yok). Şef karar verir.
- `sahne-ortak.js` kopyası: `cumle` sayı ya da dizi.

## Kare yolları
`k/` boş (EK). calistir.sh denetim kareleri: 74,5 / 82,0 / 94,5 sn + son durgun kare.

## QA 13.11
- Kapı: "çakışma yok (108 örnek, 2551 kutu)".
- Kareler: k/05-canvas-ornek3-74.5, -80, -88.5, -95.5 (açık) · -82 (koyu).
- Göz: kök cümle, halkalar, "27" tek sözcük, çeviri, Dünya + yörünge + Ay (Ay turu ilerliyor), genel gerçek + ok + tik, ek_ayir (complete|s) doğru; koyu tema doğru. Taşma yok.
- Düzeltme: yok.
- Kalan: (1) taslak "sun + yörünge" diyor, sahnede Dünya var (RAPOR notu; şef karar). (2) 95,5 sn karesinde `The Moon` halkasının üstü "3" dairesine çok yakın (değmiyor). (3) Dünya içindeki kıta çizgileri küçük/soluk, kabul.
- QA 13.11 (2. tur, sunucu): "3" dairesi sarı. Çizim kararı: ses metni ve altyazı "Ay, Dünya çevresindeki turunu…" (senaryo.json c17) → Dünya + yörünge + Ay doğru, Güneş EKLENMEDİ; taslak "sun" notu bayat. Kapı: çakışma yok (108 örnek, 2551 kutu). Kareler k/05-…-74.5, -88.5, -95.5, k/koyu -82: temiz.

- Halka kuralı: DEĞİŞTİ: completes, `27 days` (days 75,58 sonrası), `The Moon` (Moon, 90,28 sonrası) → altçizgi. BIRAKILDI: sayı dairesi "3"; Dünya/Ay çizimi (halka değil). Kapı: çakışma yok (108 örnek, 2542 kutu); kare k/…-76.3, -91.

- zaman eşitleme 13.11: KARE 809→812, ICERIK 797→800, TBAS 70.08→69.66. 25 sabit zaman eşlendi (−0,42/−0,34, cümle 19 başı −0,50). Kapı temiz (108 örnek, 2546 kutu); kareler k/…-72.1…88.5.
