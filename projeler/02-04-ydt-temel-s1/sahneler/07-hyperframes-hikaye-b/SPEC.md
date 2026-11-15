# SPEC — sahne 07 hikâye karesi B, huni v2 (02-04-ydt-temel-s1) · 15.11.2026

MAKİNE: Linux x86_64 (srv21). Python `/usr/bin/python3` (fontTools kurulu). Şef yazdı (istem D-V2); kodu agy yazar.

| Ne | Değer |
|---|---|
| Yazılacak dosya | `/home/sef/01dev/_worktrees/kalem-0204/projeler/02-04-ydt-temel-s1/sahneler/07-hyperframes-hikaye-b/uret.py` (baştan yaz) |
| En yakın kalıp (v2, salt okunur) | `/home/sef/01dev/_worktrees/kalem-0204/projeler/02-04-ydt-temel-s1/sahneler/04-hyperframes-hikaye/uret.py` (hikâye A, kapıdan geçti) |
| Eski sürüm (v1, salt okunur) | `/home/sef/Silinecekler/2026-11-15-huni-v2/02-04-ydt-temel-s1/sahneler/07-hyperframes-hikaye-b/v1/uret.py` |
| Yardımcı (HAZIR, değiştirme) | `.../sahneler/07-hyperframes-hikaye-b/yardim.py` (v2; sahne 04 ile aynı dosya: `Y.kunye_svg()`, `Y.rozet_konumlari()`, `Y.genislik`, `Y.RENK`, `Y.font_css`, `Y.ZEMIN_CSS`, `Y.zemin_html`, `Y.font_kopyala`) |
| Bağlayıcı standart | `/home/sef/01dev/dijital-anlatim/.claude/docs/huni-v2-standart.md` §1, §2, §6 |
| Çıktı (uret.py yazar) | `proje/index.html`, `nesneler.json` (sahne dizininde) |

Kare: 1080×1920, durağan, ses yok, altyazı yok, çip yok. Zaman çizelgesi 1,0 sn (yakalama 0,5 sn; `zamanlar.json` değişmez).
Düzen B = soru–cevap (A kural kartıydı): Türkçe cümle → iki şık yan yana (sol: doğru şık kartı, yeşil + tik; sağ: soluk şık)
→ şıkların altında bağlam etiketi → kural özeti → `Kaydet`.

**DUZ-1 (15.11, bağımsız inceleme):** `I live with my uncle.` dilbilgisi olarak doğru bir cümle; üstü çizili hâli "bu cümle hatalı"
okunuyordu. Yanlış olan cümle değil, `şimdilik` (geçici) bağlamına uymaması. Üstü çizgi kalktı; iki şık yan yana durur, doğru şıkta
tik, öteki soluk; altlarında küçük etiket: doğru şık `şimdilik → geçici`, soluk şık `kalıcıysa`. §3.2, §3.3, §3.3a, §3.6, §4, §5, §6
bu düzeltmeye göre yazıldı. Önceki (çizgili) sürüm: `~/Silinecekler/2026-11-15-huni-v2/02-04-ydt-temel-s1/sahneler/07-hyperframes-hikaye-b/v2-cizgili/`.

## 1. Sahne 04'ten (v2) aynen alınacak kalıplar

- Dosya başı: `from __future__ import annotations`, `AD`, `sys.path.insert`, `import yardim as Y`, `PAKET`.
- `zamanlar.json` okuma + 3 assert (sure 1,0 · kare 1 · fps 30) aynen.
- `zaman.json` doğrulaması v1 dosyasındaki gibi (v1 satır 18–24): `duragan` listesinde `klasor == AD.name` olan TEK kayıt;
  `kare == 1`, `cikti == "hikaye-b.png"`; `sahneler[]` içinde `AD.name` yok. (`hikaye` alanı sahne 04'ündür, okuma.)
- `kaydet_svg()` yapısı (yer imi yolu, hap, yazı) — yalnız y değerleri §3.5'e göre değişir.
- `kesisim()`, `kurallari_dogrula()` assert yapısı, HTML iskeleti (04 satır 285–313: `font_css`, `ZEMIN_CSS`, `#sahne` kuralı,
  `#root` `data-duration` = `Z['sure']`, `zemin_html()`, `<svg id="sahne">`, GSAP iki `tl.set`, `window.__timelines["main"]`),
  `__main__` (font kopyası, `index.html`, `nesneler.json` tam sayıya yuvarlanmış, `print(f"index.html yazıldı {len(html)}")`).
- Künye ve kanal katmanı yalnız `Y.kunye_svg()` çağrısından gelir. uret.py içinde künye/logo kodu YOK.
- Tür ipucu bütün işlevlerde; girinti 4 boşluk (dosyanın var olan stili); satır ≤ 120 karakter.
- Her `<text>`'e `xml:space="preserve"`.

## 2. Kaldırılan v1 öğeleri

v1 `kunye_svg()` (logo y 48, 2 satır ders adı, rozet, `Quiz` çipi), `soru` hapı (`Hangisi doğru?`), `kA`/`kB` seçenek kartları
(harf daireleri), `cg1`, `cg2` (eski çağrı satırları), alt `@ydspublishing` hapı (`hap`). Bu metinler kodda literal olarak da geçmez.

## 3. Yerleşim (px, mutlak; y = yazı tabanı)

```
y   0 ─ 280  boş zemin
  291 ─ 339  kanal: logo + @ydspublishing          (Y.kunye_svg)
  386 ─ 434  künye: konu + YDT · BASIC             (Y.kunye_svg)
  538 / 622  Şimdilik amcamla / yaşıyorum.         Fredoka 700 76
  664 ─ 864  [ I am living with ]   I live with       sol: yeşil çerçeve + tik, Fredoka 700 72 (x 60–628)
  742 / 822  [ my uncle.      ✓ ]   my uncle.         sağ: soluk (0,45), Fredoka 700 64, x 656; üstü çizgi YOK
  914          şimdilik → geçici      kalıcıysa       etiketler: Caveat 700 48; sol yeşil, sağ gri (R["ikincil"])
 1035 / 1117 Kalıcıysa geniş zaman, / geçiciyse şimdiki zaman.  Fredoka 700 68
 1150 ─ 1380 BOŞ ZEMİN (bağ çıkartması elle konur; kutu, çerçeve, çizgi ÇİZME)
 1416 ─ 1504 [yer imi] (Kaydet)                     sarı hap
 1570 ─ 1920 boş zemin
```

Sabitler: `YESIL = "#167a4a"` (doğru şık; açık tema değeri) · `YESIL_KOYU = "#4fbf85"` (koyu tema değeri, yalnız CSS).
Diğer renkler yalnız `Y.RENK["zemin"|"murekkep"|"ikincil"|"vurgu"]`. Kırmızı (`Y.RENK["kirmizi"]`) KULLANMA.

### 3.1 Türkçe cümle (`<g id="tr">`)
- `<text id="tr1" x="60" y="538">Şimdilik amcamla</text>` · `<text id="tr2" x="60" y="622">yaşıyorum.</text>`
- Fredoka 700, 76, `fill` R["murekkep"].

### 3.2 Doğru şık kartı (`<g id="dogru">`)
- Satırlar (DUZ-1): `DOGRU_SATIR = ("I am living with", "my uncle.")`; satır ≤ 24 kuralı tek satırı yasaklar, kart yarım genişlikte.
- `KART_SAG = int(100 + max(genişlik(Fredoka 700, satır, 72)) + 40) + 1` (= 628). Çerçeve: `<rect id="dogru-crv" x="63" y="667"
  width={KART_SAG − 66} height="194" rx="28" fill="none" stroke=YESIL stroke-width="6"/>` (dış kenar x 60–628, y 664–864).
- `<text id="dogru-s1" x="100" y="742">I am living with</text>` · `<text id="dogru-s2" x="100" y="822">my uncle.</text>`;
  Fredoka 700, 72, `fill` R["murekkep"].
- Tik: `<g id="dogru-tik" transform="translate({KART_SAG − 120} 756) scale(4)" …><path d="M5 12l5 5l10 -10"/></g>`
  (2. satır hizasında; görünür kutu x 528–588, y 784–824). Emoji YOK.

### 3.3 Öteki şık (`<g id="yanlis">`; kartın sağında, satır tabanları kartla ortak)
- `YANLIS_X = KART_SAG + 28` (= 656). `<text id="yanlis-s1" x="656" y="742" opacity="0.45">I live with</text>` ·
  `<text id="yanlis-s2" x="656" y="822" opacity="0.45">my uncle.</text>`; Fredoka 700, 64, `fill` R["murekkep"].
- Üstü çizgi, çerçeve, tik, çarpı YOK (DUZ-1: cümle dilbilgisi olarak doğru). Kırmızı YOK.

### 3.3a Bağlam etiketleri (DUZ-1; taban y 914, Caveat 700 48, `xml:space="preserve"`)
- Doğru şık altı: `<g id="dogru-etiket" fill=YESIL>` içinde `<text id="dogru-et1" x="100">şimdilik</text>`, ok
  `<path id="dogru-ok" d="M5 12l14 0M13 18l6 -6M13 6l6 6" transform="translate(… …) scale(2)" fill="none" stroke=YESIL stroke-width="2">`
  (Tabler `arrow-right`, MIT; yazı tiplerinde U+2192 yok), `<text id="dogru-et2">geçici</text>`; ok ile yazı arası 18 px.
- Öteki şık altı: `<text id="yanlis-etiket" x="656" fill=R["ikincil"]>kalıcıysa</text>`.

### 3.4 Kural özeti (`<g id="ozet">`)
- `<text id="ozet1" x="60" y="1035">Kalıcıysa geniş zaman,</text>` · `<text id="ozet2" x="60" y="1117">geçiciyse şimdiki zaman.</text>`
- Fredoka 700, 68, `fill` R["murekkep"].

### 3.5 Kaydet (`<g id="kaydet">`; sahne 04 `kaydet_svg()` ile aynı yapı, y +368)
- Yer imi: `<g transform="translate(39 1412) scale(4)" fill="none" stroke=R["murekkep"] stroke-width="1.5" stroke-linejoin="round"
  stroke-linecap="round"><path id="kaydet-imi" d="M18 7v14l-6 -4l-6 4v-14a4 4 0 0 1 4 -4h4a4 4 0 0 1 4 4z"/></g>`
  (görünür kutu x 60–108, y 1424–1496).
- Hap: `hap_w = Y.genislik("Fredoka", 700, "Kaydet", 64) + 80`; `<rect id="kaydet-hap" x="128" y="1416" width=hap_w height="88" rx="44"
  fill=R["vurgu"]/>` (tema dönüştürücüsü açıkta `#ffe066` yapar).
- Yazı: `<text id="kaydet-yazi" x={128 + hap_w/2} y="1482" text-anchor="middle">Kaydet</text>`; Fredoka 700, 64, `fill` R["zemin"]
  (açıkta `pilMetin` `#1b2440`).

### 3.6 Tema (CSS, `<style>` içinde `#sahne{…}` satırının hemen altına iki satır; ikincisi DUZ-1 etiket yazısı için)
```
#root:not(.tema-acik) [stroke="#167a4a"]{stroke:#4fbf85}
#root:not(.tema-acik) [fill="#167a4a"]{fill:#4fbf85}
```
Gerekçe: `ortak/hf_tema.py` yeşili tanımaz; `#167a4a` koyu zeminde sönük kalır. **DİKKAT:** HTML içinde `#root.tema-acik` dizisi
GEÇMEYECEK (hf_tema.py bu diziyi görürse CSS eklemez) — assert et.

### 3.7 SVG sırası
`Y.kunye_svg()` → `tr` → `dogru` → `yanlis` → etiketler → `ozet` → `kaydet`. Animasyon yok; timeline yalnız `#sahne` opaklık 1 (04 ile aynı).

## 4. Blok kutuları (`blok_kutulari`, `nesneler.json`; sıra aynen)

| ad | x | y | w | h |
|---|---|---|---|---|
| kanal | 53,2 | 291 | 263 + genişlik(Lexend 700 `@ydspublishing` 42) − 53,2 | 48 |
| kunye | 60 | 386 | rozet x + rozet w − 60 (`Y.rozet_konumlari()[0]`) | 48 |
| tr | 60 | 538 − 0,75·76 | max(genişlik(Fredoka 700, satır, 76)) iki satır | (622 + 0,25·76) − y |
| dogru | 60 | 664 | KART_SAG − 60 | 200 |
| yanlis | YANLIS_X | 742 − 0,75·64 | max(genişlik(Fredoka 700, satır, 64)) iki satır | (822 + 0,25·64) − y |
| dogru-etiket | 100 | 914 − 0,75·48 | gen(şimdilik) + 2·18 + 28 + gen(geçici) (Caveat 700 48) | 48 |
| yanlis-etiket | YANLIS_X | 914 − 0,75·48 | gen(kalıcıysa) (Caveat 700 48) | 48 |
| ozet | 60 | 1035 − 0,75·68 | max(genişlik(Fredoka 700, satır, 68)) iki satır | (1117 + 0,25·68) − y |
| kaydet | 60 | 1416 | 128 + hap_w − 60 | 88 |

## 5. Kurallar (`kurallari_dogrula(bloklar, html)`, assert)

1. tr, dogru, yanlis, dogru-etiket, yanlis-etiket, ozet: x ≥ 60, x + w ≤ 960, y ≥ 460, y + h ≤ 1140.
2. kaydet: x ≥ 60, x + w ≤ 960, y ≥ 1400, y + h ≤ 1520 (1150–1380 boş kalır, 1570–1920 boş kalır).
3. kanal ve kunye: y ≥ 280, y + h ≤ 450.
4. Bütün blok çiftlerinin kesişim alanı 0.
5. Dikey boşluk ≥ 16: kunye → tr, tr → dogru, dogru-etiket → ozet; dogru → dogru-etiket ≥ 8. Yatay: dogru → yanlis ≥ 16.
   Etiket x = kendi şıkkının x'i.
6. Kart içi: `100 + max(genişlik(Fredoka 700, satır, 72)) ≤ KART_SAG − 24`; `100 + genişlik("my uncle.", 72) ≤ KART_SAG − 124` (tik).
7. Yazı boyları (sabit olarak tanımla, assert ≥ 64): tr 76, kart 72, yanlış 64, özet 68, kaydet 64; etiket 48 (assert ≥ 44).
8. Ekran satırı ≤ 24 karakter (`len`): `Şimdilik amcamla`, `yaşıyorum.`, `I am living with`, `my uncle.`, `I live with`, `şimdilik`,
   `geçici`, `kalıcıysa`, `Kalıcıysa geniş zaman,`, `geçiciyse şimdiki zaman.`, `Kaydet` (künye ve kanal satırı hariç).
9. HTML: `id="kanal"` ve `id="logoimg"` tam 1 kez; `#root.tema-acik` 0 kez; `line-through` 0 kez; şu kimlikler var: `tr1`, `tr2`,
   `dogru-crv`, `dogru-s1`, `dogru-s2`, `dogru-tik`, `yanlis-s1`, `yanlis-s2`, `dogru-etiket`, `dogru-et1`, `dogru-ok`, `dogru-et2`,
   `yanlis-etiket`, `ozet1`, `ozet2`, `kaydet-imi`, `kaydet-hap`, `kaydet-yazi`;
   şunlar yok: `ku-cip`, `cg1`, `cg2`, `hap-kutu`, `soru-kutu`, `kA`, `kB`, `yanlis-yazi`, `yanlis-cizgi`.
10. Yasak söz denetimi kodda YOK (dış grep kapısı; koddaki literal liste grep'i kirletir). Kodda ve yorumlarda "tam ders", "dakika"
    sözleri GEÇMEZ. Emoji, `Math.random`, `Date`, try/except, gradyan, gölge YOK.

## 6. Kabul ölçütü

- `/usr/bin/python3 uret.py` rc 0; stdout `index.html yazıldı <n>`.
- `nesneler.json` 9 blok (kanal, kunye, tr, dogru, yanlis, dogru-etiket, yanlis-etiket, ozet, kaydet), tam sayı.
- `proje/index.html` §5 madde 9'u sağlar; SVG içinde `stroke="#167a4a"` 3 kez (çerçeve + tik + ok), `fill="#167a4a"` 1 kez
  (etiket grubu; CSS seçicisi sayılmaz — QA 1), `#4fbf85` 2 kez.
- DUZ-1 çakışma kapısı: araç yalnız `zaman.json sahneler[]` okur (durağan kare çıkış 2). Repo dosyasına dokunmadan geçici kök
  (`KALEM_KOK`, sahne `sahneler[]` içinde t 0–0,5) ile koşuldu → `çakışma yok (3 örnek, 333 kutu)`, çıkış 0.
- Test, render, `calistir.sh`, git YOK (şef koşar).
