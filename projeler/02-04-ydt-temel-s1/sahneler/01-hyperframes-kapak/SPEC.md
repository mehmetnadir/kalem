# SPEC v2 — 02-04-ydt-temel-s1 · sahne 01-hyperframes-kapak (huni v2, HyperFrames 1080×1920, 102 kare)

Kaynak: `uretim-tutanagi/istem/sahne-v2/D-01-hyperframes-kapak.md`, `BRIEF-S1.md` ("Yerleşim", "Kanal katmanı", "Sahne içeriği"
0,00–3,00, "Kapak"), `D/.claude/docs/huni-v2-standart.md` §1, §2, §7. Yazan: şef (15.11.2026). Eski SPEC (v1):
`~/Silinecekler/2026-11-15-huni-v2/02-04-ydt-temel-s1/sahneler/01-hyperframes-kapak/SPEC.md`.
Bu belge tasarım verir; tam kod içermez. K = `/home/sef/01dev/_worktrees/kalem-0204`.
S = `K/projeler/02-04-ydt-temel-s1/sahneler/01-hyperframes-kapak/` (bu sahne dizini).

İçerik v1 ile aynıdır. Değişen: yerleşim bantları (v2), kanal katmanı (yeni, kalıcı), künye (tek satır), çip (YOK), uçuş hedefi.

## 1. Dosyalar

| Dosya | İş | Kim |
|---|---|---|
| `S/yardim.py` | VAR (v1). §3'e göre değiştir. | ajan A |
| `S/uret.py` | VAR (v1). §4'e göre değiştir. | ajan B |
| `S/olay.py`, `S/calistir.sh`, `S/zamanlar.json`, `S/nesneler.json`, `S/cizim/*` | VAR. DOKUNMA. | şef |

Her ajan yalnız kendi dosyasını yazar. Başka dosyaya dokunma. Silme yok. Test, render, git, betik koşma yok (şef koşar).
`ortak/`, BRIEF, ana ders salt okunur. Python: girinti 4 boşluk (var olan dosyayla uyum), satır ≤ 120, yeni işlevde tip ipucu.
Çalıştırma `/usr/bin/python3 uret.py` (fontTools kullanıcı site-packages'ta; `-I` YOK). A ve B paralel çalışır: arayüz §2'de sabittir.

## 2. Arayüz (yardim.py → uret.py; ikisi de buna uyar)

| Ad (yardim.py) | Tür | Değer / davranış |
|---|---|---|
| `HUD` | dict | §3.2 tablosu (eski anahtarlar kalkar) |
| `KONU` | str | `"Simple Present vs Present Continuous"` |
| `KONU_PARCA` | tuple[str, str] | `("Simple Present vs", "Present Continuous")` (uçuş hedefi; aradaki tek boşluk KONU'daki boşluktur) |
| `ROZET` | str | `"YDT · TEMEL"` |
| `KANAL_YAZI` | str | `"@ydspublishing"` |
| `konu_boyu() -> int` | işlev | §3.3 |
| `rozet_konumu() -> tuple[float, float]` | işlev | (x, genişlik); §3.3 |
| `kunye_svg() -> str` | işlev | ARGÜMAN YOK (çip kalktı); §3.4 |
| `altyazi_svg(t_bas, sure, liste)` | işlev | imza aynı; §3.5 |
| `genislik`, `tabler`, `font_css`, `font_kopyala`, `zemin_html`, `ZEMIN_CSS`, `RENK`, `W`, `H` | — | DEĞİŞMEZ |

## 3. `yardim.py` değişiklikleri (ajan A)

Kalıp: aynı dosyanın v1 hâli (`S/yardim.py`). Değişen yerler aşağıdadır; kalan her şey harfi harfine kalır.

### 3.1 Docstring
1. satır: `"""02-04-ydt-temel-s1 sahne 01; huni v2 (15.11): kanal katmanı + künye satırı + v2 bantları (BRIEF-S1 "Kanal katmanı").`

### 3.2 `HUD` sözlüğü (eski sözlüğün yerine; değerler BRIEF-S1 tablosundan birebir)
| Anahtar | Değer | Anlam |
|---|---|---|
| `kenar` | 60 | içerik sol kenarı |
| `sagSinir` | 960 | içerik sağ sınırı (platform 960–1080'i kapatır) |
| `kanalLogoX`, `kanalLogoY` | 53.2, 291 | logo `<image>` sol üstü (SVG iç boşluğu düşülür: görünür sol kenar x 60) |
| `kanalLogoEn`, `kanalLogoYuk` | 193.5, 48 | logo boyu |
| `kanalYaziX`, `kanalYaziTaban`, `kanalYaziBoy` | 263, 330, 42 | `@ydspublishing` (Lexend 700) |
| `konuX`, `konuTaban` | 60, 420 | konu adı (Fredoka 700) |
| `konuBoyUst`, `konuBoyAlt` | 34, 28 | konu boyu aralığı |
| `rozetY`, `rozetH`, `rozetAra`, `rozetYazi`, `rozetPay` | 386, 48, 20, 26, 20 | rozet hapı (y 386–434), konu sonu + 20, Lexend 700 26, yan iç pay 20 (v1 oranı 28/36 em) |
| `icerikBas`, `icerikSon` | 460, 1380 | içerik bandı |
| `altyaziBas`, `altyaziSon` | 1400, 1550 | altyazı bandı |
| `altyaziYazi`, `altyaziSatir` | 44, 56 | Lexend 500 |
| `altyaziOrta`, `altyaziGen` | 510, 900 | altyazı ortası ve satır genişliği (x 60–960) |

Silinen anahtarlar: logoY, logoYuk, dersTaban, dersYazi, dersSatir, cipY, cipH, cipYazi, cipDolgu (v2'de yok). `DERS` sabiti kalkar.

### 3.3 Ölçü işlevleri
- `rozet_genislik()` (iç yardımcı, isteğe bağlı): `genislik("Lexend", 700, ROZET, rozetYazi) + 2 * rozetPay` (≈ 203,6).
- `konu_boyu() -> int`: boy = konuBoyUst'ten konuBoyAlt'a 1'er inerek; ilk boy için `konuX + genislik("Fredoka", 700, KONU, boy) +
  rozetAra + rozet genişliği ≤ sagSinir` ise o boy döner. Hiçbiri sığmazsa `ValueError` (metin: hangi boyda kaç px). Ölçüm: 34 → 868,2 (sığar).
- `rozet_konumu() -> (x, w)`: x = konuX + genislik(Fredoka 700, KONU, konu_boyu()) + rozetAra (≈ 664,6); w = rozet genişliği.
- `cip_olcu()` ve `rozet_konumu`'nun v1 gövdesi kalkar.

### 3.4 `kunye_svg() -> str`
Çıktı tek `<g id="kunye">`; içinde sırayla üç grup. Hiçbirine `style="opacity…"` ya da sınıf yazma.
1. `<g id="kanal">`:
   - `<image id="logoimg" href="assets/logo.svg" x="53.20" y="291" width="193.50" height="48"/>` (değerler HUD'dan, `%.2f`).
     Kimlik `logoimg` ZORUNLU (`ortak/hf_tema.py` canlı tema geçişi bu kimliği arar).
   - `<text id="kanal-yazi" x="263" y="330" font-family="Lexend" font-weight="700" font-size="42" fill="#f3efe6"
     style="font-kerning:none">@ydspublishing</text>` (fill = `RENK["murekkep"]`; hf_tema temaya çevirir).
2. `<g id="ku-konu">`: tek `<text>`: x konuX, y konuTaban, Fredoka 700, font-size `konu_boyu()`, fill `RENK["murekkep"]`,
   `style="font-kerning:none"`, metin KONU.
3. `<g id="rz0">`: `<rect x=rozet x (%.1f) y=386 width=w (%.1f) height=48 rx=24 fill=RENK["vurgu"]/>` + `<text x=x+w/2 y=rozetY+rozetH/2+9
   (= 419) text-anchor="middle" font-family="Lexend" font-weight="700" font-size="26" fill=RENK["zemin"]>ROZET</text>`.
   (hf_tema: `rect[fill="#f2a93b"]` → vurguDolgu, açık `#ffe066`; `text[fill="#1b1a17"]` → pilMetin, açık `#1b2440`.)
Yasak kimlik: `rz1`, `t1`, `t2`, `ku-nokta`, `ku-cip`, `ku-ders`, `ku-logo` (hf_tema özel kuralları ya da eski kod).

### 3.5 Altyazı (bant 1400–1550, x 60–960)
- `altyazi_satirlari()` ve `_sar()`: satır genişlik sınırı `W - 2 * HUD["kenar"]` yerine `HUD["altyaziGen"]` (900). Kalan mantık aynı.
- `altyazi_svg()`: `<text x="540"` yerine `x` = `HUD["altyaziOrta"]` (510). y0 kuralı aynı (1 satır: altyaziBas + 84; 2 satır: + 56;
  satır aralığı altyaziSatir). Her parça için denetim: son satır tabanı + 0,25·altyaziYazi ≤ altyaziSon (`assert`, metinli).
- `altyazi_dilimle()` aynı kalır (yalnız `_sar` yeni genişliği kullanır).

## 4. `uret.py` değişiklikleri (ajan B)

Kalıp: aynı dosyanın v1 hâli (`S/uret.py`): HTML iskeleti, `ac()`, altçizgi darbesi, kırpma ile yazım, `uc2()` (svgOrigin uçuştan
önce BİR KEZ `gsap.set`, `smoothOrigin: false`; tween'de svgOrigin YOK), altyazı aç/kapa, `zamanlar()`, `__main__`. Bunlar korunur.
`getattr`/`hasattr` yedek dalları kalkar: §2 arayüzü doğrudan kullanılır. `zamanlar.json`'da `ucus_ayrik` = 10 (tek satırda dikey ayrım).

### 4.1 Sabitler ve türetilen ölçüler (px; g(m, aile, ağırlık, boy) = `Y.genislik`)
| Ad | Değer | Not |
|---|---|---|
| KENAR, SAG, ORTA | `Y.HUD["kenar"]` 60, `Y.HUD["sagSinir"]` 960, (KENAR + SAG)/2 = 510 | içerik ortası |
| B | floor(min(190, (SAG − KENAR) / g(BAS1,1), (SAG − KENAR) / (g(BAS2,1) + 2·PAD))) | ≈ 152; assert 140 ≤ B ≤ 190 |
| g1, t1x | g(BAS1, Fredoka 700, B), ORTA − g1/2 | ≈ 847,7 / 86,1 |
| TOP1 | 472 | başlık 1 büyük harf üstü (içerik bandı 460 + 12) |
| T1 | TOP1 + 0,70·B | ≈ 578,4 |
| ALTI_Y, HAP_UST, T2, HAP_ALT | v1 formülü (T1 + 0,20·B; + 29; + 0,98·B; T2 + 0,26·B) | ≈ 608,8 / 637,8 / 786,8 / 826,3 |
| hap | w = g(BAS2,B) + 2·PAD·B, x = ORTA − w/2, rx = (HAP_ALT − HAP_UST)/2 | ≈ 895,1, x 62,4 |
| bas2t | x = ORTA (510), `text-anchor="middle"`, taban T2 | |
| SOL | 84 | cümle satırı sol kenarı = sahne 02 `SOL` (KUNYE.kenar 60 + 24) |
| SAT_BOY | 80 | Caveat 700 |
| R1_K, R2_K | 920, 1040 | kapak tabanları (R2 − R1 = 120 = sahne 02 aralığı) |
| R1_SON, R2_SON | 560, 680 | uçuş sonrası = sahne 02 `Y_L1`/`Y_L2` (v2) |
| DY | R1_SON − R1_K = −360 | iki satıra aynı kayma |
| ZEMIN_Y | 1372 | yer çizgisi; yol `M{KENAR+4} 1372 L{SAG−4} 1372` |
| EV_S, EV_X, EV_Y | 16, KENAR (60), ZEMIN_Y − 21·EV_S (1036) | ev ekranda x 108–396, y 1084–1372 |
| FIG_H, FIG_X | 400, 540 | figür kutusu; fs = FIG_H/(y1 − y0); üstü ZEMIN_Y − FIG_H = 972 |
| EX, EY | v1 formülü | ≈ (652, 1184) |
| BV_S, BX, BY | 9, EX + 6 − 12·BV_S, EY − 3·BV_S | v1 formülü |
| E1 | `I live`: x = EV_X + 12·EV_S (252, orta), taban EV_Y + 3·EV_S − 36 (1048) | Caveat 700 72 |
| E2 | `I am living`: x = SAG (960), `text-anchor="end"`, taban EY − 48 | Caveat 700 72 |
| boy, rz_x, rz_w | `Y.konu_boyu()`, `Y.rozet_konumu()` | ≈ 34 / 664,6 / 203,6 |
| rz_y, rz_h | `Y.HUD["rozetY"]` 386, `Y.HUD["rozetH"]` 48 | |
| gk1, gk2 | g(KONU_PARCA[0], Fredoka 700, boy), g(KONU_PARCA[1], …) | ≈ 272,8 / 303,8 |
| KONU_SON | KENAR + g(KONU, Fredoka 700, boy) | ≈ 644,6 |
| YK | `Y.HUD["konuTaban"]` − 0,35·boy | ≈ 408,1 (konu satırı orta çizgisi) |
| UK | 0,85 | uçuş ölçek payı (v1 ile aynı) |
| o1, h1, hs1 | (t1x + g1/2, T1 − 0,35·B), (KENAR + UK·gk1/2, YK − ucus_ayrik), UK·gk1/g1 | başlık 1 sol ucu x 60'a iner |
| o2, h2, hs2 | (ORTA, (HAP_UST + HAP_ALT)/2), (KONU_SON − UK·gk2/2, YK + ucus_ayrik), UK·gk2/hap.w | hap sağ ucu KONU_SON'a iner (şef simülasyonu: en dar ara 12,6 px; sol hiza 0,8 px) |

### 4.2 Olay listesi (kare = round(sn × 30); küresel sn = yerel sn)
| # | Olay | sn (kare) | Cümle sözcüğü |
|---|---|---|---|
| 1 | Kapak tam görünür: kanal katmanı, rozet x 60'ta, başlık 2 satır, ev + figür + bavul, etiketler, yer çizgisi | 0,00 (0) | söz öncesi |
| 2 | `YOR` altına sarı el altçizgisi (`strokeDashoffset`, `sine.inOut`) | `alti` 0,30–0,80 (9–24) | söz öncesi |
| 3 | altyazı dilimi açılır | SOZ[0].t0 − 0,05 = 0,95 (29) | İstanbul'da |
| 4 | satır 1 sözcük 1 `İstanbul'da` kırpmayla | 1,00–1,28 (30–38) | İstanbul'da (1,00) |
| 5 | satır 1 sözcük 2 `yaşı-yor-um.` | 1,64–1,92 (49–58) | yaşıyorum. (1,64) |
| 6 | KAPAK KARESİ: uçuş öncesi, satır 1 tam, konu adı yok | 1,97 (59) | — |
| 7 | rozet sağa kayar: x 60 → rz_x | `rozet_kay` 2,00–2,40 | — |
| 8 | sahne grubu (ev, figür, bavul, yer, etiketler) solar | `sahne_sol` 2,00–2,40 | — |
| 9 | uçuş: başlık 1 → konu adının `Simple Present vs` yeri, hap → `Present Continuous` yeri; satırlar DY kadar yukarı | `ucus` 2,00–2,85 | — |
| 10 | satır 2 `Amcamla yaşı-yor-um.` tek süpürme | 2,52–2,90 (76–87) | Amcamla (2,52) |
| 11 | başlıklar solar (2,49–2,67); konu adı açılır (`kunye_ac` 2,62–2,85, `power1.out`) | 2,49–2,85 | — |
| 12 | durgun; son 12 kare geçiş altında | 2,90–3,40 | 2. yaşıyorum. 3,08 → sahne 02 |
Kanal katmanı (`#kanal`) bütün sahne boyunca opaklık 1, konum sabit: ona hiçbir `gsap.set`/`tl.*` YAZMA. Çip kodu (`#ku-cip`) kalkar.

### 4.3 Yerleşim
```
y  291 ┌ [logo 53–247] @ydspublishing (Lexend 42, x 263, taban 330) — 0. kareden son kareye, hareketsiz ┐ kanal 280–350
   386 │ [YDT · TEMEL] kapakta x 60 ─(2,0–2,4)→ x ≈ 665 · konu adı 2,62'den (Fredoka 34, x 60, taban 420)  │ künye 360–450
   472 │ YAŞIYORUM (B ≈ 152, orta 510, kontur 12)       ← uçuşla konu adının sol parçası                │ içerik 460–1380
  ~609 │     ~~~~ sarı altçizgi YOR altında                                                           │
   638 │ ( = İKİ ZAMAN ) sarı hap x 62–958              ← uçuşla konu adının sağ parçası (sağ uç 645)    │
   920 │ İstanbul'da yaşı-yor-um.  Caveat 80, x 84      → uçuşta taban 560 (satır 2: 1040 → 680)        │
  1048 │  I live (252 orta)                       I am living (sağ uç 960, taban ≈ 1136)               │
  1084 │ [ev 108–396]          [figür 540–664] [bavul ≈ 550–712]                                      │
  1372 │ ───────── yer çizgisi 64–956 ─────────                                                        │
  1456 │ altyazı Lexend 500 44, orta x 510, genişlik 900, en çok 2 satır                               │ altyazı 1400–1550
  1570 └ boş zemin                                                                                     ┘
Son hal (2,85+): kanal + konu adı + rozet · satır 1 taban 560 · satır 2 taban 680 · altyazı.
```

### 4.4 Ekran metni, yazı, renk (KOYU hex yaz; hf_tema temaya çevirir)
v1 tablosu aynen geçerlidir (başlık 1 `#bas1t` + `#alti`, hap `#hap`, başlık 2 `#bas2t`, satırlar `#r1`/`#r2` + kırpma `#cr1`/`#cr2`,
etiketler `#etk1`/`#etk2`, `g#eskiz`, bavul örtüsü `#bvd`). Değişen: künye `Y.kunye_svg()` (argümansız), altyazı `Y.altyazi_svg(0.0, Z["sure"], ALT)`,
koordinatlar §4.1. Tek vurgu sarı (altçizgi, hap, rozet). Kırmızı, yeşil, emoji, gradyan, gölge YOK. Ekranda `İstanbul` noktalı İ.
Ekranda "Tam ders", "dakika", süre, QR, "izle" düğmesi YOK.

### 4.5 SVG düzeni ve zaman çizelgesi
- Sıra (alttan üste) v1 ile aynı: `#kapak-sahne` → `#r1` → `#r2` → `#bas2` → `#bas1` → `#kunye` → `#altyazi`.
- 0. kare `gsap.set`: `#ku-konu` opaklık 0; `#rz0` x = KENAR − rz_x; `#alti` dash gizli. (`#ku-ders`, `#ku-cip` satırları kalkar.)
- Uçuş: `uc2("#bas1", o1, h1, hs1)`, `uc2("#bas2", o2, h2, hs2)` v1 gövdesiyle. `#rz0` x → 0 (`rozet_kay`, `power3.inOut`).
  `#kapak-sahne` opaklık → 0 (`sahne_sol`, `power1.in`). `#r1`, `#r2` y → DY (`ucus`, `power3.inOut`). `#ku-konu` opaklık → 1
  (`kunye_ac`, `power1.out`). Bütün tween `immediateRender: false` (`ac()`).
- `veri` sözlüğü v1 alanları + `rz_kayma` = KENAR − rz_x.

### 4.6 Denetimler (`_denetimler()`, assert; ihlalde dur, metinde değer yaz; sabiti kendin değiştirme)
1. B ∈ [140, 190]; başlık 1 ve hap x ∈ [KENAR, SAG]; başlık 1 üstü (T1 − 0,70·B) ≥ `icerikBas`.
2. Satır metinleri ≤ 24 karakter; SOL + g(satır, Caveat 700, 80) ≤ SAG.
3. Kapak dikey sıra (≥ 24 px ara): HAP_ALT → satır 1 üstü (R1_K − 0,864·80); satır 1 altı (R1_K + 0,212·80) → figür üstü ve E1 üstü
   (taban − 0,70·72); E1 tabanı → ev üstü (EV_Y + 3·EV_S); E2 altı (taban + 0,25·72) + 12 ≤ EY; bavul altı (BY + 21·BV_S) ≤ ZEMIN_Y;
   ZEMIN_Y + 2 ≤ `icerikSon`.
4. Yatay: E2 sol (SAG − g(`I am living`)) ≥ figür sağı (FIG_X + (x1 − x0)·fs) + 20; bavul sağı (BX + 18·BV_S) ≤ SAG; E1 sağı < FIG_X;
   ev solu (EV_X + 3·EV_S) ≥ KENAR.
5. Son hal: R1_SON − 0,864·80 ≥ `icerikBas`; R2_SON + 0,212·80 ≤ `icerikSon`; R2_SON − R1_SON == 120.
6. Zaman: v1 maddesi aynı (satır 1 bitişi ≤ kapak_kare/30 − 1/30; u1 ve satir2_son ≤ (kare − 12)/30).
7. Uçuş çakışma örneklemesi: t = u0 … u0 + ud, adım 1/30; power3.inOut / power3.out Python karşılığı (v1 işlevleri); ölçek merkezi o1/o2.
   Kutular: `bas1` [t1x, t1x + g1] × [T1 − 0,70·B, T1 + 0,182·B]; `bas2t` [ORTA − g(BAS2,B)/2, ORTA + g(BAS2,B)/2] × [T2 − 0,921·B, T2];
   `hap` [hap.x, hap.x + w] × [HAP_UST, HAP_ALT]; `rz0` (x KENAR → rz_x, `rozet_kay` ease; y 386–434); `r1` [SOL, SOL + g(satır 1)] ×
   [R1_K − 0,864·80, R1_K + 0,212·80] + DY·ease; `kanal` [60, 602] × [291, 341].
   Çiftler (6 px pay, kesişim = 0): başlıklar opaklık ≥ 0,5 iken (t ≤ baslik_sol[0] + 0,71·baslik_sol[1]): bas1 × hap, bas1 × bas2t,
   bas1 × rz0, hap × rz0, hap × r1, bas1 × kanal, hap × kanal. Bütün uçuş boyunca: r1 × kanal, r1 × [60, 960] × [360, 450] (künye bandı).
   Düşerse t'yi ve çifti yazıp dur.

### 4.7 Çıktı
- `uret() -> str`, `zamanlar() -> dict` (v1 ile aynı anahtarlar: alti, r1, r2, ucus; olay.py okur).
- `__main__`: v1 ile aynı; devir.json alanları: `font` "Caveat", `agirlik` 700, `boy` 80, `kerning` "none", `sol` SOL (84),
  `taban` [R1_SON, R2_SON] = [560, 680], `satir` [iki metin], `yor` [[x0, x1], [x0, x1]] (x0 = SOL + g(`İstanbul'da yaşı-` |
  `Amcamla yaşı-`), x1 = x0 + g(`yor`)), `sag` [iki satır sağ ucu], `t` 3.0, `not` "huni v2 (15.11): sahne 02 Y_L1/Y_L2 560/680, SOL = kenar 60 + 24".
- Kök: `data-width="1080" data-height="1920"`, `data-duration` Z.sure, `data-fps` 30; `#sahne` viewBox `0 0 1080 1920`.

## 5. Kabul ölçütü (şef koşar)
1. `cd S && /usr/bin/python3 uret.py && /usr/bin/python3 olay.py` çıkış 0; assert yok; `olaylar.json` 6 olay, hepsi kare < 90.
2. `proje/index.html`: `#kunye` içinde `#kanal` (`#logoimg` + `#kanal-yazi`), `#ku-konu`, `#rz0`; `#ku-cip`, `#ku-ders` YOK; `#kanal`'a tween YOK.
3. `cd K && bash araclar/qa-yerel.sh 02-04-ydt-temel-s1 01-hyperframes-kapak 0.00,1.50,2.95 1.50 --hazirla` çıkış 0.
4. `node araclar/cakisma-kapisi.mjs 02-04-ydt-temel-s1 --sahne 01-hyperframes-kapak --port 41333 --sunucu 41022` çıkış 0, 0 uyarı.
5. Karelerde: 0–280 ve 1570–1920 boş; x 960–1080'de içerik yok; kanal katmanı her karede aynı yer ve boyda.
