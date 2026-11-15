# SPEC — 02-04-ydt-temel-s1 · sahne 05-hyperframes-kapak-b (HyperFrames, 1080×1920, tek kare, ses yok)

Yazan: şef (15.11.2026, istem S1-VAR). Kod yazmaz; tasarım verir. K = `/home/sef/01dev/_worktrees/kalem-0204`.
Sahne dizini D = `K/projeler/02-04-ydt-temel-s1/sahneler/05-hyperframes-kapak-b/`. Paket P = `K/projeler/02-04-ydt-temel-s1/`.
Kaynak: `P/uretim-tutanagi/kapak-taslak.md` §5 (bu sürüm), §7 (A/B/C farkı). Kapak B = soru/merak kapağı; cevap karede YOK.

## 1. Dosyalar

| Dosya | Durum | İş |
|---|---|---|
| `D/uret.py` | YOK | **YAZILACAK** (mutlak yol `/home/sef/01dev/_worktrees/kalem-0204/projeler/02-04-ydt-temel-s1/sahneler/05-hyperframes-kapak-b/uret.py`) |
| `D/yardim.py` | VAR (sahne 01'in birebir kopyası) | DOKUNMA; yalnız `import yardim as Y` |
| `D/cizim/ogretmen.json`, `D/cizim/luggage.svg` | VAR (sahne 01 kopyası) | salt oku |
| `D/calistir.sh`, `D/olay.py`, `D/zamanlar.json` | VAR (şef yazdı) | DOKUNMA |
| `D/nesneler.json` | uret.py yazar | §6 |

Başka dosyaya dokunma. Silme yok. Test, render, snapshot, `calistir.sh`, git YOK. `P/ortak/`, `P/zaman.json` ve başka sahneler salt okunur.

## 2. Kalıp kaynakları (salt oku)

| Kalıp | Mutlak yol | Ne alınır |
|---|---|---|
| İskelet (aynı tür: durağan tek kare) | `K/projeler/02-04-ydt-temel-s1/sahneler/04-hyperframes-hikaye/uret.py` | dosya düzeni, `zaman.json` doğrulaması, HTML kabuğu (`Y.font_css()`, `Y.ZEMIN_CSS`, `#root data-…`, `Y.zemin_html()`, tek `<svg id="sahne" … viewBox="0 0 1080 1920">`, `lib/gsap.min.js`, tek `set` çizelgesi, `window.__timelines["main"]`), blok kutusu + kesişim assert'leri, `__main__` (`proje/`, `Y.font_kopyala`, `proje/index.html`, `nesneler.json`) |
| Başlık konturu, logo, rozet, figür, bavul | `K/projeler/02-04-ydt-temel-s1/sahneler/01-hyperframes-kapak/uret.py` | başlık `<text>` konturu (satır 342–347: `stroke=zemin stroke-width=12 stroke-linejoin=round style="font-kerning:none;paint-order:stroke fill"`); figür çizimi (satır 72–76 ölçek, 276–285 yollar ve parça kalınlıkları `govde 4.4 · sac 3.6 · yuz 2.6` / ölçek); `Y.tabler("luggage", AD / "cizim")`; `<g id="eskiz" fill="none" stroke=murekkep stroke-linecap=round stroke-linejoin=round>` |
| Ev ikonu | `Y.tabler("home")` (24×24 ızgara, çizim y 3→21, x 3→21) | |
| Tema dönüşümü | `P/ortak/hf_tema.py` | §5 |

## 3. Okuma ve sabitler

- `PAKET = AD.parent.parent`. `PAKET/zaman.json` oku. `duragan` listesinde `klasor == AD.name` olan TEK kayıt var assert; o kaydın
  `kare == 1` ve `cikti == "kapak-b.png"` assert. `sahneler[]` içinde `AD.name` YOK assert.
- `Z = D/zamanlar.json`: `sure` 1,0 · `kare` 1 · `fps` 30 assert (sahne 04 ile aynı).
- Anlatım, sözcük, altyazı dosyası OKUNMAZ (ses yok).
- Renk yalnız `Y.RENK` anahtarlarıyla: `zemin #1b1a17`, `murekkep #f3efe6`, `ikincil #c9c2b3`, `vurgu #f2a93b`. Başka hex YOK.
- `W, H = Y.W, Y.H`; `KENAR = 48`; `SAG = 1032`; `BASLIK_GEN = 952` (1080 − 2 × 64); `ZEMIN_Y = 1344`; `PLATFORM = 1536`.

## 4. Yerleşim (y = yazı tabanı, px)

```
y    0 ┌───────────────────────────────────────────┐
       │ [logo 387×96]                              │ HUD (çip YOK, ders adı YOK — kapak A karesiyle aynı)
   216 │ (YDT · BASIC)                              │ rozet 216–288
   ≈480│       YAŞI[YOR]UM                          │ Fredoka 700 S, ortalı, YOR sarı kutuda
   ≈670│      NASIL DENİR?                          │ Fredoka 700 S, ortalı
   860 │ ┌fig┐   ( ev    I live?        )           │ balon 1: 860–1060
       │ │   │ o                                    │ düşünce noktaları
  1100 │ │   │   ( bavul I am living?   )           │ balon 2: 1100–1300
  1344 │─┴───┴──────────────────────────────────── │ zemin çizgisi
  1536 ├───────────────────────────────────────────┤ PLATFORM: boş
```

### 4.1 HUD — `<g id="kunye">`
| Öğe | Ölçü | Renk |
|---|---|---|
| logo `<g id="ku-logo"><image id="logoimg" href="assets/logo.svg" …/>` | x 48, y 48, yükseklik 96, genişlik `96 · Y.LOGO_EN_BOY` | dosya |
| rozet `<g id="rz0">` hap | x 48, y 216, h 72, rx 36, w = `Y.genislik("Lexend", 700, "YDT · BASIC", 36) + 56` | `<rect fill=vurgu>` |
| rozet yazısı | Lexend 700 36, `text-anchor="middle"`, x = hap ortası, taban 265 | `<text fill=zemin>` |

Ders adı ve çip YOK (kapak A'nın kapak karesi t 1,97'de de yok).

### 4.2 Başlık — `<g id="baslik">`
- Satır 1 `YAŞIYORUM` üç parça: `YAŞI` · `YOR` · `UM`. `wa, wy, wu = Y.genislik("Fredoka", 700, parça, S)`. Kutu payı `p = 0,08·S`.
  Satır 1 genişliği `g1 = wa + 2p + wy + wu`.
- Satır 2 `NASIL DENİR?` tek `<text>`: `g2 = Y.genislik("Fredoka", 700, "NASIL DENİR?", S)`.
- Boy `S`: önce boy 100 ile ölç; `S = floor(min(190, 952·100/g1_100, 952·100/g2_100))`; S ile yeniden ölç; `g1 ≤ 952` ve `g2 ≤ 952` assert.
- Taban: `T1 = 375 + 0,70·S`; `T2 = T1 + 1,26·S` (satır 1 kutusu ve Ş çengeli altı + `İ` noktası payı).
- Yatay: iki satır ayrı ayrı ortalı. `x1 = 540 − g1/2`; `YAŞI` x1 → kutu `kx0 = x1 + wa`, `kx1 = kx0 + 2p + wy` → `YOR` x `kx0 + p` →
  `UM` x `kx1`. Satır 2 x = `540 − g2/2`.
- Kutu `<rect id="bk-kutu">`: x kx0, w `kx1 − kx0`, üst `T1 − 0,86·S`, alt `T1 + 0,16·S`, rx `0,10·S`, `fill` vurgu. Kutu `YOR` yazısının ALTINDA çizilir.
- Renk ve kontur: `YAŞI`, `UM`, satır 2 → `fill` murekkep + kontur (`stroke` zemin, `stroke-width` 12, round, paint-order stroke fill).
  `YOR` → `fill` zemin (`#1b1a17`; açık temada pilMetin), KONTURSUZ. id: `bs-yasi`, `bs-yor`, `bs-um`, `bs-2`. **`t2` id YOK.**
- Tek vurgu bu kutudur. Başlıkta başka renk, altçizgi, hap YOK.

### 4.3 Sahne — `<g id="eskiz" fill="none" stroke=murekkep stroke-linecap="round" stroke-linejoin="round">`
| Öğe | Ölçü |
|---|---|
| zemin çizgisi `<path id="zc">` | `M64 1344 L1016 1344`, `stroke-width` 4 |
| figür `<g id="fig">` | `FIG_H = 500`, `fs = FIG_H / (kutu.y1 − kutu.y0)`, figür kutusu sol `FIG_X = 120`, alt = `ZEMIN_Y`; çizim sahne 01 satır 276–285 ile aynı (`translate(FIG_X − x0·fs, (ZEMIN_Y − FIG_H) − y0·fs) scale(fs)`; parça kalınlıkları / fs). `fig_sag = FIG_X + (x1 − x0)·fs`, `fig_ust = ZEMIN_Y − FIG_H` |
| balon 1 `<rect id="bl1">` | x 360, y 860, w 672 (sağ 1032), h 200, rx 56, `stroke-width` 4 |
| balon 2 `<rect id="bl2">` | x 360, y 1100, w 672, h 200, rx 56, `stroke-width` 4 |
| düşünce noktaları `<circle>` | her balon için 2 daire (r 9 ve r 15), `stroke-width` 4. Başlangıç `P0 = (fig_sag + 16, fig_ust + 70)`, bitiş `P1 = (348, balon orta y)`; daireler P0→P1 doğrusunun t = 0,30 (r 9) ve t = 0,68 (r 15) noktasında. Her dairenin sol kenarı ≥ `fig_sag + 10` assert |
| balon ikonu | 24×24 ızgara, kutu 112×112, sol üst (392, balon orta y − 56); `scale(112/24)`, `stroke-width = 4 / ölçek`. Balon 1 = `Y.tabler("home")`, balon 2 = bavul (`Y.tabler("luggage", AD / "cizim")`) |

Balon yazısı (`<text>`, eskiz grubunun DIŞINDA, `fill` murekkep, kontursuz):
- Balon 1 `I live?`, balon 2 `I am living?`. Caveat 700, boy `TB = min(88, floor((1032 − 32 − 528)·100 / genislik("Caveat", 700, "I am living?", 100)))`;
  iki balonda aynı TB; `TB ≥ 72` assert. x 528, taban = balon orta y + 0,30·TB.
- Sağ kenar ≤ 1000 assert (balon içi pay 32).

## 5. Tema (hf_tema.py ile uyum)
- `Y.ZEMIN_CSS` ve `Y.zemin_html()` DEĞİŞTİRMEDEN kullan.
- Renkler SVG özniteliği, küçük harf hex. CSS `style` içinde renk YAZMA (paint-order ve font-kerning style'da kalabilir).
- Dönüşüm: `rect fill #f2a93b` → açıkta `#ffe066` · `text fill #1b1a17` → `#1b2440` · `stroke #1b1a17` → zemin · `#f3efe6` → `#1b2440`.
  Bu yüzden rozet ve `bk-kutu` dolgusu `<rect fill="#f2a93b">`; rozet yazısı ve `YOR` `<text fill="#1b1a17">`.
  `<circle fill=…>` ya da `<path fill="#1b1a17">` YOK (düşünce noktaları `fill="none"`).
- id `t2`, `ku-nokta`, `rz1` KULLANMA.

## 6. Kurallar ve kabul ölçütü (uret.py içinde `assert`)
1. Bütün öğeler x ∈ [48, 1032]; hiçbir öğe y ≥ 1536 değil; başlık ve sahne x ∈ [64, 1016] (zemin çizgisi dahil).
2. Yazı boyu ≥ 64 (HUD rozeti 36 hariç). Başlık 2 satır, toplam 3 sözcük. Her satır ≤ 24 karakter.
3. Bloklar: `hud` (0–288), `baslik` (satır 1 kutu/Ş üstü → satır 2 altı `T2 + 0,10·S`), `fig`, `bl1`, `bl2`. Yazı kutusu y_üst = taban − 0,75·boy
   (`İ` satırında − 0,94·boy), y_alt = taban + 0,25·boy. Çiftler arası kesişim 0; `baslik` alt ile en üst sahne öğesi arası ≥ 48;
   `hud` alt (288) ile başlık üstü arası ≥ 40; `fig` sağ ile balon sol arası ≥ 60; `bl1` alt ile `bl2` üst arası ≥ 24.
4. `nesneler.json`: `[{"ad", "x", "y", "w", "h"}]` tam sayı; bloklar: hud, baslik, bk-kutu, fig, bl1, bl2, bl1-yazi, bl2-yazi.
5. Yasak: emoji, kırmızı, yeşil, gradyan, gölge, `Math.random`, `Date`, try/catch, `opacity:0` başlangıç, hareket (tek `set` dışında tween yok).
6. Ekranda "kanal", QR, süre, cevap ("ikisi de", "kalıcı/geçici") YOK. Python: tür ipuçları bütün işlevlerde.
7. `/usr/bin/python3 uret.py` stdout'a `index.html yazıldı <bayt>` ve `S=<boy> TB=<boy>` basar; hata yoksa çıkış 0.

Kabul (şef koşturur, ajan koşturmaz): `ONIZLE_YALNIZ=1 bash calistir.sh` → "önizleme hazır"; `bash calistir.sh --tema acik|koyu` →
`P/kapak-b.png` ve `D/k/koyu/kapak-b-koyu.png` 1080×1920; taşma, kesik yazı, üst üste binme yok.
