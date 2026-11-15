# SPEC — 02-04-ydt-temel-dikey · sahne 12-hyperframes-ozet (HyperFrames, 1080×1920, 463 kare)

Kaynak: `projeler/02-04-ydt-temel-dikey/BRIEF-DIKEY.md` §0, §2 + §3 satır 12. Yazan: şef (15.11.2026). Kod yazmaz; tasarım verir.
K = `/home/sef/01dev/_worktrees/kalem-0204`. Sahne dizini: `K/projeler/02-04-ydt-temel-dikey/sahneler/12-hyperframes-ozet/` (= D).
Sahne: küresel 205,30–220,33 sn, 463 kare, `t_bas` 205,30, `sure` = 463/30 = 15,4333. Cümle 14 (öğretmen, Türkçe).

## 1. Yazılacak dosyalar

| Dosya | Durum | İş |
|---|---|---|
| `D/yardim.py` | VAR (dikey 01 kopyası, bayt bayt aynı) | YALNIZ `kunye_svg()` değişir (§3). Başka işleve dokunma |
| `D/uret.py` | YOK | §4'e göre yaz |
| `D/olay.py` | VAR (dikey 01 kopyası) | DOKUNMA; `U.uret()` → `(s, _)` ve `U.Z["kare"]` ister |
| `D/calistir.sh` | VAR (şef uyarladı, KARE=463) | DOKUNMA |

Başka dosyaya dokunma. Silme yok. Test, render, git yok. `ortak/`, BRIEF, yatay paket, öteki sahneler salt okunur.

## 2. Kalıp kaynakları (salt oku)

| Kalıp | Mutlak yol | Ne alınır |
|---|---|---|
| Aynı içerik (yatay) | `K/projeler/02-04-ydt-temel/sahneler/12-hyperframes-ozet/uret.py` | İkon ızgara verisi AYNEN: `MONT`, `TISORT`, `EV`, `BAVUL`, `_kutu`, `TREN`, `_bilet`, `BILET`, `_kutusu`, `_daire_yolu`, `ikon_yollari` (IKON_EN/IKON_BOY bu SPEC'ten). `T(i, bas)` sözcük doğrulaması, `parca()`, `belirtec()`, `ok()`, `hap()` (kırpma ile açılan dolgulu hap), ikon çizim zamanlaması (`Y.cizgi_zamanlari`, `t1 = t0 + min(0.6, 0.25 + 0.05·n)`, ilk 2 yol ses olayı). Yatay bant/kart YERLEŞİMİ ALINMAZ |
| Dikey iskelet (aynı paket) | `K/projeler/02-04-ydt-temel-dikey/sahneler/01-hyperframes-giris/uret.py` | `PAKET`, `SAH`, `Z`, `SOZ` okuma; altyazı aç/kapa `s.set`; `__main__` (altyazı SVG `ek=` ile, `Y.html(...)` çağrısı); `uret()` 2 değer döndürür |
| Dikey tam HUD | `K/projeler/present-continuous-dikey/sahneler/06-hyperframes-form/yardim.py` `kunye_svg()` (satır 144–162) | `ku-ders` yazı + `ku-rz` rozet + `ku-bolum` çip kalıbı; 02-04 için ders 2 satır (§3) |
| HUD sayıları | `K/projeler/02-04-ydt-temel-dikey/ortak/kunye.js` `KUNYE`, `kunyeCiz` | logo 48,48 h96 · ders Fredoka 700 56, taban 212 ve 276 · rozet x = 48 + gen(satır 2) + 24, y 216, h 72, Lexend 700 36, yazı tabanı y 265 · çip y48 h80 |
| Tema dönüşümü | `K/projeler/present-continuous/ortak/hf_tema.py` | uret.py KOYU hex yazar (§5) |

## 3. `yardim.py` değişikliği (yalnız `kunye_svg`)

Yeni imza `kunye_svg(bolum)`. 03–14 HUD'u kare 0'dan tam çizer (BRIEF §2.2). Döner: `<g id="kunye">…</g>` içinde sırayla:
1. `<g id="ku-ders">`: iki `<text>`; x 48; tabanlar y 212 ve y 276; Fredoka 700 56; `fill=RENK["murekkep"]`; metinler
   `SIMPLE PRESENT vs` ve `PRESENT CONTINUOUS`.
2. `<g id="ku-rz">`: `rect` x = 48 + genislik("Fredoka", 700, "PRESENT CONTINUOUS", 56) + 24 (≈ 670), y 216,
   w = genislik("Lexend", 700, "YDT · BASIC", 36) + 56 (≈ 282), h 72, rx 36, `fill=RENK["vurgu"]`; `text` ortalı (rect ortası),
   y 265, Lexend 700 36, `fill=RENK["zemin"]` (hf_tema → pilMetin), metin `YDT · BASIC`.
3. `<g id="ku-bolum">` (gizli DEĞİL): çip, dikey 01'deki çizimin aynısı (cw = genislik(Lexend 700, bolum, 40) + 64, x = 1032 − cw,
   y 48, h 80, rx 40, `fill="none"`, stroke vurgu 4; yazı x = 1032 − cw/2, y 102, Lexend 700 40, fill vurgu).
ID yasağı: `t1`, `t2`, `rz1`, `ku-nokta` (hf_tema bunlara özel kural uygular). Docstring: "dikey tam HUD (sahne 03–14)".

## 4. `uret.py` (yeni)

### 4.1 Okuma ve zaman
- `PAKET = AD.parent.parent`; `zaman.json`'dan `klasor == AD.name` sahnesi. `Z = {t_bas, kare, sure}` (01 kalıbı).
- `SOZ` = `ortak/anlatim/sozcukler.json` içinde `cumle == 14` (29 sözcük). Zaman dosyadan okunur, sabit yazılmaz.
- `T(i, bas)`: i. sözcüğün `t0`'ı (küresel); `sozcuk.lower().startswith(bas.lower())` assert (yatay kalıp).
- `s = Y.Sahne(Z["t_bas"])`; bütün komut zamanları YEREL: `L = s.S` (küresel → yerel). `s.olay` yerel sn alır.

### 4.2 Sabitler (mantıksal px, `u()` ile; BRIEF-DIKEY ölçüleri)
| Ad | Değer | Not |
|---|---|---|
| KX, KW | u(48), u(984) | blok çerçevesi x 48–1032 (BRIEF §2.6) |
| IX | u(88) | blok içi yazı sol kenarı (iç boşluk 40) |
| SAG | u(992) | blok içi sağ sınır (assert) |
| BLOK | ((u(360), u(330)), (u(702), u(330)), (u(1044), u(210))) | (y0, yükseklik): blok 1, 2, 3 |
| TB, TF | u(64), u(64) | terim Caveat 700 64 · hap Fredoka 700 64 |
| R1, R2, R3 | u(70), u(180), u(288) | blok 1–2 satır tabanları (y0'dan): terim satırı a, terim satırı b, ok + hap satırı |
| R3A, R3B | u(74), u(170) | blok 3 satır tabanları (y0'dan) |
| IKON_EN, IKON_BOY, IKON_ARA | u(150), u(110), u(20) | ikon hücresi (sığdırma kutusu) 150×110; 3 hücre sağa yaslı: x 502–992 |
| IKON_UST | u(116) | ikon hücresi üstü (y0'dan); merkez y0 + 171 (QA turu 1: 112 → 116) |
| BEL_DY, BEL_W | max(0,28 em, kuyruk + 13) = 28 px, u(10) | belirteç (sözleşme satır 48; Caveat p kuyruğu 0,234 em). QA turu 1: 0,36 em → 28 px |
| AU, BO, HP, HY | u(84), u(24), u(14), 1.06 | ok uzunluğu, ok çevresi boşluk, hap yatay iç boşluk, hap yüksekliği × 64 (yatayla aynı oranlar) |
| MF_X, MF_Y, MF_B | u(88), u(1340), u(96) | `MEANING FIRST` Fredoka 700 96, sola hizalı, taban 1340 |
| MF_BEL_DY, MF_BEL_W | 0,28 em, u(12) | taban + 27 px (büyük harf, kuyruk yok) |
| GECIS_Y | u(1390) | geçiş çizgisi y; x 88–992 |
| Çizgi kalınlıkları | çerçeve u(4) `ikincil` alfa 0,85 · ok u(5) `murekkep` 0,9 · ikon u(4,0) `murekkep` / ince u(3,0) `ikincil` · geçiş u(4) `ikincil` 0,8 · belirteç alfa 0,85 | |

### 4.3 Yerleşim (1080×1920; HUD 0–320, içerik 352–1392, altyazı 1400–1536, platform 1536–1920 BOŞ)
```
y   48 ┌ [logo 387×96]                                  [ Recap ] ┐  çip x≈842–1032
   212 │ SIMPLE PRESENT vs                                         │  ders Fredoka 56
   276 │ PRESENT CONTINUOUS  [YDT · BASIC]                         │  rozet x≈670 y216 h72
   360 ├─ blok 1 çerçeve ────────────────────────────────────────┤
   430 │  general · permanent ·                     (taban 430)    │  Caveat 64, belirteç taban+23
   540 │  timetable                [mont] [ev] [tren] (ikon 472–582)│  ikon hücreleri x 502–992
   648 │  ──→ [ V1 / V-s ]                          (taban 648)    │  ok 88–172, hap rect 182–444
   690 ├──────────────────────────────────────────────────────────┤
   702 ├─ blok 2: right now · temporary · / arrangement [tişört][bavul][bilet] / ──→ [ am / is / are + V-ing ]
  1032 ├──────────────────────────────────────────────────────────┤  hap rect 182–783
  1044 ├─ blok 3 çerçeve ────────────────────────────────────────┤
  1118 │  time word · Turkish -yor  ──→ [ clue ]     (taban 1118)  │  ok 637–721, hap 731–881
  1214 │  MEANING  ──→ [ decision ]                  (taban 1214)  │  ok 363–447, hap 457–720
  1254 ├──────────────────────────────────────────────────────────┤
  1340 │  MEANING FIRST  (Fredoka 96, x 88–788) + sarı belirteç y 1367
  1390 │  ─────────── geçiş çizgisi (x 88–992) ───────────          │
  1400 │  altyazı: cümle 14 dilimi (Lexend 500 44, ≤ 2 satır)        │
  1536 └ PLATFORM: hiçbir öğe yok                                    ┘
```
Satır içi x: terimler `IX`'ten başlar, aralarında `gen(" ")`; `· ` öneki terimin parçasıdır, belirteç yalnız sözcüğün altına
(`x + gen("· ")` → sağ uç). Blok 1–2 satır b'de üçüncü terim solda, ikon hücreleri sağa yaslı (502–992). Satır 3: ok `IX` → `IX+AU`
(y = taban − 15), hap yazısı `IX + AU + BO`. Blok 3 satır a: ok `xe + BO` → `+AU`, hap yazısı `xe + BO + AU + BO`; satır b aynı kalıp.
Ölçülen genişlikler (fontTools, bilgi için): general·permanent· 464 · right now·temporary· 505 · time word·Turkish -yor 525 ·
V1 / V-s 234 · am / is / are + V-ing 573 · clue 123 · decision 235 · MEANING (Caveat 64) 251 · MEANING FIRST (96) 700.

### 4.4 Olay listesi (cümle 14; yerel = küresel − 205,30; kare = yerel × 30)
| # | Olay | Küresel sn (kare) | Sözcük (i) | Ses olayı |
|---|---|---|---|---|
| 1 | cümle 13 son altyazı dilimi kare 0'dan görünür, 205,73'te kapanır (§4.6) | 205,30–205,73 | — | — |
| 2 | çip `Recap` nabzı: `#ku-bolum` ölçek 1 → 1,08 (0,18 sn `power2.out`) → 1 (0,22 sn `power2.inOut`), svgOrigin çip ortası | T(0)=205,85 (16) | Özet. (0) | `tik` 0,4 |
| 3 | blok 1 çerçevesi (el kutusu) | T(1) − 0,30 = 206,59, 0,5 sn | Genel (1) | `cizgi` 0,45 |
| 4 | `general` (satır a) + belirteç (+0,10) | 206,89 (48) | Genel (1) | `tik` 0,5 |
| 5 | mont ikonu (hücre 1) | T(2)=207,29 | durum, (2) | `cizgi` |
| 6 | `· permanent` + belirteç; ev ikonu (+0,20) | T(3)=207,85 | kalıcı (3) | `tik` |
| 7 | `timetable` (satır b, IX) + belirteç; tren ikonu (+0,20) | T(6)=208,89 | tarifeli (6) | `tik` |
| 8 | kalem oku (satır 3) + hap `V1 / V-s` (+0,14) | T(8)=210,17 | geniş (8) | `cizgi` + `tik` 0,55 |
| 9 | blok 2 çerçevesi | T(10) − 0,30 = 210,99 | Konuşma (10) | `cizgi` 0,45 |
| 10 | blok 1 belirteçleri söner: `b1a b1b b1c` → `attr stroke = ikincil`, opaklık 0,6 (`s.set`, anlık) | T(10) + 0,10 = 211,39 | — | — |
| 11 | `right now` + belirteç | T(10)=211,29 (180) | Konuşma (10) | `tik` |
| 12 | tişört ikonu | T(11)=211,77 | anı, (11) | `cizgi` |
| 13 | `· temporary` + belirteç; bavul ikonu (+0,20) | T(12)=212,41 | geçici (12) | `tik` |
| 14 | `arrangement` (satır b) + belirteç; bilet ikonu (+0,20) | T(15)=213,37 | planlanmış (15) | `tik` |
| 15 | kalem oku + hap `am / is / are + V-ing` (+0,14, 0,5 sn) | T(17)=214,77 | şimdiki (17) | `cizgi` + `tik` |
| 16 | blok 3 çerçevesi | T(19) − 0,30 = 215,71 | Zaman (19) | `cizgi` 0,45 |
| 17 | blok 2 belirteçleri söner (`b2a b2b b2c`, olay 10 gibi) | T(19) + 0,10 = 216,11 | — | — |
| 18 | `time word` + belirteç | T(19)=216,01 | Zaman (19) | `tik` |
| 19 | `· Turkish -yor` + belirteç | T(22)=217,21 | Türkçe (22) | `tik` |
| 20 | kalem oku (0,25) + hap `clue` (+0,12, 0,3) | T(24)=217,93 | ipucu (24) | `cizgi` + `tik` |
| 21 | `MEANING FIRST` (alt, kırpma 0,40 sn) | T(26)=218,97 | Kararı (26) | `tik` 0,55 |
| 22 | MEANING FIRST belirteci: başlar T(26)+0,10, biter T(27) | 219,07–219,45 | anlam (27) | `cizgi` 0,5 |
| 23 | `MEANING` (blok 3 satır b, 0,35) | T(27)=219,45 | anlam (27) | `tik` |
| 24 | kalem oku (0,25) + hap `decision` (+0,10, 0,3 → 220,25) | T(28)=219,85 | verir. (28) | `cizgi` + `tik` |
| 25 | geçiş çizgisi (0,42 sn) | T(28)+0,02 = 219,87–220,29 | verir. (28) | `cizgi` 0,4 |
| 26 | durgun; son 12 kare | 220,33'e kadar | — | — |

Yazı açılışı: `s.yazi(kim, x, taban, [(m, renk)], aile, 700, boy, L(t), d, tur="tik", guc=0.5)` (kırpma soldan). Süreler: terim 0,35–0,45
(uzunluğa göre, yatay kalıp), belirteç 0,40, ok 0,30 (blok 3'te 0,25), hap 0,35 (uzun hap 0,50, blok 3'te 0,30).
Aynı anda en çok 3 sarı belirteç (BRIEF §0): olay 10 ve 17 bunu sağlar. Söndürme `s.set("#b1a", L(t), {"attr": {"stroke": IKN}, "opacity": 0.6})`.
`Y.kontrol(s, Z["kare"])` (ilk=True): ilk hareket ≥ 0,4 yerel (olay 2: 0,55), son bitiş ≤ (463 − 12)/30 = 15,033 yerel (olay 25: 14,99).

### 4.5 Ekran metni ve renk (KOYU hex yaz; hf_tema temaya çevirir)
| Öğe | Metin | Yazı | Renk |
|---|---|---|---|
| blok 1 terimleri | `general` · `· permanent ·` · `timetable` | Caveat 700 64 | murekkep |
| blok 2 terimleri | `right now` · `· temporary ·` · `arrangement` | Caveat 700 64 | murekkep |
| blok 3 | `time word` · `· Turkish -yor` · `MEANING` | Caveat 700 64 | murekkep |
| haplar | `V1 / V-s` · `am / is / are + V-ing` · `clue` · `decision` | Fredoka 700 64 | rect `vurgu` (→ vurguDolgu), yazı `zemin` hex (→ pilMetin) |
| alt | `MEANING FIRST` | Fredoka 700 96 | murekkep |
| belirteç | — | yol | `vurgu` (sönünce `ikincil`) |
| çerçeve, geçiş, ikon ince yolları | — | yol | `ikincil` |
| ok, ikon ana yolları | — | yol | `murekkep` |
| HUD | ders · rozet · `Recap` | §3 | §3 |
Tek vurgu sarı. Kırmızı, yeşil, emoji, gradyan, gölge YOK. Her satır ≤ 24 karakter (assert).

### 4.6 Altyazı
- `dil = Y.altyazi_dilimleri([13, 14])` → `[(t0, t1, metin)]` (küresel). Her dilim: `goster = t0 − 0,05`;
  `gizle = min(t1 + 0,35, sonraki dilimin goster'i)` (son dilimde `t1 + 0,35`). Aynı anda TEK dilim görünür.
- Sahneye giren dilimler: `gizle > t_bas` ve `goster < t_bas + sure`. Bunlar sırayla `alt0, alt1, …`.
- `s.set("#alt%d", max(0, L(goster)), {"opacity": 1})`; `L(gizle) < sure` ise `s.set(..., L(gizle), {"opacity": 0})`.
- Beklenen: alt0 = cümle 13 son dilimi (kare 0 → 205,73), sonra cümle 14 dilimleri (205,80 →); son dilim sahne sonuna kadar.
- `__main__`: aynı listeden `Y.altyazi_svg([{"id": "alt%d" % i, "metin": m} …])` → `ek=`. Karaoke bantta YOK (01 ve kunye.js ile aynı).

### 4.7 Kurallar ve assert'ler (uret.py içinde; ihlalde dur)
- ID'ler: çerçeve `kf0–kf2` · terim `m1a m1b m1c m2a m2b m2c m3a m3b m3c` · belirteç `b1a … b3b`, `bmf` · ok `o1–o4` · hap `h1–h4` ·
  ikon `ki{blok}_{n}_{j}` · alt `mf` · geçiş `gc` · altyazı `alt{i}`. `t1`, `t2`, `rz1`, `ku-nokta` YASAK.
- Assert: her terim/hap/ikon sağ ucu ≤ SAG (992); her satır metni ≤ 24 karakter; blok 1–2 satır a belirteç alt kenarı + u(10) ≤
  ikon hücresi üstü; blok 1–2 hap rect üstü − ikon hücresi altı ≥ u(10); blok 3 satır b hap rect üstü − satır a belirteç alt kenarı
  ≥ u(10); her blok çerçevesi 352 ≤ y0 ve y0 + h ≤ alt öğenin üstü; MEANING FIRST üstü (taban − 0,69·96) ≥ blok 3 altı + u(12);
  MF belirteç alt kenarı + u(10) ≤ GECIS_Y − u(2); GECIS_Y + u(2) ≤ 1392; `T()` sözcük doğrulamaları (yatay kalıptaki 17 sözcük).
- `uret()` tam 2 değer döndürür: `(s, Y.kunye_svg("Recap"))`. Altyazı `s.set` komutları `uret()` içinde.
- `__main__`: `proje/index.html` yaz: `Y.html(s, Z["sure"], kun, None, (48, 48, round(96 * Y.LOGO_EN_BOY, 2), 96), ek=altyazi)`;
  komut/olay sayısını, hareket aralığını ve olay listesini (küresel sn, yerel, kare, sözcük, olay) bas.
- Python: girinti 4 boşluk (kalıpla uyum), satır ≤ 140, sabit px yerine `u()`. `/usr/bin/python3 uret.py` ile koşar (`-I` değil:
  fontTools kullanıcı site-packages'ta).

## 5. Tema notu
uret.py koyu hex yazar. `calistir.sh` → `tema_hf` `#root`a CSS değişkenleri ekler: `#f3efe6` → murekkep, `#c9c2b3` → ikincil,
`#f2a93b` → vurgu (`rect`/`circle` dolgusu → vurguDolgu), `text[fill="#1b1a17"]` → pilMetin. Seçiciler öznitelik tabanlı:
`attr stroke` değişimi (olay 10, 17) tema rengini kendiliğinden alır.

## 6. Kabul ölçütü
1. `cd D && /usr/bin/python3 uret.py && /usr/bin/python3 olay.py` çıkış 0; assert yok; olayların hepsi kare < 451.
2. `proje/index.html`: `data-width="1080" data-height="1920"`; `#kunye` içinde `ku-ders`, `ku-rz`, `ku-bolum`; `#logoimg`; `alt0…`.
3. `cd K && bash araclar/qa-yerel.sh 02-04-ydt-temel-dikey 12-hyperframes-ozet 210.70,215.40,220.32 220.32 --hazirla` çıkış 0 (şef koşar).
4. Kareler: taşma, kesik yazı, üst üste binme, okunmaz kontrast, boş kare, platform bandında öğe YOK; altyazı bandında metin.
