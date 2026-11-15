# SPEC — 02-04-ydt-temel-s2 · sahne 01-hyperframes-kapak (HyperFrames, 1080×1920, 97 kare)

Kaynak: `BRIEF-S2.md` ("Sahneler" satır 01, "Sahne içeriği" 0,00–2,84 ve DİKKAT, "Kapak"), `uretim-tutanagi/kapak-taslak.md` §1–§3,
`uretim-tutanagi/senaryo-taslak.md` §2, `../present-continuous-dikey/BRIEF-DIKEY.md` §0, §2, §3. Yazan: şef (15.11.2026).
Bu belge tasarım verir; tam kod içermez. K = `/home/sef/01dev/_worktrees/kalem-0204`.
D = `K/projeler/02-04-ydt-temel-s2/sahneler/01-hyperframes-kapak/` (bu sahne dizini).

## 1. Dosyalar

| Dosya | Durum | İş |
|---|---|---|
| `D/uret.py` | YOK | §3'e göre yaz (agy, tek ajan) |
| `D/yardim.py` | VAR (S1 sahne 01 birebir kopyası) | DOKUNMA; `import yardim as Y` |
| `D/olay.py`, `D/calistir.sh`, `D/zamanlar.json`, `D/nesneler.json`, `D/cizim/*` | VAR (şef yazdı) | DOKUNMA |

Yalnız `D/uret.py` yazılır. Başka dosyaya dokunma. Silme yok. Test, render, git yok. Betik koşma yok (şef koşar).
Python: girinti 4 boşluk, satır ≤ 120, yeni işlevlerde tip ipucu. Çalıştırma `/usr/bin/python3 uret.py` (`-I` YOK; fontTools
kullanıcı site-packages'ta).

## 2. Kalıp kaynağı (salt oku)

| Kalıp | Mutlak yol | Ne alınır |
|---|---|---|
| Ana iskelet (aynı paket ailesi, aynı motor, dikey kapak) | `K/projeler/02-04-ydt-temel-s1/sahneler/01-hyperframes-kapak/uret.py` | modül düzeni (okuma → sabitler → `_denetimler()` → `zamanlar()` → `uret()` → `__main__`), HTML iskeleti (`#root` data-*, `#sahne` svg, `<defs>` clip), `ac()`, kırpma ile yazım (`#crN` genişlik tween'i), `uc2()` uçuş (svgOrigin BİR KEZ `gsap.set`, `smoothOrigin: false`; tween'ler yalnız x/y/scale/opacity), çip/ders gizleme, `window.__timelines["main"]`, uçuş çakışma örneklemesi (§4.7.7 kalıbı), devir.json yazımı |
| Künye/altyazı yardımcıları | `D/yardim.py` | `Y.genislik`, `Y.font_css`, `Y.font_kopyala`, `Y.ZEMIN_CSS`, `Y.zemin_html`, `Y.kunye_svg`, `Y.rozet_konumu`, `Y.altyazi_satirlari`, `Y.HUD`, `Y.RENK`, `Y.W`, `Y.H` |

## 3. `uret.py`

### 3.1 Okuma
- `Z = D/zamanlar.json`: fps 30 · kare 97 · sure 3,24 · `neq` [0,30, 0,50] · `rozet_kay` [2,18, 0,36] · `sahne_sol` [2,24, 0,30] ·
  `ucus` [2,24, 0,58] · `ucus_olcek` 0,40 · `baslik_sol` [2,50, 0,16] · `kunye_ac` [2,62, 0,20] · `soru` [2,42, 0,36] (QA tur 1: 2,82 sonu 2,8 karesinde `mı?` kesikti) ·
  `karaoke_son` 2,80 · `kapak_kare` 27. Değerleri koda gömme; hep `Z[...]` oku.
- `SOZ` = `ORTAK/anlatim/sozcukler.json` içinde `cumle == 1` sözcükler (ORTAK = `AD.parent.parent / "ortak"`).
  Assert: sözcükler `["Genel", "mi,", "şu", "an", "mı?"]` (5 adet). Zaman dosyadan okunur (sahne 01: küresel sn = yerel sn).
  Şu an: Genel 1,00–1,40 · mi, 1,48–1,92 · şu 2,12–2,24 · an 2,28–2,44 · mı? 2,52–2,92.
- `ALT` = `ORTAK/anlatim/altyazi.json`; `ALT[0]` metni `Genel mi, şu an mı?` olmalı (assert), `cumle == 1`.
- `FIG` = `D/cizim/ogretmen.json`: `kutu` [x0, y0, x1, y1] = [−16,0, 65,1, 1283,7, 2669,0], `parmak` [x, y], `govde_sag` (bel altı
  gövdenin sağ sınırı, kit x), `yollar` [{parca: govde|sac|yuz, d}]. Yollar mutlak M/L/C; SVG `path d` olarak aynen yazılır.
- `GY` = `D/cizim/giysi.json`: `mont` ve `tisort`, her biri `izgara` [UW, UH], `darbeler`, `aski`. Darbe türleri:
  `{"n": [[x, y], …]}` düz çoklu çizgi · `{"n": […], "egri": true}` yumuşak · `{"daire": [cx, cy, r]}`. Koordinatlar ızgara birimi.

### 3.2 Darbe → SVG (yeni işlev `darbe_svg(d: dict) -> str`, ızgara biriminde)
- düz: `M x0 y0 L x1 y1 L …` → `<path d="…"/>`.
- egri, 3 nokta: `M p0 Q p1 p2`; 4 nokta: `M p0 C p1 p2 p3`; daha çok nokta: `M p0`, sonra her iç nokta için `Q p_i mid(p_i, p_i+1)`,
  sonda `L p_son`.
- daire: `<circle cx cy r/>`.
Gruplar `fill="none"` miras alır (üst `g#eskiz`); çizgi kalınlığı grup özniteliği (`stroke-width` = ekran kalınlığı / ölçek).

### 3.3 Sabitler ve türetilen ölçüler (px; g(m, aile, ağırlık, boy) = `Y.genislik`)
| Ad | Değer | Not |
|---|---|---|
| KENAR | `Y.HUD["kenar"]` = 48 | |
| BAS1, BAS2 | `GENEL`, `ŞU AN` | hap yazısı `ŞU AN`; `≠` yazı DEĞİL, kalem çizimi (Fredoka'da U+2260 yok) |
| PAD, NEQ_W, GAP | 0,20·B, 0,50·B, 0,20·B (QA tur 1: 0,12·B bitişik okundu) | hap iç boşluğu (her yan), `≠` kutusu genişliği, `≠` ile yazı arası |
| B | floor(min(190, 952 / g(BAS1, Fredoka 700, 1), 952 / (g(BAS2, Fredoka 700, 1) + 0,50 + 0,20 + 0,40))) | ölçüm: 190 (üst sınır); motor ölçer, elle yazılmaz; assert 150 ≤ B ≤ 190 |
| g1, t1x | g(BAS1, Fredoka 700, B) ≈ 601, (W − g1)/2 ≈ 239 | başlık 1 sola dayalı (text-anchor yok) |
| T1 | 375 + 0,70·B = 508 | başlık 1 tabanı (büyük harf üstü 375) |
| HAP_UST, T2, HAP_ALT | T1 + 0,18·B, HAP_UST + 0,92·B, T2 + 0,28·B | ≈ 542, 717, 770 |
| hap | w = NEQ_W + GAP + g(BAS2, B) + 2·PAD ≈ 732, x = (W − w)/2 ≈ 174, rx = (HAP_ALT − HAP_UST)/2 | assert x ≥ 64, x + w ≤ 1016 |
| NX | hap.x + PAD | `≠` kutusunun sol kenarı (≈ 212) |
| BX2 | NX + NEQ_W + GAP | `ŞU AN` yazısının sol kenarı (text-anchor start, ≈ 330) |
| ZEMIN_Y | 1376 | yer çizgisi (x 64–1016) |
| FIG_H, fs | 500, FIG_H / (y1 − y0) | figür ekran yüksekliği 500 (BRIEF-DIKEY 420–560) |
| FIG_X | 540 − ((x0 + govde_sag)/2 − x0)·fs | gövde ortası x 540 (kol sağa taşar); ≈ 456, figür x ≈ 456–706, y 876–1376 |
| PX, PY | FIG_X + (parmak.x − x0)·fs, (ZEMIN_Y − FIG_H) + (parmak.y − y0)·fs | parmak ucu ≈ (706, 1010) |
| GT | 900 | iki giysinin ızgara y = 0 hattı |
| KM, MX | 2,3, 200 | mont ölçeği ve merkez x: x = MX − 50·KM … MX + 50·KM (≈ 85–315), y GT … GT + 117·KM (≈ 1169) |
| KT, TX | 2,6, 880 | tişört ölçeği ve merkez x: ≈ 750–1010, y GT … GT + 88·KT (≈ 1129) |
| LB | 1252 | iki etiketin tabanı |
| SOL, SORU, SORU_B, SORU_T | 48, `Genel mi, şu an mı?`, 80, 440 | soru satırı: Caveat 700 80, sol 48, taban 440 (= sahne 02 kare 0) |
| ALT_Y | `Y.HUD["altyaziBas"]` + 84 = 1484 | altyazı tek satır tabanı (kunye.js `altyaziCiz` ile aynı) |
| hs | 56 / B | uçuş hedef ölçeği: başlık yazısı ders adı boyuna (56) iner |

### 3.4 Olay listesi (kare = round(sn × 30); küresel sn = yerel sn)
| # | Olay | sn (kare) | Cümle sözcüğü |
|---|---|---|---|
| 1 | Kapak tam görünür: logo (HUD sol üst), rozet `YDT · BASIC` x 48'de, `GENEL`, sarı hap + `ŞU AN` (`≠` yeri boş), mont + askı, figür, tişört + askı, `wears`, `is wearing`, yer çizgisi | 0,00 (0) | söz öncesi |
| 2 | `≠` hapın içinde kalemle: üst çubuk → alt çubuk → eğik çizgi (`Y.cizgi_zamanlari` ile uzunluğa orantılı, toplam `neq`; `strokeDashoffset`, `sine.inOut`) | 0,30–0,80 (9–24) | söz öncesi |
| 3 | KAPAK KARESİ: `≠` bitmiş, altyazı yok, çip yok, ders adı yok | 0,90 (27) | — |
| 4 | altyazı sözcük zamanlı: her sözcük kendi t0 − 0,05'te açılır (`tl.set` opaklık 1); okunan sözcüğün altına sarı karaoke çizgisi t0 → min(t1, sonraki t0 − 0,04, `karaoke_son`) | Genel 0,95 · mi, 1,43 · şu 2,07 · an 2,23 · mı? 2,47 | sözcükler (1,00 · 1,48 · 2,12 · 2,28 · 2,52) |
| 5 | rozet sağa kayar: x 48 → `Y.rozet_konumu()[0]` (`power3.inOut`) | `rozet_kay` 2,18–2,54 | — |
| 6 | sahne grubu (`#kapak-sahne`: yer, mont, figür, tişört, etiketler) solar (`power1.in`) | `sahne_sol` 2,24–2,54 | — |
| 7 | uçuş: `#bas1` (GENEL) → ders adı 1. satır; `#bas2` (hap + `≠` + ŞU AN) → ders adı 2. satır (§3.7) | `ucus` 2,24–2,82 | — |
| 8 | soru satırı `Genel mi, şu an mı?` kırpmayla yazılır (`#crs` genişliği 0 → g(SORU) + 24, `ease: "power1.in"`; hap altından geçerken yazı arkada kalır) | `soru` 2,42–2,78 (73–83) | şu an mı? (2,12–2,92) |
| 9 | başlıklar solar (`baslik_sol` 2,50–2,66, `power1.in`); ders adı açılır (`kunye_ac` 2,62–2,82, `power1.out`); çip `Hook` açılır (0,20 sn, u1 − 0,22 = 2,60) | 2,50–2,82 | — |
| 10 | durgun (son hal = sahne 02 kare 0); son 12 kare geçiş altında | 2,82–3,24 (85–96) | mı? biter 2,92 |

### 3.5 Yerleşim
```
y   48 ┌ logo 387×96 (0. kareden)                            [Hook] çip 2,60'tan ┐ HUD 0–320
   212 │ SIMPLE PRESENT vs     (ders, 2,62'den)                                  │
   276 │ PRESENT CONTINUOUS    [YDT · BASIC] kapakta x 48 ─(2,18–2,54)→ x ≈ 670  │
   375 │        GENEL   (Fredoka 700 B=190, ortalı, kontur 12)   ← uçuşla ders 1 │ içerik 352–1392
   542 │   ( ≠  ŞU AN )  sarı hap x ≈ 174–906, ≠ kutusu x ≈ 212–307 ← ders 2    │
   770 │                                                                         │
 ≈ 843 │   askı kancası          baş 876                      askı kancası       │
   900 │   [mont 85–315]        [figür 456–706, işaret kolu →] [tişört 750–1010]  │
  1169 │   (mont altı)                                         (tişört altı 1129) │
  1252 │     wears                                              is wearing        │ (Caveat 700 72)
  1376 │ ─────────────────────── yer çizgisi 64–1016 ───────────────────────       │
  1484 │                  Genel mi, şu an mı?   (sözcük zamanlı, Lexend 500 44)     │ altyazı 1400–1536
  1536 └ PLATFORM: öğe yok                                                        ┘
Son hal (2,82+): HUD tam (logo, ders 2 satır, rozet, çip Hook) · soru satırı taban 440 (x 48–566) · altyazı tam satır.
```

### 3.6 Ekran metni, yazı, renk (KOYU hex yaz; `ortak/hf_tema.py` temaya çevirir)
| Öğe (ID) | Metin | Yazı / geometri | Renk |
|---|---|---|---|
| başlık 1 `text#bas1t` (grup `#bas1`) | `GENEL` | Fredoka 700 B, x t1x, taban T1, `font-kerning:none`, kontur `stroke="#1b1a17"` 12, `stroke-linejoin="round"`, `paint-order:stroke fill` | `fill="#f3efe6"` |
| hap `rect#hap` (grup `#bas2`) | — | §3.3 | `fill="#f2a93b"` (→ açık `#ffe066`) |
| `≠` `g#neq` (`#bas2` içinde, rect'ten sonra) | — | 3 `path` (id YOK): üst çubuk y T2 − 0,46·B, alt çubuk y T2 − 0,24·B, ikisi x NX + 0,06·B → NX + NEQ_W − 0,06·B, ortası ±3 px dalgalı tek `Q`; kalınlık 0,10·B. Eğik çizgi (NX + 0,74·NEQ_W, T2 − 0,70·B) → (NX + 0,26·NEQ_W, T2 + 0,02·B), kalınlık 0,09·B. Grup: `fill="none" stroke-linecap="round" style="stroke:var(--pilMetin)"` | pilMetin (açık `#1b2440`, koyu `#1b1a17`) |
| başlık 2 `text#bas2t` (`#bas2` içinde) | `ŞU AN` | Fredoka 700 B, x BX2 (text-anchor start), taban T2, `font-kerning:none` | `fill="#1b1a17"` (→ pilMetin) |
| soru `g#soru > text` | `Genel mi, şu an mı?` | Caveat 700 80, x SOL, taban SORU_T, `font-kerning:none`, `clip-path="url(#cps)"` | `fill="#f3efe6"` |
| kırpma `clipPath#cps > rect#crs` | — | x SOL − 12, y SORU_T − 80, h 108, width 0 | — |
| etiket `text#etk1`, `text#etk2` | `wears`, `is wearing` | Caveat 700 72, `text-anchor="middle"`, x MX / TX, taban LB, `stroke="none"` | `fill="#f3efe6"` |
| `g#eskiz` | — | `fill="none" stroke="#f3efe6" stroke-linecap="round" stroke-linejoin="round"` | murekkep |
| yer `path#zc` | — | `M64 1376 L1016 1376`, kalınlık 4 | murekkep |
| mont `g#mont` | — | `transform="translate(MX − 50·KM GT) scale(KM)"`; içinde `g` (darbeler, `stroke-width` 4,0/KM) + `g` (askı, `stroke-width` 3,4/KM) | murekkep |
| tişört `g#tisort` | — | aynı kalıp, TX, KT | murekkep |
| figür `g#fig` | — | `transform="translate(FIG_X − x0·fs  (ZEMIN_Y − FIG_H) − y0·fs) scale(fs)"`; her yol `path` (id f0…), `stroke-width` = parça kalınlığı / fs: gövde 4,4 · saç 3,6 · yüz 2,6 | murekkep |
| künye | `Y.kunye_svg("Hook")` (`KUNYE.cipler["01-hyperframes-kapak"]` = `Hook`) | `#ku-ders`, `#rz0`, `#ku-cip`, `#ku-logo` | yardim.py |
| altyazı `g#altyazi` | `ALT[0].metin` sözcük sözcük | her sözcük `text#aw<i>` (Lexend 500 44, `fill="#f3efe6"`, `style="opacity:0;font-kerning:none"`, taban ALT_Y, text-anchor start). Satır ortalı: x0 = 540 − g(metin, Lexend 500 44)/2; sözcük i'nin x'i = x0 + g(ilk i sözcük + boşluklar). Karaoke `path#ak<i>`: x (sözcük başı − 2) → (sözcük başı + g(sözcüğün sondaki `.,?!:` atılmış hâli) + 2), y ALT_Y + 10, `stroke="#f2a93b"` 5, round cap, `style="opacity:0"` | murekkep / vurgu |

Sıra (alttan üste): `g#kapak-sahne` [`g#eskiz` (zc, mont, tisort, fig) + `#etk1` + `#etk2`] → `#soru` → `#bas2` → `#bas1` → künye → `#altyazi`.
YASAK ID: `rz1`, `t1`, `t2`, `ku-nokta` (hf_tema bunlara özel kural uygular). Tek vurgu = hap + rozet + çip + karaoke çizgisi (aynı sarı).
Kırmızı, yeşil, emoji, gradyan, gölge YOK. Tişört mürekkep çizgi (ana ders `sahne-03.js` ile aynı; pembe dolgu yok: tek vurgu kuralı).
"kanal" sözü, QR, süre YOK. Ekranda `T-shirt` geçmez (bu sahnede yok).

### 3.7 Zaman çizelgesi (S1 kalıbı)
- 0. kare `gsap.set`: `#ku-ders` opaklık 0, `#ku-cip` opaklık 0, `#rz0` x = KENAR − `Y.rozet_konumu()[0]`; `≠` yolları
  `strokeDasharray = L + " " + (L + 2)`, `strokeDashoffset = L` (L = `getTotalLength()`). Bütün tween'ler `immediateRender: false` (`ac()`).
- `≠`: `Y.cizgi_zamanlari([L_üst, L_alt, L_eğik], Z.neq[0], Z.neq[0] + Z.neq[1])` → her yol için `tl.to(strokeDashoffset 0, sine.inOut)`.
  Uzunluklar Python'da düz çizgi boyuyla hesaplanır (`math.hypot`), JS'te `getTotalLength()` ile dash kurulur.
- Altyazı: `tl.set("#aw<i>", {opacity: 1}, t0_i − 0,05)` ve `tl.set(…, {opacity: 0}, min(ALT[0].t1 + 0,35, Z.sure))`;
  karaoke `tl.set("#ak<i>", {opacity: 1}, t0_i)`, `tl.set(…, {opacity: 0}, bitiş_i)`.
- Uçuş `uc2(id, o, h, hs)` (S1 `uc2` birebir; svgOrigin uçuştan önce bir kez `gsap.set`, `smoothOrigin: false`):
  o1 = (t1x + g1/2, T1 − 0,35·B), h1 = (KENAR + hs·g1/2, dersTaban − 0,35·56);
  o2 = (540, (HAP_UST + HAP_ALT)/2), h2 = (KENAR + hs·hap.w/2, dersTaban + dersSatir − hs·(T2 − o2.y)).
  Sonuç: GENEL'in sol ucu x 48'e, tabanı 212'ye; hap sol ucu x 48'e, ŞU AN tabanı 276'ya iner, ikisi de 56 px boyunda.
  x/y `power3.inOut` `ucus[1]`; scale `power3.out` `ucus_olcek`; opaklık → 0 `baslik_sol`, `power1.in`.
  `#rz0` x → 0 (`rozet_kay`, `power3.inOut`). `#kapak-sahne` opaklık → 0 (`sahne_sol`, `power1.in`).
  `#ku-ders` 0 → 1 (`kunye_ac`, `power1.out`). `#ku-cip` 0 → 1 (0,2 sn, u1 − 0,22, `power1.out`).
- Soru: `tl.fromTo("#crs", {attr: {width: 0}}, ac({attr: {width: g(SORU) + 24}, duration: Z.soru[1], ease: "power1.in"}), Z.soru[0])`.

### 3.8 Denetimler (`_denetimler()`, modül yüklenirken; ihlalde dur, sabiti kendin değiştirme, hangi madde düştü yaz)
1. B ∈ [150, 190]; t1x ≥ 64, t1x + g1 ≤ 1016; hap.x ≥ 64, hap.x + hap.w ≤ 1016; T1 − 0,70·B ≥ 352.
2. Hap içi: NX + NEQ_W + 16 ≤ BX2; BX2 + g(BAS2, B) + 0,15·B ≤ hap.x + hap.w; eğik çizgi y aralığı [HAP_UST + 8, HAP_ALT − 8] içinde.
3. Soru: len(SORU) ≤ 24; SOL + g(SORU, Caveat 700, 80) ≤ W − KENAR; SORU_T − 0,864·80 ≥ 352; SORU_T + 0,212·80 + 24 ≤ 1392.
4. Kapak dikey (≥ 24 px ara): HAP_ALT → askı kanca üstü (GT − 22·KM ve GT − 22·KT) ve figür üstü (ZEMIN_Y − FIG_H);
   mont altı (GT + 117·KM) ve tişört altı (GT + 88·KT) → etiket üstü (LB − 0,70·72); etiket altı (LB + 0,25·72) → ZEMIN_Y; ZEMIN_Y ≤ 1392.
5. Yatay: mont sol (MX − 50·KM) ≥ KENAR; tişört sağ (TX + 50·KT) ≤ W − KENAR; mont sağ + 24 ≤ FIG_X; PX + 24 ≤ tişört sol (TX − 50·KT);
   `wears` aralığı (MX ± g/2) ⊂ [KENAR, FIG_X − 24]; `is wearing` sol (TX − g/2) ≥ FIG_X + (govde_sag − x0)·fs + 24 ve sağ ≤ W − KENAR.
6. Altyazı: `Y.altyazi_satirlari(ALT[0].metin)` tek satır; g(metin, Lexend 500 44) ≤ W − 2·KENAR; sözcükler birleşince metne eşit.
7. Zaman: `≠` bitişi (neq toplamı) ≤ kapak_kare/30 − 1/30; ilk altyazı açılışı (SOZ[0].t0 − 0,05) > kapak_kare/30;
   u1, soru bitişi, kunye_ac bitişi, çip bitişi ≤ (Z.kare − 12)/30; kunye_ac[0] ≥ baslik_sol[0] + 0,71·baslik_sol[1].
8. Uçuş çakışma örneklemesi (S1 §4.7.7 kalıbı): t = u0 … baslik_sol[0] + 0,71·baslik_sol[1], adım 1/30; power3.inOut (x/y),
   power3.out (scale, `ucus_olcek` üstünden), power3.inOut (rozet), power1.in = p² (soru kırpması). Kutular:
   `#bas1` [t1x, t1x + g1] × [T1 − 0,70·B, T1 + 0,02·B] (merkez o1 çevresinde ölçekli + kayık); `#bas2` hap kutusu (o2 çevresinde);
   `#rz0` [x, x + rozet_w] × [216, 288]; soru açılan kısmı [SOL, min(SOL + g(SORU), SOL − 12 + genişlik(t))] × [SORU_T − 0,864·80,
   SORU_T + 0,212·80] (genişlik 0 iken yok). Çiftler: bas1 × rz0, bas2 × rz0, bas1 × bas2, bas1 × soru, bas2 × soru; pay 6 px;
   kesişim 0. Düşerse t ve çifti yazıp dur. (Şef ön hesabı: en dar ara bas2 × soru 21 px, t 2,607.)

### 3.9 Çıktı ve arayüz
- `uret() -> str` (index.html metni). Modül düzeyinde `Z`, `SOZ`; `zamanlar() -> dict`:
  `{"neq": [bas, sure], "ucus": [bas, sure], "soru": [bas, sure]}` (olay.py bunu okur; anahtar adları sabit).
- `__main__`: `proje/` yoksa aç; `Y.font_kopyala(AD/"proje"/"assets"/"fonts")`; `proje/index.html` yaz; `D/devir.json` yaz ve tek satır
  `devir: <json>` bas. devir alanları: `font` "Caveat", `agirlik` 700, `boy` 80, `kerning` "none", `sol` 48, `taban` 440,
  `satir` "Genel mi, şu an mı?", `sag` (SOL + g(SORU)), `ust` (SORU_T − 0,864·80), `alt` (SORU_T + 0,212·80), `t` 2.84,
  `altyazi` "cümle 1 tek satır, Lexend 500 44, taban 1484, ortalı".
- Kök: `data-composition-id="main" data-start="0" data-duration="{Z.sure}" data-fps="30" data-width="1080" data-height="1920"`;
  `#sahne` `width="1080" height="1920" viewBox="0 0 1080 1920"`; `<script src="lib/gsap.min.js">`.

## 4. Kabul ölçütü (şef koşar)
1. `cd D && /usr/bin/python3 uret.py && /usr/bin/python3 olay.py` çıkış 0; assert yok; `olaylar.json` 4 olay, hepsi kare < 85.
2. `proje/index.html`: `#kunye` içinde `#ku-ders`, `#rz0`, `#ku-cip`, `#logoimg`; `#bas1`, `#bas2`, `#neq`, `#soru`, `#kapak-sahne`,
   `#mont`, `#tisort`, `#fig`, `#aw0`…`#aw4`, `#ak0`…`#ak4`.
3. `cd K && bash araclar/qa-yerel.sh 02-04-ydt-temel-s2 01-hyperframes-kapak 0.2,0.9,2.5,2.8 0.9 --hazirla` çıkış 0.
4. Kareler: taşma, kesik yazı, üst üste binme, okunmaz kontrast, boş kare YOK; platform bandında öğe YOK; 0,9'da `≠` tam, altyazı yok,
   çip ve ders adı yok; 2,8'de soru satırı tam, HUD tam.
