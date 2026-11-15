# SPEC — 02-04-ydt-temel-s2 · sahne 06-hyperframes-kapak-c (HyperFrames, 1080×1920, tek kare, ses yok)

Yazan: şef (15.11.2026, istem D-S2). Kod yazmaz; tasarım verir. K = `/home/sef/01dev/_worktrees/kalem-0204`.
Sahne dizini D = `K/projeler/02-04-ydt-temel-s2/sahneler/06-hyperframes-kapak-c/`. Paket P = `K/projeler/02-04-ydt-temel-s2/`.
Kaynak: `P/BRIEF-S2.md` "Kapak B ve Kapak C" tablosu C sütunu · `P/uretim-tutanagi/kapak-taslak.md` §5, §6 C satırı.
Kapak C = karşıt çift: aynı fiil (*wear*) iki zamanda; iki cümle kartı üst üste; figür YOK.

## 1. Dosyalar

| Dosya | Durum | İş |
|---|---|---|
| `D/uret.py` | YOK | **YAZILACAK** — mutlak yol `/home/sef/01dev/_worktrees/kalem-0204/projeler/02-04-ydt-temel-s2/sahneler/06-hyperframes-kapak-c/uret.py` |
| `D/yardim.py` | VAR (S1 sahne 06 kopyası) | DOKUNMA; yalnız `import yardim as Y` |
| `D/calistir.sh`, `D/olay.py`, `D/zamanlar.json` | VAR (şef kopyaladı) | DOKUNMA |
| `D/nesneler.json` | uret.py yazar | §7 madde 4 |

Başka dosyaya dokunma. Silme yok. Test, render, snapshot, `calistir.sh`, git YOK. `P/ortak/`, `P/zaman.json`, başka sahneler salt okunur.

## 2. Kalıp kaynağı (salt oku)

| Kalıp | Mutlak yol | Ne alınır |
|---|---|---|
| İskelet (aynı tür, aynı ders, durağan tek kare) | `/home/sef/01dev/_worktrees/kalem-0204/projeler/02-04-ydt-temel-s1/sahneler/06-hyperframes-kapak-c/uret.py` | dosya düzeni; `zaman.json` + `zamanlar.json` doğrulaması (aynen); `kunye_svg()` (logo + rozet; aynen); başlık `<text>` konturu (`bs-1`); `kesisim()`; HTML kabuğu (`Y.font_css()`, `Y.ZEMIN_CSS`, `#sahne` CSS, `#root data-…`, `Y.zemin_html()`, tek `<svg id="sahne" viewBox="0 0 1080 1920">`, `lib/gsap.min.js`, iki `set` satırı, `window.__timelines["main"]`); `__main__` (`proje/`, `Y.font_kopyala`, `proje/index.html`, `nesneler.json`, stdout) |
| Kart çerçevesi + odak altçizgisi | `/home/sef/01dev/_worktrees/kalem-0204/projeler/02-04-ydt-temel-s1/sahneler/04-hyperframes-hikaye/uret.py` `kart_svg()` | `<rect fill="none" stroke=murekkep stroke-width="4">`; odak yolu biçimi `M x0 y Q orta y+3 x1 y+1` (`stroke=vurgu`, `stroke-linecap="round"`) |
| Mont / tişört darbe dizileri | `/home/sef/01dev/_worktrees/kalem-0204/projeler/02-04-ydt-temel/sahneler/03-paperjs-ornek1/sahne-03.js` satır 17–32 | `MONT` (ızgara 100×120) ve `TISORT` (ızgara 100×90) dizilerini Python sabitine BİREBİR çevir; kaynak yolunu yorumda yaz |

S1'den ALINMAYAN: ev, figür, bavul, zemin çizgisi, etiketler, sarı başlık kutusu (`bk-kutu`), `cizim/` klasörü.

## 3. Okuma ve sabitler

- `PAKET = AD.parent.parent`. `PAKET/zaman.json`: `duragan` içinde `klasor == AD.name` TEK kayıt; `kare == 1`; `cikti == "kapak-c.png"`;
  `sahneler[]` içinde `AD.name` YOK (S1 ile aynı assert'ler).
- `D/zamanlar.json`: `sure` 1,0 · `kare` 1 · `fps` 30 assert.
- Anlatım, sözcük, altyazı dosyası OKUNMAZ (ses yok).
- Renk yalnız `Y.RENK` anahtarlarıyla: `zemin #1b1a17`, `murekkep #f3efe6`, `vurgu #f2a93b`. Başka hex YOK (`ikincil` de kullanılmaz).
- `W, H = Y.W, Y.H` · `KENAR = 48` · `SAG = 1032` · `BASLIK_GEN = 952` · `SAHNE_UST = 864` · `SAHNE_ALT = 1344` · `PLATFORM = 1536`.

## 4. Olay listesi

| Olay | Kare / küresel sn | Cümle sözcüğü |
|---|---|---|
| kare tam görünür (tek `set`, hareket yok) | kare 0 / zaman çizelgesi dışı (yakalama 0,5 sn) | yok — ses yok |

`olaylar.json` = `[]` (`olay.py` yazar; dokunma).

## 5. Yerleşim (y = yazı tabanı, px)

```
y    0 ┌───────────────────────────────────────────┐
    48 │ [logo 387×96]                              │ HUD 0–288 (çip YOK, ders adı YOK — S1 kapak C ile aynı)
   216 │ (YDT · BASIC)                              │ rozet 216–288
   340 │ ┄ başlık üstü (İ noktası + kontur)          │
  ≈523 │  AYNI FİİL,                                │ Fredoka 700 S (=190), mürekkep + kontur, hapsız
  ≈749 │  İKİ ZAMAN                                 │ iki satır aynı sol x, blok ortalı
   864 │ ┌ kart 1 ─────────────────────── [mont] ┐ │ 864–1096
   948 │ │ She wears her coat                     │ │ Fredoka 700 B (=72)
  1048 │ │ in the winter.                         │ │
  1112 │ ┌ kart 2 ─────────────────────── [tişört]┐ │ 1112–1344
  1196 │ │ She is wearing her                     │ │ "is wearing" altında sarı el altçizgisi
  1296 │ │ pink T-shirt today.                    │ │
  1344 ├───────────────────────────────────────────┤ altyazı bandı 1344–1536 BOŞ
  1536 ├───────────────────────────────────────────┤ PLATFORM: BOŞ
```

### 5.1 HUD — `<g id="kunye">`
S1 `kunye_svg()` AYNEN: logo `<g id="ku-logo"><image id="logoimg" href="assets/logo.svg" x="48" y="48" height="96" width=96·Y.LOGO_EN_BOY/>`;
rozet `<g id="rz0">` hap x 48, y 216, h 72, rx 36, w = `Y.genislik("Lexend", 700, "YDT · BASIC", 36) + 56`, `<rect fill=vurgu>`;
yazı Lexend 700 36, `text-anchor="middle"`, x = hap ortası, taban 265, `<text fill=zemin>`.

### 5.2 Başlık — `<g id="baslik">` (hapsız, tek renk)
- Metin: satır 1 `AYNI FİİL,` · satır 2 `İKİ ZAMAN` (büyük noktalı İ = U+0130; virgül satır 1'de kalır).
- Ölçü `g(m, s) = Y.genislik("Fredoka", 700, m, s)`. `gmax(s) = max(g(satır1, s), g(satır2, s))`.
- Boy: `S = floor(min(190, 952·100 / gmax(100)))` (beklenen 190); `gmax(S) + 12 ≤ 952` assert (kontur payı).
- Hizalama: blok ortalı, iki satır AYNI sol x: `x0 = 540 − gmax(S)/2`.
- Taban: `T1 = 340 + 0,93·S + 6` (İ noktası 0,921 em + kontur 6) · `T2 = T1 + 1,19·S` (satır 1 virgül kuyruğu ile satır 2 İ noktası arası ≥ 0,10·S).
  Beklenen S = 190 → T1 ≈ 522,7 · T2 ≈ 748,8.
- İki `<text>`: id `bs-1`, `bs-2`; Fredoka 700 S; `fill` murekkep; `stroke` zemin, `stroke-width="12"`, `stroke-linejoin="round"`,
  `style="font-kerning:none;paint-order:stroke fill"` (S1 `bs-1` ile aynı öznitelikler).
- Başlıkta sarı YOK: kutu, hap, altçizgi, renkli sözcük yok. **`t2` id YOK.**
- Başlık kutusu: `x0 − 6 … x0 + gmax(S) + 6`; y `T1 − 0,93·S − 6` (= 340) → `T2 + 0,05·S + 6`; alt ≤ 768 assert.

### 5.3 Kartlar — `<g id="kart1">`, `<g id="kart2">`
| Ölçü | Değer |
|---|---|
| Kart dış kutusu | x 48–1032 (w 984); kart 1 y 864–1096, kart 2 y 1112–1344 (h 232, ara 16) |
| Çerçeve `<rect id="k1-crv">` / `k2-crv` | x 50, w 980, y = dış üst + 2, h 228, rx 24, `fill="none"`, `stroke` murekkep, `stroke-width="4"` (çizgi dış kenarı tam dış kutuda) |
| Yazı | Fredoka 700 B; `B = 72` (BRIEF-DIKEY §3); 4 satırın hepsi `88 + g(satır, B) ≤ IKON_X − 32` değilse B küçülür, B ≥ 64 assert |
| Yazı x | 88 (sol hizalı, iki satır) |
| Taban | satır 1 = dış üst + 84 · satır 2 = dış üst + 184 → kart 1: 948 / 1048 · kart 2: 1196 / 1296 (QA 1, şef: ilk sürüm 86 / 182) |
| Yazı öznitelikleri | `fill` murekkep, KONTURSUZ, `style="font-kerning:none"` (altçizgi x'i `Y.genislik` ile hesaplanır; kerning kapalı olmalı) |
| id | `k1-s1`, `k1-s2`, `k2-s1`, `k2-s2` |

Ekran metni (BİREBİR; satır kırılımı ana ders `sahne-03.js` `SAT` dizisi):
- kart 1: `She wears her coat` / `in the winter.`
- kart 2: `She is wearing her` / `pink T-shirt today.` (`T-shirt` tireli)

### 5.4 Tek vurgu — `<path id="k2-alti">` (kart 2, `is wearing` altı)
- x0 = `88 + g("She ", B) − 4` · x1 = `88 + g("She is wearing", B) + 4` (beklenen ≈ 219 → 556).
- y = kart 2 satır 1 tabanı + `0,40·B` (≈ 1224,8; sözleşme kuralı taban + max(0,28 em, kuyruk 0,22 em + 13); QA 1, ilk sürüm 0,36).
- `d = "M{x0} {y} Q{(x0+x1)/2} {y+3} {x1} {y+1}"`; `fill="none"`, `stroke` vurgu (`#f2a93b`), `stroke-width="10"`, `stroke-linecap="round"`.
- Kartta, başlıkta ve ikonlarda başka sarı YOK. `today` vurgulanmaz (altçizgi, daire, renk yok). `wears` vurgulanmaz.

### 5.5 Köşe ikonları — `<g id="mont">` (kart 1), `<g id="tisort">` (kart 2)
- Kutu: `IKON = 140`, `IKON_X = 862` (x 862–1002), y = dış üst + 28 … + 168 (sağ üst köşe).
- Izgara → px: `k = min(140/UW, 140/UH)`; `ox = 862 + (140 − UW·k)/2`; `oy = dış üst + 28 + (140 − UH·k)/2`; nokta `(ox + qx·k, oy + qy·k)`.
  Mont UW,UH = 100,120 (k ≈ 1,1667) · tişört 100,90 (k = 1,4).
- Darbe → SVG (px koordinatı; `scale` dönüşümü YOK):
  - `n` (egri yok): `<path d="M p0 L p1 L p2 …">`.
  - `n` + `egri: true` (3 nokta): ortadan geçen ikinci derece eğri `M p0 Q c p2`, `c = 2·p1 − (p0 + p2)/2`.
  - `daire: [cx, cy, r]`: `<circle cx cy r = r·k>`.
- Grup öznitelikleri: `fill="none" stroke=murekkep stroke-width="4" stroke-linecap="round" stroke-linejoin="round"`.
  Renk: tişört de mürekkep (pembe renk YOK; paletin dışında).

## 6. Tema (hf_tema.py ile uyum)
- `Y.ZEMIN_CSS` ve `Y.zemin_html()` DEĞİŞTİRMEDEN kullan. Renkler SVG özniteliği, küçük harf hex. CSS `style` içinde renk YAZMA.
- Dönüşüm (açık tema): `rect fill #f2a93b` → `#ffe066` (rozet) · `text fill #1b1a17` → `#1b2440` (rozet yazısı) ·
  `stroke #f2a93b` → `#d9900f` (altçizgi) · `#f3efe6` → `#1b2440` · `stroke #1b1a17` → zemin (başlık konturu).
- id `t2`, `ku-nokta`, `rz1` KULLANMA. `<path fill="#1b1a17">` YOK.

## 7. Kurallar ve kabul ölçütü (uret.py içinde `assert`)
1. Bütün bloklar x ∈ [48, 1032]; hiçbir blok y + h > 1344 değil (altyazı bandı boş); hiçbir blok y ≥ 1536 değil.
2. Yazı boyu: başlık S ≥ 64, kart B ≥ 64 (HUD rozeti 36 hariç). Başlık 2 satır. Her satır ≤ 24 karakter (başlık, 4 kart satırı, rozet).
3. Bloklar ve aralar:
   - Üst düzey `hud` (48, 0, 984, 288) · `baslik` · `kart1` · `kart2`: çiftler arası kesişim 0.
   - `baslik` üstü − 288 ≥ 40 · `kart1` üstü − `baslik` altı ≥ 48 · `baslik` altı ≤ 768.
   - Yazı kutusu: y_üst = taban − 0,75·B, y_alt = taban + 0,25·B, w = `g(satır, B)`.
   - Kart içi (her kart): satır 1, satır 2, ikon (çizilen kutu: ox, oy, UW·k, UH·k) çiftler arası kesişim 0; hepsi kart iç kutusunda
     (dış kutu her yandan 4 px içeri).
   - `k2-alti` kutusu (x0, y − 5, x1 − x0, 12): üstü ≥ `k2-s1` alt · altı ≤ `k2-s2` üst.
   - Her satır için `88 + g(satır, B) + 32 ≤ IKON_X`.
4. `nesneler.json`: `[{"ad", "x", "y", "w", "h"}]` tam sayı; sıra: hud, baslik, kart1, k1-s1, k1-s2, mont, kart2, k2-s1, k2-s2, k2-alti, tisort.
5. Yasak: emoji, kırmızı, yeşil, pembe, gradyan, gölge, `Math.random`, `Date`, try/except, `opacity:0` başlangıç, hareket (iki `set` dışında tween yok),
   figür, altyazı öğesi.
6. Ekranda "kanal", QR, süre ("6 dk" vb.) YOK. Python: bütün işlevlerde tür ipuçları; satır ≤ 140 karakter.
7. `/usr/bin/python3 uret.py` stdout'a `index.html yazıldı <bayt>` ve `S=<başlık boyu> B=<kart boyu>` basar; hata yoksa çıkış 0.

Kabul (şef koşturur, ajan koşturmaz): `ONIZLE_YALNIZ=1 bash calistir.sh` → "önizleme hazır"; `bash calistir.sh --tema acik|koyu` →
`P/kapak-c.png` ve `D/k/koyu/kapak-c-koyu.png` 1080×1920; taşma, kesik yazı, üst üste binme yok; altçizgi `g` kuyruğuna değmez.
