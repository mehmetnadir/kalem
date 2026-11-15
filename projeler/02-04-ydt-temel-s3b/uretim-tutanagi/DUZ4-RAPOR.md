uretici_model: Claude Opus 5.5 (`claude-opus-5-5`) — üretim oturumu; ajan yok

# DUZ4-RAPOR — 02-04-ydt-temel-s3b (kol b, değişken `kanca` = `yanlis-cumle`) · J3 özeti C sınıfı kanıtlar (A sınıfı düzeltme yok) · 16.11.2026

İstem: `DUZ4-0204S3` (J3-OZET-1611.md §5). Girdi: J3 §3C.1 (C1, C2, C6), §3D (K3); hüküm `juri/KBJ-hukum-1611-0055.md`; önceki tur
`DUZ2-RAPOR.md`. Kol a raporu: `../02-04-ydt-temel-s3/uretim-tutanagi/DUZ4-RAPOR.md`. KBJ jürisinin modeli Sonnet 5.5; bu oturumun modeli
Opus 5.5 (§1e sağlanır).

| Kalem | Sonuç |
|---|---|
| İçerik değişikliği | yok (senaryo, ses, sahne kodu, açıklama dosyalarına dokunulmadı) |
| Kare tazeliği (C6) | 4/4 video sahnesi taze · eski kalan 0 · yeniden çekim 0 (04–07 grup türevi, kol b'de kare beklenmez) |
| 168 px (C1) | `kapak-a-168.png`, 168 × 299 · ana yazı okunur |
| Kontak (C2) | açık 27 kare · koyu 11 kare · #16 ön sayımı 0–1 aday (§4) |
| Çakışma kapısı | koşulmadı (1. adımda kare yenilenmedi; istem madde 5) |
| Huni kapısı | çıkış 1 · tek KALDI JR-1b = gerçek · AB-2 GEÇTİ (K3 kapandı) · KS-6f GEÇTİ |
| AB-8 grep | 20 satır: 18 yorum/belge dizgisi, 1 `kimlik` alanı, 1 tutanak `kol_a` kaydı · yol başvurusu 0 |
| diff kol a ↔ kol b | 211 satır · beklenmeyen 0 (`siniflama-duz4.txt`) |
| Tek değişken | ses dosyasına dokunulmadı (AB-9 GEÇTİ) · kare çifti 27/27 piksel eşit (AB-3) |
| mp4 | yok |

## 1. İş başına satır

| J3 | Jüri maddesi (KBJ) | Dosya | Kanıt |
|---|---|---|---|
| C6 | K-1 kare tazeliği (J3 tablo ister) | — | §2 tablosu; `huni-kapi-duz4.txt` satırı `KR-1 ÖLÇÜLEMEDİ — k/ kare dizini yok ya da boş: 04-…, 05-…, 06-…, 07-…; 4 sahne taze` (§5 sınıflama) |
| C1 | KS-6 (⊕; KBJ bakmadı, özet kaldı saydı) | `kapak-a-168.png` (paket kökü) | `file` → `PNG image data, 168 x 299`; §3; kapı `KS-6f GEÇTİ — kol a kapak-a\|b\|c-168.png 168 px; kol b kapak-a-168.png` |
| C2 | EK-8 (hayır: kanıt yok) | `uretim-tutanagi/kontak/02-04-ydt-temel-s3b-duz4-kontak.png`, `…-duz4-kontak-koyu.png` | §4 (kareler + 18 madde ön sayımı) |
| — | AB-2 (KBJ: evet, kapı hatası K3) | — | kapı `AB-2 GEÇTİ — kanca: 38 beklenen fark, 0 beklenmeyen; zaman kayması (beklenen, Δ=1.000 sn): 4 dosya` |
| — | AB-8 · AB-3 · AB-9 | — | §6 |
| — | §1e (B14) | bu dosyanın ilk satırı | `uretici_model` |
| — | sürüm kaydı | `surumler.json` `revizyonlar[1]` (`no: r2`) | §8 |

## 2. Kare tazeliği (C6)

Yöntem: `stat -c %Y`. Kare = `sahneler/<s>/k/**/*.png` en yeni. Kaynak = `uret.py`, `yardim.py`, `proje/index.html` ve paketin
`ortak/kunye.js` (15.11 23:51:38) en yenisi. Tarih 15.11 yazılmayan satır 16.11'dir.

| Sahne | Kare sayısı | Kare en yeni | Kaynak en yeni (dosya) | Sonuç |
|---|---|---|---|---|
| 01-hyperframes-kapak | 10 | 23:56:28 | 23:56:20 (`proje/index.html`) | taze |
| 02-hyperframes-ornek | 11 | 23:56:40 | 23:56:33 (`proje/index.html`) | taze |
| 08-hyperframes-kaydet | 9 | 16.11 00:14:49 | 16.11 00:14:42 (`proje/index.html`) | taze |
| 03-hyperframes-cta | 7 | 23:56:53 | 23:56:47 (`proje/index.html`) | taze |
| 04 · 05 · 06 · 07 (türev) | 0 | — | 23:56:53 – 23:59:14 (`proje/index.html`) | kapsam dışı: grup türevi yalnız kol a (huni-ab §4); kol b'de kare beklenmez |

Ek bakış: kök `kapak-a.png` (= `kapak.png`) 23:56:32 ≥ `01/proje-ka/index.html` 23:56:28. `ortak/anlatim/*` en yeni 23:38:00: bütün sahne
kaynaklarından eski. Sonuç: eski kalan sahne 0, yeniden çekim yok. İstem "kol a ayrıca türevler 04–07" der; kol b'de 04–07 dizinleri kol a
kopyasıdır, çekim ve teslim yoktur.

## 3. 168 px okunurluk (C1 · kapak §5.2)

Yöntem P3 ile aynı: genişlik 168, oran korunur (1080 × 1920 → 168 × 299), PIL `LANCZOS`. Yöntem eşitliği ölçüldü: P3 `kapak-a.png`
aynı yöntemle küçültülünce P3'ün `kapak-a-168.png` dosyasıyla piksel eşit (`getbbox` None). Dosyayı Read ile açtım.

| Dosya | sha256 (ilk 12) | Ana yazı | Öteki öğeler |
|---|---|---|---|
| `kapak-a-168.png` | `d329bc7590e8` | "HATA NEREDE?" okunur | yanlış cümle iki satır ("The train to İzmir" / "is leave at 7 pm today.") küçük ama okunur; `?` işareti, saat, tren, figür seçilir |

Taşma yok, yazı ile karakter üst üste binmiyor, altyazı yok. Kanal satırı `@ydspublishing` okunur. Rozet `YDT · TEMEL` sarı hap olarak
görünür; metni bu boyda okunmaz (26 px → ≈ 4 px). Kapak §5.2 yalnız ana yazıyı ister.

## 4. Kontak (C2) ve 18 madde ön sayımı

| Sayfa | Boyut | Kare | Satırlar |
|---|---|---|---|
| `kontak/02-04-ydt-temel-s3b-duz4-kontak.png` (açık) | 1870 × 1874 | 27 | 01 ×7 (0–3,97) · 02 ×9 (4–19,6) · 08 ×5 (19,78–25,1) · 03 ×5 (25,12–32,07) · türev ×1 (kök `kapak-a`) |
| `kontak/02-04-ydt-temel-s3b-duz4-kontak-koyu.png` (koyu) | 920 × 1874 | 11 | 01 ×2 · 02 ×2 · 08 ×4 · 03 ×2 · `kapak-a koyu` |

- Kareler: var olan `sahneler/*/k/` kareleri (çekim 15.11 23:56 – 16.11 00:14; §2'ye göre taze). J3 §5: bu çiftte yeniden çekim yok.
- Kare altındaki `t` küresel saniyedir (kol a + 1,00). Küçük kare 180 × 320, LANCZOS; sayfa zemini gri 128.
- İlk üretimde koyu sayfanın başlığı sayfadan taştı. İki kolun ilk 4 dosyası `~/Silinecekler/2026-11-16-duz4-0204S3/` altına taşındı
  (`LISTE.md` satırı yazıldı); sayfalar aynı karelerden iki satırlık başlıkla yeniden üretildi.

Ön sayım (kanıt jürinin sayımıdır). #16 sayımı J3 B6 ile `juri-olcutleri.md` EK-8 metnine göre: içerik bölgesinde (y 460–1380) aynı anda
görünen yazı öbeği ≥ 5 ise işaret; tek cümlenin satır kırılımı tek öbek; altyazı, künye, kanal katmanı sayılmaz.

| # | Klişe | Açık | Koyu | Not |
|---|---|---|---|---|
| 1 | Mor–mavi gradyan zemin | 0 | 0 | açık zemin `#f7f3ea` düz + vinyet; koyu `#1b1a17` düz |
| 2 | Glassmorphism | 0 | 0 | mat kart, ince çerçeve, gölge yok |
| 3 | Neon glow | 0 | 0 | düz sarı vurgu |
| 4 | Parçacık, yüzen nokta | 0 | 0 | yok |
| 5 | 3B dönen nesne | 0 | 0 | 2B çizgi ikon: tren, saat, bilet, yer imi, kâğıt uçak |
| 6 | Inter/Roboto varsayılanı | 0 | 0 | Fredoka başlık, Lexend gövde, Caveat etiket |
| 7 | Her şey ortalı tek kolon | 0 | 0 | kart ve etiketler sol hizalı (x 60–960); tren sol, figür sağ |
| 8 | Aynı ease, nefes zoom | — | — | hareket; kontak göstermez |
| 9 | Sabit aralıklı hızlı kesme | 0 | 0 | sahne süreleri 4,00 · 15,78 · 5,34 · 6,98 sn (`zaman.json`) |
| 10 | TikTok karaoke | 0 | 0 | sözcük ikincilden mürekkebe döner; ölçek ve konum sabit (02 t=10,5 · 03 t=26,5) |
| 11 | Whoosh / ding | — | — | ses; kontak göstermez |
| 12 | "AI" ikonografisi | 0 | 0 | konunun nesneleri |
| 13 | Emoji, sticker | 0 | 0 | yok |
| 14 | Uzun intro | 0 | 0 | 0. sn'de kanca başlığı (01 t=0) |
| 15 | Konuşan kafa + slayt | 0 | 0 | yok |
| 16 | Metin duvarı | 0–1 | 0 | aşağıdaki tablo |
| 17 | Rastgele stok görsel | 0 | 0 | çizim; karakter görseli ana ders kapağının kendi görseli (HV-7) |
| 18 | Gradyan metin, outline yazı | 0 | 0 | düz renk; kanca t=2,8'de `is leave` üstü çizili (kasıtlı yanlış işareti, outline değil) |

#16 ayrıntısı (öbek sayısı, içerik bölgesi):

| Kare | Öbek | Öbekler | Okuma |
|---|---|---|---|
| 02 t=7,6 | 7 | kart 1 · `now` · `7 pm` · `tonight` · `gelecek · V-s` · `gelecek · am + V-ing` · kart 2 | katı okuma: işaret. Zaman çizgisinin etiketleri tek diyagram sayılırsa 4 → işaret değil. Kol a'da aynı kare t=6,6 |
| 02 t=5,2 · t=17,6 · t=19,6 · 03 t=32,07 | 4 | kol a'daki t − 1,00 karelerle aynı öbekler | işaret değil |
| 01 t=1,8 · t=2,8 · `kapak-a.png` | 3 | başlık "HATA NEREDE?" · yanlış cümle (iki satır, tek cümle) · `?` | işaret değil. KBJ 5 saymıştı (altyazı ve satır başına sayım); B6 kuralıyla 3 |
| öteki 19 kare | ≤ 3 | — | işaret değil |

Koyu sayfa: 02 t=7,6'nın koyu karesi yok; 11 koyu karenin hepsi ≤ 4 öbek.

Ön sayım: 18 maddeden 15'inde 0, 2'si kontak dışı (8, 11). #16: açık sayfada 0 (yorumlu okuma) ya da 1 kare (katı okuma: 02 t=7,6);
koyu sayfada 0. Sahne 02 iki kolda bayt aynı; aday kare kol a ile ortaktır. Karar jürinin.

## 5. Kapılar

Çakışma kapısı: koşulmadı. İstem madde 5 yalnız 1. adımda kare yenilenen paketi ister; bu pakette yenilenen kare yok. Son koşu DUZ2'de
(`kapi-duz2-r2.txt`, çıkış 0); o tarihten sonra sahne kaynağı ve kare değişmedi (§2).

Huni kapısı (K altında koşuldu; kapı `D/araclar/huni-kapi.mjs` son commit `d846d6e`, 16.11 01:56):

```
node /home/sef/01dev/dijital-anlatim/araclar/huni-kapi.mjs /home/sef/01dev/_worktrees/kalem-0204/projeler/02-04-ydt-temel-s3b \
  --kol-a /home/sef/01dev/_worktrees/kalem-0204/projeler/02-04-ydt-temel-s3
→ çıkış 1 · ÖZET: 23 GEÇTİ, 1 KALDI, 6 ÖLÇÜLEMEDİ, 3 UYGULANMAZ   (tam çıktı: uretim-tutanagi/huni-kapi-duz4.txt)
```

| Satır | Sınıf | Gerekçe |
|---|---|---|
| `JR-1b KALDI — jüri 2026-11-16 00:58:05 yerel (KBJ-hukum-1611-0055.md) ≤ son içerik 2026-11-16 01:36:05 yerel (surumler.json)` | gerçek (kapı hatası değil) | `surumler.json` bu oturumdan önce 01:36:05'te değişmişti; bu tur 02:00'de r2 kanıt notunu ekledi. Hüküm paketten eski; 3. tur jüri kapatır. |
| `KR-1 ÖLÇÜLEMEDİ — k/ kare dizini yok ya da boş: 04-…, 05-…, 06-…, 07-…; 4 sahne taze` | kapı notu (KALDI değil; J3 §3D'de karşılığı yok, öneri: K8) | kol b'de 04–07 grup türevidir (huni-ab §4: "öteki türevler gruba aittir, yinelenmez"). KR-1 kol b koşusunda bu dizinleri UYGULANMAZ saymalı. 4 video sahnesi taze (§2). |
| `AB-2 GEÇTİ — … 0 beklenmeyen; zaman kayması (beklenen, Δ=1.000 sn): 4 dosya` | — | J3 K3 kapandı (`d846d6e`). 4 dosya: `01/devir.json` (değişken sahne), `03/proje/index.html`, `03/zamanlar.json`, `08/zamanlar.json` |

Öteki satırlar: AB-1, AB-3, AB-6, AB-8, AB-9, KS-6f GEÇTİ. ÖLÇÜLEMEDİ 5 (HV-1, HV-10, HV-17, HV-22, HV-23) tarayıcı ya da Whisper ister;
KBJ hükmü bunları elle ölçtü, bu turda kare ve ses değişmedi. AB-4, AB-5, AB-7 yayın sonrası (UYGULANMAZ).

## 6. Tek değişken (AB-3, AB-8, AB-9)

- **AB-9:** bu turda ses dosyasına dokunulmadı. Kapı: `AB-9 GEÇTİ — 5 ortak cümlenin ses sha256 eşit: a1↔b2, a2↔b3, a3↔b4, a4↔b5, a5↔b6`.
- **AB-3:** kare yeniden çekilmedi; var olan çiftler aynı göreli anda. Ölçüm (PIL `ImageChops.difference().getbbox()`): kol a `t` ↔ kol b
  `t + 1,00`, sahne 02, 08, 03, açık + koyu → **27/27 piksel eşit**. Kapı `AB-3 GEÇTİ`.
- **AB-8:** kapı `AB-8 GEÇTİ`. İstenen grep (K öneki `projeler/` olarak kısaltıldı; satırlar 260 karakterde kesildi):

```
$ grep -rnw "02-04-ydt-temel-s3" K/projeler/02-04-ydt-temel-s3b --include=*.js --include=*.html --include=*.json --include=*.py --include=*.sh
projeler/02-04-ydt-temel-s3b/sahneler/01-hyperframes-kapak/uret.py:3:Kol a (02-04-ydt-temel-s3) SPEC v2 §3 kodu + kol b kancası (`yanlis-cumle`, istem KBC-0204S3, taslak
projeler/02-04-ydt-temel-s3b/sahneler/01-hyperframes-kapak/yardim.py:1:"""02-04-ydt-temel-s3 sahne 01; 02-04-ydt-temel-s1 sahne 01 yardim.py birebir kopyası (ORTAK = S3 ortak/).
projeler/02-04-ydt-temel-s3b/sahneler/08-hyperframes-kaydet/uret.py:1:"""02-04-ydt-temel-s3 sahne 08 Kaydet (HyperFrames, DİKEY 1080x1920, huni v2).
projeler/02-04-ydt-temel-s3b/sahneler/05-hyperframes-kapak-b/calistir.sh:11:PAKET="$(cd "$AD/../.." && pwd)"            # paket kökü (02-04-ydt-temel-s3)
projeler/02-04-ydt-temel-s3b/sahneler/07-hyperframes-hikaye-b/calistir.sh:11:PAKET="$(cd "$AD/../.." && pwd)"            # paket kökü (02-04-ydt-temel-s3)
projeler/02-04-ydt-temel-s3b/sahneler/04-hyperframes-hikaye/calistir.sh:11:PAKET="$(cd "$AD/../.." && pwd)"            # paket kökü (02-04-ydt-temel-s3)
projeler/02-04-ydt-temel-s3b/sahneler/08-hyperframes-kaydet/calistir.sh:2:# Sahne 08 Kaydet (02-04-ydt-temel-s3, huni v2, HyperFrames DİKEY 1080x1920, 172 kare, t_bas 18,78 (DUZ2 15.11), cümle 4 öğretmen):
projeler/02-04-ydt-temel-s3b/sahneler/05-hyperframes-kapak-b/uret.py:2:"""02-04-ydt-temel-s3 sahne 05 kapak B (soru) index.html üretici (HyperFrames DİKEY 1080x1920; tek kare, ses yok).
projeler/02-04-ydt-temel-s3b/sahneler/02-hyperframes-ornek/uret.py:1:"""Sahne 02 — Örnek (02-04-ydt-temel-s3 shorts, HyperFrames DİKEY 1080x1920, huni v2).
projeler/02-04-ydt-temel-s3b/sahneler/05-hyperframes-kapak-b/yardim.py:1:"""02-04-ydt-temel-s3 sahne 05; 02-04-ydt-temel-s1 sahne 05 yardim.py'nin birebir kopyası (ORTAK = S3 ortak/).
projeler/02-04-ydt-temel-s3b/sahneler/06-hyperframes-kapak-c/uret.py:2:"""02-04-ydt-temel-s3 sahne 06 kapak C (karşıt çift) index.html üretici (HyperFrames DİKEY 1080x1920; tek kare, ses yok).
projeler/02-04-ydt-temel-s3b/sahneler/07-hyperframes-hikaye-b/yardim.py:1:"""02-04-ydt-temel-s3 sahne 07 (15.11): 02-04-ydt-temel-s1 sahne 07 yardim.py birebir kopyası (ORTAK = S3 ortak/).
projeler/02-04-ydt-temel-s3b/sahneler/02-hyperframes-ornek/calistir.sh:2:# Sahne 02 örnek + soru anı (02-04-ydt-temel-s3 shorts, HyperFrames DİKEY 1080x1920, 485 kare, t_bas 3,00; DUZ2 15.11):
projeler/02-04-ydt-temel-s3b/sahneler/06-hyperframes-kapak-c/calistir.sh:11:PAKET="$(cd "$AD/../.." && pwd)"            # paket kökü (02-04-ydt-temel-s3)
projeler/02-04-ydt-temel-s3b/sahneler/03-hyperframes-cta/yardim.py:4:02-04-ydt-temel-s3 (15.11): S1 sahne 03 kopyası, değişiklik yok; S3 ortak/kunye.js KUNYE S1 ile aynı (yalnız KOK, cipler)."""
projeler/02-04-ydt-temel-s3b/sahneler/06-hyperframes-kapak-c/yardim.py:1:"""02-04-ydt-temel-s3 sahne 06: 02-04-ydt-temel-s1/sahneler/06-hyperframes-kapak-c/yardim.py kopyası (yalnız bu satır değişti).
projeler/02-04-ydt-temel-s3b/sahneler/03-hyperframes-cta/calistir.sh:2:# Sahne 03 Çağrı (02-04-ydt-temel-s3, huni v2, HyperFrames DİKEY 1080x1920, 239 kare, t_bas 24,12 (DUZ2 15.11); cümle 5 öğrenci):
projeler/02-04-ydt-temel-s3b/sahneler/03-hyperframes-cta/uret.py:1:"""Sahne 03 Çağrı index.html ve zamanlar.json üretici (02-04-ydt-temel-s3; DİKEY 1080x1920; 239 kare = 7.9667 sn).
projeler/02-04-ydt-temel-s3b/ortak/anlatim/senaryo.json:149:  "kimlik": "02-04-ydt-temel-s3",
projeler/02-04-ydt-temel-s3b/uretim-tutanagi/kol-b.json:3:  "kol_a": "02-04-ydt-temel-s3",
(grep çıkış 0; 20 satır)
```

| Sınıf | Satır | Dosyalar |
|---|---|---|
| Python belge dizgisi (`"""…"""`, kod değil) | 11 | `01/uret.py:3`, `01/yardim.py:1`, `02/uret.py:1`, `03/uret.py:1`, `03/yardim.py:4`, `05/uret.py:2`, `05/yardim.py:1`, `06/uret.py:2`, `06/yardim.py:1`, `07/yardim.py:1`, `08/uret.py:1` |
| kabuk yorum satırı (`#` sonrası) | 7 | `02/calistir.sh:2`, `03/calistir.sh:2`, `08/calistir.sh:2`; `04`, `05`, `06`, `07/calistir.sh:11` (kod kısmı göreli `$AD/../..` → kol b kökü; eşleşme yorumda) |
| JSON `kimlik` alanı (AB-8 "sayılmaz" listesi) | 1 | `ortak/anlatim/senaryo.json:149` `meta.kimlik` (grup kimliği; kol a'da aynı değer) |
| tutanak kaydı, yol değil | 1 | `uretim-tutanagi/kol-b.json:3` `kol_a` (kol a kimliği; `varyant` kaydının eşi) |

Yol başvurusu 0, simge bağı 0 (kapı: "kol a içine simge bağı yok"). Yorum ve belge dizgilerindeki eski ad kopya kaynağını anlatır; bu tur
sahne koduna dokunulmadığı için düzeltilmedi.

## 7. diff kol a ↔ kol b sınıflaması

Komut: `diff -rq K/projeler/02-04-ydt-temel-s3 K/projeler/02-04-ydt-temel-s3b` → 211 satır (`uretim-tutanagi/diff-rq-duz4.txt`); satır başına sınıf:
`uretim-tutanagi/siniflama-duz4.txt`. DUZ2 r2 sınıflamasından (`siniflama-duz2-r2.txt`, 196 satır) 195 satır aynı sınıfla kaldı; 1 satır kalktı
(`Only in …-s3/uretim-tutanagi: kontak` → kol b'de de `kontak/` var, satır dosya adlarına bölündü); 16 satır yeni.

| Sınıf | Satır | Beklenen mi |
|---|---|---|
| QA karesi: küresel zaman adı +1,00 (içerik piksel eşit 27/27, DUZ4 yeniden ölçüldü) | 54 | beklenen |
| üretim tutanağı (paket başına) | 45 | beklenen |
| değişken sahne 01 (kanca) | 37 | beklenen |
| hyperframes durum dosyası (snapshot/check geçmişi) | 16 | beklenen |
| türev karesi yalnız kol a (huni-ab §4) | 12 | beklenen |
| ses: kanca cümlesi + numara kayması (c2–c6 = kol a c1–c5 bayt aynı) | 11 | beklenen (AB-9 GEÇTİ) |
| zaman ve söz türevleri (+1,00 sn) | 9 | beklenen |
| grup türevi yalnız kol a (huni-ab §4) | 7 | beklenen (yeni 2: `kapak-b-168.png`, `kapak-c-168.png`) |
| Python derleme önbelleği | 7 | beklenen |
| açıklama üst bilgisi + `utm_content` | 3 | beklenen |
| **zaman kayması +1,00 — "B3 bekliyor / K3"**: `08/zamanlar.json` (`t_bas` 18,78 → 19,78, 9 `kuresel` +1,00), `03/zamanlar.json` (`t_bas` 24,12 → 25,12), `03/proje/index.html` (gömülü `t_bas` 24,12 → 25,12) | 3 | beklenen. Bugünkü durum: B3 metni `huni-ab-sozlesme.md` §4'te yazılı; K3 `d846d6e` ile kapandı (kapı AB-2 GEÇTİ, Δ = 1,000) |
| kapak A (kanca karesi) | 2 | beklenen |
| kapak A 168 px (kanca karesi türevi; DUZ4 C1) | 1 | beklenen (yeni) |
| BRIEF kol b notu · senaryo (değişken cümle 1 + kol b üst bilgisi) · künye `KOK` kol b yolu (AB-8) · `surumler.json` | 4 | beklenen |
| **beklenmeyen** | **0** | — |

Yeni 16 satır: `kapak-a-168.png` farkı, `kapak-b-168.png` ve `kapak-c-168.png` (yalnız kol a), iki kolun `DUZ4-RAPOR.md` ve `huni-kapi-duz4.txt`
farkı, 4 kontak dosyası, `s3-huni-yanyana.png` (kol a eski kontak), iki yeni jüri hükmü, kol b'de `diff-rq-duz2-r2.txt`, `siniflama-duz2-r2.txt`,
`diff-rq-duz4.txt`, `siniflama-duz4.txt`.

## 8. Sürüm kaydı

`surumler.json` `revizyonlar` dizisine var olan alan düzeniyle (`surum`, `no`, `tarih`, `degisiklik`, `cikti`) ikinci satır eklendi:
`surum: s3b`, `no: r2`, `tarih: 2026-11-15T23:00:37Z`, `degisiklik` 372 karakter (≤ 500), `cikti: null`. Yeni alan yok; biçim (`indent=2`,
`ensure_ascii=False`, satır sonu) önceki dosyayla bayt eşit çıktı (sınandı).

## 9. Yapılmayan iş ve sebebi

| İş | Sebep |
|---|---|
| Kare yeniden çekimi | 4/4 video sahnesi taze (§2) |
| Çakışma kapısı | kare yenilenmedi (istem madde 5) |
| Koyu kontakta 01, 02, 03 için 3. kare | pakette o sahnelerin 2'şer koyu karesi var; yeni çekim istem dışı (J3 §5). Açık sayfa sahne başına ≥ 3 kuralını karşılar |
| #16 adayının düzeltmesi (02 t=7,6) | şef kararı: bu çiftte A sınıfı düzeltme yok; sahne 02 iki kolda ortak; sayım jürinin |
| ST-2 (rozet 26 px), EK-12 (kanca kartı sesten önce) | B1, B2 ölçüt kararı; kod değişmedi. Not: `juri-olcutleri.md` 16.11 yaması iki maddeyi de yazdı (ST-2 "rozet ≥ 26 px"; EK-12 kanca kartı istisnası); hüküm 3. tur jürinin |
| `senaryo.json` `zaman.giris` bayat alanı (`sure 3`, `ilkSoz 1`) | şef kararı: bu turun işi değil |
| AB-8 grep'teki yorum ve belge dizgileri | yol başvurusu değil; sahne koduna dokunma yasağı |
| KR-1 kol b 04–07 ÖLÇÜLEMEDİ | kapı işi (`huni-kapi.mjs`, şef); paket tarafında yapılacak iş yok |
| EK-4, EK-11 | insan kanıtı (şef, Nadir) |
| AB-4, AB-5, AB-7 | yayın sonrası maddeler |

Yazılan dosyalar (bu paket): `kapak-a-168.png`, `uretim-tutanagi/kontak/02-04-ydt-temel-s3b-duz4-kontak.png`,
`uretim-tutanagi/kontak/02-04-ydt-temel-s3b-duz4-kontak-koyu.png`, `uretim-tutanagi/huni-kapi-duz4.txt`, `uretim-tutanagi/diff-rq-duz4.txt`,
`uretim-tutanagi/siniflama-duz4.txt`, `surumler.json` (r2), bu dosya.
