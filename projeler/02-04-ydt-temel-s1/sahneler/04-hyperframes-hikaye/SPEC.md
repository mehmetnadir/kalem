# SPEC — sahne 04 hikâye karesi A, huni v2 (02-04-ydt-temel-s1) · 15.11.2026

MAKİNE: Linux x86_64 (srv21). Python `/usr/bin/python3` (fontTools kurulu). Şef yazdı; kodu agy yazar.

| Ne | Değer |
|---|---|
| Yazılacak dosya | `/home/sef/01dev/_worktrees/kalem-0204/projeler/02-04-ydt-temel-s1/sahneler/04-hyperframes-hikaye/uret.py` (baştan yaz) |
| Kalıp kaynağı (v1, salt okunur) | `/home/sef/Silinecekler/2026-11-15-huni-v2/02-04-ydt-temel-s1/sahneler/04-hyperframes-hikaye/v1/uret.py` |
| Yardımcı (HAZIR, değiştirme) | `.../sahneler/04-hyperframes-hikaye/yardim.py` (v2; `Y.kunye_svg()`, `Y.HUD`, `Y.genislik`, `Y.tabler`, `Y.RENK`, `Y.font_css`, `Y.ZEMIN_CSS`, `Y.zemin_html`, `Y.font_kopyala`) |
| Bağlayıcı standart | `/home/sef/01dev/dijital-anlatim/.claude/docs/huni-v2-standart.md` §1, §2, §6 |
| Çıktı (uret.py yazar) | `proje/index.html`, `nesneler.json` (sahne dizininde) |

Kare: 1080×1920, durağan, ses yok, altyazı yok, çip yok. Zaman çizelgesi 1,0 sn (yakalama 0,5 sn, `zamanlar.json` değişmez).

## 1. v1'den aynen alınacak kalıplar

- Dosya başı: `from __future__ import annotations`, `AD`, `sys.path.insert`, `import yardim as Y`, `PAKET`.
- `zaman.json` ve `zamanlar.json` okuma + 6 assert (v1 satır 18–28) aynen.
- `hesapla_s_ve_ek()`: aynı genişlik formülü (`wa + wt + ara + 2p + wy + ara + wt + ara + wu`, `p = 0,14·S`, `ara = 0,08·S`),
  yalnız sınır değişir: **genişlik ≤ 900, üst sınır S = 124** (v1: 952 ve 170).
- `ek_svg()`: v1 ile aynı 5 metin + 1 kutu (`ek-kutu`, `ek-yasi`, `ek-tire1`, `ek-yor`, `ek-tire2`, `ek-um`), aynı renkler
  (`YAŞI`/`UM` murekkep, tireler ikincil, `YOR` yazısı `R["zemin"]`, kutu `R["vurgu"]`). Değişen: yatay merkez **510** (v1 540),
  taban `EK_Y = 583`.
- `kesisim()` işlevi, `kurallari_dogrula()` assert yapısı, HTML iskeleti (v1 satır 304–334: `font_css`, `ZEMIN_CSS`, `#root`
  `data-duration` = `Z['sure']`, `zemin_html()`, `<svg id="sahne">`, GSAP iki `tl.set`, `window.__timelines["main"]`),
  `__main__` bölümü (font kopyası, `index.html`, `nesneler.json` tam sayıya yuvarlanmış).
- `BAVUL` yol listesi (v1 satır 45–52) aynen.
- Tür ipucu zorunlu, girinti 4 boşluk (dosyanın var olan stili), satır ≤ 130 karakter.

## 2. Kaldırılan v1 öğeleri

v1 `kunye_svg()` (logo y 48, 2 satır ders adı, rozet, `Full lesson` çipi), `ust` (`Türkçede tek sözcük`), `alt`
(`İngilizcede iki zaman`), `cg1` (`Tam ders:`), `cg2` (`profildeki bağlantı`), alt `@ydspublishing` hapı, kart içi zaman ekseni,
bant, `now` noktası, altçizgi (`-odak`). Künye artık `Y.kunye_svg()` çağrısından gelir (uret.py içinde künye kodu YOK).

## 3. Yerleşim (px, mutlak)

| Blok | Kimlik | x | y | İçerik |
|---|---|---|---|---|
| kanal | `kanal` (Y.kunye_svg içinde) | resim 53,2–246,7; yazı 263 → | 291–339 | logo + `@ydspublishing` (dokunma) |
| künye | `ku-konu`, `rz0` (Y.kunye_svg içinde) | 60–868 | 386–434 | konu + rozet `YDT · TEMEL` (dokunma) |
| ek | `ek` | merkez 510, genişlik ≤ 900 | kutu 476,4–602,9; blok 476–611 | `YAŞI-YOR-UM`, S = 124, taban 583 |
| kart 1 | `kart1` | 60–498 | 636–840 | ev ikonu + `I live` + `PERMANENT` |
| kart 2 | `kart2` | 522–960 | 636–840 | bavul ikonu + `I am living` + `TEMPORARY` |
| özet | `ozet` | 60 → | taban 924, 1008, 1092 | `Live, work fiillerinde:` / `kalıcıysa geniş zaman,` / `geçiciyse şimdiki zaman.` (DUZ2 15.11) |
| kaydet | `kaydet` | 60–416 | 1416–1504 (DUZ2: hikâye B ile aynı yer) | yer imi simgesi + `Kaydet` sarı hap |
| boş | — | — | 1150–1920 | hiçbir öğe yok (bağ çıkartması elle konur; kutu, çerçeve çizme) |

### 3.1 Kart (`kart_svg(simge, x0, ikon_yollar, baslik, etiket)`)
- Çerçeve: `<rect id="{simge}-crv" x=x0+2 y=638 width=434 height=200 rx=26 fill="none" stroke=R["murekkep"] stroke-width=4>`
  (QA 1: çizginin dış kenarı x0..x0+438, y 636–840; ilk sürüm x0/438/204 ile 961'e taşıyordu). Yer imi translate x 36 → 39 (aynı sebep).
- İkon: `<g id="{simge}-ikon" transform="translate({x0+24} 660) scale({80/24})" fill="none" stroke=R["murekkep"]
  stroke-width=1.5 stroke-linecap="round" stroke-linejoin="round">` + her yol için `<path d=…/>`.
  Kart 1 `Y.tabler("home")`, kart 2 `BAVUL`.
- Başlık: `<text id="{simge}-baslik" x={x0+116} y=722>` Fredoka 700, 64, R["murekkep"], `xml:space="preserve"`.
- Etiket: `<text id="{simge}-etiket" x={x0+24} y=800>` Caveat 700, 64, R["murekkep"].
- Kart 1 x0 = 60, kart 2 x0 = 522.

### 3.2 Özet
Üç `<text>` (DUZ2): `id="ozet1"` y 924, `ozet2` y 1008, `ozet3` y 1092, x 60; Fredoka 700, 68, R["murekkep"]; bir `<g id="ozet">` içinde.

### 3.3 Kaydet
- `<g id="kaydet">` içinde:
- Yer imi: `<path id="kaydet-imi" d="M18 7v14l-6 -4l-6 4v-14a4 4 0 0 1 4 -4h4a4 4 0 0 1 4 4z">`, bir `<g transform="translate(39 1412)
  scale(4)" fill="none" stroke=R["murekkep"] stroke-width=1.5 stroke-linejoin="round" stroke-linecap="round">` içinde
  (görünür kutu x 60–108, y 1056–1128). Emoji yok.
- Hap: `hap_w = Y.genislik("Fredoka", 700, "Kaydet", 64) + 80`; `<rect id="kaydet-hap" x=128 y=1416 width=hap_w height=88 rx=44
  fill=R["vurgu"]>` (tema dönüştürücüsü açıkta `#ffe066` yapar).
- Yazı: `<text id="kaydet-yazi" x={128 + hap_w/2} y=1482 text-anchor="middle">` Fredoka 700, 64, fill R["zemin"] (açıkta `pilMetin`).

### 3.4 SVG sırası
`Y.kunye_svg()` → `ek` → `kart1` → `kart2` → `ozet` → `kaydet`. Kanal katmanında animasyon yok; timeline yalnız `#sahne` opaklık 1.

## 4. Blok kutuları (`blok_kutulari`, `nesneler.json`)

| ad | x | y | w | h |
|---|---|---|---|---|
| kanal | 53,2 | 291 | 263 + genişlik(Lexend 700 `@ydspublishing` 42) − 53,2 | 48 |
| kunye | 60 | 386 | rozet x + rozet w − 60 (`Y.rozet_konumlari()[0]`) | 48 |
| ek | 510 − top/2 | EK_Y − 0,86·S | top | 1,08·S (alt = EK_Y + 0,22·S, Ş çengeli) |
| kart1 | 60 | 636 | 438 | 204 |
| kart2 | 522 | 636 | 438 | 204 |
| ozet | 60 | 924 − 0,75·68 | max(üç satır genişliği) | (1092 + 0,25·68) − y |
| kaydet | 60 | 1416 | 128 + hap_w − 60 | 88 |

## 5. Kurallar (`kurallari_dogrula`, assert)

1. İçerik blokları (ek, kart1, kart2, ozet): x ≥ 60, x + w ≤ 960, y ≥ 460, y + h ≤ 1140; kaydet y 1400–1520 (DUZ2).
2. kanal ve kunye: y ≥ 280, y + h ≤ 450.
3. Bütün blok çiftlerinin kesişim alanı 0.
4. Dikey boşluk ≥ 16: kunye → ek, ek → kart1, ek → kart2, kart1 → ozet, ozet → kaydet. Yatay: kart2.x − (kart1.x + kart1.w) ≥ 16.
5. Kart içi: `116 + genişlik(Fredoka 700 başlık 64) ≤ 438 − 24`; `genişlik(Caveat 700 etiket 64) ≤ 438 − 48`.
6. Yazı boyları: S ≥ 64; kart başlığı, etiket, hap yazısı 64; özet 68.
7. Ekran satırı ≤ 24 karakter: `YAŞI-YOR-UM`, `I live`, `PERMANENT`, `I am living`, `TEMPORARY`, `Live, work fiillerinde:`, `kalıcıysa geniş zaman,`,
   `geçiciyse şimdiki zaman.`, `Kaydet` (künye ve kanal satırı hariç).
8. (QA 1'de kaldırıldı) Yasak söz denetimi kodda değil, dış grep kapısında: koddaki literal liste grep'i kirletiyordu.
9. HTML'de `id="kanal"` ve `id="logoimg"` tam 1 kez geçer.

## 6. Kabul ölçütü

- `/usr/bin/python3 uret.py` rc 0; çıktı `index.html yazıldı <n>` ve `S=<n>` (beklenen S = 124).
- `nesneler.json` 7 blok (kanal, kunye, ek, kart1, kart2, ozet, kaydet), tam sayı.
- `proje/index.html`: `id="kanal"`, `ek-yor`, `kart1-baslik`, `kart2-etiket`, `ozet2`, `kaydet-imi`, `kaydet-hap` var;
  `ku-cip`, `cg1`, `hap-kutu`, `ust`, `alt` kimlikleri yok.
- Test, render, git YOK (şef koşar).
