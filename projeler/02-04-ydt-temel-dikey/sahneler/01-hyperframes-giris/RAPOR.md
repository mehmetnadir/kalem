# Sahne 01 · giriş DİKEY (HyperFrames 1080×1920, 102 kare, 0,00–3,00 sn + 12 kare geçiş payı)

Durum: istem D-dikey (15.11.2026, srv21). Önizleme hazırlığı `ONIZLE_YALNIZ=1` ile koştu. Render yok, commit yok.
Tema: koyu

| Kapı | Sonuç |
|---|---|
| `qa-yerel.sh` çıkış kodu | 0 |
| Çakışma kapısı | çakışma yok (13 örnek, 88 kutu) |
| Kare bakışı (açık 3 + koyu 1 + ara 8 + telefon 4) | taşma, kesik yazı, binme, okunmaz kontrast, boş kare, platform bandında öğe YOK |
| Düzeltme turu | 0 (kod QA'dan önce şef okumasıyla 1 sadeleştirme) |

## Olay listesi (cümle 1; küresel sn = yerel sn)

| # | Olay | sn (kare) | Cümle sözcüğü (t0) | Ses olayı |
|---|---|---|---|---|
| 1 | logo damgası bant ortasında (774×192, x 153, y 776), opaklık + ölçek 1,18→1 + dönme −2→0 | 0,00–0,40 (0–12) | söz öncesi | `vurus` k2 |
| 2 | logo HUD sol üste uçar → 48, 48, 387×96 (kunye.js ile birebir) | 0,50–0,95 (15–29) | söz öncesi | `parilti` k15 |
| 3 | çip `Hook` açılır (sağ üst, y 48, h 80, Lexend 700 40, vurgu çerçeve 4 px) | 0,70–0,95 (21–29) | söz öncesi | `tik` k28 |
| 4 | altyazı cümle 1 (tek dilim, 2 satır, Lexend 500 44) | 0,95 → sahne sonu | İstanbul'da − 0,05 | — |
| 5 | `kinetik_baslik` `İstanbul'da` (x 96, taban 560, Fredoka 700 128) | 1,00 (30) | İstanbul'da (1,00) | `tik` k30 |
| 6 | `kinetik_baslik` `yaşıyorum.` bitişik (taban 740) | 1,64 (49) | yaşıyorum. (1,64) | `tik` k49 |
| 7 | `ek_ayir`: *yor* sarı kutuyla kayar | 1,94–2,30 (58–69) | "yor" hecesi | `cizgi` k58 |
| 8 | *yor* yazısı tek karede `pilMetin` | 2,14 (64) | — | — |
| 9 | tireler → `yaşı-yor-um.` | 2,22–2,37 (67–71) | — | — |
| 10 | `kinetik_baslik` `Amcamla` (taban 960) | 2,52–2,74 (76–82) | Amcamla (2,52) | `tik` k76 |
| 11 | durgun; son 12 kare geçiş altında | 2,74–3,40 (82–101) | 2. yaşıyorum 3,08 → sahne 02 | — |

`olaylar.json`: 7 ses olayı, hepsi kare < 90. `Y.kontrol(ilk=False)`: hareket en geç 2,74 sn.

## Kapı sonucu (son koşu)
```
== KAPI
01-hyperframes-giris | çakışma yok (13 örnek, 88 kutu)
== KARE (açık)  0.98 · 2.45 · 2.95
== KARE (koyu)  2.95
kapı çıkış kodu: 0
```
Komut: `cd K && bash araclar/qa-yerel.sh 02-04-ydt-temel-dikey 01-hyperframes-giris 0.98,2.45,2.95 2.95 --hazirla`
(0,98 = logo + çip bitti · 2,45 = ek_ayir + tireler bitti · 2,95 = Amcamla bitti, son düzen).

## Bakılan kareler ve bulgu

| Kare | Bulgu |
|---|---|
| `k/01-hyperframes-giris-0.98.png` | HUD logo + çip `Hook` yerinde; içerik bandı boş (ilk söz 1,00); altyazı 2 satır, sağ uç ≈ 1022 ≤ 1032 |
| `k/01-hyperframes-giris-2.45.png` | `yaşı-yor-um.` sağ uç 892; tire ↔ kutu arası 10 px; *y* kuyruğu kutu içinde (kutu 658–786) |
| `k/01-hyperframes-giris-2.95.png` | son düzen: 3 satır + boş 4. yuva; çakışma yok |
| `k/koyu/01-hyperframes-giris-2.95.png` | koyu: kutu `#f2a93b`, *yor* `pilMetin` koyu, tireler `ikincil`; okunur |
| `k/ara/` 0,2 · 0,75 · 2,05 · 2,2 · 3,3 (açık), 0,2 · 2,05 · 2,2 (koyu); kontak `k/ara/kontak-ara.png` | damga bant ortasında; uçuşta logo ↔ çip binmesi yok; kutu büyürken renk geçişi tek karede |
| `k/telefon-png.png` (360×640, 4 kare) | telefon ölçeğinde HUD, satırlar ve altyazı okunur |

## Sahne 02 devri (uret.py `devir:` satırı)
```
sol 96 · taban [560, 740, 960, 1140] · boy 128 (Fredoka 700) · "yaşı" x 96
yor kutusu x 391,68 y 658,08 w 236,29 h 128 rx 14 · tire x [329,86, 638,21] (ikincil) · satır 2 sağ uç 891,9
```
Kare 101 = kare 82 düzeni (durgun). Sahne 02 kare 0 bu düzenden başlar; 4. satır (taban 1140) ve 2. *yor* kutusu sahne 02'de.

## Kod yolu
- Şef: `SPEC.md` yazdı; yatay `olay.py`, `yardim.py`, `calistir.sh` kopyalandı. `calistir.sh` Edit ile uyarlandı (başlık, kontrol 360 px,
  telefon kontak satırı; `ONIZLE_YALNIZ`, `yuk1`, koşullu Homebrew PATH yatay kalıptan geliyor).
- agy (`agy-filo tek --rol kod`, gemini-3.8-flash-high, 220 sn, başarılı): `yardim.py` dikeye çevrildi (W/H, `u()`, çip-yalnız `kunye_svg`,
  `altyazi_svg`, `altyazi_dilimleri`, dikey zemin), `uret.py` yazıldı. Özet: `/home/sef/.claude/canavar/agy-filo/20261115-115443`.
- Şef okuması: SPEC'e uyuyor. Tek düzeltme Edit ile: `altyazi_svg` istenmeyen tuple/dize girişini kabul ediyordu → dikey örnekteki dict kalıbı.

## Açık noktalar
1. **Alt bant boşluğu.** Sahne sonunda içerik 438–970 arası dolu; 1000–1392 boş. BRIEF §3 satır 1 4. yuvayı boş ister (sahne 02 çizer).
   BRIEF §2.10 "%85 dolu" kuralı bu 3 sn'lik sahnede uygulanmaz. 0,40–1,00 arası bant da boş (soğuk açılış, logo uçuşu).
2. **Altyazı boyu 44.** İstem "yazı tabanı ≥ 50" der; BRIEF §2 ve `ortak/kunye.js` altyazıyı 44 yazar. Öteki 13 sahneyle tutarlılık için BRIEF izlendi.
3. **Altyazı ve karaoke.** Cümle 1 iki satıra sığdığı için tek dilim: tam cümle 0,95'ten görünür; "Türkçede ikisi de yaşıyorum." 3,96'da
   (sahne 02) söylenir. Bu, `kunye.js` `altyaziMetin` kuralıyla aynıdır. Altyazı bandında karaoke yok: `altyaziCiz` karaoke çizmez; bu sahnede
   sözcükler söylendiği anda kinetik gelir. İstem "karaoke alt bantta" der; bant karaokesi gerekirse 14 sahnede birlikte karar ister.
4. Koyu temada 1,94–2,14 (6 kare) krem *yor* büyüyen turuncu kutunun üstündedir; BRIEF 2,14 tek kare değişimini ister (yatayla aynı).
5. Ders adı ve rozet bu sahnede yok (BRIEF §2.2); sahne 02 15,98'de indirir.
6. `uret.py` / `olay.py` `-I` olmadan koşar: fontTools kullanıcı site-packages içinde (yatay RAPOR not 7 ile aynı).
7. agy-filo "değişen" listesi `sahneler/04-canvas-ornek2/` dosyalarını da gösterdi: başka oturumun eşzamanlı işi; bu sahne o dosyalara dokunmadı.
8. `nesneler.json` / `zamanlar.json` yok: yatay 02-04 kalıbı izlendi (zaman `zaman.json` + `sozcukler.json` tek kaynak); dikey örnekteki
   `nesneler.json` boş ve hiçbir araç okumuyor.
9. Render kısmı (`calistir.sh` sonu, telefon kontağı) koşmadı: istem render yasaklar.
10. `.claude/docs/sozlesme.md` yazılmadı: istem yalnız sahne dizinine yazmaya izin verir.

Dosyalar: `SPEC.md`, `uret.py`, `yardim.py`, `olay.py`, `calistir.sh`, `proje/index.html`, `olaylar.json`, `k/`, `RAPOR.md`.
