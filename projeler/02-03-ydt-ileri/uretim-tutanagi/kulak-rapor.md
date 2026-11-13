# KULAK-RAPOR 02-03-ydt-ileri

Ölçüm: faster-whisper large-v3 (CPU int8, P1 kapısıyla aynı aile; P1'in ham çıktısı pakette yok, parçalar yeniden çözüldü: tam cümle language=tr ve en, kelime zamanından pencere; klip = parça ±0,25 sn + initial_prompt). Pencere = parça zamanı ±0,1 sn içine düşen kelimeler. Ses dosyasına yazılmadı.

Sonuç: 1 madde, TAMAM 1, ŞÜPHELİ 0

| paket | cümle | parça | tr-duyulan | en-duyulan | klip | karar | kanıt |
|---|---|---|---|---|---|---|---|
| 02-03-ydt-ileri | 9 | 6 (en) `it` | it ile | it ile | klip tr: It is getting harder. / en: It is getting harder and harder to find a good job at the moment. At the moment points to  | TAMAM | "it ile" pencerede |

Not: Whisper tek sözcükte güvenilmez; ŞÜPHELİ = iki ölçümde de beklenen sesi vermedi, hata kesin değil.
