# DUZ2-0204S2 raporu — `02-04-ydt-temel-s2b` (A/B kol b, değişken `kapanis`) · J2 A sınıfı + KBJ gerçek hata düzeltmeleri · 15.11.2026

| Ölçüm | Değer |
|---|---|
| Düzeltilen kusur | A1 / TD-1 (rozet), A6 kaynağı (kol a ile eş), TD-4 (bayat UTM notu), KBJ AB-X1 = AB-8 (kol a yolu), KBJ "kol a'dan kopya kareler", KBJ E3 (açıklama üst bilgisi) |
| Ses | değişmedi: yeniden sentez 0 cümle |
| Süre | 29,49 sn (değişmedi; kol a 29,41; kabul ≤ 35 sağlandı, hedef 22–26 aşıldı) |
| Whisper | 10 / 10 parça 1,00 (en düşük 1,00) |
| Kareler | 50 sahne karesi (`k/`), açık + koyu; hepsi kol b'den çekildi. Kök türev yok (AB §4) |
| AB-8 taraması | 0 satır |
| `diff -rq` | 107 satır; beklenmeyen 0 |
| Çakışma kapısı | çıkış 0 (4 sahne, çakışma yok) |
| mp4 | yok |
| Üretici model | Claude Opus 5.5 (`claude-opus-5-5`) |

Girdi: `uretim-hatti/raporlar/J2-OZET-1511.md`; `juri/KBJ-hukum.md`; `KBC-RAPOR.md`; `D/.claude/docs/huni-ab-sozlesme.md` §2, §4; `juri-olcutleri.md` (AB-8, AB-9).
Kol a raporu: `../../02-04-ydt-temel-s2/uretim-tutanagi/DUZ2-RAPOR.md`.

## 1. Düzeltmeler

| # | Kusur | Dosya | Önce → sonra | Kanıt |
|---|---|---|---|---|
| 1 | A1 / TD-1 (KBJ E2; ölçüt HV-24) | 13 ortak dosya kol a'dan kopya: `BRIEF-S2.md`, `ortak/kunye.js`, `sahne-02.js`, `yardim.py` × 7, `uret.py` 04, 06, 07; `ortak/anlatim/senaryo.json` ayrı | `YDT · BASIC` → `YDT · TEMEL` | Kopyadan önce kimlik: 13 dosyanın her biri kol a'nın düzeltme öncesi hâliyle (`git show HEAD:…`) bayt aynı (`cmp`). `grep BASIC` kaynak ve çıktı: 0 |
| 2 | A6 kaynağı | `sahneler/07-hyperframes-hikaye-b/uret.py` (kol a kopyası) | ipucu → kural özeti `Genel: wears · Şu an: is wearing` | Kol b'de hikâye türevi yok (AB §4); kaynak iki kolda eşit kalır. `07…/k/` kareleri kol a ile piksel farkı 0 |
| 3 | TD-4 (KBJ E4) | `aciklama.md`, `aciklama-a.md` (2 satır), `aciklama-b.md` (1 satır) | bayat "S1 küçük harf" DİKKAT notu → silindi | `grep ing-ydt-gr aciklama*.md`: 0 |
| 4 | KBJ AB-X1 / AB-8 | `ortak/kunye.js` (`KOK`), `sahneler/02-paperjs-ornek/sahne-02.js` (2 içe aktarım), `kalem-paper.js` (2), `sayfa.html` (1) | `/projeler/02-04-ydt-temel-s2/…` → `/projeler/02-04-ydt-temel-s2b/…` (6 yol) | Paket adı dışında fark 0 (`diff <(sed s/s2b/s2/ …) …`). AB-8 taraması §4 |
| 5 | KBJ "kol a'dan kopya kareler" | bütün `sahneler/*/k/` kareleri; `proje/.hyperframes/video-state.json` (04–07) | kol a'dan `cp -a` kopyası → kol b'den yeniden çekildi; snapshot durumu önce kol a kare yolunu gösteriyordu → kol b yolu | §3; değişken dışı 34 kare kol a ile piksel farkı 0 |
| 6 | KBJ E3 | `aciklama-a.md`, `aciklama-b.md`, `aciklama.md` üst bilgisi (satır 1, 3, 4, 6) | `# 02-04-ydt-temel-s2`, `s2-aciklama-a/b`, `29,41 sn`, kol b'de olmayan taslak dosyasına kaynak → `# 02-04-ydt-temel-s2b`, `s2b-aciklama-a/b`, `29,49 sn`, kaynak "kol a açıklamasının kopyası; yalnız `utm_content` değişti" | Dosya satır 1–6; yayın metni değişmedi |
| 7 | C1 (HV-22) yan ürünü | `uretim-tutanagi/cakisma-DUZ2.json`, `cakisma-DUZ2.txt` | yeni koşu | §5 |

Tek değişken kuralı korundu: değişken (cümle 3 parça 2, cümle 4 parça 1; sahne 08 ve 03) bu işte değişmedi. Bütün düzeltmeler iki kolda eş.

## 2. Ses, süre ve Whisper

| Ölçü | Kol a | Kol b | Not |
|---|---|---|---|
| Toplam (`ffprobe anlatim.m4a`) | 29,41 sn | 29,49 sn | değişmedi; ≤ 35 sağlandı; hedef 22–26 aşıldı |
| İlk söz ("Genel" t0) | 1,00 | 1,00 | ≤ 1 sn: sınırda |
| Kanca cümlesi bitişi ("mı?" t1) | 2,92 | 2,92 | kanca ≤ 4 sn sağlandı; sahne 01 2,84'te biter, son hece 0,08 sn taşar |
| Whisper | 10 / 10 · 1,00 | 10 / 10 · 1,00 | ≥ 0,90 |
| `cumle-1.wav` | `0b0dafd59a98` | `0b0dafd59a98` | AB-9: metni aynı cümle, sha256 eşit |
| `cumle-2.wav` | `1d805b981216` | `1d805b981216` | AB-9: metni aynı cümle, sha256 eşit |
| `cumle-3.wav` | `720b3d7cc552` | `597582d3ddfd` | değişken cümlesi (parça 2) |
| `cumle-4.wav` | `b192db36b66b` | `8f69da650730` | değişken cümlesi (parça 1) |
| Yeniden sentez | 0 | 0 | ses dosyaları bu oturumdan önce yazıldı (kol b `anlatim.m4a` 22:53) |

AB-9 notu: cümle düzeyinde koşul sağlanır. Parça düzeyinde çekirdek cümle (4.2) ve 3.1 sesi iki kolda bayt aynı değildir: `el.py` önbellek
anahtarı cümle içindeki komşu parçayı içerir (`previous_text` / `next_text`). Parça eşitliği iki kolda cümle bölümünü değiştirmeyi ister; kol a
sesi de yeniden sentezlenir. Bu istemin A listesinde yok; karar şefte.

## 3. Kareler (hepsi kol b'den)

Yöntem: 01, 03, 08 `ONIZLE_YALNIZ=1 bash calistir.sh --tema acik` (HTML; render yok), sonra `node araclar/sahne-kare.mjs 02-04-ydt-temel-s2b <sahne> <t…> <dizin> --tema acik|koyu --port 41333 --sunucu 41022`.
Durağan 04–07: `bash calistir.sh --tema koyu` (kare sahne `k/` içine), sonra `ONIZLE_YALNIZ=1 … --tema acik` + `hyperframes snapshot . --at 0.5 --no-end --keep -o ../k`
(çalıştırıcı açık temada kök PNG yazar; kol b'de kök türev olmadığı için elle çektim), son olarak `ortak/tema_damga.py <sahne> acik`.

| Sahne | Açık | Koyu | Kol a ile piksel farkı |
|---|---|---|---|
| 01 kanca | 0 · 0,9 · 1,5 · 2,4 · 2,5 · 2,6 · 2,8 | 0,9 + `kapak-a-koyu.png` | 0 (9 / 9) |
| 02 değer | 2,84 · 10,1 · 17,35; `k/ara/` 4,9 · 7,6 · 12 · 14,6 · 16,1 | 14,9 | 0 (9 / 9) |
| 04–07 durağan | `k/at-0.5s.png` × 4; `07…/k/qa/` kırpım × 2 | `k/koyu/at-0.5s.png` × 4, `-koyu.png` × 4, kırpım × 1 | 0 (15 / 15) |
| 08 kaydet (değişken) | 17,41 · 20,5 · 21,2 · 21,7 · 22,4 · 22,82 | 17,41 · 21,7 · 22,82 | 17,41: 0; ötekiler değişken |
| 03 çağrı (değişken) | 22,83 · 24 · 24,6 · 26,8 · 29,48 | 22,83 · 24,6 · 29,48 | değişken (zaman kayması +0,08) |

Baktıklarım (Read; 08 ve 03 kontak sayfası; değişken dışı kareler kol a ile piksel aynı, kol a karelerine baktım): taşma yok, çakışma yok,
okunmayan yazı yok. Rozet her karede `YDT · TEMEL`; 03'te künye ve ana kapak kartı aynı rozet. Vizör 20,5'te çiziliyor, 21,2'de köşeler tam, 21,7'de dolu (deklanşör 21,35);
"Konu burada bitmiyor." 88 px Fredoka, kapak 24,97'de gelir. Altyazı 1400–1550 bandında. Karakter yalnız ana kapak kartında (kadro ile aynı).

Dokunulmayan kanıt: `uretim-tutanagi/kare/` (KBC koşusunun 3 karesi; tutanak).

## 4. AB-8 taraması

Komut: `grep -rn "02-04-ydt-temel-s2/" /home/sef/01dev/_worktrees/kalem-0204/projeler/02-04-ydt-temel-s2b --include=*.js --include=*.html --include=*.json --include=*.py`
Çıktı: **boş** (çıkış 1 = eşleşme yok). `surumler.json` `varyant` alanı paket yolu taşımaz (`{"grup": "s2", "kol": "b", …}`).
Önceki durum (bu işten önce): 14 satır: `sayfa.html:7`, `sahne-02.js:4–5`, `kalem-paper.js:11–12`, `ortak/kunye.js:8` ve 04–07 `proje/.hyperframes/video-state.json` (8 satır, kol a kare yolları).
Kalan kesişme (AB-8 dışı): HyperFrames tema çevirici logo yolu `/projeler/present-continuous/ortak/logo/` (iki kolda aynı, ortak varlık).

## 5. Çakışma kapısı

Komut: `node araclar/cakisma-kapisi.mjs 02-04-ydt-temel-s2b --port 41333 --sunucu 41022 --json projeler/02-04-ydt-temel-s2b/uretim-tutanagi/cakisma-DUZ2.json`
Çıkış kodu: **0** (49 sn). 01 13 örnek · 02 60 · 08 23 · 03 28; çakışma yok.

## 6. `diff -rq` sınıflaması

Komut: `diff -rq projeler/02-04-ydt-temel-s2 projeler/02-04-ydt-temel-s2b` → `uretim-tutanagi/DUZ2-diff-rq.txt` (107 satır; önce 85). Her satır bir kuralla sınıflandı.

| Sınıf | Satır | Beklenen mi | Gerekçe |
|---|---|---|---|
| `uretim-tutanagi/` | 28 | evet | tutanak ve kanıt, kol başına |
| Değişken sahne 08 / 03 (üretici, çalıştırıcı, HTML, zaman/olay, `vizor.svg`, kol başına QA kareleri, `k/ara`) | 35 | evet | değişken (KBC ile aynı sınıf) |
| Zaman ve ses türevi (`zaman.json`, altyazı, başlar, sözcükler, süreler, METIN, sentez + rapor, anlatım wav/m4a/imza) | 11 | evet | değişken cümlelerinin türevi |
| `cumle-3.wav`, `cumle-4.wav` | 2 | evet | değişken cümleleri |
| `senaryo.json` | 1 | evet | yalnız cümle 3 parça 2 ve cümle 4 parça 1 (+ iki `metin`); rozet iki kolda `YDT · TEMEL` |
| `surumler.json` | 1 | evet | kol kaydı + DUZ2 notu |
| Açıklama × 3 | 3 | evet | `utm_content` (`s2b-*`) + E3 üst bilgisi (satır 1, 3, 4, 6) |
| Kök türev PNG yalnız kol a'da (kapak × 4, hikâye × 3) | 7 | evet | AB §4: türev gruba ait |
| **Yeni:** AB-8 yolu (`ortak/kunye.js`, `kalem-paper.js`, `sahne-02.js`, `sayfa.html`) | 4 | evet | bu işin AB-8 düzeltmesi; paket adı dışında fark 0 |
| **Yeni:** `__pycache__/yardim.cpython-310.pyc` × 7 | 7 | evet | her kol kendi `uret.py`'sini koştu; pyc paket yolunu (`co_filename`) gömer. Kaynak `yardim.py` iki kolda bayt aynı. Git dışı. Önce kol b pyc'leri kol a yolunu taşıyan kopyaydı |
| **Yeni:** `proje/.hyperframes/history-id`, `video-state.json` (04–07) | 8 | evet | snapshot durumu; kol b kendi kare yolunu yazar (önce kol a yolu). Git dışı |
| **Beklenmeyen** | **0** | — | — |

Sahne 01, 02 (yol dışında), 04–07 (`proje/index.html`, `nesneler.json`, `RAPOR.md`, kareler) ve `ortak/` (yol dışında) iki kolda bayt aynı.

## 7. Düzeltilmeyen maddeler

| Madde | Sınıf | Sebep |
|---|---|---|
| HV-13 (yer imi + "Kaydet" yok) | **ölçüt** | Güncel HV-13 kapanış `ekran-goruntusu` için vizör + "Ekran görüntüsü al" bekler; kart 2 sn sabitliği KBJ'de ölçüldü (2,99 sn). Dokunmadım |
| HV-17 "YEDESE" | **ölçüt** | Güncel HV-17 bu dökümü beklenen davranış sayar |
| HV-20, HV-21 (kol b'de türev yok) | **ölçüt** | Güncel ölçüt: A/B kol b'de uygulanmaz (türev kol a'da) |
| AB-4, AB-5, AB-7 | **ölçüt** (yayın sonrası) | Üretim jürisi "uygulanmaz (yayın sonrası)" yazar |
| E1: `Ekran görüntüsü` iki sözcük 20,27'de, `görüntüsü` seste 20,71 | şef kararı | Madde dışı bulgu. Yazı ifadenin ilk sözcüğünde açılır; değişken sahnesine dokunmak tek değişkeni bozmaz ama tasarım kararıdır |
| E5: açıklama ilk satırı "kaydet", video "ekran görüntüsü al" | şef kararı | İlk satır huni §4'te sabit; A/B yorumu |
| E6: açıklama `kapak-a.png` / `hikaye-*.png` atfı | şef kararı | AB §4 / §5: türev gruba ait; API eşlemesi uygulama tarafında |
| `senaryo.json` `meta.kimlik` = `02-04-ydt-temel-s2` | şef kararı | KBC açık nokta 7; yol değil (AB-8 dışı). Panel bu alanı okuyorsa `…-s2b` olmalı |
| Parça düzeyinde ses eşitliği (3.1, 4.2) | şef kararı | §2 AB-9 notu |
| Süre 29,49 > hedef 22–26 | açık nokta | iki kola birlikte kısaltma (KBC açık nokta 1) |

## 8. Değişen dosyalar

Kaynak: `BRIEF-S2.md`, `ortak/kunye.js`, `ortak/anlatim/senaryo.json`, `sahneler/02-paperjs-ornek/{sahne-02.js,kalem-paper.js,sayfa.html}`,
`sahneler/0{1,3,4,5,6,7,8}-*/yardim.py`, `sahneler/0{4,6,7}-*/uret.py`, `aciklama{,-a,-b}.md`, `surumler.json` (`revizyonlar` r1).
Türetilmiş: `sahneler/*/proje/index.html`, `nesneler.json` (04–07), `olaylar.json`, `proje/assets/logo.svg`, `RAPOR.md` "Tema:" satırı (04–07), `k/` kareleri.
Silinecekler: `~/Silinecekler/2026-11-15-duz2-0204S2/02-04-ydt-temel-s2b/` (kol a'dan kopya 3 yakın kırpım; `LISTE.md`).
