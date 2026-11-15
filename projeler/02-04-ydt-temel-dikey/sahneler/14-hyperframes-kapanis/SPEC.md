# SPEC — 02-04-ydt-temel-dikey · sahne 14-hyperframes-kapanis (HyperFrames, 1080×1920, 431 kare)

Kaynak: `projeler/02-04-ydt-temel-dikey/BRIEF-DIKEY.md` §2 + §3 satır 14. Yazan: şef (15.11.2026). Kod yazmaz; tasarım verir.
K = `/home/sef/01dev/_worktrees/kalem-0204`. Sahne dizini D = `K/projeler/02-04-ydt-temel-dikey/sahneler/14-hyperframes-kapanis/`.

## 1. Yazılacak dosyalar

| Dosya | Durum | İş |
|---|---|---|
| `D/yardim.py` | VAR (dikey sahne 01 `yardim.py` kopyası) | yalnız `kunye_svg()` işlevini §3'e göre değiştir; docstring 1. satırına "sahne 14" yaz. Başka işleve DOKUNMA |
| `D/uret.py` | YOK | §4'e göre yaz |
| `D/olay.py` | VAR (dikey sahne 01 kopyası) | DOKUNMA; `U.uret()` → `(s, _)` ve `U.Z["kare"]` ister |
| `D/calistir.sh` | VAR (şef uyarladı, KARE 431) | DOKUNMA |

Başka dosyaya dokunma. Silme yok. Test, render, git yok. `ortak/`, BRIEF, yatay paket, öteki sahneler salt okunur.

## 2. Kalıp kaynakları (salt oku)

| Kalıp | Mutlak yol | Ne alınır |
|---|---|---|
| İçerik + olay sırası (yatay) | `K/projeler/02-04-ydt-temel/sahneler/14-hyperframes-kapanis/uret.py` | `T(i, bas)` (sözcük kayarsa assert), `g()`, `kayit()` olay kaydı, MEANING/FIRST kinetik `fromto` (opacity, y, scale, svgOrigin, `back.out(1.6)`), `s.yol` alt çizgi, `Y.el_daire` numara halkaları, `s.yazi` soru parçaları (boşluksuz parça + `SORU_ARA`, yazma süresi `0.12 + w/1100`, `or` için `tur=None`), `Y.el_kutu` kart, `Y.el_ok` ok, `Y.kontrol(s, Z["kare"])`, `__main__` olay tablosu çıktısı |
| Dikey iskelet (aynı paket) | `K/projeler/02-04-ydt-temel-dikey/sahneler/01-hyperframes-giris/uret.py` | dosya başı (PAKET, SAH, Z, SOZ, R), `uret()` → `(s, kun)` dönüşü, `__main__` içinde `Y.altyazi_dilimleri` + `Y.altyazi_svg` + `Y.html(..., ek=altyazi)` |
| Altyazı dilim geçişi | `K/projeler/present-continuous-dikey/sahneler/06-hyperframes-form/uret.py` satır 303–320 (`aktif(t)`) | kare kare etkin dilim; dilim değişince öncekine opaklık 0, yenisine 1 (`s.set`). İki dilim aynı anda görünmez |
| Dikey HUD (tam) | `K/projeler/present-continuous-dikey/sahneler/06-hyperframes-form/yardim.py` `kunye_svg()` (satır 144–162) | `ku-ders` metni, `ku-rz` rozet hapı (rect + text), `cip()` iç işlevi |
| HUD sayıları | `K/projeler/02-04-ydt-temel-dikey/ortak/kunye.js` `KUNYE`, `kunyeCiz`, `dersDuzen` | ders 2 satır, rozet x = 48 + 2. satır genişliği + 24 |

## 3. `yardim.py` — yeni `kunye_svg(bolum)` (tam dikey HUD, BRIEF-DIKEY §2.1)

Çıktı tek `<g id="kunye">`, içinde sırayla:
1. `<g id="ku-ders">`: iki `<text>`, x 48, taban y 212 ve 276, Fredoka 700 56, `fill=RENK["murekkep"]`:
   `SIMPLE PRESENT vs` / `PRESENT CONTINUOUS`.
2. `<g id="ku-rz">`: rozet hapı. rx0 = 48 + `genislik("Fredoka", 700, "PRESENT CONTINUOUS", 56)` + 24 (≈ 670).
   rw = `genislik("Lexend", 700, "YDT · BASIC", 36)` + 56 (≈ 282). `rect` x rx0, y 216, w rw, h 72, rx 36, `fill=RENK["vurgu"]`
   (hf_tema rect dolgusunu vurguDolgu yapar). `text` x rx0 + rw/2, y 265, `text-anchor="middle"`, Lexend 700 36,
   `fill=RENK["zemin"]` (= `#1b1a17`; hf_tema `text[fill="#1b1a17"]` → pilMetin). Metin `YDT · BASIC`.
3. `<g id="ku-bolum">`: çip (sahne 01 işlevindeki çizimin aynısı: cw = metin + 64, x = 1032 − cw, y 48, h 80, rx 40,
   `fill="none"`, vurgu çerçeve 4 px, Lexend 700 40, metin tabanı y 102, ortalı, vurgu yazı).
- `gizli` parametresi kalkar (bu sahnede HUD kare 0'dan tam görünür).
- ID YASAĞI: `t1`, `t2`, `rz1`, `ku-nokta` kullanma (hf_tema CSS bunlara özel kural uygular; `rz1` rozet yazısını zemin rengine boyar).
- Ders kutusu sağ ucu (48 + 598 ≈ 646) < rozet x; rozet sağ ucu (≈ 952) ≤ 1032; rozet üstü 216 > çip altı 128: çakışma yok.

## 4. `uret.py` (yeni) — yerleşim, olaylar, kurallar

### 4.1 Okuma
- `PAKET = AD.parent.parent`; `zaman.json`'dan `klasor == AD.name` sahnesi: t_bas 251,27, kare 431 → `Z["sure"]` = 431/30.
- `PAKET/ortak/anlatim/sozcukler.json` cümle 18 sözcükleri (27 sözcük). Zaman dosyadan okunur, sabit yazılmaz.
- Yerel sn = küresel − t_bas (`s.S()`).

### 4.2 Sabitler (px = `u()`; BRIEF-DIKEY §3 satır 14)
| Ad | Değer | Not |
|---|---|---|
| SOL | u(96) | sol hiza: başlık + numara halkaları |
| BAS_Y, BAS_BOY | u(505), u(120) | MEANING FIRST tabanı, Fredoka 700 (bant y ≈ 422–545) |
| ALT_Y, ALT_W | BAS_Y + u(34), u(11) | sarı alt çizgi: taban + 0,28 em; kalınlık (belirteç 9–12) |
| SORU_Y | u(690), u(840), u(990) | üç soru satırı tabanı (satır 150; bant 600–1060) |
| SORU_BOY | u(88) | Caveat 700 |
| HALKA_R, NUM_BOY | u(46), u(64) | numara halkası yarıçapı; numara Fredoka 700 64 (içerik yazısı ≥ 64) |
| HALKA_CX, HALKA_DY | SOL + HALKA_R, u(30) | halka merkezi x; merkez y = satır tabanı − HALKA_DY |
| SORU_X | SOL + 2·HALKA_R + u(36) | soru yazı başı (≈ 224) |
| SORU_ARA | Caveat boşluk genişliği (88) + u(8) | parça arası; parçalar boşluksuz (yatay kapı dersi) |
| KART | (u(48), u(1100), u(984), u(280)) | sonraki ders kartı x, y, w, h (BRIEF §2.6: genişlik 984, x 48–1032) |
| KART_IC | u(40) | kart iç boşluğu |
| NL_Y, NL_BOY | KART_y + u(96), u(56) | `Next lesson` tabanı (≈ 1196), Lexend 500 |
| SV_Y, SV_BOY | KART_y + u(216), u(96) | `Stative Verbs` tabanı (≈ 1316), Fredoka 700 |
| OK | x0 = kx + kw − u(262), x1 = kx + kw − u(64), y = SV_Y − u(34) | sarı ok `Stative Verbs` satırında sağda (≈ 770 → 968, y ≈ 1282); kalınlık u(10) |
| VURUS | 0,22 sn, `back.out(1.6)` | stil §4 |

### 4.3 Olay listesi (cümle 18; `T(i, bas)` ile; kare = yerel sn × 30)
| # | Olay | Küresel sn | Yerel sn (kare) | Cümle sözcüğü (i) | Ses olayı |
|---|---|---|---|---|---|
| 0 | HUD tam (logo, ders 2 satır, rozet, çip `Next lesson`) | — | kare 0'dan | — | — |
| 1 | altyazı dilim 0 görünür | 251,77 | 0,50 (15) | Dil (0) − 0,05 | — |
| 2 | `MEANING` kinetik (x SOL, taban BAS_Y) | 251,82 | 0,55 (16) | Dil (0) | `tik` 0,55 |
| 3 | `FIRST` kinetik (x SOL + g("MEANING ")) | 252,14 | 0,87 (26) | sınavında (1) | `tik` 0,55 |
| 4 | sarı alt çizgi MEANING FIRST (`el_cizgi` SOL − 6 → sağ uç + 6, y ALT_Y; 0,45 sn, alfa 0,9) | 252,62 | 1,35 (40) | boşluğu (2) | `cizgi` 0,6 |
| 5 | numara halkaları 1 · 2 · 3 (`el_daire`, 0,12 sn ara, 0,32 sn, ikincil, kalınlık u(4)); numara halka + 0,12 sn, 0,15 sn | 253,58 | 2,31 (69) | üç (4) | `cizgi` 0,4 ×3 |
| 6 | soru 1: `general` · `or` · `now?` | 254,78 / 255,18 / 255,66 | 3,51 / 3,91 / 4,39 | Genel (7) / mi (8) / şu (9) | `tik` 0,45 (or yok) |
| 7 | soru 2: `permanent` · `or` · `temporary?` | 256,54 / 257,02 / 257,42 | 5,27 / 5,75 / 6,15 | Kalıcı (12) / mı (13) / geçici (14) | `tik` 0,45 |
| 8 | altyazı dilim 0 → dilim 1 | 258,25 | 6,98 (209) | Tarife (16) − 0,05 | — |
| 9 | soru 3: `timetable` · `or` · `plan?` | 258,30 / 258,86 / 259,26 | 7,03 / 7,59 / 7,99 | Tarife (16) / mi (17) / plan (18) | `tik` 0,45 |
| 10 | kart çerçevesi (`el_kutu`, 0,55 sn, ikincil, u(4)) | 260,30 | 9,03 (271) | Sonraki (20) | `cizgi` 0,55 |
| 11 | `Next lesson` (Lexend 500 56, ikincil; 0,3 sn) | 260,70 | 9,43 (283) | derste (21) | — |
| 12 | `Stative` (Fredoka 700 96, mürekkep; 0,3 sn) | 261,18 | 9,91 (297) | -ing (22) | `tik` 0,5 |
| 13 | `Verbs` (x + g("Stative ")) | 262,06 | 10,79 (324) | fiilleri (24) | `tik` 0,5 |
| 14 | sarı ok ileri (`el_ok`, 0,3 sn, vurgu, u(10)) | 262,50 | 11,23 (337) | görüyoruz (25) | `cizgi` 0,5 |
| 15 | altyazı dilim 1 söner (t1 264,22 + 0,35) | 264,57 | 13,30 (399) | — | — |
| 16 | durgun son düzen; kare 401'den sonrası kuyruk; geçiş yok | — | 11,53 → 14,37 | Görüşürüz (26) olaysız | — |

Sözcük denetimi (`T(i, bas)` bas önekleri): 0 "Dil", 1 "sınav", 2 "boşluğu", 4 "üç", 7 "Genel", 8 "mi", 9 "şu", 12 "Kalıcı",
13 "mı", 14 "geçici", 16 "Tarife", 17 "mi", 18 "plan", 20 "Sonraki", 21 "derste", 22 "-ing", 24 "fiil", 25 "görüyoruz".
Hareket en geç 11,53'te biter. `Y.kontrol(s, Z["kare"])` (ilk=True: ilk 12 kare durgun — ilk hareket 0,55; son 12 kare durgun).

### 4.4 Altyazı
- `dil = Y.altyazi_dilimleri([18])` → 2 dilim (ölçüldü): (251,82–258,30) `Dil sınavında … geçici mi?` ve (258,30–264,22) `Tarife mi, …`.
- Geçiş: 06 kalıbı `aktif(t)` (kare kare, `t0 − 0,05 ≤ t < t1 + 0,35`, son eşleşen dilim kazanır). Dilim değişince `s.set("#alt<önceki>", f/30,
  opacity 0)` + `s.set("#alt<yeni>", f/30, opacity 1)`. Komutlar `uret()` içinde; SVG dizgisi `__main__`te `Y.altyazi_svg([{id: "alt<i>", metin}])`.
- Altyazı bandında karaoke YOK (Nadir 03.11 "karaoke şeridi yok"; sahne 01 ile aynı). Sözcükler söylenince ekranda kinetik gelir.

### 4.5 Yerleşim (1080×1920; bantlar BRIEF §2)
```
y   48 ┌ logo 387×96            [ Next lesson ] çip ┐  HUD 0–320 (kare 0'dan)
  212  │ SIMPLE PRESENT vs                          │
  276  │ PRESENT CONTINUOUS  (YDT · BASIC)          │
  ~422 │ MEANING FIRST            (taban 505, 120)  │  içerik 352–1392
  ~539 │ ═════════ sarı alt çizgi ═══════           │
  ~614 │ (1)  general  or  now?          (taban 690)│  halka r 46, merkez (142, taban−30)
  ~764 │ (2)  permanent  or  temporary?  (taban 840)│  sağ uç ≈ 1000 ≤ 1032
  ~914 │ (3)  timetable  or  plan?       (taban 990)│
 1100  │ ┌ kart 48–1032 ───────────────────────┐    │
 1196  │ │ Next lesson   (Lexend 500 56)        │    │
 1316  │ │ Stative Verbs (Fredoka 96)   ───→    │    │  ok 770→968, y 1282
 1380  │ └──────────────────────────────────────┘    │
 1456  │ altyazı 2 satır (Lexend 500 44)             │  1400–1536
 1536  └ PLATFORM: hiçbir öğe yok                    ┘
```

### 4.6 Ekran metni ve renk (KOYU hex yaz; hf_tema temaya çevirir)
| Öğe | Metin | Yazı | Renk (hex) → tema |
|---|---|---|---|
| başlık | `MEANING` `FIRST` | Fredoka 700 120 | `#f3efe6` → murekkep |
| alt çizgi, ok | — | yol | `#f2a93b` → vurgu (tek vurgu) |
| halkalar | — | yol | `#c9c2b3` → ikincil |
| numaralar | `1` `2` `3` | Fredoka 700 64 | murekkep |
| soru parçaları | `general` `now?` `permanent` `temporary?` `timetable` `plan?` | Caveat 700 88 | murekkep |
| `or` ×3 | `or` | Caveat 700 88 | ikincil |
| kart çerçevesi | — | yol | ikincil |
| kart başlığı | `Next lesson` | Lexend 500 56 | ikincil (BRIEF §3 satır 14) |
| kart adı | `Stative` `Verbs` | Fredoka 700 96 | murekkep |
| altyazı | cümle 18 dilimleri | Lexend 500 44 | murekkep |
Yeşil yok (doğru şık yok), kırmızı yok, emoji yok, gradyan yok, gölge yok.

### 4.7 Kurallar ve assert'ler (uret.py içinde, ihlalde dur)
- ID'ler: `mfa`, `mfb` (başlık sözcükleri), `mfc` (alt çizgi), `nh0–nh2` (halka), `nn0–nn2` (numara), `q00–q22` (soru parçaları),
  `kk` (kart), `k1` (Next lesson), `k2`, `k3` (Stative, Verbs), `kok` (ok), `alt0`, `alt1` (altyazı). `t1`, `t2`, `rz1`, `ku-nokta` YASAK.
- Assert:
  - MEANING FIRST sağ ucu ≤ W − 48; başlık üstü (BAS_Y − 0,72·BAS_BOY) ≥ 352.
  - her soru satırının sağ ucu (SORU_X + parça genişlikleri + 2·SORU_ARA) ≤ W − 48.
  - halka 1 üstü (SORU_Y[0] − HALKA_DY − HALKA_R) − ALT_Y ≥ u(40) (alt çizgi ile halka arası).
  - satır 3 altı (SORU_Y[2] + 0,3·SORU_BOY) + u(40) ≤ KART_y.
  - `Next lesson` ve `Stative Verbs` sağ ucu ≤ kx + kw − KART_IC; OK x0 − (kx + KART_IC + g("Stative Verbs", 96)) ≥ u(48).
  - kart altı (ky + kh) ≤ 1392; her parça yazma süresi bir sonraki parçanın başlangıcından önce biter.
- `uret()` tam 2 değer döndürür: `(s, Y.kunye_svg("Next lesson"))` (olay.py `s, _ = U.uret()` ile okur).
- `__main__`: `proje/index.html` yaz (`Y.html(s, Z["sure"], kun, None, (48, 48, round(96 * Y.LOGO_EN_BOY, 2), 96), ek=altyazi)`),
  komut/olay sayısını, hareket aralığını ve yatay `__main__` gibi olay tablosunu (yerel sn, kare, sözcük, ad) bas.
- Python: girinti 4 boşluk (kopya kalıpla uyum), satır ≤ 140. Çalıştırma `/usr/bin/python3 uret.py` (fontTools kullanıcı site-packages; `-I` yok).

## 5. Tema notu
uret.py koyu hex yazar. `calistir.sh` → `tema_hf` (hf_tema.py) `#root`a CSS değişkenlerini ve `tema-acik` sınıfını ekler:
`#f3efe6` → murekkep, `#c9c2b3` → ikincil, `#f2a93b` → vurgu (rect dolgusu → vurguDolgu), `text[fill="#1b1a17"]` → pilMetin.

## 6. Kabul ölçütü
1. `cd D && /usr/bin/python3 uret.py && /usr/bin/python3 olay.py` çıkış 0; assert yok; `olaylar.json` ≈ 16 olay, hepsi kare < 419.
2. `proje/index.html`: `data-width="1080" data-height="1920"`; `#kunye` içinde `ku-ders`, `ku-rz`, `ku-bolum`; `#logoimg` (48, 48, 387×96); `alt0`, `alt1`.
3. `cd K && bash araclar/qa-yerel.sh 02-04-ydt-temel-dikey 14-hyperframes-kapanis 256.0,260.1,263.6 263.0 --hazirla` çıkış 0 (şef koşar).
4. Kareler: taşma, kesik yazı, üst üste binme, okunmaz kontrast, boş kare, platform bandında öğe YOK; altyazı bandında metin.
