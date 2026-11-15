# DUZ2-RAPOR — simple-present-temel-s3b (A/B kol b, değişken `kanca`) · J2 A düzeltmeleri + KBJ gerçek hataları · 16.11.2026

İstem: `uretim-hatti/istemler/DUZ2-0202S3.md`. Girdi: `juri/KBJ-hukum.md`, `KBC-RAPOR.md`, kol a raporu
`../../simple-present-temel-s3/uretim-tutanagi/DUZ2-RAPOR.md` (düzeltme ayrıntısı ve A3 dil denetimi orada). Üretici: Claude Opus 5.5
(`claude-opus-5-5`). Alt ajan, agy-filo, mp4, commit yok. Silinen dosya yok; taşınanlar `~/Silinecekler/2026-11-15-duz2-0202S3/simple-present-temel-s3b/`.

| Ölçüm | Değer |
|---|---|
| Düzeltilen kusur | J2 A1/TD-1 · A2/TD-2 · A3 · TD-3 · A7; KBJ HV-24 · ST-1 · EK-5b · EK-6 · AB-8 · EK-3 · HV-13 (kanıt) · ST-2 (kanıt) · EK-8 (kanıt) |
| Yeniden sentez | **0 karakter** (el.py kapı önbelleği 9 / 9); `cumle-2.wav` kol a'dan kopya (`cmp` eş); c1 (değişken) değişmedi |
| Süre | 24,43 → **26,68 sn** (≤ 35 ✓; hedef 22–26 ✗, +0,68) |
| İlk söz · kanca | 1,00 sn · kanca sahnesi 0,00–3,24 · kanca cümlesi sözcük sonu 3,32 (değişmedi; KBC açık nokta 4) |
| Whisper en düşük | 0,93 (c3, kol a ile aynı ses); c1 1,00; c2 1,00 · 0,97 · 1,00 · 1,00 |
| Çakışma kapısı | çıkış **0** (4 sahne, 0 uyarı) |
| AB-8 taraması | **0 satır** |
| AB-9 | c2, c3, c4 sha256 kol a ile eş |
| AB-3 | 31 kare çiftinin 29'u 0 px; 2 fark beklenen (§3) |
| `diff -rq` | 190 satır (başlık + 189), **beklenmeyen 0** (§4) |
| `huni-kapi.mjs --kol-a` | 21 GEÇTİ · 2 KALDI (JR-1b; AB-2 yalnız sahne 03/04 `zamanlar.json`, araç sınıf kuralı eksik, §4) |

## 1. Düzeltmeler

| # | Kusur | Dosya | Önce → sonra | Kanıt |
|---|---|---|---|---|
| 1 | A1/TD-1 · KBJ HV-24 | `senaryo.json` `giris.rozetler`, `ortak/kunye.js`, `BRIEF-S3.md` (kol a ile `cmp` eş), sahne 01–08 `yardim.py`, `06-…/uret.py`, `SPEC.md` | `YDT · BASIC` → `YDT · TEMEL` | `huni-kapi` HV-24 GEÇTİ; bütün kol b karelerinde `YDT · TEMEL` |
| 2 | A3 · KBJ EK-5b (i) | `senaryo.json` c2 (kol a `cumleler[1]` birebir) | "Olumsuzda ve soruda does girer, s ona geçer." → "He, she, it ile olumsuzda ve soruda does girer; s ona geçer." | `senaryo.json` fark denetimi: kol a ile fark yalnız `cumleler[0]`, `giris.satir1/2`, `meta.kapak.satir1/2` |
| 3 | AB-9 | `ortak/anlatim/cumle-2.wav` | kol a dosyası kopyalandı (`cp -p`; el.py önbellek koşusunun yazdığı dosya ile `cmp` eş) | sha256 `ea1bb8233779` iki kolda; günlük `ses-sentez-DUZ2.log` |
| 4 | Zaman türevleri | `sentez.wav` (+ rapor), `sureler.json`, `sozcukler.json`, `baslar.json`, `altyazi.json`, `METIN.md`, `anlatim.wav/m4a/.imza`, kök `zaman.json` | yeniden kuruldu | §2 |
| 5 | TD-3 · KBJ EK-5b (ii) | `senaryo.json` `meta.canAlici[0]`, `surumler.json` `video.canAlici[0]` | "geniş zaman eki = s" satırı çıkarıldı | `grep -c "geniş zaman eki ="` = 0 |
| 6 | A2/TD-2 | `ortak/kapak/karakter.png`, `ana-kapak.png`, `ana-kapak-koyu.png` | erkek / eski ana kapak → ana paket dosyaları (`5a902b40…`, `7f714514…`, `7e948a3b…`) | `sha256sum` |
| 7 | A2 kanca yerleşimi | `sahneler/01-hyperframes-kanca/uret.py` (kol b sürümü) | kol a ile aynı yamalar: görsel boyu dosyadan, daire merkezi oranla, `karakter_ustu()` daire–`?` uzaklığı | karakter üst 888 (kol a ile aynı konum); `kapak-a.png` |
| 8 | A7 · KBJ ST-1 | `01-…/uret.py` (`?` mürekkep); `02-…/sahne-02.js` (✗ ve üstü çizgi mürekkep, çizilen `es` soluk) | kırmızı → mürekkep | `k/01-…-2.5 · 2.8.png`, `k/02-…-10.95 · 11.75.png` |
| 9 | A3 sahne 02 | `sahne-02.js` (kol a ile aynı kod) | sözcük sırası +4, KARE 348, kapsam etiketi `he, she, it` | `k/02-…-4.55 · 5.95.png` |
| 10 | KBJ AB-8 | `ortak/kunye.js` `KOK`, `sahneler/02-paperjs-deger/{sahne-02.js, sayfa.html, kalem-paper.js, calistir.sh}` | kol a yolu → kol b yolu; dosyalar paket adı dışında kol a ile bayt eş; sahne 02 `t_bas` kodda değil, paketin `zaman.json` kaydında (kol b 3,24) | AB-8 taraması 0 satır (aşağıda); `huni-kapi` AB-8 ve AB-3 GEÇTİ |
| 11 | KBJ AB-8 (önbellek) | `sahneler/05–08/proje/.hyperframes/` | kol a yolu taşıyan snapshot önbelleği → Silinecekler (`proje-hyperframes/`) | tarama 0 |
| 12 | KBJ EK-3 | `sahneler/*/k/`, `01-…/proje-ka*` | kol a'dan kopya kareler ve KBC kareleri → Silinecekler (`eski-kare/`); 01–04 açık + koyu ve kapak A kol b'den yeniden çekildi | §3 |
| 13 | KBJ EK-6 | `aciklama-a.md` (= `aciklama.md`), `aciklama-b.md` | başlık `simple-present-temel-s3` → `simple-present-temel-s3b (A/B kol b, değişken kanca)`; sürüm `s3-aciklama-*` → `s3b-aciklama-*`; süre 25,08 → 26,68 sn (kol b); kaynak satırı kol a tutanağını gösterir; `kapak-b|c.png`, `hikaye-a|b.png` atfı "kol a paketinde (huni A/B §4)"; kural cümlesi (A3) | `diff` kol a ↔ kol b açıklama: yalnız bu satırlar + `utm_content` |
| 14 | Grup türevi kaynakları | `sahneler/03–08` `uret.py`, `yardim.py`, `SPEC.md`, `nesneler.json` (kol a dosyası `cp -p`); `proje/index.html` (`ONIZLE_YALNIZ=1 calistir.sh --tema acik`) | kol a ile aynı | 03–08 `proje/index.html` kol a ile `cmp` eş; kol b türev PNG üretmez (AB §4) |
| 15 | `surumler.json` | `s3b` satırı | `ad` "S3b Shorts (26,68 sn)"; `revizyonlar` r1 | `json.load` geçti |

AB-8 taraması (istem komutu):

```
$ grep -rn "simple-present-temel-s3/" K/projeler/simple-present-temel-s3b --include=*.js --include=*.html --include=*.json --include=*.py
(çıktı yok) · satır 0
```

Kol b içinde simge bağı 0 (`find -type l`). `surumler.json` `varyant` alanı paket yolu taşımaz. `.md` belgelerindeki kol a anışı
(tarihli SPEC/RAPOR/tutanak) AB-8 dışıdır.

## 2. Süre, ilk söz, Whisper

| Ölçü | Kol b | Kol a | Sınır | Durum |
|---|---|---|---|---|
| Toplam süre | 26,68 sn (ffprobe 26,680000) | 27,33 sn | ≤ 35 (hedef 22–26) | sınır içinde; hedef iki kolda aşılır |
| İlk söz | 1,00 | 1,00 | ≤ 1 | ✓ |
| Kanca sahnesi bitişi | 3,24 | 3,89 | ≤ 4 | ✓ |
| Kanca cümlesi sözcük sonu | 3,32 | 3,89 | bilgi | `gider?` sonu ses bitişini 0,08 sn aşar (KBC; değişmedi) |
| Whisper en düşük | 0,93 | 0,93 | ≥ 0,90 | ✓ |

| Cümle | Kol b metni | sha256 (a / b) | Whisper |
|---|---|---|---|
| 1 (değişken) | Olumsuzda s nereye gider? | `132a1a3113c2` / `5ff705528f78` | 1,00 |
| 2 | He, she, it · ile olumsuzda ve soruda does girer; s ona geçer. · Fiile s gelmez. · He doesn't go. Does she go? | `ea1bb8233779` = | 1,00 · 0,97 · 1,00 · 1,00 |
| 3 | Does varsa fiil yalın. · Bir arkadaşına gönder; o da karıştırıyor. | `569e61237aa4` = | 0,93 · 1,00 |
| 4 (öğrenci) | Bu sadece başlangıç. · Dersin tamamı YDS Publishing YouTube kanalında. | `6a9927c66d00` = | 1,00 · 1,00 |

| Sahne (sn) | Kol b | Kol a |
|---|---|---|
| 01 kanca | 0,00–3,24 (109 kare) | 0,00–3,89 (129 kare) |
| 02 değer | 3,24–14,44 (348 kare) | 3,89–15,09 (348 kare) |
| 03 kaydet | 14,44–19,70 | 15,09–20,35 |
| 04 çağrı | 19,70–26,68 | 20,35–27,33 |

## 3. Kareler, AB-3, kapı

| Sahne / türev | Açık (küresel sn) | Koyu |
|---|---|---|
| 01 kanca (değişken) | `k/01-…-0 · 0.9 · 1.4 · 2.12 · 2.5 · 2.8 · 3 · 3.23.png` | `k/koyu/01-…-2.12 · 2.8.png` |
| Kapak A | `kapak-a.png` = `kapak.png` (t 0,90, altyazısız), `kapak-a-168.png` | `sahneler/01-…/k/koyu/kapak-a-koyu.png` |
| 02 değer | `k/02-…-3.25 · 4.55 · 5.95 · 7.75 · 8.95 · 10.35 · 10.95 · 11.75 · 12.05 · 12.75 · 13.95 · 14.4.png` | `k/koyu/02-…-4.55 · 10.95 · 11.75 · 13.95.png` |
| 03 kaydet | `k/03-…-14.55 · 15.35 · 15.95 · 17.05 · 19.05 · 19.65.png` | `k/koyu/03-…-17.05 · 19.05.png` |
| 04 çağrı | `k/04-…-19.75 · 20.55 · 22.25 · 23.95 · 26.65.png` | `k/koyu/04-…-22.25 · 26.65.png` |

Bakış sonucu: taşma, çakışma, okunmayan yazı yok; rozet `YDT · TEMEL`; kanca `?` mürekkep, karakter kadın ve `?`'i gösterir;
çağrı kartında yeni ana kapak; altyazı en çok 2 satır. Kontak `uretim-tutanagi/kontak/simple-present-temel-s3b-v2-kontak.png` (31 kare).

AB-3 (değişken dışı sahneler aynı içerik, aynı göreli an): kol b t ↔ kol a t + 0,65 sn, eşik 24/255 (`ab3-duz2.txt`).

| Çiftler | Sonuç |
|---|---|
| 02: 12 açık + 4 koyu çift | 14 çift 0 px; 3,25 ↔ 3,9: 8.675 px yalnız altyazı bandında (y 1449–1494: c1 altyazı kuyruğu, değişken); 4,55 ↔ 5,2 (açık + koyu): 11 px (etiket çizim başı; kol a 16,5 / kol b 16,5 kare yuvarlaması, 1 kare) |
| 03: 6 açık + 2 koyu, 04: 5 açık + 2 koyu | 15 çift 0 px |
| Kanal bandı (y 280–350) | 31 çiftte 0 px |

HV-13: kart bölgesi (x 60–960, y 560–1000) 17,05 ↔ 19,05 sn → **0 px**. Sahne 03/04 `proje/index.html` kol a ile bayt eş.

| Kapı | Komut | Çıkış |
|---|---|---|
| Çakışma | `node araclar/cakisma-kapisi.mjs simple-present-temel-s3b --port 41333 --sunucu 41022 --json projeler/simple-present-temel-s3b/uretim-tutanagi/kapi-duz2.json` | **0** (`kapi-duz2.txt`) |
| HyperFrames (KBJ ST-2) | `hyperframes check .` (`sahneler/01|03|04/proje`) | 0 (×3), 0 hata (`hf-check-duz2.txt`); uyarılar: rozet 26 px < 28 (huni §2 değeri, şef kararı), kanca `line_unread` |
| huni-kapi | `node D/araclar/huni-kapi.mjs K/projeler/simple-present-temel-s3b --kol-a K/projeler/simple-present-temel-s3` | 1 (`huni-kapi-duz2.txt`; §4) |

## 4. `diff -rq` sınıflaması

Çıktı `diff-rq-duz2.txt` (189 satır), sınıflama `siniflama-duz2.txt` (betik kuralları dosya başında).

| Sınıf | Satır | Beklenen mi |
|---|---|---|
| tutanak (`uretim-tutanagi/`) | 30 | evet: iki kolun ayrı tutanağı |
| değişken sahne `01-hyperframes-kanca` | 41 | evet: kaynak, proje, kapak A kopyaları, kareler, önbellek |
| `senaryo.json` | 1 | evet: cümle 1 + kanca başlığı |
| ses ve zaman türevi (`cumle-1.wav`, `sentez.wav`+rapor, `anlatim.*`, `sozcukler`, `sureler`, `baslar`, `altyazi`, `METIN`, `zaman.json`) | 12 | evet: değişken cümle 1 sesi (−0,65 sn) |
| sahne 03/04 `zamanlar.json` | 2 | evet: küresel `t_bas` −0,65 sn; `proje/index.html` bayt eş |
| bağımsız kopya (`ortak/kunye.js`, sahne 02 `sahne-02.js`, `sayfa.html`, `kalem-paper.js`, `calistir.sh`) | 5 | evet: AB-8 kol b yolu; paket adı dışında bayt eş |
| `surumler.json` | 1 | evet |
| açıklama (3 dosya) | 3 | evet: `utm_content`, EK-6 satırları |
| kapak A (`kapak.png`, `kapak-a.png`, `kapak-a-168.png`) | 3 | evet: kol b kanca karesi |
| grup türevi (kol a'da `kapak-b|c`, `hikaye*`, `kapak-b|c-168`) | 7 | evet: huni A/B §4 |
| QA kareleri (`sahneler/02–08/k`) | 66 | evet: her kol kendi anında; kol b 05–08 türev karesi üretmez |
| `__pycache__` | 6 | evet: derleme önbelleği (mutlak yol gömülü) |
| `proje/.hyperframes` | 12 | evet: araç önbelleği; kol b 05–08 snapshot koşmaz |
| **Beklenmeyen** | **0** | — |

`huni-kapi` AB-2 KALDI: "2 beklenmeyen: `sahneler/03-hyperframes-kaydet/zamanlar.json`, `sahneler/04-hyperframes-cagri/zamanlar.json`". İki dosya
sahne üreticisinin kaydıdır; içinde küresel `t_bas` ve `kuresel` değerleri var. Kol b kancası 0,65 sn kısa olduğu için bu değerler
kol a'dan 0,65 sn erkendir. Fark doğru ve kaçınılmazdır; kol a dosyasını kol b'ye kopyalamak kapıyı geçirir ama yanlış veri yazar.
Kapının `farkSinifi()` kuralı `zaman.json` dosyasını "zaman türevi" sayar, `sahneler/*/zamanlar.json` dosyasını saymaz. Öneri (araç
işi, bu istemin yazma alanı dışında): kanca/kapanış değişkeninde `sahneler/<k>/zamanlar.json` farkı "zaman türevi" sınıfına girer.
Öteki KALDI JR-1b: jüri dosyası (KBJ, 15.11 23:40) bu düzeltmeden eski; jüri yeniden koşar.

## 5. KBJ maddeleri

| KBJ | Hüküm | Bu tur |
|---|---|---|
| HV-24 | hayır | düzeltildi (#1) |
| ST-1 | hayır | düzeltildi: kanca `?` ve sahne 02 işaretleri mürekkep (#8) |
| EK-5b | hayır | düzeltildi (#2, #5) |
| EK-6 | hayır | düzeltildi (#13) |
| AB-8 | hayır | düzeltildi (#10, #11); tarama 0 |
| HV-13 | kanıt yok | kanıt: kol b kare çifti 0 px (§3) |
| EK-3 | kanıt yok | kol b'nin bütün sahne kareleri kol b'den (§3) |
| ST-2 | kanıt yok | `hf-check-duz2.txt` (0 hata; rozet 26 px uyarısı şef kararı) |
| EK-8 | kanıt yok | kontak üretildi (31 kare); klişe sayımı jürinin işi |
| EK-11 | kanıt yok | Nadir dinler (`s`, `gider?`; yeni c2 parçaları kol a ile ortak) |
| HV-13 kapanış değişkeni cümlesi, HV-17, HV-20 ve HV-21 (kol b), AB-4/5/7 | ölçüt / uygulanmaz | dokunmadım (istem) |

## 6. Düzeltilmeyen maddeler

| Madde | Sebep |
|---|---|
| Süre 26,68 > hedef 22–26 | c2 kol a ile aynı uzar (+2,25 sn); ≤ 35 tutar. Kısaltma yeni ses ister: şef kararı |
| Kanca cümlesi sonu 3,32 > kanca sahnesi 3,24 | KBC tasarımı (çıkış içerik sonuna bağlı); bu istemin kusur listesinde yok |
| `huni-kapi` AB-2 (03/04 `zamanlar.json`) | araç sınıf kuralı eksik (§4); veri doğru |
| JR-1b | jüri yeniden koşar |
| `meta.kimlik` `02-02-ydt-temel-s3` | iki kolda aynı; AB-8 kimlik alanını saymaz; KBC kararı korundu |
| Tarihli belgeler (`SPEC.md`, `RAPOR.md`, KBC/BK tutanakları) | kol a yolu ve eski değer anışı belge geçmişidir; SPEC 01/02 başına DUZ2 notu eklendi |

Silinecekler: `~/Silinecekler/2026-11-15-duz2-0202S3/simple-present-temel-s3b/` (`ortak-kapak/`, `eski-kare/`, `eski-kok-png/`,
`proje-hyperframes/`, `yanlis-mkdir/`: bu oturumda glob eşleşmeyen `mkdir` komutunun açtığı 3 boş dizin).
