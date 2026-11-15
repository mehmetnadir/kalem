# SPEC — 02-04-ydt-temel-s1 · sahne 06-hyperframes-kapak-c (HyperFrames, 1080×1920, tek kare, ses yok)

Yazan: şef (15.11.2026, istem S1-VAR). Kod yazmaz; tasarım verir. K = `/home/sef/01dev/_worktrees/kalem-0204`.
Sahne dizini D = `K/projeler/02-04-ydt-temel-s1/sahneler/06-hyperframes-kapak-c/`. Paket P = `K/projeler/02-04-ydt-temel-s1/`.
Kaynak: `P/uretim-tutanagi/kapak-taslak.md` §6 (bu sürüm), §7. Kapak C = karşıt çift: İngilizce çift başlıkta, Türkçe anlam etikette.

## 1. Dosyalar

| Dosya | Durum | İş |
|---|---|---|
| `D/uret.py` | YOK | **YAZILACAK** (mutlak yol `/home/sef/01dev/_worktrees/kalem-0204/projeler/02-04-ydt-temel-s1/sahneler/06-hyperframes-kapak-c/uret.py`) |
| `D/yardim.py` | VAR (sahne 01'in birebir kopyası) | DOKUNMA; yalnız `import yardim as Y` |
| `D/cizim/ogretmen.json`, `D/cizim/luggage.svg` | VAR (sahne 01 kopyası) | salt oku |
| `D/calistir.sh`, `D/olay.py`, `D/zamanlar.json` | VAR (şef yazdı) | DOKUNMA |
| `D/nesneler.json` | uret.py yazar | §6 |

Başka dosyaya dokunma. Silme yok. Test, render, snapshot, `calistir.sh`, git YOK. `P/ortak/`, `P/zaman.json` ve başka sahneler salt okunur.

## 2. Kalıp kaynakları (salt oku)

| Kalıp | Mutlak yol | Ne alınır |
|---|---|---|
| İskelet (aynı tür: durağan tek kare) | `K/projeler/02-04-ydt-temel-s1/sahneler/04-hyperframes-hikaye/uret.py` | dosya düzeni, `zaman.json` doğrulaması, HTML kabuğu (`Y.font_css()`, `Y.ZEMIN_CSS`, `#root data-…`, `Y.zemin_html()`, tek `<svg id="sahne" … viewBox="0 0 1080 1920">`, `lib/gsap.min.js`, tek `set` çizelgesi, `window.__timelines["main"]`), blok kutusu + kesişim assert'leri, `__main__` (`proje/`, `Y.font_kopyala`, `proje/index.html`, `nesneler.json`) |
| Başlık konturu, logo, rozet, figür, bavul | `K/projeler/02-04-ydt-temel-s1/sahneler/01-hyperframes-kapak/uret.py` | başlık `<text>` konturu (satır 342–347: `stroke=zemin stroke-width=12 stroke-linejoin=round style="font-kerning:none;paint-order:stroke fill"`); figür çizimi (satır 72–76 ölçek, 276–285 yollar ve parça kalınlıkları `govde 4.4 · sac 3.6 · yuz 2.6` / ölçek); bavul grubu (satır 287–292: `Y.tabler("luggage", AD / "cizim")` + iç dolgu `rect bvd` YOK, bu sahnede bavul boş çizilir); `<g id="eskiz" fill="none" stroke=murekkep stroke-linecap=round stroke-linejoin=round>` |
| Ev ikonu | `Y.tabler("home")` (24×24 ızgara, çizim x 3→21, y 3→21) | |
| Tema dönüşümü | `P/ortak/hf_tema.py` | §5 |

## 3. Okuma ve sabitler

- `PAKET = AD.parent.parent`. `PAKET/zaman.json` oku. `duragan` listesinde `klasor == AD.name` olan TEK kayıt var assert; o kaydın
  `kare == 1` ve `cikti == "kapak-c.png"` assert. `sahneler[]` içinde `AD.name` YOK assert.
- `Z = D/zamanlar.json`: `sure` 1,0 · `kare` 1 · `fps` 30 assert.
- Anlatım, sözcük, altyazı dosyası OKUNMAZ (ses yok).
- Renk yalnız `Y.RENK` anahtarlarıyla: `zemin #1b1a17`, `murekkep #f3efe6`, `ikincil #c9c2b3`, `vurgu #f2a93b`. Başka hex YOK.
- `W, H = Y.W, Y.H`; `KENAR = 48`; `SAG = 1032`; `BASLIK_GEN = 952`; `ZEMIN_Y = 1344`; `PLATFORM = 1536`.

## 4. Yerleşim (y = yazı tabanı, px)

```
y    0 ┌───────────────────────────────────────────┐
       │ [logo 387×96]                              │ HUD (çip YOK, ders adı YOK — kapak A karesiyle aynı)
   216 │ (YDT · BASIC)                              │ rozet 216–288
   ≈480│   I LIVE                                   │ Fredoka 700 S, sol hizalı blok
   ≈633│   I [AM LIVING]                            │ AM LIVING sarı kutuda
  ≈1000│  kalıcı                         geçici     │ Caveat 700 88 etiketler
       │  ┌ev┐          fig            ┌bavul┐      │
  1344 │──┴──┴──────────┴┴─────────────┴─────┴──── │ zemin çizgisi
  1536 ├───────────────────────────────────────────┤ PLATFORM: boş
```

### 4.1 HUD — `<g id="kunye">`
| Öğe | Ölçü | Renk |
|---|---|---|
| logo `<g id="ku-logo"><image id="logoimg" href="assets/logo.svg" …/>` | x 48, y 48, yükseklik 96, genişlik `96 · Y.LOGO_EN_BOY` | dosya |
| rozet `<g id="rz0">` hap | x 48, y 216, h 72, rx 36, w = `Y.genislik("Lexend", 700, "YDT · BASIC", 36) + 56` | `<rect fill=vurgu>` |
| rozet yazısı | Lexend 700 36, `text-anchor="middle"`, x = hap ortası, taban 265 | `<text fill=zemin>` |

### 4.2 Başlık — `<g id="baslik">` (karşıt çift)
- Metin: satır 1 `I LIVE`, satır 2 `I AM LIVING`. Ölçü `g(m) = Y.genislik("Fredoka", 700, m, S)`.
- Satır 2 iki parça: `I` (x0) ve `AM LIVING` (x `x0 + g("I ")`). Kutu payı `p = 0,08·S`.
  Kutu `<rect id="bk-kutu">`: sol `x0 + g("I ") − p`, sağ `x0 + g("I AM LIVING") + p`; üst `T2 − 0,86·S`, alt `T2 + 0,16·S`; rx `0,10·S`; `fill` vurgu.
  Kutu sol kenarı `x0 + g("I") + 0,04·S`'den büyük olmalı (kutu `I` harfine değmez) — assert.
- Blok genişliği `gb = g("I AM LIVING") + p`. Boy: önce 100 ile ölç; `S = floor(min(190, 952·100/gb_100))`; S ile yeniden ölç; `gb ≤ 952` assert.
- Hizalama: blok ortalı, iki satır AYNI sol x: `x0 = 540 − gb/2`. Satır 1 `I LIVE` x0'da başlar (iki `I` alt alta).
- Taban: `T1 = 375 + 0,70·S`; `T2 = T1 + 1,02·S` (satır 1 altı + 0,14·S boşluk + kutu üst payı).
- Renk ve kontur: satır 1 ve satır 2'deki `I` → `fill` murekkep + kontur (`stroke` zemin, `stroke-width` 12, round, paint-order stroke fill).
  `AM LIVING` → `fill` zemin (`#1b1a17`; açık temada pilMetin), KONTURSUZ. id: `bs-1`, `bs-2i`, `bs-2v`. **`t2` id YOK.**
- Tek vurgu bu kutudur (fiil öbeği `AM LIVING`; yalnız `ING` DEĞİL). Başlıkta başka renk, altçizgi, hap YOK.

### 4.3 Sahne — `<g id="eskiz" fill="none" stroke=murekkep stroke-linecap="round" stroke-linejoin="round">`
| Öğe | Ölçü |
|---|---|
| zemin çizgisi `<path id="zc">` | `M64 1344 L1016 1344`, `stroke-width` 4 |
| ev `<g id="ev">` | `Y.tabler("home")`, ölçek `EV_S = 15` (çizim 18·15 = 270 px). Izgara (3, 21) noktası (88, 1344)'e oturur: `translate(88 − 3·EV_S, 1344 − 21·EV_S) scale(EV_S)`, `stroke-width = 4 / EV_S`. Ev kutusu x 88–358, y 1074–1344 |
| figür `<g id="fig">` | `FIG_H = 480`, `fs = FIG_H / (kutu.y1 − kutu.y0)`, figür genişliği `fw = (x1 − x0)·fs`, `FIG_X = 540 − fw/2`, alt = `ZEMIN_Y`; çizim sahne 01 satır 276–285 ile aynı. Eli boş (bavul figürün elinde DEĞİL) |
| bavul `<g id="bavul">` | `Y.tabler("luggage", AD / "cizim")`, ölçek `BV_S = 11` (çizim 12·11 = 132 px geniş, 18·11 = 198 px yüksek). Izgara (18, 21) noktası (952, 1344)'e oturur: `translate(952 − 18·BV_S, 1344 − 21·BV_S) scale(BV_S)`, `stroke-width = 4 / BV_S`. Bavul kutusu x 820–952, y 1146–1344 |

Etiketler (`<text>`, eskiz grubunun DIŞINDA, `fill` murekkep, kontursuz, Caveat 700 88, `text-anchor="middle"`):
- `kalıcı`: x = ev ortası (223), taban = ev üstü (1074) − 36.
- `geçici`: x = bavul ortası (886), taban = bavul üstü (1146) − 36.
- id: `et-kalici`, `et-gecici`.

## 5. Tema (hf_tema.py ile uyum)
- `Y.ZEMIN_CSS` ve `Y.zemin_html()` DEĞİŞTİRMEDEN kullan.
- Renkler SVG özniteliği, küçük harf hex. CSS `style` içinde renk YAZMA.
- Dönüşüm: `rect fill #f2a93b` → açıkta `#ffe066` · `text fill #1b1a17` → `#1b2440` · `stroke #1b1a17` → zemin · `#f3efe6` → `#1b2440`.
  Rozet ve `bk-kutu` dolgusu `<rect fill="#f2a93b">`; rozet yazısı ve `AM LIVING` `<text fill="#1b1a17">`. `<path fill="#1b1a17">` YOK.
- id `t2`, `ku-nokta`, `rz1` KULLANMA.

## 6. Kurallar ve kabul ölçütü (uret.py içinde `assert`)
1. Bütün öğeler x ∈ [48, 1032]; hiçbir öğe y ≥ 1536 değil; başlık ve sahne x ∈ [64, 1016].
2. Yazı boyu ≥ 64 (HUD rozeti 36 hariç). Başlık 2 satır. Her satır ≤ 24 karakter.
3. Bloklar: `hud` (0–288), `baslik` (satır 1 üstü `T1 − 0,75·S` → kutu altı), `et-kalici`, `et-gecici`, `ev`, `fig`, `bavul`.
   Yazı kutusu y_üst = taban − 0,75·boy, y_alt = taban + 0,30·boy (Caveat) / 0,25·boy (diğer). Çiftler arası kesişim 0;
   `baslik` alt ile en üst sahne öğesi arası ≥ 48; `hud` alt ile başlık üstü arası ≥ 40; ev–fig ve fig–bavul yatay ara ≥ 60;
   etiket alt ile kendi ikonu üstü arası ≥ 12.
4. `nesneler.json`: `[{"ad", "x", "y", "w", "h"}]` tam sayı; bloklar: hud, baslik, bk-kutu, et-kalici, et-gecici, ev, fig, bavul.
5. Yasak: emoji, kırmızı, yeşil, gradyan, gölge, `Math.random`, `Date`, try/catch, `opacity:0` başlangıç, hareket (tek `set` dışında tween yok).
6. Ekranda "kanal", QR, süre YOK. Python: tür ipuçları bütün işlevlerde.
7. `/usr/bin/python3 uret.py` stdout'a `index.html yazıldı <bayt>` ve `S=<boy>` basar; hata yoksa çıkış 0.

Kabul (şef koşturur, ajan koşturmaz): `ONIZLE_YALNIZ=1 bash calistir.sh` → "önizleme hazır"; `bash calistir.sh --tema acik|koyu` →
`P/kapak-c.png` ve `D/k/koyu/kapak-c-koyu.png` 1080×1920; taşma, kesik yazı, üst üste binme yok.
