# DUZ3-0202I — `simple-present-ileri-dikey` (dikey tam ders) içerik düzeltmeleri · 16.11.2026

> Ana rapor: `../../simple-present-ileri/uretim-tutanagi/DUZ3-RAPOR.md` (cümle tablosu, gerekçeler, ses, Whisper, kısa video).
> Bu belge yalnız dikey pakete özgü olanı yazar. Üretici: Claude Opus 5.5 (`claude-opus-5-5`). Render yok, commit yok.

| Ölçü | Değer |
|---|---|
| Ses | ana dersle aynı dosyalar: `ortak/anlatim` dizini ana pakete bağdır (`../../simple-present-ileri/ortak/anlatim`); yeniden sentez yok, sha256 eşit |
| Ders süresi | 90,43 → 93,71 sn |
| Yeniden üretilen sahne | 6 (01–06; 02 yalnız künye rozeti) |
| Kapak | değişmedi (`ortak/kapak` ana pakete bağ; kapak "YARIN / WILL mi?" YV-DUZ'da düzeltildi) |
| `youtube.json` | yatayla birebir; `youtube-aciklama.md` tek fark `utm_content=dikey-tam` |
| Çakışma kapısı | çıkış 1 (6 hata, 5 uyarı); hiçbiri değişen öğede değil |

## 1. Dikeye özgü düzeltmeler

| # | Sahne | Önce | Sonra | Gerekçe |
|---|---|---|---|---|
| D1 | 06 çip 1 | `tarife = Simple Present` | `tarife: Simple Present` | "=" denkliği |
| D2 | 06 çip 2 | `will = predictions · sudden decisions` | `will (often): predictions · sudden decisions` | "=" denkliği; ses "We often use will …" |
| D3 | 06 çip 3 | `know · own · cost = no -ing` | `stative know · own · cost: no -ing` | mutlak kural; kapsam "stative" (durum anlamı) |
| D4 | 06 çipler | Fredoka 56 | Fredoka 50 | D2 56 px'te 1058 px (alan 984 px); üç çip aynı boy |
| D5 | 06 | `will` yanında `=` | `will` yanında Caveat `often` (110 px, «for» sözünde) | ses K1 |
| D6 | 06 | `will take off` üstünde kırmızı ✗ | ✗ yok | EK-5a; will take off doğru |
| D7 | 05 | `tomorrow` `≠ will` | `tomorrow` `tuzak` (61,85) | yanlış denklik; ses "Tomorrow tuzaktır." |
| D8 | 04 | el yazısı `durum fiili:` (sözcük: durum, fiilidir) | `durum anlamı:` (sözcük: durum 47,41, anlatır: 47,73) | ses J2 |
| D9 | 03 | formül satırı `zaman değişmez · it gives (V-s)` | `genel gerçek · it gives (V-s)` (30,21 / 30,53) | ses K3 |
| D10 | 01 | kök CSS `1920×1080`, gren `1920×1080` | `1080×1920` (kardeş dikey paketlerle aynı) | açık temada önizlemenin alt yarısı siyahtı, altyazı kırpılıyordu (eski koyu karede görünmüyordu) |
| D11 | 01, 06, künye | `YDT · ADVANCED` | `YDT · İLERİ` | HV-24 |

Zaman: 03 `KARE` 456 → 482; 04 `TBAS` 32,45 → 33,33, `KARE` 487 → 497, p1–p3 +0,88, p4 yeni sözcüklerle; 05 `TBAS`
48,29 → 49,49, sabitler +1,20; 06 sözcük sıraları yeni c7'ye (`zamanlar.json` t_bas 62,61, kare 963). Altyazı (`altyazi.json`)
sahnenin `tbas`ından okunur; sahne saatleri gerçekten kaydırıldı (`kayma` yolu dikey altyazıyı bozardı).

Değişen dosyalar: `zaman.json`, `BRIEF-DIKEY.md`, `ortak/kunye.js`, `youtube.json`, `youtube-aciklama.md`,
`sahneler/01/{uret.py, yardim.py, proje/index.html}`, `sahneler/03/{sahne-03.js, calistir.sh}`, `sahneler/04/{sahne.js, calistir.sh}`,
`sahneler/05/{sahne.js, calistir.sh}`, `sahneler/06/{uret.py, yardim.py, zamanlar.json, calistir.sh, olaylar.json, proje/index.html}`.

## 2. Kareler (kendim baktım)

Komut: `node araclar/sahne-kare.mjs simple-present-ileri-dikey <sahne> <t,…> sahneler/<sahne>/k/duz3 --tema acik --port 41333 --sunucu 41022`.

| Sahne | Anlar (sn) | Gözlem |
|---|---|---|
| 01 | 1,2 · 2,9 | rozet `YDT · İLERİ`; tam boy zemin; altyazı görünür (D10 öncesi alt yarı siyahtı) |
| 02 | 9,0 | rozet aynı |
| 03 | 22,0 · 30,8 · 32,4 · 33,25 | `genel gerçek · it gives (V-s)` tek satır sığıyor; altyazı cümle 3 yeni metin |
| 04 | 36,0 · 48,0 · 49,4 | `durum anlamı:` 412 px kutuya sığıyor (`know` kenara yakın, eskiden de dar); altyazı yeni c4 p4 |
| 05 | 53,0 · 62,4; koyu 62,4 | `tomorrow` `tuzak`; altyazı "Tarife kesin, Simple Present. Tomorrow tuzaktır." |
| 06 | 66,0 · 69,3 · 73,8 · 77,2 · 80,8 · 85,9 · 89,0 · 92,8; koyu 85,9 | ✗ yok; `takes off ✓`; `will often`; üç çip x ≤ 993 px; Kod ve `Next lesson` altyazıya binmiyor |

## 3. Çakışma kapısı

```
$ node araclar/cakisma-kapisi.mjs simple-present-ileri-dikey --port 41333 --sunucu 41022 --json …/kapi-dikey.json   → çıkış 1
01 cg:path0 × cg:text0 (2,75–3,00, hata) · 06 fing × s3:path1/2, rb0/rb1/rb2 × s3:path5 (hata)
04 TR satır kutuları üst üste 18 px (uyarı ×2) · 05 11:00 / takes off × tomorrow, takes off × tuzak 12 px (uyarı ×3)
02, 03: çakışma yok · toplam 6 hata, 5 uyarı
```

Hatalar kasıtlı öğelerdir (halka, `-ing` üstündeki çarpı, `I am knowing` üstündeki kırmızı çizgi). Uyarılar ardışık satırların
kutu payıdır; `tuzak` eski `≠ will` ile aynı yerde ve boyda. Karede okunur.

## 4. Açık kalanlar

Ana raporun §8'i geçerlidir. Dikeye özgü: 03, 04 `olaylar.json`/`zamanlar.json` render yan ürünü (render öncesi `calistir.sh`
yeniler); mp4 bayat; dikey Shorts kararı (YV-DUZ N-4) şefte.

---
Son Güncelleme: 16.11.2026 (DUZ3-0202I oturumu).
