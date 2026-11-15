# SPEC — simple-present-temel-s1 · sahne 01-hyperframes-kanca (huni v2, HyperFrames 1080×1920, 102 kare)

Kaynak: istem D-S1 (15.11.2026), `BRIEF-S1.md` ("Yerleşim", "Kanal katmanı", "Sahne içeriği" 0,00–2,52, "Kapak"),
`D/.claude/docs/huni-v2-standart.md` §1, §2, §6, §7, `uretim-tutanagi/kapak-taslak.md` §2–§3. Yazan: şef (15.11.2026).
Bu belge tasarım verir; tam kod içermez. K = `/home/sef/01dev/_worktrees/kalem-0204`.
S = `K/projeler/simple-present-temel-s1/sahneler/01-hyperframes-kanca/` (bu sahne dizini).
Emsal (huni v2): E = `K/projeler/02-04-ydt-temel-s1/sahneler/01-hyperframes-kapak/` (`uret.py`, `yardim.py`, `SPEC.md`).

## 1. Dosyalar

| Dosya | İş | Kim |
|---|---|---|
| `S/yardim.py` | VAR (E/yardim.py kopyası; KONU ve docstring kuruldu). §3'e göre coco yükleyicisi EKLE. | ajan A |
| `S/uret.py` | YOK. §4'e göre YAZ. Kalıp: `E/uret.py`. | ajan B |
| `S/olay.py`, `S/calistir.sh`, `S/zamanlar.json`, `S/nesneler.json` | VAR. DOKUNMA. | şef |

Her ajan yalnız kendi dosyasını yazar. Başka dosyaya dokunma. Silme yok. Test, render, git, betik koşma yok (şef koşar).
`ortak/`, BRIEF, emsal, ana ders salt okunur. Python: girinti 4 boşluk (var olan dosyalarla uyum), satır ≤ 120, yeni işlevde
tip ipucu. Çalıştırma `/usr/bin/python3 uret.py` (fontTools kullanıcı site-packages'ta; `-I` YOK). A ve B paralel: arayüz §2'de sabit.

## 2. Arayüz (yardim.py → uret.py)

| Ad (yardim.py) | Tür | Değer / davranış |
|---|---|---|
| `HUD`, `KANAL_YAZI`, `ROZET` | — | E ile aynı (değişmez; `ROZET` = `"YDT · BASIC"`) |
| `KONU` | str | `"Simple Present"` |
| `KONU_PARCA` | tuple[str, str] | `("Simple", "Present")` (uçuş hedefi; aradaki tek boşluk KONU'daki boşluktur) |
| `konu_boyu()`, `rozet_konumu()`, `kunye_svg()`, `altyazi_svg(t_bas, sure, liste)` | işlev | E ile aynı |
| `genislik`, `peeps`, `font_css`, `font_kopyala`, `zemin_html`, `ZEMIN_CSS`, `RENK`, `W`, `H` | — | E ile aynı |
| `coco(ad, kutu, azami=25, kisa_atla=0.02) -> list[dict]` | işlev | YENİ (§3): `coco/<ad>.svg` → kutuya oranla sığdırılmış kalem yolları `[{"d", "uz"}]`, `d` = `"M x y L x y …"` ekran px |

## 3. `yardim.py` değişikliği (ajan A)

Kalıp dosya: `K/projeler/simple-present-ileri-dikey/sahneler/01-hyperframes-giris/yardim.py`, satır 208–304
(`# ---- coco (Inkscape) SVG: kalem darbesi yolları ----` başlığı + `_coco_alt_yollar`, `_donusum`, `coco`).

1. Bu üç işlevi başlık yorumuyla birlikte `S/yardim.py` içinde `tabler()` işlevinden SONRA, `# ---- künye` yorumundan ÖNCE ekle.
   Gövdeler kalıpla harfi harfine aynı kalır. Tek fark: `read_text()` → `read_text(encoding="utf-8")`.
2. Tip ipucu ekle: `_coco_alt_yollar(d: str) -> list[tuple[list[tuple[float, float]], bool]]`,
   `_donusum(tr: str) -> tuple[float, float, float, float, float, float]`,
   `coco(ad: str, kutu: list[float] | tuple[float, ...], azami: int = 25, kisa_atla: float = 0.02) -> list[dict]`.
3. Dosyanın başka hiçbir satırına dokunma (`HUD`, `KONU`, `kunye_svg`, altyazı işlevleri, docstring aynı kalır).

## 4. `uret.py` (ajan B)

Kalıp: `E/uret.py`. Şunlar AYNI kalıp ile yazılır: modül başı (`AD`, `sys.path`, `import yardim as Y`), HTML iskeleti
(`<!doctype html>`, `Y.font_css()`, `Y.ZEMIN_CSS`, `#root` öznitelikleri, `Y.zemin_html()`, `<svg id="sahne">`), `ac()`
işlevi, `uc2()` (svgOrigin uçuştan önce BİR KEZ `gsap.set`, `smoothOrigin: false`; tween'de svgOrigin YOK), altyazı aç/kapa
döngüsü, rozet kayışı, konu açılışı, `window.__timelines["main"]`, `__main__` (proje/ + fontlar + index.html + devir.json).
E'deki ev, bavul, öğretmen figürü, etiketler, iki Caveat satırı, altçizgi, `cizim/` okuması BU SAHNEDE YOK.
`getattr`/`hasattr`/`try` yedek dalı yazma: §2 arayüzünü doğrudan kullan.

### 4.1 Okuma
- `Z` = `S/zamanlar.json` (alanlar: fps, kare 102, sure 3.4, soru, soru_nokta, ucus, ucus_olcek, rozet_kay, grup_ucus,
  baslik_sol, kunye_ac, ucus_ayrik, satir_sure, kart_sure, kapak_kare 27).
- `SOZ` = `ortak/anlatim/sozcukler.json` içinde `cumle == 1` olanlar; assert ilk üç sözcük `["Kardeşim", "gider:", "go"]`
  (metinli hata). `ALT` = `ortak/anlatim/altyazi.json`.
- Figür: `gw, gh, FIG = Y.peeps("standing-2", 60)` (gw 213, gh 733). Otobüs: `BUS = Y.coco("bus", BUS_KUTU)`.

### 4.2 Sabitler ve türetilen ölçüler (px; g(m, aile, ağırlık, boy) = `Y.genislik`; ≈ değerler şef ölçümü)
| Ad | Değer | Not |
|---|---|---|
| KENAR, SAG, ORTA | `HUD["kenar"]` 60, `HUD["sagSinir"]` 960, (KENAR + SAG)/2 = 510 | |
| BAS1, BAS2, BAS2_TAM | `"GO mu,"`, `"GOES mu"`, BAS2 + `"?"` | `mu` küçük harf |
| PAD | 0.20 (em) | hap yan payı |
| B | floor(min(190, (SAG−KENAR)/g(BAS1, Fredoka 700, 1), (SAG−KENAR)/(g(BAS2_TAM, Fredoka 700, 1) + 2·PAD))) | ≈ 178 |
| g1, t1x | g(BAS1, Fredoka 700, B), ORTA − g1/2 | ≈ 579,7 / 220,1 |
| TOP1, T1 | 472, TOP1 + 0,70·B | ≈ 596,6 |
| HAP_UST, T2, HAP_ALT | T1 + 0,34·B, HAP_UST + 0,98·B, T2 + 0,26·B | ≈ 657,1 / 831,6 / 877,8 |
| g2, hap_w, hap_x, hap_rx | g(BAS2_TAM, B), g2 + 2·PAD·B, ORTA − hap_w/2, (HAP_ALT − HAP_UST)/2 | ≈ 828,6 / 899,8 / 60,1 |
| t2x | ORTA − g2/2 | ≈ 95,7; `#bas2t` text-anchor START, metin BAS2 (soru işaretsiz) |
| QX, QB | t2x + g(BAS2, B), B/1000 | ≈ 839,6; `?` gliflerinin başlangıcı ve em ölçeği |
| ZEMIN_Y | 1372 | figür ayağı, otobüs tekeri |
| FIG_H, FIG_S, FIG_X, FIG_Y | 440, FIG_H/gh, 120, ZEMIN_Y − FIG_H | ≈ 0,6003; figür x 120–248, y 932–1372 |
| BUS_KUTU | [340, 1135, 600, 233] | coco oranla sığdırır: ekranda x 340–940, y ≈ 1135–1368 |
| G | (80, 932, 870, 442) | kapak sahne grubunun kaynak kutusu (x0, y0, w, h) |
| GK, GT | min(256/870, 140/442), (700, 465) | ≈ 0,29425; küçük grup x 700–956, y 465–595,1 |
| SATIR, SAT_BOY, SAT_X, SAT_TABAN | `"Kardeşim gider:"`, 72, 60, 560 | Caveat 700; ≈ x 60–438 |
| SATIR_BAS | Z.ucus[0] + Z.ucus[1] | 2,45 (uçuş sonu; söylendikten sonra) |
| KART | x 62, y 622, w 376, h 196, rx 28, çizgi 4 | dış kenar x 60–440, y 620–820 |
| KART_YAZI | `"go"`, Fredoka 700 120, x 250 (`text-anchor="middle"`), taban 750 | |
| KART_BAS | SOZ[2]["t0"] | 2,52 (`go` çapası) |
| boy, rz_x, rz_w | `Y.konu_boyu()`, `Y.rozet_konumu()` | ≈ 34 / 309,7 / 203,6 |
| gk1, gk2, KONU_SON | g(KONU_PARCA[0], boy), g(KONU_PARCA[1], boy), KENAR + g(KONU, boy) | ≈ 101,0 / 120,7 / 289,7 |
| YK, UK | `HUD["konuTaban"]` − 0,35·boy, 0,85 | ≈ 408,1 |
| o1, h1, hs1 | (t1x + g1/2, T1 − 0,35·B), (KENAR + UK·gk1/2, YK − Z.ucus_ayrik), UK·gk1/g1 | başlık 1 → `Simple` yeri |
| o2, h2, hs2 | (ORTA, (HAP_UST + HAP_ALT)/2), (KONU_SON − UK·gk2/2, YK + Z.ucus_ayrik), UK·gk2/hap_w | hap → `Present` yeri |

### 4.3 Soru işareti yolu (`?`, kalemle çizilir)
Merkez çizgisi em biriminde (ux sağa, uy tabandan yukarı); SVG noktası x = QX + ux·QB, y = T2 − uy·QB:
- kanca `#soru-kanca`: M(85,520) C(85,610) (160,638) (235,638) C(320,638) (385,590) (385,515) C(385,430) (235,415) (235,300) L(235,250)
- nokta `#soru-nokta`: M(235,62) L(235,64)
- ikisi de: `fill="none"`, `stroke-width` = 140·QB (≈ 24,9), `stroke-linecap="round"`, `stroke-linejoin="round"`,
  `style="stroke:var(--pilMetin);opacity:0"` (hf_tema bu değişkeni temaya göre verir; `stroke="#1b1a17"` YAZMA: zemin rengine döner).
- İkisi de `#bas2` grubunun içinde, `#bas2t`'den sonra (hapla birlikte uçar ve küçülür).

### 4.4 Olay listesi (kare = round(sn × 30); küresel sn = yerel sn)
| # | Olay | sn (kare) | Cümle sözcüğü |
|---|---|---|---|
| 1 | Kapak tam görünür: kanal katmanı, rozet x 60, `GO mu,` + hap `GOES mu`, figür + otobüs + zemin çizgisi; etiket yok | 0,00 (0) | söz öncesi |
| 2 | `?` kanca kalemle (`strokeDashoffset` → 0, `sine.inOut`) | `soru` 0,30–0,68 (9–20) | söz öncesi |
| 3 | `?` noktası (aynı yöntem) | `soru_nokta` 0,70–0,80 (21–24) | söz öncesi |
| 4 | KAPAK KARESİ: başlık tam, `?` çizili, altyazı yok | 0,90 (27) | — |
| 5 | altyazı dilimi açılır (cümle 1, tek satır) | SOZ[0].t0 − 0,05 = 0,95 (29) | Kardeşim (1,00) |
| 6 | rozet sağa kayar: x 60 → rz_x (`power3.inOut`) | `rozet_kay` 1,90–2,20 | — |
| 7 | uçuş: başlık 1 → `Simple` yeri, hap → `Present` yeri (`uc2`) | `ucus` 1,90–2,45, ölçek `ucus_olcek` 0,40 | — |
| 8 | figür + otobüs + zemin grubu küçülüp sağ üste iner (x, y, scale aynı `power3.inOut`) | `grup_ucus` 1,90–2,45 | — |
| 9 | başlıklar solar (`power1.in`) · konu adı açılır (`power1.out`) | `baslik_sol` 2,27–2,42 · `kunye_ac` 2,33–2,45 | — |
| 10 | `Kardeşim gider:` kırpmayla soldan yazılır (genişlik 0 → g(SATIR) + 24, `none`) | SATIR_BAS 2,45 + `satir_sure` 0,25 (74–81) | gider: bitti (2,24) |
| 11 | kart `go` girer: y +24 → 0, opaklık 0 → 1 (`power3.out`) | KART_BAS 2,52 + `kart_sure` 0,40 (76–88) | go (2,52) |
| 12 | durgun; son 12 kare geçiş altında | 2,92–3,40 | `mu,` 2,84 → sahne 02 |

Kanal katmanı (`#kanal`) bütün sahne boyunca opaklık 1, konum sabit: ona hiçbir `gsap.set`/`tl.*` YAZMA.

### 4.5 Yerleşim
```
y  291 ┌ [logo 53–247] @ydspublishing (Lexend 42, x 263, taban 330) — 0. kareden son kareye, hareketsiz ┐ kanal 280–350
   386 │ [YDT · BASIC] kapakta x 60 ─(1,90–2,20)→ x ≈ 310 · konu `Simple Present` 2,33'ten (Fredoka 34, taban 420) │ künye
   472 │        GO mu,   (B ≈ 178, orta 510, zemin konturu 12)          ← uçuşla `Simple` yerine         │ içerik 460–1380
   657 │ ( GOES mu? ) sarı hap x 60–960; `?` 0,30–0,80 kalemle               ← uçuşla `Present` yerine      │
   932 │   [figür 120–248]        [otobüs 340–940, ön yüz SOLDA]            ← 1,90–2,45: x 700–956, y 465–595 │
  1372 │   ───── zemin çizgisi 80–950 ─────                                                                  │
  1484 │ altyazı Lexend 500 44, orta x 510, genişlik 900 (cümle 1 tek satır)                                  │ altyazı 1400–1550
  1570 └ boş zemin                                                                                            ┘
Son hal (2,92+): kanal · konu + rozet · `Kardeşim gider:` (x 60, taban 560) · kart `go` (x 60–440, y 620–820)
                 · küçük figür + otobüs (x 700–956, y 465–595) · altyazı.  = sahne 02 kare 0.
```

### 4.6 Ekran öğeleri, renk (KOYU hex yaz; hf_tema temaya çevirir)
| Kimlik | Öğe | Biçim |
|---|---|---|
| `#bas1` > `#bas1t` | BAS1 | x t1x, taban T1, Fredoka 700 B, fill `RENK["murekkep"]`, stroke `RENK["zemin"]` 12, `stroke-linejoin="round"`, `style="font-kerning:none;paint-order:stroke fill"` |
| `#bas2` > `#hap` | hap | rect hap_x, HAP_UST, hap_w, HAP_ALT − HAP_UST, rx hap_rx, fill `RENK["vurgu"]` (açıkta `#ffe066` olur) |
| `#bas2` > `#bas2t` | BAS2 | x t2x (start), taban T2, Fredoka 700 B, fill `RENK["zemin"]` (açıkta pilMetin `#1b2440` olur), `font-kerning:none` |
| `#bas2` > `#soru-kanca`, `#soru-nokta` | `?` | §4.3 |
| `#kapak-sahne` | grup | `fill="none" stroke=RENK["murekkep"] stroke-linecap="round" stroke-linejoin="round"`; içindeki HER path `vector-effect="non-scaling-stroke"` |
| `#kapak-sahne` > `#fig` | figür | `<g id="fig" transform="translate(FIG_X FIG_Y) scale(FIG_S)">`; her yol `<path transform="translate(tx ty)" d=…>`, stroke-width 4 |
| `#kapak-sahne` > `#otobus` | otobüs | `<g id="otobus" transform="translate(1280 0) scale(-1 1)">` (1280 = 2 × BUS_KUTU orta x 640; ön yüz sola, otobüs figüre doğru gider); her `BUS` yolu stroke-width 4.4 |
| `#kapak-sahne` > `#zc` | zemin | `d="M80 1372 L950 1372"`, stroke-width 4 |
| `#satir` | SATIR | x 60, taban 560, Caveat 700 72, fill murekkep, `font-kerning:none`, `clip-path="url(#cps)"`; `<clipPath id="cps"><rect id="crs" x="48" y="488" width="0" height="97"/>` |
| `#kart-go` | kart | rect KART (fill none, stroke murekkep 4) + text KART_YAZI (fill murekkep, `font-kerning:none`) |
| `#kunye` | künye | `Y.kunye_svg()` (argümansız) |
| `#altyazi` | altyazı | `Y.altyazi_svg(0.0, Z["sure"], ALT)` |

Tek vurgu sarı (yalnız hap ve rozet). Kırmızı, yeşil, emoji, gradyan, gölge, etiket YOK. Ekranda "Tam ders", "dakika", süre, QR,
"izle" düğmesi, YouTube logosu YOK. Yasak kimlik: `t1`, `t2`, `rz1`, `ku-nokta`, `ku-cip`, `ku-ders`, `ku-logo`.

### 4.7 SVG sırası ve zaman çizelgesi
- Sıra (alttan üste): `<defs>` (cps) → `#kapak-sahne` → `#satir` → `#kart-go` → `#bas2` → `#bas1` → `#kunye` → `<g id="altyazi">`.
- 0. kare `gsap.set`: `#ku-konu` opaklık 0; `#rz0` x = KENAR − rz_x; `#kart-go` opaklık 0; `#soru-kanca` ve `#soru-nokta`
  için `getTotalLength()` ile dasharray `L (L+2)`, dashoffset L (E'deki `#alti` hazırlığı).
- `?`: `tl.set(opacity 1)` + `tl.to(strokeDashoffset 0, sine.inOut)` kanca `Z.soru`, nokta `Z.soru_nokta`.
- Uçuş: `uc2("#bas1", o1, h1, hs1)`, `uc2("#bas2", o2, h2, hs2)` E gövdesiyle (`Z.ucus_olcek`, `Z.baslik_sol`).
- Grup: `gsap.set("#kapak-sahne", {svgOrigin: "80 932", smoothOrigin: false})` BİR KEZ; sonra aynı başlangıçta üç tween
  x → GT[0] − 80, y → GT[1] − 932, scale → GK; hepsi `Z.grup_ucus`, `power3.inOut`.
- Satır: `tl.fromTo("#crs", {attr:{width:0}}, ac({attr:{width: g(SATIR)+24}, duration: Z.satir_sure, ease:"none"}), SATIR_BAS)`.
- Kart: `tl.fromTo("#kart-go", {y:24, opacity:0}, ac({y:0, opacity:1, duration: Z.kart_sure, ease:"power3.out"}), KART_BAS)`.
- Bütün tween `immediateRender: false` (`ac()`). `veri` sözlüğü: Z, alt, rz_kayma, o1, h1, hs1, o2, h2, hs2, gk (GK), gt (GT),
  satir_bas, satir_w, kart_bas.

### 4.8 Denetimler (`_denetimler()`, assert; ihlalde dur, metinde değer yaz; sabiti kendin değiştirme)
1. B ∈ [140, 190]; hap_x ≥ KENAR − 0,5 ve hap_x + hap_w ≤ SAG + 0,5; t1x ≥ KENAR ve t1x + g1 ≤ SAG; T1 − 0,70·B ≥ `icerikBas`;
   HAP_ALT ≤ 900 (kapak başlık bandı).
2. `?` kutusu (§4.3 noktaları ± stroke-width/2): sol ≥ QX, sağ ≤ hap_x + hap_w − 8, üst ≥ HAP_UST + 8, alt ≤ HAP_ALT − 8.
3. Karakter sayısı ≤ 24: BAS1, BAS2_TAM, SATIR. SAT_X + g(SATIR, Caveat 700, 72) + 24 ≤ GT[0].
4. Kapak dikey ve yatay: HAP_ALT + 24 ≤ FIG_Y; ZEMIN_Y + 2 ≤ `icerikSon`; FIG_X + gw·FIG_S + 24 ≤ BUS_KUTU[0];
   BUS_KUTU[0] + BUS_KUTU[2] ≤ SAG − 16; `BUS` yollarının ekran kutusu BUS_KUTU içinde (±1 px).
5. Son hal: GT[1] ≥ `icerikBas`; GT[1] + G[3]·GK ≤ 600; GT[0] ≥ 700; GT[0] + G[2]·GK ≤ SAG; satır üstü (560 − 0,864·72)
   ≥ `icerikBas`; satır altı (560 + 0,212·72) + 24 ≤ 620; KART dış kenarı (60–440, 620–820) içerik bandında ve 440 + 24 ≤ GT[0].
6. Zaman: soru_nokta sonu ≤ kapak_kare/30 − 1/30; soru başı ≥ 0,25 ve soru_nokta sonu < SOZ[0].t0; SATIR_BAS ≥ SOZ[1].t1;
   KART_BAS == SOZ[2].t0; uçuş, grup, satır, kart, konu açılışı sonları ≤ (kare − 12)/30.
7. Uçuş çakışma örneklemesi (E §4.6 madde 7 yöntemi; t = ucus[0] … ucus[0] + ucus[1], adım 1/30; `power3.inOut` /
   `power3.out` Python karşılığı E'deki işlevler). Kutular: `bas1` [t1x, t1x + g1] × [T1 − 0,70·B, T1 + 0,182·B] (merkez o1);
   `hap` [hap_x, hap_x + hap_w] × [HAP_UST, HAP_ALT] (merkez o2); `rz0` (x KENAR → rz_x, `rozet_kay` ease, y 386–434);
   `grup` = G'nin (80, 932) çevresinde GK'ye ölçeklenip GT'ye kayan kutusu (`grup_ucus` ease); `kanal` [60, 602] × [291, 341];
   künye bandı [60, 960] × [360, 450]. Çiftler (6 px pay, kesişim = 0): başlıklar opak ≥ 0,5 iken
   (t ≤ baslik_sol[0] + 0,71·baslik_sol[1]): bas1 × hap, bas1 × rz0, hap × rz0, grup × bas1, grup × hap, bas1 × kanal,
   hap × kanal. Bütün uçuş boyunca: grup × rz0, grup × kanal, grup × künye bandı. Düşerse t'yi ve çifti yazıp dur.
   (Şef simülasyonu bu değerlerle 0 çakışma buldu.)

### 4.9 Çıktı
- `uret() -> str`; `zamanlar() -> dict` = `{"soru": Z.soru, "ucus": Z.ucus, "satir": [SATIR_BAS, Z.satir_sure],
  "kart": [KART_BAS, Z.kart_sure]}` (olay.py okur).
- Kök: `data-composition-id="main" data-start="0" data-duration=Z.sure data-fps="30" data-width="1080" data-height="1920"`;
  `#sahne` viewBox `0 0 1080 1920`.
- `__main__`: `proje/` ve `proje/assets/fonts` (`Y.font_kopyala`), `proje/index.html`, `devir.json` (ensure_ascii False, indent 2):
  `satir` {metin, font "Caveat", agirlik 700, boy 72, x 60, taban 560, sag}, `kart_go` {x 60, y 620, w 380, h 200, rx 28, cizgi 4,
  metin "go", font "Fredoka", agirlik 700, boy 120, orta_x 250, taban 750}, `grup` {kutu [GT[0], GT[1], G[2]·GK, G[3]·GK], olcek GK,
  kaynak G, figur_kutu (FIG kutusunun küçük hâli), otobus_kutu (BUS_KUTU'nun küçük hâli), cizgi_px {figur 4, otobus 4.4, zemin 4},
  otobus_ayna true, figur "open-peeps/standing-2", otobus "coco/bus"}, `konu` {metin, boy, x 60, taban 420}, `rozet` {x, w},
  `t` 3.0, `not` "huni v2 (15.11): sahne 02 kare 0 = bu son hal". Sayılar 2 basamak yuvarlanır. devir'i yazdır (`print`).

## 6. Ek (tur 2, şef 15.11): altyazı karaokesi — `yardim.py` (ajan C)

Gerekçe: istem "Altyazı + karaoke 1400–1550"; aynı paketin 03 ve 04 sahneleri okunan sözcüğe sarı altçizgi çizer, bu sahne çizmiyordu.
Kalıp: `K/projeler/simple-present-temel-s1/sahneler/03-hyperframes-kaydet/yardim.py` işlevleri `altyazi_cumleleri` (satır ≈ 235–254) ve
`altyazi_svg` (satır ≈ 263–346, karaoke altçizgili sürüm).

1. `S/yardim.py` içine kalıptaki `altyazi_cumleleri` işlevini EKLE (gövde aynı; tek fark `read_text(encoding="utf-8")`). Konum:
   `altyazi_dilimle` işlevinden sonra.
2. `S/yardim.py` içindeki `altyazi_svg` işlevini kalıptaki karaoke sürümüyle DEĞİŞTİR. İmza ve dönüş kalıpla aynı:
   `altyazi_svg(t_bas: float, sure: float, liste: list[dict]) -> tuple[str, list[list], list[list]]` → `(svg, zaman, karaoke)`.
   Uyarlamalar (yalnız bunlar):
   - HUD anahtarı `altyaziEn` → `HUD["altyaziGen"]`, `altyaziMerkez` → `HUD["altyaziOrta"]` (bu dosyanın HUD'u; HUD'a anahtar ekleme).
   - Sözcük süzgeçlerinin üst sınırı `t1 + 0.05` yerine `t1` (sözleşme 15.11 02-04-s2 s08 düzeltmesi: sonraki cümlenin ilk sözcüğü
     karaokeyi düşürmesin); alt sınır `t0 - 0.05` aynı kalır. Bu değişiklik `altyazi_cumleleri` içindeki süzgece de uygulanır.
   - `read_text()` → `read_text(encoding="utf-8")`.
   - Kalan her şey kalıpla aynı: satır `text-anchor="start"`, x = orta − satır eni/2, x 60–960 assert'i, altçizgi `<line id="ak<i>_<j>">`
     y = taban + 12, `stroke=RENK["vurgu"]` 6 px, `style="opacity:0"`, son sözcüğün kapanışı `min(t1 − t_bas + 0,25, parça kapanışı)`.
3. Son satır tabanı denetimi kalsın: `son_taban + 0.25 * HUD["altyaziYazi"] <= HUD["altyaziSon"]` (assert, metinli).
4. Dosyanın başka satırına dokunma (`altyazi_satirlari`, `_sar`, `altyazi_dilimle`, `coco`, künye aynı kalır).
`uret.py` bağlantısı (3 değer açma, `veri["karaoke"]`, 03-kaydet `uret.py`'deki `V.karaoke.forEach` döngüsü) şef Edit'idir; ajan C yazmaz.

## 5. Kabul ölçütü (şef koşar)
1. `cd S && /usr/bin/python3 uret.py && /usr/bin/python3 olay.py` çıkış 0; assert yok; `olaylar.json` 4 olay, hepsi kare < 90.
2. `proje/index.html`: `#kunye` içinde `#kanal` (`#logoimg` + `#kanal-yazi`), `#ku-konu`, `#rz0`; `#kanal`'a tween YOK.
3. `cd K && bash araclar/qa-yerel.sh simple-present-temel-s1 01-hyperframes-kanca 0.00,1.50,2.95 1.50 --hazirla` çıkış 0.
4. `node araclar/cakisma-kapisi.mjs simple-present-temel-s1 --sahne 01-hyperframes-kanca --port 41333 --sunucu 41022` çıkış 0, 0 uyarı.
5. Karelerde: 0–280 ve 1570–1920 boş; x 960–1080'de içerik yok; kanal katmanı her karede aynı yer ve boyda.
