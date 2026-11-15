# SPEC — 02-04-ydt-temel-s3 · sahne 02-hyperframes-ornek (HyperFrames, DİKEY 1080×1920) · 15.11.2026

Şef tasarımı. Uygulayıcı (agy) YALNIZ şu dosyayı yazar:
`/home/sef/01dev/_worktrees/kalem-0204/projeler/02-04-ydt-temel-s3/sahneler/02-hyperframes-ornek/uret.py`
Başka dosyaya dokunma. Silme yok. Test, render, git yok. `uret.py`'yi koşma (şef koşar).
Aynı dizindeki `yardim.py`, `olay.py`, `calistir.sh`, `nesneler.json`, `cizim/ogretmen.json` HAZIR; değiştirme.

## 1. Kalıp kaynakları (salt oku)

| Kalıp | Mutlak yol | Ne alınır |
|---|---|---|
| Ana iskelet (aynı motor, dikey, aynı soru anı) | `/home/sef/01dev/_worktrees/kalem-0204/projeler/02-04-ydt-temel-dikey/sahneler/06-hyperframes-soru1/uret.py` | BÜTÜN yapı: okuma bloğu (`PAKET`, `SAH`, `Z`, `TB`), `g()`, `statik()`, `metin()`, `soldur()`, `kunye_tam()` (satır 247–268), öğrenci başı (satır 329–346: regex, `basm > basn > bas`, 3 yol kalemle), `balon_sol` çağrısı, `s.yazi` ile sözcük sözcük yazım, sarı nokta `nk` + bağ `cn` + `ok_basi` (satır 377–391), ikiz yol kalıbı (`ok_fig` + `ok_fig_s`, `krm` + `krm_s`, `soldur`), altyazı aç/kapa (satır 556–566), `__main__` (satır 577–593: `Y.kontrol`, logo demeti, `Y.html(..., ek=alt, bal_ids=..., gruplar=...)`) |
| Kalem geometrisi (birebir Python'a taşı) | `/home/sef/01dev/_worktrees/kalem-0204/projeler/02-04-ydt-temel-s3/ortak/kalem-canvas.js` satır 40 (`lerp`), 48–56 (`hash`, `gurul`), 254–263 (`elips`), 279–291 (`kutu`) | §3.2 |
| Tren ve bilet parça listesi | `/home/sef/01dev/_worktrees/kalem-0204/projeler/02-04-ydt-temel/sahneler/05-canvas-ornek3/sahne.js` satır 81–103 (`trenParcalari`), 118–142 (`biletParcalari`) | §3.3 |
| Sahne 01 son karesi (= bu sahnenin kare 0'ı) | `/home/sef/01dev/_worktrees/kalem-0204/projeler/02-04-ydt-temel-s3/sahneler/01-hyperframes-kapak/SPEC.md` §3.2, §3.3 tablosu (tren satırı), §3.4 (`KART`, `R1_SON`, `R2_SON`, `TREN_SON`) | kart 1, satırlar, tren aynı geometri |

Örnekten ALINMAYACAK: içerik (`TIMETABLE`, `ARRANGEMENT`, zincirler, `V-ing` hapı, uçak/kitap simgesi, baş sallama, `-ing` altı `bm8`,
`The train` altı `ktm`), örneğin yerleşim sayıları, örneğin `Question` çipi.

## 2. Zaman (tek kaynak; sabit saniye YAZMA)

- `SAH` = `PAKET/"zaman.json"` → `sahneler[]` içinde `klasor == AD.name` (t_bas 3,00 · kare 402). `Z = {"t_bas", "kare", "sure": round(kare/30, 4)}`.
  `TB = Z["t_bas"]`; yerel sn = `s.S(küresel)`.
- `SOZ` = `PAKET/"ortak/anlatim/sozcukler.json"` (54 öğe, düz liste). `T(i, bas)` = `SOZ[i]["t0"]` (küresel), `E(i, bas)` = `t1`; ikisi de
  `assert SOZ[i]["sozcuk"] == bas` (eşleşmezse dur). Modül başında 7–35 dizinlerinin tamamını bu listeyle doğrula:
  7 `p.m.` 3,00 · 8 `today.` 3,40 (t1 4,20) · 9 `I` 4,45 · 10 `am` 4,61 · 11 `going` 4,81 · 12 `to` 4,97 · 13 `the` 5,09 · 14 `movie` 5,29 ·
  15 `theater` 5,49 · 16 `tonight.` 5,93 (t1 6,53) · 17 `Hocam,` 7,00 · 18 `tren` · 19 `de` · 20 `plana` · 21 `göre` · 22 `kalkmıyor` · 23 `mu?` ·
  24 `Neden` 9,72 · 25 `-ing` · 26 `yok?` (t1 10,84) · 27 `Planı` 11,51 · 28 `bir` 12,07 · 29 `kişi` 12,31 · 30 `yapar.` 12,51 · 31 `Tren` 13,43 ·
  32 `tarifeye` 13,83 · 33 `uyar:` · 34 `geniş` 15,19 · 35 `zaman.` (t1 16,07).
- `f0(t) = max(0.40, s.S(t))`: ilk 12 kare (yerel < 0,40) geçiş altında, hareket yok. `Y.kontrol(s, Z["kare"])` hareketi [0,40, 13,00] içinde ister.
- `EKRAN = {"Izmir": "İzmir", "seven": "7", "p.m.": "pm"}`: altyazı diliminin metni boşlukla bölünür, her sözcük `EKRAN.get(w, w)` ile çevrilir
  (ekranda noktalı İ ve `7 pm`; ses değişmez). Kart ve etiketlerde ham `Izmir` / `seven` / `p.m.` YOK.

## 3. Çizim katmanı

### 3.1 Renk ve yazı
- Yalnız `Y.RENK` koyu değerleri: `KRE = murekkep`, `IKN = ikincil`, `SAR = vurgu`, `ZEM = zemin`. Tema çevirisini `calistir.sh` (`hf_tema.py`) yapar;
  açık tema hex'i (`#ffe066`, `#1b2440`, `#f7f3ea`) YAZMA. Kırmızı, yeşil, gradyan, gölge, emoji YOK. `id="t2"`, `id="rz1"`, `id="ku-nokta"` YOK.
- Kart yazısı Fredoka 700 64 · balon yazısı Fredoka 600 64 · etiket Caveat 700 64 · künye/altyazı `yardim.py` HUD ölçüsü (istisna).
- Her `s.svg` öğesinin ilk özniteliği `id="…"` (html() kimliği oradan okur). Kimlikler tekil.
- Aynı anda tek sarı (SAR) öğe kümesi: §4'teki `soldur` adımları bunu sağlar (sarı yol → ikiz `IKN` yol).

### 3.2 Kalem geometrisi (kalem-canvas.js → Python, birebir; sahne 01 ile aynı çıktı)
- `_imul(a, b) = ((a & 0xFFFFFFFF) * (b & 0xFFFFFFFF)) & 0xFFFFFFFF`.
- `hash(a, b=0, c=0) -> float`: `h = (_imul(a, 374761393) + _imul(b, 668265263) + _imul(c, 1274126177)) & 0xFFFFFFFF`;
  `h = _imul(h ^ (h >> 13), 1274126177)`; `h ^= h >> 16`; dönüş `h / 4294967296`.
- `lerp(a, b, t) = a + (b − a)·t`; `gurul(x, s)`: `i = floor(x)`, `f = x − i`, `u = f²(3 − 2f)`; `lerp(hash(i, s, 7), hash(i + 1, s, 7), u) − 0.5`.
- `elips(cx, cy, rx, ry, egim=0, tohum=1) -> list[(x, y)]` ve `kutu(x, y, w, h, tohum=1) -> list[[a, m, b]]`: JS satır 254–263 ve 279–291 formülü.
- SVG yolu: kutu kenarı `[a, m, b]` → `"M ax ay Q mx my bx by"`; öbür nokta dizileri → `"M p0 L p1 L …"`. Sayılar 2 ondalık.

### 3.3 Çizimler
| Öğe | Geometri | Kalınlık · renk |
|---|---|---|
| Kart 1 çerçevesi `kc0…kc3` (statik, kare 0'da görünür) | `kutu(57, 368, 966, 260, 71)`, 4 kenar ayrı yol | 4 · KRE, round cap, `fill="none"` |
| Tren `g#tren` (statik) | sahne 01 §3.3 tren satırı / sahne 05 `trenParcalari(0, 0)` listesinin aynısı (kutu tohumları 31–37, tekerlek `elips(x,138,17,17,0,50+i)`, ray, duman `elips(…,61)`, `elips(…,62)`); grup `transform="translate(790 404) scale(0.5)"` → ekranda kutu [785, 392]–[1000, 483] | gövde 4,5 · ince 3,6 · ray 4 · duman 3,4 / 3,2; gövde/ince KRE, ray/duman IKN; her yolda `vector-effect="non-scaling-stroke"` |
| Kart 2 çerçevesi `kd0…kd3` | `kutu(57, 860, 966, 260, 72)` (A konumu) | 4 · KRE |
| Bilet `bl0…` (kart 2 sağ üst köşesi) | `biletParcalari` noktaları: P(x, y) = (BCX + BS·(x·cos e − y·sin e), BCY + BS·(x·sin e + y·cos e)), BS 0,55, e −0,06, BCX 900, BCY 926 (A konumu); 4 kenar (sağ/sol kenarda 13 noktalı çentik yayı, yarıçap 22), 6 delik çizgisi (x 100, y0 = −58 + 20i, boy 11), 3 baskı satırı | kenar 4,5 KRE · delik 3,4 IKN · baskı 4 IKN |
| Öğrenci başı `basm > basn > bas` | örnek satır 329–340 kalıbı; `BS0 = 240/330`, `BTX = 72 + 45·BS0`, `BTY = 1090` | 4 · KRE |
| Öğretmen `g#fig` | `cizim/ogretmen.json` (`kutu` [x0, y0, x1, y1], `el` [x, y], `yollar` [{parca, d}] 3 yol): `fs = 380/(y1 − y0)`, `transform="translate(72 − x0·fs, 1010 − y0·fs) scale(fs)"`, yollar `fg0…fg2`; el ekranda `HX = 72 + (el.x − x0)·fs`, `HY = 1010 + (el.y − y0)·fs` | ekranda gövde 4,4 · saç 3,6 · yüz 2,6 (`stroke-width = w / fs`), KRE |

## 4. Olay listesi (yerel sn = `s.S(küresel)`; hepsi sözcük çapasından)

Kısaltmalar: `yazi` = `s.yazi(id, x, taban, [(m, KRE)], aile, ağırlık, 64, t, süre)` · `yol` = `s.yol(id, d, t, süre, renk, w, ...)` ·
`sol(a, b, t)` = örnekteki `soldur` (0,25 sn).

| # | Olay | Başlangıç (çapa) | Yerel | Ayrıntı |
|---|---|---|---|---|
| 0 | Kare 0 = sahne 01 son karesi (statik) | — | 0 | `kc0…kc3`, `g#tren`, `metin("r1", 97, 468, "The train to İzmir")`, `metin("r2", 97, 566, "leaves at 7")` (Fredoka 700 64, KRE), künye, logo, altyazı dilimi 0 açık |
| 1 | `pm` yazımı | `f0(T(7,"p.m."))` | 0,40 | `yazi("w7", 97 + g("leaves at 7 "), 566, "pm", Fredoka 700, t, 0.12)`, tik 0,4 |
| 2 | `today.` yazımı | `max(f0(T(8)), olay1 + 0.12)` | 0,52 | x `97 + g("leaves at 7 pm ")`, taban 566 |
| 3 | Zaman çizgisi ekseni (çizgi + ok ucu) | olay 2 | 0,52 | `yol("tx", Y.el_ok(72, 748, 1008, 748, 0.5), t, 0.30, IKN, 4.5)` |
| 4 | now noktası + `now` | olay 2 + 0,08 | 0,60 | `<circle id="tn_now" cx="150" cy="748" r="11" fill=KRE style="opacity:0">` + `s.fromto` opaklık 0→1 0,2 sn; `yazi("tl_now", 150 − g("now",64,700,"Caveat")/2, 708, "now", Caveat 700, t, 0.2)` |
| 5 | `7 pm` çentiği + nokta + `7 pm` | olay 2 + 0,20 | 0,72 | `yol("t7c", "M 400 730 L 400 766", t, 0.12, KRE, 4.5)`; `<circle id="tn_7" cx="400" cy="748" r="9">` aynı opaklık kalıbı; `yazi("tl_7", 400 − g("7 pm")/2, 708, "7 pm", Caveat, t + 0.04, 0.2)` |
| 6 | now → `7 pm` kalem oku (yay) | olay 2 + 0,28 | 0,80 | `yol("tok", "M 168 736 Q 277 696 388 738" + ok ucu, t, 0.35, KRE, 4.5)`; ok ucu: a = atan2(738 − 696, 388 − 277), k 18, uç noktaları (388 − k·cos(a ∓ 0.5), 738 − k·sin(a ∓ 0.5)) — `Y.el_ok` ucu ile aynı biçim |
| 7 | `7 pm` sarı daire (`isaret`) | olay 2 + 0,58 | 1,10 | `yol("t7d", Y.el_daire(400, 688, 80, 38, 0.6), t, 0.30, SAR, 6)`, cizgi 0,5 |
| 8 | `gelecek · V-s` (7 pm altında) | olay 2 + 0,63 | 1,15 | `yazi("tg1", 400 − g(m,64,700,"Caveat")/2, 824, "gelecek · V-s", Caveat, t, 0.30)` |
| 9 | Kart 2 çerçevesi (4 kenar sırayla, süre kenar boyuyla orantılı) | `s.S(T(9,"I")) − 0.30` | 1,15 | `Y.cizgi_zamanlari([966, 260, 966, 260], t, t + 0.30)`; kimlik `kd0…kd3` |
| 10 | Kart 2 satır 1 sözcük sözcük (`I` `am` `going` `to` `the`) | her sözcüğün `T(i)` | 1,45–2,09 | taban 960; x = 97 + g(satırın o sözcüğe kadarki öneki + boşluk); kimlik `w9…w13`, süre 0,12; ses yalnız `I`'da tik 0,35 |
| 11 | Bilet kalemle (parçalar sırayla, uzunluk orantılı) | `s.S(T(14,"movie"))` | 2,29 | toplam 0,45 sn; kimlik `bl0…`; ses ilk parçada cizgi 0,45 |
| 12 | Kart 2 satır 2 (`movie` `theater` `tonight.`) | her sözcüğün `T(i)` | 2,29–2,93 | taban 1058; kimlik `w14…w16`; ses yalnız `movie`'de tik 0,35 |
| 13 | tonight noktası + `tonight` + `gelecek · am + V-ing` | `s.S(T(16,"tonight."))` | 2,93 | `<circle id="tn_t" cx="790" cy="748" r="11">` opaklık kalıbı; `yazi("tl_t", 790 − g("tonight")/2, 708, …, t + 0.05, 0.2)`; `yazi("tg2", 790 − g(m)/2, 824, "gelecek · am + V-ing", Caveat, t + 0.17, 0.30)`, tik 0,45 |
| 14 | Zaman çizgisi grubu söner (öğrenciden önceki sessizlikte) | `s.S(T(17,"Hocam,")) − 0.50` | 3,50 | `s.to("#zc", t, {opacity 0, 0.25, power2.in})` |
| 15 | Kart 2 yukarı (kartlar üstte toplanır) | `s.S(T(17)) − 0.42` | 3,58 | `s.to("#k2", t, {y: −124, 0.42, power3.inOut})` → kart 2 736–996 (B/C konumu) |
| 16 | Öğrenci başı 3 yol | `s.S(T(17)) − 0.10` (+0,05 ara) | 3,90 | süre 0,32; cizgi 0,55 |
| 17 | Balon | `s.S(T(17)) − 0.05` | 3,95 | `yol("bal", Y.balon_sol(300, 1040, 996, 1340, 252, 1290), t, 0.55, KRE, 4.5)`, cizgi 0,7 |
| 18 | Balon sözcükleri | her sözcüğün `T(i)` (17–26) | 4,00–7,33 | Fredoka 600 64; satır 1 = 17–20, satır 2 = 21–23, satır 3 = 24–26; tabanlar 1124 / 1208 / 1292; x başı 340, ara `g(" ", 64, 600)`; kimlik `bw17…bw26`; süre 0,12; ses her satırın ilk sözcüğünde tik 0,4; `assert` satır sağ ucu ≤ 956 |
| 19 | Sarı nokta (balon üstü) | `s.S(T(24,"Neden"))` | 6,72 | `yol("nk", "M 768 1036 L 768.1 1036", t, 0.12, SAR, 18)`, tik 0,45 |
| 20 | Bağ: balon → kart 1 `leaves` | olay 19 + 0,14 | 6,86 | `yol("cn", f"M 768 1036 L 768 620 Q 768 604 752 604 L {XU1} 604 {ok1}", t, 0.45, SAR, 6, alfa 0.9)`; `XU1 = 97 + 0.75·g("leaves")`; `ok1 = f"M {XU1+19} 593.5 L {XU1} 604 L {XU1+19} 614.5"` |
| — | DURAKLAMA (öğrenci sustu): olay yok | 10,76–11,51 | 7,76–8,51 | balon durur |
| 21 | Balon grubu söner (baş dahil) | `s.S(T(27,"Planı"))` | 8,51 | `s.to("#balg", t, {opacity 0, 0.35, power2.in})`, vurus 0,5 |
| 22 | Öğretmen kalemle (3 yol sırayla, `Y.yol_uzunluk` orantılı) | olay 21 + 0,04 | 8,55 | `Y.cizgi_zamanlari(uzunluklar, t, t + 0.50)`; `s.cmd` draw kalıbı (örnekteki baş gibi); ses ilk yolda cizgi 0,5 |
| 23 | Bağ: öğretmenin eli → `am going` (sarı ok) + ikiz | `s.S(T(28,"bir"))` | 9,07 | `d = Y.el_ok(HX + 10, HY − 14, XG + WG/2, 1010, 2.0)`; `yol("ok_fig", d, t, 0.40, SAR, 8)` + `yol("ok_fig_s", d, t, 0.40, IKN, 8, alfa 0.0, tur=None)`; `XG = 97 + g("I ")`, `WG = g("am going")` |
| 24 | `am going` odak (sarı altçizgi) + ikiz | olay 23 + 0,40 | 9,47 | `d = Y.el_cizgi(XG − 2, 867, XG + WG + 2, 867, 1)` (taban 836 + 0,48·64); `yol("krm", d, t, 0.30, SAR, 10)` + `yol("krm_s", d, t, 0.30, IKN, 10, alfa 0.0, tur=None)` |
| 25 | `person` | `s.S(T(29,"kişi"))` | 9,31 | `yazi("lp0", 300, 1080, "person", Caveat, t, 0.30)`, tik 0,4 |
| 26 | etiket oku + `plan` | `s.S(T(30,"yapar."))` | 9,51 | `xa = 300 + g("person") + 16`; `yol("lpo", Y.el_ok(xa, 1058, xa + 56, 1058, 0.5), t, 0.20, KRE, 4.5)`; `yazi("lp1", xa + 72, 1080, "plan", Caveat, t + 0.15, 0.30)` |
| 27 | Önceki sarı griye döner | `s.S(T(31,"Tren"))` | 10,43 | `sol("ok_fig", "ok_fig_s", t)`; `sol("krm", "krm_s", t)` |
| 28 | Bağ: tren → `leaves` (sarı) + ikiz | olay 27 | 10,43 | `d = f"M 892.5 492 L 892.5 588 Q 892.5 604 876.5 604 L {XU1} 604 {ok1}"`; `yol("ok_trn", d, t, 0.60, SAR, 8)` + `yol("ok_trn_s", d, t, 0.60, IKN, 8, alfa 0.0, tur=None)` |
| 29 | `train` (kart 1 altında) | olay 27 + 0,10 | 10,53 | `yazi("lt0", 97, 694, "train", Caveat, t, 0.30)`, tik 0,4 |
| 30 | etiket oku + `timetable` | `s.S(T(32,"tarifeye"))` | 10,83 | `xb = 97 + g("train") + 16`; `yol("lto", Y.el_ok(xb, 672, xb + 56, 672, 0.5), t, 0.20, KRE, 4.5)`; `yazi("lt1", xb + 72, 694, "timetable", Caveat, t + 0.15, 0.30)` |
| 31 | Tren bağı griye döner + `leaves` odak (sarı) | `s.S(T(34,"geniş"))` | 12,19 | `sol("ok_trn", "ok_trn_s", t)`; `yol("klm", Y.el_cizgi(95, 584, 97 + g("leaves") + 2, 584, 1), t, 0.30, SAR, 10)`, cizgi 0,5 |

Hareket 12,49 yerel'de biter. 12,49–13,40 durgun (son 12 kare 390–401 geçiş altında). Tablodaki "Yerel" sütunu yalnız denetim içindir;
kodda her zaman çapa ifadesi kullanılır.

Altyazı (örnek satır 556–566 kalıbı): `dilimler = Y.altyazi_dilimleri([1, 2, 3])`; her dilimin metni `EKRAN` ile çevrilir; aç = `max(0, s.S(t0) − 0.05)`,
kapa = `min(s.S(t1) + 0.35, s.S(sonraki t0) − 0.05)` (son dilim kapanmaz); kapa ≤ 0 olan dilim atlanır. `Y.altyazi_svg([{"id": f"alt{i}", "metin": …}])`.

Künye: örnekteki `kunye_tam()`; çip metni `CIP = "Example"` (`ortak/kunye.js` `KUNYE.cipler["02-hyperframes-ornek"]`). Logo `(48, 48, round(96·Y.LOGO_EN_BOY, 2), 96)`.

## 5. Gruplar (`Y.html(..., gruplar=[...])`)
- `bal_ids` (`#balg`): `basm`, `bal`, `bw17…bw26`, `nk`, `cn`.
- `("zc", {...})`: `tx`, `tn_now`, `tl_now`, `t7c`, `tn_7`, `tl_7`, `tok`, `t7d`, `tg1`, `tn_t`, `tl_t`, `tg2`.
- `("k2", {...})`: `kd0…kd3`, `w9…w16`, `bl0…`.
- `s.svg` ekleme sırası (alttan üste): kart 1 (`kc*`, `g#tren`, `r1`, `r2`, `w7`, `w8`) → zaman çizgisi → kart 2 → baş → balon ve sözcükler → `nk`, `cn` →
  öğretmen → `ok_fig*`, `krm*` → `lp*` → `ok_trn*` → `lt*` → `klm`.
- Kart 2 öğeleri A konumunda (kart y 860) yazılır; `#k2` grubu olay 15'te −124 kayar. Kart 2'ye bağlı sonraki sabitler (krm y 862, ok ucu 1010)
  B/C konumundadır (kart 2: 736–996, satır 1 tabanı 836).

## 6. Yerleşim özeti (px; tek sütun; kenar 48; içerik bandı 352–1392; altyazı 1400–1536; 1536 altı BOŞ)

```
 368 ┌ kart 1 (57–1023) ─────────── tren 785–1000 × 392–483 ┐   A, B, C
 468 │ The train to İzmir                                     │
 566 │ leaves at 7 pm today.          (584 klm · 604 bağ şeridi)│
 628 └───────────────────────────────────────────────────────┘
 694   A: 708 now · 7 pm (sarı daire) · tonight   748 eksen   824 gelecek · …    C: 694 train → timetable
 736   B/C: kart 2 (736–996; A'da 860–1120) · bilet 801–999 köşede · 836 / 934 satırlar · 867 krm
1040   B: balon 300–996 × 1040–1340 (1124 / 1208 / 1292), baş 72–247 × 1090–1330, bağ x 768 → 604
1010   C: öğretmen 72–190 × 1010–1390, el → ok ucu (XG + WG/2, 1010); 1080 person → plan (x 300)
1400 ─ altyazı (Lexend 44, ≤ 2 satır) ─ 1536 ─ BOŞ ─ 1920
```

## 7. Kurallar ve bekçiler (`assert`, sessiz geçiş yok)
- Ekran metni yalnız: kart satırları (`The train to İzmir`, `leaves at 7`, `pm`, `today.`, `I am going to the`, `movie theater tonight.`),
  `now`, `7 pm`, `tonight`, `gelecek · V-s`, `gelecek · am + V-ing`, balon sözcükleri, `person`, `plan`, `train`, `timetable`, künye, altyazı.
  `→` glifi YOK (yazı tiplerinde yok): ok `Y.el_ok` ile çizilir.
- `assert`: kart satırı sağ ucu ≤ 785 − 24 (satır 1) ve ≤ 1023 − 40 (satır 2); `gelecek · am + V-ing` sağ ucu ≤ 1032; iki alt etiket arası ≥ 24;
  balon satırı sağ ucu ≤ 956; `person → plan` ve `train → timetable` sağ ucu ≤ 760; öğretmen sağ ucu ≤ 290 ve altı ≤ 1392;
  `XU1 ≤ 97 + g("leaves")` (ok ucu `leaves`'in altında biter).
- Her yazı ve çizgi başlangıçta görünmez (`s.yazi` kırpma genişliği 0, `s.yol` opaklık 0) — kare 0 statik öğeleri hariç.
- Python: tip ipucu (yeni işlevlerde `-> …`), satır ≤ 120, girinti 4, sessiz `try/except` yok.
- `uret()` `(s, parca)` döndürür; modül düzeyinde `Z` olur (`olay.py` `U.uret()` ve `U.Z["kare"]` okur).

## 8. Kabul ölçütü (şef doğrular)
1. `cd <sahne> && /usr/bin/python3 uret.py` çıkış 0; `proje/index.html` yazılır; `Y.kontrol` geçer.
2. `/usr/bin/python3 olay.py` çıkış 0.
3. `index.html`: `data-width="1080"`, `data-height="1920"`, `data-duration="13.4"`, `id="kunye"`, `id="zc"`, `id="k2"`, `id="balg"`, `Example`,
   `İzmir`; `Izmir`, `seven`, `p.m.`, `→`, `#ffe066`, `#1b2440` YOK.
4. `bash araclar/qa-yerel.sh 02-04-ydt-temel-s3 02-hyperframes-ornek 6.6,10.9,15.9 13.5 --hazirla` → kapı çıkış kodu 0 (şef koşturur).
