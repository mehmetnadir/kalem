# Sahne 01 · kapak (HyperFrames DİKEY 1080×1920, 102 kare, 0,00–3,00 sn + 12 kare geçiş payı)

Durum: yazıldı (istem D-S3, 15.11.2026, srv21). Önizleme hazırlığı `ONIZLE_YALNIZ=1` ile koştu. Render yok, `kapak-a.png` / `kapak.png` yok,
commit yok. Tema: acik (koyu kareyle de denetlendi).

Kod yolu: şef `SPEC.md` yazdı → agy tek şerit `uret.py` yazdı → şef baştan sona okudu, kapıya soktu, 1 küçük düzeltmeyi Edit ile yaptı
(≠ eğik çizgisi). `calistir.sh`, `yardim.py`, `olay.py`, `cizim/ogretmen.json` S1 sahne 01'den kopyalandı ve küçük Edit'le uyarlandı;
`zamanlar.json`, `nesneler.json`, `cizim/KAYNAK.md` şefin.

## İçerik
İlk kare = kapak A: logo HUD sol üst, rozet `YDT · BASIC`, başlık `TARİFE` (B = 190 px: üst sınır; 952 px sınırı 280 / 264 px verirdi) /
`≠ PLAN` sarı hapta (hap 689 px; `≠` Fredoka'da yok → hap içinde 3 kalem çizgisi, `pilMetin`). Solda tren + saat (kollar yedide, rakamsız),
etiket `leaves`; sağda elinde sinema bileti tutan öğretmen figürü (`kadro.ogretmen`), etiket `am going` (Caveat 72). Çizimler ana ders
sahne 05 geometrisi (`trenParcalari`, `saatParcalari`, `biletParcalari`; kalem biçimi `kalem-canvas.js` `hash/gurul/kutu/elips` Python'a
taşındı). Kart 1 satırları Fredoka 700 64, sözcük zamanlı. 2,00–2,85 uçuş: başlıklar ders adına küçülüp solar, rozet sağa kayar, sahne
grubu solar, tren küçülüp kart 1 sağ üst köşesine iner, iki satır kart içine çıkar; 2,62–2,90 kart çerçevesi kalemle çizilir.

## Olay listesi (küresel sn = yerel sn)
| Olay | Kare / sn | Cümle sözcüğü |
|---|---|---|
| kapak tam görünür (logo, rozet x 48, `TARİFE`, hap `≠ PLAN`, tren, saat, bilet tutan figür, etiketler) | 0 / 0,00 | söz öncesi |
| `TARİFE` altına sarı el altçizgisi (`cizgi`) | 9–24 / 0,30–0,80 | söz öncesi |
| altyazı dilimi (cümle 1, ekran metni, tek satır) | 29 / 0,95 → sahne sonu | The t0 − 0,05 |
| satır 1 `The` · `train` · `to` · `İzmir` kırpmayla (`hisirti` 30, 49) | 30–35 · 38–42 · 44–47 · 49–58 / 1,00–1,92 | The 1,00 · train 1,28 · to 1,48 · Izmir 1,64 |
| KAPAK A KARESİ (çip yok, ders adı yok, satır 1 tam, altçizgi tam) | 59 / 1,97 | — |
| rozet sağa kayar · sahne grubu solar | 60–72 / 2,00–2,40 | — |
| uçuş: başlıklar → ders adı, tren → kart köşesi, satırlar yukarı (`parilti` 60) | 60–85 / 2,00–2,85 | — |
| satır 2 `leaves` · `at` · `7` (`hisirti` 66) | 66–73 · 77–80 · 84–88 / 2,20–2,92 | leaves 2,20 · at 2,56 · seven 2,80 |
| başlıklar solar · ders adı açılır · çip `Hook` (`tik` 85) | 75–85 / 2,49–2,85 | — |
| kart 1 çerçevesi 4 kenar sırayla (`cizgi` 79) | 79–87 / 2,62–2,90 | — |
| durgun; son 12 kare geçiş altında | 88–101 / 2,92–3,40 | `p.m.` 3,00 → sahne 02 |

`olaylar.json`: 7 olay (kare 9, 30, 49, 60, 66, 79, 85), hepsi < 90. `uret.py` 7 denetim maddesini assert eder (tren dahil uçuş çakışma örneklemesi).

## Kapı sonucu (son koşu, tur 2)
```
== HAZIRLA → olay 7 · önizleme hazır
== KAPI
01-hyperframes-kapak | çakışma yok (13 örnek, 5329 kutu)
== KARE (açık)  0.2 · 1.97 · 2.95
== KARE (koyu)  1.97
kapı çıkış kodu: 0
```
Komut: `bash araclar/qa-yerel.sh 02-04-ydt-temel-s3 01-hyperframes-kapak 0.2,1.97,2.95 1.97 --hazirla` (tur 1 de çıkış 0, 5338 kutu).

## Bakılan kareler ve bulgu
| Tur | Kare | Bulgu | Düzeltme |
|---|---|---|---|
| 1 | k/1.97, k/koyu/1.97 | `≠` eğik çizgisinin alt ucu hapın sol alt kavisinden taşıyor | eğik uçları (0,322; 0,555) → (0,150; −0,005) em; kavise ≥ 11 px (uret.py satır 590, SPEC §3.4) |
| son | k/0.2, k/1.97, k/2.95, k/koyu/1.97, k/ara/0.55, 1.5, 2.2, 2.45, 2.62, 2.75, k/ara/koyu/2.45, 2.62 | taşma, kesik yazı, üst üste binme, okunmaz kontrast, boş kare YOK; platform bandı boş; altyazı bandında tek satır; 1,97'de satır 1 tam, çip ve ders adı yok; 2,95'te kart çerçevesi, `leaves at 7`, tren köşede, HUD tam. 1,5 / 2,62'de sözcük yazım ortasında (beklenen) | — |

## agy koşu özeti
| Şerit | Dosya | Süre | Özet |
|---|---|---|---|
| tek | `uret.py` (SPEC §3, 847 satır) | 306 sn | `~/.claude/canavar/agy-filo/20261115-125109` |
Rol `kod` (gemini-3.8-flash-high). agy-filo "değişen" listesinde S2 paketinin dosyaları göründü: aynı worktree'deki paralel oturum; ajan yalnız
`uret.py` yazdı (mtime ile doğrulandı). Şef Edit düzeltmesi: `uret.py` ≠ eğik çizgisi (1 satır).

## Sahne 02 devri (`devir.json`)
Fredoka 700 64, `font-kerning:none`, x 97, taban [468, 566]; tam satırlar `The train to İzmir` / `leaves at 7 pm today.`, görünen
`leaves at 7`; 9 sözcüğün x aralığı (`pm` 428,8–514,1 · `today.` 529,1–714,3). Kart çerçevesi `kutu(57, 368, 966, 260, tohum 71)`, çizgi 4.
Tren kutusu [785, 392, 1000, 483] (ölçek 0,5, iç grup `translate(58 1226)`, çizgi `non-scaling-stroke`). Altyazı ekran dönüşümü
`altyazi_ekran` = {Izmir → İzmir, seven p.m. → 7 pm}: sahne 02 aynı dilimi aynı metinle göstermeli (3,00 sınırında metin değişmesin).

## Açık noktalar
1. Altyazı: `ortak/anlatim/altyazi.json` ses metnini yazar (`Izmir`, `seven p.m.`). İstem "ekranda İzmir noktalı, `7 pm`" der; sahne kendi
   kopyasında dönüştürdü (`EKRAN`). Ortak dosya düzeltmesi ya da sahne 02'nin aynı dönüşümü şefte (yazma kapsamı dışı).
2. Logo: BRIEF-S3 "Kapak A" ve `kapak-taslak.md` "logo sol alt y ≈ 1478" der; BRIEF-DIKEY §0 (Nadir bulgusu) "alt bantta logo yok, HUD sol
   üst 96 px" der. HUD sol üst uygulandı (S1 ile aynı). BRIEF satırının düzeltilmesi şefte.
3. Saat akrebi mürekkep (ana ders sahne 05'te sarı): kapakta sarı altçizgi + hap + rozet zaten var; tek vurgu kuralı için.
4. `kapak-taslak.md` "başı trene dönük": kit figürü önden bakar; baş dönmedi (S1 açık nokta 4 ile aynı).
5. Son hal (2,85–3,00) içerik bandının alt yarısı boş; kart 2 ve zaman çizgisi sahne 02'de. BRIEF-DIKEY §0 "%85 dolu" bu 0,15 sn'de tutmaz.
6. Kart çerçevesi sahne 01'de çizildi (BRIEF-DIKEY §3 kart: 4 px kalem çizgisi, iç boşluk 40, genişlik 984 → x 57, taşma payıyla 48–1032).
   Sahne 02 kare 0 bu çerçeveyi `devir.json`'dan aynı tohumla çizmeli.
7. mp4 render ve `kapak-a.png` / `kapak.png` yok (istem gereği); `calistir.sh` render dalı kare 59'u paket köküne `kapak-a.png` yazar ve
   `kapak.png` olarak kopyalar.
