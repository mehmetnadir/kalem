# KULAK-RAPOR 02-02-ydt-ileri

Ölçüm: faster-whisper large-v3 (CPU int8, P1 kapısıyla aynı aile; P1'in ham çıktısı pakette yok, parçalar yeniden çözüldü: tam cümle language=tr ve en, kelime zamanından pencere; klip = parça ±0,25 sn + initial_prompt). Pencere = parça zamanı ±0,1 sn içine düşen kelimeler. Ses dosyasına yazılmadı.

Sonuç: 7 madde, TAMAM 5, ŞÜPHELİ 2

| paket | cümle | parça | tr-duyulan | en-duyulan | klip | karar | kanıt |
|---|---|---|---|---|---|---|---|
| 02-02-ydt-ileri | 27 | 5 (tr) `ve` | ve hope, | ve hope. | klip tr: web / en: WEP | TAMAM | "ve hope" (tr penceresi) |
| 02-02-ydt-ileri | 30 | 2 (tr) `ve` | Work. | work, carry | klip tr: Altyazı M.K. / en: What? | ŞÜPHELİ | pencere "Work." ve yok; klip "Altyazı M.K."/"What?" |
| 02-02-ydt-ileri | 55 | 1 (en) `it,` | it, yani | it, yani | klip tr: It. / en: It. | TAMAM | "it, yani" + klip "It." |
| 02-02-ydt-ileri | 55 | 3 (en) `says.` | says. | says. | klip tr: 6 / en: 6 | TAMAM | pencere "says." |
| 02-02-ydt-ileri | 56 | 1 (en) `says.` | Sez. | Sez. | klip tr: Says. / en: Says. | TAMAM | klip "Says." |
| 02-02-ydt-ileri | 56 | 3 (en) `says.` | sez. | sez. | klip tr:  / en:  | ŞÜPHELİ | pencere "sez" (yazım eşleşmedi), klip boş; /sez/ olabilir, kanıt zayıf |
| 02-02-ydt-ileri | 57 | 1 (en) `it` | it için | no S for | klip tr: Çeldirici B / en: Çeldirici B | TAMAM | "it için" |

Not: Whisper tek sözcükte güvenilmez; ŞÜPHELİ = iki ölçümde de beklenen sesi vermedi, hata kesin değil.
