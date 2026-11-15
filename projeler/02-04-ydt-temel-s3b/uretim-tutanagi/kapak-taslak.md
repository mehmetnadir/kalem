# 02-04-ydt-temel-s3b · kapak taslağı (yalnız A, 1080×1920 PNG)

Durum: TASLAK (istem BK-0204S3, 15.11.2026). Görsel üretim ve render YOK.
Kural: `D/.claude/docs/huni-v2-standart.md` §2, §6 · `D/.claude/docs/huni-ab-sozlesme.md` §4 (değişken `kanca` → kol b kendi
`s3b-kapak-a` karesini taşır; B ve C gruba aittir, yinelenmez). Kol a emsali: `../../02-04-ydt-temel-s3/uretim-tutanagi/kapak-taslak.md`.
A kapağı = kanca karesi: sahne 01'in ≈ 1,75 sn karesi (kare 52), altyazı katmanı GİZLİ (kol a yöntemi, `BRIEF-S3.md` "kanca karesi").
Çıktı adı (öneri): `kapak-a.png` (kol b paketinde; `kapak.png` = A).

## 1. Öğeler

| Öğe | Kol b A | Kol a A (karşılaştırma) |
|---|---|---|
| Başlık satır 1 | `HATA` · altında sarı el altçizgisi | `TARİFE` · altçizgi |
| Başlık satır 2 | `NEREDE?` (sarı hap) | `≠ PLAN` (sarı hap) |
| Sözcük sayısı | 2 (≤ 4) | 2 |
| Uzunluk (karakter) | 4 / 7 | 6 / 6 |
| Kart | yanlış cümle, 2 satır, Fredoka 700 64, x 97: `The train to İzmir` (taban 986) / `is leave at 7 pm today.` (taban 1084); vurgusuz (hatanın yeri gösterilmez) | satır 1 `The train to İzmir` (sözle yazılmış) |
| İşaret | mürekkep el çizimi `?`, satır 1'in sağında | yok |
| Görsel | solda tren + saat (kollar yedide, rakamsız); sağda öğretmen figürü ≈ 250 px, trene işaret eder; bilet yok | tren + saat · bilet tutan figür 340 px |
| Etiket | yok (`leaves` cevabı verir) | `leaves` / `am going` |
| Kanal katmanı | var: logo + `@ydspublishing` (y 291–339, kol a ile aynı) | aynı |
| Künye | yalnız rozet `YDT · BASIC` (konu adı kapak karesinde yok) | aynı |
| Altyazı | YOK | yok |
| Can alıcı | `canAlici[1]` (tarifeli gelecek: V1 / V-s); kısa kod `is leave → leaves`. Kart yanlış biçimi gösterir, cevap videoda (3,35 `leaves`) | `canAlici[1]` + `[2]`: `tarife → leaves · plan → am going` |
| Vurgu | tek vurgu = `HATA` altçizgisi + `NEREDE?` hapı; `?` mürekkep | altçizgi + hap |
| Yasak | kırmızı, yeşil, ✗ simgesi, emoji, gradyan, gölge, "Tam ders", süre sözü | aynı |

- `HATA`, `NEREDE?` Türkçe büyük harf elle yazılır; `text-transform` yok. İ yok, yerel sorun yok.
- Yeni metin: `HATA` / `NEREDE?` (kanca sözünün kendisi) ve kart satırı `is leave at 7 pm today.` — jüri bakacak (BK-RAPOR §b).
- Kart satırı ≤ 24 karakter: `is leave at 7 pm today.` = 23. Ekranda `7` rakamdır (rakam kuralı yalnız söylenen metinde; kol a jürisi, `s3.dil.md` açık noktalar).

## 2. Yerleşim (1080×1920, huni v2 §2 bantları, y px)

```
   0 ─  280   boş zemin
 291 ─  339   [logo] @ydspublishing                      kanal katmanı (kol a ile aynı yer)
 386 ─  434   [YDT · BASIC]                              künye: yalnız rozet
 466 ─ ≈900   HATA        (altında sarı altçizgi)        başlık; boy motor ölçer, üst sınır 190
              ( NEREDE? ) sarı hap
 927 ─ 1000   The train to İzmir          ?              kart satır 1 (taban 986) · ? satır 1'in sağında
1036 ─ 1098   is leave at 7 pm today.                    kart satır 2 (taban 1084)
1107 ─ 1376   saat + tren (sol, 60–490)   figür ≈ 250 (sağ, işaret eder)
1400 ─ 1550   (videoda altyazı; PNG'de boş)
1570 ─ 1920   boş zemin
```

Denetim (sahne kodunda, motor ölçer): satır 2 sağ ucu ≤ 940; figür üstü ≥ 1098 + 24; saat üstü ≥ 1098 + 6; `?` kutusu satır 2 ve başlık
hapıyla çakışmaz; içerik x 60–960.

## 3. `senaryo.json` alanları (kol b, yalnız A)

```json
"giris": {
  "logo": "varlik/logo/yds-publishing.svg",
  "satir1": "HATA",
  "satir2": "NEREDE?",
  "rozetler": ["YDT · BASIC"],
  "sahne": [
    {"ad": "train", "x": 28, "y": 62, "olcek": 0.6},
    {"ad": "clock", "x": 14, "y": 60, "olcek": 0.3},
    {"figur": "ogretmen", "x": 66, "y": 64, "olcek": 0.6}
  ]
},
"meta": {
  "kapak": {
    "satir1": "HATA",
    "satir2": "NEREDE?",
    "canAlici": "is leave → leaves (tarife: V-s)"
  }
}
```

x, y, olcek başlangıç önerisidir; sahne kodu yazılırken kontak sayfasında düzeltilir. Ad değerleri kol a ile aynı (`train`, `clock`);
çizimler kol a `01-hyperframes-kapak` (`_tren_parcalari_svg`, `_saat_svg`); işaret eden figür kol a kapak B (`05-hyperframes-kapak-b`).
