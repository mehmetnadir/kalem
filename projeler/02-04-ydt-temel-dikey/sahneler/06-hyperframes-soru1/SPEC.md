# SPEC — 02-04 DİKEY sahne 06 `06-hyperframes-soru1` · uret.py (şef tasarımı, 15.11)

## 0. Görev

| Alan | Değer |
|---|---|
| Yazılacak TEK dosya | `/home/sef/01dev/_worktrees/kalem-0204/projeler/02-04-ydt-temel-dikey/sahneler/06-hyperframes-soru1/uret.py` |
| Dokunma | aynı dizindeki `yardim.py`, `olay.py`, `calistir.sh`, `SPEC.md`; `ortak/`, başka sahne, BRIEF, yatay paket. Silme yok. Test, render, git yok. `uret.py`'yi KOŞMA (şef koşar). |
| Yardımcı modül (hazır, DİKEY) | `…/06-hyperframes-soru1/yardim.py` (dikey 01 kopyası): `W=1080, H=1920`, `u(n)=n`, `RENK`, `LOGO_EN_BOY`, `genislik()`, `Sahne` (`S`, `olay`, `to`, `set`, `fromto`, `yol`, `yazi`, `figur`), `el_cizgi`, `el_ok`, `balon_sol`, `tabler`, `cizgi_zamanlari`, `altyazi_dilimleri`, `altyazi_svg`, `html(...)`, `kontrol(s, kare)`, `ORTAK`. `kunye_svg` yalnız çip çizer: KULLANMA, §3.1'deki `kunye_tam()`'ı yaz. |
| Kalıp 1 (dikey iskelet) | `/home/sef/01dev/_worktrees/kalem-0204/projeler/02-04-ydt-temel-dikey/sahneler/01-hyperframes-giris/uret.py` — başlık bloğu (`PAKET`, `SAH`, `Z`), altyazı aç/kapa döngüsü, `__main__` (`altyazi_svg` → `html(..., ek=altyazi)`). |
| Kalıp 2 (içerik yardımcıları) | `/home/sef/01dev/_worktrees/kalem-0204/projeler/02-04-ydt-temel/sahneler/06-hyperframes-soru1/uret.py` (YATAY) — `T6`, `T7`, `g`, `statik`, `metin`, `kutu_d`, `daire_d`, `bukum_ok`, `tren_parcalari`, `ikon`, `nabiz`, `kalinlik`, `zincir`, öğrenci başı regex'i, balon sözcük döngüsü. Bu işlevleri al; yerleşim sayılarını ALMA (yatay 1920×1080). |
| Çağıran | `olay.py`: `import uret as U; s, _ = U.uret(); U.Z["kare"]` → `uret()` `(s, parca)` döndürür; modül düzeyinde `Z` olur. |
| Docstring | 1. satır sahne kimliği; bir satır `yanılgı: tarifeli gelecek planlanmış gelecekle karışır (tren de plana göre kalkar → -ing). Soru 10 sözcük (≤ 12).`; bir satır `Tasarım: SPEC.md (şef); kod agy-filo (rol kod) 15.11.` |

## 1. Zaman (tek kaynak; sabit saniye yazma)

- `PAKET = AD.parent.parent`; `SAH` = `PAKET/zaman.json` içinde `klasor == AD.name` (t_bas 93,35 · kare 613).
- `Z = {"t_bas", "kare", "sure": round(kare/30, 4)}`; `TB = Z["t_bas"]`; yerel sn = `s.S(küresel)`.
- `S6` = cümle 6 (öğrenci), `S7` = cümle 7 (öğretmen), kaynak `PAKET/ortak/anlatim/sozcukler.json`.
- `assert` S6 sözcükleri = `["Hocam,", "tren", "de", "plana", "göre", "kalkmıyor", "mu?", "Neden", "-ing", "yok?"]`.
- `T6(i)`, `T7(sozcuk, n=0)` yatay kalıptaki gibi (bulunmazsa `assert`).
- `__main__`: `Y.kontrol(s, Z["kare"])` (ilk hareket ≥ 0,4 sn; son bitiş ≤ (613−12)/30 = 20,033 sn).

## 2. Renk, yazı, genel kurallar

- Renk yalnız `Y.RENK`: `KRE = murekkep`, `IKN = ikincil`, `SAR = vurgu`, `ZEM = zemin`. Kırmızı, yeşil, emoji, gradyan, gölge YOK.
  Tema çevirisi `hf_tema.py` ile olur (calistir.sh): `rect fill=SAR` → vurguDolgu, `text fill=ZEM` → pilMetin. Hex yazma.
- Ölçüler 1080×1920 mantıksal px (`u(n)` = n). Bu SPEC'teki sayılar mutlak koordinattır.
- Yazı: Fredoka 700 (şerit), Caveat 700 (balon, zincirler), Lexend 700 (künye). İçerik yazısı 64; künye 56 / 36 / 40; altyazı 44.
- Python tip ipuçları zorunlu. `try/except: pass` YOK. Satır ≤ 120 karakter. Girinti 4 boşluk (dosyadaki kalıp).
- Ekran metni yalnız bu SPEC'teki metinler. Başka yazı ekleme.
- **İkiz kuralı (en çok 3 sarı belirteç, BRIEF §0):** sönecek her sarı çizginin aynı `d` ile `IKN` ikizi olur (`<kim>_s`, başta opaklık 0).
  `soldur(s, a, b, t, d=0.25)` = `#a` opaklık 0'a, `#b` opaklık 1'e (`power1.inOut`). Parlatma = `soldur(s, "<kim>_s", "<kim>", t)`.
  Yazı ikizi (V-ing) solmaz: iki `s.set` ile tek karede değişir.
- **Sarı yazı yok, hap var (sözleşme satır 36):** açık temada `vurgu` renkli yazı okunmaz (≈ 2,3:1). Vurgulanan kalıp (`V-ing`,
  `V1 / V-s`) haptır: `hap(kim, x, taban, metin) -> str` = `<g id=kim style="opacity:0">` içinde `rect` (x − 10, taban − 52,
  g(metin, 64, 700, "Caveat") + 20, 74, rx 16, fill SAR) + `text` (x, taban, Caveat 700 64, fill ZEM). Hap `s.goster(#kim, t, d=0.3)` ile gelir.
- **Altçizgi yüksekliği (sözleşme satır 35, BRIEF §0):** kuyruksuz sözcük taban + 0,28 em; kuyruklu sözcük (g, y, p) Fredoka'da
  taban + 0,48 em, Caveat'ta taban + 0,52 em.

## 3. Yerleşim (mutlak px)

### 3.1 Künye `kunye_tam() -> str` (kare 0'dan sabit; BRIEF-DIKEY §2.1)

| Öğe | Değer |
|---|---|
| Kök | `<g id="kunye">…</g>` |
| Ders satır 1 | `<text id="ku-ders1">` `SIMPLE PRESENT vs`, x 48, taban 212, Fredoka 700 56, fill KRE |
| Ders satır 2 | `<text id="ku-ders2">` `PRESENT CONTINUOUS`, x 48, taban 276, aynı yazı |
| Rozet | `<g id="ku-rz">`: `rect` x = 48 + g("PRESENT CONTINUOUS", Fredoka 700 56) + 24 (≈ 670), y 216, w = g("YDT · BASIC", Lexend 700 36) + 56 (≈ 282), h 72, rx 36, fill SAR; `text` `YDT · BASIC` ortası, taban 265, `text-anchor="middle"`, Lexend 700 36, fill ZEM |
| Çip | `<g id="ku-bolum">`: cw = g("Question", Lexend 700 40) + 64; `rect` x 1032 − cw, y 48, w cw, h 80, rx 40, fill none, stroke SAR, stroke-width 4; `text` `Question` ortası, taban 102, middle, Lexend 700 40, fill SAR |
| Logo | `Y.html` logo parametresi `(48, 48, round(96 * Y.LOGO_EN_BOY, 2), 96)` |

### 3.2 Üst şerit (kare 0'dan sabit; sahne 05'in iki cümlesi)

| Öğe | Değer |
|---|---|
| Satır 1 | `metin("st1", 48, 400, "The train … leaves at 7 pm today.", "Fredoka", 700, 64, KRE)` — tek `<text>`; `assert 48 + g(...) <= 1032` |
| Satır 2 | `metin("st2", 48, 500, "I am going … tonight.", "Fredoka", 700, 64, KRE)` |
| Konumlar | `XL = 48 + g("The train … ", 64)`, `WL = g("leaves", 64)`; `XG = 48 + g("I ", 64)`, `WG = g("am going", 64)`; `L2SON = 48 + g(satır 2, 64)` |
| `klm` + `klm_s` | *leaves* altı: `Y.el_cizgi(XL − 2, 418, XL + WL + 2, 418, 1)`, w 10; `klm` SAR opaklık 1, `klm_s` IKN opaklık 0 (`statik`) |
| `krm` + `krm_s` | *am going* altı (g kuyruğunun altından, taban + 0,48 em): `Y.el_cizgi(XG − 2, 531, XG + WG + 2, 531, 1)`, w 10; `krm` SAR 1, `krm_s` IKN 0 |
| Kanal | *leaves* altına giden iki çizgi (§3.3 bağ, §3.6 tren oku) satır 1 ile satır 2 arasındaki y 438 kanalından gelir. Son parça: `L XU 438`, `XU = XL + 0,75·WL`; ok başı sola: `M XU+19 427.5 L XU 438 L XU+19 448.5` (aynı yolun sonuna eklenir) |

### 3.3 Soru anı: öğrenci başı + balon (y 540–960)

| Öğe | Değer |
|---|---|
| Baş | `ortak/cizim/peeps-kit/ogrenci-bas.svg` 3 yolu (yatay regex). viewBox −45 0 240 330. Başlangıç kutusu sol üst (96, 680), yükseklik 240: `BS0 = 240/330`, `BTX = 96 + 45·BS0`, `BTY = 680`. Yapı: `<g id="basm"><g id="basn"><g id="bas" transform="translate(BTX BTY) scale(BS0)" fill="none" stroke=KRE stroke-width=4.0/BS0 …>bas0..2</g></g></g>`; yollar opaklık 0, kalemle çizilir. `#balg` İÇİNE GİRMEZ. |
| Balon | `s.yol("bal", Y.balon_sol(410, 565, 1010, 905, 290, 845), …, KRE, 4.5)`; kuyruk ucu başın sağında |
| Soru metni | Caveat 700 64, KRE, sözcük sözcük (`s.yazi`, `bw0..bw9`, d 0,12). Satır 1 sözcük 0–3 taban 665; satır 2 sözcük 4–6 taban 749; satır 3 sözcük 7–9 taban 833; her satır x 450'den, sözcük arası `g(" ", 64, 700, "Caveat")`. `assert` her satırın sağ ucu ≤ 980 |
| Sarı nokta `nk` | `NX` = *tren* sözcüğünün ortası (`pos[1]`), `NY = 548`; tek noktalı yol `M NX NY L NX+0.1 NY`, SAR, w 18. `assert NX >= L2SON + 20` |
| Bağ `cn` | `M NX 548 L NX 454 Q NX 438 NX−16 438 L XU 438` + §3.2 ok başı; SAR, w 6, alfa 0,9 |
| `bm8` | *-ing* altı (Caveat, g kuyruğu: taban + 0,52 em): `Y.el_cizgi(xi − 2, 866, xi + wi + 2, 864, 1)` (xi, wi = `pos[8]`), SAR, w 10 |
| `bal_ids` | `bal`, `bw0..bw9`, `nk`, `cn`, `bm8` (hepsi `#balg` içinde birlikte söner) |
| Bitiş konumu | 98,41'de `#basm` (§4 olay 6) baş kutusunu sol üst (892, 1230), yükseklik 160'a taşır: `x 796`, `y 550`, `scale 160/240`, `svgOrigin "96 680"` |

### 3.4 Cevap 1 (y 540–965): öğretmen figürü + zincir

| Öğe | Değer |
|---|---|
| Figür | `s.figur("standing-3", "fig", 72, 556, 420, t0, t0 + 1.0, w=4.4)` (erkek, K22; 02-02'de erkek figür). `FW` = dönen genişlik; `assert 72 + FW + 40 <= 268` |
| Figür oku `ok_fig` + `ok_fig_s` | `Y.el_ok(72 + FW + 14, 710, XG + WG/2 + 10, 552, 2.0)`, w 8; `ok_fig` SAR alfa 1, `ok_fig_s` IKN alfa 0 (aynı `t`, aynı süre; `s.yol(..., alfa=0)`) |
| Zincir 1 (`zs`) | x0 268, tabanlar (690, 800, 910), Caveat 700 64. Satır 0 `person` KRE; satır 1 `plan` KRE; satır 2 `am / is / are + ` KRE (`s.yazi`, kimlik `zsy2`) + hap `zsy2v` `V-ing` (x = satır x + g("am / is / are + ", 64, 700, "Caveat") + 12, yazıdan 0,2 sn sonra `goster`). Yazı ikizi `zsy2s`: `V-ing` düz `<text>`, KRE, hapla aynı x/taban, `opacity="0"` ile sabit eklenir (kırpma yok); olay 17'de görünür. `assert` hap sağ ucu ≤ 960 |

### 3.5 Cevap 2 (y 990–1392): zincir solda, tren sağda, simgeler trenin altında

| Öğe | Değer |
|---|---|
| Zincir 2 (`zt`) | x0 72, tabanlar (1065, 1175, 1285), Caveat 700 64. Satır 0 `train` KRE; satır 1 `timetable` KRE (kimlik `zty1`); satır 2 hap `zty2v` `V1 / V-s` (büküm okunun ucundan sonra, x = xp + 74) |
| Tren | yatay `tren_parcalari(TX0=548, TY0=1035, k=1.1)` (aynı parça tablosu; `u()` dikeyde birim). Kimlikler `tr0..`; `Y.html` `gruplar=[("trn", tren_ids)]`. `assert TX0 + 420·k <= 1032` |
| Uçak / kitap | `ikon(s, "ik_ucak", "plane", 540, 1240, 140, t, 0.35)`, `ikon(s, "ik_kitap", "book", 700, 1240, 140, t, 0.35)` |
| Öğrenci başı (bitiş) | kutu x 892–1008, y 1230–1390 (BRIEF: 870–1030 kutusunun ortası) |

### 3.6 Tren oku `ok_trn` + `ok_trn_s`

`M 1000 TY0+60 L 1000 454 Q 1000 438 984 438 L XU 438` + §3.2 ok başı; w 8. `ok_trn` SAR alfa 1, `ok_trn_s` IKN alfa 0.
Dikey parça x 1000: zincir 1 sağ ucu (≤ 960) ile satır 1 sonu (y 413) arasında boştur; yatay parça y 438 kanalındadır.

### 3.7 Altyazı (y 1400–1536)

- `dilimler = Y.altyazi_dilimleri([6, 7])` (4 dilim); `Y.altyazi_svg([{"id": f"alt{i}", "metin": m} ...])` → `__main__`'de `html(..., ek=...)`.
- Aç: `s.set("#alt{i}", max(0, s.S(t0) − 0.05), {"opacity": 1})`. Kapa: `min(s.S(t1) + 0.35, s.S(sonraki t0) − 0.05)`; değer `Z["sure"]`'den küçükse.
  Son dilim açık kalır. İki dilim aynı anda görünmez.

## 4. Olay listesi (küresel sn = sözcük t0; kod `s.S(...)` ile yerel)

| # | Olay | Zaman | Cümle sözcüğü |
|---|---|---|---|
| 1 | baş 3 yolu kalemle (her biri 0,32 sn, 0,05 ara), ses `cizgi` | yerel 0,43 | — (ilk 12 kare durgun) |
| 2 | balon çizimi 0,55 sn, `cizgi` 0,7 | T6(0) − 0,05 | 6 · Hocam, (93,90) |
| 3 | soru sözcükleri `bw0..9` (d 0,12, `tik`) | her sözcüğün t0 | 6 · 0–9 |
| 4 | `nk` (0,12 sn, `tik`) + `cn` +0,14'te (0,45 sn, `cizgi`) | T6(1) | 6 · tren (94,62) |
| 5 | `bm8` (0,28 sn, `cizgi`) + `soldur(krm → krm_s)` | T6(8) | 6 · -ing (96,98) |
| — | DURAKLAMA: olay yok | 97,74–98,41 | — |
| 6 | `#balg` opaklık 0 (0,4 sn, `power2.in`, `vurus` 0,5) + `#basm` taşıma (§3.3, 0,6 sn, `power3.inOut`) | T7("Planı") | 7 · Planı (98,41) |
| 7 | figür kalemle 1,0 sn; zincir 1 satır 0 `person` +0,1; `soldur(klm → klm_s)` +0,1 | T7("kişi") | 7 · kişi (99,05) |
| 8 | büküm oku + `plan` | T7("yapar:") (yazı +0,15) | 7 · yapar: (99,33) |
| 9 | `ok_fig` + ikizi (0,45 sn, `cizgi` 0,55); `soldur(krm_s → krm)` +0,45 | T7("ben,") | 7 · ben, (100,17) |
| 10 | büküm oku + `zsy2` `am / is / are + ` (+0,15) + hap `zsy2v` `V-ing` (+0,35, `goster` 0,3 sn) | T7("arkadaşım.") | 7 · arkadaşım. (101,45) |
| 11 | tren kalemle 1,0 sn (`Y.cizgi_zamanlari`, ilk 4 parçada `cizgi`); zincir 2 satır 0 `train` +0,1; `soldur(ok_fig → ok_fig_s)` ve `soldur(krm → krm_s)` | T7("Tren") | 7 · Tren (102,57) |
| 12 | büküm oku + `timetable` | T7("tarifeye") (yazı +0,15) | 7 · tarifeye (103,93) |
| 13 | `ok_trn` + ikizi (0,6 sn, `cizgi` 0,55); `soldur(klm_s → klm)` +0,6 | T7("uyar.") | 7 · uyar. (104,49) |
| 14 | öğrenci 1 sn baş sallar: `#basn` 4 `to` (y 12 rot 4 · 0,22 → 0 · 0,26 → y 12 rot 4 · 0,22 → 0 · 0,30), `sine.inOut`, `svgOrigin` = `(BTX + 75·BS0) (BTY + 300·BS0)` (başlangıç koordinatı; `#basm` dışta taşır) | T7("uyar.") + 0,46 | 7 · uyar. sonrası (104,95) |
| 15 | TIMETABLE nabzı (şeritte): `kalinlik(s, "#klm", t, 10, 16)` + `nabiz(s, "#zty1", t, orta x, orta y, 1.08)` | T7("Tarife") | 7 · Tarife (105,21) |
| 16 | büküm oku + hap `zty2v` `V1 / V-s` (+0,15, `goster` 0,3 sn); `soldur(ok_trn → ok_trn_s)` | T7("geniş") | 7 · geniş (106,89) |
| 17 | `ktm`: *The train* altı `Y.el_cizgi(46, 418, 48 + g("The train", 64) + 2, 418, 1)`, SAR, w 10, 0,4 sn; `s.set("#zsy2v", t, {opacity: 0})` + `s.set("#zsy2s", t, {opacity: 1})` (hap söner, düz `V-ing` kalır) | T7("özne") | 7 · özne (109,53) |
| 18 | `nabiz(s, "#trn", t, TX0 + 205·k, TY0 + 80·k, 1.06)` | T7("tren,") | 7 · tren, (111,49) |
| 19 | uçak simgesi kalemle 0,35 sn | T7("uçak,") | 7 · uçak, (112,21) |
| 20 | kitap simgesi kalemle 0,35 sn — son hareket ≤ yerel 20,033 | T7("ders.") | 7 · ders. (112,97) |

Sarı belirteç sayımı (en çok 3): kare 0 `klm`, `krm` · 94,62 + bağ · 96,98 `krm` söner + `bm8` · 98,41 balon söner ·
99,15 `klm` söner · 100,62 `krm` parlar (+ `ok_fig`) · 101,60 `V-ing` · 102,57 `ok_fig`, `krm` söner · 104,49 `ok_trn` + `klm` ·
106,89 `V1 / V-s` + `ok_trn` söner · 109,53 `ktm` + `V-ing` hapı söner. Son kare: `klm`, `V1 / V-s` hapı, `ktm`.

## 5. Yazılacak işlevler (ad + davranış; kodu sen yaz)

- Yatay kalıptan: `T6`, `T7`, `g(m, boy, agr=700, aile="Fredoka")`, `statik(kim, d, renk, w, alfa)`, `metin(...)`, `kutu_d`, `daire_d`,
  `bukum_ok`, `tren_parcalari`, `ikon`, `nabiz`, `kalinlik`.
- `zincir(s, ad, satirlar, zamanlar, x0, ZB) -> dict`: yatay kalıp, ama tabanlar parametre (`ZB`), yazı Caveat 700 64, büküm oku
  `bukum_ok(xp + 14, ZB[i−1] + 28, ZB[i] − 16, xp + 50)` IKN 4,5 (0,3 sn), yazı x = xp + 64, d 0,3. Satır 2'nin hapı ve
  ikizi §3.4 / §3.5 (zincir dışında, `uret()` içinde yazılabilir). Yazı kimlikleri `{ad}y{i}`, ok kimlikleri `{ad}z{i}`.
  Dönüş: satır kimliği → (x, genişlik, taban) (olay 15 nabız merkezi ve hap x'i için).
- `kunye_tam() -> str` §3.1. `soldur(s, a, b, t, d=0.25) -> None` §2. `hap(kim, x, taban, metin) -> str` §2.
- `uret() -> tuple[Y.Sahne, dict]`: şerit + künye → baş + balon → cevap olayları (§4) → altyazı aç/kapa →
  `return s, {"kun": kunye_tam(), "bal_ids": bal_ids, "tren_ids": set(tren_ids), "alt": altyazi_svg_dizgisi}`.
- `__main__`: `s, p = uret()`; `Y.kontrol(s, Z["kare"])`; `proje/index.html` = `Y.html(s, Z["sure"], p["kun"], None, logo,
  ek=p["alt"], bal_ids=p["bal_ids"], gruplar=[("trn", p["tren_ids"])])`; tek satır özet yazdır (komut, olay sayısı).

## 6. Çakışma kapısı (yazı kutusu × çizim; 6 px pay) — yerleşim bunun için seçildi, değiştirme

- Kapı `<text>` kutusunu tam genişlikte ölçer (satır 1 kutusu x 48–1016, y ≈ 355–413; satır 2 x 48–647, y ≈ 452–515).
  Bu yüzden *leaves*'e giden çizgiler satır 2'yi KESMEZ: x ≥ L2SON + 20'de yükselir, y 438 kanalından girer.
- Figür oku *am going*'e satır 2'nin altından gelir (ucu y 552, `krm` altında); `person` yazısına ≥ 20 px uzak kalır.
- Altçizgiler yalnız kendi sözcüğünün altında (≤ 24 px); iki farklı altçizgi üst üste binmez.
- Hiçbir öğe y 1392'den aşağı inmez (altyazı ve platform bandı boş); hiçbir öğe x 48–1032 dışına taşmaz.

## 7. Kabul

1. Şef `ONIZLE_YALNIZ=1 bash calistir.sh` koşar: `assert` / `kontrol` hatasız; `proje/index.html` ve `olaylar.json` yazılır.
2. `cd /home/sef/01dev/_worktrees/kalem-0204 && bash araclar/qa-yerel.sh 02-04-ydt-temel-dikey 06-hyperframes-soru1 97.5,104.0,113.3 108.0 --hazirla` çıkış 0.
3. Karelerde taşma, kesik yazı, üst üste binme, okunmaz kontrast, boş kare yok; platform bandı boş.
