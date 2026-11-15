# DUZ2-0202S2 raporu — `simple-present-temel-s2b` (A/B kol b, değişken `kapanis`) · J2 A sınıfı + KBJ gerçek hata düzeltmeleri · 16.11.2026

| Ölçüm | Değer |
|---|---|
| Düzeltilen kusur | kol a düzeltmeleri birebir: A1 / TD-1 (rozet), A2 / TD-2 (karakter + ana kapak), A3 + A4 (= KBJ E1), TD-3 (`canAlici`), KS-4 / HV-20b kaynağı; KBJ E2 = AB-8 (kol a yolu), KBJ "kol a'dan kopya kareler", KBJ E4 (açıklama üst bilgisi, rozet, kapak C karakteri) |
| Yeniden sentez | 1 cümle (c3 = değişken cümlesi; 3 parça, 88 karakter ≈ 0,43 TL); c1, c2 sha256 kol a ile eş (AB-9); c4 değişmedi |
| Süre (`ffprobe anlatim.m4a`) | 25,73 → **27,00 sn** (kabul ≤ 35 sağlandı; hedef 22–26 1,00 sn aşıldı; kol a 26,68) |
| İlk söz · kanca cümlesi bitişi | 1,00 sn · 3,48 sn (kol a ile aynı; kanca ≤ 4) |
| Whisper | 9 / 9 parça 1,00 (en düşük 1,00; önceki 2·3 = 0,92 bu koşuda 1,00) |
| AB-8 taraması | **boş** (çıkış 1 = eşleşme yok) |
| `diff -rq` | 103 satır; **beklenmeyen 0** |
| Kareler | bütün sahne kareleri kol b'den yeniden çekildi (01–04 açık + koyu; 05–08 `k/` açık + koyu; 01 kapak A `k/ka-*`). Kök türev yok (huni-ab §4) |
| Çakışma kapısı | çıkış **0** (4 sahne, çakışma yok) |
| mp4 | yok |
| Üretici model | Claude Opus 5.5 (`claude-opus-5-5`) |

Girdi: `uretim-hatti/raporlar/J2-OZET-1511.md`, `juri/KBJ-hukum.md`, `KBC-RAPOR.md`, `D/.claude/docs/huni-ab-sozlesme.md` §2–§4, `juri-olcutleri.md` (AB-3, AB-8, AB-9, HV-13).
Kol a raporu: `../../simple-present-temel-s2/uretim-tutanagi/DUZ2-RAPOR.md` (düzeltme ayrıntısı, öneri denetimi, terim birliği orada).
Not: 15.11 gecesi kol b `el.py` koşusu bellek arızasında öldü (`ses-sentez-DUZ2.log` 00:24 `Killed`); arkasından koşan türev adımları eski sesle çalışmıştı.
Bu oturum sentezi 00:39'da ön planda (`timeout 1500`) yeniden koştu, bütün türevleri yeniden kurdu.

## 1. Düzeltmeler

| # | Kusur | Dosya | Önce → sonra | Kanıt |
|---|---|---|---|---|
| 1 | A1 / TD-1 (HV-24, KBJ E4) | 18 dosya kol a'dan kopya: `BRIEF-S2.md`, `ortak/kunye.js`, 7 `yardim.py`, `uret.py` 05, 06, 07, SPEC 01, 03, 05, 06, 07, 08 | `YDT · BASIC` → `YDT · TEMEL` (+ kol a'nın A3/A4 kaynak değişiklikleri) | Kopyadan önce: 18 dosyanın her biri kol a'nın düzeltme öncesi hâliyle (`git show HEAD:…`) bayt aynıydı (`cmp`). `grep BASIC` kaynak ve çıktı: 0 |
| 2 | A2 / TD-2 (KBJ E4) | `ortak/kapak/karakter.png`, `ana-kapak.png`, `ana-kapak-koyu.png` | eski (erkek) → ana paketin dosyaları (`5a902b40…`, `7f714514…`, `7e948a3b…`) | sha256 kol a ve ana paketle eş; eski dosyalar `~/Silinecekler/2026-11-15-duz2-0202S2/simple-present-temel-s2b/ortak/kapak/` |
| 3 | A3 + A4 = KBJ E1 (ses) | `ortak/anlatim/senaryo.json` c3 (önceki oturum) | `…: Simple Present. Ekran görüntüsü al, sınav günü bak.` → `…: çoğunlukla Simple Present. Ekran görüntüsü al, sınav günü bak.` | `diff` kol a ↔ kol b senaryo: yalnız c3·3, c4·1 ve iki `metin` |
| 4 | A3 + A4 (kart, değişken sahnede) | `sahneler/03-hyperframes-kaydet/uret.py` | kol a ile aynı kart değişikliği; sözcük sırası kol b'ye göre (`çoğunlukla` 4, `Simple` 5, `Present` 6, çerçeve `al,` 9) | kol a ↔ kol b `uret.py` farkı düzeltmeden önce 71 satır, sonra 71 satır (yalnız değişken kalıp). Kart bölgesi (x 60–960, y 548–912) kol a ↔ kol b 16,9 sn: 0 px |
| 5 | KBJ E2 / AB-8 | `ortak/kunye.js` (`KOK`), `sahneler/02-paperjs-deger/sahne-02.js` (2), `kalem-paper.js` (2), `sayfa.html` (1) | `/projeler/simple-present-temel-s2/…` → `/projeler/simple-present-temel-s2b/…` (6 yol) | paket adı dışında fark 0 (`diff <(sed s#s2b/#s2/#g …) …`); §4 |
| 6 | KBJ "kol a'dan kopya kareler" | bütün `sahneler/*/k/`; `proje/.hyperframes`, `proje-ka/.hyperframes` (kol a mutlak kare yolları) | Silinecekler'e taşındı; kareler kol b'den yeniden çekildi; snapshot durumu kol b yolunu yazar | §3 |
| 7 | KBJ E4 (açıklama üst bilgisi) | `aciklama.md`, `aciklama-a.md`, `aciklama-b.md` satır 1, 3, 4, 7 (+ B satır 35) | `# simple-present-temel-s2`, `s2-aciklama-a/b`, kol b'de olmayan taslak kaynağı, `Eşleşen kapak: kapak-a.png` → `# simple-present-temel-s2b (A/B kol b)`, `s2b-aciklama-a/b`, "kol a açıklama seti kopyası; yalnız `utm_content` değişti", "Eşleşen kapak (grup türevi, kol a paketinde; huni-ab §4)" | yayın metni (kod blokları) kol a ile aynı, yalnız `utm_content=s2b-*`; `grep "utm_content=s2-"`: 0; `aciklama.md` = A (`cmp`) |
| 8 | TD-3 | `surumler.json` `video.canAlici` | yanlış denklik + mutlak kod → ana paketin `canAlici` dizisi | dosya |
| 9 | sürüm kaydı | `surumler.json` | `ad` `S2b Shorts (25,73 sn)` → `(27,00 sn)`; `revizyonlar` r1 | dosya |

Tek değişken kuralı korundu: değişken (c3 parça 3, c4 parça 1; sahne 03 kaydet kalıbı ve simgesi, sahne 04 giriş sözü) bu işte değişmedi.
Kart metni, rozet, karakter, ana kapak ve öteki türev kaynakları iki kolda eş.

## 2. Ses, süre ve Whisper

Komut: `timeout 1500 bash araclar/ses-sunucu.sh simple-present-temel-s2b` (00:39, rc 0), sonra `sozcuk_uret.py` → `zaman_uret.py` → `kur.py` →
`ses-paketle.py --yaz --paket simple-present-temel-s2b` → `altyazi_uret.py` → `metin_uret.py` (rc 0; `ses-sentez-DUZ2.log`).

| Parça | Konuşan | Metin | Duyulan | Benzerlik |
|---|---|---|---|---|
| 1·1 | öğretmen | Usually görünce hangi zaman? | aynı | 1,00 |
| 2·1 | öğretmen | My brother usually goes to school by bus. | aynı | 1,00 |
| 2·2 | öğretmen | Alışkanlık işareti. | Alışkanlık işareti | 1,00 |
| 2·3 | öğretmen | Şu an değil, her sabah yedide kalkarım gibi. | … 7'de … | 1,00 |
| 3·1 | öğretmen (`en`) | Usually, always, every day: | Usually, always, every day. | 1,00 |
| 3·2 | öğretmen (`tr`) | çoğunlukla Simple Present. | Çoğunlukla Simple Present. | 1,00 |
| 3·3 | öğretmen | Ekran görüntüsü al, sınav günü bak. | Ekran görüntüsü al. Sınav günü bak. | 1,00 |
| 4·1 | öğrenci | Konu burada bitmiyor. | aynı | 1,00 |
| 4·2 | öğrenci | Dersin tamamı YDS Publishing YouTube kanalında. (ses metni `YeDeSe`) | … YEDESE Publishing … | 1,00 |

| Cümle wav | Kol a | Kol b | Sonuç |
|---|---|---|---|
| `cumle-1.wav` | `3128f4881413` | `3128f4881413` | AB-9: metni aynı, sha256 eş |
| `cumle-2.wav` | `c102637639ac` | `c102637639ac` | AB-9: metni aynı, sha256 eş |
| `cumle-3.wav` | `3a7e07035c51` | `269009dbaa8a` (önce `3fa5c40623a7`) | değişken cümlesi (parça 3) |
| `cumle-4.wav` | `b192db36b66b` | `4201e1dfc0f9` (değişmedi) | değişken cümlesi (parça 1) |

| Ölçü | Kol a | Kol b |
|---|---|---|
| Toplam | 26,68 | 27,00 |
| Sahne 01 · 02 | 0,00–3,00 · 3,00–11,87 | aynı |
| Sahne 03 kaydet | 11,87–20,02 (257 kare) | 11,87–20,34 (266 kare) |
| Sahne 04 çağrı | 20,02–26,68 (230 kare) | 20,34–27,00 (230 kare) |
| Parça 3·1 | 2,72 sn | 2,80 sn |
| Kart sabit (03) | 16,65–20,04 | 16,67–20,34 |
| Çekirdek 4·2 başı (sahne 04 yerel) | 2,14 | 2,14 |
| Hap `@ydspublishing` · `YouTube` (sahne 04 yerel) | 3,42 · 4,54 | 3,42 · 4,54 |

AB-3 parça notu: AB-9 cümle düzeyinde sağlanır. Parça düzeyinde 3·1 (kural özeti başı) ve 4·2 (çekirdek) sesi iki kolda bayt aynı değildir:
`el.py` önbellek anahtarı cümle içindeki komşu parçayı içerir. 4·2 süresi iki kolda 3,52 sn ve sahne içinde aynı göreli anda başlar; sözcük içi
zamanlar 0,2 sn'ye kadar ayrışır (`Publishing` kol a +1,76, kol b +1,96 sn). Parça eşitliği için ya `el.py`'ye komşusuz anahtar seçeneği gerekir
(D yazma alanı dışı) ya da çekirdek iki kolda ayrı cümle olur (kol a sesi de yeniden sentez). Elle wav eklemek "derleme, yama değil" kuralına aykırı;
yapmadım. Karar şefte.

## 3. Kareler (hepsi kol b'den)

Yöntem: 01 `ONIZLE_YALNIZ=1 … --tema koyu|acik` + `proje-ka` kapak A (`k/ka-*`, `k/koyu/kapak-a-koyu.png`; kök kopya yok); 01–04
`node araclar/sahne-kare.mjs simple-present-temel-s2b <sahne> <t…> <k> --tema acik|koyu --port 41333 --sunucu 41022`; 05–08 `bash calistir.sh --tema koyu`,
sonra `ONIZLE_YALNIZ=1 … --tema acik` + `hyperframes snapshot . --at 0.5 --no-end --keep -o ../k` (çalıştırıcı açık temada kök PNG yazar; kol b'de kök
türev yok) + `ortak/tema_damga.py <sahne> acik`. Sırayla, tek tarayıcı.

| Sahne | Açık | Koyu | Kol a ile piksel farkı (kanal farkı > 16) |
|---|---|---|---|
| 01 kanca | 0 · 1,5 · 2,95; `k/ka-acik/at-0.9s.png` | 1,5; `k/ka-koyu/at-0.9s.png`, `k/koyu/kapak-a-koyu.png` | 0 (7 / 7) |
| 02 değer | 3,05 · 7,45 · 11,8 | 7,45 | 0 (4 / 4) |
| 03 kaydet (değişken) | 11,95 · 15,6 · 16,9 · 18,9 · 19,3 · 20,3 | 20,3 | 11,95 tam kare 0; kart bölgesi 16,9 ↔ 16,9 0; kanal + künye bandı (y 280–450) 0 |
| 04 çağrı (değişken) | 20,42 · 21,92 · 23,32 · 25,02 · 26,92 | 23,32 · 26,92 | yerel kare 2, 89, 197'de kanal + künye bandı, ana kapak kartı (y 600–1140), hap + `YouTube` (y 1150–1250): 0 |
| 05–08 durağan | `k/at-0.5s.png` × 4 | `k/koyu/at-0.5s.png` × 4, `k/koyu/<türev>-koyu.png` × 4 | 0 (12 / 12); `proje/index.html` iki kolda bayt aynı |

HV-13 (kol b): kart bölgesi 16,9 ↔ 18,9 sn **0 px** (en büyük 12); 16,9 ↔ 20,3: 6 px (en büyük 21). Vizör çerçevesi 18,86'da kartın altında çizilir.
Baktıklarım (Read): `uretim-tutanagi/kontak/DUZ2-degisken.png` (03 ve 04, 13 kare, açık + koyu). Taşma yok, çakışma yok, okunmayan yazı yok; rozet her
karede `YDT · TEMEL`; kart 2. satırı `every day: çoğunlukla`; vizör + `Ekran görüntüsü al`; `Konu burada bitmiyor.` tek satır; ana kapak kartında yeni
kadın öğrenci. Değişken dışı kareler kol a ile piksel aynı; kol a karelerine baktım (kol a raporu §3).

## 4. AB-8 taraması

Komut: `grep -rn "simple-present-temel-s2/" /home/sef/01dev/_worktrees/kalem-0204/projeler/simple-present-temel-s2b --include=*.js --include=*.html --include=*.json --include=*.py`
Çıktı: **boş** (çıkış 1). `surumler.json` `varyant` alanı paket yolu taşımaz (`{"grup": "s2", "kol": "b", …}`).
Önceki durum: `ortak/kunye.js:7`, `sahne-02.js:4–5`, `kalem-paper.js:10–11`, `sayfa.html:7` ve 05–08, 01 `proje*/.hyperframes/video-state.json` (16 satır, kol a kare yolları).

## 5. Çakışma kapısı

Komut: `node araclar/cakisma-kapisi.mjs simple-present-temel-s2b --port 41333 --sunucu 41022 --json projeler/simple-present-temel-s2b/uretim-tutanagi/cakisma-DUZ2.json`
Çıkış kodu: **0**. 01 13 örnek · 02 37 · 03 35 · 04 28; çakışma yok (`cakisma-DUZ2.txt`).

## 6. `diff -rq` sınıflaması

Komut: `diff -rq projeler/simple-present-temel-s2 projeler/simple-present-temel-s2b` → `uretim-tutanagi/DUZ2-diff-rq.txt` (103 satır; KBC 70). Her satırı bir
düzenli ifade kuralı sınıfladı; kural dışı satır 0.

| Sınıf | Satır | Beklenen mi | Gerekçe |
|---|---|---|---|
| `uretim-tutanagi/` | 28 | evet | tutanak, kanıt ve kontak, kol başına |
| Değişken sahne 03 / 04 karesi (`k/`, kol başına zaman) | 22 | evet | değişken sahneler; zamanlar kayık (kol b c3 0,32 sn uzun) |
| Değişken sahne 03 / 04 kaynağı ve türevi (`uret.py` × 2, `proje/index.html` × 2, `zamanlar.json` × 2, `olaylar.json` 03) | 7 | evet | değişken (KBC sınıfı) |
| Ses ve zaman türevi (`sentez.wav` + rapor, `anlatim.wav/m4a/imza`, `sozcukler`, `sureler`, `altyazi`, `baslar`, `METIN.md`) | 10 | evet | değişken cümlelerinin türevi |
| `cumle-3.wav`, `cumle-4.wav` | 2 | evet | değişken cümleleri |
| `senaryo.json` | 1 | evet | yalnız c3·3, c4·1 + iki `metin` |
| `zaman.json` | 1 | evet | sahne 03 / 04 sınırı |
| `surumler.json` | 1 | evet | kol kaydı + DUZ2 notu |
| Açıklama × 3 | 3 | evet | `utm_content` (`s2b-*`) + E4 üst bilgisi |
| Kök grup türevi yalnız kol a (kapak × 4, hikâye × 3) | 7 | evet | huni-ab §4: türev gruba ait |
| AB-8 yolu (`ortak/kunye.js`, `kalem-paper.js`, `sahne-02.js`, `sayfa.html`) | 4 | evet | paket adı dışında fark 0 |
| `__pycache__/yardim.cpython-310.pyc` × 7 | 7 | evet | pyc paket yolunu gömer; kaynak `yardim.py` iki kolda bayt aynı; git dışı |
| `proje/.hyperframes`, `proje-ka/.hyperframes` (`history-id`, `video-state.json`; 01, 05–08) | 10 | evet | snapshot durumu kol başına kare yolu yazar; git dışı |
| **Beklenmeyen** | **0** | — | — |

Sahne 01 (kaynak, HTML, `proje-ka/index.html`), 02 (yol dışında), 05–08 (`uret.py`, `proje/index.html`, `nesneler.json`, `RAPOR.md`), `ortak/kapak/` ve
`ortak/` kalanı iki kolda bayt aynı. Kol a'daki 15.11 QA kırpımları (`01/k/ara`, `05/k/qa`, `08/k/qa`) bu işte Silinecekler'e taşındı; fark vermez.

## 7. Düzeltilmeyen maddeler

| Madde | Sınıf | Sebep |
|---|---|---|
| HV-13 (yer imi + "Kaydet" yok) | **ölçüt** | güncel HV-13: kapanış `ekran-goruntusu` için vizör + "Ekran görüntüsü al" beklenir; 2 sn kart sabitliği ölçüldü (§3: 0 px) |
| HV-17 "YEDESE" | **ölçüt** | güncel HV-17 bu dökümü beklenen davranış sayar |
| HV-20, HV-21 (kol b'de türev yok) | **ölçüt** | güncel ölçüt: A/B kol b'de uygulanmaz (türev kol a'da) |
| AB-4, AB-5, AB-7 | **ölçüt** (yayın sonrası) | üretim jürisi "uygulanmaz (yayın sonrası)" yazar |
| AB-3 parça düzeyi (3·1, 4·2 sha256) | şef kararı | §2 notu; AB-9 cümle düzeyinde sağlandı |
| KBJ E3: açıklama ilk satırı "kaydet", video "ekran görüntüsü al" | şef kararı | ilk satır huni §4'te sabit; A/B yorumu |
| `senaryo.json` `meta.kimlik` = `02-02-ydt-temel-s2` | şef kararı | yol değil (AB-8 dışı); panel bu alanı okuyorsa `…-s2b` olmalı |
| `{UZUN_VIDEO_URL}` boş | yayın aşaması | ana ders yüklenince doldurulur |
| Süre 27,00 > hedef 22–26 | açık nokta | "çoğunlukla" iki kolda ≈ 1 sn ekledi; kabul ≤ 35 sağlandı |
| `calistir.sh` `uret.py && olay.py` zinciri `set -e` altında durmaz | açık nokta | kol a raporu §5; şablon iki kolda aynı, bu işte değişmedi |

## 8. Değişen dosyalar

Kaynak: `BRIEF-S2.md`, `aciklama{,-a,-b}.md`, `ortak/kunye.js`, `ortak/kapak/{karakter,ana-kapak,ana-kapak-koyu}.png`, `ortak/anlatim/senaryo.json` (önceki oturum),
`sahneler/02-paperjs-deger/{sahne-02.js,kalem-paper.js,sayfa.html}`, `sahneler/0{1,3,4,5,6,7,8}-*/yardim.py`, `sahneler/0{3,5,6,7}-*/uret.py`, SPEC 01, 03, 05–08,
`surumler.json` (`canAlici`, `ad`, `revizyonlar` r1).
Türetilmiş: `ortak/anlatim/*` (ses ve zaman), `zaman.json`, sahne `proje*/index.html`, `zamanlar.json`, `olaylar.json`, `nesneler.json`, `devir.json`, `k/` kareleri.
Silinecekler: `~/Silinecekler/2026-11-15-duz2-0202S2/simple-present-temel-s2b/` ve `eski-ses/s2b/` (`LISTE.md` satırları).
