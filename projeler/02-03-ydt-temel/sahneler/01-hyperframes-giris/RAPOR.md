# Sahne 01 · giriş (HyperFrames, 102 kare, 0,00–3,00 sn + 12 kare geçiş payı)

Durum: P2 yazıldı, canlı önizleme hazırlığı koşuldu (`ONIZLE_YALNIZ=1`, açık tema son koşu). Render yok. Kapı ve `sahne-kare` koşulmadı (şef EK 13.11 12:40); `k/` boş.
Tema: acik.

## İçerik
Soğuk açılış kapağı (K23): logo damgası 0,00 sn, rozetler `YDT · BASIC` / `GRAMMAR`, iki satır başlık `ONE VERB` / `TWO TENSES` (sarı: VERB, TENSES), sağda kalemle iki kart `goes` ve `is going`, 2,50–3,00 sn başlık ve logo künyeye uçar, künye (Hook, ajanda Hook · Examples · Rule · Trap) açılır. İlk söz 1,00 sn. Son 12 kare durgun (hareket 3,00 sn'de biter; kontrol uret.py içinde).

## Olay ↔ sözcük (cümle 1, küresel sn = yerel sn)
| Olay | Sözcük | Sözcük t0 | Olay sn | Sapma |
|---|---|---|---|---|
| `ONE` başlığı | Aynı | 1,00 | 1,00 | 0,00 |
| `VERB` (sarı) + `goes` kartı yazısı | fiil, | 1,40 | 1,40 | 0,00 |
| `TWO` başlığı + `is going` kartı yazısı | iki | 2,04 | 2,04 | 0,00 |
| `TENSES` (sarı) + `is going` sarı belirteç | zaman. | 2,28 | 2,28 | 0,00 |
| Başlık + logo künyeye uçuş | (cümle 1 sonu öncesi, sahne sonu) | — | 2,50–3,00 | süs |
| Rozetler, logo damgası, iki kart çerçevesi | (soğuk açılış süsü, söz öncesi) | — | 0,00–1,45 | süs |

## Kapı
Koşulmadı (EK). Yerinde kontroller: `Y.kontrol` (hareket en geç 3,00 sn) geçti · başlık ile kart arası ≥ 40 px (assert) · olay.py 14 olay.

## Açık notlar
- `SIGNAL WORD` sarı belirteci bu sahnede YOK: "sinyal" 3,72 sn'de söylenir (sahne 02). Söylenmeden gelmesin diye eklemedim; sahne 02 sahibi çizsin.
- `goes` / `is going` kartları 3,00 sn'de söner; sahne 02 kendi kartlarını yeniden çizer (BRIEF sahne 02 satırı).
- Künye: `ortak/kunye.js` KUNYE değerleri (ders `PRESENT CONTINUOUS vs SIMPLE PRESENT`, seviye `YDT BASIC`, ajanda Hook · Examples · Rule · Trap) aynen.

Dosyalar: `uret.py`, `olay.py`, `calistir.sh`, `yardim.py`, `proje/index.html`, `olaylar.json`.
Kare yolları: yok (EK).

## QA 13.11
- Kapı: "ölçülmedi (HyperFrames)" (kapı HyperFrames'i ölçmez). Kareler: `k/01-hyperframes-giris-{1.1,1.5,2.1,2.8}.png`, koyu `kk/01-hyperframes-giris-2.4.png`.
- Göz: başlık/kart yerleşimi, rozet, logo, künye ajandası (Hook · Examples · Rule · Trap) doğru; koyu tema renkleri doğru. Düzeltme yok. Kalan sorun yok.
