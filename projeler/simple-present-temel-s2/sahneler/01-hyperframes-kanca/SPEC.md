# SPEC — simple-present-temel-s2 · sahne 01-hyperframes-kanca (huni v2, HyperFrames 1080×1920, 102 kare)

MAKİNE: Linux x86_64 (srv21), kullanıcı sef. Yazan: şef (15.11.2026). Bu belge tasarım verir; tam kod içermez.
K = `/home/sef/01dev/_worktrees/kalem-0204` · S = `K/projeler/simple-present-temel-s2/sahneler/01-hyperframes-kanca/` (bu dizin).
Kaynak: istem `K/projeler/simple-present-temel-s2/uretim-tutanagi/istem/sahne/D-01-hyperframes-kanca.md`, `BRIEF-S2.md` ("Yerleşim",
"Kanal katmanı", "Sahne içeriği" 0,00–3,00, "Kapak"), `/home/sef/01dev/dijital-anlatim/.claude/docs/huni-v2-standart.md` §1, §2, §7.
Yeniden hesaplama: yok. `uret.py` tek koşu; girdiler JSON dosyalarıdır.

## 1. Dosyalar

| Dosya | Durum | Kim |
|---|---|---|
| `S/uret.py` | YENİ. Bu belgeye göre yaz. | agy |
| `S/yardim.py`, `S/olay.py`, `S/calistir.sh`, `S/zamanlar.json`, `S/nesneler.json`, `S/cizim/*` | VAR. DOKUNMA. | şef |

Yalnız `S/uret.py` dosyasını yaz. Başka dosyaya dokunma. Silme yok. Test, render, git, betik koşma yok (şef koşar).
Python: girinti 4 boşluk, satır ≤ 120, her işlevde tip ipucu. Çalıştırma `/usr/bin/python3 uret.py` (fontTools kullanıcı site-packages'ta; `-I` YOK).

**Kalıp kod (salt okunur; oradan al, kopyala-uyarla):**
- `K/projeler/02-04-ydt-temel-s1/sahneler/01-hyperframes-kapak/uret.py` — iskelet: modül başı okuma (`Z`, `SOZ`, `ALT`), sabitler,
  `_denetimler()` (assert + metinli hata, `_p3_in_out`, `_p3_out`, `_kesisir`), `zamanlar()`, `uret()` HTML iskeleti (`<style>` font + ZEMIN_CSS,
  `#root` data öznitelikleri, `Y.zemin_html()`, `<svg id="sahne">`, `<script src="lib/gsap.min.js">`, `ac()`, `uc2()` orijin kuralı,
  `window.__timelines["main"]`), `__main__` (font kopyala, `proje/index.html` yaz, `devir.json` yaz).
- `K/projeler/02-04-ydt-temel-s1/sahneler/03-hyperframes-cta/yardim.py` satır 257–340 — karaoke altçizgili altyazı (`altyazi_svg`);
  aynı dizinin `uret.py` satır 262–279 — karaoke JS döngüsü.
- `S/yardim.py` (emsal 01 kopyası; `KONU = "Simple Present"`): `Y.genislik`, `Y.HUD`, `Y.RENK`, `Y.kunye_svg()`, `Y.konu_boyu()`,
  `Y.rozet_konumu()`, `Y.altyazi_dilimle()`, `Y.altyazi_satirlari()`, `Y.font_css()`, `Y.font_kopyala()`, `Y.zemin_html()`, `Y.ZEMIN_CSS`, `Y.W`, `Y.H`.

## 2. Girdiler

| Ad | Kaynak | Not |
|---|---|---|
| `Z` | `S/zamanlar.json` | fps 30, kare 102, sure 3.4, tik_bas 0.30, tik_sure 0.11, tik_ara 0.13, ucus [2.40, 0.60], ucus_olcek 0.45, ucus_hs 0.20, baslik_sol [2.70, 0.30], sahne_sol [2.40, 0.60], kapak_kare 27 |
| `SOZ` | `S/../../ortak/anlatim/sozcukler.json`, `cumle == 1` | assert ilk 4 sözcük = `["Usually", "görünce", "hangi", "zaman?"]` |
| `ALT` | `S/../../ortak/anlatim/altyazi.json` | altyazı parçaları |
| `FIG` | `S/cizim/ogrenci.json` | `kutu` [kx0, ky0, kx1, ky1] = [-37.4, 46.0, 1284.3, 1200.0], `parmak` [1235.4, 537.1], `yollar` [{parca, d}] (parca: govde, sac, yuz, aks), `kirp_y` 1200 |

## 3. Sabitler ve türetilen ölçüler (px; g(metin, aile, ağırlık, boy) = `Y.genislik(aile, ağırlık, metin, boy)`)

| Ad | Değer | Yaklaşık |
|---|---|---|
| KENAR, SAG, ORTA | `Y.HUD["kenar"]`, `Y.HUD["sagSinir"]`, (KENAR + SAG) / 2 | 60, 960, 510 |
| BAS1, BAS2, PAD | `"USUALLY"`, `"= ALIŞKANLIK"`, 0.20 (em) | |
| B | floor(min(190, (SAG − KENAR) / g(BAS1, Fredoka, 700, 1), (SAG − KENAR) / (g(BAS2, Fredoka, 700, 1) + 2·PAD))) | 137 |
| g1, t1x | g(BAS1, Fredoka, 700, B), ORTA − g1/2 | 599,9 / 210,0 |
| TOP1, T1 | 472, TOP1 + 0,70·B | 567,9 |
| HAP_UST, T2, HAP_ALT | T1 + 0,20·B + 29, HAP_UST + 0,98·B, T2 + 0,26·B | 624,3 / 758,6 / 794,2 |
| hap_w, hap_x, hap_rx | g(BAS2, Fredoka, 700, B) + 2·PAD·B, ORTA − hap_w/2, (HAP_ALT − HAP_UST)/2 | 893,8 / 63,1 |
| BOX (başlık birleşik kutusu) | x [hap_x, hap_x + hap_w], y [T1 − 0,70·B, HAP_ALT]; w0, h0 genişlik/yükseklik; O = merkez | O ≈ (510, 633,1) |
| boy, (rz_x, rz_w), KONU_SON | `Y.konu_boyu()`, `Y.rozet_konumu()`, KENAR + g(`Y.KONU`, Fredoka, 700, boy) | 34, (309,7, 203,6), 289,7 |
| HEDEF_X0, HEDEF_X1, HEDEF_Y0, HEDEF_Y1 | rz_x + rz_w + 24, 940, 372, 438 | 537,2 … 940 |
| H (uçuş hedef merkezi), HS | ((HEDEF_X0 + HEDEF_X1)/2, 405), `Z["ucus_hs"]` | (738,6, 405), 0,20 |
| TK_X0, TK_X1, TK_Y0, TK_Y1, TK_R | 60, 440, 918, 1310, 28 | takvim yaprağı |
| HALKA_X, HALKA_Y | (155, 345), (876, 960) | iki halka |
| BASLIK_Y | 1018 | yaprak başlık çizgisi |
| KUTU, KUTULAR | 100; [(80, 1044), (200, 1044), (320, 1044), (80, 1164), (200, 1164)] | sol üst köşeler; 5. kutu boş kalır |
| TIK, TIK_KAY | yerel noktalar (24, 54) → (44, 74) → (78, 28); kaymalar [(0, 0), (2, −2), (−2, 2), (1, −1)] | tik i = KUTULAR[i] + TIK + TIK_KAY[i], i 0–3 |
| FIG_S, FIG_R, FIG_ALT | 0.37, 954, 1376 | figür ölçeği, sağ kenar, kırpma tabanı |
| FIG_UST, FIG_SOL | FIG_ALT − (ky1 − ky0)·FIG_S, FIG_R − (kx1 − kx0)·FIG_S | 949,0 / 465,0 |
| PARMAK | (FIG_R − (px − kx0)·FIG_S, FIG_UST + (py − ky0)·FIG_S) | (483,1, 1130,7) |
| FIG_KAL | {govde: 4.4, sac: 3.6, yuz: 2.6, aks: 2.6} | ekran px; yolda `stroke-width` = değer / FIG_S |

## 4. Olay listesi (kare = round(sn × 30); küresel sn = yerel sn; t_bas 0,00)

| # | Olay | sn (kare) | Cümle sözcüğü |
|---|---|---|---|
| 1 | Kapak tam görünür: kanal katmanı + künye (`Simple Present` + rozet, son yerinde), başlık 2 satır, takvim (5 boş kutu), figür | 0,00 (0) | söz öncesi |
| 2 | tik 1–4 kalemle çizilir (`strokeDashoffset`, `sine.inOut`, süre tik_sure); başlangıç tik_bas + i·tik_ara | 0,30 / 0,43 / 0,56 / 0,69 (9 / 13 / 17 / 21); son tik 0,80'de biter | söz öncesi |
| 3 | KAPAK KARESİ (başlık tam, 4 tik bitmiş, ses yok) | 0,90 (27) | — |
| 4 | altyazı dilimi açılır | SOZ[0].t0 − 0,05 = 0,95 (29) | Usually |
| 5 | karaoke altçizgisi sözcük başında | 1,00 (30) · 1,80 (54) · 2,60 (78) · 2,92 (88) | Usually · görünce · hangi · zaman? |
| 6 | takvim + figür solar (`power2.in`) | sahne_sol 2,40–3,00 (72–90) | — |
| 7 | uçuş: `#baslik` küçülerek künye satırının sağ boş bölümüne gider (x, y `power3.inOut` ucus; ölçek `power3.out` ucus_olcek) | ucus 2,40–3,00 (72–90) | — |
| 8 | başlık solar (`power2.in`), 3,00'te opaklık 0 | baslik_sol 2,70–3,00 (81–90) | — |
| 9 | durgun: yalnız kanal + künye + altyazı; son 12 kare geçiş altında | 3,00–3,40 (90–101) | `zaman?` sürer → sahne 02 |

Kanal katmanı ve künye (`#kunye`, `#kanal`, `#ku-konu`, `#rz0`) 0. kareden son kareye opaklık 1, konum sabit: hiçbirine `gsap.set` ya da `tl.*` YAZMA
(emsalin `#ku-konu` gizleme ve `#rz0` kaydırma satırları bu sahnede YOK).

## 5. Yerleşim

```
y  291 ┌ [logo] @ydspublishing — Y.kunye_svg() #kanal, hareketsiz                                     ┐ kanal 280–350
   386 │ Simple Present (Fredoka 34, x 60, taban 420) [YDT · BASIC] x ≈ 310–513 · hedef bölge x 537–940 │ künye 360–450
   472 │ USUALLY (B ≈ 137, orta 510, kontur 12)                       ─(2,40–3,00)→ hedef bölge, ölçek 0,20 │ içerik 460–1380
   624 │ ( = ALIŞKANLIK ) sarı hap x 63–957, y 624–794                                                    │
   876 │ halkalar x 155 / 345 (876–960)                                                                    │
   918 │ ┌ takvim yaprağı x 60–440, y 918–1310, köşe 28 ┐        figür (aynalı) x 465–954, y 949–1376     │
  1018 │ ├ başlık çizgisi ───────────────────────────────┤        parmak ucu ≈ (483, 1131) takvime bakar  │
  1044 │ │ [K1 ✓] [K2 ✓] [K3 ✓]   (100×100, x 80/200/320) │                                                │
  1164 │ │ [K4 ✓] [K5  ]                                  │                                                │
  1310 │ └───────────────────────────────────────────────┘                                                 │
  1484 │ altyazı Lexend 500 44, orta x 510, karaoke sarı altçizgi (taban + 12)                               │ altyazı 1400–1550
  1570 └ boş zemin                                                                                          ┘
Son hal (3,00+): kanal + künye + altyazı; içerik bandı boş (sahne 02 kare 0 ile aynı).
```

## 6. Ekran öğeleri (KOYU hex yaz: zemin `#1b1a17`, mürekkep `#f3efe6`, vurgu `#f2a93b`; `ortak/hf_tema.py` temaya çevirir)

Sıra (alttan üste): `#takvim` → `#figur` → `#baslik` (`#bas2`, sonra `#bas1`) → `#kunye` (`Y.kunye_svg()`) → `#altyazi`.

| Kimlik | İçerik |
|---|---|
| `#takvim` | `<g fill="none" stroke="#f3efe6" stroke-linecap="round" stroke-linejoin="round">`. İçinde: `<rect id="tk-yaprak">` (TK_X0, TK_Y0, genişlik TK_X1 − TK_X0, yükseklik TK_Y1 − TK_Y0, rx TK_R, stroke-width 7); iki halka yolu `M155 876 L155 960`, `M345 876 L345 960` (7); başlık çizgisi `M60 1018 L440 1018` (7); 5 gün kutusu `el_kutu()` yolu `id="gk{0-4}"` (5); 4 tik yolu `id="tk{0-3}"` `M a L b L c` (10, `style="opacity:0"`) |
| `el_kutu(x, y, w, h, i) -> str` | el çizimi kare: 4 kenar, her kenar tek kübik `C`; kontrol noktaları kenara dik, sabit tablodan ±2,5 px'i aşmayan kayma (tablo i ile döner); yol başlangıç noktasını 6 px geçerek biter (kalem bindirmesi). `A` komutu yok (yalnız M, L, C) |
| `#figur` | `<g id="figur" clip-path="url(#figkl)" fill="none" stroke="#f3efe6" stroke-linecap="round" stroke-linejoin="round">` + iç `<g id="fig-ic" transform="translate(FIG_R + kx0·FIG_S, FIG_UST − ky0·FIG_S) scale(−FIG_S, FIG_S)">` (yatay ayna) + her yol `<path d=… stroke-width=FIG_KAL[parca]/FIG_S>`. `<defs>` içinde `<clipPath id="figkl"><rect x="440" y="900" width="520" height="476"/></clipPath>` (ekran koordinatı; taban FIG_ALT 1376 = kit y 1200) |
| `#bas2` | `<rect id="hap">` (hap_x, HAP_UST, hap_w, HAP_ALT − HAP_UST, rx hap_rx, fill vurgu) + `<text id="bas2t">` (x ORTA, taban T2, `text-anchor="middle"`, Fredoka 700 B, fill zemin, `font-kerning:none`) BAS2 |
| `#bas1` | `<text id="bas1t">` (x t1x, taban T1, Fredoka 700 B, fill mürekkep, stroke zemin 12, `stroke-linejoin="round"`, `font-kerning:none;paint-order:stroke fill`) BAS1. Altçizgi YOK |
| `#baslik` | `<g id="baslik">` = `#bas2` + `#bas1` (uçuş ve solma bu grupta) |
| `#altyazi` | `<g id="altyazi">` + `altyazi_karaoke(0.0, Z["sure"], ALT)` çıktısı |

`altyazi_karaoke(t_bas: float, sure: float, liste: list[dict]) -> tuple[str, list[list], list[list]]`: kalıp 03-cta `yardim.py` 257–340. Farklar:
`liste = Y.altyazi_dilimle(liste)` (altyazi_cumleleri değil); satırlar `Y.altyazi_satirlari`; satır x = `Y.HUD["altyaziOrta"]` (510) − satır genişliği/2,
`text-anchor="start"`, `style="font-kerning:none"`; y0 = altyaziBas + (84 tek satır, 56 iki satır), satır aralığı altyaziSatir; assert son taban +
0,25·altyaziYazi ≤ altyaziSon ve 60 ≤ satır x, satır sonu ≤ 960. Sözcük eşleme: `cumle` aynı ve t0 ∈ [p.t0 − 0,06, p.t1); sayı eşitse altçizgi
`<line id="ak{i}_{j}" … stroke="#f2a93b" stroke-width="6" stroke-linecap="round" style="opacity:0"/>` (y = taban + 12, x sözcük başı → noktalamasız
sözcük sonu); aç = sözcük t0 − t_bas; kapat = sonraki sözcük t0 − t_bas, son sözcükte min(t1 − t_bas + 0,25, parça kapanışı). Cümle 1 için eşleşme
ZORUNLU (4 sözcük, 4 altçizgi; değilse assert). Parça aç/kapat kuralı emsal 01 `Y.altyazi_svg` ile aynı (t0 − 0,05; t1 + 0,35 ile sonraki parça
t0 − 0,05'in küçüğü; sure ile kırp).

Yazı: Fredoka 700 (başlık), Lexend 500 (altyazı). Ekran metni yalnız BAS1, BAS2, künye, kanal ve altyazı. Kırmızı, yeşil, emoji, gradyan, gölge YOK.
Ekranda "Tam ders", "dakika", süre, QR, "izle" düğmesi YOK.

## 7. Zaman çizelgesi (GSAP; bütün tween `ac()` ile `immediateRender: false`)

- Altyazı ve karaoke: 03-cta `uret.py` 262–279 döngüsü aynen (`V.alt`, `V.karaoke`; çizim 0,15 sn `power2.out`).
- Tikler: her `#tk{i}` için `getTotalLength()` → `strokeDasharray = L + " " + (L + 2)`, `strokeDashoffset = L` (emsal `#alti` kalıbı);
  `tl.set(opacity 1)` ve `tl.to(strokeDashoffset 0, duration tik_sure, ease "sine.inOut")` başlangıç tik_bas + i·tik_ara.
- Uçuş: `gsap.set("#baslik", {svgOrigin: "Ox Oy", smoothOrigin: false})` BİR KEZ (emsal `uc2` yorumu); `tl.to` x = Hx − Ox ve y = Hy − Oy
  (ucus[1], `power3.inOut`, ucus[0]); `tl.to` scale HS (ucus_olcek, `power3.out`, ucus[0]); tween'de svgOrigin YOK.
- Solma: `tl.to("#baslik", opacity 0, baslik_sol[1], "power2.in")` baslik_sol[0]'da; `tl.to(["#takvim", "#figur"], opacity 0, sahne_sol[1],
  "power2.in")` sahne_sol[0]'da.
- `veri` sözlüğü (`V`): Z, alt, karaoke, tikler [[id, t0, süre], …], O, H, HS.

## 8. Denetimler (`_denetimler()`; assert, ihlalde metinde değer yaz; sabiti kendin değiştirme)

1. Başlık: 120 ≤ B ≤ 190; t1x ≥ KENAR ve t1x + g1 ≤ SAG; hap_x ≥ KENAR ve hap_x + hap_w ≤ SAG; T1 − 0,70·B ≥ `icerikBas`; HAP_ALT ≤ 800;
   len(BAS1), len(BAS2) ≤ 24.
2. Takvim: yaprak ve halkalar x [KENAR, SAG], y [820, `icerikSon`] içinde; her kutu yaprağın iç kenarından ≥ 20 px içeride ve BASLIK_Y'den ≥ 24 px
   aşağıda; her tikin üç noktası kendi kutusunun 4 px içinde; `el_kutu` noktaları kutunun 4 px çevresinde.
3. Figür: FIG_SOL ≥ TK_X1 + 20; FIG_R ≤ SAG − 4; FIG_UST ≥ HAP_ALT + 24; FIG_ALT ≤ `icerikSon` − 2; PARMAK x > TK_X1 + 20 ve
   TK_Y0 ≤ PARMAK y ≤ TK_Y1.
4. Dikey sıra: HAP_ALT + 24 ≤ min(HALKA_Y[0], FIG_UST).
5. Uçuş örneklemesi: t = u0 … u0 + ud (son nokta dahil), adım 1/30; e_konum = `_p3_in_out((t − u0)/ud)`, e_olcek = `_p3_out((t − u0)/ucus_olcek)`;
   merkez = O + (H − O)·e_konum, ölçek s = 1 + (HS − 1)·e_olcek, kutu = merkez ± s·(w0/2, h0/2). Çiftler (6 px pay, kesişim yok): kutu × rozet
   [rz_x, rz_x + rz_w] × [386, 434]; kutu × konu [KENAR, KONU_SON] × [420 − 0,75·boy, 420 + 0,25·boy]; kutu × kanal [60, 602] × [291, 341].
   Her t'de kutu x [KENAR, SAG] içinde ve kutu altı ≤ min(HALKA_Y[0], FIG_UST) − 6. Son t'de kutu [HEDEF_X0, HEDEF_X1] × [HEDEF_Y0, HEDEF_Y1]
   içinde (1 px tolerans). Düşerse t'yi ve çifti yazıp dur.
6. Zaman: son tik bitişi (tik_bas + 3·tik_ara + tik_sure) ≤ 0,80 + 1e-6 ve ≤ kapak_kare/30 − 1/30; SOZ[0].t0 ≥ kapak_kare/30 + 1/30;
   ucus[0] + ucus[1], baslik_sol[0] + baslik_sol[1], sahne_sol[0] + sahne_sol[1] üçü de 3,00 (|fark| < 1e-6) ve = (kare − 12)/30.
7. Metin: yasak söz denetimi `uret.py` içinde YOK (kod satırı istem grep'ine takılır; şef düzeltmesi 15.11); kapı 3 grep'i üretilen HTML'i tarar.

## 9. Çıktı

- `zamanlar() -> dict`: `{"tikler": [[t0, süre] × 4], "altyazi_ac": SOZ[0].t0 − 0,05, "ucus": [ucus[0], ucus[1]]}` (`olay.py` bu anahtarları okur).
- `uret() -> str`: tam HTML. Kök `<div id="root" data-composition-id="main" data-start="0" data-duration="{Z.sure}" data-fps="30"
  data-width="1080" data-height="1920">`; `#sahne` viewBox `0 0 1080 1920`. CSS'e `#root.tema-acik` dizgisi YAZMA (hf_tema kuralı).
- `__main__`: `proje/` aç, `Y.font_kopyala(S/proje/assets/fonts)`, `S/proje/index.html` yaz, `S/devir.json` yaz:
  `{"icerik_bandi": "bos", "t": 3.0, "kunye": {"konu": Y.KONU, "boy": boy, "rozet": [rz_x, rz_w], "rozet_y": [386, 434]},
  "altyazi": "cümle 1 sahne sonuna dek (3,40)", "not": "huni v2 (15.11): sahne 02 kare 0 içerik bandı boş; kanal + künye 0. kareden aynı"}`
  (sayılar 2 basamak yuvarlak, `ensure_ascii=False`, indent 2); `devir:` satırını yazdır.

## 10. Kabul ölçütü (şef koşar)

1. `cd S && /usr/bin/python3 uret.py && /usr/bin/python3 olay.py` çıkış 0; assert yok; `olaylar.json` 6 olay, hepsi kare < 90.
2. `proje/index.html`: `#kunye` içinde `#kanal` (`#logoimg` + `#kanal-yazi`), `#ku-konu`, `#rz0`; bunlara `gsap`/`tl` satırı YOK; `#tk0`–`#tk3`,
   `#gk0`–`#gk4`, `#figkl`, `#baslik`, `#altyazi`, `#ak0_0`–`#ak0_3` var.
3. `cd K && bash araclar/qa-yerel.sh simple-present-temel-s2 01-hyperframes-kanca 0.00,1.50,2.95 1.50 --hazirla` çıkış 0.
4. `node araclar/cakisma-kapisi.mjs simple-present-temel-s2 --sahne 01-hyperframes-kanca --port 41333 --sunucu 41022` çıkış 0, 0 uyarı.
5. Karelerde: 0–280 ve 1570–1920 boş; x 960–1080'de içerik yok; kanal katmanı her karede aynı yer ve boyda; 4 tik + 1 boş kutu.
