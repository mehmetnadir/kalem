# KULAK-RAPOR 02-02-ydt-temel

Ölçüm: faster-whisper large-v3 (CPU int8, P1 kapısıyla aynı aile; P1'in ham çıktısı pakette yok, parçalar yeniden çözüldü: tam cümle language=tr ve en, kelime zamanından pencere; klip = parça ±0,25 sn + initial_prompt). Pencere = parça zamanı ±0,1 sn içine düşen kelimeler. Ses dosyasına yazılmadı.

Sonuç: 9 madde, TAMAM 4, ŞÜPHELİ 5

| paket | cümle | parça | tr-duyulan | en-duyulan | klip | karar | kanıt |
|---|---|---|---|---|---|---|---|
| 02-02-ydt-temel | 9 | 1 (en) `I.` | iyi. Fiiller | iyi. Fiiller | klip tr: i / en: E | ŞÜPHELİ | iki ölçümde de Türkçe "i"/"E"; İngilizce "ay" duyulmadı |
| 02-02-ydt-temel | 33 | 4 (tr) `ve` | ve look. | when, look. | klip tr: Whip / en: web | TAMAM | tr penceresi "ve look" |
| 02-02-ydt-temel | 19 | 3 (en) `it.` | et. Feel | et. Feel, | klip tr: Et. / en: Et... | ŞÜPHELİ | iki ölçümde "et"; "it" duyulmadı |
| 02-02-ydt-temel | 14 | 4 (tr) `ve` | weigh, swims. | weigh, swims. | klip tr: Wey / en: Wey? | ŞÜPHELİ | "weigh"/"Wey"; "ve" duyulmadı |
| 02-02-ydt-temel | 42 | 1 (en) `she` | var. | şimdi var. | klip tr: şimşek / en: See you in the next video. | ŞÜPHELİ | "var." / "şimdi var." / "şimşek"; "she" yok |
| 02-02-ydt-temel | 42 | 2 (tr) `var. /ˈdʌzənt/` | var. Olmaz mı? | var. Doesn't it? | klip tr: var / en: varış, doesn't eat | TAMAM | en penceresi "var. Doesn't it?" |
| 02-02-ydt-temel | 37 | 3 (en) `Ing` | In yok. | In yok. | klip tr: İngiliz. / en:  | ŞÜPHELİ | "In yok" / "İngiliz"; "ing" eksik |
| 02-02-ydt-temel | 14 | 1 (en) `he.` | he. | he. | klip tr: He. / en: He. | TAMAM | "he." iki dilde + klip (ek madde) |
| 02-02-ydt-temel | 57 | 3 (en) `he.` | he. | he. | klip tr: He. / en: He. | TAMAM | "he." iki dilde + klip |

Not: Whisper tek sözcükte güvenilmez; ŞÜPHELİ = iki ölçümde de beklenen sesi vermedi, hata kesin değil.
