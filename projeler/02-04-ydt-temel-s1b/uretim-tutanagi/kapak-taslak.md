# 02-04-ydt-temel-s1b · A kapağı taslağı (kanca karesi, 1080×1920 PNG)

Durum: TASLAK (istem BK-0204S1, 15.11.2026). Görsel üretim ve render YOK.
Kural: sözleşme §4 (değişken `kanca` → kol b kendi `s1b-kapak-a` karesini taşır; B ve C gruba aittir) · huni v2 §6 (altyazı yok,
kanal katmanı var, A = kanca karesi) · kol a `../../02-04-ydt-temel-s1/uretim-tutanagi/kapak-taslak.md` §1–§2 (ölçüler).
Çıktı: `kapak-a.png` (paket kökü), açık + koyu. Yöntem kol a ile aynı: sahne 01 kapak karesi (≈ t 1,75; kol b `zaman.json`'dan),
`#altyazi{display:none}`, `hyperframes snapshot --at <t>`.

## 1. Öğeler

| Öğe | Değer | Kol a A'dan farkı |
|---|---|---|
| Başlık satır 1 | `YAŞIYORUM` · mürekkep `#1b2440` · `YOR` altında sarı el altçizgisi | aynı |
| Başlık satır 2 | `AYNI MI?` · sarı hap: dolgu `#ffe066` (`RENK.vurguDolgu`), yazı `#1b2440` (`RENK.pilMetin`) | **değişti** (kol a `= İKİ ZAMAN`): yargı → soru |
| Sözcük sayısı | 3 (`YAŞIYORUM`, `AYNI`, `MI`) · 2 satır | kol a 3 |
| Cümle satırları | `İstanbul'da yaşı-yor-um.` (taban 920) · `Amcamla yaşı-yor-um.` (taban 1040); Caveat 700 80, x 84; iki satırda `yor` sarı kutuda | **değişti**: kol a karede yalnız satır 1, `yor` kutusu yok |
| İngilizce etiket | YOK (cevap karede yok) | **değişti**: kol a `I live` / `I am living` |
| Görsel | ev (sol) + elinde bavul tutan öğretmen figürü; figür yüksekliği ≈ 280, ev ve figür y 1084–1372 | **değişti**: figür küçük (kol a 400) |
| Kanal katmanı | logo + `@ydspublishing` (y 280–350, kol a ile aynı piksel) | aynı |
| Rozet | `YDT · BASIC`, x 60 (künye bandı; konu adı yok) | aynı |
| Altyazı | yok | aynı |
| Yasak | üçüncü başlık satırı, emoji, "Tam ders", süre sözü, QR | aynı |

## 2. Yerleşim (v2 bantları, y px)

```
0 ─────── 280   üst boş (zemin)
280 ───── 350   kanal katmanı: logo + @ydspublishing
386 ───── 434   rozet YDT · BASIC (x 60)
472 ───── 826   başlık: YAŞI[YOR]UM (altçizgi) / ( AYNI MI? ) sarı hap
851 ──── 1057   İstanbul'da yaşı-[yor]-um.  (taban 920)
                Amcamla yaşı-[yor]-um.      (taban 1040)
1084 ─── 1372   ev (sol) · öğretmen figürü + bavul (sağ) · yer çizgisi 1372 · etiket yok
1400 ─── 1920   boş (altyazı gizli)
```

- Başlık boyu: kol a formülü; `YAŞIYORUM` belirler (B ≈ 152). `AYNI MI?` hapı kol a hapından dardır, ortası x 510.
- Dikey aralar (≥ 24 px): hap altı 826 → satır 1 üstü ≈ 851 (25 px; kol a ile aynı R1_K) · satır 2 altı ≈ 1057 → görsel üstü 1084 (27 px).

## 3. Kapak gerekçesi

- Kol a karesi cevabı verir (`= İKİ ZAMAN`, `I live` / `I am living`). Kol b karesi soruyu sorar ve iki örneği gösterir; cevap videodadır.
- Dikkat: grubun kapak B'si (`YAŞIYORUM` / `NASIL DENİR?`) da soru biçimindedir. Kol b A kapağı ondan iki öğeyle ayrılır: iki Türkçe
  cümle satırı ve `yor` kutuları. Kapak değişkeni ayrı sınanırsa bu benzerlik not edilir (BK-RAPOR §e).
