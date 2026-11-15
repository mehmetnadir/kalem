# SPEC v2 — 02-04-ydt-temel-s2 · sahne 07-hyperframes-hikaye-b (Hikâye B, soru kartı, huni v2; HyperFrames, 1080×1920, tek kare, ses yok)

Yazan: şef (15.11.2026, istem D-S2-V2). Tasarım verir; tam kod yazmaz. K = `/home/sef/01dev/_worktrees/kalem-0204`.
D = `K/projeler/02-04-ydt-temel-s2/sahneler/07-hyperframes-hikaye-b/` · P = `K/projeler/02-04-ydt-temel-s2/`.
Bağlayıcı: `/home/sef/01dev/dijital-anlatim/.claude/docs/huni-v2-standart.md` §1, §2, §6 · `P/BRIEF-S2.md` "Yerleşim" + "Hikâye B" sütunu ·
`P/uretim-tutanagi/hikaye-taslak.md` §4 · `P/uretim-tutanagi/S2-duzeltme.md` madde 1. v1 (SPEC, RAPOR, uret.py, yardim.py) yedekte:
`/home/sef/Silinecekler/2026-11-15-huni-v2/02-04-ydt-temel-s2/sahneler/07-hyperframes-hikaye-b/`.
Hikâye B = soru kartı: `Hangisi doğru?` + boşluklu kök + iki şık + ipucu + yer imi `Kaydet`. **CEVAP YOK.** Doğru şık (B) yalnız belgede.

## 1. Dosyalar

| Dosya | Durum | İş |
|---|---|---|
| `/home/sef/01dev/_worktrees/kalem-0204/projeler/02-04-ydt-temel-s2/sahneler/07-hyperframes-hikaye-b/uret.py` | v1 VAR (eski içerik) | **BAŞTAN YAZILACAK** (bu spec) |
| `D/yardim.py` | v2 VAR (şef `04-hyperframes-hikaye/yardim.py`'den kopyaladı; sha256 `3d1ac3d54474…`; kanal katmanı + künye) | DOKUNMA; `import yardim as Y` |
| `D/calistir.sh`, `D/olay.py`, `D/zamanlar.json` | VAR | DOKUNMA |
| `D/nesneler.json`, `D/proje/index.html` | uret.py yazar (§6.10) | — |

Başka dosyaya dokunma. Silme yok. Test, render, snapshot, `calistir.sh`, git YOK. `P/ortak/`, `P/zaman.json`, başka sahneler salt okunur.

## 2. Kalıp kaynakları (salt oku)

| Kalıp | Mutlak yol | Ne alınır |
|---|---|---|
| **İskelet** (v2, kardeş sahne, aynı tür) | `/home/sef/01dev/_worktrees/kalem-0204/projeler/02-04-ydt-temel-s2/sahneler/04-hyperframes-hikaye/uret.py` | docstring düzeni; satır 13–20 (`AD`, `sys.path` + iki site-packages ekleme döngüsü, `import yardim as Y`, `PAKET`); `zamanlar.json` assert'leri (30–33); `Y.KONU` / `Y.ROZETLER` assert'leri (35–36); `R = Y.RENK` + anahtar assert'i; `YERIMI_D` sabiti ve yorumu; `kesisim()`; `kaydet_svg()` dönüşüm hesabı biçimi (burada SOLA yaslı ve dolgulu, §4.3.5); `uret()` HTML kabuğu (`{kunye}` → `<g id="icerik">`, iki `tl.set("#icerik", …)`); `__main__` (`proje/`, `Y.font_kopyala`, `index.html`, `nesneler.json`, iki stdout satırı). **04'ün soru/kart/eşleşme/today hapı/MONT/TISORT ızgarası ALINMAZ** |
| **İçerik** (v1, aynı sahne) | `/home/sef/Silinecekler/2026-11-15-huni-v2/02-04-ydt-temel-s2/sahneler/07-hyperframes-hikaye-b/uret.py` | `zaman.json` → `duragan` assert'leri (satır 20–26, birebir); `tisort_svg()` nokta listesi ve 4 yol (58–88; yalnız dönüşüm değişir, §4.4); `secenek_karti_svg()` yapısı (129–150; ölçüler değişir, §4.3.3); `_norm_sik` eşitlik denetimi fikri (423–435). **v1'in `Y.kunye_svg(CIP)`, `kunye.js` regex'i, çip, `cagri_svg`, `hap_svg`, `@ydspublishing` hapı ALINMAZ** |
| Kanal katmanı + künye | `D/yardim.py` → `Y.kunye_svg()` (parametresiz), `Y.KONU`, `Y.ROZETLER`, `Y.HUD`, `Y.rozet_konumlari()`, `Y.genislik()` | olduğu gibi çağır; sayı kopyalama |
| Yer imi simgesi | Tabler Icons `bookmark` (MIT), 24×24: `M18 7v14l-6 -4l-6 4v-14a4 4 0 0 1 4 -4h4a4 4 0 0 1 4 4z` (yol sınır kutusu x 6–18, y 3–21) | sabit `YERIMI_D`; yorumda kaynak ve lisans |
| Tema | `P/ortak/hf_tema.py` | §5 |

## 3. Okuma ve sabitler

- `PAKET = AD.parent.parent`. `PAKET/zaman.json` → `duragan` içinde `klasor == AD.name` olan TEK kayıt; `kare == 1`, `cikti == "hikaye-b.png"`;
  `sahneler[]` içinde `AD.name` YOK (v1 satır 20–26). `Z = D/zamanlar.json` (`sure` 1,0 · `kare` 1 · `fps` 30 assert).
- Anlatım, sözcük, altyazı, `kunye.js` OKUNMAZ (ses yok; künye `yardim.py`'den; çip YOK).
- `assert Y.KONU == "Simple Present vs Present Continuous"` ve `assert Y.ROZETLER == ("YDT · BASIC",)`.
- Renk yalnız `R = Y.RENK` anahtarlarıyla: `zemin`, `murekkep`, `vurgu`. Başka hex YOK. Koyu hex yazılır; açık tema hf_tema ile gelir.
- Yazı genişliği yalnız `Y.genislik(aile, agirlik, metin, boy)` ile ölçülür; aşağıdaki "≈" değerler doğrulama içindir, koda yazılmaz.

| Ad | Değer | Not |
|---|---|---|
| `X0`, `X1` | 60, 960 | içerik sol/sağ sınır |
| `BASLIK_BOY`, `BASLIK_TABAN` | 88, 536 | `Hangisi doğru?` Fredoka 700 (≈ 585 px) |
| `KOK` | rect x 62, y 572, w 896, h 162, rx 28 | çerçeve dış kenarı 60–960 × 570–736 (stroke 4) |
| `TX` | 92 | kök yazı sol kenarı |
| `KOK_BOY`, `L1`, `L2` | 64, 634, 704 | kök iki satır tabanı, Fredoka 700 |
| `BOS_W` | 200 | boşluk çizgisi genişliği (cevap uzunluğunu ele vermez: wears ≈ 174, is wearing ≈ 292) |
| `TIS_X`, `TIS_Y`, `TIS_S` | 844, 615, 0.9 | küçük tişört dönüşümü (§4.4); kutu x 844–934, y 615–690,6 |
| `SIK_Y` | (750, 854) | şık kartı A, B rect y; w 896, x 62, h `SIK_H` 88, rx 28 → dış 748–840, 852–944 |
| `DAIRE_X`, `DAIRE_R`, `SIK_TX`, `SIK_BOY` | 122, 36, 184, 64 | harf dairesi merkezi/yarıçapı, şık metni x, Fredoka 700 (QA tur 1: r 34 → 36) |
| `HARF_KAYMA`, `BOS_KAYMA` | 19, 6 | harf tabanı cy + 19 (ilk koşu cy + 22: `A` ayakları daireye değdi) · boşluk çizgisi L1 + 6 (ilk koşu L1 + 12: alt satıra 8 px) |
| `IPUCU_BOY`, `IPUCU_TABAN` | 64, 1004 | `Genel mi, şu an mı?` Caveat 700 (≈ 415 px) |
| `YERIMI_S`, `YERIMI_X`, `YERIMI_UST` | 5, 63, 1039 | yer imi ölçeği, geometri sol ve üst kenarı (görünür kutu stroke dahil 60–126 × 1036–1132) |
| `KAYDET_BOY`, `KAYDET_TABAN` | 88, 1116 | `Kaydet` Fredoka 700 (≈ 286 px) |
| `BOS_UST` | 1150 | bu y'den aşağısı boş (bağ çıkartması 1150–1380 + 1400–1920) |

## 4. Yerleşim (y = yazı tabanı; kutu: yazı üstü = taban − 0,75·boy, altı = taban + 0,30·boy Caveat / 0,25·boy diğer)

```
y    0 ┌──────────────────────────────────────┐
       │ (boş zemin)                          │ 0–280
   291 │ [logo] @ydspublishing                │ kanal katmanı 291–341 (Y.kunye_svg)
   386 │ Simple Present vs Present Cont. (YDT · BASIC) │ künye 386–434
   536 │ Hangisi doğru?                       │ Fredoka 88 · 470–558
   572 │ ┌ kök kartı ───────────────────────┐ │ dış 570–736
   634 │ │ Look! She ________ her   [tişört]│ │ Fredoka 64 · boşluk = kalem çizgisi
   704 │ │ pink T-shirt today.              │ │ Fredoka 64
       │ └──────────────────────────────────┘ │
   750 │ ┌ (A)  wears ──────────────────────┐ │ dış 748–840
   854 │ ┌ (B)  is wearing ─────────────────┐ │ dış 852–944 (A ile birebir aynı biçim)
  1004 │ Genel mi, şu an mı?                  │ Caveat 64 · 956–1023
  1116 │ [yer imi] Kaydet                     │ SOLA yaslı · yer imi SARI dolgu (TEK SARI) · 1036–1138
  1150 │ (boş zemin: bağ çıkartması)          │ 1150–1380 hiçbir şey çizilmez
  1400 │ (boş)                                │ 1400–1920 boş
  1920 └──────────────────────────────────────┘
```

### 4.1 Kanal katmanı + künye
`Y.kunye_svg()` çıktısı aynen (içinde `<g id="kunye"><g id="kanal">…</g>…</g>`, logo `<image id="logoimg">`). Ekleme, değişiklik yok. Çip YOK.

### 4.2 SVG düzeni
`<svg id="sahne">` içinde sıra: `<defs>` (yalnız §4.3.5 `clipPath`) → `{kunye}` → `<g id="icerik">` (başlık, kök, kA, kB, ipucu, kaydet).
`#kanal` ve `#kunye` hiçbir tween'e girmez.

### 4.3 Öğeler (renkler SVG özniteliği, küçük harf hex; her `<text>` `xml:space="preserve"`)
| # | id | Öğe | Ölçü | Renk |
|---|---|---|---|---|
| 1 | `baslik` | `<text>` `Hangisi doğru?` | Fredoka 700 88, x 60, taban 536 | fill murekkep |
| 2 | `kok` (g) | kök kartı | 4.3.2 | — |
| 3 | `kA` (g) | şık kartı A: harf `A`, metin `wears` | rect y 750; 4.3.3 | — |
| 4 | `kB` (g) | şık kartı B: harf `B`, metin `is wearing` | rect y 854; 4.3.3 | — |
| 5 | `ipucu` | `<text>` `Genel mi, şu an mı?` | Caveat 700 64, x 60, taban 1004 | fill murekkep |
| 6 | `kaydet` (g) | yer imi + `Kaydet` | 4.3.5 | — |

#### 4.3.2 Kök kartı (`<g id="kok">`)
- `kok-crv`: `<rect x="62" y="572" width="896" height="162" rx="28" fill="none" stroke=murekkep stroke-width="4"/>`.
- `kok-s1a`: `Look! She` (sonda boşluk YOK), Fredoka 700 64, x 92, taban 634, fill murekkep. `Look!` vurgusuz (aynı renk, aynı boy).
- `kok-bos` (`<path>`): `bx0 = 92 + genislik("Fredoka", 700, "Look! She ", 64)` (≈ 383,5) · `bx1 = bx0 + 200` · `x0 = bx0 + 4`, `x1 = bx1 − 4`,
  `yb = 634 + BOS_KAYMA` (6); `d = M x0 yb Q (x0+x1)/2 yb+5 x1 yb+1` (1 ondalık; el çizgisi). `fill="none"`, stroke murekkep, `stroke-width="5"`, `stroke-linecap="round"`.
- `kok-s1b`: `her`, Fredoka 700 64, x = `bx1 + genislik("Fredoka", 700, " ", 64)` (≈ 598,5), taban 634, fill murekkep.
- `kok-s2`: `pink T-shirt today.` (tireli), Fredoka 700 64, x 92, taban 704, fill murekkep.
- `kok-tis` (g): §4.4.
Boşlukta yazı YOK: `_`, `wears`, `is wearing` kök grubunda geçmez.

#### 4.3.3 Şık kartı (`kA` rect y0 = 750, `kB` y0 = 854; iki kart BİREBİR aynı biçim; `cy = y0 + 44`)
| Öğe (id) | Ölçü | Renk |
|---|---|---|
| `kA-crv` | `<rect x="62" y=y0 width="896" height="88" rx="28" fill="none" stroke-width="4">` | stroke murekkep |
| `kA-daire` | `<circle cx="122" cy=cy r="36" fill="none" stroke-width="4">` | stroke murekkep |
| `kA-harf` | Fredoka 700 64, `text-anchor="middle"`, x 122, taban cy + 19 (harf üstü ve taban köşeleri dairenin iç kenarına ≥ 4 px; assert) | fill murekkep |
| `kA-metin` | Fredoka 700 64, x 184, taban cy + 22 | fill murekkep |
(B için `kB-…`.) Cevap belirtisi YOK: tik, çarpı, renk farkı, dolgu, kalın çerçeve, altçizgi, ikon, yeşil YOK.

#### 4.3.5 Kaydet (`<g id="kaydet">`, SOLA yaslı; tek sarı öğe)
- Dönüşüm: `tx = YERIMI_X − 6·YERIMI_S` (33) · `ty = YERIMI_UST − 3·YERIMI_S` (1024) · `transform="translate(tx ty) scale(5)"`.
- `<defs>` içinde: `<clipPath id="yerimi-kirp"><path d=YERIMI_D transform=…/></clipPath>` (yalnız geometri; fill/stroke özniteliği yok).
- `yerimi-dolgu`: `<rect x="63" y="1039" width="60" height="90" fill=vurgu clip-path="url(#yerimi-kirp)"/>` (12·5 × 18·5).
  **Neden rect:** hf_tema yalnız `rect|circle fill="#f2a93b"` öğesini açık temada `#ffe066` (vurguDolgu) yapar; `<path fill>` `#d9900f` olur.
- `yerimi`: `<path d=YERIMI_D transform=… fill="none" stroke=murekkep stroke-width="1.2" stroke-linecap="round" stroke-linejoin="round"/>`
  (görünür 6 px), dolgunun ÜSTÜNDE çizilir.
- `kaydet-yazi`: `Kaydet` Fredoka 700 88; `kx = (YERIMI_X + 12·YERIMI_S + 3) + 22` (= 148; görünür yer imi sağı 126 + 22); taban 1116; fill murekkep; text-anchor yok.

### 4.4 Küçük tişört (`<g id="kok-tis">`; v1 `tisort_svg` noktaları, dönüşüm değişir)
`x = 844 + gx·0.9`, `y = 615 + (gy − 4)·0.9` (1 ondalık). Yollar v1 ile aynı: `kok-tis-0` dış hat (12 nokta, `M … L …`, stroke 4) ·
`kok-tis-1` yaka `Q` (stroke 4) · `kok-tis-2`, `kok-tis-3` kol dikişleri (stroke 3). Hepsi `fill="none"`, stroke murekkep, round cap/join.
Pembe dolgu YOK (palet dışı renk; tek vurgu kuralı).

### 4.5 Ekran metni (tamamı; başka metin yok)
Künye (yardim): `@ydspublishing` · `Simple Present vs Present Continuous` · `YDT · BASIC`.
İçerik: `Hangisi doğru?` · `Look! She` · `her` · `pink T-shirt today.` · `A` · `wears` · `B` · `is wearing` · `Genel mi, şu an mı?` · `Kaydet`.
v1'deki `Cevap ve neden:`, `tam derste`, ikinci `@ydspublishing` hapı, `Full lesson` çipi KALKAR.

### 4.6 Olay listesi (tek kare; zaman çizelgesi dışı, anlatım yok)
| Olay | Kare / küresel sn | Cümle sözcüğü | Not |
|---|---|---|---|
| bütün öğeler görünür (kanal katmanı + künye + §4.3 1–6) | kare 0 (yakalama 0,5 sn; çizelge 1,0 sn) / küresel sn yok | — (ses yok; metin `hikaye-taslak.md` §4, BRIEF-S2 Hikâye B) | hiçbir öğe `opacity:0` başlamaz; giriş/çıkış hareketi yok |

GSAP: `gsap.timeline({ paused: true })`; `tl.set("#icerik", { opacity: 1, immediateRender: false }, 0)` ve aynı set `Z["sure"]`'de;
`window.__timelines["main"] = tl`. Başka tween YOK. Hedef `#icerik` (`#sahne` hedeflenmez; kanal katmanı tween dışında).

## 5. Tema (hf_tema.py ile uyum)
- `Y.ZEMIN_CSS` ve `Y.zemin_html()` DEĞİŞTİRMEDEN kullan. `<style>` içinde yalnız `Y.font_css()`, `Y.ZEMIN_CSS`, `#sahne{position:absolute;left:0;top:0;}`.
  **`#root.tema-acik` dizgisini uret.py çıktısına YAZMA** (hf_tema "zaten çevrildi" sanar, açık tema koyu kalır).
- Renkler SVG özniteliği; CSS `style` içinde renk YOK. Dönüşüm: `#f3efe6` → açıkta `#1b2440`; `rect fill #f2a93b` → `#ffe066`.
- `<path|circle fill="#1b1a17">` YOK. id `t2`, `ku-nokta`, `rz1` KULLANMA.

## 6. Kurallar ve kabul ölçütü (uret.py içinde `assert`)
Blok kutuları (`ad, x, y, w, h`, float): `kanal` (53,15 · 291 · 263 + genislik(Lexend 700, "@ydspublishing", 42) − 53,15 · 50) ·
`kunye` (60 · 386 · rozet sağı − 60 · 48; `Y.rozet_konumlari()`) · `baslik` (60 · 536 − 66 · genişlik · 88) · `kok` (60 · 570 · 900 · 166) ·
`kA` (60 · 748 · 900 · 92) · `kB` (60 · 852 · 900 · 92) · `ipucu` (60 · 1004 − 48 · genişlik · 1,05·64) ·
`kaydet` (60 · 1036 · kx + genişlik("Kaydet", 88) − 60 · 1116 + 22 − 1036) · ek `tisort` (844 · 615 · 90 · 75,6; çift kesişim denetimine girmez).
1. Bütün blok x ∈ [53, 960]; `kanal` dışındakiler x ≥ 60. Hiçbir blok y < 280; içerik blokları (baslik … kaydet) y ≥ 460 ve alt ≤ `BOS_UST` (1150).
2. İçerik yazı boyu ≥ 64 (başlık 88, kök 64, harf 64, şık 64, ipucu 64, Kaydet 88). Künye/kanal hariç (BRIEF ölçüsü).
3. İçerik satırı ≤ 24 karakter (`len`): `Hangisi doğru?` · `Look! She ____ her` (boşluk 4 karakter sayılır) · `pink T-shirt today.` · `A` · `wears` · `B` ·
   `is wearing` · `Genel mi, şu an mı?` · `Kaydet`. Künye konu satırı BRIEF gereği tek satırdır, sayılmaz.
4. Ana blok çiftleri (tisort hariç 8 blok) kesişmez (alan 0). Dikey sıra `kanal → kunye → baslik → kok → kA → kB → ipucu → kaydet` komşu boşluğu ≥ 12.
5. Kök içi: `kok-s1b` sağı + 24 ≤ 844 (tişört solu); `kok-s2` sağı + 24 ≤ 844; tişört kutusu iç kenarlara (x 64–956, y 574–732) ≥ 16;
   kök yazı kutuları x ≥ 92, sağ ≤ 956 − 24, üst ≥ 574 + 12, alt ≤ 732 − 8; boşluk çizgisi `yb + 3` < `kok-s2` üstü (704 − 48).
6. Şık içi: daire sağı (158) + 24 ≤ 184; metin sağı ≤ 956 − 24; harf ve metin yazı kutusu (taban − 48 … taban + 16) rect içinde
   (y0 + 2 … y0 + 86); daire (cy ± 36) rect içinde.
7. Kaydet: görünür yer imi (60–126 × 1036–1132) ile `kaydet-yazi` arası ≥ 20; `kaydet-yazi` sağı ≤ 960; yer imi altı ≤ 1140.
8. Tek sarı: `#icerik` HTML'inde `fill="#f2a93b"` tam 1 kez (`yerimi-dolgu`), `stroke="#f2a93b"` 0 kez; `kok`, `kA`, `kB` gruplarında `#f2a93b` YOK.
9. Cevap yok: `kA` ve `kB` grupları id önekini, y/cy/taban sayılarını, harf ve metni normalleştirince eşit dize; `kok` grubunda `wears` ve
   `is wearing` YOK; HTML'de yeşil (`#167a4a`, küçük/büyük harf duyarsız) YOK.
10. Yasak (küçük/büyük harf duyarsız; `<text>` içeriklerinde): `tam\s+ders`, `dak[iı]ka`, `\bdk\b`, `\bqr\b`, `izle`, `oynat`, `cevap`,
    `full lesson`, `kanal`; `>@ydspublishing<` HTML'de tam 1 kez (kanal katmanı). HTML'de `opacity:0`, `R["kirmizi"]`, `#root.tema-acik`,
    emoji (U+1F000 üstü, U+2600–U+27BF) YOK. `Math.random`, `Date`, try/catch, gölge, gradyan ekleme YOK.
11. `nesneler.json`: blok kutuları `[{"ad","x","y","w","h"}]` tam sayı (yuvarla), §6 sırası (tisort sonda).
12. Python: bütün işlevlerde tür ipuçları. `python3 uret.py` stdout: `index.html yazıldı <bayt>` ve
    `baslik=<üst>-<alt> kok=… kA=… kB=… ipucu=… kaydet=…`; hata yoksa çıkış 0.

Kabul (şef koşturur, ajan koşturmaz): `ONIZLE_YALNIZ=1 bash calistir.sh` → "önizleme hazır"; `bash calistir.sh --tema acik|koyu` →
`P/hikaye-b.png` ve `D/k/koyu/hikaye-b-koyu.png` 1080×1920; karede taşma, kesik yazı, üst üste binme, cevap belirtisi yok; 0–280 ve 1150–1920 boş;
kanal katmanı iki temada yerinde; tek sarı öğe yer imi dolgusu (künye rozeti hariç).
