# DUZ2-0202S1 raporu — `simple-present-temel-s1b` (A/B kol b, değişken `kanca`) · J2 A sınıfı + KBJ gerçek hatalar · 16.11.2026

Girdi: `uretim-hatti/raporlar/J2-OZET-1511.md` (§3A, §4.1, §4.2 P1, §4 "Sıra"), `uretim-tutanagi/juri/KBJ-hukum.md`, `uretim-tutanagi/KBC-RAPOR.md`.
Kol a raporu: `../simple-present-temel-s1/uretim-tutanagi/DUZ2-RAPOR.md`. Oturum: Claude Opus 5.5, tek oturum, alt ajan yok.

| Ölçüm | Değer |
|---|---|
| Düzeltilen kusur | A1 / TD-1 (rozet), A2 / TD-2 (karakter + ana kapak kopyası); KBJ HV-1, HV-7, HV-13, HV-14 (kol a'dan kopya kareler → kol b'den çekildi); HV-22 (kapı koştu); HV-20 (kol b kapak A yeniden) |
| Yeniden sentezlenen cümle | **0** (kanca cümlesi değişmedi; cümle 2–4 sha256 kol a ile eşit, AB-9 GEÇTİ) |
| Toplam süre | **24,33 sn** (değişmedi; hedef 22–26, sınır 35) |
| Whisper en düşük | **1,00** (10 / 10 parça; eşik 0,90) |
| İlk söz · kanca sahnesi bitişi | 1,00 sn · 3,00 sn (HV-12 GEÇTİ) |
| Kanca cümlesi bitişi (bilgi) | 4,45 sn: 4 sn eşiğinin 0,45 sn üstü (kol a 4,12). HV-12 tanımında bilgi satırıdır |
| Çakışma kapısı (paket) | `node araclar/cakisma-kapisi.mjs simple-present-temel-s1b --port 41333 --sunucu 41022 --json projeler/simple-present-temel-s1b/uretim-tutanagi/cakisma-DUZ2.json` → **çıkış 0**, 4 sahne, 0 uyarı |
| AB-8 taraması | 0 satır (grep çıkış 1); §4 |
| `diff -rq` | 113 satır: beklenen 106 · gerekçeli 7 (sahne 02 × 5, 03/04 `zamanlar.json` × 2); gerekçesiz beklenmeyen **0**; §5 |
| huni-kapi | `node D/araclar/huni-kapi.mjs projeler/simple-present-temel-s1b --kol-a projeler/simple-present-temel-s1` → 19 GEÇTİ, 4 KALDI (HV-1s araç, JR-1b jüri bayat, AB-2 + AB-3 aynı kök §6), 5 ÖLÇÜLEMEDİ, 3 UYGULANMAZ · HV-20, HV-24, AB-8, AB-9 GEÇTİ |
| mp4 | 0 |

## 1. Düzeltmeler

| Kusur | Dosya | Önce → sonra | Kanıt |
|---|---|---|---|
| A1 / TD-1 | `ortak/anlatim/senaryo.json` `giris.rozetler` | `YDT · BASIC` → `YDT · TEMEL` | huni-kapi HV-24 GEÇTİ (21 dosya, `BASIC` 0) |
| A1 / TD-1 | `ortak/kunye.js` `KUNYE.rozet` (yalnız bu satır; `KOK` kol b yolunda kaldı) | aynı | `diff` kol a ile yalnız `KOK` |
| A1 / TD-1 | `sahneler/01-hyperframes-kanca/yardim.py` `ROZET`, `SPEC.md` (2 yer) | aynı | `grep BASIC` → 0 |
| A1 / TD-1 | `BRIEF-S1.md`, `sahneler/03-…/yardim.py`, `sahneler/04-…/yardim.py`, `sahneler/04-…/SPEC.md` | kol a'dan KOPYA (fark yalnız rozet satırlarıydı; BRIEF'te ek olarak can alıcı satırı, kol a §1.3) | dosyalar kol a ile bayt eşit |
| A1 / TD-1 | yeniden üretilen HTML: 01 `proje/` + `proje-ka/`, 03, 04 | hap 203,6 → 207,6 px | kareler §3 |
| A2 / TD-2 | `ortak/kapak/karakter.png` | `a4198903833d…` (erkek) → `5a902b401816…` (ana paket, kadın) | `sha256sum` ana paket ve kol a ile eşit |
| A2 / TD-2 | `ortak/kapak/ana-kapak.png`, `-koyu.png`; `sahneler/04-…/proje/assets/ana-kapak*.png` | `e2bbf46d…` / `df33df75…` → `7f714514…` / `7e948a3b…` | çağrı kareleri: kartta kadın karakter |
| KBJ HV-1, 7, 13, 14 | `sahneler/03-…/k/`, `sahneler/04-…/k/` | kol a kopyası (19:23, 19:28) → kol b'den çekildi | §3; kol a ile aynı göreli anda 0 px fark |
| KBJ HV-22 | paket | üretici cümlesi → kapı bu oturumda koştu | `cakisma-DUZ2.json`, çıkış 0 |
| HV-20 (kol b) | `kapak-a.png` = `kapak.png`, `sahneler/01-…/k/koyu/kapak-a-koyu.png` | yarım oturum eskilerini taşımıştı → yeniden çekildi (md5 `4f6d4323…`) | huni-kapi HV-20 GEÇTİ |

Kol b'de karakter yalnız çağrı sahnesindeki ana kapak kartında görünür. Kapak B ve C, hikâye A ve B gruba aittir ve kol a'da durur
(AB §4). Kanca sahnesi karakter görseli kullanmaz.

## 2. Ses, süre, Whisper

Ses değişmedi. `zaman.json`, `sozcukler.json`, `baslar.json` değişmedi.

| Cümle | Başlangıç–bitiş (sn) | sha256 kol a / kol b | Whisper duyulan | Benz. |
|---|---|---|---|---|
| 1 kanca (değişken) | 1,00–4,45 | `e9fa0350…` / `9a113bfd…` | My brother go to school by bus. · Hata nerede? | 1,00 |
| 2 değer (5 parça) | 5,00–14,96 | `bb9402db…` / `bb9402db…` | 5 × birebir | 1,00 |
| 3 kaydet | 15,51–18,07 | `9cb210d9…` / `9cb210d9…` | Sınavdan önce lazım olacak. Kaydet. | 1,00 |
| 4 çağrı (öğrenci, 2 parça) | 18,62–23,33 | `dd50c6bc…` / `dd50c6bc…` | Gerisi bizde. · Dersin tamamı YEDESE Publishing YouTube kanalında. | 1,00 |

## 3. Kareler (bu oturumda kol b'den çekildi; her kareye bakıldı)

| Sahne / türev | Komut | Kareler (açık · koyu) | Gördüğüm | Kapı |
|---|---|---|---|---|
| 01 kanca | `bash araclar/qa-yerel.sh simple-present-temel-s1b 01-hyperframes-kanca 0,0.55,0.9,2.2,2.65,2.95 2.65 --hazirla` | 0 · 0,55 · 0,9 · 2,2 · 2,65 · 2,95 · koyu 2,65 | `MY BROTHER` / `GO.` + kırmızı ✗; rozet TEMEL; yanlış cümle kartı soldan açılır | 0 |
| Kapak A | S1-KAPAK-A yöntemi (koyu önce; `proje-ka`, `#altyazi{display:none}`, snapshot 0,90) | `kapak-a.png` = `kapak.png` · `k/koyu/kapak-a-koyu.png` | altyazı yok; kanal, rozet TEMEL, ✗, figür, otobüs | — |
| 02 değer | `… 02-paperjs-deger 3.05,4.25,5.5,6.2,8.8,14.9 4.25 --hazirla` | 3,05 · 4,25 · 5,5 · 6,2 · 8,8 · 14,9 · koyu 4,25 | kanca kuyruğu (✗, kayış, `go` kartı devri), sonra kol a ile aynı değer düzeni | 0 |
| 03 kaydet | `… 03-hyperframes-kaydet 15.03,15.98,16.53,17.98 17.98 --hazirla` | 15,03 · 15,98 · 16,53 · 17,98 · koyu 17,98 | kart + yer imi + `Kaydet` | 0 |
| 04 çağrı | `… 04-hyperframes-cagri 18.13,21.23,22.83,24.28 24.28 --hazirla` | 18,13 · 21,23 · 22,83 · 24,28 · koyu 24,28 | kadın karakterli ana kapak, iki rozet TEMEL; `@ydspublishing · YouTube` 21,23'te var (HV-14) | 0 |

Piksel ölçümü (eşik 8/255; kol b zamanı = kol a + 0,33 sn):

| Karşılaştırma | Fark |
|---|---|
| HV-13 kart bölgesi (x 60–960, y 560–1000): `03-…-15.98` ↔ `03-…-17.98` (2,00 sn) | **0 px** |
| Sahne 03: kol a 17,65 ↔ kol b 17,98 (açık ve koyu) | 0 px (tam kare) |
| Sahne 04: kol a 20,9 ↔ kol b 21,23; kol a 23,95 ↔ kol b 24,28 (açık ve koyu) | 0 px (tam kare) |
| Sahne 02: kol a 8,8 ↔ kol b 9,13; kol a 14,55 ↔ kol b 14,88 | 12.349 px · 13.881 px, bbox x 62–958, y 620–1292: yalnız kalem çizgisi titreşimi (kutu kenarı, otobüs, ok, çember); metin ve yerleşim aynı |

HV-1: kanal katmanı 0. sn (`01-…-0.png`), orta (`02-…-8.8.png`) ve son karede (`04-…-24.28.png`) görünür. HV-7: ana kapak kartı son karede
x 60–960, y 620–1126.

## 4. AB-8 taraması

```
$ grep -rn "simple-present-temel-s1/" K/projeler/simple-present-temel-s1b --include=*.js --include=*.html --include=*.json --include=*.py
(çıktı yok; çıkış 1)
```

`ortak/kunye.js` `KOK` = `/projeler/simple-present-temel-s1b/ortak`. Kol a içine simge bağı 0 (huni-kapi AB-8 GEÇTİ).

## 5. `diff -rq` sınıflaması

Komut: `diff -rq K/projeler/simple-present-temel-s1 K/projeler/simple-present-temel-s1b` → bu rapor yazıldıktan sonra 113 satır.

| Sınıf | Satır | Dosyalar | Karar |
|---|---|---|---|
| Açıklama `utm_content` (`s1-*` → `s1b-*`) | 3 | `aciklama.md`, `-a`, `-b` | beklenen |
| Grup türevi yalnız kol a (AB §4) | 9 | `kapak-b/c.png`, `hikaye*.png` (3), `sahneler/05`–`08` | beklenen |
| Kol b kapak A (kanca karesi) | 2 | `kapak-a.png`, `kapak.png` | beklenen |
| Senaryo, ses ve zaman türevi (kanca cümlesi) | 13 | `ortak/anlatim/`: `senaryo.json`, `cumle-1.wav`, `sentez.wav` + rapor, `anlatim.wav/.m4a/.imza`, `altyazi`, `baslar`, `sozcukler`, `sureler`, `METIN.md`, `zaman_uret.py` (KBC açık nokta 2) | beklenen |
| `ortak/kunye.js` | 1 | yalnız `KOK` yolu | beklenen (AB-8) |
| Değişken sahnesi 01 | 13 | `uret.py`, `olay.py`, `olaylar.json`, `zamanlar.json`, `devir.json`, `SPEC.md`, `RAPOR.md`, `proje/index.html`, `proje-ka/index.html`, `proje-ka/.hyperframes/` (2), `__pycache__` (2) | beklenen |
| `k/` QA kareleri | 42 | zaman noktaları kola göre ayrı (git dışı üretim izi) | beklenen |
| `sahneler/02-…/kalem-paper.js` | 1 | yalnız paket yolu (içe aktarım) | beklenen (AB-8) |
| `surumler.json`, `zaman.json` | 2 | varyant + DUZ2 satırı; sahne zamanları | beklenen |
| `uretim-tutanagi/` | 18 | her kolun kendi tutanağı (bu rapor dahil) | beklenen |
| `__pycache__` 03/04 `yardim.pyc` | 2 | kaynak bayt aynı; `.pyc` kaynak zamanını taşır (türetilmiş, huni-kapi dışlar) | beklenen |
| **Sahne 02 değer** | **5** | `sahne-02.js`, `calistir.sh` (N 371), `sayfa.html` (yorum: 371 kare), `SPEC.md`, `RAPOR.md` | **gerekçeli** (§6) |
| **03/04 `zamanlar.json`** | **2** | küresel sn +0,33 (kanca cümlesi +0,33 sn); `proje/index.html` iki kolda bayt aynı; kareler 0 px | **gerekçeli** |

Toplam 113 = beklenen 106 + gerekçeli 7. Gerekçesiz beklenmeyen 0.

## 6. KBJ maddeleri

| Kimlik | KBJ hükmü | Bu oturum | Sınıf |
|---|---|---|---|
| HV-1, HV-7, HV-13, HV-14 | kanıt yok (kol a kopya kareler) | kol b'den çekildi; HV-13 0 px; HV-14 21,23'te `· YouTube` var | gerçek → düzeltildi |
| HV-22 | kanıt yok | paket kapısı çıkış 0 (araç `K/araclar/`, srv21'de var) | gerçek → kanıt üretildi |
| HV-12 | hayır (kanca cümlesi 4,45) | dokunulmadı; HV-12 15.11 gece tanımı kanca = sahne 1 bitişi (3,00); huni-kapi GEÇTİ | ölçüt |
| AB-3 | hayır (sahne 02 iki kolda farklı) | düzeltilmedi (aşağıda) | şef kararı |
| HV-21, HV-20 (kol b'de kapak B/C, hikâye) | kanıt yok / — | kol b'de uygulanmaz (AB §4; ölçüt HV-20/21 metni) | ölçüt |
| HV-17 | evet | — | ölçüt (istem listesi) |
| AB-4, AB-5, AB-7 | kanıt yok | yayın sonrası; üretim jürisinde uygulanmaz | ölçüt |
| Ek bulgu 2 (rozet) | — | düzeltildi (A1) | gerçek |

AB-3 neden düzeltilmedi: kanca cümlesi (değişken) 4,45 sn'de biter; HV-12 sahne 1'i en çok 4 sn tutar, sahne 1 3,00'te biter. Bu yüzden
değer sahnesinin ilk 2,00 sn'si kanca kuyruğunu taşır (kol a'da 1,67 sn; kol a'nın kuyruğu da kendi kancasına özgüdür). İki kolun sahne
02 dosyalarını bayt eşit yapmak için ya kanca cümlesi kısalır (yeni ses, değişkenin kendisi değişir) ya da sahne 02 kuyruğu veri
dosyasına taşınır (Paper.js sahnesinin yeniden yazımı). İkisi de A sınıfı düzeltme değil, tasarım kararıdır. KBJ de "şef kararı" yazdı.
Ölçülen durum: değer cümlesi sesi, kanal katmanı, çekirdek cümle ve ses kadrosu aynı; değer içeriği (metin, yerleşim, karaoke) aynı;
fark baştaki kanca kuyruğu ve kalem titreşimidir. Seçenekler: (a) AB §3'e "kanca kuyruğu değer sahnesinin başında kalabilir" satırı,
(b) kanca cümlesini kısalt ("Hata?"), (c) sahne 02 kuyruğunu `devir.json` verisine taşı.

## 7. Düzeltilmeyen öteki maddeler

| Madde | Sebep |
|---|---|
| huni-kapi HV-1s | araç sınırı: kanal yazısı `ortak/kunye.js`'den çizilir; karelerde görünür |
| huni-kapi JR-1b | beklenen: jüri yeniden koşar |
| Açıklama dosyalarında kol a kimliği (`# simple-present-temel-s1`, `Sürüm: A (s1-aciklama-a)`, `kapak-c.png` başvurusu) | iç not satırları, yayın metnine girmez; kapak ve hikâye başvurusu grup türevini gösterir (kol a'da). KBC açık nokta 3: şef kararı |
| "s gelir" / `-es` (KBJ ek bulgu 1) | iki kolda ve ana derste aynı; A sınıfı değil; değişirse iki kol birlikte değişir (AB-9) |
| EK-11 kulak kararı (`My brother go`) | Nadir dinler |

## 8. Silinecekler

`~/Silinecekler/2026-11-15-duz2-0202S1/` (`LISTE.md`): `s1b/ortak-kapak/` (erkek karakter, eski ana kapak), `s1b/eski-kare/` (01–04 eski
kareler; 03/04 kol a kopyasıydı), `s1b/eski-kok/` (eski kapak A), `qa-kare-eski/simple-present-temel-s1b/`. Silme yok.

---
Son Güncelleme: 16.11.2026 — ilk sürüm (DUZ2-0202S1).
