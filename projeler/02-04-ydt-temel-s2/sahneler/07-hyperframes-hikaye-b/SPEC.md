# SPEC — 02-04-ydt-temel-s2 · sahne 07-hyperframes-hikaye-b (HyperFrames, 1080×1920, tek kare, ses yok)

Yazan: şef (15.11.2026, istem D-S2). Kod yazmaz; tasarım verir. K = `/home/sef/01dev/_worktrees/kalem-0204`.
Sahne dizini D = `K/projeler/02-04-ydt-temel-s2/sahneler/07-hyperframes-hikaye-b/`. Paket P = `K/projeler/02-04-ydt-temel-s2/`.
Kaynak: `P/BRIEF-S2.md` "Hikâye" tablosu B sütunu · `P/uretim-tutanagi/hikaye-taslak.md` §4 · `P/uretim-tutanagi/S2-duzeltme.md` madde 1.
Hikâye B = soru kartı: başlık `Hangisi doğru?` + boşluklu kök + iki şık + ipucu + çağrı. **CEVAP YOK.**

## 1. Dosyalar

| Dosya | Durum | İş |
|---|---|---|
| `D/uret.py` | YOK | **YAZILACAK** — mutlak yol `/home/sef/01dev/_worktrees/kalem-0204/projeler/02-04-ydt-temel-s2/sahneler/07-hyperframes-hikaye-b/uret.py` |
| `D/yardim.py` | VAR (S1 sahne 07 kopyası) | DOKUNMA; yalnız `import yardim as Y` |
| `D/calistir.sh`, `D/olay.py`, `D/zamanlar.json` | VAR (şef yazdı) | DOKUNMA |
| `D/nesneler.json`, `D/proje/index.html` | uret.py yazar | §7 |

Başka dosyaya dokunma. Silme yok. Test, render, snapshot, `calistir.sh`, git YOK. `P/ortak/`, `P/zaman.json`, başka sahneler salt okunur.

## 2. Kalıp (salt oku) — en yakın örnek

`K/projeler/02-04-ydt-temel-s1/sahneler/07-hyperframes-hikaye-b/uret.py` (aynı tür, S1 hikâye B). Aynısını al:
- Dosya düzeni: docstring, `AD`, `sys.path` + `import yardim as Y`, `PAKET`, zaman doğrulaması, sabitler, işlevler, `__main__`.
- `zaman.json` / `zamanlar.json` doğrulaması BİREBİR (assert'ler aynı; `duragan` kaydı, `kare == 1`, `cikti == "hikaye-b.png"`,
  `sahneler[]` içinde `AD.name` yok, `sure 1.0 · kare 1 · fps 30`).
- `Y.RENK` assert'leri BİREBİR (`zemin #1b1a17`, `murekkep #f3efe6`, `ikincil #c9c2b3`, `vurgu #f2a93b`).
- HTML kabuğu BİREBİR: `Y.font_css()`, `Y.ZEMIN_CSS`, `#sahne{position:absolute;left:0;top:0;}`, `#root` div öznitelikleri,
  `Y.zemin_html()`, `<svg id="sahne" …>`, `lib/gsap.min.js`, tek `tl.set` çifti (0 ve `Z['sure']`), `window.__timelines["main"]`.
- `kesisim`, `blok_kutulari`, `kurallari_dogrula`, `uret`, `__main__` (font kopyası, `index.html`, `nesneler.json`, stdout satırı) kalıbı.

Farklar (bu sahne):
- **Künye:** örnekteki elle yazılmış `kunye_svg()` YOK. Yerine `Y.kunye_svg(cip)` çağrılır (yardim.py içinde VAR; logo + ders adı 2 satır
  + rozet `rz0` + çip). `cip` sabit yazılmaz: `P/ortak/kunye.js` metni okunur, `re.search(r'"07-hyperframes-hikaye-b":\s*"([^"]+)"', …)`
  ile çekilir; eşleşme yoksa assert. (Bugünkü değer `Full lesson`; tek otorite kunye.js.)
- Soru hapı (`soru_svg`) YOK. `Hangisi doğru?` hapsız, mürekkep, Fredoka 96.
- Kök kartı (boşluk çizgisi + küçük tişört) YENİ. Şık kartları tek satır (örnekte 2 satır).

## 3. Sabitler

`W, H = Y.W, Y.H` · `KENAR = 48` · `SAG = 1032` · `ICERIK = (352, 1392)` · `CAGRI = (1344, 1536)` · `PLATFORM = 1536` ·
`IC = 40` (kart iç boşluğu, BRIEF-DIKEY §3) · `ARA = 40` (içerik blokları arası dikey boşluk).
Renk yalnız `R = Y.RENK`; başka hex YOK. İçerikte (künye ve `@ydspublishing` hapı dışında) `R["vurgu"]` KULLANILMAZ.
Yazı genişliği yalnız `Y.genislik(aile, agirlik, metin, boy)` ile ölçülür.

## 4. Yerleşim (y = yazı tabanı, px; x sol kenar)

```
y    0 ┌──────────────────────────────────────────────┐
       │ [logo]                          [Full lesson] │ HUD: Y.kunye_svg(cip)  (0–288)
   212 │ SIMPLE PRESENT vs                             │
   276 │ PRESENT CONTINUOUS  (YDT · BASIC)             │
   448 │ Hangisi doğru?                                │ Fredoka 700 96 · blok 376–472
   512 │ ┌ kök kartı ──────────────────────── [tişört]┐ │ 512–788 (h 276)
   620 │ │ Look! She ________ her                      │ │ Fredoka 700 72 · boşluk = kalem çizgisi
   716 │ │ pink T-shirt today.                         │ │ Fredoka 700 72
   828 │ ┌ şık A ─────────────────────────────────────┐ │ 828–988 (h 160)
       │ │ (A)  wears                                  │ │
  1028 │ ┌ şık B ─────────────────────────────────────┐ │ 1028–1188 (h 160)
       │ │ (B)  is wearing                             │ │
  1276 │ Genel mi, şu an mı?                           │ Caveat 700 64 · blok 1228–1295
  1418 │ Cevap ve neden:            [@ydspublishing]   │ Caveat 700 72 · hap sağa hizalı (y 1398, h 84)
  1498 │ tam derste                                    │ Caveat 700 72
  1536 ├──────────────────────────────────────────────┤ PLATFORM 1536–1920: boş
```
Ölçülmüş genişlikler (`Y.genislik`, ±1 px): `Hangisi doğru?`@96 = 638 · `Look! She `@72 = 328 · ` `@72 = 17 · `her`@72 = 110 ·
`pink T-shirt today.`@72 = 605 · `wears`@72 = 196 · `is wearing`@72 = 329 · `Genel mi, şu an mı?` Caveat@64 = 415 ·
`Cevap ve neden:` Caveat@72 = 382 · `tam derste` Caveat@72 = 266 · `@ydspublishing`@64 = 451. Kod bunları ÖLÇER, sabit yazmaz.

### 4.1 Öğeler
| # | id | Öğe | Ölçü | Renk |
|---|---|---|---|---|
| 1 | `kunye` | HUD | `Y.kunye_svg(cip)` | yardim.py verir |
| 2 | `baslik` | `Hangisi doğru?` | Fredoka 700 96, x 48, taban 448 | `fill` murekkep |
| 3 | `kok` (grup) | kök kartı | §4.2 | §4.2 |
| 4 | `kA` (grup) | şık kartı A, harf `A`, metin `wears` | y0 = 828; §4.3 | §4.3 |
| 5 | `kB` (grup) | şık kartı B, harf `B`, metin `is wearing` | y0 = 1028; §4.3 | §4.3 |
| 6 | `ipucu` | `Genel mi, şu an mı?` | Caveat 700 64, x 48, taban 1276 | `fill` murekkep |
| 7 | `cg1` | `Cevap ve neden:` | Caveat 700 72, x 48, taban 1418 | `fill` murekkep |
| 8 | `cg2` | `tam derste` | Caveat 700 72, x 48, taban 1498 | `fill` murekkep |
| 9 | `hap` (grup) | `@ydspublishing` hapı | örnekle BİREBİR: `<rect>` x = 1032 − w, y 1398, w = genişlik(@64) + 56, h 84, rx 42; yazı Fredoka 700 64, `text-anchor="middle"`, taban 1462 | rect `fill` vurgu · yazı `fill` zemin |

Her `<text>` `xml:space="preserve"`. Sarı vurgu YOK (rozet, çip, `@ydspublishing` hapı künye öğesidir). Altçizgi, daire, ok YOK.
`Look!` kökün parçasıdır: aynı renk, aynı boy, ayrı vurgu YOK (S2-duzeltme madde 1).

### 4.2 Kök kartı (`kok`, y0 = 512, h `KOK_H = 276`)
| Öğe (id) | Ölçü | Renk |
|---|---|---|
| çerçeve `kok-crv` `<rect>` | x 48, y 512, w 984, h 276, rx 28, `fill="none"`, `stroke-width` 4 | `stroke` murekkep |
| satır 1a `kok-s1a` | `Look! She` (sonda boşluk YOK), Fredoka 700 72, x 88, taban 620 | `fill` murekkep |
| boşluk `kok-bos` `<path>` | `bx0 = 88 + genişlik("Look! She ", 72)` · `bx1 = bx0 + 240` · çizgi `bx0 + 4` → `bx1 − 4`, `yb = 620 + 14`. Hafif eğri el çizgisi: `M x0 yb Q (x0+x1)/2 yb+6 x1 yb+1` (main ders `el_cizgi` biçimi, egim 3). `fill="none"`, `stroke-width` 5, `stroke-linecap="round"` | `stroke` murekkep |
| satır 1b `kok-s1b` | `her`, Fredoka 700 72, x = `bx1 + genişlik(" ", 72)`, taban 620 | `fill` murekkep |
| satır 2 `kok-s2` | `pink T-shirt today.` (tire ile), Fredoka 700 72, x 88, taban 716 | `fill` murekkep |
| küçük tişört `kok-tis` (grup) | §4.4; kutu x 876–996, y 540–641 (sağ üst köşe) | `stroke` murekkep |

Boşlukta yazı YOK (cevap yok): `_`, `is wearing`, `wears` kök içinde geçmez.

### 4.3 Şık kartı (y0 = 828 ya da 1028; iki kart BİREBİR aynı biçim, h `SIK_H = 160`, `cy = y0 + 80`)
| Öğe (id) | Ölçü | Renk |
|---|---|---|
| çerçeve `kA-crv` | x 48, y y0, w 984, h 160, rx 28, `fill="none"`, `stroke-width` 4 | `stroke` murekkep |
| harf dairesi `kA-daire` | `<circle>` cx 136, cy, r 48, `fill="none"`, `stroke-width` 4 | `stroke` murekkep |
| harf `kA-harf` | Fredoka 700 64, `text-anchor="middle"`, x 136, taban cy + 22 | `fill` murekkep |
| metin `kA-metin` | Fredoka 700 72, x 220, taban cy + 26 | `fill` murekkep |
(B için `kB-…`.) Şık dili ana ders sahne 13'ten: harf dairesi + şık metni (`A) wears` yazımı ekranda daire + metin olur).
Cevap belirtisi YOK: tik, çarpı, renk farkı, dolgu, kalın çerçeve, altçizgi, ikon YOK. Doğru şık yeşil DEĞİL (bu sahnede geçersiz).

### 4.4 Küçük tişört (main ders `TISORT` ızgarası; kaynak `K/projeler/02-04-ydt-temel/sahneler/03-paperjs-ornek1/sahne-03.js` satır 27)
Izgara noktaları (gx, gy), dönüşüm `x = 876 + gx·1.2`, `y = 540 + (gy − 4)·1.2`:
- dış hat (açık çoklu çizgi, `<path>` M/L): (37,4) (14,12) (0,36) (14,46) (24,37) (24,88) (76,88) (76,37) (86,46) (100,36) (86,12) (63,4) · `stroke-width` 4
- yaka (eğri): (37,4) → (63,4), denetim noktası (50,24) ile `Q` (eğri (50,14)'ten geçer) · `stroke-width` 4
- kol dikişleri: (14,12)–(24,37) ve (86,12)–(76,37) · `stroke-width` 3
Hepsi `fill="none"`, `stroke` murekkep, `stroke-linecap="round"`, `stroke-linejoin="round"`. id `kok-tis-0` … `kok-tis-3`.
Pembe dolgu YOK (palet dışı renk; tek vurgu kuralı).

## 5. Tema (hf_tema.py ile uyum)
- `Y.ZEMIN_CSS` ve `Y.zemin_html()` DEĞİŞTİRMEDEN kullan. Renkler SVG özniteliği, küçük harf hex; CSS `style` içinde renk YOK.
- Açık temada dönüşüm `P/ortak/hf_tema.py` ile olur: `rect fill #f2a93b` → `#ffe066` (vurguDolgu) · `text fill #1b1a17` → `#1b2440`
  (pilMetin) · `fill/stroke #f3efe6` → `#1b2440` (murekkep). Hap dolgusu `<rect fill="#f2a93b">`, hap yazısı `<text fill="#1b1a17">`.
- id `t2`, `ku-nokta`, `rz1` KULLANMA. `<circle fill="#1b1a17">` YOK (daireler `fill="none"`).

## 6. Olay listesi (ses yok; zaman çizelgesi dışı)
| Olay | Kare | Küresel sn | Yerel sn | Cümle sözcüğü |
|---|---|---|---|---|
| tek kare (bütün öğeler kare 0'dan görünür) | 0 (yakalama 15) | — (anlatımda yeri yok) | 0,0 (yakalama 0,5) | — |
`olaylar.json = []` (olay.py yazar). Tween YOK; yalnız örnekteki tek `set` çifti.

## 7. Kurallar ve kabul ölçütü (uret.py içinde `assert`)
1. Bütün metin ve kutular x ∈ [48, 1032]; hiçbir öğe y ≥ 1536 değil (yazı alt sınırı = taban + 0,30·boy Caveat / 0,25·boy diğer).
2. Yazı boyu ≥ 64 (HUD hariç: ders adı 56, rozet 36, çip 40).
3. Her ekran satırı ≤ 24 karakter (`len`), HUD ve çip dahil. Liste: ders 2 satır, rozet, çip, `Hangisi doğru?`, `Look! She ____ her`
   (boşluk 4 karakter sayılır), `pink T-shirt today.`, `A`, `B`, `wears`, `is wearing`, `Genel mi, şu an mı?`, `Cevap ve neden:`,
   `tam derste`, `@ydspublishing`.
4. Blok kutuları: yazı kutusu y_üst = taban − 0,75·boy, y_alt = taban + 0,30·boy (Caveat) / 0,25·boy (diğer); x = sol, w = ölçülen genişlik.
   Bloklar: `hud` (48, 0, 984, 288) · `baslik` · `kok` (kart dikdörtgeni) · `kA` · `kB` · `ipucu` · `cg1` · `cg2` · `hap`.
   Çiftler arası kesişim 0. Dikey komşular (`hud`→`baslik`→`kok`→`kA`→`kB`→`ipucu`→`cg1`, `ipucu`→`hap`) arası boşluk ≥ 16
   (istisna `cg1`–`cg2`: yalnız kesişim 0). `cg1`, `cg2` sağ kenarı ile `hap` sol kenarı arası ≥ 24.
5. Kök kartı içi: `kok-s1b` sağı + 24 ≤ tişört solu (876); tişört altı + 16 ≤ `kok-s2` üstü; tişört kutusu kart içinde, kenarlara ≥ 16;
   bütün kök yazıları x ∈ [88, 1032 − IC] ve y ∈ [512 + 16, 788 − 16].
6. Şık kartı içi: daire sağı (184) + 24 ≤ metin solu (220); metin sağı ≤ 1032 − IC; harf ve metin y kutusu kart içinde.
7. `baslik` üstü ≥ 352; `ipucu` altı ≤ 1344 − 16; `hap`, `cg1`, `cg2` [1344, 1536] içinde.
   Bant doluluğu: (`ipucu` altı − `baslik` üstü) / (1392 − 352) ≥ 0,85 (BRIEF-DIKEY §0; beklenen ≈ 0,88).
8. Cevap yok: içerik SVG'si (künye ve hap hariç) `R["vurgu"]` içermez; `kA` ve `kB` grupları y, id, harf ve metin dışında aynı
   öznitelikleri taşır (harf ve metin çıkarılıp y/id normalleştirilince iki dize eşit); kök metinlerinde `is wearing` ve `wears` YOK.
9. Yasak: emoji, kırmızı, yeşil, gradyan, gölge, filtre (gren dışında), `Math.random`, `Date`, try/catch, `opacity:0` başlangıç,
   hareket (tek `set` dışında tween yok). Ekranda "kanal", QR, süre ("dk") YOK. Python: bütün işlevlerde tür ipucu.
10. `nesneler.json`: `[{"ad", "x", "y", "w", "h"}]` tam sayı; bloklar §7.4 + `tisort` (kök kartı içinde; kesişim denetimine girmez).
11. `/usr/bin/python3 uret.py` stdout'a `index.html yazıldı <bayt>` basar; hata yoksa çıkış 0.

Kabul (şef koşturur, ajan koşturmaz): `ONIZLE_YALNIZ=1 bash calistir.sh` → "önizleme hazır"; `bash calistir.sh --tema acik|koyu` →
`P/hikaye-b.png` ve `D/k/koyu/hikaye-b-koyu.png` 1080×1920; taşma, kesik yazı, üst üste binme, cevap belirtisi yok; 1536 altı boş.
