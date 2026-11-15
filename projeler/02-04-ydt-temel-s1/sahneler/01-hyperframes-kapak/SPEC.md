# SPEC — 02-04-ydt-temel-s1 · sahne 01-hyperframes-kapak (HyperFrames, 1080×1920, 102 kare)

Kaynak: `BRIEF-S1.md` ("Sahneler" satır 01, "Sahne içeriği" 0,00–3,00, "Kapak"), `uretim-tutanagi/kapak-taslak.md`,
`uretim-tutanagi/S1-duzeltme.md` madde 1, `../present-continuous-dikey/BRIEF-DIKEY.md` §0, §2, §3. Yazan: şef (15.11.2026).
Bu belge tasarım verir; tam kod içermez. K = `/home/sef/01dev/_worktrees/kalem-0204`.
D = `K/projeler/02-04-ydt-temel-s1/sahneler/01-hyperframes-kapak/` (bu sahne dizini).

## 1. Dosyalar

| Dosya | Durum | İş |
|---|---|---|
| `D/yardim.py` | VAR (örnek `present-continuous-ileri-s1/.../01-hyperframes-kapak/yardim.py` birebir kopyası) | §3'e göre değiştir (ajan A) |
| `D/uret.py` | YOK | §4'e göre yaz (ajan B) |
| `D/olay.py` | YOK | §5'e göre yaz (ajan C) |
| `D/calistir.sh`, `D/zamanlar.json`, `D/nesneler.json`, `D/cizim/*` | VAR (şef yazdı) | DOKUNMA |

Her ajan yalnız kendi dosyasını yazar. Başka dosyaya dokunma. Silme yok. Test, render, git yok. Betik koşma yok (şef koşar).
`ortak/`, BRIEF, ana ders, dikey paket, örnek sahne salt okunur. Python: girinti 4 boşluk (kopya kalıpla uyum), satır ≤ 120,
yeni işlevlerde tip ipucu. Çalıştırma `/usr/bin/python3 uret.py` (fontTools kullanıcı site-packages'ta; `-I` YOK).

## 2. Kalıp kaynakları (salt oku)

| Kalıp | Mutlak yol | Ne alınır |
|---|---|---|
| Ana iskelet (aynı motor, dikey kapak) | `K/projeler/present-continuous-ileri-s1/sahneler/01-hyperframes-kapak/uret.py` | HTML iskeleti (`#root` data-* öznitelikleri, `#sahne` svg, `<defs>` clip), `darbe()`, `ac()`, kırpma ile yazım (`#crN` genişlik tween'i), `uc2()` uçuş kalıbı (svgOrigin + x/y `power3.inOut`, scale `power3.out` 0,85·süre, sonda opaklık), altyazı aç/kapa `tl.set`, çip gizleme, `window.__timelines["main"]`, `__main__` |
| Olay kalıbı | `K/projeler/present-continuous-ileri-s1/sahneler/01-hyperframes-kapak/olay.py` | `f = round(t*30)`, kare başına en çok 3 olay kaydırması, sıralama, assert, `olaylar.json` yazımı |
| Künye sayıları (tek otorite) | `K/projeler/02-04-ydt-temel-s1/ortak/kunye.js` | `KUNYE` (satır 55–60), `dersDuzen` + `kunyeCiz` (143–162), `altyaziDilimle` + `altyaziSar` (222–268) |
| Tema dönüşümü | `K/projeler/02-04-ydt-temel-s1/ortak/hf_tema.py` | uret.py KOYU hex yazar; §6 |

## 3. `yardim.py` değişiklikleri (ajan A)

1. Docstring 1. satır: "02-04-ydt-temel-s1 sahne 01; present-continuous-ileri-s1 kopyası, künye S1 HUD'una (kunye.js) çevrildi".
2. `HUD` sözlüğü kunye.js `KUNYE` ile birebir: kenar 48 · logoY 48 · logoYuk 96 · dersTaban 212 · dersYazi 56 · dersSatir 64 ·
   rozetY 216 · rozetH 72 · rozetAra 24 · rozetYazi 36 · cipY 48 · cipH 80 · cipYazi 40 · cipDolgu 64 · icerikBas 352 ·
   icerikSon 1392 · altyaziBas 1400 · altyaziYazi 44 · altyaziSatir 56.
3. `ROZETLER` kalkar. Yerine `DERS = ("SIMPLE PRESENT vs", "PRESENT CONTINUOUS")` ve `ROZET = "YDT · BASIC"`.
4. `rozet_konumlari()` yerine `rozet_konumu() -> tuple[float, float]`: x = kenar + genislik(Fredoka 700, DERS[-1], dersYazi) +
   rozetAra; w = genislik(Lexend 700, ROZET, rozetYazi) + 56 (kunye.js `dersDuzen` + satır 153 ile aynı).
5. `cip_olcu()`: yapı aynı; dolgu `HUD["cipDolgu"]` (64) olur.
6. `kunye_svg(cip)` yeniden: `<g id="kunye">` içinde sırayla
   - `<g id="ku-ders">`: iki `<text>` (x kenar, y = dersTaban + i·dersSatir, Fredoka 700 56, `fill=RENK["murekkep"]`), metin DERS[i];
   - `<g id="rz0">`: `rect` (rozet_konumu x, y rozetY, w, h rozetH, rx rozetH//2, `fill=RENK["vurgu"]`) + `text` (orta, x + w/2,
     y rozetY + rozetH/2 + 13, Lexend 700 36, `fill=RENK["zemin"]`, metin ROZET);
   - `<g id="ku-cip">`: örnekteki çip (rect `ku-cipr` çerçeve 4, text `ku-cipt`), ölçü `cip_olcu()`;
   - `<g id="ku-logo">`: örnekteki `image#logoimg` (x kenar, y logoY, w logoYuk·LOGO_EN_BOY, h logoYuk).
   Yasak ID: `rz1`, `t1`, `t2`, `ku-nokta` (hf_tema bunlara özel kural uygular).
7. `altyazi_cumleleri()` kalkar. Yerine `altyazi_dilimle(liste) -> list[dict]`: kunye.js `altyaziDilimle` (222–258) Python karşılığı.
   Parça `_sar(metin)` (açgözlü satır kırma, Lexend 500 44, genişlik W − 2·kenar, satır birleştirme YOK) ile ≤ 2 satırsa olduğu gibi
   kalır; değilse `ORTAK/anlatim/sozcukler.json`'dan `s["cumle"] == p["cumle"]` ve `p.t0 − 0,06 ≤ s.t0 < p.t1` sözcüklerle dilimlenir
   (sayı tutmazsa karakter oranı), dilim t1 = sonraki dilim t0 − 0,4, son dilim t1 = p.t1. `altyazi_svg()` artık bunu çağırır;
   geri kalanı (aç = t0 − 0,05, kapat = t1 + 0,35 ve sonraki parçanın t0 − 0,05'i, y0 1400 + 84/56, satır 56) aynı.
   Ölçüm: cümle 1 iki satıra sığar (969 / 619 px) → tek dilim; sahne 02 (kunye.js) ile aynı metin görünür.
8. `tabler(ad, kok=None)`: kok None ise `ORTAK/cizim/tabler`, değilse verilen dizin; dosya `<kok>/<ad>.svg`. Düzenli ifade aynı
   (`<path d="…"`; `M0 0h24v24` atılır).
9. Başka işlev değişmez (`genislik`, `font_css`, `font_kopyala`, `yol_uzunluk`, `peeps`, `altyazi_satirlari`, `zemin_html`,
   `ZEMIN_CSS`, `cizgi_zamanlari`, `RENK`, `LOGO_EN_BOY`). `ZEMIN_CSS` dizgileri hf_tema arar; harfi harfine kalır.

## 4. `uret.py` (yeni, ajan B)

### 4.1 Okuma
- `Z = zamanlar.json` (D içinde): fps 30, kare 102, sure 3,4, `alti` [0,30, 0,50], `yazi_cap` 0,28, `satir2_son` 2,90 (QA tur 2: 2,97 iken 2,95 karesinde satır 2 kesikti),
  `ucus` [2,00, 0,85], `ucus_olcek` 0,72, `rozet_kay` [2,00, 0,40], `sahne_sol` [2,00, 0,40], `kunye_ac` [2,62, 0,23], `baslik_sol` [2,49, 0,18], `ucus_ayrik` 16, `kapak_kare` 59 (QA tur 1: çapraz solma kapıda hata verdi; başlık ≥ 0,5 ile ders ≥ 0,5 artık aynı anda yok).
- `SOZ` = `ORTAK/anlatim/sozcukler.json` içinde `cumle == 1` sözcükler. Assert: ilk 4 sözcük
  `["İstanbul'da", "yaşıyorum.", "Amcamla", "yaşıyorum."]`. Zaman dosyadan okunur (sahne 01: küresel sn = yerel sn).
- `ALT` = `ORTAK/anlatim/altyazi.json`. `FIG` = `D/cizim/ogretmen.json` (`kutu` [x0,y0,x1,y1], `el` [x,y], `yollar` [{parca, d}]).
- Ev `Y.tabler("home")`; bavul `Y.tabler("luggage", AD / "cizim")`.

### 4.2 Sabitler ve türetilen ölçüler (px; g(m, aile, ağırlık, boy) = `Y.genislik`)
| Ad | Değer | Not |
|---|---|---|
| KENAR | `Y.HUD["kenar"]` = 48 | |
| BAS1, BAS2 | `YAŞIYORUM`, `= İKİ ZAMAN` | kapak başlığı |
| PAD | 0,20 em | hap yatay iç boşluğu (her yan) |
| B | floor(min(190, 952 / g(BAS1,1), 952 / (g(BAS2,1) + 2·PAD))) | ≈ 161; motor ölçer, elle yazılmaz; assert 150 ≤ B ≤ 190 |
| t1x, g1 | (W − g1)/2, g(BAS1, Fredoka 700, B) | başlık 1 sola dayalı ölçülür (altçizgi için) |
| T1 | 375 + 0,70·B | başlık 1 tabanı (büyük harf üstü 375) |
| ALTI_Y | T1 + 0,20·B | `YOR` altçizgisi orta çizgisi |
| HAP_UST | ALTI_Y + 29 | |
| T2 | HAP_UST + 0,98·B | başlık 2 tabanı (İ noktası 0,921 em) |
| HAP_ALT | T2 + 0,26·B | |
| hap | w = g(BAS2,B) + 2·PAD·B, x = (W − w)/2, rx = (HAP_ALT − HAP_UST)/2 | assert x ≥ 63, x + w ≤ 1017 |
| SOL | 48 | cümle satırları sol kenarı |
| SAT_BOY | 80 | Caveat 700 (BRIEF-DIKEY §3 kanca cümlesi 64–80) |
| R1_K, R2_K | 856, 1004 | kapak konumu tabanları (R2_K = R1_K + 148) |
| R1_SON, R2_SON | 452, 600 | uçuş sonrası = sahne 02 kare 0 |
| DY | R1_SON − R1_K = −404 | iki satıra aynı kayma |
| ZEMIN_Y | 1384 | yer çizgisi |
| EV_S, EV_X, EV_Y | 16, 48, ZEMIN_Y − 21·EV_S | Tabler home (24 ızgara, 3–21): ekranda x 96–384, y 1096–1384 |
| FIG_H, FIG_X | 460, 600 | figür kutusu yüksekliği ve sol kenarı; fs = FIG_H / (y1 − y0); üstü ZEMIN_Y − FIG_H = 924 |
| EX, EY | FIG_X + (el.x − x0)·fs, (ZEMIN_Y − FIG_H) + (el.y − y0)·fs | el noktası ≈ (729, 1168) |
| BV_S, BX, BY | 9, EX + 6 − 12·BV_S, EY − 3·BV_S | bavul (Tabler luggage, 24 ızgara; sap üstü (12, 3) ele oturur) |
| E1 | `I live`: x = EV_X + 12·EV_S (orta), taban EV_Y + 3·EV_S − 36 | Caveat 700 72 |
| E2 | `I am living`: x = W − KENAR (sağa dayalı, `text-anchor="end"`), taban EY − 48 | Caveat 700 72 |

### 4.3 Olay listesi (kare = round(sn × 30))
| # | Olay | sn (kare) | Cümle sözcüğü |
|---|---|---|---|
| 1 | Kapak tam görünür: logo, rozet `YDT · BASIC` (x 48'de), başlık 2 satır, ev + figür + bavul, etiketler, yer çizgisi | 0,00 (0) | söz öncesi |
| 2 | `YOR` altına sarı el altçizgisi kalemle çizilir (`strokeDashoffset`, `sine.inOut`) | `alti` 0,30–0,80 (9–24) | söz öncesi |
| 3 | altyazı dilimi açılır (cümle 1, 2 satır), sahne sonuna kadar | SOZ[0].t0 − 0,05 = 0,95 (29) | İstanbul'da |
| 4 | satır 1, sözcük 1 `İstanbul'da` kırpmayla yazılır | SOZ[0].t0 → + min(t1 − t0, yazi_cap) = 1,00–1,28 (30–38) | İstanbul'da (1,00) |
| 5 | satır 1, sözcük 2 `yaşı-yor-um.` yazılır | SOZ[1].t0 → + yazi_cap = 1,64–1,92 (49–58) | yaşıyorum. (1,64) |
| 6 | KAPAK KARESİ: uçuş öncesi, çip yok, satır 1 tam | 1,97 (59) | — |
| 7 | rozet sağa kayar: x 48 → `rozet_konumu().x` (kunye `dersDuzen` yeri) | `rozet_kay` 2,00–2,40 (60–72) | — |
| 8 | sahne grubu (ev, figür, bavul, yer, etiketler) solar | `sahne_sol` 2,00–2,40 | — |
| 9 | uçuş: başlık 1 → ders adı 1. satır, başlık 2 (hap) → ders adı 2. satır; satır grupları DY kadar yukarı | `ucus` 2,00–2,85 (60–85) | — |
| 10 | satır 2 `Amcamla yaşı-yor-um.` tek süpürmeyle yazılır (satır grubu uçuşla birlikte yerine iner) | SOZ[2].t0 → `satir2_son` = 2,52–2,90 (76–87) | Amcamla (2,52) |
| 11 | başlıklar solar (2,49–2,67), ders adı açılır (2,62–2,85), çip `Hook` açılır (2,63–2,83) | 2,49–2,85 | — |
| 12 | durgun; son 12 kare geçiş altında | 2,90–3,40 (87–101) | 2. `yaşıyorum.` 3,08 → sahne 02 karaokesi |

Not 10: ikinci `yaşıyorum.` 3,08'de söylenir; D-02 "kare 0 = iki satır tam" ister → satır 2 sahne 01'de 2,90'da tamamlanır (RAPOR açık nokta).

### 4.4 Yerleşim
```
y   48 ┌ logo 387×96 (0. kareden)                         [Hook] çip 2,63'ten ┐ HUD 0–320
  ~173 │ SIMPLE PRESENT vs      (ders, 2,60'tan; taban 212)                    │
   216 │ [YDT · BASIC] kapakta x 48 ─(2,0–2,4)→ x ≈ 670  ·  PRESENT CONTINUOUS │
   375 │ YAŞIYORUM  (B ≈ 161, ortalı, kontur 12)              ← uçuşla ders 1  │ içerik 352–1392
  ~520 │     ~~~~~ sarı altçizgi YOR altında                                   │
   549 │ ( = İKİ ZAMAN )  sarı hap, x ≈ 66–1014               ← uçuşla ders 2  │
   856 │ İstanbul'da yaşı-yor-um.   Caveat 80, x 48   → uçuşta taban 452        │
       │  I live                    I am living   (Caveat 72)                   │
  1096 │ [ev 96–384]        [figür 600–743] [bavul ≈ 681–789, 1168–1329]        │
  1384 │ ───────────── yer çizgisi 64–1016 ─────────────                       │
  1456 │ İstanbul'da yaşıyorum. Amcamla yaşıyorum.   (Lexend 500 44)           │ altyazı 1400–1536
  1512 │ Türkçede ikisi de yaşıyorum.                                          │
  1536 └ PLATFORM: öğe yok                                                      ┘
Son hal (2,97+): HUD tam (logo, ders 2 satır, rozet, çip) · satır 1 taban 452 · satır 2 taban 600 · altyazı.
```

### 4.5 Ekran metni, yazı, renk (KOYU hex yaz; hf_tema temaya çevirir)
| Öğe (ID) | Metin | Yazı | Renk (hex → tema) |
|---|---|---|---|
| başlık 1 `text#bas1t` (grup `#bas1`) | `YAŞIYORUM` | Fredoka 700 B, x t1x, taban T1, `font-kerning:none`, kontur `stroke="#1b1a17"` 12, `paint-order:stroke fill` | `#f3efe6` → murekkep |
| altçizgi `path#alti` (`#bas1` içinde) | — | x: t1x + g(`YAŞI`) − 6 → t1x + g(`YAŞIYOR`) + 6; ALTI_Y çevresinde ±5 px dalgalı tek kübik yol; w 10, round cap; 0. karede opaklık 0 | `stroke="#f2a93b"` → vurgu |
| hap `rect#hap` (grup `#bas2`) | — | §4.2 | `fill="#f2a93b"` → vurguDolgu (açık `#ffe066`) |
| başlık 2 `text#bas2t` (`#bas2` içinde) | `= İKİ ZAMAN` | Fredoka 700 B, x 540 `text-anchor="middle"`, taban T2, `font-kerning:none` | `fill="#1b1a17"` → pilMetin (açık `#1b2440`) |
| satır 1 `g#r1 > text` | `İstanbul'da yaşı-yor-um.` | Caveat 700 80, x SOL, taban R1_K, `font-kerning:none`, `clip-path="url(#cp1)"` | murekkep |
| satır 2 `g#r2 > text` | `Amcamla yaşı-yor-um.` | Caveat 700 80, x SOL, taban R2_K, `clip-path="url(#cp2)"` | murekkep |
| kırpma `clipPath#cp1/#cp2 > rect#cr1/#cr2` | — | x SOL − 12, y taban − SAT_BOY, h 1,35·SAT_BOY, width 0 | — |
| etiket `text#etk1`, `text#etk2` | `I live`, `I am living` | Caveat 700 72, §4.2 E1/E2; `stroke="none"` | `fill="#f3efe6"` |
| ev / figür / bavul / yer (`g#eskiz`) | — | `fill="none" stroke="#f3efe6"` round cap/join; kalınlık ekranda: figür gövde 4,4 · saç 3,6 · yüz 2,6 · ev 4,0 · bavul 4,0 · yer 4 (yerel ölçeğe bölünür) | murekkep |
| bavul örtüsü `rect#bvd` (bavul grubunda, çizgilerden önce) | — | yerel x 6, y 6, w 12, h 14, rx 2, `stroke="none"`, `style="fill:var(--zemin)"` (bacağın önünde durur) | zemin |
| künye | `Y.kunye_svg("Hook")` (`KUNYE.cipler["01-hyperframes-kapak"]` = `Hook`) | §3.6 | |
| altyazı `g#altyazi` | `Y.altyazi_svg(0.0, Z["sure"], ALT)` | Lexend 500 44 | murekkep |

Tek vurgu = altçizgi + hap + rozet + çip (aynı sarı). Kırmızı, yeşil, emoji, gradyan, gölge YOK. Ekranda `İstanbul` noktalı İ.
"kanal" sözü, QR, süre ("6 dk") YOK.

### 4.6 SVG düzeni ve zaman çizelgesi
- Sıra (alttan üste): `g#kapak-sahne` [`g#eskiz` (yer `#zc`, ev `#ev`, figür `#fig`, bavul `#bavul` = örtü + yollar) + `#etk1` + `#etk2`] →
  `#r1` → `#r2` → `#bas2` → `#bas1` → künye → `#altyazi`.
- Figür: `g#fig transform="translate(FIG_X − x0·fs  (ZEMIN_Y − FIG_H) − y0·fs) scale(fs)"`; her yol `path` (id f0…), `stroke-width` = parça
  kalınlığı / fs. Ev ve bavul: örnekteki `#ktg` kalıbı (translate + scale, `stroke-width` = 4,0 / ölçek).
- 0. kare durumu `gsap.set` ile: `#ku-ders` opaklık 0, `#ku-cip` opaklık 0, `#rz0` x = KENAR − rozet_konumu().x, `#alti` dash gizli.
  Bütün tween'ler `immediateRender: false` (örnekteki `ac()`).
- Altçizgi: `darbe("alti", Z.alti[0], Z.alti[1])` ama ease `sine.inOut`.
- Satır 1: `#cr1` genişliği sözcük sonlarına (SOL + g(önek) + 8 − (SOL − 12)) kademeli; satır 2: `#cr2` 0 → tam genişlik tek tween, `ease: "none"`.
- Uçuş (`uc2` kalıbı; `svgOrigin` uçuştan önce bir kez `gsap.set` ile, `smoothOrigin: false`; tween'lerde YOK. QA tur 3: tween başına svgOrigin doğrudan aramada x/y'yi kaydırdı): UK = 0,85 (sabit; şef ölçtü: 1,0'da başlık sağ ucu rozete 16 px giriyordu, 0,85'te en yakın ara 44 px).
  o1 = (t1x + g1/2, T1 − 0,35·B), h1 = (KENAR + UK·gd1/2, dersTaban − 0,35·56), hs1 = UK·gd1 / g1;
  o2 = (540, (HAP_UST + HAP_ALT)/2), h2 = (KENAR + UK·gd2/2, dersTaban + dersSatir − 0,35·56), hs2 = UK·gd2 / hap.w;
  gd1, gd2 = g(DERS[0|1], Fredoka 700, 56). Küçülen başlığın sol ucu x 48'e (ders adının başına) iner. x/y `power3.inOut` `ucus[1]`; scale `power3.out` `ucus_olcek`; opaklık → 0 `baslik_sol` [baş, süre],
  `power1.in`. `#ku-ders` opaklık 0 → 1 (`kunye_ac` [baş, süre], `power1.out`). h1 y − `ucus_ayrik`, h2 y + `ucus_ayrik` (QA tur 1: bas1 × bas2 26 px). `#ku-cip` 0 → 1 (0,2 sn, u1 − 0,22'de).
  `#rz0` x → 0 (`rozet_kay`, `power3.inOut`). `#kapak-sahne` opaklık → 0 (`sahne_sol`, `power1.in`). `#r1`, `#r2` y → DY (`ucus`, `power3.inOut`).
- Altyazı: örnekteki `V.alt.forEach` aç/kapa.

### 4.7 Denetimler (uret.py içinde assert; ihlalde dur, sabiti kendin değiştirme)
1. B ∈ [150, 190]; hap ve başlık 1 x ∈ [63, 1017]; başlık 1 üstü (T1 − 0,70·B) ≥ 352.
2. Satır metinleri ≤ 24 karakter; SOL + g(satır, Caveat 700, 80) ≤ W − KENAR.
3. Kapak dikey sıra (≥ 24 px ara): HAP_ALT → satır 1 üstü (R1_K − 0,864·80); satır 1 altı (R1_K + 0,212·80) → figür üstü ve E1 üstü
   (taban − 0,70·72); E1 tabanı → ev üstü (EV_Y + 3·EV_S); E2 altı (taban + 0,25·72) + 12 ≤ bavul sap üstü (EY).
4. Yatay: E2 sol (W − KENAR − g(`I am living`)) ≥ figür sağı (FIG_X + (x1 − x0)·fs) + 20; bavul sağı (BX + 18·BV_S) ≤ W − KENAR;
   E1 sağı < FIG_X.
5. Son hal: R1_SON − 0,864·80 ≥ 352; R2_SON + 0,212·80 ≤ 1392; R2_SON − R1_SON ≥ 1,85·SAT_BOY (sahne 02'nin *yor* kutusuna yer).
6. Zaman: satır 1 yazımı bitişi ≤ kapak_kare/30 − 1/30; bütün hareket bitişi (u1, satir2_son) ≤ (Z.kare − 12)/30 = 3,00.
7. Uçuş çakışma örneklemesi: t = u0 … u1 − 0,11, adım 1/30; Python'da power3.inOut / power3.out ile kutular hesaplanır
   (ölçek merkezleri o1/o2): `#bas1` kutusu [t1x, t1x + g1] × [T1 − 0,70·B, ALTI_Y + 5]; `#bas2` kutusu hap; `#rz0` kutusu
   (rozet_kay ile kayan x, y 216–288); `#r1` kutusu [SOL, SOL + g(satır 1)] × [R1_K − 0,864·80, R1_K + 0,212·80] + DY·ease.
   bas1 × rz0, bas2 × rz0, bas2 × r1 kesişimi (6 px pay) = 0. Düşerse hangi t ve hangi çift olduğunu yazıp dur.

### 4.8 Çıktı ve arayüz
- `uret() -> str` (index.html metni). Modül düzeyinde `Z`, `SOZ`; ayrıca `zamanlar() -> dict`:
  `{"alti": [bas, sure], "r1": [[bas, sure], [bas, sure]], "r2": [bas, sure], "ucus": [bas, sure]}` (olay.py bunu okur).
- `__main__`: `proje/` yoksa aç; `Y.font_kopyala(AD/"proje"/"assets"/"fonts")`; `proje/index.html` yaz; `D/devir.json` yaz ve tek satır
  `devir: <json>` bas. devir alanları: `font` "Caveat", `agirlik` 700, `boy` 80, `kerning` "none", `sol` 48, `taban` [452, 600],
  `satir` [iki metin], `yor` [[x0, x1], [x0, x1]] (x0 = SOL + g(`İstanbul'da yaşı-` | `Amcamla yaşı-`), x1 = x0 + g(`yor`)),
  `sag` [iki satır sağ ucu], `t` 3.0.
- Kök: `data-width="1080" data-height="1920"`, `data-duration` = Z.sure, `data-fps` 30; `#sahne` `viewBox="0 0 1080 1920"`.

## 5. `olay.py` (yeni, ajan C)
`import uret as U` (örnekteki gibi `sys.path`). `zz = U.zamanlar()`, `f = round(t * 30)`. Olaylar:
| kare | tür | güç |
|---|---|---|
| f(zz["alti"][0]) | `cizgi` | 0,6 |
| f(zz["r1"][0][0]), f(zz["r1"][1][0]) | `hisirti` | 0,45 |
| f(zz["ucus"][0]) | `parilti` | 0,5 |
| f(zz["r2"][0]) | `hisirti` | 0,45 |
| f(zz["ucus"][0] + zz["ucus"][1]) − 1 | `tik` | 0,5 (künye yerine oturur) |
Örnekteki kaydırma (kare başına ≤ 3) ve sıralama; assert `0 ≤ kare < U.Z["kare"] − 12`; `D/olaylar.json` yaz; `olay N` bas.

## 6. Tema notu
uret.py koyu hex yazar. `calistir.sh` → `tema_hf` (`ortak/hf_tema.py`) `#root`a CSS değişkenleri ve `tema-acik` sınıfını ekler:
`#f3efe6` → murekkep, `#f2a93b` → vurgu (`rect` dolgusu → vurguDolgu), `text[fill="#1b1a17"]` → pilMetin, `stroke="#1b1a17"` → zemin.
`style="fill:var(--zemin)"` değişkeni hf_tema tanımlar (iki temada).

## 7. Kabul ölçütü (şef koşar)
1. `cd D && /usr/bin/python3 uret.py && /usr/bin/python3 olay.py` çıkış 0; assert yok; `olaylar.json` 6 olay, hepsi kare < 90.
2. `proje/index.html`: 1080×1920; `#kunye` içinde `#ku-ders`, `#rz0`, `#ku-cip`, `#logoimg`; `#bas1`, `#bas2`, `#r1`, `#r2`, `#kapak-sahne`, `#al0`.
3. `cd K && bash araclar/qa-yerel.sh 02-04-ydt-temel-s1 01-hyperframes-kapak 0.2,1.97,2.95 1.97 --hazirla` çıkış 0.
4. Kareler: taşma, kesik yazı, üst üste binme, okunmaz kontrast, boş kare YOK; platform bandında öğe YOK; altyazı bandında 2 satır;
   1,97 karesinde satır 1 tam, çip yok, ders adı yok.
