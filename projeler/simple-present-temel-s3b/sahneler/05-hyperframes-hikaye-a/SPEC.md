# SPEC — sahne 05 hikâye karesi A, huni v2 (simple-present-temel-s3) · 15.11.2026

MAKİNE: Linux x86_64 (srv21). Python `/usr/bin/python3` (fontTools kurulu). Şef yazdı; kodu agy yazar.

| Ne | Değer |
|---|---|
| Yazılacak dosya | `/home/sef/01dev/_worktrees/kalem-0204/projeler/simple-present-temel-s3/sahneler/05-hyperframes-hikaye-a/uret.py` (yeni) |
| Kalıp kaynağı (salt okunur) | `/home/sef/01dev/_worktrees/kalem-0204/projeler/02-04-ydt-temel-s1/sahneler/04-hyperframes-hikaye/uret.py` |
| Yardımcı (HAZIR, değiştirme) | `.../simple-present-temel-s3/sahneler/05-hyperframes-hikaye-a/yardim.py` (`Y.kunye_svg()`, `Y.genislik`, `Y.RENK`, `Y.rozet_konumlari`, `Y.font_css`, `Y.ZEMIN_CSS`, `Y.zemin_html`, `Y.font_kopyala`, `Y.W`, `Y.H`) |
| Bağlayıcı | `/home/sef/01dev/dijital-anlatim/.claude/docs/huni-v2-standart.md` §1, §2, §6 · `.../simple-present-temel-s3/BRIEF-S3.md` "Hikâye kareleri" |
| Çıktı (uret.py yazar) | `proje/index.html`, `nesneler.json` (sahne dizininde) |

Kare: 1080×1920, durağan, ses yok, altyazı yok, çip yok, hitap yok (tek istisna `Kaydet`). Zaman çizelgesi 1,0 sn,
yakalama 0,5 sn (`zamanlar.json` hazır, değişmez).

## 1. Kalıp kaynağından aynen alınacaklar

- Dosya başı (`from __future__ import annotations`, `AD`, `sys.path.insert`, `import yardim as Y`, `PAKET = AD.parent.parent`).
- `zaman.json` + `zamanlar.json` okuma ve 6 assert (kaynak satır 18–28) aynen; `R = Y.RENK` ve anahtar assert'i
  (`zemin`, `murekkep`, `ikincil`, `vurgu`, `kirmizi`).
- `kesisim()`, `kurallari_dogrula()` yapısı, HTML iskeleti (kaynak satır 285–313: `font_css`, `ZEMIN_CSS`, `#root`
  `data-duration` = `Z['sure']`, `zemin_html()`, `<svg id="sahne">`, GSAP iki `tl.set`, `window.__timelines["main"]`),
  `__main__` (font kopyası, `index.html`, `nesneler.json` tam sayı, `print(f"index.html yazıldı {len(html)}")`).
- Kaynaktaki `ek`, `kart_svg`, `ozet`, `BAVUL`, `hesapla_s_ve_ek` ALINMAZ (içerik farklı).
- Tür ipucu zorunlu, girinti 4 boşluk, satır ≤ 130 karakter. Dosyaya yasak söz listesi YAZMA (dış grep kapısı tarar).

## 2. Ekran metni (sırayla) ve renk

| Kimlik | Metin | Yazı | Renk (`R[...]`) |
|---|---|---|---|
| `etiket` | `Sınav tuzağı` | Caveat 700 64 | `ikincil` |
| `kart1` / `kart2` | `Does varsa` / `fiil yalın.` | Fredoka 700 88 | `murekkep` |
| `yanlis-yazi` | `He doesn't go` + tspan `yanlis-es` `es` + `.` | Fredoka 700 56 | `ikincil` (soluk; `es` de `ikincil`) |
| `dogru1-yazi` | `He doesn't go.` | Fredoka 700 64 | `murekkep` |
| `dogru2-yazi` | `Does she go?` | Fredoka 700 64 | `murekkep` |
| `kaydet-yazi` | `Kaydet` | Lexend 700 52 | `zemin` (hf_tema açıkta `pilMetin` yapar) |

Kesme işareti ASCII `'`. Bütün `<text>` öğelerine `style="font-kerning:none"` (genişlik ölçümüyle aynı konum).
Kırmızı (`R["kirmizi"]`) YALNIZ `✗` ve `es` üstü çizgisinde. Sarı (`R["vurgu"]`) YALNIZ `kaydet-hap` (+ künye rozeti).
Yeşil yok. `✗` ve `✓` karakter olarak YAZILMAZ; SVG `<path>`.

## 3. Yerleşim (px, mutlak; sol ikon sütunu x 60–112, yazı sütunu x 132)

| Blok | Bant (istem) | Öğeler |
|---|---|---|
| kanal, künye | 291–339, 386–434 | `Y.kunye_svg()` (dokunma) |
| etiket | 470–550 | `<text id="etiket" x="60" y="526">` |
| kart | 560–760 | `<g id="kart">`: `<rect id="kart-zemin" x=60 y=560 w=900 h=200 rx=30 fill=R["murekkep"] fill-opacity="0.06">` · `<rect id="kart-cerceve" x=62 y=562 w=896 h=196 rx=28 fill="none" stroke=R["murekkep"] stroke-width=4 stroke-linecap/linejoin round>` (çizgi merkezde: dış kenar 60–960) · `kart1` x 510 taban 639, `kart2` x 510 taban 723 (QA 1: 642/726'dan 3 px yukarı), ikisi `text-anchor="middle"` |
| yanlis | 780–860 | `<g id="yanlis">`: `✗` = `<path id="yanlis-carpi" d="M64 799 Q85 819 107 842 M107 798 Q87 821 65 841" fill="none" stroke=R["kirmizi"] stroke-width=7 stroke-linecap="round">` · yazı x 132 taban 840 · üstü çizgi (aşağıda) |
| dogru1 | 870–950 | `<g id="dogru1">`: `✓` = `<path id="dogru1-tik" d="M64 909 L79 927 Q90 905 108 888" fill="none" stroke=R["murekkep"] stroke-width=7 linecap/linejoin round>` · yazı x 132 taban 932 |
| dogru2 | 960–1040 | `<g id="dogru2">`: `<path id="dogru2-tik">` = dogru1 yolu y + 90 (`M64 999 L79 1017 Q90 995 108 978`) · yazı x 132 taban 1022 |
| kaydet | 1060–1140 | `<g id="kaydet">` (aşağıda) |
| boş zemin | 1150–1920 | hiçbir öğe yok (bağ çıkartması elle konur; kutu, çerçeve, yer tutucu ÇİZME) |

### 3.1 `es` üstü çizgisi (`go` + çizili `es`)
`x_es = 132 + Y.genislik("Fredoka", 700, "He doesn't go", 56)`, `w_es = Y.genislik("Fredoka", 700, "es", 56)`.
`<path id="yanlis-cizik" d="M{x_es+1:.1f} 827 L{x_es+w_es-1:.1f} 821"` (QA 1: ±4 uçları `o`ya ve noktaya değiyordu) fill="none" stroke=R["kirmizi"] stroke-width=6
stroke-linecap="round">` (taban 840 − 13 / − 19; sahne 02 oranı). Çizgi yazıdan SONRA (üstte) gelir.

### 3.2 Kaydet
- Yer imi: `<g transform="translate(39 1052) scale(4)" fill="none" stroke=R["murekkep"] stroke-width="1.5"
  stroke-linejoin="round" stroke-linecap="round"><path id="kaydet-imi" d="M18 7v14l-6 -4l-6 4v-14a4 4 0 0 1 4 -4h4a4 4 0 0 1 4 4z"/></g>`
  (görünür kutu x 60–114, y 1061–1139; emoji yok).
- Hap: `hap_w = Y.genislik("Lexend", 700, "Kaydet", 52) + 56`; `<rect id="kaydet-hap" x=132 y=1060 width=hap_w height=80 rx=40 fill=R["vurgu"]>`.
- Yazı: `<text id="kaydet-yazi" x={132 + hap_w/2} y=1118 text-anchor="middle">` Lexend 700 52, `R["zemin"]`.

### 3.3 SVG sırası
`Y.kunye_svg()` → `etiket` → `kart` → `yanlis` → `dogru1` → `dogru2` → `kaydet`. Animasyon yok; timeline yalnız `#sahne` opaklık 1.

## 4. Blok kutuları (`blok_kutulari`, `nesneler.json`; yazı kutusu = taban − 0,75·boy … taban + 0,25·boy)

| ad | x | y | w | h |
|---|---|---|---|---|
| kanal | 53,2 | 291 | 263 + genişlik(Lexend 700 `@ydspublishing` 42) − 53,2 | 48 |
| kunye | 60 | 386 | `rz_x + rz_w − 60` (`Y.rozet_konumlari()[0]`) | 48 |
| etiket | 60 | 526 − 48 = 478 | genişlik(Caveat 700 `Sınav tuzağı` 64) | 64 |
| kart | 60 | 560 | 900 | 200 |
| yanlis | 60 | 794 (✗ üstü, çizgi payı dahil) | 132 + genişlik(Fredoka 700 `He doesn't goes.` 56) − 60 | 854 − 794 = 60 |
| dogru1 | 60 | 884 | 132 + genişlik(Fredoka 700 `He doesn't go.` 64) − 60 | 64 |
| dogru2 | 60 | 974 | 132 + genişlik(Fredoka 700 `Does she go?` 64) − 60 | 64 |
| kaydet | 60 | 1060 | 132 + hap_w − 60 | 80 |

## 5. Kurallar (`kurallari_dogrula`, assert)

1. İçerik blokları (etiket, kart, yanlis, dogru1, dogru2, kaydet): x ≥ 60, x + w ≤ 960, y ≥ 460, y + h ≤ 1140.
2. Her içerik bloğu kendi istem bandında (§3 tablo "Bant"): `bant_bas ≤ y` ve `y + h ≤ bant_son`.
3. kanal ve kunye: y ≥ 280, y + h ≤ 450.
4. Bütün blok çiftlerinin kesişim alanı 0; ardışık bloklar arası dikey boşluk ≥ 16 (kunye → etiket → kart → yanlis → dogru1 → dogru2 → kaydet).
5. Kart içi: `max(genişlik(kart1), genişlik(kart2)) ≤ 900 − 2·56`; `639 − 0,75·88 ≥ 560 + 12`; `723 + 0,25·88 ≤ 760 − 8`.
6. Yazı boyları (sabitler): etiket 64, kart 88, yanlış 56, doğru 64, hap 52; hepsi ≥ 50 (ikincil/etiket tabanı), doğru ve kart ≥ 64.
7. Ekran satırı ≤ 24 karakter: `Sınav tuzağı`, `Does varsa`, `fiil yalın.`, `He doesn't goes.`, `He doesn't go.`, `Does she go?`, `Kaydet`.
8. Renk: `html.count(R["kirmizi"]) == 2` ve ikisi de `yanlis` grubunun SVG dizesinde; `html.count(R["vurgu"]) == 2`
   (künye rozeti + `kaydet-hap`); `"#167a4a"` yok; `"✗"` ve `"✓"` karakteri html'de yok.
9. HTML'de `id="kanal"` ve `id="logoimg"` tam 1 kez.
10. Var: `id="etiket"`, `kart-cerceve`, `kart1`, `kart2`, `yanlis-carpi`, `yanlis-es`, `yanlis-cizik`, `dogru1-tik`, `dogru2-tik`,
    `dogru1-yazi`, `dogru2-yazi`, `kaydet-imi`, `kaydet-hap`, `kaydet-yazi`. Yok: `ku-cip`, `cg1`, `ek-yor`, `ozet`.

## 6. Olay listesi (tek kare)

| Olay | Kare / sn | Cümle sözcüğü |
|---|---|---|
| bütün öğeler görünür (kanal, künye, etiket, kart, yanlış, 2 doğru, kaydet) | kare 0 (yakalama 0,5; çizelge 1,0) | — (anlatım yok; `olay.py` boş liste yazar) |

## 7. Kabul ölçütü

- `/usr/bin/python3 uret.py` rc 0; çıktı `index.html yazıldı <n>`.
- `nesneler.json` 8 blok (kanal, kunye, etiket, kart, yanlis, dogru1, dogru2, kaydet), tam sayı.
- Test, render, git YOK (şef koşar). Başka dosyaya dokunma.
