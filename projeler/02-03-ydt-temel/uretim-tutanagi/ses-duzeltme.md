# SES-DUZELTME 02-03-ydt-temel (13.11)

Yöntem: IPA `/ɪŋ/` (tr parçada "-ing") ve "özne I → ay" kuralı (`ses-sozluk.json`), 3 tohum (0, 1, 2), seçim Whisper large-v3 (tr + en çözüm, parça penceresi ±0,1 sn). Yedek: `_is/ses-duzeltme/yedek-1113/`.

| cümle | madde | eski duyulan | yeni duyulan | tohum | süre farkı |
|---|---|---|---|---|---|
| 6 | "Neden -ing?" | İngi | İng (tr), ING (en) | 0 | −0,08 sn |
| 12 | "Sinyal var ama -ing yok." | ı, n, g yok | ing yok | 2 | −0,88 sn |
| 12 | "-ing koymak istersin" | ING'yi koymak | İng koymak (tr), Ink koymak (en) | 2 | (aynı cümle) |
| 14 | "Onlar da -ing almaz" | ing'i / yenge almaz | ing almaz | 2 (parça 4) | −0,64 sn |
| 14 | "Have … -ing almaz" | INEG almaz | ing almaz | 0 (parça 6) | (aynı cümle) |
| 15 | "Sinyal olsa da -ing yok" | iğenge yok | ing yok | 0 | −0,32 sn |
| 18 | "özne I ile uyumsuz" | özne A | özne I (tr ve en) | 0 | −0,16 sn |
| 19 | "believe gibi fiiller -ing almaz" | inge almaz / ilgi | ink almaz | 0 | +0,32 sn |

Sonuç: 8 madde düzeltildi, 0 KULAK (Nadir) zorunlu. Ek not: cümle 19 ve cümle 12 "Ink koymak" için Whisper "ink" yazdı; sonuç /ɪŋk/ gibi, ünlüsüz "-ng" ucu var, "İngi" ve harf harf okuma yok. Kulakla son bakış önerilir (cümle 19).

Süre: toplam −1,76 sn (282,19 → 280,43 sn). Cümle başları: 7–12 −0,08 sn, 13–14 −0,96 sn, 15 −1,60 sn, 16–18 −1,92 sn, 19 −2,08 sn. Sahne 01 = 0–3,0 sn, ilk söz 1,00 sn (K23 bozulmadı).

## Zamanı kayan sahneler (`zaman.json`, `zaman_uret.py` ile yeniden üretildi)

| sahne | eski t_bas–t_son (kare) | yeni t_bas–t_son (kare) |
|---|---|---|
| 06 hyperframes-soru1 | 68,56–87,78 (589) | 68,56–87,70 (586) |
| 07 hyperframes-kural | 87,78–109,61 (667) | 87,70–109,53 (667) |
| 08 canvas-karsit1 | 109,61–130,74 (646) | 109,53–130,66 (646) |
| 09 canvas-karsit2 | 130,74–167,60 (1118) | 130,66–167,52 (1118) |
| 10 hyperframes-tuzak | 167,60–188,50 (639) | 167,52–187,54 (613) |
| 11 canvas-tuzak-fiiller | 188,50–226,45 (1150) | 187,54–224,85 (1131) |
| 12 hyperframes-ozet | 226,45–242,28 (487) | 224,85–240,36 (477) |
| 13 hyperframes-mini-soru | 242,28–272,42 (916) | 240,36–270,34 (911) |
| 14 hyperframes-kapanis | 272,42–282,19 (323) | 270,34–280,43 (333) |

Sahne 01–05 değişmedi. Sahne 06–14 dosyalarında sabit zaman yazılıysa hepsi kayar (sahne 10–14 en çok: −0,96 … −2,08 sn). Sahne dosyalarına dokunulmadı; şef önizlemeyi yeniden kurdurur.

## Yenilenen dosyalar
`ortak/anlatim/{cumle-6,12,14,15,18,19.wav, sureler.json, sozcukler.json, baslar.json, anlatim.wav, anlatim.m4a(+.imza), altyazi.json}`, `zaman.json`. `METIN.md` ve `senaryo.json` değişmedi (ekran metni aynı, tutarlı). `sentez.wav` ve `sentez.wav.rapor.json` eski (bilgi amaçlı, paket kullanmıyor).

## Kulak notu
Kulak notu: `-ing` ve `ink`: Whisper /ɪŋ/ ucunu "ink" yazabiliyor (cümle 12 ikinci `-ing`, cümle 19). /ɪŋ/ ucu böyle yazılıyor; başka yazım denemesi yapılmadı (koordinatör kararı 13.11).
