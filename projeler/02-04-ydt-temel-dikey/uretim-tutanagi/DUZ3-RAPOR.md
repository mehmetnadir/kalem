# DUZ3-0204T — `02-04-ydt-temel-dikey`: dersin kendi içerik düzeltmeleri (dikey eş) · 16.11.2026

Girdi: `../02-04-ydt-temel/uretim-tutanagi/juri/DJ-hukum-1611-0019.md` (yatay + dikey ortak hüküm). Cümle tablosu, gerekçeler, ses ve
Whisper ayrıntısı yatay raporda: `../02-04-ydt-temel/uretim-tutanagi/DUZ3-RAPOR.md` §1–§3. Bu rapor dikeye özgü işi yazar.

| Ölçüm | Sonuç |
|---|---|
| Ses | yeniden sentez yok: `ortak/anlatim` → `../../02-04-ydt-temel/ortak/anlatim` bağlantısı; tek kopya (dikey aynı dosyayı okur) |
| Süre | 264,64 → 267,04 sn; `zaman.json` yatayla aynı (yalnız `genislik 1080`, `yukseklik 1920` farklı) |
| Düzeltilen ekran metni | sahne 11 `always → long-term`; sahne 12 blok 3 `time word → clue` / `-yor → trap`; sahne 14 kart "durum" ile; kapak |
| DK-2 (altyazı satırı ≤ 24 karakter) | düzeldi: JS (`ortak/kunye.js`), 7 HyperFrames `yardim.py`, sahne 08 yerel dilim; HyperFrames 78 altyazı satırı, en uzun 24 |
| Yeniden üretilen sahne | 14 sahnenin 14'ü yeniden denetlendi; HyperFrames 7'si (01, 06, 07, 10, 12, 13, 14) yeniden üretildi (koyu tema, depo düzeni) |
| Kapak | değişti: `KALICI mı / GEÇİCİ mi?` (açık + koyu); `uretim-tutanagi/kapak-168.png` ilk kez (KS-6 dikey) |
| Çakışma kapısı | 14 sahne, hepsi çıkış **0** |
| Yayın verisi | `youtube.json` yatayla bayt bayt aynı; açıklama yalnız `utm_content=dikey-tam` farklı |

## 1. Sahneler

| Sahne | Ne yaptım |
|---|---|
| 01, 07, 10, 13 HyperFrames | yeniden üretildi (`ONIZLE_YALNIZ=1 bash calistir.sh --tema koyu`); yerel zaman aynı, fark DUZ2 rozeti + kısa altyazı satırları. 10'da sabit `L(177.40)` → `L(Q(0) - 0.45)` ("Hocam," − 0,45; yerel zaman aynı kaldı) |
| 02, 03 Paper.js | kod değişmedi; altyazı `ortak/kunye.js`'ten 24 karakterle gelir. 03'ün yerel altyazı girdileri 24 karakterle 2 satıra sığar |
| 04 kanvas | `KARE 762 → 779`; cümle 4 içine sabitlenmiş 7 zaman sözcüğe bağlandı (`t(4) + 0,50` kart A; `t(22) − 0,79 … − 0,31` grup küçülmesi, şerit, live, ok, PERMANENT, ev); `calistir.sh` |
| 05, 08, 09 kanvas | `KAYMA −0,56 / −1,68` (yatayla aynı düzen) + `sahne-ortak.js` satır 450: altyazı yeni çerçevede aranır (`zm(f) − kayma`); yoksa altyazı 1,68 sn kayardı |
| 08 kanvas (ek) | sahnenin yerel `altyaziDuzelt()` dilimi: 24 karakter sınırı + zamanlar `S.sozc`'den (eski çerçeve) geldiği için `− S.kayma`. İlk çekimde 3 satırlık uzun altyazı ve 1,68 sn erken altyazı gördüm; düzelttim, yeniden çektim |
| 06 HyperFrames | `T7("kişi") → T7("insanlar")`; `KARE 613 → 646` |
| 11 kanvas | `KARE 657 → 643`, `KAYMA −1,68`; `always → long-term` (not + `(permanent)` konumu); now noktaları `t(10) + 0,32`, `t(14) + 0,42`; `(permanent)` `t(17) + 0,35`; baş sallama `t(32) − 0,44` |
| 12 HyperFrames | blok 3: satır a `time word → clue`, satır b `-yor → trap`; eski satır b `MEANING → decision` kalktı (iki ok + iki hap dikey genişliğe sığmıyor; aynı iddiayı alttaki `MEANING FIRST` taşır); `KARE 463 → 497` |
| 14 HyperFrames | kart "Stative" `T(22, "durum")`; `KARE 431 → 434` |
| 90 kapak | yatayla aynı `uret.py` (bkz. yatay rapor §7) |

DK-2 kararı: istem "altyazı satır uzunluğu"nu gerçek hata saydı; `dikey-senaryo-kalibi.md` tablosu "Satır uzunluğu en çok 24 karakter".
Altyazı 44 px'te kalır (değiştirmedim); dilim 2 satır × ≤ 24 karakter, parça daha sık dilimlenir. Ortak `altyaziSar` (JS) ve
`altyazi_svg` / `altyazi_dilimleri` (Python) aynı kuralla kırar.

## 2. Kareler (kendi bakışım)

Araç: `bash araclar/qa-yerel.sh 02-04-ydt-temel-dikey <sahne> <açık_t…> <koyu_t> --kapisiz` (sahne sahne, tek tarayıcı). Eski `k/`
içeriği `/home/sef/Silinecekler/2026-11-16-duz3-0204T/k-eski/` altında; ara çekimler `k-ara-dikey/`, `k-ara-dikey-08/`.

Kontak sayfaları (`uretim-tutanagi/duz3-kareler/`): `kontak-dikey-acik-degisen-1.png`, `-2.png` (04, 06, 11, 12, 14) ·
`kontak-dikey-acik-1.png`, `-2.png` (14 sahne) · `kontak-dikey-koyu.png` · `kontak-kapak.png`.

Bakış: taşma, çakışma, okunmayan yazı yok. Altyazı her karede en çok 2 satır, satır ≤ 24 karakter, ses ile aynı anda (08 dahil, düzeltme
sonrası). Künye `YDT · TEMEL`; `BASIC` hiçbir karede yok. 11'de `long-term (permanent)` kart içinde; 12'de blok 3 iki satır bandın
içinde; 14'te kart `Next lesson · Stative Verbs`.

| Sahne | Açık (t, sn) | Koyu |
|---|---|---|
| 01-hyperframes-giris | 0.98, 2.45, 2.95 | 2.95 |
| 02-paperjs-kanca | 14.6, 16, 16.25, 16.5, 17, 20.1, 5.6, 6.75 | 16.25 |
| 03-paperjs-ornek1 | 31.85, 38.9, 43.6 | 43.6 |
| 04-canvas-ornek2 | 56.42, 56.7, 57.4, 63.74, 69.2 | 69.2 |
| 05-canvas-ornek3 | 79.96, 84.56, 93.86 | 93.86 |
| 06-hyperframes-soru1 | 105.81, 114.82, 98.16 | 109.48 |
| 07-hyperframes-kural | 125.78, 129.28, 131.88 | 131.88 |
| 08-canvas-karsit1 | 133.18, 138.28, 139.98, 141.28, 142.88, 146.92 | 138.88 |
| 09-canvas-karsit2 | 150.68, 158.28, 163.88 | 163.88 |
| 10-hyperframes-tuzak | 176.48, 178.88, 185.38 | 185.38 |
| 11-canvas-tuzak-cevap | 189.32, 194.05, 195.54, 201.26, 203.21, 204.31, 205.74 | 195.54 |
| 12-hyperframes-ozet | 206.64, 208.15, 211.98, 214.28, 216.77, 221.62, 222.6 | 217.86 |
| 13-hyperframes-mini-soru | 229.52, 236.82, 242.82, 248.22, 253.32 | 242.82 |
| 14-hyperframes-kapanis | 258.48, 262.66, 265.92 | 265.36 |

## 3. Çakışma kapısı

Komut (sahne sahne): `node araclar/cakisma-kapisi.mjs projeler/02-04-ydt-temel-dikey --sahne <sahne> --json
uretim-tutanagi/duz3-kareler/cakisma/<sahne>.json --port 41333 --sunucu 41022`. Altyazı değişikliğinden (kunye.js 01:25) sonra
14 sahne yeniden koştu; 08 yerel dilim düzeltmesinden sonra bir kez daha (01:34).

| Sahne | Çıkış | Örnek | Kutu |
|---|---|---|---|
| 01-hyperframes-giris | 0 | 13 | 88 |
| 02-paperjs-kanca | 0 | 70 | 1951 |
| 03-paperjs-ornek1 | 0 | 96 | 5434 |
| 04-canvas-ornek2 | 0 | 104 | 1698 |
| 05-canvas-ornek3 | 0 | 99 | 1571 |
| 06-hyperframes-soru1 | 0 | 86 | 38038 |
| 07-hyperframes-kural | 0 | 69 | 16053 |
| 08-canvas-karsit1 | 0 | 61 | 660 |
| 09-canvas-karsit2 | 0 | 69 | 1448 |
| 10-hyperframes-tuzak | 0 | 87 | 19647 |
| 11-canvas-tuzak-cevap | 0 | 85 | 1457 |
| 12-hyperframes-ozet | 0 | 66 | 30982 |
| 13-hyperframes-mini-soru | 0 | 125 | 35595 |
| 14-hyperframes-kapanis | 0 | 55 | 7497 |

## 4. Kapak

| Dosya | Ölçü | Not |
|---|---|---|
| `kapak.png` · `kapak-koyu.png` | 1080 × 1920 | `KALICI mı` / kutulu `GEÇİCİ mi?`; S1 140 · S2 168 · karakter ölçeği 0,66 (eski 0,67) |
| `uretim-tutanagi/kapak-168.png` | 168 × 299 | ilk kez (KS-6 dikey önizleme); yazı okunur |

Karakter ve nesne aynı. Üretici değişikliği ve gerekçe: yatay rapor §7 (dikeyde `ValueError` ile duran nesne boyutu).

## 5. Yayın verisi ve tutarlılık kapısı

`youtube.json` yatayla bayt bayt aynı (bölüm 13, bildirim 69,95 ve 186,22). `youtube-aciklama.md` damga bloğu aynı; tek fark
`utm_content=dikey-tam`. Bölüm tablosu: yatay rapor §8.

Tutarlılık kapısı: `python3 uretim-hatti/betikler/yv-tutarlilik.py --kilitli simple-present-temel,simple-present-temel-dikey,02-04-ydt-temel-dikey`
→ **çıkış 1**. `02-04-ydt-temel-dikey`: 0 sorun (`süre 267.04 sn`, bölüm 13). 14 sorunun hepsi `present-continuous*` (başka ders).

## 6. Sürüm notu

`surumler.json` → `revizyonlar` sonuna r3 (`dikey-tam`, `2026-11-15T22:37:00Z`, DUZ3 değişiklik metni).

## 7. Kısa video, dokunulmayan maddeler, açık kalanlar

- Kısa video `02-04-ydt-temel-s1` / `-s1b` "Hep orada" cümlesi: yatay rapor §9 (dokunulmadı).
- mp4 eski (`cikti*.mp4`, sahne `video*.mp4`, `kontrol*.png`, `_is/`): render yasağı; yayından önce şef derlemesi gerekir.
- Kanvas `olaylar.json` (04, 11): render ile tazelenir. HyperFrames `olaylar.json` tazelendi.
- EK-11 dinleme, DK-1, DK-3, ST-2, EK-3, EK-12, EK-4: kanıt yok (yatay rapor §10).
- `BRIEF-DIKEY.md` tablo saniyeleri 15.11 zamanlarıdır (belgeye not düşüldü).
- git commit yok (şef atar). Yeni dosyalar: bu rapor, `uretim-tutanagi/kapak-168.png`, `uretim-tutanagi/duz3-kareler/`.
