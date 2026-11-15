# SPEC v2 — 02-04-ydt-temel-s3 · sahne 06-hyperframes-kapak-c (kapak C, karşıt çift) · huni v2 · 15.11.2026

Yazan: şef (istem D-V2-S3). Kod yazmaz; tasarım verir. K = `/home/sef/01dev/_worktrees/kalem-0204`.
D = `K/projeler/02-04-ydt-temel-s3/sahneler/06-hyperframes-kapak-c/` · P = `K/projeler/02-04-ydt-temel-s3/`.
BAĞLAYICI: `/home/sef/01dev/dijital-anlatim/.claude/docs/huni-v2-standart.md` §2 (bantlar), §6 (kapak: altyazı yok, kanal katmanı var).
Tarif: `P/BRIEF-S3.md` "Yerleşim" + "Kapak B ve C" (C satırı). v1 SPEC yedeği: `~/Silinecekler/2026-11-15-huni-v2/02-04-ydt-temel-s3/sahneler-v1/06-hyperframes-kapak-c/SPEC.md`.

## 1. Dosyalar

| Dosya | Durum | İş |
|---|---|---|
| `/home/sef/01dev/_worktrees/kalem-0204/projeler/02-04-ydt-temel-s3/sahneler/06-hyperframes-kapak-c/uret.py` | VAR (v1) | **YENİDEN YAZILACAK** (v1 başlangıç noktası; §2 tablosundaki işlevler korunur, §3–§7 değişir) |
| `D/yardim.py` | VAR (v1 HUD) | DOKUNMA. Yalnız `Y.genislik`, `Y.font_css`, `Y.font_kopyala`, `Y.ZEMIN_CSS`, `Y.zemin_html`, `Y.RENK`, `Y.LOGO_EN_BOY`, `Y.LOGO_KAYMA`, `Y.W`, `Y.H`. `Y.kunye_svg`, `Y.HUD`, `Y.rozet_konumu`, `Y.DERS`, `Y.altyazi_*` KULLANILMAZ (v1 HUD) |
| `D/cizim/ogretmen.json` | VAR | salt oku (`kutu` = [43,7, 54,6, 958,9, 3006,8], `yollar[].d`, `yollar[].parca`) |
| `D/calistir.sh`, `D/olay.py`, `D/zamanlar.json` | VAR | DOKUNMA |
| `D/nesneler.json`, `D/proje/index.html` | uret.py yazar | §7 |

Başka dosyaya dokunma. Silme yok. Test, render, snapshot, `calistir.sh`, git YOK.

## 2. Kalıp kaynakları (salt oku)

| Kalıp | Mutlak yol | Ne alınır |
|---|---|---|
| v1 kodu (aynı sahne) | `/home/sef/01dev/_worktrees/kalem-0204/projeler/02-04-ydt-temel-s3/sahneler/06-hyperframes-kapak-c/uret.py` | AYNEN koru: `zaman.json` + `zamanlar.json` doğrulaması (satır 21–35), `g()`, `_kutu`, `TREN`, `_bilet`/`BILET`, `_kutusu`, `_daire_yolu`, `ikon_yollari`, `ikon_kutusu`, `ikon_svg`, `el_kutu`, `kesisim`, başlık `<text>` kalıbı (`bs-1` konturlu, `bk-kutu`, `bs-2` kontursuz), figür çizimi (`fig_kalinlik`, `/ fs`), HTML kabuğu (satır 620–645, iki `tl.set`), `__main__` bloğu. DEĞİŞİR: sabitler, `kunye_svg`, `hesapla_s_ve_baslik`, `kartlar_svg`, `eskiz_svg`, `blok_kutulari`, `kurallari_dogrula`, modül docstring'i |
| Kanal katmanı + rozet (aynı paket, kapak A) | `/home/sef/01dev/_worktrees/kalem-0204/projeler/02-04-ydt-temel-s3/sahneler/01-hyperframes-kapak/uret.py` satır 191–201 (`ROZET_W`, `KB_K` döngüsü, `ROZET_X`), 228–229 (`LOGO_W`, `LOGO_X`), 664–684 (`_kunye_svg`) | `kanal` grubu ve `rz0` grubu birebir; `ku-konu` YAZILMAZ (KONU yalnız rozet konumunu ölçmek için) |

## 3. Sabitler ve renk

- `SOL = 60`, `SAG = 960` (içerik x), `ICERIK_UST = 460`, `ICERIK_ALT = 1380`. 0–280 ve 1400–1920 yalnız zemin (hiçbir öğe yok).
- Renk yalnız `Y.RENK` anahtarlarıyla: `zemin #1b1a17`, `murekkep #f3efe6`, `ikincil #c9c2b3`, `vurgu #f2a93b`. Başka hex YOK.
  Tema dönüşümü `P/ortak/hf_tema.py` yapar (açık: `rect fill #f2a93b` → `#ffe066`, `text fill #1b1a17` → `#1b2440`, `#f3efe6` → `#1b2440`,
  `stroke #1b1a17` → zemin). Bu yüzden rozet/`bk-kutu`/`hap-leaves` = `<rect fill="#f2a93b">`; rozet yazısı, `bs-2`, `m1b` = `<text fill="#1b1a17">`.
  CSS içinde renk yazma. `<path fill="#1b1a17">` YOK.
- Ölçü: `g(m, b) = Y.genislik("Fredoka", 700, m, b)`; her Fredoka yazısında `style="font-kerning:none"`.

## 4. Yerleşim (y = yazı tabanı; beklenen değerler `≈`)

```
y    0 ┌──────────────────────────────────────────┐ 0–280 yalnız zemin
   291 │[logo 193,5×48] @ydspublishing            │ kanal katmanı (kapak A ile aynı piksel)
   386 │                      (YDT · TEMEL)       │ rozet x ≈ 664,6–868,2 (kapak A konumu); konu adı YOK
   460 │   İKİ ÖRNEK                              │ Fredoka 700 S = 170; kontur dahil üst = 460
  ≈645 │  [İKİ ZAMAN]                             │ sarı kutu x ≈ 87,6–932,4
  ≈849 │                                          │ başlık altı
   896 │┌───────────────────────────────┐         │ kart 1: [tren] The train [leaves] …
  1096 │└───────────────────────────────┘    o    │
  1132 │┌───────────────────────────────┐   /|\   │ kart 2: [bilet] I am going …
  1332 │└───────────────────────────────┘  _/ \_  │ figür 280 px, ayak 1332 + kısa zemin çizgisi
  1400 ├──────────────────────────────────────────┤ 1400–1920 BOŞ (altyazı yok)
       60                                 ≈841 ≈865 952 960
```

### 4.1 Künye — `<g id="kunye">` = `kanal` + `rz0` (konu adı, çip, üst logo YOK)
| Öğe | Ölçü |
|---|---|
| `<g id="kanal">` logo | `<image id="logoimg" href="assets/logo.svg" x=LOGO_X y="291" width=LOGO_W height="48"/>`; `LOGO_W = 48·Y.LOGO_EN_BOY` (≈ 193,49), `LOGO_X = 60 − Y.LOGO_KAYMA·LOGO_W` (≈ 53,15) |
| `kanal` yazısı | `<text id="kanal-ad" x="263" y="330" font-family="Lexend" font-weight="700" font-size="42" fill=murekkep>@ydspublishing</text>` |
| `<g id="rz0">` | `KONU = "Simple Present vs Present Continuous"`, `ROZET = "YDT · TEMEL"`, `ROZET_W = Y.genislik("Lexend", 700, ROZET, 26) + 40` (≈ 203,57); `KB_K` = 34'ten 28'e ilk `60 + g(KONU, k) + 20 + ROZET_W ≤ 960` (≈ 34); `ROZET_X = 60 + g(KONU, KB_K) + 20` (≈ 664,63). `<rect x=ROZET_X y="386" width=ROZET_W height="48" rx="24" fill=vurgu/>` + `<text x=ROZET_X+ROZET_W/2 y="419.4" text-anchor="middle" font-family="Lexend" font-weight="700" font-size="26" fill=zemin>YDT · TEMEL</text>` |

Opaklık 1; giriş/çıkış yok (zaman çizelgesinde yalnız iki `tl.set("#sahne", {opacity:1})`).

### 4.2 Başlık — `<g id="baslik">`
- Metin elle büyük harf, Türkçe `İ` (U+0130); `text-transform` YOK: `bs-1` `İKİ ÖRNEK`, `bs-2` `İKİ ZAMAN`.
- Boy: `S = 170`; `p = 0,08·S`; `B = max(g("İKİ ÖRNEK", S), g("İKİ ZAMAN", S) + 2p)`; `B > 900` iken S'yi 1 azalt. Beklenen S = 170, B ≈ 844,7.
- Yatay: içerik bandında ortalı. `KX = 510 − B/2` (≈ 87,6); iki satırın yazı başı aynı `x0 = KX + p`; kutu genişliği `kutu_w = g("İKİ ZAMAN", S) + 2p`.
- Dikey: `T1 = 466 + 0,93·S` (≈ 624,1; İ noktası 466, kontur 6 → 460) · `KU = T1 + 0,12·S` (≈ 644,5) · `T2 = KU + 1,00·S` (≈ 814,5) ·
  `KA = T2 + 0,20·S` (≈ 848,5) · kutu rx `0,10·S`.
- `bs-1`: x0, T1, `fill` murekkep, `stroke` zemin, `stroke-width` 12, `stroke-linejoin="round"`, `style="font-kerning:none;paint-order:stroke fill"`.
- `<rect id="bk-kutu">` x KX, y KU, w kutu_w, h KA − KU, `fill` vurgu. `bs-2`: x0, T2, `fill` zemin, KONTURSUZ.

### 4.3 Figür — önce hesaplanır (kart genişliği buna bağlı)
`FIG_H = 280`, `FIG_ALT = 1332`, `fs = FIG_H / (kutu.y1 − kutu.y0)`, `fw = (kutu.x1 − kutu.x0)·fs` (≈ 86,8), `FIG_SAG = 952`, `FIG_X = FIG_SAG − fw` (≈ 865,2).
Çizim v1 `eskiz_svg()` ile aynı (translate + scale, `fig_kalinlik / fs`), yalnız ölçüler bu değerler. `<path id="zc">` zemin çizgisi
`M{FIG_X − 12} 1332 L956 1332`, `stroke-width` 4. Grup `<g id="eskiz" fill="none" stroke=murekkep stroke-linecap="round" stroke-linejoin="round">`.

### 4.4 Kartlar — `<g id="kartlar">` (üst üste, AYNI x, w, h)
| Ölçü | Değer |
|---|---|
| Kart x | `KART_X0 = 64` → `KART_X1 = FIG_X − 24` (≈ 841,2); `KART_W = KART_X1 − KART_X0` (≈ 777,2); `KART_H = 200` |
| Kart üstü | kart 1 `896`, kart 2 `1132` (ara 36); kart 2 altı 1332 = `FIG_ALT` |
| Çizgi | `<path id="kc1">` / `<path id="kc2">` d = `el_kutu(KART_X0, y, KART_W, 200)`, `fill="none"`, `stroke` murekkep, 4, round |
| Yazı tabanı | `b = y + 126` (kart 1 1022, kart 2 1258); ikon merkezi y = `y + 100` |
| Yazı başı (iki kartta aynı) | `METIN_X = KART_X1 − 24 − g("The train leaves …", 72)` (≈ 208,6) |
| İkon kutusu (iki kartta aynı) | x `84` → `METIN_X − 20`; `IKON_EN = METIN_X − 20 − 84` (≈ 104,6), `IKON_BOY = 100`, merkez x `84 + IKON_EN/2`; `ikon_yollari`/`ikon_svg` oranı korur, ortalar |

Kart 1 (`<g id="kart1">`): `kc1` + `ik-tren` + Fredoka 700 72 üç `<text>`:
- `m1a` `The train` x METIN_X, `fill` murekkep.
- `<rect id="hap-leaves">` x `XL − 0,12·72`, y `b − 0,86·72`, w `g("leaves", 72) + 2·0,12·72`, h `1,04·72`, rx 12, `fill` vurgu; `XL = METIN_X + g("The train ", 72)`.
- `m1b` `leaves` x XL, `fill` zemin, KONTURSUZ. **Kapaktaki tek kart vurgusu budur.**
- `m1c` `…` (U+2026) x `XL + g("leaves ", 72)`, `fill` murekkep.

Kart 2 (`<g id="kart2">`): `kc2` + `ik-bilet` + `<text id="m2">` `I am going …` x METIN_X, b 1258, Fredoka 700 72, `fill` murekkep. `am going` VURGUSUZ.
İkonlar v1 `TREN` (lokomotif alt kümesi) ve `BILET` aynen; ince parça `ikincil` 3, diğeri `murekkep` 4; dolgu yok.

## 5. Olay listesi (durağan kare; ses, altyazı, karaoke yok)

| Olay | Kare / sn | Cümle sözcüğü |
|---|---|---|
| kapak tam görünür (kanal, rozet, başlık, kutu, iki kart, ikonlar, hap, figür, zemin çizgisi) | 0 / 0,00 → son (çizelge 1,0 sn, yakalama 0,5 sn) | — (anlatımdan bağımsız) |

Ekran metni (tam liste): `@ydspublishing` · `YDT · TEMEL` · `İKİ ÖRNEK` · `İKİ ZAMAN` · `The train` `leaves` `…` · `I am going …`. Başka yazı yok.
Can alıcı: `canAlici[1]` (V-s, `leaves`) + `[2]` (am + V-ing, `am going`).

## 6. Kurallar ve kabul ölçütü (uret.py içinde `assert`)

1. Bloklar (nesneler.json sırası): `kanal` (x 60, y 280, w `263 + Y.genislik("Lexend", 700, "@ydspublishing", 42) − 60`, h 70) ·
   `rozet` (ROZET_X, 386, ROZET_W, 48) · `baslik` (x KX, y `T1 − 0,93·S − 6`, w B, alt KA) · `bk-kutu` · `kart-1` · `ik-tren` · `m-1` ·
   `hap-leaves` · `kart-2` · `ik-bilet` · `m-2` · `fig` (FIG_X, FIG_ALT − FIG_H, fw, FIG_H). Yazı kutusu: y_üst = taban − 0,75·boy, h = boy.
   Kart kutusu el kutusu salınımını içerir (x − 4, y − 4, w + 8, h + 8). İkon kutusu = `ikon_kutusu` sonucu.
2. Bütün bloklar: x ≥ 60 − 1e-4, x + w ≤ 960, y ≥ 280, y + h ≤ 1380. `kanal`, `rozet` dışı bloklar y ≥ 460 − 1e-4.
3. Kesişim 0: `kanal`, `rozet`, `baslik`, `kart-1`, `kart-2`, `fig` çiftleri.
   Aralar: rozet altı 434 → başlık üstü ≥ 20 · KA → kart 1 üstü ≥ 40 · kart 1 altı → kart 2 üstü ≥ 24 · `KART_X1 + 4` → FIG_X ≥ 16.
4. Başlık: S ≤ 170, S ≥ 64, B ≤ 900, `KX ≥ 60`, `KX + kutu_w ≤ 960`, `KU ≤ T2 − 0,93·S` (kutu İ noktasını içerir).
5. Kart içi: `ik-*` ve `m-*` kendi kartının iç kutusunda (kenara ≥ 16); ikon sağı → METIN_X ≥ 20; `m-1` sağı ≤ `KART_X1 − 24`;
   `hap-leaves` solu ≥ `METIN_X + g("The train", 72) + 4`, sağı ≤ `XL + g("leaves ", 72) − 4`. `IKON_EN ≥ 96`; `ik-tren` h ≥ 70.
6. Kart 1 ile kart 2 aynı (x, w, h). Yazı boyu ≥ 64 (künye 42 ve 26 hariç). Satır ≤ 24 karakter (§5 metinleri).
7. HTML: `#[0-9a-fA-F]{6}` kümesi ⊆ {4 renk}. Küçük harfe çevrilmiş HTML'de `tam ders`, `dakika`, `qr`, ` dk`, `izle` YOK.
   HTML'de `id="kanal"`, `@ydspublishing`, `href="assets/logo.svg"`, `id="rz0"` VAR; `id="ku-konu"`, `id="ku-logo"`, `id="ku-cip"`,
   `id="ku-ders"`, `id="altyazi"`, `id="t2"` YOK. (v1'deki "`kanal` geçmez" kuralı KALKAR.)
8. Yasak: `Math.random`, `Date`, `try`, `catch`, `opacity:0`, tween (iki `set` dışında hareket yok), gradyan, gölge, emoji, kırmızı, yeşil.
   Python: bütün işlevlerde tür ipucu.
9. `nesneler.json`: `[{"ad", "x", "y", "w", "h"}]` tam sayı (yuvarla), §6.1 sırası, `ensure_ascii=False`, `indent=2`.
10. `/usr/bin/python3 uret.py` stdout'a `index.html yazıldı <bayt>` ve `S=<boy>` basar; hata yoksa çıkış 0.

Kabul (şef koşturur, ajan koşturmaz): `bash calistir.sh --tema acik|koyu` → `P/kapak-c.png` ve `D/k/koyu/kapak-c-koyu.png` 1080×1920;
kanal katmanı x 60, y 291–339; 0–280 ve 1400–1920 boş; x 960 sağı boş; taşma, kesik yazı, üst üste binme yok.
