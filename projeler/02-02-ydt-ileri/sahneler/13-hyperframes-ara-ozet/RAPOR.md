# Sahne 13 — Ara özet (HyperFrames, 731 kare = 719 içerik + 12 geçiş; t_bas 315,77)

Tema: acik

Durum: önizleme hazır (koyu, sonra açık; son koşu AÇIK). Render, kapı ve kare görüntüsü bu turda YOK (şef EK 13.11 12:40).

## İçerik
- `ozet` ilk satır: Caveat `Özet`, sarı el madde işareti + `tekrar · kalıcı · genel gerçek`.
- İkinci satır: Caveat `dört çerçeve → geniş zaman`; dört kutu sırayla yanar (Özet · Tabela · Tören · Tarife, sarı kenar); altta Caveat `Türkçesi şimdiki · geçmiş · gelecek`.
- Cümle 49: üç kutu ok ile bağlanır: `çerçeve → özne → yardımcı fiil` (kutu başına sarı numara 1–3), Caveat `Sınavda sırayla bak`.
- Cümle 50: `kinetik_baslik` `Kod:` + `Türkçeye değil,` (soluk, üstü çizili) + `çerçeveye bak.` (Fredoka 156, `çerçeveye` sarı).
- Künye: `Recap`, ajanda etkin Roots. Renk yalnız `RENK` (kırmızı yok, yeşil yok).

## Olay ↔ sözcük t0 (sozcukler.json; yerel = küresel − 315,77)
| Olay | Cümle / sözcük | Sözcük t0 | Olay küresel | Yerel | Sapma |
|---|---|---|---|---|---|
| `Özet` başlığı | 47 Özet: | 316,32 | 316,32 | 0,55 | 0,00 |
| `tekrar` | 47 tekrarı, | 318,00 | 318,00 | 2,23 | 0,00 |
| `kalıcı` | 47 kalıcı | 318,88 | 318,88 | 3,11 | 0,00 |
| `genel gerçek` | 47 genel | 320,00 | 320,00 | 4,23 | 0,00 |
| `dört çerçeve` | 48 Dört | 321,99 | 321,99 | 6,22 | 0,00 |
| `geniş zaman` | 48 geniş | 323,03 | 323,03 | 7,26 | 0,00 |
| Özet kutusu yanar | 48 özet, | 324,31 | 324,31 | 8,54 | 0,00 |
| Tabela kutusu yanar | 48 tabela, | 325,07 | 325,07 | 9,30 | 0,00 |
| Tören kutusu yanar | 48 tören, | 325,91 | 325,91 | 10,14 | 0,00 |
| Tarife kutusu yanar | 48 tarife. | 326,67 | 326,67 | 10,90 | 0,00 |
| `çerçeve` kutusu (1) | 49 çerçeve, | 333,58 | 333,53 (kenar) / 333,58 | 17,76 / 17,81 | 0,00 |
| `özne` kutusu (2) + ok 1 | 49 özne, | 334,58 | 334,28 (ok) / 334,58 | 18,51 / 18,81 | 0,00 |
| `yardımcı fiil` kutusu (3) + ok 2 | 49 yardımcı | 335,30 | 335,00 (ok) / 335,30 | 19,23 / 19,53 | 0,00 |
| `Kod:` | 50 Kod: | 336,77 | 336,77 | 21,00 | 0,00 |
| `Türkçeye` | 50 Türkçeye | 337,57 | 337,57 | 21,80 | 0,00 |
| `değil,` + üstü çizgi | 50 değil, | 338,05 | 338,05 | 22,28 | 0,00 |
| `çerçeveye` (sarı) | 50 çerçeveye | 338,69 | 338,69 | 22,92 | 0,00 |
| `bak.` | 50 bak. | 339,41 | 339,41 | 23,64 | 0,00 |
C47–C48 grubu 331,42'de solar (cümle 48 biter 331,35; cümle 49 başlar 331,82); C49 grubu 336,42'de solar (cümle 50 başlar 336,77). Oklar kendi sözcüklerinden 0,30 sn önce çizilir (bağlantı kutuyu karşılar). olaylar.json 26 olay (kare 16–668).

## Kontroller (kapı/görüntü yok)
- Üretimde taşma sınamaları (assert): madde satırı, notlar, kutu başlıkları, adım zinciri, kod satırları sığıyor.
- `node --check` 2 blok OK · yinelenen id yok · `Math.random`/`Date` yok · negatif zaman yok.
- İlk hareket 0,55 sn (kare 16), son olay 23,64 sn (kare ≈ 709 < 719); son 12 kare durgun.

## Açık
- C48 sahnesi yoğun (başlık, madde satırı, not, dört kutu, alt not); QA şeridi göz kontrolünde bakılmalı.


## QA 13.11
Kapı: bu motor için ölçülmedi. Kareler: k/13-hyperframes-ara-ozet-{318.2,324.9,331.6,339.2}.png (açık), k/koyu/ içinde (bakılmadı). Göz: şef maddesi 4: 331,6 karesi yoğun (başlık, madde, not, dört kutu, alt not) ama taşma/binme yok; 'Özet' başlığı künyeye ~20 px yakın, okunur. 339,2'de sahne 'Kod: Türkçeye değil, çerçeveye' ile sade. Sadeleştirme gerekmedi. Kalan: yok.

zaman eşitleme 13.11: cümle 30 +0,38 sn. `--hazirla` yeniden kuruldu. Kareler 325,3 / 332,0 / 339,6 bakıldı; 332,0'da Özet grubu soluyor (geçiş), taşma yok.
