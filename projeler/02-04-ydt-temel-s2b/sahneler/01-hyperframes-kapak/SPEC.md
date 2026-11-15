# SPEC v2 — 02-04-ydt-temel-s2 · sahne 01-hyperframes-kapak (HyperFrames, 1080×1920, 97 kare) · huni v2

Kaynak: istem D-S2-V2 (15.11.2026), `BRIEF-S2.md` ("Yerleşim", "Sahneler" satır 01, "Sahne içeriği" 0,00–2,84, "Kapak A"),
`dijital-anlatim/.claude/docs/huni-v2-standart.md` §1, §2, §7. Yazan: şef. Bu belge tasarım verir; tam kod içermez.
K = `/home/sef/01dev/_worktrees/kalem-0204`. D = `K/projeler/02-04-ydt-temel-s2/sahneler/01-hyperframes-kapak/`.
v1 yedeği (SPEC, RAPOR, kod): `~/Silinecekler/2026-11-15-huni-v2/02-04-ydt-temel-s2/sahneler/01-hyperframes-kapak/`.

İçerik v1 ile aynıdır (başlık `GENEL` / `≠ ŞU AN`, mont + işaret eden öğretmen + tişört, `wears` / `is wearing`, `≠` kalemi,
altyazı + karaoke, uçuş, soru satırı). Değişen yalnız yerleşim (huni v2 §2) ve künye (kanal katmanı + tek satır konu + rozet; çip YOK).

## 1. Dosyalar

| Dosya | İş | Kim |
|---|---|---|
| `D/yardim.py` | §2'ye göre DÜZENLE (var olan dosya; yalnız künye bölümü değişir) | agy şerit A |
| `D/uret.py` | §3'e göre DÜZENLE (var olan v1 dosya; iskelet kalır, ölçüler/künye/uçuş/denetim değişir) | agy şerit B |
| `D/olay.py`, `D/zamanlar.json`, `D/nesneler.json`, `D/cizim/*` | DOKUNMA (değerler aynı) | — |
| `D/calistir.sh` | şef Edit | şef |

Her şerit yalnız kendi dosyasını yazar. Silme yok. Test, render, git yok. Betik koşma serbest (`/usr/bin/python3 uret.py` yazım denetimi
için), ama `proje/` dışında dosya üretme. Python: girinti 4 boşluk, satır ≤ 120, yeni işlevlerde tip ipucu. Çalıştırma
`/usr/bin/python3` (`-I` YOK; fontTools kullanıcı site-packages'ta).

## 2. `yardim.py` (şerit A) — kanal katmanı + künye

Kalıp kaynağı (salt oku): `K/projeler/02-04-ydt-temel-s2/sahneler/03-hyperframes-cta/SPEC.md` §2 (aynı paket, aynı değerler;
o şerit kendi `yardim.py`'sini yazıyor). Bu dosya onunla birebir aynı künyeyi üretir.

Değişmeyenler (AYNEN): `genislik`, `font_css`, `font_kopyala`, `yol_uzunluk`, `peeps`, `tabler`, `altyazi_satirlari`, `_sar`,
`altyazi_dilimle`, `altyazi_svg`, `zemin_html`, `ZEMIN_CSS`, `cizgi_zamanlari`, `RENK`, `LOGO_EN_BOY`, `LOGO_KAYMA`, `W`, `H`, `AD`, `ORTAK`, `FONT`.

Değişenler:
1. Modül docstring: "02-04-ydt-temel-s2 sahne 01 huni v2: kanal katmanı (y 280–350) + künye (y 360–450); değerler BRIEF-S2.md Yerleşim
   tablosu (S1 ile aynı). Yol verisi, yazı genişliği (fontTools, kerning yok), künye SVG'si, yazı tipi CSS'i."
2. `HUD` sözlüğü (eski `logoY 48`, `dersTaban`, `dersYazi`, `dersSatir`, `rozetY 216`, `rozetH 72`, `rozetAra 24`, `rozetYazi 36`, `cip*`,
   `icerikBas 352`, `icerikSon 1392` ÇIKAR):

| Anahtar | Değer | Anlam |
|---|---|---|
| `kenar` | 48 | YALNIZ altyazı genişliği (W − 2×48 = 984; `ortak/kunye.js` altyaziCiz ile aynı) |
| `logoYuk`, `logoY` | 48, 291 | logo y 291–339; genişlik 48 × `LOGO_EN_BOY` = 193,49 |
| `kanalX`, `kanalTaban`, `kanalYazi` | 263, 330, 42 | `@ydspublishing` Lexend 700 |
| `konuX`, `konuTaban` | 60, 420 | konu sol x ve taban |
| `konuUst`, `konuAlt` | 34, 28 | konu yazı boyu üst / alt sınırı |
| `rozetY`, `rozetH`, `rozetAra`, `rozetYazi`, `rozetDolgu` | 386, 48, 20, 26, 20 | hap y 386–434 rx 24; konu sonu + 20; Lexend 700 26; yazının iki yanı 20 |
| `sagSinir` | 960 | künye ve içerik sağ sınırı |
| `icerikUst`, `icerikAlt` | 460, 1380 | içerik bandı |
| `altyaziBas`, `altyaziYazi`, `altyaziSatir` | 1400, 44, 56 | AYNEN |

3. `DERS` çıkar; `KONU = "Simple Present vs Present Continuous"`; `ROZET = "YDT · BASIC"` kalır.
4. Yeni `konu_boyu() -> int`: `konuUst`'ten `konuAlt`'a inerek ilk tam sayı boy; şart
   `konuX + genislik("Fredoka", 700, KONU, boy) + rozetAra + genislik("Lexend", 700, ROZET, rozetYazi) + 2·rozetDolgu ≤ sagSinir`.
   Hiçbiri sığmazsa `AssertionError`. (Ölçüm: 34'te sağ uç 868,2 → 34.)
5. `rozet_konumu()` yerine `rozet_konumlari() -> list[tuple[float, float]]`: tek öğe `(x, w)`; x = `konuX + genislik(Fredoka 700, KONU,
   konu_boyu()) + rozetAra` (≈ 664,63), w = `genislik(Lexend 700, ROZET, 26) + 2·rozetDolgu` (≈ 203,57).
6. `cip_olcu` ÇIKAR (çip YOK).
7. `kunye_svg() -> str` (PARAMETRESİZ). Çıktı sırası ve kimlikler aynen:
   - `<g id="kunye">` dış grup. İçinde önce `<g id="kanal">` (kanal grubunda `style`, `opacity`, `transform`, sınıf YOK):
     - `<image id="logoimg" href="assets/logo.svg" x="{lx:.2f}" y="291" width="{lw:.2f}" height="48"/>`; `lw = logoYuk × LOGO_EN_BOY`,
       `lx = konuX − lw × LOGO_KAYMA` (= 53,15; görünür sol kenar 60). Kimlik `logoimg` DEĞİŞMEZ (`ortak/hf_tema.py`).
     - `<text id="kanal-ad" x="263" y="330" font-family="Lexend" font-weight="700" font-size="42" fill="#f3efe6">@ydspublishing</text>`.
   - Sonra `<text id="ku-konu" x="60" y="420" font-family="Fredoka" font-weight="700" font-size="{konu_boyu()}" fill="#f3efe6"
     style="font-kerning:none">Simple Present vs Present Continuous</text>`.
   - Sonra `<g id="rz0"><rect x="{x:.1f}" y="386" width="{w:.1f}" height="48" rx="24" fill="#f2a93b"/><text x="{x+w/2:.1f}" y="419"
     text-anchor="middle" font-family="Lexend" font-weight="700" font-size="26" fill="#1b1a17">YDT · BASIC</text></g>`
     (`#f2a93b` rect → `vurguDolgu`, `#1b1a17` yazı → `pilMetin`; çeviri `hf_tema.py`).
   - Dış grup `</g>`. Logo grubu `ku-logo`, ders grubu `ku-ders`, çip `ku-cip` YOK.
   YASAK kimlik: `rz1`, `t1`, `t2`, `ku-nokta` (hf_tema özel kural uygular).

Kabul A: `/usr/bin/python3 -c "import sys; sys.path.insert(0,'D'); import yardim as Y; print(Y.konu_boyu(), Y.rozet_konumlari(), len(Y.kunye_svg()))"`
→ `34 [(664.63…, 203.56…)] …`; çıktıda `id="kanal"`, `id="logoimg"`, `id="kanal-ad"`, `id="ku-konu"`, `id="rz0"` var; `ku-cip` yok.

## 3. `uret.py` (şerit B) — v1 dosyası düzenlenir

v1 iskeleti kalır (okuma → `darbe_svg` → sabitler → `_denetimler()` → `zamanlar()` → `uret()` → `__main__`); `zamanlar()` çıktısı
ve anahtarları aynı (olay.py okur). `yardim.py` arayüzü §2'deki gibidir (şerit A paralel yazar): `Y.HUD`, `Y.konu_boyu()`,
`Y.rozet_konumlari()`, `Y.kunye_svg()` (parametresiz), `Y.KONU`, `Y.ROZET`. `getattr`/`hasattr` geri dönüşleri KALDIR (doğrudan çağır).

### 3.1 Okuma (değişmez)
`Z` (zamanlar.json: neq [0,30, 0,50] · rozet_kay [2,18, 0,36] · sahne_sol [2,24, 0,30] · ucus [2,24, 0,58] · ucus_olcek 0,40 ·
baslik_sol [2,50, 0,16] · kunye_ac [2,62, 0,20] · soru [2,42, 0,36] · karaoke_son 2,80 · kapak_kare 27 · sure 3,24 · kare 97),
`SOZ` (cümle 1: Genel 1,00 · mi, 1,48 · şu 2,12 · an 2,28 · mı? 2,52), `ALT`, `FIG`, `GY`; v1 assert'leri aynı.

### 3.2 Sabitler (px; g(m, aile, ağırlık, boy) = `Y.genislik`). Değerleri koda gömme; formülle türet.
| Ad | Değer (formül) | Ölçüm |
|---|---|---|
| SOL, SAG, UST, ALT_SINIR | 60, `Y.HUD["sagSinir"]` 960, `Y.HUD["icerikUst"]` 460, `Y.HUD["icerikAlt"]` 1380 | içerik bandı |
| B | floor(min(190, 900 / g(BAS1,1), 900 / (g(BAS2,1) + 0,50 + 0,20 + 0,40))) | 190; assert 150 ≤ B ≤ 190 |
| PAD, NEQ_W, GAP | 0,20·B, 0,50·B, 0,20·B | v1 ile aynı |
| g1 | g(BAS1, Fredoka 700, B) | 601,16 |
| t1x | SOL (başlık 1 SOLA YASLI; v1'de ortalıydı) | 60 |
| T1 | UST + 6 + 0,70·B | 599 (GENEL üstü 466) |
| HAP_UST, T2, HAP_ALT | T1 + 0,18·B, HAP_UST + 0,92·B, T2 + 0,28·B | 633,2 · 808 · 861,2 |
| hap | w = NEQ_W + GAP + g(BAS2, B) + 2·PAD; x = SOL (sola yaslı); rx = (HAP_ALT − HAP_UST)/2 | w 747,27, x 60–807,27 |
| NX, BX2 | hap_x + PAD, NX + NEQ_W + GAP | 98, 231 |
| ZEMIN_Y | 1372 | yer çizgisi `M60 1372 L960 1372` |
| FIG_H, fs | 440, FIG_H / (y1 − y0) | fs 0,16898 |
| FIG_X | 400 | figür kutusu sol kenarı (kit x0'ın ekran x'i); gövde 400–547,9 |
| PX, PY | FIG_X + (parmak.x − x0)·fs, (ZEMIN_Y − FIG_H) + (parmak.y − y0)·fs | 619,6 · 1049,6 |
| GT | 944 | iki giysinin ızgara y = 0 hattı |
| KM, MX | 2,1, SOL + 50·KM | 165 → mont ızgara x 60–270, y 944–1189,7, kanca üstü 897,8 |
| KT, TX | 2,4, 830 | tişört x 710–950, y 944–1155,2, kanca üstü 891,2 |
| LB | 1280 | iki etiketin tabanı (Caveat 700 72) |
| SORU, SORU_B, SORU_T | `Genel mi, şu an mı?`, 72, 530 | soru satırı: Caveat 700 72, sol x 60, taban 530 (= sahne 02 kare 0) |
| g_soru | g(SORU, Caveat 700, 72) | 466,27 → x 60–526,27, üst 467,79, alt 545,26 |
| ALT_Y | `Y.HUD["altyaziBas"]` + 84 | 1484 (v1 ile aynı) |
| KS | `Y.konu_boyu()` | 34 |
| hs | KS / B | 0,17895 (başlık yazısı konu boyuna iner) |
| rz_x, rz_w | `Y.rozet_konumlari()[0]` | 664,63 · 203,57 |
| SP, SPV, PC | g("Simple Present", Fredoka 700, KS), g("Simple Present vs ", …), g("Present Continuous", …) | 229,7 · 280,8 · 303,8 |

Uçuş merkezleri (svgOrigin = o; hedef h; ölçek hs):
- o1 = (t1x + g1/2, T1 − 0,35·B) = (360,58, 532,5) → h1 = (SOL + SP/2, 420 − 0,35·KS) = (174,84, 408,1): `GENEL` "Simple Present" üstüne.
- o2 = (hap_x + hap_w/2, (HAP_UST + HAP_ALT)/2) = (433,64, 747,2) → h2 = (SOL + SPV + PC/2, 420 − 0,35·KS + (o2.y − (T2 − 0,35·B))·hs)
  = (492,72, 409,12): hap "Present Continuous" üstüne.

### 3.3 Olay listesi (kare = round(sn × 30); küresel sn = yerel sn)
| # | Olay | sn (kare) | Cümle sözcüğü |
|---|---|---|---|
| 1 | Kapak tam görünür: kanal katmanı (logo + `@ydspublishing`), künye satırında yalnız rozet (x 60), `GENEL`, hap + `ŞU AN` (`≠` yeri boş), mont, figür, tişört, `wears`, `is wearing`, yer çizgisi | 0,00 (0) | söz öncesi |
| 2 | `≠` hapın içinde kalemle: üst → alt → eğik (v1 ile aynı) | 0,30–0,80 (9–24) | söz öncesi |
| 3 | KAPAK KARESİ: `≠` bitmiş, altyazı yok, konu yok | 0,90 (27) | — |
| 4 | altyazı sözcük zamanlı + karaoke çizgisi (v1 ile aynı) | 0,95 · 1,43 · 2,07 · 2,23 · 2,47 | Genel 1,00 · mi, 1,48 · şu 2,12 · an 2,28 · mı? 2,52 |
| 5 | rozet sağa kayar: x 60 → rz_x (`power3.inOut`) | `rozet_kay` 2,18–2,54 | — |
| 6 | `#kapak-sahne` solar (`power1.in`) | `sahne_sol` 2,24–2,54 | — |
| 7 | uçuş: `#bas1` → o1→h1, `#bas2` → o2→h2, ölçek hs (v1 `uc2` birebir) | `ucus` 2,24–2,82 | — |
| 8 | soru satırı kırpmayla yazılır (`power1.in`) | `soru` 2,42–2,78 | şu an mı? |
| 9 | başlıklar solar (`baslik_sol` 2,50–2,66, `power1.in`); konu `#ku-konu` açılır (`kunye_ac` 2,62–2,82, `power1.out`) | 2,50–2,82 | — |
| 10 | durgun (son hal = sahne 02 kare 0: kanal + konu + rozet + soru satırı); son 12 kare geçiş altında | 2,82–3,24 (85–96) | mı? biter 2,92 |

Çip `Hook` ve çip tween'i KALKAR. Kanal katmanı (`#kanal`, `#logoimg`, `#kanal-ad`) hiçbir `gsap.set`/tween'e girmez.

### 3.4 Yerleşim
```
y  280 ┌ (0–280 yalnız zemin)                                                       ┐
   291 │ [logo 53,15–246,6 × 291–339]  @ydspublishing (x 263, taban 330)  ← 0. kareden son kareye sabit
   386 │ [YDT · BASIC] x 60 (kapak) ─(2,18–2,54)→ x 664,6 · konu (x 60, taban 420, 34 px) 2,62'den
   466 │ GENEL  (Fredoka 700 190, x 60, taban 599, kontur 12)       ← uçuşla "Simple Present" üstüne
   633 │ ( ≠  ŞU AN )  sarı hap x 60–807, y 633–861                ← uçuşla "Present Continuous" üstüne
   891 │ kanca          baş 932                                kanca
   944 │ [mont 60–270]  [figür 400–620, işaret kolu → tişört]  [tişört 710–950]
  1280 │   wears                                                  is wearing     (Caveat 700 72)
  1372 │ ───────────────── yer çizgisi 60–960 ─────────────────
  1484 │            Genel mi, şu an mı?  (sözcük zamanlı, Lexend 500 44, ortalı 540)   altyazı 1400–1550
  1570 └ (1570–1920 yalnız zemin)                                                     ┘
Son hal (2,82+): kanal · konu + rozet · soru satırı (x 60–526, taban 530) · altyazı tam satır.
```

### 3.5 Ekran metni, yazı, renk (KOYU hex yaz; `ortak/hf_tema.py` temaya çevirir)
v1 tablosu geçerli; farklar:
- `text#bas1t`: x = t1x (60), taban T1; diğer öznitelikler v1 (Fredoka 700 B, kontur `#1b1a17` 12, `paint-order:stroke fill`).
- `rect#hap` x = 60; `≠` yolları ve `text#bas2t` formülleri v1 (NX, BX2 yeni değerlerle).
- soru `g#soru > text`: Caveat 700 72, x 60, taban 530, `font-kerning:none`, `clip-path="url(#cps)"`, `fill="#f3efe6"`.
- kırpma `clipPath#cps > rect#crs`: x SOL − 12 (48), y SORU_T − SORU_B (458), h 1,35·SORU_B (97,2), width 0.
- etiketler: x MX / TX, taban LB, Caveat 700 72, `text-anchor="middle"`.
- `path#zc`: `M60 1372 L960 1372`, kalınlık 4.
- mont/tişört/figür grupları v1 kalıbı, yeni GT/KM/MX/KT/TX/FIG_X/FIG_H/ZEMIN_Y ile.
- künye: `Y.kunye_svg()` (parametresiz).
- altyazı ve karaoke: v1 ile birebir (ALT_Y 1484, ortalı 540).
Sıra (alttan üste): `g#kapak-sahne` → `#soru` → `#bas2` → `#bas1` → künye → `#altyazi`. YASAK kimlik: `rz1`, `t1`, `t2`, `ku-nokta`.
Tek vurgu = hap + karaoke çizgisi (rozet hapı künye öğesidir). Kırmızı, yeşil, emoji, gradyan, gölge YOK. Ekranda "kanal" sözü
(`@ydspublishing` dışında), `Tam ders`, `dakika`, `dk`, QR, oynat/izle düğmesi YOK.

### 3.6 Zaman çizelgesi (v1 kalıbı; farklar)
- 0. kare `gsap.set`: `#ku-konu` opaklık 0; `#rz0` x = SOL − rz_x (= −604,63); `≠` dash kurulumu v1. (`#ku-ders`, `#ku-cip` YOK.)
- `#rz0` x → 0 (`rozet_kay`, `power3.inOut`). `#ku-konu` 0 → 1 (`kunye_ac`, `power1.out`). Çip satırı SİLİNİR.
- Uçuş `uc2` birebir (svgOrigin bir kez `gsap.set`, `smoothOrigin: false`; x/y `power3.inOut` `ucus[1]`; scale `power3.out` `ucus_olcek`;
  opaklık → 0 `baslik_sol`, `power1.in`), yeni o1/h1/o2/h2/hs ile.
- Soru: `tl.fromTo("#crs", {attr:{width:0}}, ac({attr:{width: g_soru + 24}, duration: Z.soru[1], ease: "power1.in"}), Z.soru[0])`.
- `veri` sözlüğünde `rz_kayma` = SOL − rz_x.

### 3.7 Denetimler (`_denetimler()`, modül yüklenirken; ihlalde dur, sabiti kendin değiştirme, hangi madde düştü yaz)
1. B ∈ [150, 190]; t1x + g1 ≤ SAG; hap_x + hap_w ≤ SAG; max(g1, hap_w) ≤ 900; T1 − 0,70·B ≥ UST.
2. Hap içi (v1): NX + NEQ_W + 16 ≤ BX2; BX2 + g(BAS2, B) + 0,15·B ≤ hap_x + hap_w; eğik çizgi y ∈ [HAP_UST + 8, HAP_ALT − 8].
3. Soru: len(SORU) ≤ 24; SOL + g_soru ≤ SAG; SORU_T − 0,864·72 ≥ UST; SORU_T + 0,212·72 ≤ ALT_SINIR.
4. Dikey (≥ 24 px): HAP_ALT → kanca üstü (GT − 22·KM, GT − 22·KT) ve figür üstü (ZEMIN_Y − FIG_H); mont altı (GT + 117·KM) ve tişört
   altı (GT + 88·KT) → etiket üstü (LB − 0,70·72); etiket altı (LB + 0,25·72) → ZEMIN_Y; ZEMIN_Y ≤ ALT_SINIR.
5. Yatay: mont sol (MX − 50·KM) ≥ SOL; tişört sağ (TX + 50·KT) ≤ SAG; mont sağ (MX + 50·KM) + 24 ≤ FIG_X; PX + 24 ≤ TX − 50·KT;
   `wears` (MX ± g/2) ⊂ [SOL, FIG_X − 24]; `is wearing` sol ≥ FIG_X + (govde_sag − x0)·fs + 24 ve sağ ≤ SAG.
6. Künye: KS ∈ [28, 34]; rz_x + rz_w ≤ SAG; kapakta rozet x = SOL.
7. Altyazı (v1 madde 6 aynen).
8. Zaman (v1 madde 7; çip satırı çıkar): `≠` bitişi ≤ kapak_kare/30 − 1/30; ilk altyazı açılışı (SOZ[0].t0 − 0,05) > kapak_kare/30
   (kapak karesi ve render dalının kare 27'si altyazısız olsun diye); u1, soru bitişi, kunye_ac bitişi ≤ (Z.kare − 12)/30;
   kunye_ac[0] ≥ baslik_sol[0] + 0,71·baslik_sol[1].
9. Uçuş çakışma örneklemesi (v1 madde 8 kalıbı; t = u0 … baslik_sol[0] + 0,71·baslik_sol[1], adım 1/30; pay 6; kesişim 0).
   Kutular: `#bas1` [t1x, t1x + g1] × [T1 − 0,70·B, T1 + 0,02·B], her yana kontur 6 px (ölçekle) eklenir, o1 çevresinde ölçekli + kayık;
   `#bas2` hap kutusu o2 çevresinde; `#rz0` [x(t), x(t) + rz_w] × [386, 434], x(t) = SOL + (rz_x − SOL)·power3.inOut;
   soru açılan kısmı [SOL, min(SOL + g_soru, SOL − 12 + genişlik(t))] × [SORU_T − 0,864·72, SORU_T + 0,212·72] (genişlik 0 iken yok).
   Çiftler: bas1 × rz0, bas2 × rz0, bas1 × bas2, bas1 × soru, bas2 × soru. Şef ön hesabı (en dar ara): bas1 × bas2 24,4 px (t 2,24),
   bas1 × rz0 26,0 (t 2,24), bas1 × soru 27,8 (t 2,607), bas2 × rz0 113,7, bas2 × soru 237,4.

### 3.8 Çıktı
- `uret() -> str`; `zamanlar() -> dict` aynı anahtarlar (`neq`, `ucus`, `soru`).
- `__main__`: v1 gibi; `devir.json` alanları: `font` "Caveat", `agirlik` 700, `boy` 72, `kerning` "none", `sol` 60, `taban` 530,
  `satir` SORU, `sag` round(SOL + g_soru, 2), `ust` round(SORU_T − 0,864·72, 2), `alt` round(SORU_T + 0,212·72, 2), `t` 2.84,
  `altyazi` "cümle 1 tek satır, Lexend 500 44, taban 1484, ortalı"; tek satır `devir: <json>` bas.
- Kök öznitelikleri ve `<script src="lib/gsap.min.js">` v1 ile aynı. Modül docstring: "huni v2" ve "SPEC.md §3" desin.

## 4. Kabul ölçütü (şef koşar)
1. `cd D && /usr/bin/python3 uret.py && /usr/bin/python3 olay.py` çıkış 0; `olaylar.json` 4 olay, hepsi kare < 85.
2. `proje/index.html`: `#kunye` > `#kanal` (`#logoimg`, `#kanal-ad`), `#ku-konu`, `#rz0`; `#bas1`, `#bas2`, `#neq`, `#soru`, `#kapak-sahne`,
   `#mont`, `#tisort`, `#fig`, `#aw0`…`#aw4`, `#ak0`…`#ak4`; `ku-cip`, `ku-ders`, `ku-logo`, `Hook` YOK.
3. `cd K && bash araclar/qa-yerel.sh 02-04-ydt-temel-s2 01-hyperframes-kapak 0.0,1.5,2.8 0.9 --hazirla` çıkış 0.
4. `cd K && node araclar/cakisma-kapisi.mjs 02-04-ydt-temel-s2 --sahne 01-hyperframes-kapak --port 41333 --sunucu 41022` → 0 uyarı.
5. Kareler: taşma, kesik yazı, üst üste binme, okunmaz kontrast, boş kare YOK; 0–280 ve 1570–1920 boş; içerik x ≤ 960;
   kanal katmanı 0,0 / 1,5 / 2,8'de aynı konumda; 0,9'da `≠` tam, altyazı ve konu yok.
