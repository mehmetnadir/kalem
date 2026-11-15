# İstem S2-C raporu — 02-04-ydt-temel-s2 paket + ses + zaman + sahne istemleri + açıklama · 15.11.2026

| Ölçüm | Değer |
|---|---|
| Ses kapısı (faster-whisper large-v3-turbo, eşik 0,85) | 9 / 9 parça geçti; en düşük 0,90; her parça tohum 0 (yeniden deneme yok) |
| Anlatım | 27,98 sn (`anlatim.m4a` ffprobe 27.980000; imza `fcb2e7cc…` aac-96k-48000-mono). Hedef 24–28 içinde, 30 sınırının altında |
| Cümle başı–bitişi (küresel sn) | 1: 1,00–2,84 · 2: 3,39–17,41 · 3: 17,96–26,98 · kuyruk 1,0 |
| Sahneler | 01 0,00–2,84 (97 kare) · 02 2,84–17,41 (449) · 03 17,41–27,98 (347) · 04–07 durağan, zaman çizelgesi dışı (1 kare) |
| ElevenLabs | 192 karakter (≈ 0,94 TL), yalnız `araclar/ses-sunucu.sh` (kayit vekili). Cümle 3 önbellekten: `cumle-3.wav` md5 `80e56127…` = S1 |
| Jüri maddeleri | 8 / 8 işlendi (`S2-duzeltme.md`); uygulanmayan jüri maddesi yok |

Yapılmayan (istem kuralı): render, sahne kodu, git commit, Claude alt ajanı, silme, kanca atlama bayrağı. Kovan kaydı yazılmadı (yazma
kapsamı dışında). Paket dışına tek yazım: `K/.claude/docs/sozlesme.md`'ye 1 satır (istemdeki sözleşme istisnası; altyazı kayması).

## 1. Yazılanlar

| Dosya | İçerik |
|---|---|
| `uretim-tutanagi/senaryo-taslak.md`, `kapak-taslak.md`, `hikaye-taslak.md`, `aciklama-taslak.md` | jüri düzeltmeleri + çok sürüm dosya adları (S2-A metni silinmedi; ek satır ve değişen satır) |
| `uretim-tutanagi/S2-duzeltme.md` | madde → yapılan → kanıt (6 satır, 8 jüri maddesi); iki jürinin ayrıştığı yer tablosu |
| `gorevler.json`, `yorumlar.json`, `harita-konum.json` | S1'den kopya (boş) |
| `ortak/` bağları `cizim`, `font`, `hf_tema.py`, `logo` | `../../present-continuous/ortak/…` (S1 ile aynı) |
| `ortak/kalem-canvas.js`, `tema_damga.py`, `tema.sh` | S1 kopyası (değişiklik yok) |
| `ortak/kunye.js` | S1 kopyası; yalnız `KOK` (`/projeler/02-04-ydt-temel-s2/ortak`) ve `cipler` (7 klasör) değişti |
| `ortak/anlatim/senaryo.json` | S1 şeması; ses `gsJ9nrlXYbPztJxC4fwc` (ana ders öğretmeni); cümle 2 S2-C sırası; cümle 3 S1 ile birebir; rakam yok; `giris` + `meta` kapak A |
| `ortak/anlatim/sozcuk_uret.py`, `metin_uret.py`, `kur.py` | S1 kopyası (değişiklik yok) |
| `ortak/anlatim/zaman_uret.py` | S1 kopyası; Edit: `hikaye` → `hikaye-a.png`, `duragan` listesi (05, 06, 07) |
| `ortak/anlatim/altyazi_uret.py` | `araclar/altyazi_uret.py` kopyası; Edit: parça sınırı `sureler.json` `parcalar`'dan (açık nokta 1) |
| `ortak/anlatim/` üretilen | `cumle-1..3.wav`, `sentez.wav` (+ `.rapor.json`), `sureler.json`, `sozcukler.json`, `baslar.json`, `anlatim.wav`, `anlatim.m4a` (+ `.imza`), `altyazi.json` (9 parça), `METIN.md` |
| `zaman.json` | 1080×1920, 30 fps, gecis_kare 12; 3 sahne; `hikaye` (04) + `duragan` (05, 06, 07) `sahneler[]` dışında (S1 biçimi) |
| `BRIEF-S2.md` | çıktı, kaynaklar, sahne tablosu (7), ölçülmüş sözcük çapalı sahne içeriği, kapak A/B/C ve hikâye A/B tarifi, çalıştırma |
| `aciklama-a.md`, `aciklama-b.md`, `aciklama.md` (= A, `cmp` aynı) | YouTube / Instagram / TikTok; UTM; yer tutucu tablosu |
| `surumler.json` | `video` bloğu S1 ile aynı (`kimlik` `02-04-ydt-temel`); tek satır `s2` / `shorts` / `S2 Shorts (27,98 sn)` |
| `uretim-tutanagi/huni-surumler.json` | `s2-kapak-a|b|c`, `s2-hikaye-a|b` (`uretimde`), `s2-aciklama-a|b` (`inceleme`); şef taşır |
| `uretim-tutanagi/istem/sahne/D-s2-sablon.md` + `D-<klasör>.md` × 7 | `D-dikey-sablon.md` kopyası, S2'ye uyarlandı; örnek sahneler S1'den; kanca bayrağı + sözleşme satırı + KÜRESEL saniye her istemde |
| `uretim-tutanagi/ses-sentez.log` | el.py çıktısı |

Durağan kare biçimi: `zaman.json` → `hikaye` = `{klasor, motor, kare: 1, cikti: "hikaye-a.png", …}`, `duragan` = aynı biçimde 3 kayıt.
Gerekçe: `birlestir.py`, `kur.py` ve editör yalnız `fps/genislik/yukseklik/tema/sahneler` okur; ek üst alan birleştirmeyi bozmaz (S1 ile aynı).

## 2. Ses kapısı (parça başına)

| Cümle | Dil | Metin | Duyulan (Whisper) | Benzerlik |
|---|---|---|---|---|
| 1 | tr | Genel mi, şu an mı? | Genel mi, şu an mı? | 1,00 |
| 2 | en | She wears her coat in the winter. | She wears her coat in the winter. | 1,00 |
| 2 | tr | Genel durum: geniş zaman. | Genel Durum Geniş Zaman | 1,00 |
| 2 | en | She is wearing her pink T-shirt today. (ses: `T shirt`) | She is wearing her pink t-shirt today. | 1,00 |
| 2 | tr | Today iki zamanda da geçebilir; farkı anlam yapar. | Today, iki zamanda da geçebilir. Farkı anlam yapar. | 1,00 |
| 2 | tr | Konuşma anı: şimdiki zaman. | Konuşma Anı, Şimdiki Zaman | 1,00 |
| 3 | tr | Bu, üç farktan yalnız biri. | Bu üç farktan yalnız biri. | 1,00 (önbellek) |
| 3 | tr | Tam ders: Simple Present ve Present Continuous. | Tam Ders, Simple Present ve Present Continuous | 1,00 (önbellek) |
| 3 | tr | Üç farkın hepsi dört buçuk dakikada. | 3 farkın hepsi 4,5 dakikada. | 0,90 (önbellek; Whisper rakam yazımı, S1 ile aynı) |

Cümle başına en düşük: 1 → 1,00 · 2 → 1,00 · 3 → 0,90. Kulak kontrolü (3021) bekliyor: *today*, *wears*, *is wearing*.

## 3. Açık noktalar

| # | Nokta | Önerim |
|---|---|---|
| 1 | **Ortak altyazı hatası:** `araclar/altyazi_uret.py` sözcüksüz parçada sonraki parçanın sözcüklerini kullanır. Ana ders `altyazi.json`: cümle 3 EN2 35,37'de yazılı (ses 32,40), cümle 9 EN 138,57'de (ses 135,60); render edilmiş ana ders ve dikey paket etkilenir (sözleşme satır 48, 50: "ortak düzeltme bekliyor"). S2 bunu paket kopyasıyla çözdü | `araclar/altyazi_uret.py`'yi S2 kopyasındaki `parcalar` yöntemine çek, ana ders + dikey + S3 `altyazi.json`'u yeniden üret (kapsam dışı; şef) |
| 2 | Jüri madde 2'de iki öneri ayrıştı: dil (c) ses `geçebilir`, kaynak (b) ok yalnız PC + açıklamadan satır çıkar. Birleşik uygulandı (`S2-duzeltme.md` tablo) | şef onaylasın; geri almak 50 karakterlik tek parça sentezi |
| 3 | `She is wearing her pink T-shirt today.` parçası `sozcukler.json`'da yok (el.py `T shirt` eşleşmez; ana derste de yok). Çapalar ElevenLabs önbellek hizalamasından BRIEF'e yazıldı (`T-shirt` 9,65 · `today.` 10,13). Sözleşme satır 30 faster-whisper + RMS yöntemini öngörür | sahne 02 ajanı BRIEF değerini kullanır; kuşkuda faster-whisper ile karşılaştırır |
| 4 | Cümle 1 1,84 sn (S2-A tahmini 1,44). Sahne 01 2,84 sn, K23 (≤ 3 sn) içinde; uçuş penceresi 2,24–2,84 | yok |
| 5 | Hikâye B `Look!` iki jürinin önerisi; birebir metin jüriden geçmedi (yeni sözcük) | kısa dil okuması istenirse yalnız hikâye B |
| 6 | Ses `geçebilir`, `meta.canAlici[3]` `geçer` (ana ders listesi). Listeye dokunmadım | liste ana dersin; değişmesin |
| 7 | `METIN.md` başlığında "sahne 01 3 sn" (S1 `metin_uret.py` sabit metni); gerçek 2,84. BRIEF'te DİKKAT notu var | gerekirse `metin_uret.py` başlığına tek Edit |
| 8 | Durağan sahneler (04–07) qa-yerel / çakışma kapısıyla ölçülemez (S1-VAR: 3/3 "sahne bulunamadı"); istemler tek kare PNG + `ffprobe` doğrulaması verir | S1 ile aynı; şef onaylasın |
| 9 | S1 açıklama dosyaları "konusu püf noktası" taşır (dil 3); `utm_campaign` S1 küçük, S2 büyük harf | S1 için şef istek açsın; harf kararı Nadir'de |
| 10 | `huni-surumler.json` kayit yeni sürümü yayına alınınca taşınır; D-0278 srv21 defterinde yok; `platform_url` canlılığı ve TikTok `@ydspublishing` doğrulanmadı | şef / Nadir |

Sonraki adım: 7 sahne istemini (`istem/sahne/D-*.md`) koştur; sahne 01 render dalı `kapak-a.png` + `kapak.png` yazar.
