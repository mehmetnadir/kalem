# SPEC v2 — 02-04-ydt-temel-s2 · sahne 04-hyperframes-hikaye (Hikâye A, huni v2; HyperFrames, 1080×1920, tek kare, ses yok)

Yazan: şef (15.11.2026). Tasarım verir; tam kod yazmaz. K = `/home/sef/01dev/_worktrees/kalem-0204`.
D = `K/projeler/02-04-ydt-temel-s2/sahneler/04-hyperframes-hikaye/` · P = `K/projeler/02-04-ydt-temel-s2/`.
Bağlayıcı: `/home/sef/01dev/dijital-anlatim/.claude/docs/huni-v2-standart.md` §1, §2, §6 · `P/BRIEF-S2.md` "Yerleşim" + "Hikâye A" sütunu ·
istem `P/uretim-tutanagi/istem/sahne-v2/D-04-hyperframes-hikaye.md`. v1 (SPEC, RAPOR, uret.py) yedekte:
`/home/sef/Silinecekler/2026-11-15-huni-v2/02-04-ydt-temel-s2/sahneler/04-hyperframes-hikaye/`.

## 1. Dosyalar

| Dosya | Durum | İş |
|---|---|---|
| `/home/sef/01dev/_worktrees/kalem-0204/projeler/02-04-ydt-temel-s2/sahneler/04-hyperframes-hikaye/uret.py` | v1 VAR (eski içerik) | **BAŞTAN YAZILACAK** (bu spec) |
| `D/yardim.py` | v2 VAR (şef `03-hyperframes-cta/yardim.py`'den kopyaladı; kanal katmanı + künye) | DOKUNMA; `import yardim as Y` |
| `D/calistir.sh`, `D/olay.py`, `D/zamanlar.json` | VAR | DOKUNMA |
| `D/nesneler.json` | uret.py yazar (§6.7) | — |

Başka dosyaya dokunma. Silme yok. Test, render, snapshot, git yok.

## 2. Kalıp kaynakları (salt oku)

| Kalıp | Mutlak yol | Ne alınır |
|---|---|---|
| **İskelet** (v1, aynı sahne) | `/home/sef/Silinecekler/2026-11-15-huni-v2/02-04-ydt-temel-s2/sahneler/04-hyperframes-hikaye/uret.py` | docstring düzeni; `AD`, `sys.path` + `import yardim as Y`, `PAKET`; `zaman.json` `hikaye` assert'leri (satır 20–25) ve `zamanlar.json` assert'leri (27–30); `MONT` ve `TISORT` listeleri (71–105, birebir); `ikon_svg` kalıbı (136–162; kutu ölçüsü burada değişir, §4.4); `kesisim()`; `uret()` HTML kabuğu (451–482); `__main__` (`proje/`, `Y.font_kopyala`, `index.html`, `nesneler.json`, stdout). **v1'in künyesi (`kunye_svg`, `kunye.js` regex okuması, çip), kartları, `today` hapı, `not1/not2`, `cg1/cg2`, `@ydspublishing` hapı ve `"kanal"` yasak taraması ALINMAZ** |
| Kanal katmanı + künye | `D/yardim.py` → `Y.kunye_svg()` (parametresiz), `Y.KONU`, `Y.ROZETLER`, `Y.HUD`, `Y.konu_boyu()`, `Y.rozet_konumlari()` | olduğu gibi çağır; sayı kopyalama |
| Yer imi simgesi | Tabler Icons `bookmark` (MIT), 24×24 viewBox: `M18 7v14l-6 -4l-6 4v-14a4 4 0 0 1 4 -4h4a4 4 0 0 1 4 4z` (yol sınır kutusu x 6–18, y 3–21) | uret.py içinde sabit `YERIMI_D`; yorumda kaynak ve lisans |
| Tema | `P/ortak/hf_tema.py` | §5 |

## 3. Okuma ve sabitler

- `PAKET = AD.parent.parent`. `PAKET/zaman.json` → `hikaye`: `klasor == AD.name`, `kare == 1`, `cikti == "hikaye-a.png"` assert;
  `sahneler[]` içinde `AD.name` YOK assert. `Z = D/zamanlar.json` (`sure` 1,0 · `kare` 1 · `fps` 30 assert).
- Anlatım, sözcük, altyazı, `kunye.js` OKUNMAZ (ses yok; künye `yardim.py`'den).
- `assert Y.KONU == "Simple Present vs Present Continuous"` ve `assert Y.ROZETLER == ("YDT · BASIC",)`.
- Renk yalnız `R = Y.RENK` anahtarlarıyla: `zemin`, `murekkep`, `ikincil`, `vurgu`. Başka hex YOK. Koyu hex yazılır; açık tema hf_tema ile gelir.

| Ad | Değer | Not |
|---|---|---|
| `X0`, `X1` | 60, 960 | içerik sol/sağ sınır |
| `SORU_TABAN` | 530 | Caveat 700 72 |
| `KART` | x 62, y 570, w 896, h 292, rx 32 | çerçeve dış kenarı 60–960 (stroke 4) |
| `TX` | 124 | kart yazı sol kenarı |
| `TABAN` | (658, 744, 826) (şef QA tur 1; v2 ilk koşu 740, 822) | kart cümlesinin 3 satırı, Fredoka 700 72 |
| `HAP_PAD`, `HAP_H`, `HAP_RX`, `HAP_UST` | 22, 88, 44, 64 (QA tur 1; ilk koşu h 84, üst 66: `y` kuyruğu kenara değdi) | `Today` hapı |
| `ESLESME_TABAN` | (926, 1000) | Caveat 700 64 |
| `IKON_X`, `IKON_W`, `IKON_H` | 60, 64, 56 | satır başı küçük ikon kutusu |
| `FIIL_X`, `OK_SON`, `ETIKET_X` | 140, 460, 484 | eşleşme sütunları |
| `KAYDET_BOY`, `KAYDET_TABAN` | 88, 1116 | Fredoka 700 |
| `YERIMI_S`, `YERIMI_UST` | 5.5, 1036 | 24×24 yol ölçeği, görünür üst kenar |
| `BOS_UST` | 1150 | bu y'den aşağısı boş (bağ çıkartması + platform) |

## 4. Yerleşim (y = yazı tabanı; kutu: yazı üstü = taban − 0,75·boy, altı = taban + 0,30·boy Caveat / 0,25·boy diğer)

```
y    0 ┌──────────────────────────────────────┐
       │ (boş zemin)                          │ 0–280
   291 │ [logo] @ydspublishing                │ kanal katmanı 291–341 (Y.kunye_svg)
   386 │ Simple Present vs Present Cont. (YDT · BASIC) │ künye 386–434
   530 │ Genel mi, şu an mı?                  │ Caveat 72 · 476–552
   570 │ ┌ kart ────────────────────────────┐ │ 570–862
   658 │ │ (Today) iki zamanda              │ │ Fredoka 72 · Today sarı hap (TEK SARI)
   744 │ │ da geçebilir;                    │ │
   826 │ │ farkı anlam yapar.               │ │
       │ └──────────────────────────────────┘ │
   926 │ [mont]   wears ─────────→ GENERAL    │ Caveat 64 · 878–945
  1000 │ [tişört] is wearing ───→ RIGHT NOW   │ Caveat 64 · 952–1019
  1116 │                 [yer imi] Kaydet     │ Fredoka 88, SAĞA yaslı (sağ kenar 960) · 1036–1138
  1150 │ (boş zemin: bağ çıkartması)          │ 1150–1380 hiçbir şey çizilmez
  1400 │ (boş)                                │ 1400–1920 boş
  1920 └──────────────────────────────────────┘
```

### 4.1 Kanal katmanı + künye
`Y.kunye_svg()` çıktısı aynen (içinde `<g id="kunye"><g id="kanal">…</g>…</g>`, logo `<image id="logoimg">`). Ekleme, değişiklik yok.

### 4.2 SVG düzeni
`<svg id="sahne">` içinde sıra: `{kunye}` → `<g id="icerik">` (soru, kart, eşleşme, kaydet). `#kanal` ve `#kunye` hiçbir tween'e girmez.

### 4.3 Öğeler (renkler SVG özniteliği, küçük harf hex)
| # | id | Öğe | Ölçü | Renk |
|---|---|---|---|---|
| 1 | `soru` | `<text>` `Genel mi, şu an mı?` | Caveat 700 72, x 60, taban 530 | fill murekkep |
| 2 | `kart` (g) | kural kartı | 4.3.1 | — |
| 3 | `eslesme` (g) | iki satır | 4.3.2 | — |
| 4 | `kaydet` (g) | yer imi + `Kaydet` | 4.3.3 | — |

#### 4.3.1 Kart (`<g id="kart">`, çizim sırası aşağıdaki gibi)
- `kart-crv`: `<rect x="62" y="570" width="896" height="292" rx="32" fill="none" stroke=murekkep stroke-width="4"/>`.
- `today-hap` (g): `hw = Y.genislik("Fredoka", 700, "Today", 72) + 2·22`; `<rect id="today-kutu" x=TX−22 (102) y=658−64 (594) width=hw height=88 rx=44 fill=vurgu/>`
  + `<text id="today-yazi" x=TX (124) y=658 Fredoka 700 72 fill=zemin>Today</text>` (text-anchor yok, sol başlangıç).
- `s1`: `<text x=(TX − 22 + hw + 20) y=658 Fredoka 700 72 fill=murekkep>iki zamanda</text>` (baştaki boşluk YOK).
- `s2`: `<text x=124 y=744 …>da geçebilir;</text>` · `s3`: `<text x=124 y=826 …>farkı anlam yapar.</text>` (Fredoka 700 72, murekkep).
- Her `<text>`'e `xml:space="preserve"`. Başka öğe yok (odak, altçizgi, ok, bant YOK).

#### 4.3.2 Eşleşme (`<g id="eslesme">`; satır i ∈ {1, 2}, taban T = 926 | 1000)
- İkon `ikon1` = `MONT` (ızgara 100×120), `ikon2` = `TISORT` (100×90). Kutu x 60–124, y (T − 20 − 28)–(T − 20 + 28) (64×56).
  `s = min(64/gw, 56/gh)`; kutuda ortalı `translate(60 + (64 − gw·s)/2, T − 48 + (56 − gh·s)/2) scale(s)`; `fill="none"`,
  `stroke` murekkep, `stroke-width = 3 / s` (görünür 3 px), round cap/join. Yol kuralı v1 `ikon_svg` ile aynı (egri 3 nokta → `M Q`, diğerleri `M L…`, daire → `<circle fill="none">`).
- Fiil `fiil1` = `wears`, `fiil2` = `is wearing`: Caveat 700 64, x 140, taban T, fill murekkep.
- Ok `ok1`, `ok2` (kalem çizgisi; glif DEĞİL): `<path>`; `oy = T − 16`; `ox0 = 140 + genislik(Caveat 700, fiil, 64) + 20`; gövde
  `M ox0 oy L 460 oy`; ok başı iki kısa çizgi, uzunluk 16, açı ±0,5 rad: `M (460 − 16·cos0.5) (oy − 16·sin0.5) L 460 oy L (460 − 16·cos0.5) (oy + 16·sin0.5)`
  (tek `d` dizisi, 1 ondalık). `fill="none"`, `stroke` ikincil, `stroke-width="4"`, round cap/join.
- Etiket `etiket1` = `GENERAL`, `etiket2` = `RIGHT NOW`: Caveat 700 64, x 484, taban T, fill murekkep.

#### 4.3.3 Kaydet (`<g id="kaydet">`, SAĞA yaslı)
- `kaydet-yazi`: `Kaydet` Fredoka 700 88; `kx = 960 − genislik(Fredoka 700, "Kaydet", 88)` (≈ 674,2); taban 1116; fill murekkep; text-anchor yok.
- `yerimi`: `<path d=YERIMI_D transform="translate(tx ty) scale(5.5)" fill="none" stroke=murekkep stroke-width=(6/5.5, 4 ondalık) stroke-linecap/linejoin round/>`.
  Görünür sağ kenar = `kx − 24` → `tx = (kx − 24 − 12·5.5) − 6·5.5`; `ty = 1036 − 3·5.5`. Görünür kutu ≈ x 584–650, y 1036–1135. Sarı DEĞİL (dolgu yok).

### 4.4 Ekran metni (tamamı; başka metin yok)
Künye (yardim): `@ydspublishing` · `Simple Present vs Present Continuous` · `YDT · BASIC`.
İçerik: `Genel mi, şu an mı?` · `Today` · `iki zamanda` · `da geçebilir;` · `farkı anlam yapar.` · `wears` · `GENERAL` · `is wearing` · `RIGHT NOW` · `Kaydet`.
Türkçe karakterler aynen (ş, ı, ç, ğ). `Tam ders`, `profildeki bağlantı`, ikinci `@ydspublishing` hapı, örnek kartları, çip YOK.

### 4.5 Olay listesi (tek kare; zaman çizelgesi dışı, anlatım yok)
| Olay | Kare / küresel sn | Cümle sözcüğü | Not |
|---|---|---|---|
| bütün öğeler görünür (kanal katmanı + künye + §4.3 1–4) | kare 0 (yakalama 0,5 sn; çizelge 1,0 sn) / küresel sn yok | — (ses yok; metin `hikaye-taslak.md` §3, BRIEF-S2 Hikâye A) | hiçbir öğe `opacity:0` başlamaz; giriş/çıkış hareketi yok |

GSAP: `gsap.timeline({ paused: true })`; `tl.set("#icerik", { opacity: 1, immediateRender: false }, 0)` ve aynı set `Z["sure"]`'de;
`window.__timelines["main"] = tl`. Başka tween YOK. Hedef `#icerik` (kanal katmanı tween dışında kalsın; `#sahne` hedeflenmez).

## 5. Tema (hf_tema.py ile uyum)
- `Y.ZEMIN_CSS` ve `Y.zemin_html()` DEĞİŞTİRMEDEN kullan. `<style>` içinde yalnız `Y.font_css()`, `Y.ZEMIN_CSS`, `#sahne{position:absolute;left:0;top:0;}`.
  **`#root.tema-acik` dizgisini uret.py çıktısına YAZMA** (hf_tema "zaten çevrildi" sanar, açık tema koyu kalır; S2 sahne 03 tur 1 hatası).
- Renkler SVG özniteliği: `fill="#f3efe6"`, `stroke="#c9c2b3"` vb. CSS `style` içinde renk YOK.
- Dönüşüm: `rect fill #f2a93b` → açıkta `#ffe066` · `text fill #1b1a17` → `#1b2440` · `#f3efe6` → `#1b2440` · `#c9c2b3` → `#5a6275`.
  Bu yüzden hap dolgusu `<rect fill="#f2a93b">`, hap yazısı `<text fill="#1b1a17">`. `<path|circle fill="#1b1a17">` YOK.
- id `t2`, `ku-nokta`, `rz1` KULLANMA.

## 6. Kurallar ve kabul ölçütü (uret.py içinde `assert`)
Blok kutuları (`ad, x, y, w, h`, float): `kanal` (53,15 · 291 · 263 + genislik(Lexend 700, "@ydspublishing", 42) − 53,15 · 341 − 291) ·
`kunye` (60 · 386 · rozet sağ kenarı − 60 · 48; rozet sağı `Y.rozet_konumlari()`'ndan) · `soru` · `kart` (60 · 568 · 900 · 296; stroke dahil) ·
`eslesme` (60 · 878 · max(etiket sağ kenarı) − 60 · 1000 + 0,30·64 − 878) · `kaydet` (yer imi sol − 3 · 1036 − 3 · 960 − (yer imi sol − 3) · 1138 − 1033).
1. Bütün blok x ∈ [53, 960]; `kanal` dışındaki bloklar x ≥ 60. Hiçbir blok y < 280; içerik blokları (soru, kart, eslesme, kaydet) y ≥ 460 ve alt ≤ `BOS_UST` (1150).
2. İçerik yazı boyu ≥ 64 (soru 72, kart 72, eşleşme 64, Kaydet 88). Künye/kanal hariç (BRIEF ölçüsü).
3. İçerik satırı ≤ 24 karakter (`len`): `Today iki zamanda` (hap + s1 birlikte) · `da geçebilir;` · `farkı anlam yapar.` · `Genel mi, şu an mı?` · `wears` ·
   `GENERAL` · `is wearing` · `RIGHT NOW` · `Kaydet`. Künye konu satırı BRIEF gereği tek satırdır, sayılmaz.
4. Blok çiftleri kesişmez (alan 0). Dikey sıra `kanal → kunye → soru → kart → eslesme → kaydet` komşu boşluğu ≥ 12.
5. Kart içi: hap kutusu kart çerçevesinin içinde, her yönde ≥ 16 boşluk; `s1` sol ≥ hap sağı + 16; s1/s2/s3 sağ kenarı ≤ 958 − 32;
   satır 2 yazı üstü (744 − 54) > hap altı (594 + 88); satır 3 alt (826 + 18) + 16 ≤ çerçeve altı (862).
6. Eşleşme: satır 1 alt (926 + 19,2) ≤ satır 2 üst (1000 − 48); her satırda `ox0 ≥ fiil sağı + 16`, `460 − ox0 ≥ 40`, `460 + 20 ≤ 484`;
   etiket sağ kenarı ≤ 960; ikon kutusu sağı (124) + 16 ≤ 140.
7. Kaydet: `kaydet-yazi` sağ kenarı = 960 (±0,5); yer imi görünür sağı + 20 ≤ `kx`; yer imi görünür üstü 1036, altı ≤ 1140.
8. Tek sarı: `#icerik` grubunun HTML'inde `fill="#f2a93b"` tam 1 kez (`today-kutu`), `stroke="#f2a93b"` 0 kez.
9. Yasak (küçük/büyük harf duyarsız, üretilen HTML): `tam ders`, `dakika`, `qr`; SVG `<text>` içeriklerinde `dk`; `opacity:0`; `R["kirmizi"]`;
   `#root.tema-acik`; emoji (U+1F000 üstü ve U+2600–U+27BF kod noktası). `Math.random`, `Date`, try/catch, gölge, gradyan ekleme YOK.
10. `nesneler.json`: blok kutuları `[{"ad","x","y","w","h"}]` tam sayı (yuvarla), §6 sırası.
11. Python: bütün işlevlerde tür ipuçları. `python3 uret.py` stdout: `index.html yazıldı <bayt>` ve
    `soru=<üst>-<alt> kart=… eslesme=… kaydet=…`; hata yoksa çıkış 0.

Kabul (şef koşturur, ajan koşturmaz): `ONIZLE_YALNIZ=1 bash calistir.sh` → "önizleme hazır"; `bash calistir.sh --tema acik|koyu` →
`P/hikaye-a.png` + `P/hikaye.png` ve `D/k/hikaye-a-koyu.png` 1080×1920; karede taşma, kesik yazı, üst üste binme yok; 0–280 ve 1150–1920 boş;
kanal katmanı iki temada yerinde; tek sarı öğe `Today` hapı (künye rozeti hariç).
