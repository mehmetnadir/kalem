# SPEC — 02-04-ydt-temel-s2 · sahne 05-hyperframes-kapak-b (HyperFrames, 1080×1920, tek kare, ses yok)

Yazan: şef (15.11.2026, istem D-S2 05). Kod yazmaz; tasarım verir. K = `/home/sef/01dev/_worktrees/kalem-0204`.
Sahne dizini D = `K/projeler/02-04-ydt-temel-s2/sahneler/05-hyperframes-kapak-b/`. Paket P = `K/projeler/02-04-ydt-temel-s2/`.
Kaynak: `P/BRIEF-S2.md` "Kapak B ve Kapak C" tablosu B sütunu · `P/uretim-tutanagi/kapak-taslak.md` §4, §6 B satırı.
Kapak B = soru / merak kapağı. Cevap karede YOK (zaman adı, "wears", "is wearing" yazılmaz).

## 1. Dosyalar

| Dosya | Durum | İş |
|---|---|---|
| `D/uret.py` | YOK | **YAZILACAK** (mutlak yol `/home/sef/01dev/_worktrees/kalem-0204/projeler/02-04-ydt-temel-s2/sahneler/05-hyperframes-kapak-b/uret.py`) |
| `D/yardim.py` | VAR (S1 sahne 05 kopyası) | DOKUNMA; yalnız `import yardim as Y` |
| `D/cizim/ogretmen-dusunen.json`, `D/cizim/question-mark.svg` | VAR (şef hazırladı) | salt oku |
| `D/calistir.sh`, `D/olay.py`, `D/zamanlar.json` | VAR (şef) | DOKUNMA |
| `D/nesneler.json` | uret.py yazar | §6 madde 4 |

Başka dosyaya dokunma. Silme yok. Test, render, snapshot, `calistir.sh`, git YOK. `P/ortak/`, `P/zaman.json` ve başka sahneler salt okunur.

## 2. Kalıp kaynakları (salt oku)

| Kalıp | Mutlak yol | Ne alınır |
|---|---|---|
| İskelet (aynı tür, aynı ders, durağan tek kare) | `/home/sef/01dev/_worktrees/kalem-0204/projeler/02-04-ydt-temel-s1/sahneler/05-hyperframes-kapak-b/uret.py` | dosya düzeni; `zaman.json` + `zamanlar.json` doğrulaması (AYNEN, `cikti == "kapak-b.png"`); `kunye_svg()` (logo + rozet; AYNEN); başlık `<text>` konturu (`fill` murekkep, `stroke` zemin, `stroke-width` 12, round, `style="font-kerning:none;paint-order:stroke fill"`, `xml:space="preserve"`); `hesapla_s()` döngüsü (önce 100 ile ölç, sonra küçült); `kesisim()`; HTML kabuğu (`Y.font_css()`, `Y.ZEMIN_CSS`, `#sahne` CSS, `#root data-…`, `Y.zemin_html()`, tek `<svg id="sahne" viewBox="0 0 1080 1920">`, `lib/gsap.min.js`, iki `set` satırı, `window.__timelines["main"]`); `__main__` (`proje/`, `Y.font_kopyala`, `proje/index.html`, `nesneler.json`, stdout) |
| Takvim ikonu | `Y.tabler("calendar")` (`P/ortak/cizim/tabler/calendar.svg`) | dönen listenin İLK 4 yolu: `M4 7a2…` (sayfa), `M16 3v4`, `M8 3v4` (halkalar), `M4 11h16` (başlık çizgisi). 5. ve 6. yol (rakam) KULLANILMAZ. Her birinin başını assert et |
| Soru işareti | `Y.tabler("question-mark", AD / "cizim")` | 2 yol: kıvrım (`M8 8a3.5 3…`) + nokta (`M12 19l0 .01`). Izgara x 8→16, y 5→19 |
| Figür | `AD / "cizim" / "ogretmen-dusunen.json"` | alanlar: `kutu` [x0,y0,x1,y1] = [30.4, 54.6, 927.6, 1157.5] · `bas` = [264.6, 54.6, 656.7, 522.6] · `el` = [812.5, 543.5] (yumruk ortası) · `el_kutu` = [721, 410, 866, 714] · `yollar` = 5 kayıt `{parca, dolgu, d}` (sıra: govde beyaz, govde murekkep, sac beyaz, sac murekkep, yuz murekkep) |

## 3. Okuma ve sabitler

- `PAKET = AD.parent.parent`. `zaman.json`: `duragan` içinde `klasor == AD.name` TEK kayıt; `kare == 1`, `cikti == "kapak-b.png"`;
  `sahneler[]` içinde `AD.name` YOK. `zamanlar.json`: `sure` 1,0 · `kare` 1 · `fps` 30 (S1 ile aynı assert'ler).
- Anlatım, sözcük, altyazı dosyası OKUNMAZ (ses yok).
- Renk yalnız `Y.RENK` anahtarlarıyla: `zemin #1b1a17`, `murekkep #f3efe6`, `vurgu #f2a93b`. Başka hex YOK.
- `KENAR = 48`, `SAG = 1032`, `BASLIK_GEN = 952`, `ZEMIN_Y = 1344`, `PLATFORM = 1536`.

## 4. Yerleşim (px; y = yazı tabanı)

```
y    0 ┌───────────────────────────────────────────┐
    48 │ [logo 387×96]                              │ HUD 0–288 (çip YOK, ders adı YOK — S1 kapak B ile aynı)
   216 │ (YDT · BASIC)                              │ rozet 216–288
  ≈495 │         TODAY VARSA                        │ Fredoka 700 S, ortalı, mürekkep + kontur
  ≈661 │        HANGİ ZAMAN?                        │ Fredoka 700 S, ortalı (İ noktalı)
  ≈760 │            ┌○──────○┐                      │ takvim yaprağı (halkalar), +4° eğik
       │   ( baş )  │────────│      ╭─╮             │
       │    ☝ yumruk│ today  │        │  büyük ?     │ ? vurgu çizgisi (kalem görünümü)
  1093 │  ╱ gövde ╲ └────────┘        •             │
  1344 │─┴─────────┴────────────────────────────── │ zemin çizgisi (masa kenarı); büst alt kenarı burada
  1536 ├───────────────────────────────────────────┤ PLATFORM: boş (1344–1536 de boş: ses yok)
```

### 4.1 HUD — `<g id="kunye">`
S1 `kunye_svg()` AYNEN: logo `<g id="ku-logo"><image id="logoimg" href="assets/logo.svg" x="48" y="48" height="96" width=96·Y.LOGO_EN_BOY/>`;
rozet `<g id="rz0">` hap x 48, y 216, h 72, rx 36, w = `Y.genislik("Lexend", 700, "YDT · BASIC", 36) + 56`, `<rect fill=vurgu>`;
yazı Lexend 700 36, ortalı, taban 265, `<text fill=zemin>`. Logo sol üstte (BRIEF-DIKEY §0 Nadir bulgusu: alt bantta logo yok).

### 4.2 Başlık — `<g id="baslik">` (hapsız, tek renk mürekkep)
- Satır 1 `TODAY VARSA` (`<text id="bs-1">`), satır 2 `HANGİ ZAMAN?` (`<text id="bs-2">`, `İ` = U+0130). İkisi de Fredoka 700, AYNI boy `S`.
- `g1_100 = Y.genislik("Fredoka", 700, "TODAY VARSA", 100)`, `g2_100` aynı biçimde. `S = floor(min(190, 952·100/g1_100, 952·100/g2_100))`;
  S ile yeniden ölç; `g1 ≤ 952`, `g2 ≤ 952` değilse S'yi 1 azaltarak döngü (S1 `hesapla_s` gibi). Beklenen S = 132 (g2 ≈ 950).
- Taban (başlık bloğu 288–768 bandının ortasında, merkez 528): `T1 = 528 − 0,25·S`; `T2 = T1 + 1,26·S`. Beklenen T1 ≈ 495, T2 ≈ 661,3.
- Yatay: iki satır ayrı ayrı ortalı: `x1 = 540 − g1/2`, `x2 = 540 − g2/2` (`text-anchor` YOK; x sol kenar).
- Kontur S1 başlığıyla aynı (bkz. §2). Başlıkta hap, kutu, sarı, altçizgi YOK. id `t2` YOK.

### 4.3 Sahne — çizim sırası (z): `zc` → `takvim` → `tk-yazi-g` → `fig` → `soru`

**Zemin çizgisi** `<path id="zc" d="M64 1344 L1016 1344" fill="none" stroke=murekkep stroke-width="4" stroke-linecap="round"/>`.

**Figür** `<g id="fig" transform="translate(tx ty) scale(fs)">` — DOLGU ile çizilir (kontur YOK):
- `FIG_H = 480`, `FIG_X = 64`, `FIG_UST = ZEMIN_Y − FIG_H = 864`. `x0, y0, x1, y1 = kutu`; `fs = FIG_H / (y1 − y0)` (≈ 0,43522);
  `tx = FIG_X − x0·fs`, `ty = FIG_UST − y0·fs`. Kanvas → px dönüşümü: `px(x, y) = (FIG_X + (x − x0)·fs, FIG_UST + (y − y0)·fs)`.
- `yollar` JSON sırasıyla: `dolgu == "beyaz"` → `<path class="dz" fill="#1b1a17" d="…"/>` (örtücü zemin dolgusu: yumruk takvimin köşesini
  örter); `dolgu == "murekkep"` → `<path fill="#f3efe6" fill-rule="evenodd" d="…"/>`. `stroke` özniteliği YOK.
- `<style>` içine tek kural ekle: `#root .dz{fill:var(--zemin,#1b1a17)}` (tema köprüsü: `hf_tema.py` `--zemin` değişkenini tanımlar;
  path `fill="#1b1a17"` için hf_tema eşlemesi yoktur). Başka CSS renk kuralı YOK.
- Türetilen px değerleri (assert ve blok için): `G = px(*el)` (≈ 404,4 · 1076,8 — yumruk ortası);
  `el_px = px(el_kutu)` kutusu (≈ x 364,6–427,7 · y 1018,7–1151,0); `bas_px = px(bas)` (≈ x 165,9–336,6 · y 864–1067,7);
  `fig` kutusu x `FIG_X` → `FIG_X + (x1 − x0)·fs` (≈ 454,5), y 864 → 1344.

**Takvim yaprağı** `<g id="takvim" transform="rotate(4 Gx Gy) translate(Ox Oy) scale(k)" fill="none" stroke=murekkep
stroke-width="{6/k}" stroke-linecap="round" stroke-linejoin="round">` + §2'deki 4 Tabler yolu (her biri `<path d="…"/>`):
- `k = 300 / 16 = 18,75` (sayfa 300 × 300 px). Sayfanın sol alt köşesi (Tabler noktası (4, 21)) yumruğun arkasında:
  `C = (Gx − 14, Gy + 16)`; `Ox = Cx − 4·k`, `Oy = Cy − 21·k`. Dönme `rotate(4 Gx Gy)` = yumruk etrafında saat yönünde 4°.
- Döndürülmemiş px: sayfa x `Cx` → `Cx + 300`, y `Oy + 5k` → `Cy`; halka üstü `Oy + 3k`; başlık çizgisi `Hy = Oy + 11k`.
- `takvim` bloğu = şu 6 noktanın G etrafında +4° döndürülmüş hâllerinin sınır kutusu, her yana +3 px (kontur payı):
  sayfa 4 köşesi + halka üstleri `(Ox + 8k, Oy + 3k)`, `(Ox + 16k, Oy + 3k)`. Dönme: `(dx, dy) → (dx·cos − dy·sin, dx·sin + dy·cos)`, 4° radyan.

**Takvim yazısı** `<g id="tk-yazi-g" transform="rotate(4 Gx Gy)"><text id="tk-yazi" …>today</text></g>`:
- Caveat 700, `fill` murekkep, kontursuz, `text-anchor="middle"`, küçük harf `today`.
- Yazı alanı (döndürülmemiş): sol sınır `XL = el_px.sağ + 16`, sağ sınır `XR = Cx + 300 − 24`.
  `TT = min(100, floor((XR − XL)·100 / Y.genislik("Caveat", 700, "today", 100)))`; `TT ≥ 72` assert. Beklenen TT = 100.
- x = `(XL + XR) / 2`; taban = `(Hy + Cy) / 2 + 0,30·TT`.
- `takvim-yazi` bloğu = yazı kutusunun (x merkez ± w/2, y taban − 0,75·TT → taban + 0,30·TT) 4 köşesinin G etrafında +4° döndürülmüş sınırı.

**Soru işareti** `<g id="soru" transform="translate(QX QY) scale(q)" fill="none" stroke=vurgu stroke-width="{26/q}"
stroke-linecap="round" stroke-linejoin="round">` + §2'deki 2 yol:
- `q = 27`. Sağ kenar: `16·q + QX = 1000 − 13` → `QX = 987 − 16q`. Üst: `5·q + QY = 890 + 13` → `QY = 903 − 5q`.
- `soru` bloğu: x `8q + QX − 13` → `16q + QX + 13`, y `5q + QY − 13` → `19q + QY + 13` (≈ x 758–1000 · y 890–1294).
- Tek vurgu rengi bu `?`'dir (rozet hapı künye öğesidir). Başka vurgu YOK.

## 5. Tema (hf_tema.py ile uyum)
- `Y.ZEMIN_CSS` ve `Y.zemin_html()` DEĞİŞTİRMEDEN kullan (hf_tema birebir dize arar).
- Renkler SVG özniteliği, küçük harf hex. Dönüşüm: `#f3efe6` (fill/stroke) → mürekkep · `stroke #f2a93b` → vurgu (açıkta `#d9900f`) ·
  `rect fill #f2a93b` → vurguDolgu (açıkta `#ffe066`) · `text fill #1b1a17` → pilMetin · `stroke #1b1a17` → zemin.
  Bu yüzden rozet `<rect fill="#f2a93b">` + `<text fill="#1b1a17">`; figür dolgusu `fill="#f3efe6"`; `?` `stroke="#f2a93b"`.
- `.dz` yolları `fill="#1b1a17"` taşır ve §4.3 CSS kuralıyla temaya bağlanır. `<circle>` YOK. id `t2`, `ku-nokta`, `rz1` KULLANMA.

## 6. Kurallar ve kabul ölçütü (uret.py içinde `assert`)
1. Bütün bloklar x ∈ [48, 1032]; hiçbir blok y + h > 1536 değil. `baslik`, `fig`, `takvim`, `soru`, `zc` x ∈ [64, 1016];
   `fig`, `takvim`, `soru` alt kenarı ≤ 1344 + 4.
2. Yazı boyu: `S ≥ 64`, `TT ≥ 72` (HUD rozeti 36 hariç). Satırlar `["YDT · BASIC", "TODAY VARSA", "HANGİ ZAMAN?", "today"]` her biri ≤ 24
   karakter. Başlık 2 satır, toplam 4 sözcük. `"HANGİ"` içinde U+0130 assert.
3. Bloklar: `hud` (48, 0, 984, 288) · `baslik` (x min(x1,x2), y `T1 − 0,86·S` → `T2 + 0,10·S`) · `fig` · `bas` (`bas_px`) · `el` (`el_px`) ·
   `takvim` · `takvim-yazi` · `soru` · `zc` (64, 1342, 952, 4).
   Kesişim 0 olmalı: [hud, baslik, takvim, soru] çiftlerinin hepsi; `baslik`–`fig`; `fig`–`soru`; `bas`–`takvim`; `el`–`takvim-yazi`.
   `fig`–`takvim` kesişimi SERBEST (el yaprağı tutar). `takvim-yazi` tamamen `takvim` içinde.
   Boşluk: `baslik.y − 288 ≥ 40`; `min(takvim.y, fig.y, soru.y) − baslik.alt ≥ 48`; `soru.x − takvim.sağ ≥ 32`; `takvim.x − bas.sağ ≥ 32`;
   başlık satır 1 alt (`T1 + 0,25·S`) < satır 2 `İ` noktası üstü (`T2 − 0,94·S`).
4. `nesneler.json`: `[{"ad", "x", "y", "w", "h"}]` tam sayı (round); §6.3 bloklarının hepsi, bu sırayla.
5. Hex beyaz listesi: `re.findall(r"#[0-9a-fA-F]{6}\b", html)` kümesi ⊆ {`#1b1a17`, `#f3efe6`, `#c9c2b3`, `#f2a93b`}.
6. Yasak (html küçük harfte arama): `kanal`, `qr`, `6 dk`, `wears`, `is wearing`, `ikisi de`, `şimdiki`, `geniş`, `math.random`, `date.now`,
   `new date`, `opacity:0`. Emoji, kırmızı, yeşil, gradyan (zemin vinyeti hariç), gölge, try/catch, tek `set` çifti dışında tween YOK.
7. Python: bütün işlevlerde tür ipuçları; `from __future__ import annotations`. `/usr/bin/python3 uret.py` stdout'a
   `index.html yazıldı <bayt>` ve `S=<S> TT=<TT> fs=<fs:.5f>` basar; hata yoksa çıkış 0.

Kabul (şef koşturur, ajan koşturmaz): `ONIZLE_YALNIZ=1 bash calistir.sh` → "önizleme hazır"; `bash calistir.sh --tema acik|koyu` →
`P/kapak-b.png` ve `D/k/koyu/kapak-b-koyu.png` 1080×1920; taşma, kesik yazı, üst üste binme yok; yumruk takvim köşesini örter.
