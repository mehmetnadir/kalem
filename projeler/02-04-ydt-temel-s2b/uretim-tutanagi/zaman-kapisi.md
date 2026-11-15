# Zaman kapısı (EK-12) — `02-04-ydt-temel-s2b` · DUZ4-0204S2 · 16.11.2026

| Ölçüm | Değer |
|---|---|
| Satır | 57 (kanca 0–4 sn: 10 · gövde: 47) |
| Fark < 0 (öğe sözden önce) | 10: kanca 3 · gövde 7 |
| Sınıf | kare yuvarlaması 6 · yazısız kart çerçevesi 2 · kanca istisnası 2 · **gerçek 0** |
| Gövdede fark < 0 (ham) | 02 Simple Present (-0.01); 02 kart 2 kutusu (-0.33); 02 tisort (-0.01); 02 today daire (-0.01); 02 today daire mürekkep (-0.01); 02 RIGHT NOW (-0.01); 02 Present Continuous (-0.02) |

Kaynak: sahne 01, 03, 08 `zamanlar.json` (olay zamanları; 08 `olay_listesi.kuresel`, 03 `t_bas` + yerel); sahne 02 çalışma anı
`not()` kaydı (`kalem-paper.js` ZAMAN dizisi, son karede `/log` gövdesi; `sahne-kare.mjs --png 0 --olc` ile yakalandı, kare → 2,84 + kare/30).
Sözcük t0: `ortak/anlatim/sozcukler.json`. Sahne 02 parça 3 (`She is wearing her pink T-shirt today.`) sözcükleri `sozcukler.json`'da yok;
t0 `sahne-02.js` EN2 çapasından (ElevenLabs hizalaması). Fark = giriş − t0; ⚠ = fark < 0.
Kapsam dışı: altyazı satırı (DK-1 ölçer; satır t0 − 0,05'te bütün sözcükleriyle açılır, karaoke sözcüğü t0'da işaretler) ve krom (kanal, künye).

## Kanca (0–4 sn)

| Sahne | Öğe | Giriş (sn) | Sözcük | t0 (sn) | Fark (sn) | Not |
|---|---|---|---|---|---|---|
| 01 | başlık GENEL / ŞU AN + kapak çizimi (kanca kartı) | 0.00 | Genel | 1.00 | ⚠ -1.00 | kanca istisnası: başlık ve kanca kartı |
| 01 | ≠ işareti | 0.30 | Genel | 1.00 | ⚠ -0.70 | kanca istisnası: başlık parçası |
| 01 | rozet kayması | 2.18 | — (krom) | — | — |  |
| 01 | sahne sola / başlık uçuşu | 2.24 | — (geçiş) | — | — |  |
| 01 | soru satırı `Genel mi, şu an mı?` (Caveat) | 2.42 | Genel | 1.00 | +1.42 |  |
| 01 | künye konu satırı | 2.62 | — (krom) | — | — |  |
| 02 | soru satırı (sahne 01'den sürer) | 2.84 | Genel | 1.00 | +1.84 |  |
| 02 | kart 1 kutusu | 3.24 | She | 3.39 | ⚠ -0.15 | yazısız kart çerçevesi; kart metni `She` ile açılır |
| 02 | kart 1 sözcükleri | 3.41 | She | 3.39 | +0.02 |  |
| 02 | kart 1 karaoke | 3.41 | She | 3.39 | +0.02 |  |

## Gövde (≥ 4 sn)

| Sahne | Öğe | Giriş (sn) | Sözcük | t0 (sn) | Fark (sn) | Not |
|---|---|---|---|---|---|---|
| 02 | mont | 4.27 | coat | 4.27 | +0.00 |  |
| 02 | odak in the winter | 4.47 | in | 4.47 | +0.00 |  |
| 02 | GENERAL | 5.57 | Genel | 5.56 | +0.01 |  |
| 02 | zaman-1 eksen | 6.04 | durum: | 6.04 | +0.00 |  |
| 02 | zaman-1 ok | 6.41 | durum: | 6.04 | +0.37 |  |
| 02 | now 1 nokta | 6.31 | durum: | 6.04 | +0.27 |  |
| 02 | now 1 metin | 6.44 | durum: | 6.04 | +0.40 |  |
| 02 | Simple Present | 6.67 | geniş | 6.68 | ⚠ -0.01 | kare yuvarlaması (< 1 kare, 0,033 sn; `fr()` en yakın kare) |
| 02 | kış bandı 1 | 7.01 | zaman. (1. geçiş) | 7.00 | +0.01 |  |
| 02 | kar tanesi 1 | 7.21 | zaman. (1. geçiş) | 7.00 | +0.21 |  |
| 02 | kış bandı 2 | 7.14 | zaman. (1. geçiş) | 7.00 | +0.14 |  |
| 02 | kar tanesi 2 | 7.34 | zaman. (1. geçiş) | 7.00 | +0.34 |  |
| 02 | kış bandı 3 | 7.27 | zaman. (1. geçiş) | 7.00 | +0.27 |  |
| 02 | kar tanesi 3 | 7.47 | zaman. (1. geçiş) | 7.00 | +0.47 |  |
| 02 | kış bandı 4 | 7.41 | zaman. (1. geçiş) | 7.00 | +0.41 |  |
| 02 | kar tanesi 4 | 7.61 | zaman. (1. geçiş) | 7.00 | +0.61 |  |
| 02 | odak 1 kapanır | 8.37 | She (EN2 çapası) | 8.37 | +0.00 |  |
| 02 | kart 2 kutusu | 8.04 | She (EN2 çapası) | 8.37 | ⚠ -0.33 | yazısız kart çerçevesi; kart metni `She` ile açılır |
| 02 | kart 2 sözcükleri | 8.37 | She (EN2 çapası) | 8.37 | +0.00 |  |
| 02 | kart 2 karaoke | 8.37 | She (EN2 çapası) | 8.37 | +0.00 |  |
| 02 | tisort | 9.64 | T-shirt (EN2 çapası) | 9.65 | ⚠ -0.01 | kare yuvarlaması (< 1 kare, 0,033 sn; `fr()` en yakın kare) |
| 02 | odak today | 10.14 | today. (EN2 çapası) | 10.13 | +0.01 |  |
| 02 | today daire | 11.41 | Today | 11.42 | ⚠ -0.01 | kare yuvarlaması (< 1 kare, 0,033 sn; `fr()` en yakın kare) |
| 02 | today daire mürekkep | 11.41 | Today | 11.42 | ⚠ -0.01 | kare yuvarlaması (< 1 kare, 0,033 sn; `fr()` en yakın kare) |
| 02 | MEANING hapı | 14.14 | anlam | 14.14 | +0.00 |  |
| 02 | soru altçizgi | 14.21 | anlam | 14.14 | +0.07 |  |
| 02 | RIGHT NOW | 15.24 | Konuşma | 15.25 | ⚠ -0.01 | kare yuvarlaması (< 1 kare, 0,033 sn; `fr()` en yakın kare) |
| 02 | zaman-2 eksen | 15.37 | Konuşma | 15.25 | +0.12 |  |
| 02 | zaman-2 ok | 15.67 | Konuşma | 15.25 | +0.42 |  |
| 02 | bag today | 15.74 | Konuşma | 15.25 | +0.49 |  |
| 02 | nabiz | 15.91 | anı: | 15.81 | +0.10 |  |
| 02 | now 2 nokta | 15.81 | anı: | 15.81 | +0.00 |  |
| 02 | now 2 metin | 16.01 | anı: | 15.81 | +0.20 |  |
| 02 | Present Continuous | 16.47 | şimdiki | 16.49 | ⚠ -0.02 | kare yuvarlaması (< 1 kare, 0,033 sn; `fr()` en yakın kare) |
| 02 | today çentik 1 | 16.74 | şimdiki | 16.49 | +0.25 |  |
| 02 | today çentik 2 | 16.84 | şimdiki | 16.49 | +0.35 |  |
| 02 | today bandı | 16.61 | şimdiki | 16.49 | +0.12 |  |
| 08 | kart `Today iki zamanda da geçebilir; farkı anlam yapar.` | 17.96 | Bu, | 17.96 | +0.00 |  |
| 08 | 3 nokta (üç farktan biri) | 18.48 | üç | 18.48 | +0.00 |  |
| 08 | vizör çizimi + `Ekran görüntüsü` | 20.27 | Ekran | 20.27 | +0.00 | BİLGİ (B2, EK-12 kol b): `görüntüsü` t0 20.71; ifade ilk sözcüğüyle açılır, ikinci sözcük 0.44 sn önce görünür. Kod değişmedi |
| 08 | deklanşör + `al,` | 21.35 | al, | 21.35 | +0.00 |  |
| 08 | `sınav günü bak.` | 21.79 | sınav | 21.79 | +0.00 |  |
| 03 | `Konu burada` | 23.38 | Konu | 23.38 | +0.00 | BİLGİ (B2 kalıbı): `burada` t0 23.70; ifade ilk sözcüğüyle açılır, ikinci sözcük 0.32 sn önce görünür. Kod değişmedi (kol b değişken sahnesi) |
| 03 | `bitmiyor.` | 24.14 | bitmiyor. | 24.14 | +0.00 |  |
| 03 | ana ders kapak kartı | 24.97 | Dersin | 24.97 | +0.00 |  |
| 03 | `@ydspublishing` hapı | 26.25 | YDS | 26.25 | +0.00 |  |
| 03 | `· YouTube` | 27.37 | YouTube | 27.37 | +0.00 |  |

---
Üretim: DUZ4-0204S2 oturumu (Opus 5.5); ölçüm, kod değişikliği yok.
