# İstem S3-C raporu — 02-04-ydt-temel-s3 paket + ses + zaman + sahne istemleri + açıklama · 15.11.2026

| Ölçüm | Değer |
|---|---|
| Ses kapısı (faster-whisper turbo, eşik 0,85) | 7 / 7 parça geçti; en düşük 0,90 |
| Anlatım | 26,56 sn (`anlatim.m4a` ffprobe 26.560000; imza `5bd492a3…` aac-96k-48000-mono). Hedef 24–28 sn: içinde |
| Cümle başı–bitişi (küresel sn) | 1: 1,00–6,45 · 2: 7,00–10,76 · 3: 11,51–15,99 · 4: 16,54–25,56 · kuyruk 1,0 |
| Sahneler | 01 0,00–3,00 (102 kare) · 02 3,00–15,99 (402) · 03 15,99–26,56 (347) · durağan 4 kare zaman dışı |
| ElevenLabs | 140 karakter (≈ 0,69 TL), yalnız `araclar/ses-sunucu.sh` (kayit vekili); 4 / 7 parça önbellekten (ücretsiz) |
| Jüri maddeleri | 8 / 8 işlendi (`S3-duzeltme.md`; dil 2 = kaynak 1, 7 satır) |

Yapılmayan (istem kuralı): render, sahne kodu, git commit, Claude alt ajanı, kanca atlama bayrağı. Silinen dosya yok (geçici istem verisi
`/tmp/s3c-istem-veri.txt` → `~/Silinecekler/2026-11-15-0204/s3c/`). Yazma yalnız `projeler/02-04-ydt-temel-s3/` altında.

## 1. Yazılanlar

| Dosya | İçerik |
|---|---|
| `uretim-tutanagi/senaryo-taslak.md`, `kapak-taslak.md`, `hikaye-taslak.md`, `aciklama-taslak.md` | jüri düzeltmeleri |
| `uretim-tutanagi/S3-A-RAPOR.md` | yalnız ek bölüm §5 (S3-C eki) |
| `uretim-tutanagi/S3-duzeltme.md` | madde → yapılan → kanıt; uygulanmayan / Nadir kararı tablosu |
| `gorevler.json`, `yorumlar.json`, `harita-konum.json` | S1'den kopya (boş) |
| `ortak/` bağları `cizim`, `font`, `hf_tema.py`, `logo` | `../../present-continuous/ortak/…` (S1 ile aynı) |
| `ortak/kalem-canvas.js`, `tema_damga.py`, `tema.sh` | S1'den kopya (değişiklik yok) |
| `ortak/kunye.js` | S1 kopyası; yalnız `KOK` (`/projeler/02-04-ydt-temel-s3/ortak`) ve `cipler` (7 klasör) değişti |
| `ortak/anlatim/senaryo.json` | S1 şeması; `sesler` öğretmen + öğrenci (ana ders), `kadro.ogretmen` (S1) + `kadro.ogrenci` (ana ders), 4 cümle, `giris` (kapak A), `meta` (kod `ING-YDT-GR-02-04-T-S3`); rakam yok |
| `ortak/anlatim/sozcuk_uret.py`, `metin_uret.py`, `kur.py` | S1 kopyası (değişiklik yok) |
| `ortak/anlatim/zaman_uret.py` | S1 kopyası; Edit: sahne 02 `02-hyperframes-ornek` (son cümle 3), sahne 03 son cümle 4, `hikaye` = `hikaye-a.png`, `duragan` listesi (05, 06, 07) |
| `ortak/anlatim/` üretilen | `cumle-1..4.wav`, `sentez.wav` (+ `.rapor.json`), `sureler.json`, `sozcukler.json` (54 sözcük), `baslar.json`, `anlatim.wav`, `anlatim.m4a` (+ `.imza`), `altyazi.json` (7 parça), `METIN.md` |
| `zaman.json` | 3 sahne + `hikaye` (A) + `duragan` (kapak B, kapak C, hikâye B), ikisi de `sahneler[]` dışında |
| `BRIEF-S3.md` | çıktı, kaynaklar, sahne tablosu (7 klasör), ölçülen sözcük çapalı sahne içeriği, kapak A/B/C ve hikâye A/B tarifi, çalıştırma |
| `aciklama-a.md`, `aciklama-b.md`, `aciklama.md` (= A, `cmp` aynı) | YouTube / Instagram / TikTok, UTM kuralı, yer tutucu listesi |
| `surumler.json` | `video` bloğu ana dersten birebir (`kimlik` `02-04-ydt-temel`); tek sürüm `s3`, `shorts`, ad `S3 Shorts (26,56 sn)` |
| `uretim-tutanagi/huni-surumler.json` | `s3-kapak-a/b/c`, `s3-hikaye-a/b` (uretimde), `s3-aciklama-a/b` (inceleme); surumler.json'a girmez, şef taşır |
| `uretim-tutanagi/istem/sahne/D-s3-sablon.md` + `D-<klasör>.md` × 7 | D-dikey şablonu kopyası, S3'e uyarlandı; her istemde kanca bayrağı yasağı, sözleşme istisnası, "qa-yerel t KÜRESEL" satırı |
| `uretim-tutanagi/ses-sentez.log` | ses zinciri günlüğü (el.py → sözcük → zaman → kur → m4a → altyazı → METIN, rc=0) |

Durağan kare biçimi: S1 `zaman.json` ile aynı (`hikaye` nesnesi + `duragan` listesi). Gerekçe: `birlestir.py`, `kur.py` ve editör yalnız
`fps/genislik/yukseklik/tema/sahneler` okur; ek üst alanlar birleştirmeyi bozmaz (S1-C raporu §1).

## 2. Ses kapısı (parça başına)

| Cümle | Dil | Metin | Duyulan (Whisper) | Benzerlik |
|---|---|---|---|---|
| 1 | en | The train to Izmir leaves at seven p.m. today. | The train to Izmir leaves at 7 p.m. today. | 1,00 (yeni) |
| 1 | en | I am going to the movie theater tonight. | I am going to the movie theater tonight. | 1,00 (yeni) |
| 2 | tr | Hocam, tren de plana göre kalkmıyor mu? Neden -ing yok? (ses: `/ɪŋ/`) | Hocam trende plana göre kalkmıyor mu? Neden ingi yok? | 0,98 (önbellek; `cumle-2.wav` md5 = ana ders `cumle-6.wav` `83fdfaa9…`) |
| 3 | tr | Planı bir kişi yapar. Tren tarifeye uyar: geniş zaman. | Planı bir kişi yapar. Tren tarifeye uyar. Geniş zaman. | 1,00 (yeni) |
| 4 | tr | Bu, üç farktan yalnız biri. | Bu üç farktan yalnız biri. | 1,00 (önbellek) |
| 4 | tr | Tam ders: Simple Present ve Present Continuous. (ses: `ve,`) | Tam Ders, Simple Present ve Present Continuous | 1,00 (önbellek) |
| 4 | tr | Üç farkın hepsi dört buçuk dakikada. | 3 farkın hepsi 4,5 dakikada. | 0,90 (önbellek; `cumle-4.wav` md5 = S1 `cumle-3.wav` `80e56127…`) |

Cümle başına en düşük: 1 → 1,00 · 2 → 0,98 · 3 → 1,00 · 4 → 0,90. Her parça tohum 0'da geçti; yeniden deneme yok.
0,98 ve 0,90'ın nedeni Whisper yazımı ("tren de" → "trende", rakam yazımı); okuma hatası değil. İkisi de ana ders ve S1'de kabul gören dosya.

Süre: tahmin 27,45 → ölçülen 26,56 sn. Cümle 1 5,45 sn (tahmin 6,01; parça arası 0,25), cümle 3 4,48 sn (tahmin 4,81).
Sözcük çapaları taslak tahmininden kaydı (`today.` 3,84 → 3,40 · `I` 4,61 → 4,45 · `Neden` 10,28 → 9,72 · `Planı` 12,07 → 11,51);
BRIEF ve istemler ölçülen değeri yazar. Sahne 01/02 sınırı korunur: `seven` 2,80–2,92 sahne 01'de, `p.m.` 3,00'te sahne 02'de.

## 3. Açık noktalar

| # | Nokta | Önerim |
|---|---|---|
| 1 | Jürinin "karar şefte" dediği seçimleri bu oturum verdi: kapak C `İKİ ÖRNEK` / `İKİ ZAMAN` (dil jürisinin 2. önerisi), kapak B/C can alıcısı seçenek (i), hikâye B = eski yedek B | şef onaylasın; ses etkilenmez, geri dönüş yalnız taslak ve istem metni |
| 2 | Dil jürisi madde 3'ün eşi S1 açıklamasında da var ("konusu püf noktası", `02-04-ydt-temel-s1/aciklama.md`, `aciklama-a.md`) | şef S1'i eşitlesin (yazma kapsamı dışı) |
| 3 | `utm_campaign` S3 büyük harf (`ING-YDT-GR-02-04-T`), S1 küçük harf: aynı ders iki kampanya adına bölünebilir | sabah Nadir'e; önerim S1'i büyük harfe çekmek |
| 4 | Sahne 02 en yoğun sahne: 2 kart + zaman çizgisi + 2 etiket + balon + figür + 2 `bag` (12,99 sn) | istem "kartlar üstte küçülür, balon solar" der; kontak sayfasında kalabalık görülürse zaman çizgisi etiketleri balon girerken solsun |
| 5 | Altyazı bandı EN parçada `Izmir` (noktasız) yazar; ana ders ve S1 aynı biçimde (`altyazi.json` EN parça senaryodan) | ana dersle aynı kalsın; değişecekse `altyazi_uret.py` kararı bütün paketleri etkiler |
| 6 | Durağan sahneler (04–07) `qa-yerel` ile ölçülemez (`sahneler[]` dışında, bilerek); istemler tek kare PNG + `ffprobe` doğrulaması verir | S1 ile aynı; şef onaylasın |
| 7 | `kunye.js` `cipler`'e 05/06/07 eklendi (S1 kopyasında yok); kapak B/C istemi çipi gizli tutar | zararsız; şef kaldırmak isterse tek satır |
| 8 | Huni sürümleri `huni-surumler.json`'da bekler; kayit yeni türleri tanıyınca şef taşır | — |
| 9 | S1'den devreden yayın öncesi ölçümler: `platform_url` canlılığı, TikTok `@ydspublishing`, D-0278 kimliği (defter eşitlenince) | yayından önce |
