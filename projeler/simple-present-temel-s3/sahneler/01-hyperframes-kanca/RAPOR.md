# Sahne 01 · kanca (huni v2; HyperFrames DİKEY 1080×1920, 129 kare, 0,00–3,89 sn + 12 kare geçiş payı)

| Ölçüm | Değer |
|---|---|
| Durum | yazıldı (istem D-01, 15.11.2026, srv21). Önizleme hazırlığı `ONIZLE_YALNIZ=1`. mp4 yok, commit yok |
| Tema | açık (koyu kareyle de denetlendi) |
| qa-yerel (son koşu) | çıkış 0 · `01-hyperframes-kanca \| çakışma yok (17 örnek, 876 kutu)` |
| Çakışma kapısı (ayrı koşu) | çıkış 0 · 0 uyarı |
| Metin taraması (`tam ders\|dakika`) | boş (grep çıkış 1) |
| Kanal katmanı | 6 karede (0 · 0,9 · 1,95 · 3,5 · 3,8 açık, 1,95 koyu) aynı piksel: logo görünür sol kenar x 60–61, y 298–335; yazı y 296–339, sağ uç x 596 |
| Boş bantlar | 0–280, 1570–1920, x 961–1080: kenar pikseli 0 (6 kare + iki kapak) |
| Kapak A | `kapak-a.png` = `kapak.png` (md5 `397006b4…`, `cmp` aynı), `k/koyu/kapak-a-koyu.png` (`f6e8ef9c…`); 1080×1920; t 0,90; altyazısız |

Kod yolu: şef `SPEC.md` yazdı → agy (rol `kod`) `uret.py` yazdı → şef baştan sona okudu, koşturdu, kapıya soktu.
Kopya (emsal `02-04-ydt-temel-s1/sahneler/01-hyperframes-kapak/`): `yardim.py` (yalnız docstring + `KONU = "Simple Present"`; kullanılmayan
`KONU_PARCA` çıktı), `olay.py` (olay listesi), `calistir.sh` (`KARE=129`, karakter kopyası satırı, denetim kareleri, yorumlar).
Şef Edit'leri (`uret.py`): kart kalem kenarı `pilMetin` + açık dolgu `#fffdf8` (S1 kaydet kalıbı, sözleşme 15.11); `#root.tema-acik` assert;
karakter üstü aramalı (`karakter_ustu()`: 880'den 2 px adım, kart ve `?` kutusuna 26 px pay; sonuç 902); çıkış örneklemesinde başlık ve `?`
opaklığı kendi sönme süresiyle (0,15 sn; agy kartın 0,50 sn'sini kullanmıştı). `zamanlar.json` `karakter_cik` 0,45 → 0,40.

## İçerik
İlk kare = kapak: kanal katmanı, künye (`Simple Present` Fredoka 34 + `YDT · BASIC`), başlık `BU CÜMLE` (B = 133, kontur 10) / `YANLIŞ` sarı hapta
(x 259–761, y 648–792), kart `He doesn't goes.` (Fredoka 700 80, kâğıt kart x 60–737, y 840–1000, yazı x 100 taban 948), karakter
(`ortak/kapak/karakter.png`, ölçek 0,3057, alfa x 767–949, y 902–1215, el ucu ≈ (767, 1092), sola karta işaret eder) + sarı daire (cx 858,5,
cy 1018,5, r 99,5) + 10 px krem çıkartma kenarı. Hap çerçevesi 0,30–0,80 kalemle (mürekkep 5 px, hap kenarı üstünde, 36 px el taşması).
Çıkışta başlık söner, karakter sağa kayıp söner, kart y 480–640'a kayar (sahne 02 kare 0; `devir.json`).

## Olay listesi (küresel sn = yerel sn)
| Olay | Kare / sn | Cümle sözcüğü |
|---|---|---|
| kapak tam görünür (kanal, künye, başlık, hap, kart, karakter, daire) | 0 / 0,00 | söz öncesi |
| `YANLIŞ` hap çerçevesi kalemle (`cizgi`) | 9–24 / 0,30–0,80 | söz öncesi |
| KAPAK A karesi | 27 / 0,90 | — |
| kart karaoke `He` · `doesn't` · `goes.` (sarı altçizgi) | 30–35 · 40–49 · 52–73 / 1,00–1,16 · 1,32–1,64 · 1,72–2,44 | He · doesn't · goes. |
| altyazı `Hata` açılır · karaoke | 79 · 81–90 / 2,64 · 2,69–3,01 | Hata |
| kırmızı `?` kanca + nokta (`cizgi`) | 81–94 / 2,69–3,13 | Hata (2,69) |
| altyazı `nerede?` açılır · karaoke | 91 · 93–117 / 3,04 · 3,09–3,89 | nerede? |
| başlık ve `?` söner (`parilti` kare 102) | 102–106 / 3,39–3,54 | nerede? sonu − 0,50 |
| kart y 840 → 480 (`power3.inOut`; `tik` kare 116) | 102–117 / 3,39–3,89 | — |
| karakter + daire sağa kayar, söner (`power2.in`) | 102–114 / 3,39–3,79 | — |
| altyazı kapanır | 127 / 4,24 | — |
| durgun; son 12 kare geçiş altında | 117–128 / 3,89–4,30 | → sahne 02 |

`olaylar.json`: 4 olay (9 `cizgi`, 81 `cizgi`, 102 `parilti`, 116 `tik`), hepsi kare < 117. `uret.py` 8 denetim maddesini assert eder.

## Kapı çıktısı (son koşu)
```
== HAZIRLA → olay 4 · önizleme hazır
== KAPI
01-hyperframes-kanca | çakışma yok (17 örnek, 876 kutu)
== KARE (açık) 0 · 1.95 · 3.8   == KARE (koyu) 1.95
kapı çıkış kodu: 0
== ÇAKIŞMA KAPISI (ayrı): 01-hyperframes-kanca | çakışma yok (17 örnek, 876 kutu) · çıkış 0
```
Komutlar: `bash araclar/qa-yerel.sh simple-present-temel-s3 01-hyperframes-kanca 0.00,1.95,3.80 1.95 --hazirla` ·
`node araclar/cakisma-kapisi.mjs simple-present-temel-s3 --sahne 01-hyperframes-kanca --port 41333 --sunucu 41022`.

## Bakılan kareler ve bulgu
| Tur | Kare | Bulgu | Düzeltme |
|---|---|---|---|
| 0 (uret.py) | — | assert: karakter saçı `?` kutusuna 13 px (krem kenarla 3 px); assert: çıkış örneklemesi opaklığı yanlış süreyle | karakter üstü aramalı (902); sönme süreleri düzeldi |
| 1 | k/0, k/1.95, k/3.8, k/koyu/1.95, k/ara/0.9, 2.9, 3.2, 3.5, 3.65, 3.75, k/ara/koyu/2.9, 3.5 (kontak `k/ara/kontak-acik.png`) | 3,80'de sağ kenarda (x ≈ 1077) soluk sarı daire: GSAP `power2.in` kübik (p³), karakter 3,84'e dek görünür | `karakter_cik` 0,40 (3,79'da biter); 3,80 sağ bantta sarı piksel 0 |
| 2 | k/0, k/1.95, k/3.8, k/koyu/1.95 (yeniden) | taşma, kesik yazı, üst üste binme, okunmaz kontrast, boş kare YOK; `?` kartın sağ üst köşesinde, kenar çizgisinin üstünden geçer, okunur | — |
| Kapak A | `proje-ka/k/ka-acik/at-0.9s.png`, `proje-ka-koyu/k/ka-koyu/at-0.9s.png` | altyazı, karaoke, `?` yok; kanal, künye, başlık, çizili hap, kart, karakter; iki temada okunur | — |

Kapak A yöntemi (S1-KAPAK-A): `ONIZLE_YALNIZ=1 bash calistir.sh --tema <t>` → `cp -a proje/. <kopya>/` (koyu `proje-ka-koyu`, açık `proje-ka`)
→ kopyada ilk `</style>` önüne `#altyazi{display:none}` → `hyperframes snapshot . --at 0.9 --no-end --keep -o <kopya>/k/ka-<t>` (koyu önce,
açık sonra; `proje/` açık kalır). Koyu kopyada logo `yds-publishing-seffaf.svg` (md5 `33189e5b`), açıkta `lacivert` (`316d8df3`).

## agy koşu özeti
| Şerit | Dosya | Süre | Özet |
|---|---|---|---|
| tek | `uret.py` (SPEC §1–§8) | 488 sn | `~/.claude/canavar/agy-filo/20261115-192815` |
Rol `kod` (gemini-3.8-flash-high). "değişen" listesindeki başka dosyalar aynı worktree'deki paralel oturumların işidir; ajan yalnız `uret.py` yazdı.

## Sahne 02 devri (`devir.json`)
Kart x 60, y 480, w 677,04, h 160, rx 18, kenar 4 `pilMetin`, dolgu koyu `#fff9e6` / açık `#fffdf8`; yazı Fredoka 700 80, `font-kerning:none`,
x 100, taban 588, renk `pilMetin`; sözcük x: `He` 100–194,8 · `doesn't` 213,6–477,0 · `goes.` 495,8–681,1 · `does` 213,6–381,9 · `go` 495,8–584,1 ·
`es` 584,1–663,4; t 3,89.

## Açık noktalar
1. **Karakter küçük.** Kart 677 px (Fredoka 80 yazı 581 + pay 96); istemin "kartın sağı + 20 … 960" alanı 203 px. Karakter 182×313 px (istem
   ≈ 500 px yükseklik bekliyordu); içerik bandının alt kısmı (y ≈ 1220–1380) ve kartın altı boş. Büyütme yolu: kart payı ya da kart boyu (istem kartı
   sabitler) ya da karakterin kartın altına taşması (istem dışı). Şef/Nadir kararı.
2. **Başlık boyu bant sınırlı.** Genişlik sınırı B ≈ 185 verirdi; başlık bandı 468–796 (istem "y ≈ 470–800", kart 840) B = 133'e indirdi.
3. **Hap yazısı konturu yok.** İstem iki satıra zemin konturu yazar; emsal S1/S2 hap yazısı (`bas2t`) kontursuzdur; emsal izlendi (hap zemini ayırır).
4. **Daire iki temada sarı** (`#fece00`, istem ve BRIEF-S3); `kapak-standardi.md` krem daire der (sarı zeminli ana kapak için).
5. **Sahne 02 eşleşmesi.** D-02 kartın yalnız x 60, y 480–640, Fredoka 80 değerini yazar; yazı x, kart genişliği ve renkler `devir.json`'da.
   Sahne 02 başka değer kullanırsa geçişte kart sıçrar.
6. HF kutu adları grup adıdır (`kart-g:*`, `baslik:*`, `soru:*`); karakter ve daire `#sahne` dışında, kapı ölçmez (denetim uret.py maskesiyle).
