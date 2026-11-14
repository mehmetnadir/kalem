# Sahne 01 · giriş (HyperFrames, 102 kare, 0,00–3,00 sn + 12 kare geçiş payı)

Durum: P2 yazıldı (istem D, 14.11.2026, srv21). Önizleme hazırlığı `ONIZLE_YALNIZ=1` ile koştu. Render yok, commit yok.
Tema: acik

## İçerik (BRIEF §3 No 1)
Soğuk açılış (K23). Logo damgası 0,00 sn ortada, 0,50–0,95 künye köşesine uçar. Bölüm (`Hook`) ve ajanda 0,70–0,95 açılır.
İlk söz 1,00 sn, geri sayım yok. İki Türkçe satır sözcük sözcük vurur (`kinetik_baslik`, `back.out(1.6)`, 0,22 sn).
"yaşıyorum" söylenirken `ek_ayir`: sözcük bitişik gelir, sonra *yor* sarı kutuyla kayar, tireler belirir → `yaşı-yor-um.`
Tek vurgu: `RENK["vurgu"]` (hf_tema ile açık `#ffe066` dolgu / koyu `#f2a93b`). Kırmızı, yeşil, emoji yok.
Yazı: Fredoka 700, 128 mantıksal px (`u()` oranı); en küçük içerik yazısı 128 px (künye ölçüleri `ortak/kunye.js` tablosu).

## Olay listesi (cümle 1; küresel sn = yerel sn)

| Olay | Kare / sn | Cümle sözcüğü (t0) |
|---|---|---|
| logo damgası (`vurus`) | 0–12 / 0,00–0,40 | söz öncesi süs |
| logo künyeye uçar (`parilti`) | 15–29 / 0,50–0,95 | söz öncesi süs |
| künye bölüm + ajanda açılır (`tik`) | 21–29 / 0,70–0,95 | söz öncesi süs |
| `kinetik_baslik` "İstanbul'da" | 30 / 1,00 | İstanbul'da (1,00) |
| `kinetik_baslik` "yaşıyorum." (bitişik) | 49 / 1,64 | yaşıyorum. (1,64) |
| `ek_ayir` *yor* kutuyla kayar (`cizgi`) | 58–69 / 1,94–2,30 | yaşıyorum. "yor" hecesi (~1,94) |
| *yor* yazısı zemin rengine döner | 64 / 2,14 | — (kutu %90 dolu) |
| tireler belirir | 67–71 / 2,22–2,37 | — |
| `kinetik_baslik` "Amcamla" | 76 / 2,52 | Amcamla (2,52) |
| durgun bekleme + geçiş payı | 82–101 / 2,74–3,40 | 2. "yaşıyorum" 3,08: sahne 02 |

olaylar.json: 7 ses olayı (vurus, parilti, tik×4, cizgi); hepsi kare 90'dan önce. `Y.kontrol`: hareket en geç 2,74 sn.

## Kapı sonucu (son koşu, tur 3)
```
== KAPI
01-hyperframes-giris | çakışma yok (13 örnek, 79 kutu)
== KARE (açık)  1.25 · 2.45 · 2.9
== KARE (koyu)  2.9
kapı çıkış kodu: 0
```
Komut: `bash araclar/qa-yerel.sh 02-04-ydt-temel 01-hyperframes-giris 1.25,2.45,2.9 2.9 --hazirla`

## Bakılan kareler ve bulgu

| Tur | Kare | Bulgu | Düzeltme |
|---|---|---|---|
| 1 | k/2.9 (açık, koyu) | tireler yor kutusunun kenarına değiyor | `TIRE_ARA` 0,08 em (≈10 px) boşluk |
| 2 | k/ara/2.05 | renk geçişi solarken *yor* yarı saydam görünüyor | soluma yerine 2,14 sn'de tek karede değişim |
| 3 | k/ara/koyu/2.1, 2.15 | sağ tire erken beliriyor, kayan "um." ile üst üste biniyor | tireler kayma %99 bitince (2,22) belirir |
| son | k/1.25, k/2.45, k/2.9, k/koyu/2.9, k/ara/0.2, 0.75, 2.25, k/ara/koyu/2.1, 2.2 | taşma, kesik yazı, üst üste binme, okunmaz kontrast, boş kare yok | — |

Kare yolları: `k/01-hyperframes-giris-{1.25,2.45,2.9}.png`, `k/koyu/01-hyperframes-giris-2.9.png`, ara kareler `k/ara/`.
Bayat kareler (tur 1–2) `~/Silinecekler/2026-11-14-0204/01-giris-*` altına taşındı, `LISTE.md` satırı yazıldı.

## Açık noktalar
1. **2. satır sahne 02'de biter.** "Amcamla" 2,52'de gelir. Arkasındaki "yaşıyorum" 3,08'de söylenir, sahne 3,00'te biter.
   Söylenmeden gelmesin diye bu sahnede yok. Sahne 02 (cümle 1 sonu) `yaşı-yor-um.` ve 2. *yor* kutusunu çizer.
   Devir ölçüleri: sol 120 · taban Y1 505 / Y2 685 · Fredoka 700 128 · "yaşı" x 788,2 · yor kutusu x 1083,8 w 236,3
   y 423,1 h 128 rx 14 · tire `ikincil`, kutu ile arası 10 px.
2. **Künye ders adı gizli.** Ders adı cümle 2'de söylenir; BRIEF No 2'ye göre başlık sahne 02'de künyeye uçar.
   Sahne 02 künyeyi ilk kareden tam çizerse ders adı geçişte (BookFlip) belirir. Karar sahne 02 sahibinde.
3. Koyu temada 1,94–2,14 sn (6 kare) krem *yor*, büyüyen turuncu kutunun üstündedir; sonra zemin rengine döner.
4. Rozetler (YDT · BASIC / GRAMMAR) yok: BRIEF satırında yok. 02-03 kapak kalıbından yalnız logo damgası alındı.
5. Yazma kapısı (`write-size-gate`, 15 satır) yeni dosya yazımını engelledi. İstem alt ajanı yasaklar.
   Örnek dosyalar kopyalandı, 15 satırdan kısa Edit parçalarıyla uyarlandı. Bypass bayrağı yazılmadı.
6. `qa-yerel.sh`, `~/qa-kare/<paket>/<sahne>/` klasörünün tamamını `k/` içine kopyalar. O klasörde tur 2'den kalma
   `2.35.png` durur; sonraki koşuda `k/` içine geri gelir (araç davranışı, sahne dışı).
7. `uret.py` / `olay.py` `-I` olmadan koşar: fontTools kullanıcı site-packages içinde (02-03 örneğiyle aynı).
8. `.claude/docs/sozlesme.md` yazılmadı: istem yalnız sahne dizinine yazmaya izin verir.

Dosyalar: `uret.py`, `olay.py`, `yardim.py` (02-03 kopyası; künye ders adı 02-04, `u()` eklendi), `calistir.sh`,
`proje/index.html`, `olaylar.json`, `RAPOR.md`.
