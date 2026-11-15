# SPEC — 02-04-ydt-temel-s2 sahne 03 çağrı (huni v2) · HyperFrames DİKEY 1080×1920 · 15.11.2026

Sahne dizini (S): `/home/sef/01dev/_worktrees/kalem-0204/projeler/02-04-ydt-temel-s2/sahneler/03-hyperframes-cta/`
Bağlayıcı: `/home/sef/01dev/dijital-anlatim/.claude/docs/huni-v2-standart.md` §1–§3 · paket `../../BRIEF-S2.md` "Yerleşim" ve 22,75–29,41 satırları.
v1 kalıp kaynağı (yedek, salt oku): `/home/sef/Silinecekler/2026-11-15-huni-v2/02-04-ydt-temel-s2/sahneler/03-hyperframes-cta/`
(`uret.py`, `yardim.py`). Şu an S içindeki `uret.py` ve `yardim.py` v1 ile aynıdır.

## 0. İş bölümü (iki ayrı ajan, sahiplik ayrık)

| Ajan | Yazacağı tek dosya | Bölüm |
|---|---|---|
| A | `S/yardim.py` | §2 |
| B | `S/uret.py` | §3–§6 |

Kurallar (ikisi için): yalnız kendi dosyanı yaz. Başka dosyaya dokunma. Silme yok. Test, render, git yok.
Python 3, tür ipucu zorunlu, 4 boşluk girinti (v1 dosyaları gibi), satır ≤ 120. Yeni bağımlılık yok.

## 1. Neden yeniden yazılıyor

v1 içeriği (`üç farktan biri`, `Tam ders:`, ders bandı, saat, `dört buçuk dakikada`, mont/tişört, `Full lesson` çipi) TAMAMEN çıkar.
v1 HUD değerleri (logo y 48, ders adı y 212 iki satır 56 px, rozet y 216, çip y 48) KULLANILMAZ.
Kalan: dosya yapısı, `T()`/`E()` sözcük erişimi + assert, `altyazi_svg` kalıbı, GSAP zaman çizelgesi kalıbı, `window.__timelines["main"]`.

## 2. `yardim.py` (Ajan A) — kanal katmanı + künye

Değişmeyenler (AYNEN kalır): `genislik`, `font_css`, `font_kopyala`, yol verisi işlevleri, `peeps`, `tabler`, `altyazi_satirlari`,
`altyazi_cumleleri`, `altyazi_svg`, `zemin_html`, `ZEMIN_CSS`, `cizgi_zamanlari`, `RENK`, `LOGO_EN_BOY`, `LOGO_KAYMA`, `W`, `H`.

Değişenler:
1. Modül docstring'i: "02-04-ydt-temel-s2 huni v2: kanal katmanı (y 280–350) + künye (y 360–450); değerler BRIEF-S2.md Yerleşim tablosu".
2. `HUD` sözlüğü yeni değerlerle (eski anahtarlar `logoY 48`, `dersTaban`, `dersYazi`, `dersSatir`, `cip*` çıkar):

| Anahtar | Değer | Anlam |
|---|---|---|
| `kenar` | 48 | YALNIZ altyazı genişliği için (W − 2×48 = 984; `ortak/kunye.js` altyaziCiz ile aynı). Başka yerde kullanma |
| `logoYuk` | 48 | logo yüksekliği; genişlik = 48 × `LOGO_EN_BOY` = 193,49 |
| `logoY` | 291 | logo üst kenarı (y 291–339) |
| `kanalX` | 263 | `@ydspublishing` sol x |
| `kanalTaban` | 330 | `@ydspublishing` taban y |
| `kanalYazi` | 42 | Lexend 700 |
| `konuX` | 60 | görünür sol kenar (logo da bu kenara hizalı) |
| `konuTaban` | 420 | konu taban y |
| `konuUst`, `konuAlt` | 34, 28 | konu yazı boyu üst ve alt sınırı |
| `rozetY`, `rozetH` | 386, 48 | rozet hapı y 386–434, rx 24 |
| `rozetAra` | 20 | konu sonu → rozet |
| `rozetYazi` | 26 | Lexend 700 |
| `rozetDolgu` | 20 | rozet yazısının iki yanındaki iç boşluk (her yan) |
| `sagSinir` | 960 | künye sağ sınırı |
| `altyaziBas`, `altyaziYazi`, `altyaziSatir` | 1400, 44, 56 | AYNEN |

3. `DERS` yerine `KONU = "Simple Present vs Present Continuous"`. `ROZETLER = ("YDT · BASIC",)` kalır.
4. Yeni `konu_boyu() -> int`: 34'ten 28'e inerek ilk tam sayı boy; şart `konuX + genislik(Fredoka 700, KONU, boy) + rozetAra + rozet genişliği ≤ sagSinir`.
   Hiçbiri sığmazsa `AssertionError`. (Ölçüm: 34'te son x 868,2 → 34 döner.)
5. `rozet_konumlari() -> list[tuple[float, float]]`: tek rozet; x = `konuX + genislik(Fredoka 700, KONU, konu_boyu()) + rozetAra`,
   genişlik = `genislik(Lexend 700, rozet, 26) + 2 × rozetDolgu`.
6. `cip_olcu` kaldırılır (çip YOK).
7. `kunye_svg() -> str` (parametresiz). Çıktı sırası ve kimlikler aynen:
   - `<g id="kunye">` dış grup. İçinde önce `<g id="kanal">`:
     - `<image id="logoimg" href="assets/logo.svg" x="{lx:.2f}" y="291" width="{lw:.2f}" height="48"/>`;
       `lw = logoYuk × LOGO_EN_BOY`, `lx = konuX − lw × LOGO_KAYMA` (= 53,15; görünür sol kenar 60). Kimlik `logoimg` DEĞİŞMEZ
       (`ortak/hf_tema.py` tema değişiminde logoyu bu kimlikle bulur).
     - `<text id="kanal-ad" x="263" y="330" font-family="Lexend" font-weight="700" font-size="42" fill="#f3efe6">@ydspublishing</text>`
       (`#f3efe6` = koyu mürekkep; `hf_tema.py` açık temada `#1b2440`'a çevirir).
   - Sonra `<text id="ku-konu" x="60" y="420" font-family="Fredoka" font-weight="700" font-size="{konu_boyu()}" fill="#f3efe6">KONU</text>`.
   - Sonra `<g id="rz0">`: `<rect x y="386" width h="48" rx="24" fill="#f2a93b"/>` + `<text x="{x+w/2}" y="419" text-anchor="middle"
     font-family="Lexend" font-weight="700" font-size="26" fill="#1b1a17">YDT · BASIC</text>` (`#f2a93b` rect → `vurguDolgu`,
     `#1b1a17` yazı → `pilMetin`; çeviri `hf_tema.py` CSS'inde).
   - Kanal grubunda `style`, `opacity`, `transform`, sınıf YOK.

## 3. `uret.py` (Ajan B) — veri

- `PAKET`, `SAH` (zaman.json `klasor == AD.name`), `T_BAS = SAH["t_bas"]` (22,75), `KARE = SAH["kare"]` (230), `SURE = round(KARE/30, 4)` (7,6667): v1 gibi.
- `SOZ` = `sozcukler.json` içinde `cumle == 4` olanlar. `T(i, bas)` / `E(i, bas)` v1 ile aynı (t0 / t1, önek assert'i).
- Assert listesi (sıra): `(0,"Bitmedi"), (1,"gel"), (2,"Dersin"), (3,"tamamı"), (4,"YDS"), (5,"Publishing"), (6,"YouTube"), (7,"kanalında")`.
- `ALT` = `altyazi.json` içinde `cumle == 4` olan parçalar (2 parça: 23,30–24,74 · 24,89–28,41). Cümle 3'ün kuyruğu bu sahnede GÖRÜNMEZ.
- v1'deki `CIP`, `MONT`, `TISORT`, `ikon_yollari`, `_kutusu`, `_daire_yolu`, bütün v1 yerleşim sabitleri çıkar.

## 4. Olay listesi (sahne içi sn = küresel − 22,75; kare = round(sn × 30))

| Olay | Sözcük (çapa) | Küresel sn | Sahne içi sn | Kare | Hareket | Ses olayı |
|---|---|---|---|---|---|---|
| kare 0 | — | 22,75 | 0,00 | 0 | kanal katmanı + künye görünür; içerik boş | — |
| bitmedi_giris | `T(0,"Bitmedi")` | 23,30 | 0,55 | 17 | `#tx_bitmedi` kinetik | `tik` 0,4 |
| gel_giris | `T(1,"gel")` | 24,26 | 1,51 | 45 | `#tx_gel` kinetik | `tik` 0,45 |
| kapak_giris | `T(2,"Dersin")` | 24,89 | 2,14 | 64 | `#kapakg` yumuşak giriş 0,4 sn | `vurus` 0,7 |
| hap_giris | `T(4,"YDS")` | 26,17 | 3,42 | 103 | `#hapg` giriş 0,3 sn | `tik` 0,6 |
| youtube_giris | `T(6,"YouTube")` | 27,29 | 4,54 | 136 | `#tx_youtube` kinetik | `tik` 0,4 |
| kuyruk | `E(7,"kanalında")` sonrası | 28,49 | 5,74 → 7,67 | 172 → 230 | durgun; her öğe yerinde | — |

Bütün zamanlar sözcük çapasından hesaplanır (sabit saniye yazma). `zamanlar` sözlüğü anahtarları: `fps`, `kare`, `sure`, `t_bas`,
`bitmedi_giris`, `gel_giris`, `kapak_giris`, `hap_giris`, `youtube_giris` (her biri `[sahne_ici_sn, sure]`; süreler 0,22 · 0,22 · 0,4 · 0,3 · 0,22),
`olaylar` = `[[sahne_ici_sn, tur, guc], …]` (tablodaki 5 satır). `olay.py` bu listeyi okur; her olay karesi 12 ≤ kare < KARE − 12 olmalı.

## 5. Yerleşim ve ekran metni (px, 1080×1920; tek sütun, sol hizalı x 60)

| Öğe | Kimlik | Değer |
|---|---|---|
| Giriş sözü 1 | `tx_bitmedi` | `Bitmedi,` Fredoka 700 96, x 60, taban y 572, `fill="#f3efe6"`, `style="opacity:0"` |
| Giriş sözü 2 | `tx_gel` | `gel.` aynı boy ve taban; x = 60 + genislik(Fredoka 700, "Bitmedi, ", 96) (≈ 432,3) |
| Kapak kartı grubu | `kapakg` | `style="opacity:0"`; kart x 60, y 627, 900×506 (merkez 510, 880) |
| Kapak kırpması | `cpkapak` | `<clipPath id="cpkapak"><rect x="60" y="627" width="900" height="506" rx="24"/></clipPath>` (`<defs>` içinde) |
| Açık kapak | `kapak-acik` | `<image href="assets/ana-kapak.png" x="60" y="627" width="900" height="506" preserveAspectRatio="xMidYMid slice">`, `clip-path="url(#cpkapak)"` taşıyan `<g>` içinde |
| Koyu kapak | `kapak-koyu` | aynı, `href="assets/ana-kapak-koyu.png"` |
| Kart çerçevesi | `kapak-cerceve` | `<rect x="60" y="627" width="900" height="506" rx="24" fill="none" stroke="#f3efe6" stroke-width="3"/>` (kırpma dışında, resimlerin üstünde) |
| Hap grubu | `hapg` | `style="opacity:0"` |
| Hap | `hap` | `<rect x="60" y="1170" width="{hw}" height="80" rx="40" fill="#f2a93b"/>`; hw = genislik(Lexend 700, "@ydspublishing", 64) + 2×20 (≈ 556,4) |
| Hap yazısı | `tx_hap` | `@ydspublishing` Lexend 700 64, x 80, taban y 1232, `fill="#1b1a17"` |
| YouTube satırı | `tx_youtube` | `· YouTube` Lexend 700 64, x = 60 + hw + 14, taban y 1232, `fill="#f3efe6"`, `style="opacity:0"` |
| Altyazı | `altyazi` | `<g id="altyazi">` + `Y.altyazi_svg(T_BAS, SURE, ALT)` (v1 gibi) |
| Künye | — | `Y.kunye_svg()` (parametresiz), altyazıdan önce, içerikten sonra (v1 sırası) |

Ölçü assert'leri (uret.py içinde): YouTube satırının sağ ucu (x + genişlik) ≤ 958; `Bitmedi, gel.` sağ ucu ≤ 960.
Tema CSS'i `<style>` içine (Y.font_css + Y.ZEMIN_CSS'ten sonra):
`#root #kapak-acik{display:none}#root.tema-acik #kapak-acik{display:inline}#root.tema-acik #kapak-koyu{display:none}`.
Kapak resmi yazılarla üst üste binmez: giriş sözü y ≈ 500–592, kart 627–1133, hap 1170–1250, altyazı 1400+.

## 6. Zaman çizelgesi (GSAP, v1 kalıbı)

- `tl = gsap.timeline({paused: true})`; `ac(o)` ile `immediateRender: false`; `window.__timelines["main"] = tl`.
- Altyazı: v1 döngüsü (`V.alt` her parça için `set opacity 1` aç, `set opacity 0` kapat).
- `kinetik(id, bas)`: v1 ile aynı (opacity 0, y 24 → opacity 1, y 0; 0,22 sn; `back.out(1.6)`). `#tx_bitmedi`, `#tx_gel`, `#tx_youtube`.
- Kapak: `gsap.set("#kapakg", {svgOrigin: "510 880"})`; `tl.fromTo("#kapakg", {opacity: 0, scale: 0.96}, {opacity: 1, scale: 1,
  duration: 0.4, ease: "power3.out", immediateRender: false}, Z.kapak_giris[0])`.
- Hap: `svgOrigin` = hap merkezi (60 + hw/2, 1210); `fromTo` opacity 0, scale 0.9 → 1, 1; 0,3 sn; `power3.out`.
- `#kunye`, `#kanal`, `#logoimg`, `#kanal-ad` hiçbir tween'e girmez (opaklık, ölçek, konum yok).
- Çıkış animasyonu yok; son karede her öğe yerinde.
- `<div id="root" data-composition-id="main" data-start="0" data-duration="{SURE}" data-fps="30" data-width="1080" data-height="1920">` v1 gibi.

## 7. Yasaklar (ekranda)

`Tam ders`, süre sözü (`dakika`, `dk`), ders bandı, saat ikonu, oynat üçgeni, "izle" düğmesi taklidi, YouTube logosu, QR, emoji, kırmızı,
içerikte "kanal" sözü (altyazı konuşmayı yazar; o hariç), çip. Sarı (vurgu) yalnız hap; rozet künye öğesidir.
Dosyada `tam ders` ya da `dakika` dizgisi geçmez (yorumlarda da).

## 8. Kabul ölçütü

1. `cd S && /usr/bin/python3 uret.py` hatasız biter; `proje/index.html` + `zamanlar.json` yazar (şef koşar).
2. `index.html` içinde: `id="kanal"`, `id="logoimg"`, `id="kapak-acik"`, `id="kapak-koyu"`, `id="cpkapak"`, `id="altyazi"`; `ku-cip` YOK.
3. `zamanlar.json` `olaylar` 5 satır, kareleri 17 · 45 · 64 · 103 · 136.
4. Kare 0'da yalnız kanal katmanı + künye; son karede kapak kartı + giriş sözü + hap satırı görünür.
5. `grep -niE "tam ders|dakika"` iki dosyada boş.
