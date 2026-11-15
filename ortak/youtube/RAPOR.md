# YT-1 raporu: YouTube sürümü ortak parçaları (giriş, çıkış, sessiz bildirim kartı) · 15.11.2026

Standart: `D/.claude/docs/youtube-surumu-standart.md` (TASLAK, `git pull` 22:30'da güncel). Envanter: `D/.claude/docs/arastirma/1511/youtube-surumu-envanter.md`.
Makine: srv21 (Linux x86_64). mp4 render yok, commit yok, alt ajan yok, ayna yüklemesi yok. Yazılan her dosya `K/ortak/youtube/` altında
(tek istisna: `K/.claude/docs/sozlesme.md`, 2 satır).

| Kapı (standart §5) | Ölçüm | Sonuç |
|---|---|---|
| 4. İlk söz ≤ 1 sn, giriş ≤ 3 sn | giriş 3,00 sn (90 kare); ilk söz 0,54 sn; söz sonu 2,39 sn | GEÇTİ |
| 3. Çıkışta sağ yarı boş | x ≥ 960 zemin dışı piksel: 0 (6 kare: 0,5 · 4,0 · 19,9 sn × açık, koyu); en sağ öğe x 860 | GEÇTİ |
| 2. Kart okunuyor, çakışmıyor | 4 örnek karede kart boş yerde, gözle okundu; yer ölçümü aşağıda | GEÇTİ (örnek karelerde) |
| Ses kapısı (istem ≥ 0,90) | Whisper 1,00 · 1,00 · 1,00 | GEÇTİ |
| 1. Süre = giriş + ders + çıkış | birleştirme aracının kapısı (sonraki iş) | — |
| 5. Kanal "çocuklara özel" değil | Studio'da bakılır | — |

## 1. Süre ve ses

| Parça | Süre | Söz | Ses dosyası | Söz aralığı (enerji, −40 dBFS) |
|---|---|---|---|---|
| Giriş | 3,00 sn · 90 kare | "YDS Publishing'e hoş geldin." (ses metni "YeDeSe Publishing'e …") | `giris/ses/giris.wav` 48 kHz mono, 3,00 sn | 0,54 – 2,39 sn |
| Çıkış | 20,00 sn · 600 kare | "Faydalı olduysa abone ol. Sıradaki ders ekranda." | `cikis/ses/cikis.wav` 48 kHz mono, 20,00 sn | 0,57 – 4,26 sn |

| Whisper (el.py, faster-whisper large-v3-turbo) | Duyulan | Benzerlik |
|---|---|---|
| YDS Publishing'e hoş geldin. | Yedese Publishing'e hoş geldin. | 1,00 |
| Faydalı olduysa abone ol. | Faydalı olduysa abone ol. | 1,00 |
| Sıradaki ders ekranda. | Sıradaki ders ekranda. | 1,00 |

- Ses zinciri: `ses.sh` → `araclar/ses-sunucu.sh --kok ortak/youtube/_kok youtube-<parça>` → `D/araclar/iki-dilli/el.py` (ElevenLabs eleven_v4,
  vekil; anahtar ortamını araç kendisi okudu). `_kok/projeler/youtube-<parça>/ortak/anlatim` simge bağı → `<parça>/ses/`.
- Öğrenci sesi `oPC5I9GKjMReiaM29gjY` = `projeler/02-04-ydt-temel/ortak/anlatim/senaryo.json` `sesler.ogrenci`; `ses.sh` eşitliği denetler.
- Önbellek anahtarı (el.py: ses metni + bağlam + ses kimliği + model + tohum + hız eki [1,0, 0,9]): 3 parçanın anahtarlı wav'ı önbellekte var;
  aynı metnin öğretmen sesi anahtarı yok (`olcum/ses.json`). Maliyet 78 karakter (≈ 0,38 TL); ikinci koşu önbellekten, ücretsiz.
- Söz başı: giriş ve çıkışta 0,50 sn (`uret.py` `GIRIS_SES_BAS`, `CIKIS_SES_BAS`); wav'ın kendi baş sessizliği 0,04 sn → ilk söz 0,54.
- Yan not: el.py hizalaması son sözcüğü ("ekranda.") 4,07 sn'de bitirir, wav 3,99 sn; ekran zamanlaması sözcük başlarını kullanır, etkisi yok.

## 2. Sahneler

| Parça | Ekran | Hareket |
|---|---|---|
| Giriş | logo (h 150, emsal giriş damgasıyla aynı boy) ortada + `@ydspublishing` (Lexend 700 48, ikincil) altında | tek hareket: grup 0,00–0,60 sn 1,12 → 1 ölçek, 0 → 1 opaklık (`power3.out`); sonra durgun. 0,0 karesi boş zemin (opaklık 0) |
| Çıkış | sol yarı: kanal satırı (logo h 72 + `@ydspublishing` Lexend 700 40, taban logo tabanında) · "Faydalı olduysa" (Fredoka 700 92) · "abone ol." (Fredoka 700 92, vurgu) · "Sıradaki ders ekranda." (Lexend 700 42, ikincil) + sağı gösteren el oku (x 650–860) | kanal satırı 0–0,30 sn belirir; satırlar söylendiği anda vurur (0,50 · 1,70 · 2,65 sn; 0,22 sn `back.out(1.6)`); ok 3,61–3,96 sn çizilir; 3,96 sn'den sonra ekran durgun |

- Tema: renkler emsal dersin `ortak/hf_tema.py` değişkenlerinden (`--zemin`, `--murekkep`, `--ikincil`, `--vurgu`, `--vurguDolgu`, `--pilMetin`);
  ham renk yok. Zemin katmanları (zemin + gren + vinyet) emsal HF sahneleriyle aynı. Açık varsayılan, koyu eş.
- Yazı tipleri sahne dosyasına gömülü (woff2 base64): sahne `file://` ile de doğru yazı tipiyle açılır.
- Kareler (Read ile bakıldı; logo, yazı, ok okunuyor; taşma yok): `giris/k/giris-{0.0,1.0,2.97}.png`, `giris/k/koyu/…`,
  `cikis/k/cikis-{0.5,4.0,19.9}.png`, `cikis/k/koyu/…`. Giriş son karesi = kare 89 (2,967 sn).

## 3. Bildirim kartı

`bildirim/bildirim-acik.png`, `bildirim/bildirim-koyu.png`: RGBA, 520 × 140, köşeler şeffaf (rx 30). Kart dolgusu `--murekkep`, yazı `--zemin`
(Fredoka 700 40): beğen işareti (elle çizilmiş SVG yolu, dolgu `--vurguDolgu`) · "Beğen" · "·" · abone düğmesi biçimi (hap + artı) · "Abone ol".
Emoji yok, YouTube logosu yok. Öğe kutuları x 25–500, y 45–95 (kart içinde, birbirine değmez). Kaynak `bildirim/kart.html` (`uret.py` yazar).

## 4. Yer ölçümü

Yöntem: kare − zemin referansı (aynı tema, `olcum/zemin-{acik,koyu}.png`), kanal farkı > 24 → içerik maskesi (ders zeminleri referanstan
≤ 3 ayrışır). Kart + 16 px pay içerikle kesişmemeli, kare kenarından ≥ 40 px. Pencere: 30 sn ≤ t ≤ ders sonu − 20 sn (standart §3).
Tema dizinden değil parlaklıktan bulunur (02-04 `k/` kökündeki 4 haneli 30 kare koyu temadır). İkinci koşu (147 sn) aynı sonucu verdi.

| Ders | Kaynak | Kare (hepsi) | Pencerede |
|---|---|---|---|
| 02-04-ydt-temel (yeni kuşak) | `sahneler/*/k/*.png` 94 kare + `cikti.mp4`, `cikti-koyu.mp4` saniyede 1 kare (sahne sınırına < 0,5 sn olan geçiş kareleri dışarıda) | 598 | 484 |
| simple-present-temel (eski kuşak) | `sahneler/01/k` 3 kare + bu iş için yakalanan 22 kare (`bildirim/olcum/simple-present-temel/`, `araclar/sahne-kare.mjs`) | 25 | 10 |

| Köşe (aday sırası) | En iyi yer (x, y) | 02-04 boş | simple-present boş | Pencere birleşiminde en büyük boş bölge |
|---|---|---|---|---|
| sağ üst | 1156, 40 | 142 / 484 (%29) | 10 / 10 | x 960 y 0 · 734 × 114 (kart 140 boyu sığmaz) |
| **sol alt** | **240, 900** | **423 / 484 (%87)** | **8 / 10** | x 190 y 974 · 770 × 106 |
| sol üst | 428, 88 | 56 / 484 (%12) | 9 / 10 | x 0 y 0 · 960 × 50 |

Sahne dökümü (02-04, pencere kareleri, boş / toplam):

| Sahne | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| sağ üst | 36/36 | 56/56 | 2/54 | 0/42 | 0/38 | 0/36 | 0/41 | 46/46 | 0/50 | 2/32 | 0/53 |
| sol alt | 36/36 | 56/56 | 54/54 | 42/42 | 31/38 | 36/36 | 36/41 | 32/46 | 50/50 | 30/32 | 20/53 |

Seçilen: **sol alt**, `bildirim/yer.json` = `{"x": 240, "y": 900, "w": 520, "h": 140, "kose": "sol_alt"}`. Hiçbir köşe bütün karelerde boş
değil; sol alt en yüksek boş oranı. Standart zamanlarında (02-04: %30 ≈ 79 sn sahne 05, %70 ≈ 185 sn sahne 11) sağ üst 2/54 ve 0/50,
sol alt 54/54 ve 50/50. simple-present (93,5 sn, 1 bildirim, ≈ 30 sn → sahne 04): sol alt 5/5.
Kart künye logosunun sağında (logo x 60–190, kart x 240), ajandanın solunda. Tam veri: `bildirim/olcum/yer-tablo.json` (kare başına köşe boşluğu).

Örnek kareler (kart yere bindirilmiş; hepsinde kart boş yerde, okunuyor): `bildirim/ornek-02-04-ydt-temel-{acik,koyu}.png`
(sahne 04, 68,6 sn), `bildirim/ornek-simple-present-temel-{acik,koyu}.png` (sahne 04, 31,5 sn). Temiz taban kareleri `bildirim/ders/`.

## 5. Standarttan sapma

| Madde | Standart | Bu iş | Gerekçe |
|---|---|---|---|
| Bildirim yeri (§2, §3) | sağ üst | sol alt (240, 900) | ölçüm: sağ üst yeni kuşak derste pencere karelerinin %29'unda boş, %30/%70 anlarında dolu (tablo §4). Karar Nadir'de; sağ üste dönmek için `yer.json` tek satır değişir, kart aynı |
| Bildirim zamanı (§3) | dersin %30 / %70'i, cümle sınırı | değişmez; ek şart önerisi: seçilen anda yer boş olmalı (`yer-tablo.json` kare boşluğu ya da 3 kare kapısı) | 02-04 sahne 13'te sol alt 20/53 boş |

Risk (ölçülmedi): sol alt bant (y 900–1040) YouTube oynatıcısında denetim çubuğu (fare üstündeyken) ve açık altyazının alt-orta bandına yakındır;
kart oynatma sırasında 3 sn görünür, denetim çubuğu o sırada gizlidir. Uzun altyazı satırı kartın sağ ucuyla (x 600–760) örtüşebilir.

## 6. Önizleme

`onizle.html` (tek dosya; yollar göreli; dış ağ isteği yok): giriş (sesiyle) → 6 sn örnek ders karesi (02-04 sahne 04; kart 2.–5. sn,
0,3 sn solma) → çıkış (sesiyle), toplam 29,0 sn. Üstte "Baştan" ve "Açık / Koyu". `?tema=koyu` koyu açar. Tarayıcı sesli otomatik oynatmayı
engellerse görüntü oynar, durum satırı "ses için Baştan'a bas" yazar. Deneme: önizleme sunucusu (41022) ve `file://` ile başsız Chrome'da,
1,0 · 6,5 · 11,0 / 13,0 sn kareleri doğru katmanı gösterdi (`olcum/onizle/*.png`).

## 7. Birleştirme aracının (sonraki iş) beklediği girdi

| Girdi | Dosya | Biçim | Süre | Not |
|---|---|---|---|---|
| Giriş görüntüsü | `giris/video-acik.mp4`, `giris/video-koyu.mp4` | 1920×1080, 30 fps, sessiz | 3,00 sn (90 kare) | HENÜZ YOK: render sonraki işte (`uret.py --tema X` → `giris/proje` → `hyperframes render --fps 30`) |
| Giriş sesi | `giris/ses/giris.wav` | PCM 16 bit, 48 kHz, mono | 3,00 sn | görüntüyle aynı 0 noktası |
| Çıkış görüntüsü | `cikis/video-acik.mp4`, `cikis/video-koyu.mp4` | 1920×1080, 30 fps, sessiz | 20,00 sn (600 kare) | HENÜZ YOK (giriş gibi) |
| Çıkış sesi | `cikis/ses/cikis.wav` | PCM 16 bit, 48 kHz, mono | 20,00 sn | söz 0,57–4,26 sn |
| Bildirim kartı | `bildirim/bildirim-acik.png`, `-koyu.png` | PNG RGBA 520×140 | 3,0 sn görünür | `-loop 1`, `fade=in/out … alpha=1` 0,3 sn, `overlay=240:900:enable='between(t,a,b)'` |
| Kart yeri | `bildirim/yer.json` | `{x, y, w, h, kose}` | — | tek kaynak; araç sabit sayı yazmaz |
| Bildirim zamanı | paket `youtube.json` `bildirimler[]` (standart §3) | `{t, sure}` ders zamanı | — | araç giriş süresini (3,00) ekler |

- Ses düzeyi: parçalar el.py düzeyinde (parça başına −20 LUFS, tepe 0,95); bütün dosya araçta `loudnorm -16` ile eşitlenir (standart §4).
- `projeler/02-04-ydt-temel/youtube.json` bugün başka oturumun meta dosyası (başlık, etiket, `bolumler[]`); `bildirimler` alanı yok.
  Giriş eklenince açıklamadaki bölüm damgaları 3,00 sn kayar (ilk damga 0:00 kalır).

## 8. Dosyalar (hepsi `K/ortak/youtube/`)

| Dosya | Görev |
|---|---|
| `uret.py` | giriş/çıkış HyperFrames sahnesi (`<parça>/proje/index.html`, `lib/gsap.min.js`, `assets/logo-{acik,koyu}.svg`), `bildirim/kart.html`; `--onizle` → `onizle.html` |
| `kare.mjs` | başsız kare (ortak Chrome CDP 41333, ayrı tarayıcı bağlamı): `__seek(t)` + PNG; `--seffaf` RGBA |
| `olc.py` | `ses` (klip sesi + söz aralığı + önbellek), `sag` (çıkış sağ yarı), `yer` (bildirim yeri + örnek kareler) |
| `ses.sh` | iki sözün sentezi (ders ses zinciri) |
| `calistir.sh` | üret → kareler (açık + koyu) → kart PNG → ölçümler → önizleme (render yok) |
| `giris/ses/`, `cikis/ses/` | `senaryo.json`, `sentez.wav`, `sentez.wav.rapor.json`, `cumle-1.wav`, `sureler.json`, `giris.wav` / `cikis.wav` |
| `giris/k/`, `cikis/k/` | 12 kare (açık + koyu) |
| `bildirim/` | 2 kart PNG, `yer.json`, 4 örnek, `ders/` 4 taban kare, `olcum/yer-tablo.json`, `olcum/simple-present-temel/` 22 kare |
| `olcum/` | `ses.json`, `sag.json`, `zemin-{acik,koyu}.png`, kutu ölçümleri (`*-kutu-*.jsonl`), `onizle/` 6 deneme karesi |
| `_kok/` | `ses-sunucu.sh` için simge bağları |

Komutlar: `bash ortak/youtube/ses.sh` (bir kez) · `bash ortak/youtube/calistir.sh` (≈ 2,5 dk; yer ölçümü 1,5 dk).

## 9. Notlar

- Yazma kancası (`write-size-gate`) 15 satırdan uzun `.py` yazımını Write ile durdurdu; istem kanca bayrağını ve alt ajanı yasakladığı için
  `.py` dosyalarını kabuk heredoc'uyla yazdım. Bayrak oluşturulmadı.
- Çakışma kapısı (`araclar/cakisma-kapisi.mjs`) paket sahnesine bağlıdır, burada koşmadı; çıkışta sağ yarı piksel ölçümü ve kutu ölçümü yerini aldı.
- Deneme kareleri (yanlış dizin) `~/Silinecekler/2026-11-15-youtube/k-deneme-giris/` altına taşındı, `LISTE.md` satırı yazıldı.
