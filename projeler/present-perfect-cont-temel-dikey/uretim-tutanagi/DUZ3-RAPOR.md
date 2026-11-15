# DUZ3-0209T — `present-perfect-cont-temel-dikey` (9:16) dersin kendi içerik düzeltmeleri · 16.11.2026

> Ana rapor (cümle tablosu, gerekçeler, Whisper, kısa video bulgusu): `../present-perfect-cont-temel/uretim-tutanagi/DUZ3-RAPOR.md`.
> Bu dosya dikey pakete özgü işi yazar. Makine srv21. Render yok, mp4 yok, commit yok.

## 1. Ses

`ortak/anlatim` bu pakette ana paketin `ortak/anlatim` dizinine göreli bağdır (`readlink -f` = ana paket). Ses, `sozcukler.json`, `altyazi.json`,
`METIN.md` tek dosyadır; sha256 kendiliğinden eşit (`anlatim.wav` `9ec3ab880004`, `anlatim.m4a` `30697c0471f2`). Kopya gerekmedi, yeniden sentez yok.

## 2. Değişen dosyalar

| # | Konu | Dosya | Değişiklik |
|---|---|---|---|
| 1 | Zaman | `zaman.json` | 02: 580 kare, 3,00–21,93 · 03: 21,93–37,08 (467 kare aynı) · 04: 37,08–52,47, 474 kare · 05: 52,47–66,87, 444 kare · 06: 66,87–88,58 (681 kare aynı) |
| 2 | Sahne 02 | `sahne-02.js`, `calistir.sh` | c2 yeni sözcük zamanları; 15,64'te sağ grup toplanır, ajanda kartı 15,77; İngilizce cümlede 3 daire sese bağlı (9,54 `for two hours` yeni · 12,74 `have been` · 14,34 `-ing`); `N=580`. Dikeyde denklik oku yoktu |
| 3 | Sahne 03 | `sahne-03.js` | `kayma: -4.8`, `tGercek: 21.93` (altyazı gerçek zamanda) |
| 4 | Sahne 04 | `sahne.js`, `sahne-ortak.js`, `calistir.sh` | 474 kare, `kayma: -4.8`; Türkçe pencere 37,65; `has` halkası 45,59 ve formül 45,59 / 46,71 / 46,95 / 47,19 (eski çerçeve); altyazı zamanı `zm(f) - kayma` |
| 5 | Sahne 05 | `sahne.js`, `sahne-ortak.js`, `calistir.sh` | 444 kare, `kayma: -5.2`; ekran `Yağmur yağıyormuş.`; `izi şimdi` / `görünüyor` 56,12 / 56,64–57,92; formül 58,07; halkalar 59,67 / 59,99 / 61,19; altyazı `zm(f) - kayma` |
| 6 | Sahne 06 | `zamanlar.json`, `uret.py`, `nesneler.json`, `yardim.py` → `proje/index.html`, `olaylar.json` | gerçek çerçeve t_bas 66,87; `-dir … -yor ⇄ have been … -ing` grubu kalktı, yerine Caveat `süre:` + Fredoka 107 `for / since` (77,00 / 78,04 / 79,00); toplanma 79,96; künye rozeti `YDT · TEMEL` |
| 7 | Sahne 01 | `uret.py`, `yardim.py`, `nesneler.json` → `proje/index.html` | rozet `YDT · TEMEL` (HV-24) |
| 8 | Künye | `ortak/kunye.js` | `rozet: "YDT · TEMEL"` (02–05 çalışma anında çizer) |
| 9 | Kapak | `sahneler/90-hyperframes-kapak/proje/index.html`, `nesneler.json`, paket kökü `kapak.png`, `kapak-koyu.png` | ana paket üreticisiyle (`--duzen dikey`): `İKİ SAATTİR` / `NASIL DENİR?` + `I have been working for two hours.` (43 px; karaktere değmeyene dek küçüldü) |
| 10 | Yayın verisi | `youtube.json`, `youtube-aciklama.md` | ana paketle aynı zamanlar (`cmp` eşit; açıklamada yalnız `utm_content=dikey-tam` farkı önceden vardı) |
| 11 | Belge | `BRIEF-DIKEY.md` | rozet `YDT · TEMEL`; sahne 06 satırı `süre: for / since` |

## 3. Kareler (kendim baktım; dizin `sahneler/<sahne>/k/duz3/`, git dışı)

| Sahne | Anlar (sn) | Gözlem |
|---|---|---|
| 01 | 1,2 · 2,9 | hap `YDT · TEMEL`; altyazı `İki saattir çalışıyorum.` |
| 02 | 5,6 · 9,6 · 12,9 · 14,6 · 17,2 · 21,5 | daireler sesle; altyazı `İngilizcede süreyi for ya da since söyler, …` 2 satır; kart 17,2'de yazılıyor |
| 03 | 23,0 · 31,0 · 36,5 | altyazı `For twenty minutes.` 31,0'da (kayma doğru) |
| 04 | 38,6 · 44,6 · 47,6 · 50,6 · 52,3 | altyazı `Başlangıç noktası. Üçüncü tekil kişide has been, artı -ing.` 2 satır; formül sesle |
| 05 | 54,6 · 57,2 · 60,5 · 62,4 · 65,3 · 66,7 (+ koyu 62,4) | `Yağmur yağıyormuş.`; altyazı yeni metin |
| 06 | 69,5 · 72,8 · 75,2 · 77,6 · 79,6 · 80,6 · 82,0 · 84,2 · 86,2 · 88,3 (+ koyu 79,6) | `süre: for / since` toplanmadan önce y 1030, sonra küçük; cümle, köprü, kart okunur; altyazı 2 satır (son parça `-ing.` ikinci satıra iner; metin değişmedi, eskisi de böyleydi) |
| kapak | açık + koyu | taşma yok, yazı karaktere binmiyor, üst ve alt %20 boş |

## 4. Çakışma kapısı

```
$ node araclar/cakisma-kapisi.mjs present-perfect-cont-temel-dikey --port 41333 --sunucu 41022 --json ~/is/duz3-0209T/kapi-dikey.json
03: çakışma yok
01: kunye:ku-rz × t1 (2,50 sn, giriş uçuşu) hata
02: Bu derste: × cizgi, cizgi × time expressions hata; 2 saat önce × result clue uyarı (16,50–21,93)
04: Kardeşim … × nota (4 aralık), kardes × since, gitar × since hata; has been × since uyarı
05: bulut × has been + V-ing hata
06: row0 × row1 (72,12, toplanma) uyarı; tr2 parça renkleri uyarı
→ çıkış 1
```

Değerlendirme: bu işte hiçbir öğenin konumu değişmedi; yalnız zamanlar kaydı (04 ve 05'te kayma, 02'de toplanma 10,6 → 15,64, kart 10,73 → 15,77,
aynı sıra). 02'deki `cizgi` zaman çizgisidir; 15,64'te ölçeklenip kartın altına taşınır, kapı dönüşümden önceki kutuyu ölçer (karede çizgi kartın
altında, bkz. 17,2 ve 21,5 kareleri). 01'deki hap 5,5 px genişledi (`BASIC` → `TEMEL`); kesişim 246×8 px dikey uçuş kesişimidir. Eski hâlin
kapısını yeniden koşmadım; bu satırlar konum değişmediği için önceden var sayıldı, doğrulanmadı.

---
Son Güncelleme: 16.11.2026 (DUZ3-0209T oturumu).
