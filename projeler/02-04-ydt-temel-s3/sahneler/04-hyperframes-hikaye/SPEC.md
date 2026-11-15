# SPEC v2 — 02-04-ydt-temel-s3 · sahne 04-hyperframes-hikaye (hikâye A, kural kartı) · huni v2

Yazan: şef (15.11.2026, istem D-V2-S3). Kod yazmaz; tasarım verir. K = `/home/sef/01dev/_worktrees/kalem-0204`.
Sahne dizini D = `K/projeler/02-04-ydt-temel-s3/sahneler/04-hyperframes-hikaye/`. Paket P = `K/projeler/02-04-ydt-temel-s3/`.
Bağlayıcı: `/home/sef/01dev/dijital-anlatim/.claude/docs/huni-v2-standart.md` §2, §6 · `P/BRIEF-S3.md` "Yerleşim" + "Hikâye karesi A".
v1 yedeği: `~/Silinecekler/2026-11-15-huni-v2/02-04-ydt-temel-s3/sahneler-v1/04-hyperframes-hikaye/`.

Durağan kare: ses yok, altyazı yok, zaman çizelgesi 1,0 sn (yakalama 0,5 sn). Olay listesi YOK (`olaylar.json` = `[]`, `olay.py` değişmez).

## 1. Dosyalar

| Dosya | Durum | İş |
|---|---|---|
| `D/uret.py` | VAR (v1) | **YERİNDE YENİDEN YAZ** — mutlak yol `/home/sef/01dev/_worktrees/kalem-0204/projeler/02-04-ydt-temel-s3/sahneler/04-hyperframes-hikaye/uret.py` |
| `D/yardim.py` | VAR (v1 HUD) | DOKUNMA; yalnız `Y.genislik`, `Y.font_css`, `Y.font_kopyala`, `Y.ZEMIN_CSS`, `Y.zemin_html`, `Y.RENK`, `Y.LOGO_EN_BOY`, `Y.LOGO_KAYMA` kullanılır. `Y.kunye_svg`, `Y.HUD`, `Y.rozet_konumlari` KULLANILMAZ (v1) |
| `D/calistir.sh`, `D/olay.py`, `D/zamanlar.json` | VAR (şef) | DOKUNMA |
| `D/nesneler.json`, `D/proje/index.html` | uret.py yazar | §8 |

Başka dosyaya dokunma. Silme yok. Test, render, snapshot, git yok.

## 2. Kalıp kaynakları (salt oku)

| Kalıp | Mutlak yol | Ne alınır |
|---|---|---|
| İskelet + ikon verisi | `D/uret.py` (v1, şu anki dosya) | Docstring yeni bantlarla; `AD`, `sys.path` + `import yardim as Y`, `PAKET`, `zaman.json`/`zamanlar.json` okuma + bütün assert'ler; `R = Y.RENK`; `_kutu`, `TREN`, `_bilet`, `BILET`, `_kutusu`, `_daire_yolu`, `ikon_yollari` **BİREBİR korunur**; `bas_svg` içindeki `≠` kalem çizimi (3 yol) ve `PLAN` yerleşim oranları korunur; `kesisim()`; `uret()` HTML kabuğu (font_css, ZEMIN_CSS, `#root`, `Y.zemin_html()`, tek `<svg id="sahne">`, `esitdegil-stil`, gsap, iki `tl.set`, `window.__timelines["main"]`); `__main__` (font_kopyala, index.html, nesneler.json, iki print). SİLİNECEK v1 içerik: `kunye_svg` (v1 HUD: logo 48–144, 2 satır ders adı, `Full lesson` çipi), `kart1_svg`, `kart2_svg`, `alt` satırı, `cg1`/`cg2` (Caveat çağrı), `hap` (`@ydspublishing` alt hap), saat ikonu, Caveat etiketleri |
| v2 kanal katmanı + künye | `/home/sef/01dev/_worktrees/kalem-0204/projeler/02-04-ydt-temel-s2/sahneler/01-hyperframes-kapak/yardim.py` satır 147–222 | `HUD` sözlüğü, `konu_boyu()`, `rozet_konumlari()`, `kunye_svg()` kalıbı: `uret.py` içine yerel işlev olarak taşınır (yardim.py'ye yazılmaz). Fark: S2'de metin kimliği `kanal-ad`; burada `kanal-yazi` |

## 3. Renk ve tema (hf_tema.py ile)

Kaynak renkler koyu temadır; `P/ortak/hf_tema.py` açık temaya çevirir. Kural:
- yazı/çizgi mürekkep: `R["murekkep"]` (`#f3efe6`); ince detay: `R["ikincil"]` (`#c9c2b3`).
- sarı hap: `rect fill=R["vurgu"]` (`#f2a93b` → `--vurguDolgu`, açıkta `#ffe066`); hap üstündeki yazı `text fill=R["zemin"]` (`#1b1a17` → `--pilMetin`).
- hap içindeki `≠`: `stroke=R["zemin"]` + v1'deki `<style id="esitdegil-stil">#root #esitdegil path{stroke:var(--pilMetin)}</style>` aynen.
- `id="rz1"` YASAK (hf_tema yazısını zemine boyar); rozet grubu `rz0`.
- Tek sarı öğe: başlıktaki `≠ PLAN` hapı + künyedeki rozet hapı (künye standart parçası). Kartta ve `Kaydet` satırında sarı YOK.
- Kırmızı, yeşil, gradyan, gölge, emoji YOK.
- CSS'e ekle: `#sahne text{font-kerning:none;}` (fontTools genişlik ölçümü kerning'siz; yerleşim ölçümle birebir olsun).

## 4. Yerleşim (1080×1920; bütün sayılar px)

| Bant (y) | Öğe | Kimlik | Değer |
|---|---|---|---|
| 0–280 | boş | — | yalnız zemin; hiçbir öğe yok |
| 291–339 | kanal katmanı | `<g id="kunye"><g id="kanal">` | §5 |
| 386–434 | künye | `#kunye` içinde `#ku-konu`, `#rz0` | §5 |
| 460–550 | üst satır | `#ust` | `İkisi geleceği anlatıyor` Lexend 500 64, mürekkep, x 60, taban 530 (İ noktası üstü 472, ğ/y kuyruğu 545). Genişlik 728 → sağ kenar 788 |
| 570–830 | başlık | `#bas` (`#bas1`, `#bas2`) | §6 |
| 850–1040 | kural özeti kartı | `#kart` | §7 |
| 1050–1140 | kaydet satırı | `#kaydet` | §7.4 |
| 1150–1380 | bağ çıkartması yeri | — | yalnız zemin: boş kutu, çerçeve, ok, "buraya" yazısı ÇİZME |
| 1400–1920 | boş | — | altyazı YOK; yalnız zemin |

Yatay: içerik x 60–960; sağ şerit x 960–1080'e hiçbir öğe girmez. Sol hizalı kolon (ortalama yok).

## 5. Kanal katmanı + künye (S1/S2 kısalarıyla aynı piksel)

- `HUD = {"logoYuk": 48, "logoY": 291, "kanalX": 263, "kanalTaban": 330, "kanalYazi": 42, "konuX": 60, "konuTaban": 420,
  "konuUst": 34, "konuAlt": 28, "rozetY": 386, "rozetH": 48, "rozetAra": 20, "rozetYazi": 26, "rozetDolgu": 20, "sagSinir": 960}`.
- Logo: `<image id="logoimg" href="assets/logo.svg" x="{lx:.2f}" y="291" width="{lw:.2f}" height="48"/>`;
  `lw = 48 * Y.LOGO_EN_BOY` (= 193,49), `lx = 60 - lw * Y.LOGO_KAYMA` (= 53,15). Kimlik `logoimg` ZORUNLU (hf_tema canlı önizleme logoyu bununla değiştirir).
- Yazı: `<text id="kanal-yazi" x="263" y="330" font-family="Lexend" font-weight="700" font-size="42" fill=R["murekkep"]>@ydspublishing</text>`.
- `<g id="kanal">` = logo + yazı; `#kunye` grubunun İÇİNDE (çakışma aracı `#kunye` altını `kunye` türü sayar; ad `kunye:kanal:image0`, `kunye:kanal:text0`).
  Tween, opacity, transform YOK (durağan kare; opaklık 1).
- Konu: `KONU = "Simple Present vs Present Continuous"`, `konu_boyu()` 34'ten 28'e iner: `60 + genislik(Fredoka 700, KONU, boy) + 20 +
  (genislik(Lexend 700, ROZET, 26) + 40) <= 960` sağlanan ilk boy (beklenen 34). `<text id="ku-konu" x="60" y="420" ... style="font-kerning:none">`, mürekkep.
- Rozet: `ROZET = "YDT · BASIC"`; `x = 60 + genislik(KONU) + 20`, `w = genislik(Lexend 700, ROZET, 26) + 40`;
  `<g id="rz0"><rect x y="386" width height="48" rx="24" fill=R["vurgu"]/><text x="{x+w/2}" y="419" text-anchor="middle" Lexend 700 26 fill=R["zemin"]>`.
- Çip YOK. v1 HUD öğeleri (üst logo 48–144, 2 satır ders adı, `Full lesson`) YOK.

## 6. Başlık `TARİFE` / `≠ PLAN` (bant 570–830, sol hizalı x 60)

v1 `hesapla_s_ve_bas()` + `bas_svg()` yeniden düzenlenir; hap iç oranları aynı.
1. `w1 = genislik(Fredoka 700, "TARİFE", 100)/100` (3,41); `wh = 0.36 + 0.50 + 0.24 + genislik("PLAN",100)/100 + 0.36` (4,005).
2. `S = min(120, floor(900 / max(w1, wh)))` (beklenen 120).
3. Döngü (S ≥ 64 iken): `taban1 = 570 + ceil(0.921 * S) + 2` (İ noktası `yMax` 0,921 em; üst ≥ 570) ·
   `hh = 1.02 * S`, `hy = 828 - hh` (hap alt kenarı 828), `taban2 = hy + 0.86 * S` ·
   şart `hy - (taban1 + 0.01 * S) >= 12` (TARİFE ile hap arası); sağlanmazsa `S -= 1`. `assert S >= 64`.
   Beklenen S 120: taban1 683, hy 705,6, taban2 808,8.
4. `#bas1`: `TARİFE` Fredoka 700 S, mürekkep, x 60, y taban1 (`İ` Türkçe noktalı büyük harf; `text-transform` yok).
5. `#bas2`: hap `rect x=60 y=hy width=wh*S height=hh rx=hh/2 fill=R["vurgu"]`; `≠` v1 `esitdegil` grubu aynen (`cx = 60 + 0.36S + 0.25S`,
   iki yatay çizgi `taban2 - 0.47S` ve `taban2 - 0.23S`, yarı genişlik 0,25S; eğik çizgi `(cx - 0.14S, taban2 - 0.02S)` →
   `(cx + 0.14S, taban2 - 0.68S)`; `stroke-width 0.12S`, `stroke-linecap round`, `stroke=R["zemin"]`);
   `PLAN` metni x `60 + 1.10S`, y taban2, Fredoka 700 S, `fill=R["zemin"]`.
6. `≠` (U+2260) karakteri HTML'de YOK (fontta glif yok); yalnız çizgi.

## 7. Kural özeti kartı (bant 850–1040) + Kaydet

### 7.1 Kart çerçevesi
`<rect id="kart-crv" x="62" y="852" width="896" height="186" rx="28" fill="none" stroke=R["murekkep"] stroke-width="4"/>`
(dış kenar 60–960 × 850–1040). İç kullanılabilir alan x 86–934 (24 iç boşluk).

### 7.2 İki satır (Fredoka 700 72, mürekkep, `xml:space="preserve"`; vurgu YOK, altçizgi YOK)
Sahne 08 ile aynı tek cümle: satır 1 `Tarife → leaves,` · satır 2 `plan → am going.`
- Metin kolonu sol x `TX = 242`. Taban: satır 1 `922`, satır 2 `1004` (Fredoka `l` üstü 0,73 em, `g` kuyruğu 0,22 em → iç boşluk üstte ≈ 15, altta ≈ 16).
- Her satır üç parça: sol sözcük (`Tarife` / `plan`) → kalem oku → sağ sözcük (`leaves,` / `am going.`).
  `x_ok0 = TX + genislik(sol, 72) + 0.22*72`, `x_ok1 = x_ok0 + 0.70*72`, sağ sözcük x `x_ok1 + 0.22*72`.
- Ok (U+2192 fontta yok → çizgi): `<path class="ok">` gövde `M x_ok0 y_ok L x_ok1 y_ok`, uç `M x_ok1-dx y_ok-dy L x_ok1 y_ok L x_ok1-dx y_ok+dy`;
  `y_ok = taban - 0.28*72`, `dx = 18*cos(0.5)`, `dy = 18*sin(0.5)`; `stroke=R["murekkep"]`, `stroke-width 6`, `fill none`, `linecap/linejoin round`.
  `→` karakteri HTML'de YOK.
- Kimlikler: `#kart-s1-sol`, `#kart-s1-ok`, `#kart-s1-sag`, `#kart-s2-sol`, `#kart-s2-ok`, `#kart-s2-sag`.

### 7.3 İkonlar (solda tren, sağda bilet; ikon kendi satırının hizasında)
- Tren (satır 1, solda): `ikon_yollari(TREN, mx=154, my=922-0.30*72, en=136, boy=64)` (kutu ≈ 136×47, x 86–222).
  Renk v1 `kart1_svg` kalıbı: son parça (ray) ikincil 3; `ince` parçalar mürekkep 3; diğerleri mürekkep 4. `<g id="kart-tren" fill="none" stroke-linecap="round" stroke-linejoin="round">`.
  Saat ikonu YOK.
- Bilet (satır 2, sağda): `ikon_yollari(BILET, mx=934-66, my=1004-0.30*72, en=132, boy=60)`; `<g id="kart-bilet" transform="rotate(-3 mx my)" ...>`;
  kenar mürekkep 4, `ince` parçalar ikincil 3 (v1 `kart2_svg` kalıbı). Döndürülmüş kutu x 934'ü geçmez (assert).
- Satır 2 metninin sağ ucu (≈ 774) ile bilet sol ucu arası ≥ 16; tren sağ ucu (≈ 222) ile `TX` arası ≥ 16.

### 7.4 Kaydet satırı (bant 1050–1140, x 60'tan)
- Yer imi simgesi (SVG yol, emoji DEĞİL): `<path id="kaydet-imi" d="M63 1062 Q63 1058 67 1058 H107 Q111 1058 111 1062 V1128 L87 1110 L63 1128 Z"
  fill="none" stroke=R["murekkep"] stroke-width="5" stroke-linejoin="round"/>` (dış kenar ≈ 60,5–113,5 × 1055,5–1131). Sarı dolgu YOK.
- Yazı: `<text id="kaydet-yazi" x="135" y="1110" font-family="Fredoka" font-weight="700" font-size="64" fill=R["murekkep"]>Kaydet</text>`
  (genişlik 208 → sağ 343; `K` üstü 1065, `y` kuyruğu 1125).
- `<g id="kaydet">` = simge + yazı.

## 8. Blok kutuları, nesneler.json ve iç kurallar (`kurallari_dogrula`, assert)

Bloklar (sıra aynı; nesneler.json bu listeden yuvarlanarak yazılır, alanlar `ad,x,y,w,h`):
`kanal` {60, 291, (263 + genislik(Lexend 700 "@ydspublishing", 42)) − 60, 48} · `kunye` {60, 386, rozet sağ − 60, 48} ·
`ust` {60, 530 − 0.901·64, genişlik, (0.901 + 0.23)·64} · `bas` {60, taban1 − 0.921·S, max(TARİFE genişliği, wh·S), 828 − üst} ·
`kart` {60, 850, 900, 190} · `kaydet` {60.5, 1055.5, 343 − 60.5, 75.5}.

Kurallar:
1. Her blok: `x >= 60 - 1e-4`, `x + w <= 960 + 1e-4`, `y >= 280`, `y + h <= 1140 + 1e-4` (1150–1920'de öğe yok).
2. Bant içi: kanal ⊂ [280, 350] · kunye ⊂ [360, 450] · ust ⊂ [460, 550] · bas ⊂ [570, 830] · kart ⊂ [850, 1040] · kaydet ⊂ [1050, 1140].
3. Blok kutuları kesişmez (alan 0); dikey komşu boşluğu ≥ 10.
4. İçerik yazı boyu ≥ 64: ust 64, S ≥ 64, kart 72, kaydet 64. Künye 28–34 ve kanal 42 standart ölçüsü (muaf).
5. Ekran satırları ≤ 24 karakter: `@ydspublishing`, `Simple Present vs Present Continuous` (künye satırı; standart ölçüsü, 36 karakter — bu satır muaf, listeye `muaf` notuyla yazılır), `YDT · BASIC`,
   `İkisi geleceği anlatıyor`, `TARİFE`, `≠ PLAN`, `Tarife → leaves,`, `plan → am going.`, `Kaydet`.
6. Kart içi: tren x ∈ [86, TX − 16]; satır 1/2 sağ uç ≤ bilet sol − 16; bilet döndürülmüş kutusu x ≤ 934, y ∈ [856, 1036]; tren y ∈ [856, 1036];
   satır metinleri sağ uç ≤ 934; ok gövdesi sol sözcükten ≥ 10, sağ sözcükten ≥ 10 uzak.
7. Üretilen HTML'de şu dizgiler YOK (büyük/küçük harf duyarsız): `tam ders`, `dakika`, `Full lesson`, `profildeki`,
   `font-family="Caveat"` (font-face tanımı serbest), `≠`, `→`, `id="altyazi"`, `id="rz1"`. Emoji yok: HTML'de U+1F000 üstü karakter yok.

## 9. HTML kabuğu

v1 `uret()` kabuğu aynen; `<style>` içine `#sahne text{font-kerning:none;}` eklenir. SVG sırası: `esitdegil-stil`, `kunye` (kanal + konu + rozet),
`ust`, `bas`, `kart`, `kaydet`. Zaman çizelgesi: iki `tl.set("#sahne", {opacity:1})` (0 ve `Z['sure']`). `data-duration` = `Z['sure']`.

## 10. Kabul ölçütü

1. `/usr/bin/python3 D/uret.py` (calistir.sh ile aynı çağrı) hatasız biter; `index.html yazıldı N` ve `S=120` basar; nesneler.json 6 blok.
2. §8 kuralları assert ile koşar (hepsi geçer).
3. Python tür ipuçları var; v1 dosya düzeni (4 boşluk girinti) korunur.
4. HTML'de `#kanal` içinde tam 1 `image` (`#logoimg`) + 1 `text` (`@ydspublishing`); `#kunye` içinde konu + rozet; altyazı öğesi yok.
5. Şef `calistir.sh --tema acik|koyu` ile tek kare çeker ve PNG'ye bakar (agy render/snapshot KOŞMAZ).
