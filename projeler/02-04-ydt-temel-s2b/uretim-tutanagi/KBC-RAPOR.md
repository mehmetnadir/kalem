# KBC-0204S2 raporu — `02-04-ydt-temel-s2b` kol b paketi · değişken `kapanis` · 15.11.2026

| Ölçüm | Değer |
|---|---|
| Değer (a → b) | `kaydet` (`Bu kuralı kaybetme. Kaydet.` + `Bitmedi, gel.`) → `ekran-goruntusu` (`Ekran görüntüsü al, sınav günü bak.` + `Konu burada bitmiyor.`) |
| Süre (a → b) | 29,41 → 29,49 sn (+0,08; taslak tahmini 30,22). Kabul ≤ 35 sağlandı; hedef 22–26 iki kolda da aşıldı |
| Yeni sentez | 2 cümle, 4 parça, 133 karakter (≈ 0,65 TL); 6 parça önbellekten |
| Whisper | 10 / 10 parça 1,00 (en düşük 1,00); ilk söz 1,00 sn; marka sese `YeDeSe` (ses sözlüğü) |
| Tek değişken | `diff -rq` 81 satır; beklenmeyen fark 0 |
| Kapı | `cakisma-kapisi.mjs 02-04-ydt-temel-s2b --port 41333 --sunucu 41022` çıkış 0 (4 sahnede çakışma yok) |
| Üretici model | Claude Opus 5.5 (`claude-opus-5-5`); jüri farklı modelle koşmalı |
| mp4 | yok (render koşulmadı) |

## 1. Kopya (adım 1)

- `cp -a` kol a → kol b, `uretim-tutanagi/` hariç. Kopya sonrası: 284 = 284 öğe (dosya + bağ); `diff -rq` boş.
- Git dışı 87 varlığın sha256'sı iki pakette eşit, fark 0: png 50, pyc 14, js 7 (`gsap.min.js`), wav 6, json 4, hyperframes kimliği 4,
  m4a 1, imza 1. Yazı tipleri git içinde, `diff` ile aynı.
- Kol a `ortak/{cizim,font,logo,hf_tema.py}` simge bağıdır (`../../present-continuous/ortak/…`); `logo/` içinde de 1 bağ var.
  `cp -a` bunları bağ olarak taşıdı. Simge bağı yasağı nedeniyle bağları `~/Silinecekler/2026-11-15-kol-b/02-04-ydt-temel-s2b/ortak-baglar/`
  altına taşıdım; yerine hedefin `cp -a` kopyasını koydum (iç bağ yerine hedef dosyanın kopyası). Kol b'de bağ 0. `diff` içerik aynı.

## 2. Değişen dosyalar

| Dosya | Değişiklik |
|---|---|
| `ortak/anlatim/senaryo.json` | yalnız cümle 3 parça 2 ve cümle 4 parça 1 (+ iki `metin` alanı). Kadro, sesler, meta aynı |
| `ortak/anlatim/` türevleri | `sentez.wav`, `.rapor.json`, `cumle-3.wav`, `cumle-4.wav`, `sureler.json`, `sozcukler.json`, `baslar.json`, `anlatim.wav/.m4a/.imza`, `altyazi.json`, `METIN.md` |
| `zaman.json` | sahne 08: 172 → 175 kare, t_son 22,75 → 22,83; sahne 03: t 22,83–29,49. Sahne 01–02, hikâye, durağan aynı |
| `sahneler/08-hyperframes-kaydet/` | `uret.py` (vizör + 3 parça kalıp), `cizim/vizor.svg` (yeni, elle), `calistir.sh` (kare 175, başlık), `proje/index.html`, `zamanlar.json`, `olaylar.json`, `k/` (yeni QA kareleri) |
| `sahneler/03-hyperframes-cta/` | `uret.py` (giriş `Konu burada` · `bitmiyor.` Fredoka 700 88), `calistir.sh` (başlık), `proje/index.html`, `zamanlar.json`, `olaylar.json`, `k/` |
| `surumler.json` (kol b) | `s2b` kısa satırı + `varyant {s2, b, kapanis, ekran-goruntusu}`; `s2b-aciklama-a/b`; kapak ve hikâye satırları çıktı |
| `aciklama-a.md`, `aciklama-b.md`, `aciklama.md` | yalnız `utm_content` (`s2-a` → `s2b-a`, `s2-b` → `s2b-b`): dosya başına 5 bağ + 1 tablo satırı |
| Kol a `surumler.json` | yalnız `s2` satırına `varyant {s2, a, kapanis, kaydet}` (`git diff`: +7 / −1) |
| Taşınan (Silinecekler) | kol b kökü `kapak{,-a,-b,-c}.png`, `hikaye{,-a,-b}.png` (grup türevi); 08 ve 03 `k/` içindeki kol a QA kareleri; 4 + 1 simge bağı. Liste: `~/Silinecekler/2026-11-15-kol-b/LISTE.md` |
| Paket dışı | `K/.claude/docs/sozlesme.md` 1 satır |

## 3. Ses tablosu

Önbellek anahtarı = el.py (metin, dil, cümle içi önceki/sonraki parça, ses, model, tohum, hız `[1.0, 0.9]`). sha256 = önbellek wav'ı (ilk 12).

| Parça | Ses | Metin | Kaynak | sha256 a | sha256 b | Whisper |
|---|---|---|---|---|---|---|
| 1.1 | …4fwc | Genel mi, şu an mı? | önbellek | 0dcd2f3bc03a | 0dcd2f3bc03a | 1,00 |
| 2.1 | …4fwc | She wears her coat in the winter. | önbellek | e1229ade1b32 | e1229ade1b32 | 1,00 |
| 2.2 | …4fwc | Genel durum: geniş zaman. | önbellek | 0409d4fcd378 | 0409d4fcd378 | 1,00 |
| 2.3 | …4fwc | She is wearing her pink T-shirt today. | önbellek | d66d91172a06 | d66d91172a06 | 1,00 |
| 2.4 | …4fwc | Today iki zamanda da geçebilir; farkı anlam yapar. | önbellek | db3469551a2e | db3469551a2e | 1,00 |
| 2.5 | …4fwc | Konuşma anı: şimdiki zaman. | önbellek | b606e6c3016f | b606e6c3016f | 1,00 |
| 3.1 | …4fwc | Bu, üç farktan yalnız biri. | yeni (komşu parça değişti) | 644b5df847b9 | 993ddb49bee2 | 1,00 |
| 3.2 | …4fwc | Ekran görüntüsü al, sınav günü bak. | yeni | b82632ab01d8 | 753bec96d60f | 1,00 |
| 4.1 | …9gjY | Konu burada bitmiyor. | yeni | 9dcd4e7c4a8c | 76f803a33785 | 1,00 |
| 4.2 | …9gjY | Dersin tamamı YDS Publishing YouTube kanalında. | yeni (komşu parça değişti) | 56e15792f1d4 | 2f2e6595e1ea | 1,00 |

Cümle dosyaları: `cumle-1.wav` 0b0dafd59a98 = 0b0dafd59a98 · `cumle-2.wav` 1d805b981216 = 1d805b981216 · `cumle-3.wav` 720b3d7cc552 → 597582d3ddfd ·
`cumle-4.wav` b192db36b66b → 8f69da650730. Whisper metni: `Bu üç farktan yalnız biri.` · `Ekran görüntüsü al, sınav günü bak.` · `Konu burada bitmiyor.` ·
`Dersin tamamı YEDESE Publishing YouTube kanalında.` (kıyas ses metniyle). Çağrı öğrenci sesiyle (…9gjY). Günlük: `ses-sentez-kolb.log`.

## 4. Süreler (kol a ↔ kol b)

| Öğe | Kol a | Kol b | Fark |
|---|---|---|---|
| Cümle 1 / 2 | 1,00–2,84 / 3,39–17,41 | aynı | 0 |
| Cümle 3 parça 2 (kaydet kalıbı) | 2,48 | 2,56 | +0,08 |
| Cümle 4 parça 1 (çağrı girişi) | 1,44 | 1,44 | 0 |
| Cümle 3 / 4 | 17,96–22,75 / 23,30–28,41 | 17,96–22,83 / 23,38–28,49 | +0,08 kayma |
| Sahne 08 kaydet | 17,41–22,75 (5,34 sn, 172 kare) | 17,41–22,83 (5,42 sn, 175 kare) | +0,08 |
| Sahne 03 çağrı | 22,75–29,41 (6,66 sn, 230 kare) | 22,83–29,49 (6,66 sn, 230 kare) | 0 (kayma) |
| Toplam (`anlatim.m4a` ffprobe) | 29,41 | 29,49 | +0,08 |

Sahne 08 çapaları (küresel): kart `Bu,` 17,96 · üç nokta `üç` 18,48 (kol a 18,52; yeniden sentez) · vizör köşeleri `Ekran` 20,27 (`cizgi`) ·
`Ekran görüntüsü` 20,27 · deklanşör + `al,` + Today hapı → çerçeve 21,35 (`tik`) · `sınav günü bak.` 21,79 · kuyruk 22,84. Ses olayı türü ve sayısı kol a ile aynı
(vurus · tik · cizgi · tik). Sahne 03: `Konu burada` 23,38 · `bitmiyor.` 24,14 · kapak 24,97 · hap 26,25 · YouTube 27,37 (yerel çapalar kol a ile aynı: 0,55 · 2,14 · 3,42 · 4,54).

## 5. Fark sınıflama (`diff -rq` → `diff-rq.txt`)

| Sınıf | Satır | Beklenen mi |
|---|---|---|
| Değişen sahne klasörü (08, 03: üretici, çalıştırıcı, `proje/index.html`, zamanlar, olaylar, `cizim/vizor.svg`, QA kareleri) | 35 | evet |
| `uretim-tutanagi/` | 21 | evet |
| Zaman ve ses türevi (`zaman.json`, altyazı, başlar, sözcükler, süreler, METIN, sentez + rapor, anlatım wav/m4a/imza) | 11 | evet |
| Çıkarılan grup türevi (kapak ×4, hikâye ×3) | 7 | evet |
| Açıklamada utm | 3 | evet |
| Yeni ses (`cumle-3.wav`, `cumle-4.wav`) | 2 | evet |
| Senaryo | 1 | evet |
| `surumler.json` | 1 | evet |
| **Beklenmeyen** | **0** | — |

Sahne 01, 02, 04–07 ve `ortak/` (anlatım dışı) için fark satırı yok: değişmeyen sahnelerin `proje/` içeriği bayt bayt aynı.
Türevlerin içinde de cümle 1–2 aynı: sözcükler, süreler, başlar, sentez raporu parça 1–6, altyazı parça 1–7, `zaman.json` sahne 1–2 ve öteki alanlar.

## 6. Kapı ve kareler

- Çakışma kapısı: `01` 13 örnek · `02` 60 · `08` 23 · `03` 28; çakışma 0; çıkış 0 (`kapi-cikti.txt`, `kapi.json`).
- QA kareleri (açık + koyu; Read ile baktım): 08 `k/` 17,41 · 20,50 · 21,20 · 21,70 · 22,40 · 22,82, `k/koyu/` 17,41 · 21,70 · 22,82;
  03 `k/` 22,83 · 24,00 · 24,60 · 26,80 · 29,48, `k/koyu/` 22,83 · 24,60 · 29,48; ilk kare `kare/01-hyperframes-kapak-0.png`, orta `kare/02-paperjs-ornek-10.png`.
  Taşma, çakışma, okunmayan yazı yok. Vizör 20,50'de çiziliyor, 21,70'te dolu; Today hapı çerçeveye döndü (tek sarı vizörde). Satır sağ uçları 923,5 ve 781,8; çağrı girişi 943,8 (≤ 960).
- Kanal katmanı: mürekkep maskesi HyperFrames sahnelerinde aynı kutu x 61–595, y 296–339; kol b 08 maskesi kol a 08 ile birebir (aynı 7.838 piksel).
- Metin taraması: `Tam ders` 0; `dakika`/`dk` yalnız çalıştırıcı yorumlarında (kol a ile aynı). Emoji 0 (yeni HTML, senaryo, altyazı, açıklamalar). mp4 0.
- Önizleme: `http://127.0.0.1:41022/p/02-04-ydt-temel-s2b/onizle.html` 200.

## 7. Açık noktalar

1. **Süre.** 29,49 sn; hedef 22–26 iki kolda da aşılır. Kısaltma iki kola ortak yapılmalı (BK-RAPOR (e) 1, önerisi [2]).
2. **Mutlak yol.** Sahne 02 (`sayfa.html`, `sahne-02.js`, `kalem-paper.js`) ve `ortak/kunye.js` `KOK` kol a'yı `/projeler/02-04-ydt-temel-s2/…` ile yükler.
   Bayt aynılığı (AB-3) için değiştirmedim. Kol b tek başına taşınırsa sahne 02 kırılır; kol a'daki sonraki değişiklik kol b'ye sızar.
3. **HV-13.** Madde "yer imi + Kaydet" der; kol b değişken gereği vizör + `Ekran görüntüsü al, sınav günü bak.` taşır. Jüri bu maddeyi değişkene göre okumalı.
4. **Açıklama ilk satırı** `Sınav günü bakmak için kaydet.` grup türevidir; kol b videosundaki kalıpla söz farkı var (BK-RAPOR (e) 7).
5. **Ölçü yanlılığı.** Ekran görüntüsü platform kaydetme sayacına yazılmaz (BK-RAPOR (e) 2).
6. **Belge.** 08 ve 03 `SPEC.md`, `RAPOR.md` kol a belgesi olarak kaldı; kol b tanımı `senaryo-taslak.md` + bu rapor.
7. **`meta.kimlik`.** `senaryo.json` `meta.kimlik` = `02-04-ydt-temel-s2` kaldı (istem: başka alan değişmez). Panel bu alanı okuyorsa `…-s2b` olmalı; karar şefte.
8. **Türev üreticileri.** Sahne 04–07 ve `zaman.json` `hikaye`/`duragan` kopya olarak duruyor (fark yok); png çıktıları taşındı. Bu klasörlerde `calistir.sh` koşulursa png kol b köküne yeniden yazılır.
9. **Paper.js kanal katmanı.** Sahne 02'de katman kutusu 3 px geniş (x 61–598, maske farkı 985 piksel). Kol a ile aynı; kol b değiştirmedi.
10. **Kulak.** Yeni iki söz Whisper 1,00; Nadir dinlemedi (EK-11). `hyperframes check` koşulmadı (istem kapısı çakışma kapısı; emsalde de yok).
11. **Altyazı yolu.** Zincirde önce `araclar/altyazi_uret.py` koştu, 9 parça çıktı (`T shirt` parçası kaydı). Kol a'nın yolu olan paket içi `ortak/anlatim/altyazi_uret.py projeler/<paket>` ile yeniden ürettim: 10 parça, ilk 7 kol a ile aynı (günlükte iki koşu da var).
12. **Düzenleme yolu.** Yazma boyutu kancası 15 satırdan uzun Edit'i kesti. Sahne 08'i küçük Edit'lerle yazdım. Sahne 03 üreticisini ve iki çalıştırıcı başlığını kesin dizge değiştiren kısa Python betiğiyle yazdım (her değişiklik ≤ 5 satır).
13. Kol a `uretim-tutanagi/juri/J2-hukum.md` başka bir oturumun dosyası (izlenmiyor); bu iş dokunmadı.
