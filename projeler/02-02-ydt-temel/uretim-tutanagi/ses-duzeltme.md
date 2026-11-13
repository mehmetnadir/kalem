# SES-DUZELTME 02-02-ydt-temel (13.11)

Yöntem: tek sözcüklük en parça için sözlük yazımları (`ses-sozluk.json` "en_tek"), düz yazım ve varyant × 3 tohum, seçim Whisper large-v3 (tr + en çözüm, parça penceresi ±0,1 sn). Yedek: `_is/ses-duzeltme/yedek-1113/` (`cumle-baslar.json` yedeğe girmedi; değerler zaman.json yedeğinden türetilir).

| cümle | madde | eski duyulan | yeni duyulan | tohum | süre farkı |
|---|---|---|---|---|---|
| 9 | `I.` (en) | iyi / E | I. (tr ve en çözüm); yazım `/aɪ/.` | 0 | +0,08 sn |
| 19 | `it.` (en) | et | it. (en çözüm), tr çözüm "et"; yazım `/ɪt/.` | 0 | +0,08 sn |
| 37 | `Ing` (en) | In yok / İngiliz | Ing. Yok. (tr ve en); yazım `Ing,` | 0 | +0,88 sn |
| 42 | `she` (en) | var / şimdi var | she var (tr), she, var (en); yazım `She,` | 1 | +0,48 sn |
| 14 | `ve` (tr, "gets ve swims") | weigh / Wey | duyulmadı (way, with, Swims; 4 yazım × 3 tohum) | – | cümle değişmedi |

Sonuç: 4 madde düzeltildi, 1 KULAK (Nadir): cümle 14 `ve`. Tek heceli Türkçe "ve", iki İngilizce sözcüğün arasında İngilizce "way/with" okunuyor; IPA denemesi "eğik çizgi ve eğik çizgi" okudu. Senaryoda "ve" parçasını önceki ya da sonraki Türkçe metne bağlamak çözer (şef kararı). TAMAM kalanlar: cümle 33 `ve`, cümle 14 ve 57 `he.`, cümle 42 `var. /ˈdʌzənt/`.

Süre: toplam +1,52 sn (388,05 → 389,57 sn). Sahne 01 = 0–3,0 sn, ilk söz 1,00 sn (K23 bozulmadı).

## Zamanı kayan sahneler (`zaman.json`, sahne t_son = cümle bitişi + fark)

| sahne | eski t_bas–t_son (kare) | yeni t_bas–t_son (kare) |
|---|---|---|
| 03 | 16,27–44,37 (855) | 16,27–44,45 (857) |
| 04 | 44,37–70,08 (783) | 44,45–70,16 (783) |
| 05 | 70,08–96,65 (809) | 70,16–96,81 (812) |
| 06 | 96,65–157,88 (1849) | 96,81–158,04 (1849) |
| 07 | 157,88–218,97 (1845) | 158,04–220,01 (1871) |
| 08 | 218,97–280,71 (1864) | 220,01–282,23 (1879) |
| 09 | 280,71–316,41 (1083) | 282,23–317,93 (1083) |
| 10 | 316,41–368,49 (1574) | 317,93–370,01 (1574) |
| 11 | 368,49–388,05 (599) | 370,01–389,57 (599) |

Sahne 01–02 değişmedi. Sahne 03–11 dosyalarında sabit zaman yazılıysa kayar (sahne 07–11 en çok: +0,16 … +1,52 sn). Sahne dosyalarına dokunulmadı.

## Yenilenen dosyalar
`ortak/anlatim/{cumle-9,19,37,42.wav, sureler.json, sozcukler.json, cumle-baslar.json, anlatim.wav, anlatim.m4a(+.imza), altyazi.json}`, `zaman.json`. `METIN.md` ve `senaryo.json` değişmedi. `sentez.wav` eski.

## Ek: cümle 14 `ve` (13.11, koordinatör kararı)

`senaryo.json` cümle 14: `gets` | `ve` | `swims.` | `İkisinin…` parçaları, `ve` sonraki Türkçe metne bağlandı: son parça tr `ve, swims. İkisinin sonunda da se var.` (virgül ses metninde; ekranda altyazıda da görünür). Yedek: `_is/senaryo-ve-oncesi.json`, `_is/ses-duzeltme/yedek-1113-ve/`.

| deneme | duyulan "ve" | not |
|---|---|---|
| `ve swims.` | We swims (3 tohum) | İngilizce "we" okundu |
| `Ve swims.`, `Ve, swims.`, `/vɛ/ swims.` | Ve (çoğu tohum) | |
| `ve, swims.` | Ve Swims, 3/3 tohum | seçildi (en az değişiklik) |

Seçilen: tohum 0, kapı 0,99. large-v3 tam cümle: "Gets ve swims. İkisinin sonunda da S var." → "ve" Türkçe duyuldu. KAPANDI (KULAK kalmadı).
Süre: cümle 14 süresi eski 9,74 → 9,24 sn. Paket toplamı 389,57 → 389,07 sn (orijinale göre 388,05 → 389,07, +1,02 sn). K23 korundu: sahne 01 0–3,0 sn, ilk söz 1,00 sn.

Kayan sahneler (bugünkü adım / orijinale göre toplam):

| sahne | bugünkü adım Δson (Δkare) | orijinale göre Δson (Δkare) |
|---|---|---|
| 03 | 0 | +0,08 (+2) |
| 04 | −0,50 (−15) | −0,42 (−15) |
| 05 | −0,50 (0) | −0,34 (+3) |
| 06 | −0,50 (0) | −0,34 (0) |
| 07 | −0,50 (0) | +0,54 (+26) |
| 08 | −0,50 (0) | +1,02 (+15) |
| 09–11 | −0,50 (0) | +1,02 (0) |

Not: sahne 04–11 t_bas/t_son değişti; sahne 04 uzunluğu 15 kare kısaldı. Sahne dosyalarına dokunulmadı.

## Kulak notu
Kulak notu: `-ing` ve `ink`: Whisper /ɪŋ/ ucunu "ink" yazabiliyor, Türkçe "İngi" ya da harf harf okuma yok. Başka yazım denemesi yapılmadı (koordinatör kararı).

## Ek: virgül yalnız sese (13.11, koordinatör düzeltmesi)
`senaryo.json` ekran metninde virgül yok (`ve swims.` / `ve work …`). Virgül `ses_metni.py` Kural 7 ile yalnız ses metnine girer (`ve,`); sentezde kullanılan metinle birebir aynı, önbellek wav'ı bulundu, yeniden sentez yok. `altyazi.json`, `sozcukler.json`, `sureler.json` virgülsüz yenilendi (virgüllü sürümler `_is/ses-duzeltme/yedek-1113-ve/*.virgullu.json`). `zaman.json` ve ses dosyaları değişmedi.
