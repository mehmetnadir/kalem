# SPEC — simple-present-temel-s3 · sahne 06-hyperframes-kapak-b (huni v2; HyperFrames, 1080×1920, tek kare, ses yok) · 15.11.2026

MAKİNE: Linux x86_64 (srv21). Python `/usr/bin/python3` (fontTools kullanıcı site-packages'ta: `-I` YOK). Şef yazdı; kodu agy yazar.
İstem: `uretim-tutanagi/istem/sahne/D-06-hyperframes-kapak-b.md` (P0202-S3-C). Tasarım verir; tam kod yok.

| Ne | Değer |
|---|---|
| Yazılacak dosya (yeni) | `/home/sef/01dev/_worktrees/kalem-0204/projeler/simple-present-temel-s3/sahneler/06-hyperframes-kapak-b/uret.py` |
| İskelet kalıbı (salt okunur) | `/home/sef/01dev/_worktrees/kalem-0204/projeler/02-04-ydt-temel-s1/sahneler/05-hyperframes-kapak-b/uret.py` |
| Başlık + kâğıt kart kalıbı (salt okunur) | `/home/sef/01dev/_worktrees/kalem-0204/projeler/simple-present-temel-s3/sahneler/01-hyperframes-kanca/uret.py` (satır 406–417 başlık, 449–467 kart ve kalem `?`, 555–557 kart CSS) |
| Yardımcı (HAZIR, DEĞİŞTİRME) | `.../06-hyperframes-kapak-b/yardim.py` (`Y.kunye_svg()`, `Y.genislik`, `Y.RENK`, `Y.rozet_konumu`, `Y.font_css`, `Y.ZEMIN_CSS`, `Y.zemin_html`, `Y.font_kopyala`, `Y.W`, `Y.H`, `Y.HUD`) |
| Hazır, DOKUNMA | `calistir.sh`, `olay.py`, `zamanlar.json`, `yardim.py`, bu `SPEC.md` |
| uret.py yazar | `proje/index.html`, `proje/assets/fonts/` (`Y.font_kopyala`), `nesneler.json` |
| Bağlayıcı | `/home/sef/01dev/dijital-anlatim/.claude/docs/huni-v2-standart.md` §1, §2, §6 · `.../simple-present-temel-s3/BRIEF-S3.md` "Kapak", "Kanal katmanı" · `.../uretim-tutanagi/kapak-taslak.md` §2, §4 |

Başka dosyaya dokunma. Silme yok. Test, render, git YOK. `ortak/`, `zaman.json`, başka sahneler salt okunur.

## 1. İskelet (kalıp uret.py'den aynen)

- Dosya başı: `#!/usr/bin/python3`, docstring (`simple-present-temel-s3 sahne 06 kapak B (soru) index.html üretici …`),
  `from __future__ import annotations`, `AD`, `sys.path.insert(0, str(AD))`, `import yardim as Y`, `PAKET = AD.parent.parent`.
- `zaman.json` + `zamanlar.json` okuma ve assert'ler (kalıp satır 21–33) AYNEN: `duragan` içinde `klasor == AD.name` tek kayıt,
  `kare == 1`, `cikti == "kapak-b.png"`, `AD.name` `sahneler[]` içinde YOK; `zamanlar.json` `sure` 1.0 · `kare` 1 · `fps` 30.
  Anlatım, sözcük, altyazı dosyası OKUNMAZ.
- `R = Y.RENK`; anahtar assert'i (`zemin`, `murekkep`, `ikincil`, `vurgu`).
- `kesisim()` (kalıp satır 445–449) aynen. HTML iskeleti ve GSAP (kalıp satır 580–608) aynen; şu farklarla: karakter `<img>`
  YOK, `.kenar` CSS YOK; `<style>` içine §5 CSS satırları; `<svg id="sahne">` içeriği §3 sırası.
- `__main__`: `proje/` aç, `Y.font_kopyala(proje/"assets"/"fonts")`, `index.html` yaz, `nesneler.json` (tam sayı, `indent=2`, sonda
  `\n`), stdout iki satır (§6 madde 10).
- ALINMAZ: numpy, PIL, `alfa_kutusu`, `maske`, `bos_mu`, `maske_kutusu`, `gorsel_kopyala`, `gorsel_img`, `hesapla_yerlesim`, balon,
  düşünce izi, `KARAKTER` (bu kapakta figür ve karakter görseli YOK).
- Tür ipucu bütün işlevlerde; girinti 4 boşluk; satır ≤ 130 karakter; try/except yok; `print` yalnız `__main__`'de.

## 2. Sabitler (px)

| Ad | Değer | Not |
|---|---|---|
| `X0, X1, ORTA` | 60, 960, 510 | içerik bandı, orta |
| `Y0, Y1` | 460, 1380 | içerik bandı |
| `BAS1, BAS2` | `"GOES mu,"`, `"GO mu?"` | soru eki küçük harf; İngilizce sözcük büyük |
| `KONTUR` | 10 | başlık konturu (zemin rengi) |
| `CAP, VIRGUL, ALT, SATIR` | 0.71, 0.16, 0.02, 1.12 | Fredoka ölçüsü: büyük harf üstü 0,703; `,` alt −0,157; `O` alt −0,02; satır aralığı |
| `BAS_UST, BAS_SON, BAS_TAVAN` | 470, 800, 190 | başlık bandı ve üst sınır |
| `KB` | 72 | kart yazısı (Fredoka 700) |
| `KPAD, KY, KH, KRX, KCIZGI` | 64, 860, 260, 18, 4 | kart iç payı, üst, yükseklik, köşe, kalem kenarı |
| `KT1, KT2` | 957, 1061 | kart satır tabanları |
| `BOS_PAY, BOS_SON_ARA, BOS_ALT, BOS_CIZGI` | 16, 6, 10, 5 | boşluk çizgisi: iki yan pay, çizgi → noktalama arası, tabandan aşağı, çizgi kalınlığı |
| `HB` | 80 | hap yazısı (Fredoka 700) |
| `HAP_PAY, HAP_Y, HAP_H, HAP_CIZGI, HAP_ARA` | 44, 1170, 120, 5, 40 | hap iç payı, üst, yükseklik, çizgi, iki hap arası |
| `QS, Q_ARA` | 1.6, 48 | kalem `?` ölçeği, hap 2 → `?` arası |

## 3. Yerleşim ve öğeler (SVG sırası: künye → başlık → kart → haplar → `?`)

```
y    0 ┌───────────────────────────────────────────┐
       │              (boş zemin)                   │ 0–280
   291 │ [logo] @ydspublishing                      │ kanal 280–350 (Y.kunye_svg)
   420 │ Simple Present (YDT · BASIC)               │ künye 360–450
  ≈475 │              GOES mu,                      │ başlık, orta x 510, B ≈ 172
  ≈800 │               GO mu?                       │
   860 │      ┌──────────────────────────┐          │ kâğıt kart, ortalı
   957 │      │ He doesn't _______.      │          │ Fredoka 72
  1061 │      │ Does she _______?        │          │
  1120 │      └──────────────────────────┘          │
  1170 │      ( go )   ( goes )    ?               │ iki eş hap + sarı kalem ?
  1290 │                                            │
  1320 ├────────── içerik sonu (öğe yok) ───────────┤
  1920 └──────────────── boş ───────────────────────┘ 1320–1920 boş (altyazı yok)
```

### 3.1 Künye
`Y.kunye_svg()` aynen (argümansız). uret.py künyeye ve kanal katmanına değer yazmaz.

### 3.2 Başlık — `<g id="baslik">`
- `g1_1 = Y.genislik("Fredoka", 700, BAS1, 1.0)`, `g2_1` aynı (`BAS2`).
- `B = floor(min(BAS_TAVAN, (900 − KONTUR) / max(g1_1, g2_1), (BAS_SON − BAS_UST − KONTUR) / (CAP + SATIR + ALT)))`
  (beklenen 172; genişlik 900 içinde, yükseklik bandı belirler).
- `BH = KONTUR + (CAP + SATIR + ALT)·B`; `ust = BAS_UST + (BAS_SON − BAS_UST − BH) / 2` (bantta dikey ortala).
- `T1 = ust + KONTUR/2 + CAP·B`; `T2 = T1 + SATIR·B`.
- İki `<text>`: `id="bas1"` (`BAS1`, taban T1) ve `id="bas2"` (`BAS2`, taban T2); ikisi `x=ORTA`, `text-anchor="middle"`,
  Fredoka 700, `font-size=B`, `fill=R["murekkep"]`, `stroke=R["zemin"]`, `stroke-width=KONTUR`, `stroke-linejoin="round"`,
  `style="font-kerning:none;paint-order:stroke fill"`, `xml:space="preserve"`. Hap YOK, kutu YOK, sarı YOK.
- Kalıp: kanca `bas1t` öğesi (satır 408–410).

### 3.3 Kâğıt kart — `<g id="kart">`
- Satır parçaları: satır 1 `"He doesn't"` + boşluk + `"."`; satır 2 `"Does she"` + boşluk + `"?"`. Kesme işareti ASCII `'`.
- `BOS_W = ceil(Y.genislik("Fredoka", 700, "goes", KB)) + 2·BOS_PAY` (beklenen 183; iki cevaptan uzun olana göre; iki satırda AYNI).
- Satır `i` için: `bas_i` = parça a (`"He doesn't"` / `"Does she"`); `b0_i = TX + Y.genislik("Fredoka", 700, bas_i + " ", KB)`
  (boşluk çizgisi başı; sondaki boşluk ilerlemesi dahil); `b1_i = b0_i + BOS_W`; noktalama x `n_i = b1_i + BOS_SON_ARA`;
  satır genişliği `L_i = (n_i + Y.genislik("Fredoka", 700, nokta_i, KB)) − TX`.
- `LW = max(L_1, L_2)`; `KW = LW + 2·KPAD`; `KX = ORTA − KW/2`; `TX = KX + KPAD` (önce `L_i`'yi `TX = 0` ile hesapla, sonra kaydır).
  Beklenen: `LW ≈ 561`, `KW ≈ 689`, `KX ≈ 165,5`.
- `<rect id="kart-zemin" x=KX y=KY width=KW height=KH rx=KRX fill="#fff9e6" stroke="#1b1a17" stroke-width=KCIZGI>`
  (kanca kartı ile aynı görünüm; temaya göre CSS §5).
- Yazılar: `<text id="k1a" x=TX y=KT1>He doesn't</text>`, `<text id="k1b" x=n_1 y=KT1>.</text>`,
  `<text id="k2a" x=TX y=KT2>Does she</text>`, `<text id="k2b" x=n_2 y=KT2>?</text>`; hepsi Fredoka 700 `KB`, `fill="#1b1a17"`,
  `style="font-kerning:none"`, `xml:space="preserve"`. Alt çizgi karakteri (`_`) YAZILMAZ: boşluk kalemle çizilir.
- Boşluk çizgileri: `<g id="bosluk" fill="none" stroke="#1b1a17" stroke-width=BOS_CIZGI stroke-linecap="round">` içinde
  `<path id="bos1">` ve `<path id="bos2">`; satır `i` için `y = KT_i + BOS_ALT`, `d = "M{b0} {y+1.5} Q{(b0+b1)/2} {y−2.5} {b1} {y+1.5}"`
  (hafif kavisli el çizgisi; iki çizgi aynı boy).

### 3.4 İki eş hap — `<g id="haplar">`
- `HAP_W = ceil(Y.genislik("Fredoka", 700, "goes", HB)) + 2·HAP_PAY` (beklenen 256; iki hap AYNI genişlik ve boy).
- `?` kutusu (yerel, ölçek öncesi): x −2,5 … 59,5, y −3,5 … 99,5 → ekran `QW = 62·QS`, `QH = 103·QS`.
- Sıra genişliği `RW = 2·HAP_W + HAP_ARA + Q_ARA + 57·QS`; `RX0 = ORTA − RW/2` (sıra yatayda ortalı; beklenen ≈ 164).
- `hap1_x = RX0`, `hap2_x = RX0 + HAP_W + HAP_ARA`; `qx = hap2_x + HAP_W + Q_ARA`; `qy = HAP_Y + HAP_H/2 − 50·QS` (= 1150).
- `<g id="haplar" fill="none" stroke=R["murekkep"] stroke-width=HAP_CIZGI>` içinde `<rect id="hap-go" x=hap1_x y=HAP_Y
  width=HAP_W height=HAP_H rx=HAP_H/2>` ve `<rect id="hap-goes" x=hap2_x …>` (dolgusuz).
- Hap yazıları grubun DIŞINDA: `<text id="hap-go-yazi">go</text>`, `<text id="hap-goes-yazi">goes</text>`; x hap ortası,
  `text-anchor="middle"`, taban `HAP_Y + HAP_H/2 + 16` (= 1246), Fredoka 700 `HB`, `fill=R["murekkep"]`, `style="font-kerning:none"`.
  İki hap aynı biçim; hiçbiri vurgulanmaz (vurgu cevabı verir).

### 3.5 Büyük sarı kalem `?` — `<g id="soru">` (tek sarı öğe)
- `<g id="soru" transform="translate(qx qy) scale(QS)" fill="none" stroke=R["vurgu"] stroke-linecap="round" stroke-linejoin="round">`
  - `<path id="soru-kanca" d="M3 27 C3 11 15 2 29 2 C44 2 54 12 54 27 C54 41 44 47 35 53 C29 57 28 63 28 72" stroke-width="11"/>`
    (kanca satır 451 yolu; renk sarı, kırmızı DEĞİL)
  - `<path id="soru-nokta" d="M28 92 L28 92.01" stroke-width="15"/>` (nokta = yuvarlak uçlu kısa çizgi)
- Çocuklarda `stroke` özniteliği YOK (gruptan alır). `<circle>` YAZILMAZ (hf_tema `circle[fill=vurgu]`'yu soluk dolguya çevirir).
  Emoji ya da `?` karakteri olarak YAZILMAZ.

## 4. Blok kutuları (`blok_kutulari()` → `nesneler.json`, sıra AYNEN)

| ad | x | y | w | h |
|---|---|---|---|---|
| `kanal` | 60 | 291 | `263 + Y.genislik("Lexend", 700, "@ydspublishing", 42) − 60` | 48 |
| `kunye` | 60 | `min(386, 420 − 0,75·Y.konu_boyu())` | `rozet_x + rozet_w − 60` (`Y.rozet_konumu()`) | `max(434, 420 + 0,25·konu_boyu) − y` |
| `baslik` | `ORTA − max(g1, g2)/2 − KONTUR/2` | `T1 − CAP·B − KONTUR/2` | `max(g1, g2) + KONTUR` | `T2 + ALT·B + KONTUR/2 − y` |
| `kart` | `KX − KCIZGI/2` | `KY − KCIZGI/2` | `KW + KCIZGI` | `KH + KCIZGI` |
| `hap-go` | `hap1_x − HAP_CIZGI/2` | `HAP_Y − HAP_CIZGI/2` | `HAP_W + HAP_CIZGI` | `HAP_H + HAP_CIZGI` |
| `hap-goes` | `hap2_x − HAP_CIZGI/2` | aynı | aynı | aynı |
| `soru` | `qx − 2,5·QS` | `qy − 3,5·QS` | `62·QS` | `103·QS` |

(`g1`, `g2` = `B` boyunda başlık satır genişlikleri.)

## 5. Tema (hf_tema.py ile uyum)

- `Y.ZEMIN_CSS`, `Y.zemin_html()`, `Y.font_css()` DEĞİŞTİRMEDEN. `#sahne{position:absolute;left:0;top:0;}`.
- Kart CSS satırları (kanca satır 555–557 kalıbı; seçiciler `#kart-zemin` ve `#bosluk`):
  `.tema-acik #kart-zemin{fill:#fffdf8;}` · `#root #kart-zemin{stroke:var(--pilMetin);}` · `#root #bosluk{stroke:var(--pilMetin);}`.
  Gerekçe: hf_tema `[stroke="#1b1a17"]` → `--zemin` (açıkta krem) eşler; bu seçiciler (öncelik 2,0,0) kalem kenarını ve boşluk
  çizgisini mürekkepte tutar. `#root.tema-acik` dizgesi CSS'e YAZILMAZ (hf_tema onu "zaten çevrildi" sayar).
- Kart yazıları `fill="#1b1a17"` → hf_tema `text[fill="#1b1a17"]` → `--pilMetin` (iki temada koyu mürekkep, açık kart üstünde).
- `?` `stroke=#f2a93b` → açıkta `--vurgu`, koyuda sarı. Künye rozeti `rect fill=#f2a93b` → `--vurguDolgu`.
- Renkler SVG özniteliği, küçük harf hex.

## 6. Kurallar ve kabul ölçütü (`kurallari_dogrula()`, `assert`)

1. Sınır: `kanal` ⊂ x [60, 960] × y [280, 350]; `kunye` ⊂ x [60, 960] × y [360, 450]; öteki bütün bloklar ⊂ x [60, 960] × y [460, 1320].
   Böylece 0–280, 1320–1920 ve x 960–1080 boş.
2. Bant: `baslik` y ≥ 465 ve alt ≤ 805; `kart` üstü ≥ `baslik` altı + 40; `hap-go`, `hap-goes`, `soru` üstü ≥ `kart` altı + 20.
3. Bütün blok çiftlerinin kesişim alanı 0 (`kesisim`, 7 blok → 21 çift).
4. Yazı boyu: `64 ≤ B ≤ 190`; `KB == 72`; `HB == 80`. Başlık satır genişliği + KONTUR ≤ 900. Kart satırları kart içinde:
   `TX ≥ KX + 40` ve `TX + LW ≤ KX + KW − 40`; `KT1 − 0,73·KB ≥ KY + 30`; `KT2 + BOS_ALT + 4 ≤ KY + KH − 30`.
5. Başlık 2 satır, toplam 4 sözcük; her ekran satırı ≤ 24 karakter: `GOES mu,`, `GO mu?`, `He doesn't ____.`, `Does she ____?`, `go`, `goes`.
6. Görünen metin: `re.findall(r">([^<]+)</text>", html)` kümesi TAM OLARAK
   `{"@ydspublishing", "Simple Present", "YDT · BASIC", "GOES mu,", "GO mu?", "He doesn't", ".", "Does she", "?", "go", "goes"}`.
   Her görünen metinde U+2FFF üstü karakter (emoji) YOK; `_`, `✗`, `✓` YOK. Yasak söz taraması: küçük harfe çevrilmiş görünen
   metinde `"tam" + " ders"`, `"dak" + "ika"`, `"izle"`, `"qr"`, `"kanal"` YOK. **DİKKAT:** ilk iki söz kodda PARÇALI yazılır
   (`"tam" + " ders"`, `"dak" + "ika"`); bitişik yazılırsa istemin `grep 'tam ders|dakika'` kapısı koda takılır.
7. HTML (küçük harf) içinde YOK: `math.random`, `date.now`, `new date`, `opacity:0`, `<circle`, `<img`, `#root.tema-acik`.
   HTML'deki her `#rrggbb` değeri şu kümede: `R` zemin/murekkep/ikincil/vurgu + `#fff9e6`, `#fffdf8`. Kırmızı (`#e0473b`,
   `#d6453a`), yeşil (`#167a4a`), `#fece00` YOK. `html.count(R["vurgu"]) == 2` (künye rozeti + `soru` grubu).
   `id="kanal"`, `id="logoimg"` TAM bir kez; `html.count("<image") == 1`.
8. Var olması gereken id'ler: `baslik`, `bas1`, `bas2`, `kart`, `kart-zemin`, `k1a`, `k1b`, `k2a`, `k2b`, `bosluk`, `bos1`, `bos2`,
   `haplar`, `hap-go`, `hap-goes`, `hap-go-yazi`, `hap-goes-yazi`, `soru`, `soru-kanca`, `soru-nokta`. Yok: `karakter`, `daire`,
   `hap` (tek başına), `bk-kutu`, `t2`, `ku-nokta`, `rz1`, `ku-cip`.
9. Zaman çizelgesi kalıpla aynı: `tl.set("#sahne", {opacity: 1, immediateRender: false}, 0)` ve `…, Z["sure"])`;
   `window.__timelines["main"]`. Başka tween yok.
10. `/usr/bin/python3 uret.py` stdout: `index.html yazıldı <bayt>` ve `B=<B> KX=<KX:.1f> KW=<KW:.1f> RX0=<RX0:.1f> HAP_W=<HAP_W>`; çıkış 0.

## 7. Olay listesi (tek kare; anlatım yok)

| Olay | Kare / küresel sn | Cümle sözcüğü |
|---|---|---|
| bütün öğeler görünür: kanal, künye, başlık, kart (2 satır + 2 boşluk çizgisi), 2 hap, sarı `?` | kare 0 (çizelge 1,0 sn; yakalama 0,5 sn) | — (zaman çizelgesi dışı; `olay.py` boş liste yazar) |

Ekran metni seste karşılık arar: cümle 2 EN parça `He doesn't go. Does she go?` (cevap videoda; kapakta cevap YOK).

## 8. Kabul (şef koşturur; ajan koşturmaz)

`bash calistir.sh --tema acik|koyu` → `P/kapak-b.png` ve `k/koyu/kapak-b-koyu.png` 1080×1920; taşma, kesik yazı, üst üste binme
yok; kanal katmanı görünür; 0–280, 1320–1920 ve x 960–1080 boş; y 1150–1380 aralığında kutu/yer tutucu yok (yalnız hap ve `?`).
