# DUZ2-0204S2 raporu — `02-04-ydt-temel-s2` (kol a) · J2 A sınıfı düzeltmeleri · 15.11.2026

| Ölçüm | Değer |
|---|---|
| Düzeltilen kusur | A1 / TD-1 (rozet, HV-24), A6 (hikâye B kural özeti, HV-21), TD-4 (bayat UTM notu) |
| Ses | değişmedi: yeniden sentez 0 cümle (T2'de A3/A4 satırı yok) |
| Süre | 29,41 sn (değişmedi; kabul ≤ 35 sağlandı, hedef 22–26 aşıldı) |
| Whisper | 10 / 10 parça 1,00 (en düşük 1,00) |
| Kareler | 44 sahne karesi (`k/`) + 7 kök türev, açık + koyu; hepsine baktım |
| Çakışma kapısı | çıkış 0 (4 sahne, çakışma yok) |
| mp4 | yok (render koşulmadı) |
| Kol b | ayrı rapor: `../../02-04-ydt-temel-s2b/uretim-tutanagi/DUZ2-RAPOR.md` |
| Üretici model | Claude Opus 5.5 (`claude-opus-5-5`) |

Girdi: `uretim-hatti/raporlar/J2-OZET-1511.md` §3A, §4.1, §4.2 satır T2; `juri/J2-hukum.md`; `D/.claude/docs/` standartları (15.11 akşam sürümü).
Sıra (J2-OZET §4 "Sıra"): ses (iş yok) → metin ve kart → kareler tek koşuda → kapı.

## 1. Düzeltmeler

| # | Kusur | Dosya | Önce → sonra | Kanıt |
|---|---|---|---|---|
| 1 | A1 / TD-1 (J2 KS-2; ölçüt HV-24) | `ortak/anlatim/senaryo.json` (`giris.rozetler`), `BRIEF-S2.md` (2 yer), `ortak/kunye.js` (`KUNYE.rozet`), `sahneler/02-paperjs-ornek/sahne-02.js` (`ROZET`), `yardim.py` × 7 (01, 03, 04, 05, 06, 07, 08; 08'de belge satırı dahil 2 yer), `uret.py` denetimleri 04, 06 (2 yer), 07 | `YDT · BASIC` → `YDT · TEMEL` (14 dosya, 18 yer) | `grep -rn BASIC` kaynak kümesi (js, py, json, sh, BRIEF): 0 satır; çıktı (`sahneler/*/proje/index.html`, `ortak/*.js`, `senaryo.json`, `sahne-02.js`): 0 dosya. Kareler: bütün kareler `YDT · TEMEL`; sahne 03 karesinde künye rozeti ve ana kapak kartı rozeti artık aynı metin (`03-hyperframes-cta-29.35.png`) |
| 2 | A6 (J2 HV-21) | `sahneler/07-hyperframes-hikaye-b/uret.py` | ipucu satırı `Genel mi, şu an mı?` → kural özeti `Genel: wears · Şu an: is wearing` (Caveat 700, 64 px, x 60, taban 1004, genişlik 693 px; blok y 956–1023, öteki bloklar yerinde) | `hikaye-b.png`; `sahneler/07-hyperframes-hikaye-b/k/koyu/hikaye-b-koyu.png`; `uret.py` denetimleri geçti (`kural=956-1023 kaydet=1036-1138`, 1150–1920 boş) |
| 3 | TD-4 | `aciklama.md`, `aciklama-a.md` (§4, 2 satır), `aciklama-b.md` (§4, 1 satır), `uretim-tutanagi/aciklama-taslak.md` (§2 DİKKAT notu 2 satır + eski satır 174 sonundaki aynı bayat cümle) | "S1 `utm_campaign=ing-ydt-gr-02-04-t` (küçük harf) yazar" notu → silindi | `grep -ohE "utm_campaign=…" 02-04-ydt-temel-s1*/aciklama*.md`: 30 / 30 `ING-YDT-GR-02-04-T`; T2 açıklamalarında `ing-ydt-gr` 0 |
| 4 | C1 (HV-22) yan ürünü | `uretim-tutanagi/cakisma-DUZ2.json`, `cakisma-DUZ2.txt` | v2 kapı çıktısı yoktu → var | §4 |

### 1.1 A6 metni: karar ve dil denetimi

| Soru | Cevap |
|---|---|
| Neden bu metin? | J2-OZET önerisi "Genel → wears · şu an → is wearing". `→` glifi Caveat, Fredoka ve Lexend dosyalarında yok (fontTools cmap, latin + latin-ext). Ok yerine iki nokta kullandım. Biçim sesteki "Genel durum: geniş zaman." cümlesiyle aynı |
| Sesle aynı terim mi? | Evet. "Genel" ve "şu an" cümle 1'de ("Genel mi, şu an mı?") geçer |
| Kaynaktan bağımsız doğru mu? | Evet. Satır örnek fiile bağlıdır: genel durum ya da alışkanlık → `wears` (Simple Present); konuşma anında süren eylem → `is wearing` (Present Continuous). `wear` eylem fiilidir. Satır durum fiillerine (know, like) genelleme yapmaz |
| Soru kartını cevaplıyor mu? | Hayır. Kart "Look!" işaretini taşır; öğrenci işareti kural satırıyla kendisi eşler |
| Neden ipucu satırının yerine? | Hikâye karesinde içerik 1150'de biter; Kaydet 1036–1138. İkinci satıra yer yok. İpucu sorusunun iki terimi kural satırında kalır |
| 24 karakter sınırı | Satır 32 karakter. `uret.py` 24 sınırını bu satır için genişlik denetimine çevirdim (x 60 + 693 ≤ 960). Gerekçe: ≤ 24 karakter ders kalıbıdır (DK-2); kısa türevde HV-25 yalnız altyazıyı ölçer |

## 2. Ses, süre ve Whisper

Ses değişmedi. Cümle dosyaları bu oturumdan önce yazıldı (`anlatim.m4a` 15.11 18:25); sha256 değerleri KBC-RAPOR tablosuyla aynı.

| Ölçü | Değer | Sınır |
|---|---|---|
| Toplam (`ffprobe anlatim.m4a`) | 29,41 sn | ≤ 35 sağlandı; hedef 22–26 aşıldı (açık nokta, A değil) |
| İlk söz (`sozcukler.json` "Genel" t0) | 1,00 sn | ≤ 1 sn: sınırda |
| Kanca cümlesi bitişi ("mı?" t1) | 2,92 sn | kanca ≤ 4 sn sağlandı. Not: sahne 01 2,84'te biter; son hece 0,08 sn sahne 02'ye taşar |
| Whisper (`sentez.wav.rapor.json`) | 10 / 10 parça 1,00 | ≥ 0,90 |
| Cümle sha256 (ilk 12) | 1 `0b0dafd59a98` · 2 `1d805b981216` · 3 `720b3d7cc552` · 4 `b192db36b66b` | değişmedi |
| Yeniden sentez | 0 cümle | — |

## 3. Kareler (tek koşu)

Yöntem: HyperFrames sahneleri önce `ONIZLE_YALNIZ=1 bash calistir.sh --tema acik` ile yeniden üretildi (render yok). Video sahneleri
`node araclar/sahne-kare.mjs <paket> <sahne> <t…> <dizin> --tema acik|koyu --port 41333 --sunucu 41022` ile çekildi. Durağan türevler
(04–07) `bash calistir.sh --tema koyu`, sonra `--tema acik` ile çekildi (`hyperframes snapshot`, mp4 yok; son hâl açık tema).

| Sahne / türev | Açık | Koyu |
|---|---|---|
| Kapak A (01 @ 0,9) | `kapak-a.png` = `kapak.png` (md5 `ac89abad8bcd`) | `sahneler/01-hyperframes-kapak/k/koyu/kapak-a-koyu.png` |
| Kapak B, C | `kapak-b.png`, `kapak-c.png` | `05…/k/koyu/kapak-b-koyu.png`, `06…/k/koyu/kapak-c-koyu.png` |
| Hikâye A, B | `hikaye-a.png` = `hikaye.png`, `hikaye-b.png` | `04…/k/hikaye-a-koyu.png`, `07…/k/koyu/hikaye-b-koyu.png` |
| 01 kanca | 0 · 0,9 · 1,5 · 2,4 · 2,5 · 2,6 · 2,8 | 0,9 |
| 02 değer | 2,84 · 10,1 · 17,35; `k/ara/` 4,9 · 7,6 · 12 · 14,6 · 16,1 | 14,9 |
| 08 kaydet | 17,41 · 20,1 · 22,7; `k/ara/` 20,72 · 22,27 | 22,7; `k/ara/koyu/` 22,27 |
| 03 çağrı | 22,75 · 26,5 · 29,35 | 28,5 |
| 07 yakın kırpım | `07…/k/qa/yakin-kok-sik{,-acik}.png` | `…-koyu.png` |

Baktıklarım (Read; kontak sayfası + tam boy kırpım): taşma yok, çakışma yok, okunmayan yazı yok. Rozet her karede `YDT · TEMEL`.
Karakter: kapak B'de öğrenci (kadın, uzun kâkül, yuvarlak gözlük; kadro ile aynı), kapak A'da öğretmen figürü. Altyazı 1400–1550 bandında,
kapak A karesinde altyazı yok. Hikâye B kural satırı açık ve koyu temada okunur; Ş doğru çizili.
Gözlem (kapsam dışı, önceden de böyle): 01'in 0,00 karesinde `≠` henüz çizilmemiş (`GENEL / ŞU AN`); kapak karesi 0,9'dan alınır.

## 4. Çakışma kapısı

Komut: `node araclar/cakisma-kapisi.mjs 02-04-ydt-temel-s2 --port 41333 --sunucu 41022 --json projeler/02-04-ydt-temel-s2/uretim-tutanagi/cakisma-DUZ2.json`
Çıkış kodu: **0** (47 sn). 01 13 örnek · 02 60 · 08 23 · 03 28; çakışma yok. Durağan türevler (04–07) kapının zaman çizelgesinde yok; onlara gözle baktım (§3).

## 5. Metin taraması

`Tam ders` 0 dosya · `dakika` 0 dosya · `BASIC` (çıktı) 0 dosya · mp4 0 (`find -name '*.mp4'`). Küme: sahne `proje/index.html`, `ortak/*.js`,
`ortak/anlatim/*.json`, açıklamalar, `sahne-02.js`.

## 6. Düzeltilmeyen maddeler

| Madde | Sınıf | Sebep |
|---|---|---|
| HV-17 "YEDESE" | B1 (ölçüt) | İstem: B sınıfına dokunma. Güncel HV-17 bu dökümü beklenen davranış sayar |
| KS-3 krem zemin | B3 (ölçüt) | İstem: dokunma. Güncel ölçüt kısa kapakta HV-20a'yı uygular (açık `#f7f3ea`) |
| KS-4 kapak B = başlık B | B4 (ölçüt) | İstem: dokunma. **Risk:** güncel HV-20b'ye göre kapak B "TODAY VARSA HANGİ ZAMAN?" `aciklama-b.md` YouTube başlığını ("Today varsa hangi zaman?") birebir yineler; J2 yeniden koşusunda kaldı çıkabilir. Karar şefte |
| HV-13 kart 2 sn sabitliği | C2 (kanıt) | J2-OZET sırası adım 5; bu istemin kapsamı dışı. Kare üçlüsü (18,2 · 20,2 · 22,2) çekilmedi |
| KS-6, EK-8, EK-11, EK-12 | C3, C5, C6, C7 (kanıt) | J2-OZET sırası adım 5 ve şef/Nadir işi; kapsam dışı |
| Süre 29,41 > hedef 22–26 | açık nokta | A listesinde yok; ses yazımı kararı şefte |
| `SPEC.md`, `RAPOR.md`, `uretim-tutanagi/istem/` içindeki `YDT · BASIC` ve "ipucu" | belge | Tarihî üretim kaydı; çıktı değil. Kaynak artık `yardim.py` / `uret.py` |
| Hikâye A etiketleri İngilizce (`GENERAL`, `RIGHT NOW`) | gözlem | Değer sahnesiyle aynı; J2 geçti. Hikâye B kural satırı sesin Türkçe terimini taşır |

## 7. Değişen dosyalar

Kaynak: `ortak/anlatim/senaryo.json`, `BRIEF-S2.md`, `ortak/kunye.js`, `sahneler/02-paperjs-ornek/sahne-02.js`, `sahneler/0{1,3,4,5,6,7,8}-*/yardim.py`,
`sahneler/0{4,6,7}-*/uret.py`, `aciklama{,-a,-b}.md`, `uretim-tutanagi/aciklama-taslak.md`, `surumler.json` (`revizyonlar` r1).
Türetilmiş: `sahneler/*/proje/index.html`, `nesneler.json` (04–07), `olaylar.json`, `proje/assets/logo.svg` (04, 06: son çalıştırma koyu temadaydı,
şimdi açık), kök PNG × 7, `k/` kareleri. Silinecekler: `~/Silinecekler/2026-11-15-duz2-0204S2/` (eski 3 yakın kırpım; `LISTE.md`).
Paket dışı: yok. Sözleşme ve `ortak/` dokunulmadı.
