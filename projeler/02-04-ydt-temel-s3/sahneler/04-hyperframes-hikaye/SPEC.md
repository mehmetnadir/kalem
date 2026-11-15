# SPEC — 02-04-ydt-temel-s3 · sahne 04-hyperframes-hikaye (HyperFrames, 1080×1920, tek kare, ses yok)

Yazan: şef (15.11.2026, istem D-S3). Kod yazmaz; tasarım verir. K = `/home/sef/01dev/_worktrees/kalem-0204`.
Sahne dizini D = `K/projeler/02-04-ydt-temel-s3/sahneler/04-hyperframes-hikaye/`. Paket P = `K/projeler/02-04-ydt-temel-s3/`.
Kaynak: `P/BRIEF-S3.md` "Hikâye karesi A" · `P/uretim-tutanagi/hikaye-taslak.md` §2 · `P/uretim-tutanagi/S3-duzeltme.md` madde 1, 4 ·
`K/projeler/present-continuous-dikey/BRIEF-DIKEY.md` §0, §2, §3 · `K/.claude/docs/sozlesme.md` (altçizgi, hap, pilMetin satırları).

## 1. Dosyalar

| Dosya | Durum | İş |
|---|---|---|
| `D/uret.py` | YOK | **YAZILACAK** — mutlak yol `/home/sef/01dev/_worktrees/kalem-0204/projeler/02-04-ydt-temel-s3/sahneler/04-hyperframes-hikaye/uret.py` |
| `D/yardim.py` | VAR (S1 kopyası, sha256 `2cddbe805c13…`) | DOKUNMA; yalnız `import yardim as Y` |
| `D/calistir.sh`, `D/olay.py`, `D/zamanlar.json` | VAR (şef) | DOKUNMA |
| `D/nesneler.json` | YOK | uret.py çalışınca yazar (§7) |

Başka dosyaya dokunma. Silme yok. Test, render, snapshot, git yok. `P/ortak/`, BRIEF, `zaman.json`, başka sahneler salt okunur.

## 2. Kalıp kaynakları (salt oku)

| Kalıp | Mutlak yol | Ne alınır |
|---|---|---|
| İskelet (aynı ders, aynı motor, aynı sahne türü) | `/home/sef/01dev/_worktrees/kalem-0204/projeler/02-04-ydt-temel-s1/sahneler/04-hyperframes-hikaye/uret.py` | Dosya düzeni birebir: docstring, `AD`, `sys.path` + `import yardim as Y`, `PAKET`, `zaman.json` / `zamanlar.json` okuma + assert'ler, `R = Y.RENK`, sabitler, **`kunye_svg()` BİREBİR** (HUD aynı), `kesisim()`, `kurallari_dogrula()` yapısı, `uret()` HTML kabuğu (font_css, ZEMIN_CSS, `#root` div, `Y.zemin_html()`, tek `<svg id="sahne">`, gsap, `window.__timelines["main"]`, iki `tl.set`), `__main__` bloğu (font_kopyala, index.html, nesneler.json, iki print). `ek_svg`, `kart_svg`, `BAVUL`, `NOW_X`, `EK_Y` ve S1 içeriği (`YAŞI-YOR-UM`, `I live`, `PERMANENT`, ev, bavul, bant, now noktası) ALINMAZ |
| Tren ve bilet ızgara verisi + ikon yolu | `/home/sef/01dev/_worktrees/kalem-0204/projeler/02-04-ydt-temel-dikey/sahneler/12-hyperframes-ozet/uret.py` satır 66–148 | `_kutu`, `TREN`, `_bilet`, `BILET`, `_kutusu`, `_daire_yolu`, `ikon_yollari` kopyalanır. `ikon_yollari` imzası değişir: `ikon_yollari(parcalar, mx, my, en, boy)` (modül sabiti `IKON_EN`/`IKON_BOY` yerine parametre); dönüş `[(d, uzunluk, ince)]` aynı. Tür ipuçları eklenir |
| Çizim görünümü (renk, kalınlık, saat 7) | `/home/sef/01dev/_worktrees/kalem-0204/projeler/02-04-ydt-temel/sahneler/05-canvas-ornek3/sahne.js` satır 80–142 | Tren gövdesi kalın, camlar ince, ray ikincil; saat kadran + 4 çentik + yelkovan 12'de + akrep 7'de; bilet kenarı mürekkep, delik ve baskı satırları ikincil |
| Tema dönüşümü | `P/ortak/hf_tema.py` | §6 |

## 3. Okuma ve sabitler

- `PAKET/zaman.json`: `hikaye.klasor == AD.name`, `hikaye.kare == 1`, `hikaye.cikti == "hikaye-a.png"` assert; `AD.name` `sahneler[]` içinde YOK assert.
- `Z = D/zamanlar.json` (`sure` 1,0, `kare` 1, `fps` 30 assert). Anlatım, sözcük, altyazı dosyası OKUNMAZ (ses yok).
- Renk yalnız `Y.RENK` anahtarlarıyla: `zemin #1b1a17`, `murekkep #f3efe6`, `ikincil #c9c2b3`, `vurgu #f2a93b`. Başka hex YOK.
- `g(aile, ağırlık, metin, boy) = Y.genislik(...)`. Her konum aşağıdaki sabitlerden ve `g` ölçümünden türer.
- Bu belgede formüllerdeki virgül ondalık ayırıcıdır (`0,12·S` = `0.12 * S`). Kodda ve SVG değerinde nokta yazılır.

| Ad | Değer | Kaynak |
|---|---|---|
| `W, H` | 1080, 1920 | yardim |
| `KENAR`, `SAG` | 48, 1032 | BRIEF-DIKEY §2 |
| `ICERIK` | (352, 1392); bu karede içerik alt sınırı 1344 | BRIEF-DIKEY §2; istem: 1344–1536 çağrı bandı |
| `CAGRI` | (1344, 1536) | altyazı yok (ses yok) |
| `PLATFORM` | 1536 | altında hiçbir öğe yok |
| `UST_Y` | 404 | `ust` tabanı |
| `BAS_BANT` | (444, 724) | başlık bloğu |
| `KART_Y` | (748, 996) | kart 1, kart 2 üst kenarı |
| `KART_H` | 228 | |
| `ALT_Y` | 1296 | `alt` tabanı |
| `IKON_X` | (664, 1000) | kart içi ikon alanı |

## 4. Yerleşim (y = yazı tabanı, px)

```
y    0 ┌───────────────────────────────────────────┐
       │ [logo 387×96]                [Full lesson] │ HUD: S1 kunye_svg() birebir
   212 │ SIMPLE PRESENT vs                          │
   276 │ PRESENT CONTINUOUS  (YDT · BASIC)          │ rozet 216–288
   404 │ İkisi geleceği anlatıyor                   │ Lexend 500 64, x 48
 ≈ 562 │              TARİFE                        │ Fredoka 700 S (≈124), ortalı
 ≈ 703 │          ( ≠  PLAN )                       │ sarı hap, ortalı; ≠ kalemle çizilir
   748 │ ┌ kart 1 ───────────────────────────────┐  │ 748–976
       │ │ The train leaves …        [tren] (saat)│  │ leaves sarı altçizgi
       │ │ train ──→ timetable                    │  │
   996 │ ┌ kart 2 ───────────────────────────────┐  │ 996–1224
       │ │ I am going …                 [bilet]   │  │ am going sarı altçizgi
       │ │ person ──→ plan                        │  │
  1296 │ Tren tarifeye uyar                         │ Lexend 500 64, x 48
  1418 │ Tam ders:                 [@ydspublishing] │ Caveat 72 · hap sağa hizalı (S1 aynen)
  1498 │ profildeki bağlantı                        │ Caveat 72
  1536 ├───────────────────────────────────────────┤ PLATFORM: boş
  1920 └───────────────────────────────────────────┘
```

### 4.1 Künye (HUD)
S1 `kunye_svg()` işlevini birebir kopyala (logo, `ku-ders1` / `ku-ders2`, `rz0` rozet `YDT · BASIC`, `ku-cip` çip). Çip metni
`Full lesson` (= `P/ortak/kunye.js` `KUNYE.cipler["04-hyperframes-hikaye"]`).

### 4.2 Düz satırlar
| id | Metin | Yazı | x | taban | Renk |
|---|---|---|---|---|---|
| `ust` | `İkisi geleceği anlatıyor` | Lexend 500 64 | 48 | `UST_Y` 404 | murekkep |
| `alt` | `Tren tarifeye uyar` | Lexend 500 64 | 48 | `ALT_Y` 1296 | murekkep |
| `cg1` | `Tam ders:` | Caveat 700 72 | 48 | 1418 | murekkep |
| `cg2` | `profildeki bağlantı` | Caveat 700 72 | 48 | 1498 | murekkep |
| `hap` | `@ydspublishing` hapı | S1 ile aynı: hw = g(Fredoka 700, metin, 64) + 56; x = 1032 − hw; y 1398; h 84; rx 42; rect `fill` vurgu; yazı Fredoka 700 64 ortalı, taban 1462, `fill` zemin | | | |

### 4.3 Başlık bloğu `bas` — `TARİFE` / `≠ PLAN`
- Birim genişlikler (boy 1 için): `w1 = g(Fredoka 700, "TARİFE", 100)/100`; hap içi `wh = 0,36 + 0,50 + 0,24 + g(Fredoka 700, "PLAN", 100)/100 + 0,36`.
- Boy `S = min(190, floor((724 − 444) / 2,25), floor(952 / max(w1, wh)))` (beklenen 124; yükseklik sınırlar). `S ≥ 64` assert.
- `taban1 = round(444 + 0,95·S)`, `taban2 = taban1 + round(1,14·S)`.
- Satır 1 `<text id="bas1">TARİFE</text>`: Fredoka 700 S, x = 540 − g("TARİFE", S)/2, taban `taban1`, `fill` murekkep. Metin elle büyük harf, Türkçe `İ`; `text-transform` YOK.
- Satır 2 hap `<g id="bas2">`:
  - `hw = wh·S`, `hx = 540 − hw/2`, `hh = 1,02·S`, `hy = taban2 − 0,86·S`, `rx = hh/2`. `<rect id="bas2-hap">` `fill` vurgu (açıkta `#ffe066`).
  - `≠` (Fredoka'da glif YOK, `→` da YOK; ikisi de kalemle çizilir — sözleşme): `<g id="esitdegil" fill="none" stroke="#1b1a17" stroke-width="0,12·S" stroke-linecap="round">`
    içinde 3 `<path>`. Merkez `cx = hx + 0,36·S + 0,25·S`. Çubuk 1: `cx − 0,25·S → cx + 0,25·S`, y = `taban2 − 0,47·S`. Çubuk 2: aynı x, y = `taban2 − 0,23·S`.
    Eğik çizgi: `(cx − 0,14·S, taban2 − 0,02·S) → (cx + 0,14·S, taban2 − 0,68·S)`.
  - Renk köprüsü (sözleşme 15.11, 02-04-dikey s13): `<svg>` içine `<style id="esitdegil-stil">#root #esitdegil path{stroke:var(--pilMetin)}</style>`.
    Gerekçe: hf_tema `[stroke="#1b1a17"]`'yi zemine boyar, açık temada ≠ sarı hapta kaybolur. Bu tek CSS satırı dışında `style` içinde renk YOK.
  - `<text id="bas2-yazi">PLAN</text>`: Fredoka 700 S, x = `hx + (0,36 + 0,50 + 0,24)·S`, taban `taban2`, `fill` zemin (`#1b1a17` → açıkta pilMetin `#1b2440`).
- Blok kutusu: x = min(satır 1 x, hx), y = `taban1 − 0,95·S` (İ noktası), sağ = max(satır 1 sağ, hx + hw), alt = `hy + hh`.

### 4.4 Kart (`kart1` y0 = 748, `kart2` y0 = 996; aynı ızgara)
| Öğe | Ölçü | Renk |
|---|---|---|
| çerçeve `<rect>` | x 48, y y0, w 984, h 228, rx 28, `fill="none"`, `stroke-width` 4 | `stroke` murekkep |
| cümle | Fredoka 700 64, x 80, taban y0 + 84, tek `<text xml:space="preserve">`. Kart 1 `The train leaves …`, kart 2 `I am going …` (`…` = U+2026, tek glif) | murekkep |
| odak altçizgisi | önek / odak: kart 1 `The train ` / `leaves`, kart 2 `I ` / `am going`. `x0 = 80 + g(önek) − 4`, `x1 = 80 + g(önek) + g(odak) + 4`, `y = taban + 0,48·64` (sözleşme: g kuyruğuna değmez). `d = M x0 y Q (x0+x1)/2 y+3 x1 y+1`; `stroke-width` 8, round uç, `fill="none"` | `stroke` vurgu |
| etiket | Caveat 700 64, taban y0 + 180. Sözcük 1 x 80; ok; sözcük 2. Kart 1 `train` → `timetable`, kart 2 `person` → `plan`. Ok gövdesi: `xa0 = 80 + g(Caveat, sözcük1, 64) + 18`, `xa1 = xa0 + 64`, `ya = taban − 14`, `d = M xa0 ya Q (xa0+xa1)/2 ya−3 xa1 ya`; ok başı: `(xa1, ya)`'dan iki çizgi, uzunluk 18, açı ±0,5 rad geriye. Sözcük 2 x = `xa1 + 18`. Ok `stroke-width` 4, round uç ve birleşim, `fill="none"` | yazı `fill` murekkep · ok `stroke` murekkep |
| ikonlar | ikon alanı x 664–1000, dikey merkez `yc = y0 + 114`. Hepsi `fill="none"`, round uç ve birleşim; yol koordinatı zaten ölçekli (transform `scale` YOK) | aşağıda |

İkonlar:
- **Kart 1 tren:** `ikon_yollari(TREN, 774, yc, 220, 100)` (beklenen 220 × 76). Normal parça `stroke` murekkep 4; `ince` parça murekkep 3;
  son parça (ray) ikincil 3.
- **Kart 1 saat:** merkez (954, yc), r 46. Kadran `_daire_yolu` murekkep 4. 4 çentik (12, 3, 6, 9 yönü) `0,80·r → 0,64·r` murekkep 3.
  Yelkovan merkezden 12 yönüne `0,66·r`, murekkep 4. Akrep 7'de (açı 210°): uç `(cx + sin(210°)·0,50·r, cy − cos(210°)·0,50·r)`, murekkep 6.
  Rakam yok. Sarı yok (tek vurgu altçizgide ve haplarda kalır).
- **Kart 2 bilet:** `ikon_yollari(BILET, 832, yc, 300, 140)` (beklenen 300 × 117), grup `transform="rotate(-3 832 yc)"`.
  Kenar `stroke` murekkep 4; `ince` parçalar (delik, baskı satırı) ikincil 3.

Çizim sırası kart içinde: çerçeve → ikon → cümle → altçizgi → etiket yazıları → ok.

### 4.5 Olay listesi (tek kare; zaman çizelgesi dışı, anlatım yok)
| Olay | Kare / küresel sn | Cümle · sözcük | Not |
|---|---|---|---|
| bütün öğeler görünür (HUD + `ust` + `bas` + `kart1` + `kart2` + `alt` + `cg1` + `cg2` + `hap`) | kare 0 (yakalama 0,5 sn) / küresel sn yok | — (hikâye karesi sese bağlı değil; metin `hikaye-taslak.md` §2) | `opacity:0` başlangıç yok; giriş/çıkış hareketi yok |

GSAP: S1 ile aynı — `gsap.timeline({ paused: true })`, `#sahne` için 0'da ve `Z["sure"]`'de `set` (opaklık 1, `immediateRender: false`); başka tween YOK.

## 5. Ekran metni (tam liste; başka metin YOK)
`SIMPLE PRESENT vs` · `PRESENT CONTINUOUS` · `YDT · BASIC` · `Full lesson` · `İkisi geleceği anlatıyor` · `TARİFE` · `PLAN` (+ çizilen ≠) ·
`The train leaves …` · `train` · `timetable` · `I am going …` · `person` · `plan` · `Tren tarifeye uyar` · `Tam ders:` · `profildeki bağlantı` · `@ydspublishing`.
Eski metinler YASAK: `İkisi de gelecek`, tam cümleli kartlar (`to İzmir`, `movie theater`). "kanal", QR, süre ("dk"), emoji YOK.

## 6. Tema (hf_tema.py ile uyum)
- `Y.ZEMIN_CSS` ve `Y.zemin_html()` DEĞİŞTİRMEDEN kullan (hf_tema 4 CSS dizgisini harfi harfine arar).
- Renkler SVG özniteliği, küçük harf hex (`fill="#f3efe6"`, `stroke="#f2a93b"`). Tek istisna §4.3 `esitdegil-stil` satırı.
- Dönüşüm: `rect fill #f2a93b` → `#ffe066` · `text fill #1b1a17` → `#1b2440` · `stroke #f2a93b` → `#d9900f` · `#f3efe6` → `#1b2440` · `#c9c2b3` → `#5a6275`.
- id `t2`, `ku-nokta`, `rz1` YOK. `<circle>` ya da `<path>` `fill="#1b1a17"` YOK.

## 7. Kurallar ve kabul ölçütü (uret.py içinde `assert`)
1. Bütün blok kutuları x ∈ [48, 1032]; hiçbir öğe y ≥ 1536 değil (yazı alt sınırı = taban + 0,30·boy).
2. Yazı boyu ≥ 64 (HUD hariç: ders adı 56, rozet 36, çip 40).
3. Her ekran satırı ≤ 24 karakter (`len`); `→` ve `≠` içeren mantıksal satırlar da sayılır (`train → timetable` 17, `≠ PLAN` 6). En uzun `İkisi geleceği anlatıyor` = 24.
4. Blok kutuları: `hud` (48, 0, 984, 288) · `ust` · `bas` · `kart1` · `kart2` · `alt` · `cg1` · `cg2` · `hap`. Yazı kutusu y_üst = taban − 0,75·boy,
   y_alt = taban + 0,30·boy (Caveat) / 0,25·boy (diğer). Çiftler arası kesişim 0; dikey komşular (`hud→ust→bas→kart1→kart2→alt`, `alt→cg1`, `alt→hap`)
   arası boşluk ≥ 16; `cg1`/`cg2` sağ kenarı ile `hap` sol kenarı arası ≥ 24.
5. `ust` üstü ≥ 352; `alt` altı ≤ 1344; `cg1`, `cg2`, `hap` [1344, 1536] içinde.
6. Kart içi: cümle sağ kenarı ve etiket sağ kenarı ≤ 640 (ikon alanı 664'ten 24 önce); altçizgi alt kenarı (y + 1 + 4) < etiket üstü (taban2 − 0,75·64);
   ikon kutuları kartın içinde ve kenardan ≥ 16 (y0 + 16 … y0 + 212; x ≤ 1000); etiket alt kenarı (taban + 0,30·64) ≤ y0 + 212.
7. `nesneler.json`: `[{"ad", "x", "y", "w", "h"}]` tam sayı, 9 blok (§7.4 sırasıyla).
8. Yasak: emoji, kırmızı, yeşil, gradyan (vinyet zeminin kendisidir), gölge, `random`, tarih, try/except, `opacity:0` başlangıç. Python tür ipuçları bütün işlevlerde.
9. `python3 uret.py` stdout: `index.html yazıldı <bayt>` ve `S=<boy>`; çıkış 0.

Kabul (şef koşturur, ajan koşturmaz): `ONIZLE_YALNIZ=1 bash calistir.sh` → "önizleme hazır"; `bash calistir.sh --tema acik|koyu` →
`P/hikaye-a.png` + `P/hikaye.png` (aynı) ve `D/k/hikaye-a-koyu.png`, 1080×1920; karede taşma, kesik yazı, üst üste binme, boş bant yok.
