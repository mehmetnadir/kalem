# DUZ3-0206I — `present-perfect-ileri-dikey` (1080×1920) · 16.11.2026

> Bu belge yalnız dikeye özgü işi yazar. Cümle tablosu, ses, Whisper, kapak gerekçesi ve kısa video bulgusu ana paketin raporundadır:
> `../../present-perfect-ileri/uretim-tutanagi/DUZ3-RAPOR.md`. Render yok, mp4 yok, commit yok, alt ajan yok, silinen dosya yok.

| Ölçü | Değer |
|---|---|
| Ses | ana paketle ortak: `ortak/anlatim` → `../../present-perfect-ileri/ortak/anlatim` (sembolik bağ); ders 93,77 → 98,29 sn |
| Düzeltilen cümle | ana paketle aynı 5 parça (jüri 3 + kendi bulgum 2) |
| Yeniden üretilen sahne | 5 (01, 02, 03, 06, kapak) + 2 kayma (04, 05) |
| Kapak | değişti: `AGO VARSA / SIMPLE PAST`, küçük satır `ago → took off` (açık + koyu) |
| Çakışma kapısı | 01–04 çıkış 0 · 05 çıkış 1 (eski yerleşim, §4) · 06 çıkış 1 (yalnız bilinçli çarpı çiftleri) |
| Dikeyde bulunan eski hata | 2 düzeltildi: sahne 01 kökü 1920×1080 (alt yarı siyah); sahne 04–05 altyazısı kaymalı çerçevede |

## 1. Dosyalar

| Dosya | Değişiklik |
|---|---|
| `zaman.json` | ana paketle aynı: 02 kare 473 · 03 kare 526, 18,37 · 04 35,49 · 05 52,85 · 06 kare 873, 70,20–98,29 |
| `youtube.json`, `youtube-aciklama.md` | ana paketle aynı zamanlar (bölüm 0 / 18,37 / 35,49 / 52,85 / 70,2; bildirim 36,04; damga 00:00 / 00:18 / 00:35 / 00:53 / 01:10); yalnız `utm_content` farklı. İki dosya git'te izlenmiyor (YV oturumundan); şef ekler |
| `BRIEF-DIKEY.md` | iddia satırları (c1, c6, rozet, `yasak`) düzeltildi; başa DUZ3 notu |
| `ortak/kunye.js` | `seviye: "YDT İLERİ"` (HV-24) |
| `sahneler/*/calistir.sh` | 02 `N=473`, `GLOBAL_SN="4.9 11.9 15.2"`, başlık 431 → 473 · 03 `N=526`, `TBAS=18.37` · 04 `TBAS=35.49` · 05 `TBAS=52.85` · 06 `KARE=873`, `TBAS=70.20` |

## 2. Sahneler

| Sahne | Değişiklik | Neden |
|---|---|---|
| 01 giriş | `uret.py` rozet `YDT · İLERİ`; altyazı artık `sozcukler.json` cümle 1'den (`ALT_METIN`; eski sabit metin `Ago varsa Present Perfect yok.` kalırdı) | HV-24, c1 |
| 01 giriş `yardim.py` | `W, H = 1080, 1920`, gren ve kök `#root` 1080×1920, vinyet 1300 px (eski: 1920×1080 kök → karenin alt yarısı siyah; HEAD'de de vardı, kardeş dikey paketlerle eşitlendi) | önceden var olan hata; karede görüldü |
| 02 kanca | c1 sözcükleri `Ago varsa, fiil Simple Past.` (satır 0 / 1); c2 zamanları +0,4; `KARE` 473 | c1 metni, c1 +0,4 sn |
| 03 kök 1 | sözcük çapalı zaman eşlemesi (`~/is/duz3-0206I/esle.py`); `KARE` 526, `T_BAS` 18,37; formül kartında `Simple Past` yazısının sağına soluk `çoğu zaman` (Caveat 48, `x: a3.x1 + 28`, `y: 1312`) | c3 yeni ses + EK-5b |
| 04, 05 | `sahne.js` `kayma: -1.6`; `sahne-ortak.js` altyazı `zm(f) - kayma` (kayma olmadan altyazı 1,6 sn erken cümleyi gösterirdi) | c1 + c3 kayması |
| 06 soru + kural | balon `Hocam, took off yerine` / `has taken off diyemez miyiz?` (Caveat 76, sözcük 0–3 / 4–8); sarı belirteç `took off`; kırmızı çarpı `has taken off`; A2 satırı `fiil → Simple Past` (üstü çizili `Present Perfect` ve çizgiler kalktı); kod kartı KF 64 + soluk `çoğu zaman` (Caveat 52, sığma assert'i); iskelet c6 başı + 0,85 / 1,2 / 1,45 / 1,7 sn; `yardim.py` `ROZET` `YDT · İLERİ`; `zamanlar.json` 70,2 / 873 / 29,1 / 843 | c6, c7 yeni metin + HV-24 |
| 06 toplanma | `#balg` ölçeklemesi `tr − 0,32` → `tr − 0,5` (c6 bitişi `tr − 0,59`) | kapı `bas × hay` (§4) |
| 90 kapak | dikey sarmalayıcı `calistir.sh` (+ `--tema koyu`) ana paketin `uret.py`'sini kullanır; `nesneler.json`, `proje/index.html` yeniden | ana rapor §5 |

## 3. Kareler (kendim baktım)

Komut: `node araclar/sahne-kare.mjs present-perfect-ileri-dikey <sahne> <t,…> <dizin> --tema acik --port 41333 --sunucu 41022`;
dizin `sahneler/<sahne>/k/duz3/` (git dışı), koyu örnekler `k/duz3/koyu/`.

| Sahne | Anlar (sn) | Gözlem |
|---|---|---|
| 01 | 1,2 · 2,2 · 2,9 | kök düzeltmesinden sonra tam tuval; hap `YDT · İLERİ`; c1 sözcük sözcük; altyazı yeni c1 |
| 02 | 3,4 · 15,2 | c1 iki satır, `Ago` kırmızı çizgi; formül ve `V3 = past participle` |
| 03 | 21,3 · 32,3 · 33,6 · 35,4 (+ koyu 35,4) | `çoğu zaman` `Simple Past` yazısının sağında, kart kenarına değmez; `Present Perfect` 34,53 |
| 04 | 39,6 | `for thirty years`; altyazı c4 ile eş |
| 05 | 66,4 | `ago → Simple Past` kartı; altyazı c5 ile eş |
| 06 | 73,9 · 76,9 · 80,6 · 86,6 · 97,4 (+ koyu 97,4) · 75,1 / 75,45 / 75,55 (toplanma) | balon iki satır, çarpı `has taken off` üstünde; `fiil → Simple Past`; kod kartı iki satır + `çoğu zaman` + tik; 75,45'te baş yukarıda, `Hayır.` 75,42'de başlar |

## 4. Çakışma kapısı

```
$ node araclar/cakisma-kapisi.mjs present-perfect-ileri-dikey --sahne <sahne> --port 41333 --sunucu 41022 --json …
01-hyperframes-giris  rc 0 — çakışma yok (13 örnek, 2262 kutu)
02-paperjs-kanca      rc 0 — çakışma yok (63 örnek, 1810 kutu)
03-paperjs-ornek1     rc 0 — çakışma yok (70 örnek, 4808 kutu)
04-canvas-ornek2      rc 0 — çakışma yok (71 örnek, 1541 kutu)
05-canvas-ornek3      rc 1 — saat × took off (61,35–70,20; 125×6 px) · ucak × → Simple Past (65,85–70,20; 38×6 px)
06-hyperframes-form   rc 1 — 1. koşu: bw4/bw5/bw6 × xk1/xk2 (6) + bas:path0 × hay (75,45, tek örnek, 7×15 px)
06-hyperframes-form   rc 1 — 2. koşu (toplanma tr − 0,5): yalnız bw4/bw5/bw6 × xk1/xk2 (6)
```

Kayıt: `~/is/duz3-0206I/kapi-present-perfect-ileri-dikey-<sahne>.{json,log}` (06 2. koşu `…-r2.{json,log}`), özet `kapi-ozet.txt`.

1. 05: içerik değişmedi. Saat (x 60, y 832, 160 px), `took off` etiketi ve uçak kutusu sabit konumdadır; kayma yalnız zamanı taşır.
   Çiftler eski yerleşimden gelir (6 px yükseklik: çizim kutusu ile yazı kutusunun kenarı). Düzeltmek için yerleşim değişmeli; bu işin kapsamı
   dışında bıraktım (§5).
2. 06 `bw × xk`: kırmızı çarpı ile çarpılan `has taken off` arasındadır; bilinçlidir (eski sürümde `has landed` × çarpı aynı sınıftı).
3. 06 `bas × hay`: öğrenci başı yukarı toplanırken `Hayır.` yazılmaya başlıyordu (eski sürümde de aynı göreli zamanlama vardı: 73,30 / 73,62).
   Toplanmayı c6 bitişinden hemen sonraya çektim; 2. koşuda çift yok.

## 5. Açık kalanlar

| Madde | Sebep |
|---|---|
| 05 `saat × took off`, `ucak × → Simple Past` | eski yerleşim, içerik değişmedi; ince kenar teması; yerleşim kararı şefte |
| mp4 ve `olaylar.json` (02–05) bayat | render yasak; `calistir.sh` güncel kare sayısında |
| EK-11 kulak dinlemesi, YVJ / kapak jürisi yeniden | ana rapor §9 |
| `youtube.json`, `youtube-aciklama.md` git'te izlenmiyor | YV oturumundan; commit şefin |

---
Son Güncelleme: 16.11.2026 (DUZ3-0206I oturumu).
