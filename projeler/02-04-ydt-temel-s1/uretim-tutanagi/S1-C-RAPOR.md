# İstem S1-C raporu — 02-04-ydt-temel-s1 paket + ses + zaman + sahne istemleri + açıklama · 15.11.2026

| Ölçüm | Değer |
|---|---|
| Ses kapısı (faster-whisper large-v3-turbo, eşik 0,85) | 9 / 9 parça geçti; en düşük 0,90 |
| Anlatım | 30,56 sn (`anlatim.m4a` ffprobe 30.560000; imza `f75722c2…` aac-96k-48000-mono) |
| Cümle başı–bitişi (küresel sn) | 1: 1,00–6,36 · 2: 6,91–19,99 · 3: 20,54–29,56 · kuyruk 1,0 |
| Sahneler | 01 0,00–3,00 (102 kare) · 02 3,00–19,99 (522) · 03 19,99–30,56 (347) · hikâye zaman dışı (1 kare) |
| ElevenLabs | 257 karakter (≈ 1,26 TL), yalnız `araclar/ses-sunucu.sh` (kayit vekili); cümle 1 önbellekten (ücretsiz) |
| Jüri maddeleri | 7 / 7 işlendi (`S1-duzeltme.md`) |

Yapılmayan (istem kuralı): render, sahne kodu, git commit, Claude alt ajanı. Silinen dosya yok (`__pycache__` →
`~/Silinecekler/2026-11-15-0204/02-04-ydt-temel-s1-anlatim/`).

## 1. Yazılanlar

| Dosya | İçerik |
|---|---|
| `uretim-tutanagi/senaryo-taslak.md`, `kapak-taslak.md`, `aciklama-taslak.md`, `S1-A-RAPOR.md` | jüri düzeltmeleri (S1-A raporuna yalnız ek satır) |
| `uretim-tutanagi/S1-duzeltme.md` | madde → yapılan → kanıt (7 madde) |
| `gorevler.json`, `yorumlar.json`, `harita-konum.json` | örnekten kopya (boş) |
| `ortak/` bağları `cizim`, `font`, `hf_tema.py`, `logo` | `../../present-continuous/ortak/…` (örnekle aynı) |
| `ortak/kalem-canvas.js`, `tema_damga.py`, `tema.sh` | örnekten kopya (ana dersle de birebir) |
| `ortak/kunye.js` | `02-04-ydt-temel-dikey/ortak/kunye.js` kopyası (sha256 `34252b76…`; ders adı 2 satır + `YDT · BASIC`); yalnız `KOK` ve `cipler` değişti |
| `ortak/anlatim/senaryo.json` | örnek şeması; ses `gsJ9nrlXYbPztJxC4fwc` (ana ders öğretmeni), `kadro.ogretmen`, `giris`, `meta`; rakam yok |
| `ortak/anlatim/sozcuk_uret.py`, `metin_uret.py` | ana ders kopyası (değişiklik yok) |
| `ortak/anlatim/kur.py` | örnek kopyası (değişiklik yok) |
| `ortak/anlatim/zaman_uret.py` | ana ders kopyası; Edit: 3 sahne, 1080×1920, son sahne +1,0 sn, `hikaye` alanı |
| `ortak/anlatim/` üretilen | `cumle-1..3.wav`, `sentez.wav` (+ `.rapor.json`), `sureler.json`, `sozcukler.json`, `baslar.json`, `anlatim.wav`, `anlatim.m4a` (+ `.imza`), `altyazi.json` (9 parça), `METIN.md` |
| `zaman.json` | 3 sahne + `hikaye` alanı (`sahneler[]` dışında) |
| `BRIEF-S1.md` | çıktı, kaynaklar, sahne tablosu, sözcük çapalı sahne içeriği, kapak ve hikâye karesi tarifi, çalıştırma |
| `aciklama.md` | YouTube / Instagram / TikTok metni, UTM kuralı, yer tutucu listesi |
| `surumler.json` | `video` bloğu ana ders `surumler.json`'dan birebir (`kimlik` `02-04-ydt-temel`); tek sürüm `shorts`, ad `S1 Shorts (30,56 sn)` |
| `uretim-tutanagi/huni-surumler.json` | `kapak`, `hikaye`, `aciklama` (surumler.json'a girmez; şef taşır) |
| `uretim-tutanagi/istem/sahne/D-s1-sablon.md` + `D-<klasör>.md` × 4 | D-dikey şablonu kopyası, S1'e uyarlandı; 01 kapak (`kapak.png`), 02 örnek, 03 CTA, 04 hikâye (`hikaye.png`) |
| `uretim-tutanagi/ses-sentez.log` | el.py çıktısı (git dışı) |

Hikâye biçimi: `zaman.json` → `hikaye` = `{klasor, motor, kare: 1, cikti: "hikaye.png", …}`. Gerekçe: `birlestir.py` (`Z["sahneler"]`),
`kur.py`, editör (`zaman.fps/genislik/yukseklik/tema/sahneler`) yalnız bu alanları okur; ek üst alan birleştirmeyi bozmaz.

## 2. Ses kapısı (parça başına)

| Cümle | Dil | Metin | Duyulan (Whisper) | Benzerlik |
|---|---|---|---|---|
| 1 | tr | İstanbul'da yaşıyorum. Amcamla yaşıyorum. Türkçede ikisi de yaşıyorum. | İstanbul'da yaşıyorum, amcamla yaşıyorum, Türkçe'de ikisi de yaşıyorum. | 1,00 (önbellek; `cumle-1.wav` md5 ana dersle aynı `a069f11d…`) |
| 2 | tr | İngilizcede ikisi ayrılır. | İngilizce'de ikisi ayrılır. | 1,00 |
| 2 | en | I live in Istanbul. | I live in Istanbul. | 1,00 |
| 2 | tr | Hep orada: kalıcı durum, geniş zaman. | Hep orada. Kalıcı durum, geniş zaman. | 1,00 |
| 2 | en | I am living with my uncle. | I'm living with my uncle. | 0,96 |
| 2 | tr | Şimdilik: geçici durum, şimdiki zaman. | Şimdilik, geçici durum, şimdiki zaman. | 1,00 |
| 3 | tr | Bu, üç farktan yalnız biri. | Bu üç farktan yalnız biri. | 1,00 |
| 3 | tr | Tam ders: Simple Present ve Present Continuous. (ses: `ve,`) | Tam Ders, Simple Present ve Present Continuous | 1,00 |
| 3 | tr | Üç farkın hepsi dört buçuk dakikada. | 3 farkın hepsi 4,5 dakikada. | 0,90 |

Cümle başına en düşük: 1 → 1,00 · 2 → 0,96 · 3 → 0,90. Tekrar deneme yok (her parça tohum 0'da geçti).
0,90'ın nedeni Whisper'ın rakam yazımı ("4,5" → "dört beş"); okuma hatası değil.

## 3. Açık noktalar

| # | Nokta | Önerim |
|---|---|---|
| 1 | Toplam 30,56 sn; kalıp §5 aralığı (15–30 sn) 0,56 sn aşılır. Neden: cümle 2 13,08 sn (tahmin 11,8) + dil jürisi madde 3'ün 5 sözcüğü. Kural değiştirmedim | Olduğu gibi bırak: platform sınırı değil, kuyruk döngü kuralı (1,0 sn) korunur. Seçenek: kuyruğu 0,44 sn'ye indir (`zaman_uret.py` tek sabit, sentez yok) |
| 2 | "I am living": Whisper "I'm living" duydu (0,96); `am` hizalaması 40 ms. Ekran `I am living` yazar. Ana derste aynı parça aynı biçimde duyuldu (0,96) ve kabul edildi | Kulak kontrolü (3021): `am` duyuluyor mu |
| 3 | Kaynak jürisi madde 4 "sentezden önce dil jürisi yeni 4 TR cümleyi okusun": S1-B dil jürisi bu cümleleri denetledi, madde açmadı; ayrı koşu açmadım | Yeterli. Ayrı okuma istenirse metin değişen parça yeniden sentezlenir (önbellek, düşük maliyet) |
| 4 | `ortak/kunye.js` dikey paketin bugünkü (11:39) kopyası; o dosyada iş sürüyor | Dikey kunye.js değişirse S1 kopyası el ile eşitlenir |
| 5 | Hikâye sahnesi `qa-yerel.sh` / `cakisma-kapisi.mjs` / `sahne-kare.mjs` ile ölçülemez (`sahneler[]` dışında, bilerek). İstem 04 calistir.sh ile tek kare PNG doğrulaması verir; mp4 yasağına "tek kare PNG serbest" istisnası yazıldı | Şef onaylasın |
| 6 | Örnek S1 `calistir.sh` dosyaları `ONIZLE_YALNIZ`'ı tanımaz; qa-yerel `--hazirla` tam render başlatırdı | İstemlere satır eklendi (kalıp ana ders `calistir.sh`) |
| 7 | `surumler.json` `video.kod` = ana ders kodu (`ING-YDT-GR-02-04-T`); örnekte S1 kodu vardı. Shorts kodu `senaryo.json` `meta.kod`'da | `video.kimlik` ana ders olduğu için doğru |
| 8 | Huni sürümleri `huni-surumler.json`'da bekler | kayit yeni sürümü yayına alınınca şef taşır |
| 9 | Ana ders `surumler.json` `shorts` kaydının adı `S1 Shorts` (süre yok); ana pakete dokunmadım | şef eşitler |
| 10 | Nadir kararları: huni-plan §6 `utm_campaign` küçük harf · Instagram/TikTok dili (öğretmen + YDT öğrencisi) · `platform_url` canlılığı · TikTok `@ydspublishing` | sabah Nadir'e |
