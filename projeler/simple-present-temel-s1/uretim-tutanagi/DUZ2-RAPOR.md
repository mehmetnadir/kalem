# DUZ2-0202S1 raporu — `simple-present-temel-s1` (kol a) · J2 özeti A sınıfı düzeltmeleri · 16.11.2026

Girdi: `uretim-hatti/raporlar/J2-OZET-1511.md` §3A, §4.1, §4.2 satır P1, §4 "Sıra"; hüküm `uretim-tutanagi/juri/J2-hukum.md`.
Oturum: Claude Opus 5.5, tek oturum, alt ajan yok. 15.11 oturumu bellek arızasıyla yarıda kaldı; bu oturum yarım işi okudu, eksikleri
tamamladı ve her şeyi yeniden doğruladı (kareler bu oturumda baştan çekildi).

| Ölçüm | Değer |
|---|---|
| Düzeltilen kusur | A1 / TD-1 (rozet), A2 / TD-2 (SP karakteri kadın); C1 / HV-22 kanıtı (kapı yeniden koştu); C2 / HV-13 piksel çifti |
| P1'e düşmeyen | A3, A4, A5, A6, A7, TD-3, TD-4 (J2-OZET §4.2 satır P1 yalnız TD-1 + TD-2) |
| Yeniden sentezlenen cümle | **0** (P1'de ses işi yok; 4 cümlenin `cumle-N.wav` sha256 değeri değişmedi) |
| Toplam süre | **24,00 sn** (değişmedi; hedef 22–26, sınır 35) |
| Whisper en düşük | **1,00** (9 / 9 parça; eşik 0,90) |
| İlk söz · kanca sahnesi bitişi | 1,00 sn · 3,00 sn (HV-12 GEÇTİ) |
| Kanca cümlesi bitişi (bilgi) | 4,12 sn: 4 sn eşiğinin 0,12 sn üstü. HV-12 15.11 gece tanımında kanca = sahne 1 bitişi; cümle bitişi bilgi satırıdır |
| Çakışma kapısı (paket) | `node araclar/cakisma-kapisi.mjs simple-present-temel-s1 --port 41333 --sunucu 41022 --json projeler/simple-present-temel-s1/uretim-tutanagi/cakisma-DUZ2.json` → **çıkış 0**, 4 sahne, 0 hata, 0 uyarı |
| huni-kapi | `node D/araclar/huni-kapi.mjs projeler/simple-present-temel-s1` → 15 GEÇTİ, 2 KALDI (HV-1s araç sınırı, JR-1b jüri bayat; §5), 5 ÖLÇÜLEMEDİ, 6 UYGULANMAZ · HV-20 ve HV-24 GEÇTİ |
| mp4 | 0 (`find -name '*.mp4'` → 0; `proje/renders/` boş) |

## 1. Düzeltmeler

### 1.1 A1 / TD-1 — rozet `YDT · BASIC` → `YDT · TEMEL`

| Dosya | Önce → sonra | Kanıt |
|---|---|---|
| `ortak/anlatim/senaryo.json` `giris.rozetler` | `["YDT · BASIC"]` → `["YDT · TEMEL"]` | huni-kapi HV-24: "2 kaynakta rozet YDT · TEMEL; BASIC yok (21 dosya tarandı)" |
| `ortak/kunye.js` `KUNYE.rozet` (sahne 02 Paper.js künyesi buradan okur) | `"YDT · BASIC"` → `"YDT · TEMEL"` | aynı; kare `02-…-3.05.png` |
| `BRIEF-S1.md` (künye satırı, 0,00 sn satırı) | 2 yer | `grep BASIC` → 0 |
| `yardim.py` × 7 (01 `ROZET`; 03, 04, 05, 06, 07, 08 `ROZETLER`) | `BASIC` → `TEMEL` | `grep -rn BASIC --include=*.py` → 0 |
| `SPEC.md` × 6 (01, 04, 05, 06, 07, 08) | belge satırı | aynı |
| Yeniden üretilen sahne HTML: 01 `proje/` + `proje-ka/`, 03, 04, 05, 06, 07, 08 | hap genişliği 203,6 → 207,6 px (`nesneler.json` künye `w` 204 → 208; 05 `w` 453 → 457) | çakışma kapısı 0; kareler §3 |

Aynı karede iki rozet yok: çağrı karesinde künye ve ana kapak kartı ikisi de `YDT · TEMEL` (`04-…-23.95.png`, koyu dahil).

### 1.2 A2 / TD-2 — SP karakteri kadın (K22)

| Dosya | Önce → sonra | Kanıt |
|---|---|---|
| `ortak/kapak/karakter.png` | erkek (sha256 `a4198903833d…`) → ana paketin kadın karakteri, KOPYA (`5a902b401816…`) | `sha256sum`: ana paket `simple-present-temel/ortak/kapak/karakter.png` ile eşit; eski dosya `~/Silinecekler/2026-11-15-duz2-0202S1/s1/ortak-kapak/` |
| `ortak/kapak/ana-kapak.png`, `ana-kapak-koyu.png` | eski ana ders kapağı (`e2bbf46d…`, `df33df75…`) → ana paket `kapak.png` / `kapak-koyu.png` (`7f714514…`, `7e948a3b…`) | `sha256sum` eşit |
| `sahneler/04-hyperframes-cagri/proje/assets/ana-kapak*.png` | `calistir.sh` kopyası tazelendi (`7f714514…`, `7e948a3b…`) | kareler `04-…-20.9 / 22.5 / 23.95.png` (+ koyu): kartta kadın karakter |
| `sahneler/06-hyperframes-kapak-b/uret.py` | `KAR_KUTU` (152, 89, 744, 1113) → (148, 85, 793, 1024) · `BAS_X` 462 → 526 · `PARMAK` (154, 715) → (162, 502) · yeni `NESNE_UST` 16 · ölçek ve `ky` `KAR_KUTU`'dan; `ny` = parmak ucu + 16 − nesne üstü | `kapak-b.png`, `k/koyu/kapak-b-koyu.png` |
| `sahneler/06-…/nesneler.json` | nesne (195, 1116) → (157, 1132) · karakter (599, 923, 271×455) → (555, 924, 319×455) | aynı |

Karakteri kullanan sahne yalnız 06 (kapak B) ve 04 (çağrı, ana kapak kartı içinde). Kanca (01) Open Peeps figürü + otobüs çizimi
kullanır (`uret.py` `karakter.png` okumaz); kapak A, kapak C, hikâye A ve B karaktersiz. Bu sahnelerde karakter değişikliği yok.

Yerleşim denetimi (`kapak-standardi.md` §2 + huni §2/§6; yeni karakter sol eliyle sol üste işaret eder):

| Madde | Ölçüm | Sonuç |
|---|---|---|
| İçerik bandı 460–1380, sağ kenar ≤ 960 | karakter x 555–874, y 924–1379 · daire x 520–960 · nesne x 157–537, y 1132–1298 | içinde |
| Yazı ile karakter binmiyor | başlık bloğu alt kenarı 812 < karakter üstü 924 | evet |
| İşaret yönü | parmak ucu sol üstte; otobüs parmak ucunun altında ve solunda, arada 18 px | parmak otobüsü gösterir; çakışma yok |
| Çıkartma kenarı, daire | 10 px krem kenar; açık temada krem daire, koyuda daire yok | evet (yakın görünüm denetlendi) |

### 1.3 Ek: BRIEF can alıcı satırı (TD-3 ile aynı denklik)

| Dosya | Önce → sonra | Gerekçe |
|---|---|---|
| `BRIEF-S1.md` satır 12 | "Türkçedeki geniş zaman eki = İngilizcedeki s: gider = goes" → "Gider = goes; ama yalnız he, she, it ile. I, you, we, they ile go." | `senaryo.json` `meta.canAlici[0]` 15.11 22:38'de düzelmişti; BRIEF geride kalmıştı. Yeni cümle dil bilgisi açısından bağımsız doğru: üçüncü tekil kişide `goes`, öteki kişilerde `go`. Ses ve ekranda bu satır yok |

Kural cümlesi denetimi (istem: "öneriyi kendin de denetle"): P1'de A3/A4 önerisi yok. Var olan kural "He, she, it: s gelir; I, you,
we, they: s yok." olumlu cümlede doğrudur. `goes` örneğinde ek `-es` olur; jüri bunu "küçük kusur" diye yazdı, EK-5b "evet" verdi
(J2-OZET A3 tablosunda P1 yok). A sınıfı olmadığı için ses ve kart değişmedi.

## 2. Ses, süre, Whisper

Ses değişmedi; `el.py` koşmadı. Sözcük, altyazı ve karaoke zamanları değişmedi (`sozcukler.json`, `zaman.json` git farkı yok).

| Cümle | Ses | Başlangıç–bitiş (sn) | `cumle-N.wav` sha256 | Whisper duyulan | Benz. |
|---|---|---|---|---|---|
| 1 kanca | öğretmen | 1,00–4,12 | `e9fa0350749c…` | Kardeşim gider. Go mu, goes mu? | 1,00 |
| 2 değer (5 parça) | öğretmen | 4,67–14,63 | `bb9402dbf3f7…` | 5 × birebir | 1,00 |
| 3 kaydet | öğretmen | 15,18–17,74 | `9cb210d9225a…` | Sınavdan önce lazım olacak. Kaydet. | 1,00 |
| 4 çağrı (2 parça) | öğrenci | 18,29–23,00 | `dd50c6bcd452…` | Gerisi bizde. · Dersin tamamı YEDESE Publishing YouTube kanalında. | 1,00 |

Toplam 24,00 sn (4 sahne: 0–3,00 · 3,00–14,63 · 14,63–17,74 · 17,74–24,00).

## 3. Kareler (bu oturumda baştan çekildi; her kareye bakıldı)

Eski QA kareleri `~/qa-kare/simple-present-temel-s1/` altında duruyordu; `qa-yerel.sh` onları `k/` altına geri kopyalardı. Önce
Silinecekler'e taşındı (`qa-kare-eski/`), sonra her sahne tek koşuda çekildi.

| Sahne / türev | Komut | Kareler (açık · koyu) | Gördüğüm | Kapı |
|---|---|---|---|---|
| 01 kanca | `bash araclar/qa-yerel.sh simple-present-temel-s1 01-hyperframes-kanca 0,0.9,1.5,2.2,2.95 1.5 --hazirla` | 0 · 0,9 · 1,5 · 2,2 · 2,95 · koyu 1,5 | rozet TEMEL; kanal 0. sn'de; uçuşta rozet x ≈ 310; taşma yok; altyazı tek satır | 0 |
| Kapak A | S1-KAPAK-A yöntemi (sahne 01 RAPOR.md): `proje-ka` + `#altyazi{display:none}` + `hyperframes snapshot --at 0.90`, koyu önce | `kapak-a.png` = `kapak.png` (md5 `2d4d2d2d…`) · `k/koyu/kapak-a-koyu.png` | altyazı yok; kanal, rozet, başlık, hap, `?`, figür, otobüs | — |
| 02 değer | `… 02-paperjs-deger 3.05,4.5,8.8,14.55 8.8 --hazirla` | 3,05 · 4,5 · 8,8 · 14,55 · koyu 8,8 | künye `Simple Present` + TEMEL; `go-es` çemberi, `go` + çizili `s` | 0 |
| 03 kaydet | `… 03-hyperframes-kaydet 14.7,15.65,16.2,17.65 17.65 --hazirla` | 14,7 · 15,65 · 16,2 · 17,65 · koyu 17,65 | kart iki satır; yer imi SVG + `Kaydet` hapı | 0 |
| 04 çağrı | `… 04-hyperframes-cagri 17.8,20.9,22.5,23.95 23.95 --hazirla` | 17,8 · 20,9 · 22,5 · 23,95 · koyu 23,95 | ana kapak kartında kadın karakter + `YDT · TEMEL`; `@ydspublishing · YouTube` 20,9'dan sonra | 0 |
| 05 hikâye A | `bash calistir.sh --tema koyu` sonra `--tema acik` (`hyperframes snapshot`, mp4 yok) | `hikaye-a.png` (= `hikaye.png`, `cmp` eşit) · `k/koyu/hikaye-a-koyu.png` | kanal + künye + kural özeti + Kaydet; y 1150–1380 boş | — |
| 06 kapak B | aynı | `kapak-b.png` · `k/koyu/kapak-b-koyu.png` | kadın karakter otobüsü gösterir; §1.2 tablosu | — |
| 07 kapak C | aynı | `kapak-c.png` · `k/koyu/kapak-c-koyu.png` | `HE GOES` / `I GO`, rozet TEMEL | — |
| 08 hikâye B | aynı | `hikaye-b.png` · `k/koyu/hikaye-b-koyu.png` | soru kartı + kural özeti 2 satır + Kaydet (A6 karşılanır) | — |

Kare dizinleri: `~/qa-kare/simple-present-temel-s1/<sahne>/` ve sahne `k/`. Bütün PNG 1080×1920. Emoji yok. Statik türevler
çakışma kapısının `sahneler[]` listesinde değildir; göz denetimi yapıldı.

HV-13 (C2) piksel çifti, kart bölgesi x 60–960, y 560–1000, eşik 8/255: `03-…-15.65.png` ↔ `03-…-17.65.png` (2,00 sn) → **0 px**.

## 4. Kapı çıktısı

```
$ node araclar/cakisma-kapisi.mjs simple-present-temel-s1 --port 41333 --sunucu 41022 --json …/cakisma-DUZ2.json   → çıkış 0
01-hyperframes-kanca | çakışma yok (13 örnek, 6252 kutu)
02-paperjs-deger | çakışma yok (48 örnek, 1985 kutu)
03-hyperframes-kaydet | çakışma yok (14 örnek, 1542 kutu)
04-hyperframes-cagri | çakışma yok (26 örnek, 3880 kutu)
```

## 5. Düzeltilmeyen maddeler ve sebebi

| Madde | Sebep |
|---|---|
| EK-4 (C4), EK-8 (C5), EK-11 (C6), EK-12 (C7) | C sınıfı (kanıt eksikliği); J2-OZET sırası A → C. Sahibi şef, üretici ya da Nadir. Kareler hazır: C5 kontağı bu karelerden çıkar |
| KS-6 / C3 (`kapak-*-168.png`) | C sınıfı; istem kapsamı dışı. `magick` bu makinede kırık (`libwebp.so.6` yok); PIL ile üretilebilir |
| huni-kapi HV-1s KALDI | araç sınırı: betik `sahne-02.js` içinde `@ydspublishing` arar; sahne 02 kanal yazısını `ortak/kunye.js` (`yazi: "@ydspublishing"`) içinden çizer. Kareler 3,05 · 8,8 · 14,55'te kanal görünür |
| huni-kapi JR-1b KALDI | beklenen: içerik jüriden sonra değişti; J2 yeniden koşar (§1b) |
| HV-20a riski (ölçüt) | kapak B zemini sarı `#fece00`; yeni HV-20a kısa kapak zemini için krem `#f7f3ea` yazar. Tasarım kararı; şef bakar. Dokunulmadı |
| `meta.amaclar` "Türkçe geniş zaman eki ile köprü" (`senaryo.json`, `surumler.json`) | denklik değil, amaç satırı; J2-OZET §0.2 P1'i temiz sayar; TD-3 kapsamı P2/P3. Dokunulmadı |
| "s gelir" / `-es` | jüri notu; EK-5b geçti; A sınıfı değil (§1.3) |

## 6. Silinecekler

`~/Silinecekler/2026-11-15-duz2-0202S1/` (`LISTE.md`): `s1/ortak-kapak/` (erkek karakter, eski ana kapak), `s1/eski-kare/<sahne>/k/`,
`s1/eski-kok/*.png` (eski türevler), `qa-kare-eski/simple-present-temel-s1/`. Silme yok.

---
Son Güncelleme: 16.11.2026 — ilk sürüm (DUZ2-0202S1).
