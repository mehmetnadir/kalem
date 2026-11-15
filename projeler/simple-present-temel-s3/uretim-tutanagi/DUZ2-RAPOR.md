# DUZ2-RAPOR — simple-present-temel-s3 (kol a) · J2 özeti A sınıfı düzeltmeleri · 15–16.11.2026

İstem: `uretim-hatti/istemler/DUZ2-0202S3.md`. Girdi: `uretim-hatti/raporlar/J2-OZET-1511.md` §3A, §4.1, §4.2 satır P3; `juri/J2-hukum.md`.
Kol b raporu: `../../simple-present-temel-s3b/uretim-tutanagi/DUZ2-RAPOR.md`. Üretici: Claude Opus 5.5 (`claude-opus-5-5`). Alt ajan, agy-filo,
mp4, commit yok. Silinen dosya yok; taşınanlar `~/Silinecekler/2026-11-15-duz2-0202S3/` (`~/Silinecekler/LISTE.md` 16.11 satırları).

Devir: önceki oturum (15.11 gece) bellek arızasıyla kesildi. O oturum yalnız ses adımını bitirmişti: senaryo c2 + rozet + `canAlici`,
c2 sentezi ve zaman zinciri (`ses-sentez-DUZ2.log` 00:20–00:24), önce kopyaları `~/Silinecekler/…/once/`. Bu oturum o çıktıyı
yeniden doğruladı (sha256, Whisper raporu, süreler) ve kalan bütün işi yaptı.

| Kalem | Sonuç |
|---|---|
| Düzeltilen kusur | A1/TD-1 (J2 EK-RZ) · A2/TD-2 (KS-10) · A3 (EK-5b i) · TD-3 (EK-5b ii) · A7 (ST-1) · C8 (KARE-BAYAT) |
| Ek kanıt (C) | C1 kapı çıktısı · C2 HV-13 piksel çifti · C3 `kapak-a|b|c-168.png` · C5 v2 kontak |
| Yeniden sentez | 1 cümle (c2; 4 parça, 103 karakter ≈ 0,5 TL); c1, c3, c4 sha256 değişmedi |
| Süre | 25,08 → **27,33 sn** (≤ 35 ✓; hedef 22–26 ✗, +1,33) |
| İlk söz · kanca | 1,00 sn · kanca sahnesi 0,00–3,89, kanca cümlesi biter 3,89 (değişmedi) |
| Whisper en düşük | 0,93 (c3 `Does varsa fiil yalın.`, "döz"; değişmedi); yeni c2 parçaları 1,00 · 0,97 · 1,00 · 1,00 |
| Çakışma kapısı | çıkış **0** (4 sahne, 0 uyarı) |
| `hyperframes check` | 3 HyperFrames sahnesi çıkış 0, 0 hata |
| `huni-kapi.mjs` | 16 GEÇTİ · 1 KALDI (JR-1b: jüri DUZ2'den eski; J2 yeniden koşar) · 5 ÖLÇÜLEMEDİ |
| mp4 | yok |

## 1. Düzeltmeler

| Kusur | Dosya | Önce → sonra | Kanıt |
|---|---|---|---|
| A1/TD-1 rozet | `senaryo.json` `giris.rozetler` (önceki oturum), `BRIEF-S3.md`, `ortak/kunye.js`, 7 × `yardim.py`, `06-…/uret.py`, 7 × `SPEC.md` | `YDT · BASIC` → `YDT · TEMEL` | `grep -rn BASIC` (py, js, json, sh; `k/` ve tutanak dışı) = 0; `huni-kapi` HV-24 GEÇTİ (33 dosya); bütün karelerde `YDT · TEMEL` |
| A2/TD-2 karakter | `ortak/kapak/karakter.png` | erkek (`a4198903…`) → kadın öğrenci (`5a902b40…`, ana paketle sha256 eş) | `sha256sum`; eskisi `…/simple-present-temel-s3/ortak-kapak/` |
| A2 çağrı kartı | `ortak/kapak/ana-kapak.png`, `ana-kapak-koyu.png` | eski ana kapak (erkek) → ana paketin yeni `kapak.png` (`7f714514…`) / `kapak-koyu.png` (`7e948a3b…`) | `k/04-…-22.9 · 24.6 · 27.3.png`, `k/koyu/04-…-22.9 · 27.3.png` |
| A2 kanca yerleşimi | `sahneler/01-hyperframes-kanca/uret.py` | görsel boyu sabit 896×1200 → dosyadan (1024×1024); daire merkezi sabit 470 px → alfa kutusunun %37,2'si (eski görselde de 470); `karakter_ustu()` daire merkezini `?` kutusundan DAIRE_R + 16 uzak arar | ilk koşu denetim 5'te düştü (daire `?` kutusuna 112 px < 115,5); sonuç üst 888, alfa x 767–948, y 888–1151 |
| A2 kapak standardı (§2, §4) | kanca + kapak A | işaret eli sol üstte, kartın sağ üst köşesindeki `?`'e bakar; karakter kart ve `?` kutusuna ≥ 26 px uzak (assert); 10 px krem çıkartma kenarı iki temada görünür; karakter içerik bandında | `kapak-a.png`, `sahneler/01-…/k/koyu/kapak-a-koyu.png`, `k/01-…-2.9.png` |
| A3 c2 sesi | `ortak/anlatim/senaryo.json` c2 (önceki oturum) | "Olumsuzda ve soruda does girer, s ona geçer." → "He, she, it ile olumsuzda ve soruda does girer; s ona geçer." | `cumle-2.wav` `6cbf7b4efbd3` → `ea1bb8233779`; §2 |
| A3 sahne 02 | `sahneler/02-paperjs-deger/sahne-02.js`, `calistir.sh`, `sayfa.html` | sözcük sırası +4; KARE 281 → 348; kapsam etiketi `he, she, it` (soluk el yazısı, "He," anında, kart 0 ile söner; kendi `KAPSAM` grubu) | `k/02-…-5.2 · 6.6.png` |
| A3 açıklama | `aciklama-a.md` (= `aciklama.md`, `cmp` eş), `aciklama-b.md` (2 yer) | kural cümlesi "He, she, it ile olumsuzda ve soruda does girer; s ona geçer …"; süre satırı 25,08 → 27,33 | `git diff` |
| A3 BRIEF | `BRIEF-S3.md` | DUZ2 notu (yeni metin, yeni zamanlar, eski tablo +2,25 sn kayar), süre | `git diff`; kol b ile `cmp` eş |
| TD-3 | `senaryo.json` `meta.canAlici[0]` (önceki oturum), `surumler.json` `video.canAlici[0]` | "Türkçedeki geniş zaman eki = İngilizcedeki s: gider = goes" çıkarıldı | `grep -c "geniş zaman eki ="` = 0 |
| A7 kanca `?` | `sahneler/01-…/uret.py` | `#e0473b` → mürekkep | `k/01-…-2.9 · 3.2.png` |
| A7 sahne 02 (aynı kusur, jürinin bakmadığı kare) | `sahne-02.js` | üstü çizgi ve ✗ `RT.kirmizi` → `RT.murekkep`; çizilen `es` aynı anda soluk tona geçer (mürekkep çizgi mürekkep harf üstünde okunmuyordu) | `k/02-…-11.6 · 12.4.png`, `k/koyu/02-…-11.6 · 12.4.png` |
| A7 kapak C, hikâye A | `07-…/uret.py`, `05-…/uret.py` | çizik + ✗ kırmızı → mürekkep; denetim "kırmızı = 0" | `kapak-c.png`, `hikaye-a.png`, `k/koyu/kapak-c-koyu.png`, `hikaye-a-koyu.png` |
| C8 bayat kare | bütün sahneler | 4 sahne + 5 türev açık + koyu yeniden çekildi; eskiler Silinecekler'de | §3 |
| AB-3 için kod | `sahne-02.js`, `calistir.sh` | `T_BAS` sabit → paketin `zaman.json` kaydından; denetim kareleri sahne içi saniye | iki kolda kod paket adı dışında bayt eş; görüntü değişmedi (3 kare 0 px) |
| Yan etki onarımı | `05`–`08` `RAPOR.md` | türev koşusu (`ortak/tema.sh`) tema satırı yazdı → HEAD içeriği geri yazıldı | `git diff --stat` 0 |
| SPEC notu | `01-…/SPEC.md`, `02-…/SPEC.md` | DUZ2 notu (sözcük sırası, t_bas kaynağı, karakter, renk) | — |

Dil denetimi (şef kararı "kendin denetle"):

- Önerilen cümle kaynaktan bağımsız doğrudur. `does` yalnız üçüncü tekil kişide (he, she, it) olumsuz ve soru yardımcısıdır;
  `I, you, we, they` `do` alır. Cümle bu sınırı açıkça söyler.
- "s ona geçer" olumluda `-s` alan sözlük fiilini (go → goes) varsayar. `be` ve kiplik fiiller bu kalıba girmez, ama olumluda da
  `-s` eki almaz (is, can). Kısa sözlük fiilini anlatır (örnek go). Ek sınır sesi uzatırdı; süre zaten hedef dışıdır. Öneri değişmedi.
- "He, she, it" ekrandaki örnek kişilerle (`He doesn't go.`, `Does she go?`) aynı terimdir. Sahne 02 etiketi aynı terimi karta taşır.
- Kapak, hikâye ve kaydet kartı c3'ün kuralını taşır ("Does varsa fiil yalın."): `does` görünüyorsa özne zaten he, she, it. Değişmedi.

## 2. Ses, süre, Whisper

| Cümle | Metin (parçalar) | sha256 (12) | Whisper | Durum |
|---|---|---|---|---|
| c1 | He doesn't goes. · Hata nerede? | `132a1a3113c2` | 1,00 · 1,00 | değişmedi |
| c2 | He, she, it · ile olumsuzda ve soruda does girer; s ona geçer. · Fiile s gelmez. · He doesn't go. Does she go? | `ea1bb8233779` (önce `6cbf7b4efbd3`) | 1,00 · 0,97 · 1,00 · 1,00 | **yeni** (4 parça; önbellek anahtarı cümle içi bağlamı da taşır, değişmeyen 2 parça da yeniden istendi) |
| c3 | Does varsa fiil yalın. · Bir arkadaşına gönder; o da karıştırıyor. | `569e61237aa4` | 0,93 · 1,00 | değişmedi |
| c4 (öğrenci) | Bu sadece başlangıç. · Dersin tamamı YDS Publishing YouTube kanalında. | `6a9927c66d00` | 1,00 · 1,00 | değişmedi |

Zincir (günlük `ses-sentez-DUZ2.log`): `araclar/ses-sunucu.sh` (el.py, kapı önbelleği 6 / 10) → `sozcuk_uret.py` → `zaman_uret.py` →
`kur.py` → `araclar/ses-paketle.py --yaz` → `araclar/altyazi_uret.py` → `metin_uret.py`. `anlatim.m4a` ffprobe 27,330000.

| Ölçü (sn) | Önce | Sonra | Sınır |
|---|---|---|---|
| Toplam | 25,08 | 27,33 | ≤ 35 ✓ · hedef 22–26 ✗ (+1,33) |
| İlk söz | 1,00 | 1,00 | ≤ 1 ✓ |
| Kanca sahnesi bitişi · kanca cümlesi bitişi | 3,89 · 3,89 | 3,89 · 3,89 | ≤ 4 ✓ |
| Sahne 02 değer | 3,89–12,84 | 3,89–15,09 (348 kare) | huni §3 rehberi 4–15: bitiş +0,09 |
| Sahne 03 kaydet | 12,84–18,10 | 15,09–20,35 | — |
| Sahne 04 çağrı | 18,10–25,08 | 20,35–27,33 | — |

## 3. Kareler ve kapı

Kareleri ben çektim ve baktım (`sahne-kare.mjs --port 41333 --sunucu 41022`; kapak A `proje-ka` + `hyperframes snapshot --at 0.9`;
türevler `calistir.sh --tema koyu|acik`). Aynı anda tek tarayıcı işi koştu.

| Sahne / türev | Açık (küresel sn) | Koyu |
|---|---|---|
| 01 kanca | `k/01-…-0 · 0.9 · 1.95 · 2.9 · 3.2 · 3.5 · 3.8.png` | `k/koyu/01-…-1.95 · 2.9.png`, `kapak-a-koyu.png` |
| 02 değer | `k/02-…-3.9 · 5.2 · 6.6 · 8.4 · 9.6 · 11 · 11.6 · 12.4 · 12.7 · 13.4 · 14.6 · 15.05.png` | `k/koyu/02-…-5.2 · 11.6 · 12.4 · 14.6.png` |
| 03 kaydet | `k/03-…-15.2 · 16 · 16.6 · 17.7 · 19.7 · 20.3.png` | `k/koyu/03-…-17.7 · 19.7.png` |
| 04 çağrı | `k/04-…-20.4 · 21.2 · 22.9 · 24.6 · 27.3.png` | `k/koyu/04-…-22.9 · 27.3.png` |
| Türevler (kök) | `kapak-a.png` = `kapak.png`, `kapak-b.png`, `kapak-c.png`, `hikaye-a.png` = `hikaye.png`, `hikaye-b.png`; `kapak-a|b|c-168.png` | `sahneler/0{1,5,6,7,8}-…/k/koyu/*-koyu.png` |

Bakış sonucu: taşma yok; yazı × çizim çakışması yok; rozet her karede `YDT · TEMEL`; karakter kadın (kanca, kapak A, çağrı kartı);
kırmızı yok (kanca `?`, sahne 02, kapak C, hikâye A mürekkep); altyazı en çok 2 satır, karaoke sesle; koyu temada okunmayan yazı yok;
hikâye B kural özeti taşır ("Does varsa fiil yalın.", A6 karşılanıyor). 168 px kapaklarda ana yazı okunur.
Kontak: `uretim-tutanagi/kontak/simple-present-temel-s3-v2-kontak.png` (4 sahne, 30 açık kare; klişe sayımı jüri işi).

| Kapı | Komut | Çıkış |
|---|---|---|
| Çakışma | `node araclar/cakisma-kapisi.mjs simple-present-temel-s3 --port 41333 --sunucu 41022 --json projeler/simple-present-temel-s3/uretim-tutanagi/kapi-duz2.json` | **0** (`kapi-duz2.txt`; 01 · 02 · 03 · 04 "çakışma yok") |
| HyperFrames | `hyperframes check .` (`sahneler/01|03|04/proje`) | 0 (×3), 0 hata (`hf-check-duz2.txt`) |
| huni-kapi | `node D/araclar/huni-kapi.mjs K/projeler/simple-present-temel-s3` | 1 (yalnız JR-1b KALDI; `huni-kapi-duz2.txt`) |
| HV-13 kart sabitliği | 03 kare çifti 17,7 ↔ 19,7 sn; kart bölgesi x 60–960, y 560–1000 | **0 px** (tam karede fark yalnız y 1022–1499: Kaydet/Gönder satırı ve altyazı) |

Ara bulgu: kapının ilk koşusu sahne 02'de 1 uyarı verdi (`es × he, she, it`, 3,89–12,64). Sebep: `elYazisi` `oge` verilince bütün grubu
kendi adıyla etiketler; etiket `ESKI` grubundaydı, kart 0 grubu "he, she, it" sayıldı. Etiket kendi grubuna (`KAPSAM`) alındı; ikinci
koşu 0 uyarı. `hyperframes check` uyarıları: rozet 26 px < 28 px taban (huni §2 değeri; ST-2 çelişkisi, şef kararı); `line_unread` tek
sahne koşusunun sahne sonu uyarısı.

## 4. Değişen dosyalar

`git diff --name-only` 57 izli dosya: BRIEF, 3 açıklama, `surumler.json`, `zaman.json`, `ortak/anlatim` 7 dosya, `ortak/kunye.js`,
`ortak/kapak` 3 PNG, sahne 01–08 kaynakları (`uret.py`, `yardim.py`, `SPEC.md`, `calistir.sh`, `sahne-02.js`, `sayfa.html`),
üretilen `proje*/index.html`, `zamanlar.json`, `nesneler.json`, `proje*/assets/*.png`. Git dışı türev: `*.wav`, `*.m4a`, kök `*.png`,
`sahneler/*/k/`. Yeni tutanak: `kapi-duz2.{txt,json}`, `hf-check-duz2.txt`, `huni-kapi-duz2.txt`, `kontak/`, bu dosya.
`surumler.json`: `ad` "S3 Shorts (27,33 sn)", `revizyonlar` r1 (02-04 kısalarıyla aynı alan düzeni).

## 5. Düzeltilmeyen maddeler

| Madde | Sebep |
|---|---|
| B4 KS-4 / HV-20b: kapak C "DOES VARSA FİİL YALIN" kuralın tamamı | J2 B sınıfı; istem "B'ye dokunma". `juri-olcutleri.md` HV-20b (15.11 akşam) bunu ölçer: J2 yeniden koşunca kalır. Kapak metni şef kararı |
| B2 HV-19, B5 KS-5, B7 vinyet, B8 §1b | J2 B sınıfı (ölçüt hatası) |
| C4 EK-4 | şefin işi (adres gidiş zamanı) |
| C6 EK-11 | Nadir dinler: yeni parçalar "He, she, it", "ile olumsuzda … döz girer" (Whisper 0,97) |
| Süre 27,33 > hedef 22–26 | yeni c2 eski cümleden 2,25 sn uzun; ≤ 35 sınırı tutar. Kısaltma yeni ses ister: şef kararı |
| HV-25 bilgi | sahne 02 altyazısı 2 satır, satır 1 41 karakter (N kararı Nadir'de) |
| JR-1b (§1b) | J2 hükmü bu düzeltmeden eski; J2 yeniden koşar (J2-OZET sıra 6) |
| Sahne `RAPOR.md`, `istem/`, taslak belgelerinde `BASIC`, kırmızı işaret, eski zaman anışı | tarihli belge; değiştirmedim. Güncel durum SPEC DUZ2 notlarında ve bu raporda |

Silinecekler: `~/Silinecekler/2026-11-15-duz2-0202S3/simple-present-temel-s3/` (`ortak-kapak/` eski karakter + ana kapak, `eski-kare/`
sahne kareleri ve kapak A kopyaları, `eski-kok-png/` kök türevler, `ara-kare/` sahne 02 ara çekim).
