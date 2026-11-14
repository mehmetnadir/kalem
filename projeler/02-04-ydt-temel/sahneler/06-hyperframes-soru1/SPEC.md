# SPEC — 02-04 sahne 06 `06-hyperframes-soru1` · uret.py (şef tasarımı, 14.11)

## 0. Görev

| Alan | Değer |
|---|---|
| Yazılacak TEK dosya | `/home/sef/01dev/_worktrees/kalem-0204/projeler/02-04-ydt-temel/sahneler/06-hyperframes-soru1/uret.py` |
| Dokunma | aynı dizindeki `yardim.py`, `olay.py`, `calistir.sh`, `SPEC.md`; `ortak/`, başka sahne, BRIEF, senaryo, ses. Silme yok. Test, render, git yok. `uret.py`'yi KOŞMA (proje/index.html yazar; şef koşar). |
| Örnek (kalıp) | `/home/sef/01dev/_worktrees/kalem-0204/projeler/02-03-ydt-temel/sahneler/06-hyperframes-soru1/uret.py` — dosya yapısı, `Sahne` kullanımı, balon + baş, `__main__` bloğu buradan. İçeriği değil, kalıbı al. |
| Yardımcı modül (hazır) | `…/06-hyperframes-soru1/yardim.py` (02-04 sürümü): `u()`, `RENK`, `genislik()`, `Sahne` (`S`, `olay`, `to`, `set`, `fromto`, `yol`, `yazi`, `figur`), `el_kutu`, `el_cizgi`, `el_ok`, `balon_sol`, `tabler`, `cizgi_zamanlari`, `AJANDA`, `kunye_svg(bolum, etkin)`, `html(...)`, `kontrol(s, kare)`, `ORTAK`, `LOGO_EN_BOY`. Örnek sahnenin `yardim.py`'sinden farkı: `u()` var, künye `kunye_svg(bolum, etkin)` (tek ajanda). |
| Çağıran | `olay.py`: `import uret as U; s, _ = U.uret(); U.Z["kare"]` → `uret()` `(s, parca)` döndürmeli, modül düzeyinde `Z` olmalı. `calistir.sh` `uret.py`'yi doğrudan koşar. |

## 1. Zaman (tek kaynak, sabit sayı yazma)

- `PAKET = AD.parent.parent`; `SAH` = `PAKET/zaman.json` içinde `klasor == AD.name` (t_bas 93,35 · kare 613 · süre 613/30).
- `Z = {"t_bas", "kare", "sure": round(kare/30, 4)}`; `TB = Z["t_bas"]`; yerel sn = `s.S(küresel)`.
- Sözcükler `PAKET/ortak/anlatim/sozcukler.json`: `S6` = cümle 6 (öğrenci), `S7` = cümle 7 (öğretmen).
- `assert` cümle 6 sözcükleri: `Hocam, tren de plana göre kalkmıyor mu? Neden -ing yok?` (10 sözcük, SORU listesi).
- `T6(i)` = `S6[i]["t0"]`; `T7(sozcuk, n=0)` = cümle 7'de sözcüğün n. geçişinin `t0`'ı (yoksa `assert`).
- İlk ve son 12 kare durgun: `__main__` içinde `Y.kontrol(s, Z["kare"])` çağır (ilk hareket ≥ 0,4 sn, son bitiş ≤ (613−12)/30).

## 2. Renk, yazı, kurallar

- Renk yalnız `Y.RENK`: `KRE = murekkep`, `IKN = ikincil`, `SAR = vurgu` (tek vurgu; temada sarı). Kırmızı YOK, yeşil YOK
  (bu sahnede şık yok), emoji YOK, gradyan/gölge YOK. Tema çevirisi `hf_tema.py` ile (calistir.sh yapar); renk hex'i yazma.
- Bütün ölçüler `u(n)` (mantıksal px, yatay 1920 tabanı). Çıplak sayı px yasak (yalnız oran/katsayı: 0.55 ölçek gibi).
- Yazı: Fredoka 700 (kart, zincir), Fredoka 600 (balon), Caveat 700 (etiket). En küçük yazı `u(44)` (taban 30'un üstü).
- Künye: `Y.kunye_svg("Question", Y.AJANDA.index("Examples"))`; logo `(u(56), u(1002), u(34)*Y.LOGO_EN_BOY, u(34))`.
- Sessiz catch yok (`try/except: pass` yazma). Python tip ipuçları (`-> tuple`, `: float`) kullan. Satır ≤ 120 karakter.
- Ekran metni yalnız senaryo sütunu: soru balonu metni, `person · plan · am / is / are + V-ing · train · timetable · V1 / V-s`,
  kartlarda sahne 05'in cümleleri ve `TIMETABLE` / `ARRANGEMENT` etiketi. Başka yazı ekleme.

## 3. Yerleşim (mantıksal px, hepsi `u()` ile)

| Öğe | Değer |
|---|---|
| Kartlar (ilk kareden statik) | sol x 100, sağ x 1010; y 118; w 810; h 300; iç pay 40; çerçeve `Y.el_kutu`, KRE, kalınlık 4,5 |
| Kart satırları (Fredoka 700, 48) | taban B1 = 200, B2 = 268. Sol: `The train to İzmir` / `leaves at 7 pm today.` · Sağ: `I am going to the` / `movie theater tonight.`; her satır için `assert genişlik ≤ 730` |
| Etiket (Caveat 700, 54) | taban 372, kartın sağ iç kenarına yaslı (`text-anchor="end"`, x = kart x + 810 − 40): sol `TIMETABLE`, sağ `ARRANGEMENT`; altında SAR el çizgisi (taban + 16, kalınlık 7, alfa 0,9), kimlik `klu` / `kru` |
| Sahne 05 odakları (statik) | `leaves` altı (sol 2. satır, taban+14) kimlik `klm`; `am going` altı (sağ 1. satır, x = kart iç + genişlik("I ")) kimlik `krm`; SAR, kalınlık 9, alfa 0,85, `Y.el_cizgi(..., 1)` |
| Öğrenci başı | `ortak/cizim/peeps-kit/ogrenci-bas.svg` 3 yolu (örnekteki regex); ölçek 0,55; translate (118, 790); DIŞ sarmal grup `<g id="basn">` içinde `<g id="bas" transform=…>`; baş yolları `bas0..2` (opaklık 0, kalemle çizilir) |
| Balon | `Y.balon_sol(BX0=300, BY0=660, x1b, BY0+190, BX0−62, BY0+212)`; x1b = BX0 + en geniş satır + 70 (`assert x1b < 1880`); Fredoka 600 44; satır 1 sözcük 0–6, satır 2 sözcük 7–9; tabanlar BY0+72, BY0+136; sözcük x başı BX0+35 |
| Sağ zincir | x 1040; tabanlar 560 / 650 / 740; Fredoka 700 44 |
| Sol zincir | x 140; aynı tabanlar |
| Figür | Open Peeps `standing-1` (`s.figur`), sol üst (1640, 470), yükseklik 470, çizgi 3,4; `assert x + genişlik ≤ 1864` |
| Tren | sol üst (515, 500), katsayı 0,85 (`u(0.85)`); ölçüler sahne 05 `trenParcalari` ile aynı (§5) |
| Uçak / kitap simgesi | Tabler `plane` ve `book`, kenar 84; sol üst (555, 660) ve (685, 660) |

## 4. Olay listesi (küresel sn = sözcük t0; yerel = `s.S(t)`)

| # | Olay | Zaman (küresel) | Cümle sözcüğü |
|---|---|---|---|
| 1 | baş 3 yolu kalemle (0,32 sn, 0,05 ara) | yerel 0,43 | — (ilk 12 kare durgun) |
| 2 | balon çizimi (0,55 sn) | T6(0) − 0,05 | 6 · Hocam, (93,90) |
| 3 | soru sözcükleri tek tek (`s.yazi`, 0,12 sn) | her sözcüğün t0 | 6 · 0–9 |
| 4 | sarı nokta (balon üstü, x BX0+110, y BY0−22; tek noktalı yol, kalınlık 18) + bağ çizgisi `Y.el_cizgi` noktadan `leaves` ortasının altına (y B2+34) | T6(1) ve +0,14 | 6 · tren (94,62) |
| 5 | `-ing` altı SAR (0,28 sn) | T6(8) | 6 · -ing (96,98) |
| — | DURAKLAMA: olay yok | 97,74–98,41 | — |
| 6 | `#balg` (balon, sözcükler, -ing altı, nokta, bağ) söner 0,4 sn; baş KALIR | T7("Planı") | 7 · Planı (98,41) |
| 7 | `kru` (ARRANGEMENT altı) kalınlık nabzı 7 → 12 → 7 | Planı + 0,1 | 7 · Planı |
| 8 | figür kalemle (1,0 sn) | T7("kişi") | 7 · kişi (99,05) |
| 9 | sağ zincir satır 0 `person` | kişi + 0,1 | 7 · kişi |
| 10 | büküm oku + `plan` | T7("yapar:") (yazı +0,15) | 7 · yapar: (99,33) |
| 11 | SAR kalem oku figür → `am going` (`Y.el_ok`, başlangıç figür sol omzu (FX−14, FY+70), uç kart altında (am going ortası, 118+300+16)); ardından `krm` kalınlık nabzı 9 → 14 → 9 | T7("ben,"); nabız +0,45 | 7 · ben, (100,17) |
| 12 | büküm oku + `am / is / are + ` (KRE) `V-ing` (SAR) | T7("arkadaşım.") | 7 · arkadaşım. (101,45) |
| 13 | tren kalemle (1,0 sn; parça süreleri `Y.cizgi_zamanlari` uzunluk orantılı) | T7("Tren") | 7 · Tren (102,57) |
| 14 | sol zincir satır 0 `train` | Tren + 0,1 | 7 · Tren |
| 15 | büküm oku + `timetable` | T7("tarifeye") | 7 · tarifeye (103,93) |
| 16 | SAR kalem oku tren → `leaves` (başlangıç (TX0−10, TY0+22), uç `leaves` ortası+14, B2+36; eğim −3); ardından `klm` nabzı 9 → 14 → 9 | T7("uyar."); nabız +0,45 | 7 · uyar. (104,49) |
| 17 | öğrenci 1 sn baş sallar: `#basn` 4 `to` (y 9 rot 4 · 0,22 sn → 0 · 0,26 → 9 rot 4 · 0,22 → 0 · 0,30), `svgOrigin` baş alt ortası (BTX+75·0,55, BTY+300·0,55), ease `sine.inOut` | T7("uyar.") + 0,46 | 7 · uyar. sonrası |
| 18 | `klu` (TIMETABLE altı) kalınlık nabzı | T7("Tarife") | 7 · Tarife (105,21) |
| 19 | büküm oku + `V1 / V-s` (SAR) | T7("geniş") | 7 · geniş (106,89) |
| 20 | `The train` altı SAR (sol 1. satır, B1+14, 0,4 sn) kimlik `ktm` | T7("özne") | 7 · özne (109,53) |
| 21 | `#trn` (tren grubu) tek nabız: ölçek 1,06 (0,2 sn) → 1 (0,25 sn), merkez (TX0+205·k, TY0+80·k) | T7("tren,") | 7 · tren, (111,49) |
| 22 | uçak simgesi kalemle (0,35 sn) | T7("uçak,") | 7 · uçak, (112,21) |
| 23 | kitap simgesi kalemle (0,35 sn) — son hareket ≤ yerel 20,03 | T7("ders.") | 7 · ders. (112,97) |

Ses olayları (`s.olay`): çizim başlarında `cizgi`, yazı/nokta `tik`, cevap başı `vurus`; tren ve simge parçalarında yalnız ilk 4 / ilk parça.

## 5. Yazılacak işlevler (ad + davranış; kodu sen yaz)

- `T6`, `T7`, `g(m, boy, agr=700, aile="Fredoka")` (= `Y.genislik`).
- `statik(kim, d, renk, w, alfa)` → hareketsiz çizgi `<path>` dizgisi (örnekteki gibi); `metin(kim, x, y, m, aile, agr, boy, renk, anchor)` → `<text>` dizgisi.
- `kutu_d(x, y, w, h, j)` el kutusu, YALNIZ `M/L/Z` (yardim.yol_uzunluk Q desteklemez; tren yolu Q kullanmasın).
- `daire_d(cx, cy, r, ry)` 29 noktalı, %4 kapanış paylı el dairesi, yalnız `M/L` (`Y.el_daire` küçük yarıçapta çarpık; kullanma).
- `bukum_ok(x, y0, y1, x1)` basamak oku: x'te y0 → y1 aşağı, yuvarlak köşe (Q, yarıçap 12), sağa x1, ok başı (13).
- `tren_parcalari()` → `[(d, renk, kalınlık, uzunluk)]`: vagon (0,45,175,85) · lokomotif (200,55,170,75) · kabin (200,10,75,45) ·
  baca (320,22,26,33; 3,6) · burun (370,95)-(398,130)-(370,130) · bağlantı (175,112)-(200,112; 3,6) · camlar (20,60,50,30),
  (100,60,50,30), (215,20,42,25; 3,6) · tekerlek r 17 x 40/135/240/335 y 138 · ray (−10,158)-(420,158) IKN 4 · duman (345,2) 11×9 ve
  (372,−16) 8×7 IKN 3,4. Nokta = (TX0 + k·x, TY0 + k·y). Uzunluk elle (kutu çevresi, 2πr, doğru uzunluğu). Kimlik `tr0..`.
- `ikon(s, kim, ad, x, y, boy, t, sure)` → `Y.tabler(ad)` yolları, her biri `s.yol(..., ek='transform="translate(x y) scale(boy/24)"')`,
  çizgi kalınlığı u(4,6)/ölçek, KRE.
- `nabiz(s, sec, t, ox, oy, olcek)` ve `kalinlik(s, sec, t, w0, w1)` (GSAP `attr: {"stroke-width"}`; konum değişmez).
- `zincir(s, ad, satirlar, zamanlar)`: satır 0 düz `s.yazi`; i ≥ 1: önceki satırın x'inden `bukum_ok(xp+14, ZB[i−1]+22, ZB[i]−14, xp+50)`
  IKN 4,5 (0,3 sn), yazı x = xp+64, zamanı +0,15. Kimlikler `{ad}z{i}`, `{ad}y{i}`.
- `uret()`: kartlar → baş + balon (+ `bal_ids`) → cevap olayları (§4) → `return s, {"kun": …, "bal_ids": …, "tren_ids": set(…)}`.
- `__main__`: `s, parca = uret()`; `Y.kontrol`; `proje/index.html` = `Y.html(s, Z["sure"], parca["kun"], None, logo, bal_ids=…,
  gruplar=[("trn", parca["tren_ids"])])`; tek satır özet yazdır.

## 6. Çakışma kapısı (yazı × çizim = hata; 6 px pay) — yerleşim bunun için seçildi, değiştirme

- Hiçbir çizgi (ok, bağ, figür, tren, simge, balon kenarı) bir yazının mürekkep kutusuna 6 px'ten çok girmez.
- Figür okunun ucu KART DIŞINDA (kart altı + 16) kalır: `am going` altında 2. satır yazısı var.
- Altçizgiler yalnız kendi sözcüğünün altında (en çok 24 px aşağıda); iki altçizgi üst üste binmez.
- Etiketler sağa yaslı: bağ çizgisi ve tren oku `leaves` altına sol yarıdan gelir, etiketi kesmez.

## 7. Kabul

1. Şef `ONIZLE_YALNIZ=1 bash calistir.sh` koşar: `assert`/`kontrol` hatasız, `proje/index.html` ve `olaylar.json` yazılır.
2. `bash araclar/qa-yerel.sh 02-04-ydt-temel 06-hyperframes-soru1 <açık t1,t2,t3> <koyu t> --hazirla` çıkış kodu 0.
3. Karelerde taşma, kesik yazı, üst üste binme, okunmaz kontrast yok.
