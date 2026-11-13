# SES-DUZELTME 02-02-ydt-ileri (13.11)

Paket sesi DEĞİŞMEDİ (anlatim.wav/m4a, sureler.json, zaman.json aynı). Ölçüm: Whisper large-v3, 3 tohum × (düz yazım + IPA), cümle 30 ve 56 yeniden sentezlendi (deneme çıktısı pakete yazılmadı).

| cümle | madde | eski duyulan | deneme sonucu | karar |
|---|---|---|---|---|
| 30 | `ve` (tr, "Live ve work") | Work. | 3 tohumda "work / with Work."; "ve" duyulmadı | KULAK (Nadir) |
| 56 | `says.` (en, 1. parça) | Sez | tüm tohumlarda "Sez." | TAMAM: Whisper /sɛz/ sesini "Sez" yazıyor, "says" doğru söylenmiş |
| 56 | `says.` (en, 3. parça) | sez | tüm tohumlarda "sez." (IPA `/sɛz/.` dahil) | TAMAM (aynı gerekçe) |
| 55 | `it,` ve `says.` | TAMAM | – | değişmedi |
| 57 | `it` | TAMAM | – | değişmedi |
| 27 | `ve` | TAMAM | – | değişmedi |

Sonuç: 0 düzeltilen, 1 KULAK (Nadir): cümle 30 `ve`. Neden cümle 14 (02-02-temel) ile aynı: tek heceli Türkçe "ve" İngilizce sözcüklerin arasında duyulmuyor. Çözüm önerisi: "ve" parçasını sonraki Türkçe metne bağlamak (senaryo.json, şef kararı). Süre farkı yok; sahne zamanı kaymadı.

## Ek: cümle 30 `ve` (13.11, koordinatör kararı) — SES DEĞİŞTİ

Önceki "ses değişmedi" notu bu ekle geçersiz: yalnız cümle 30 yeniden seslendirildi. `senaryo.json` cümle 30: `Live` | `ve` | `work` | `süreklilik taşır.` → `ve` sonraki Türkçe metne bağlandı: son parça tr `ve, work süreklilik taşır.` Yedek: `_is/senaryo-ve-oncesi.json`, `_is/ses-duzeltme/yedek-1113-ve/`.

Deneme: `ve work` → "We work" (İngilizce okundu); `ve, work` → 3 tohumda "Ve Work" (kapı 1,0). Seçilen: tohum 0. large-v3: "Live ve Work. Süreklilik taşır." → "ve" Türkçe duyuldu. KAPANDI (KULAK kalmadı).
Süre: cümle 30 +0,38 sn; paket toplamı 418,74 → 419,12 sn. K23 korundu (sahne 01 0–3,0 sn, ilk söz 1,00 sn).

Kayan sahneler (sahne 01–08 değişmedi):

| sahne | eski t_bas–t_son (kare) | yeni t_bas–t_son (kare) | Δson |
|---|---|---|---|
| 09 | 196,44–224,18 (844) | 196,44–224,56 (856) | +0,38 (+12 kare) |
| 10 | 224,18–259,61 (1075) | 224,56–259,99 (1075) | +0,38 |
| 11 | 259,61–289,65 (913) | 259,99–290,03 (913) | +0,38 |
| 12 | 289,65–315,77 (796) | 290,03–316,15 (796) | +0,38 |
| 13 | 315,77–339,73 (731) | 316,15–340,11 (731) | +0,38 |
| 14 | 339,73–357,83 (555) | 340,11–358,21 (555) | +0,38 |
| 15 | 357,83–404,64 (1416) | 358,21–405,02 (1416) | +0,38 |
| 16 | 404,64–418,74 (453) | 405,02–419,12 (453) | +0,38 |

Yenilenen: `cumle-30.wav`, `sureler.json`, `sozcukler.json`, `anlatim.wav`, `anlatim.m4a`(+`.imza`), `altyazi.json`, `zaman.json`. Sahne dosyalarına dokunulmadı.

## Kulak notu
Kulak notu: `-ing` ve `ink`: Whisper /ɪŋ/ ucunu "ink" yazabiliyor (bu pakette `-ing` düzeltmesi yok). Başka yazım denemesi yapılmadı.

## Ek: virgül yalnız sese (13.11, koordinatör düzeltmesi)
`senaryo.json` ekran metninde virgül yok (`ve swims.` / `ve work …`). Virgül `ses_metni.py` Kural 7 ile yalnız ses metnine girer (`ve,`); sentezde kullanılan metinle birebir aynı, önbellek wav'ı bulundu, yeniden sentez yok. `altyazi.json`, `sozcukler.json`, `sureler.json` virgülsüz yenilendi (virgüllü sürümler `_is/ses-duzeltme/yedek-1113-ve/*.virgullu.json`). `zaman.json` ve ses dosyaları değişmedi.
