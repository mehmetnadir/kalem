# SPEC — 02-04-ydt-temel-s1 sahne 03 CTA (HyperFrames, DİKEY 1080×1920) · 15.11.2026

## 0. Görev
Yazılacak dosya (yalnız bu): `/home/sef/01dev/_worktrees/kalem-0204/projeler/02-04-ydt-temel-s1/sahneler/03-hyperframes-cta/uret.py`
Başka dosyaya dokunma. Silme yok. Test, render, git yok.

Örnek (kalıp kaynağı): `/home/sef/01dev/_worktrees/kalem-0204/projeler/present-continuous-ileri-s1/sahneler/03-hyperframes-cta/uret.py`
Oradan alınacak kalıp: dosya iskeleti (`AD`, `sys.path`, `import yardim as Y`), `uret()` → `html` dizesi, `<style>` içinde
`Y.font_css()` + `Y.ZEMIN_CSS` + `#sahne{position:absolute;left:0;top:0;}`, `#root` div'i (`data-composition-id="main"`,
`data-start="0"`, `data-duration`, `data-fps="30"`, `data-width="1080"`, `data-height="1920"`), `Y.zemin_html()`, tek `<svg id="sahne">`,
`<defs>` içinde clipPath'ler (`cp()` lambdası), `Y.kunye_svg(CIP)`, `Y.altyazi_svg(T_BAS, sure, ALT)` → `<g id="altyazi">`,
`<script src="lib/gsap.min.js">`, IIFE içinde `gsap.timeline({paused:true})`, `ac()`, `darbe()`, `yaz()`, altyazı aç/kapa döngüsü,
`gsap.set(... svgOrigin)` + `fromTo` ile hap/bant girişi, `window.__timelines["main"] = tl`, `__main__` bloğu
(`Y.font_kopyala(AD/"proje"/"assets"/"fonts")`, `proje/index.html` yazımı).
Örnekten ALINMAYACAK: metinler (`ileri seviye`, `6 dakika`, `Tam ders kanalda · 6 dk`), yerleşim sayıları, sabit `zamanlar.json` okuması,
kuyruk nabzı (`scale 1.015 yoyo`). "kanal" sözü, QR, süre "6 dk" YOK.

Ek kalıp kaynakları:
- Sözcük çapası işlevi `T(i, bas)`: `/home/sef/01dev/_worktrees/kalem-0204/projeler/02-04-ydt-temel/sahneler/14-hyperframes-kapanis/uret.py` satır 17–48
  (zaman.json'dan `SAH`, sözcükler.json süzgeci, sözcük kayarsa `assert`).
- Bavul ikonu verisi `BAVUL` + `_kutusu` + `_daire_yolu` + `ikon_yollari`: `/home/sef/01dev/_worktrees/kalem-0204/projeler/02-04-ydt-temel/sahneler/12-hyperframes-ozet/uret.py`
  satır 64–69 ve 100–150. Kutu sabitlerini (`IKON_EN`, `IKON_BOY`) parametre yap ya da 72×72'ye uyarla.
- Ev ikonu: `Y.tabler("home")`, saat ikonu: `Y.tabler("clock")` (Tabler 24×24, göreli yol komutları; uzunluğu tarayıcıda `getTotalLength` ile al,
  `Y.yol_uzunluk` bu yollarda ÇALIŞMAZ).

## 1. Zaman (tek kaynak; sabit saniye yazma)
- `PAKET = AD.parent.parent`; `SAH` = `PAKET/"zaman.json"` → `sahneler[]` içinde `klasor == AD.name` (t_bas 19.99, kare 347).
- `T_BAS = SAH["t_bas"]`, `KARE = SAH["kare"]`, `SURE = round(KARE / 30, 4)` (11.5667). Yerel sn = küresel − T_BAS. Yerel kare = round(yerel × 30).
- `SOZ` = `PAKET/"ortak/anlatim/sozcukler.json"` içinde `cumle == 3` (18 sözcük). `T(i, bas)` = t0, `E(i, bas)` = t1 (küresel), ikisi de
  `assert sozcuk.lower().startswith(bas.lower())`.
- `ALT` = `PAKET/"ortak/anlatim/altyazi.json"`. `CIP = "Full lesson"` (`ortak/kunye.js` `KUNYE.cipler["03-hyperframes-cta"]`).

Cümle 3 sözcük sırası (i · sözcük · t0 küresel): 0 Bu, 20.54 · 1 üç 21.02 · 2 farktan 21.18 · 3 yalnız 21.74 · 4 biri. 22.22 ·
5 Tam 22.77 · 6 ders: 23.21 (t1 23.81) · 7 Simple 23.97 · 8 Present 24.21 · 9 ve 24.77 · 10 Present 25.25 · 11 Continuous. 25.93 ·
12 Üç 27.00 · 13 farkın 27.24 · 14 hepsi 27.72 · 15 dört 28.36 · 16 buçuk 28.60 · 17 dakikada. 28.84 (t1 29.64).

## 2. Olay listesi (yerel = küresel − 19.99; kare = round(yerel × 30); hepsi `T(i, …)`'den türetilir)

| # | Olay | Başlangıç (sözcük) | Yerel sn · kare | Süre / ease | Ses olayı (tur, guc) |
|---|---|---|---|---|---|
| 1 | `üç` kinetik giriş (satır A) | T(1,"üç") | 1.03 · 31 | 0.22, `back.out(1.6)`, opacity 0→1, y +24→0 | tik 0.4 |
| 2 | `farktan` kinetik | T(2,"farktan") | 1.19 · 36 | aynı | — |
| 3 | `üç` sarı altçizgi (darbe) | T(1)+0.22 | 1.25 · 38 | 0.30, `none` | cizgi 0.5 |
| 4 | `biri` kinetik | T(4,"biri") | 2.23 · 67 | aynı | — |
| 5 | `Tam ders:` Caveat yazımı (clip genişler) | T(5,"tam") | 2.78 · 83 | E(6,"ders") − T(5) = 1.04, `none` | hisirti 0.45 |
| 6 | Ders bandı girişi (dolgu + scale 0.92→1) | T(7,"simple") | 3.98 · 119 | 0.35, `power3.out`, svgOrigin bant merkezi | vurus 0.9 |
| 7 | `Simple` kinetik (bant satır 1) | T(7) | 3.98 · 119 | 0.22 back.out(1.6) | — |
| 8 | `Present` kinetik (satır 1) | T(8,"present") | 4.22 · 127 | aynı | — |
| 9 | `vs` kinetik (satır 2; sesteki `ve`) | T(9,"ve") | 4.78 · 143 | aynı | tik 0.5 |
| 10 | `Present` kinetik (satır 2) | T(10,"present") | 5.26 · 158 | aynı | — |
| 11 | `Continuous` kinetik (satır 2) | T(11,"continuous") | 5.94 · 178 | aynı | — |
| 12 | `farktan` + `biri` çıkış (satır A boşalır, `üç` kalır) | T(12,"üç") | 7.01 · 210 | 0.25, `power2.in`, opacity→0, y→−16 | tik 0.4 |
| 13 | `farkın` kinetik (satır A, aynı x) | T(13,"farkın") | 7.25 · 218 | 0.22 back.out(1.6) | — |
| 14 | `hepsi` kinetik | T(14,"hepsi") | 7.73 · 232 | aynı | — |
| 15 | Saat ikonu darbe (daire, sonra ibre; uzunluğa orantılı) | T(15,"dört") | 8.37 · 251 | 0.35 toplam | cizgi 0.5 |
| 16 | `dört` kinetik (satır E) | T(15) | 8.37 · 251 | 0.22 back.out(1.6) | — |
| 17 | `buçuk` kinetik | T(16,"buçuk") | 8.61 · 258 | aynı | — |
| 18 | `dakikada` kinetik | T(17,"dakikada") | 8.85 · 266 | aynı | — |
| 19 | `@ydspublishing` hap girişi (scale 0.9→1) | T(17) | 8.85 · 266 | 0.30, `power3.out`, svgOrigin hap merkezi | tik 0.6 |
| 20 | `@ydspublishing` yazımı (clip genişler) | T(17)+0.10 | 8.95 · 268 | E(17) − (T(17)+0.10) = 0.70, `none` | hisirti 0.5 |
| 21 | Ev ikonu darbe (bandın solu) | E(17,"dakikada") | 9.65 · 290 | 0.45 toplam | cizgi 0.45 |
| 22 | Bavul ikonu darbe (bandın sağı) | E(17)+0.10 | 9.75 · 293 | 0.45 toplam | cizgi 0.45 |

Hareket 10.20 yerel'de (kare 306) biter. Kare 306–346 durgun son düzen (anlatım 29.64'te biter, 29.56–30.56 durgun kuyruk).
İlk 12 kare (0–11) ve son 12 kare (335–346) durgun: hiçbir tween bu aralıkta başlamaz/sürmez (altyazı aç/kapa hariç).
`farktan` ve `biri` kinetik girişinden önce `opacity:0`; çıkıştan sonra 0 kalır. Satır A'da `üç` ve altçizgisi sahne sonuna kadar kalır.

`uret.py` iki veri dosyası da yazar (sahne dizinine):
- `zamanlar.json`: `{"fps":30, "kare":347, "sure":11.5667, "t_bas":19.99, "<olay adı>": [yerel_bas, sure], …, "olaylar": [[yerel_t, tur, guc], …]}`
  (`olaylar` = tablodaki "Ses olayı" sütunu; 11 satır; yerel_t 4 ondalık).
- `olaylar.json`'u YAZMA (onu `olay.py` `zamanlar.json`'dan üretir).

## 3. Yerleşim (px, 1080×1920; tek sütun; kenar 48; içerik bandı 352–1392; altyazı 1400–1536; 1536 altı BOŞ)

Sabit px yerine adlandırılmış sabitler (modül başında) ve `Y.genislik` ile hesap. Satırlar yatay ortalı (x merkez 540).

| Satır | Öğe | Yazı | Boy | Konum |
|---|---|---|---|---|
| A | `üç` · `farktan` · `biri` → (olay 12) `üç` · `farkın` · `hepsi` | Lexend 700 | 72 | taban y 452. Ortak sol başlangıç `A_X0 = 540 − max(w("üç farktan biri"), w("üç farkın hepsi"))/2` (≈ 267). Her sözcük ayrı `<text text-anchor="start">`, x = A_X0 + `Y.genislik` (önek + boşluk). `üç` iki cümlede aynı yerde durur. |
| A alt | `üç` altçizgisi | path, stroke `R["vurgu"]`, w 10, round | — | y = 452 + 0.42×72 (≈ 482); x A_X0−4 → A_X0+w("üç")+4; elle çizilmiş eğim (orta nokta ±2 px, örnekteki `iu` yolu gibi) |
| B | `Tam ders:` | Caveat 700 | 96 | taban y 620, ortalı; clip rect soldan sağa açılır (örnek `yaz`) |
| Bant | ders bandı: `rect` x 132 · y 660 · w 816 · h 236 · rx 48 · fill `R["vurgu"]` | — | — | bant merkezi (540, 778) |
| Bant 1 | `Simple` · `Present` | Fredoka 700 | `BANT_BOY` | taban y 758; satır ortalı (x0 = 540 − w(satır)/2), sözcük x = x0 + önek genişliği; fill `R["zemin"]` |
| Bant 2 | `vs` · `Present` · `Continuous` | Fredoka 700 | `BANT_BOY` | taban y 850; aynı kural; fill `R["zemin"]` |
| İkon sol | ev (`Y.tabler("home")`), kutu 72×72 | stroke `R["murekkep"]`, görünür kalınlık 4.4 | — | kutu merkezi (84, 778) → x 48–120 (banda 12 px boşluk) |
| İkon sağ | bavul (`BAVUL` verisi), kutu 72×72 | stroke `R["murekkep"]`, 4.4 (ince parça 3.0) | — | kutu merkezi (996, 778) → x 960–1032 |
| E | saat ikonu + `dört` · `buçuk` · `dakikada` | Lexend 700 | 72 | taban y 1066. Grup genişliği = 88 (saat) + 20 + w("dört buçuk dakikada"); grup x0 = 540 − grup/2 (≈ 99). Saat kutusu 88×88, merkez y = 1066 − 0.36×72 (≈ 1040); stroke `R["murekkep"]`, görünür 4.4 (iç grupta `scale(88/24)`, dış grupta `stroke-width = 4.4/ölçek`; örnekteki `saat` grubu kalıbı). Yazı x0 = grup x0 + 108. |
| F | `@ydspublishing` hapı: `rect` fill `R["vurgu"]`, h 112, rx 56, w = w("@ydspublishing", Fredoka 700, 64) + 112 | Fredoka 700 | 64 | rect y 1200, ortalı; yazı fill `R["zemin"]`, taban y 1279, clip rect soldan açılır |

`BANT_BOY = min(96, floor((816 − 2×28) / Y.genislik("Fredoka", 700, "vs Present Continuous", 1)))` → 74 beklenir.
Kontrol: satır 2 genişliği ≤ 760 (bant içi 28 px boşluk); `assert` ile denetle.

Altyazı ve künye `yardim.py`'den gelir (değiştirme): `Y.kunye_svg(CIP)` (logo, 2 satır ders adı, `YDT · BASIC` rozeti, `Full lesson` çipi),
`Y.altyazi_svg(T_BAS, SURE, ALT)`. Künye kare 0'dan tam görünür (uçuş yok).

## 4. Renk ve tema kuralları
- Yalnız `Y.RENK` koyu değerleri yazılır: `zemin #1b1a17`, `murekkep #f3efe6`, `vurgu #f2a93b`. Tema dönüşümünü `calistir.sh` → `hf_tema.py` yapar:
  `rect[fill="#f2a93b"]` → açıkta `#ffe066` (vurguDolgu), `text[fill="#1b1a17"]` → açıkta `#1b2440` (pilMetin). Bant ve hap bu yüzden
  `rect fill=vurgu` + `text fill=zemin` olmalı.
- Vurgu renginde YAZI yok (açık temada ≈ 2,3:1). Sarı yalnız: bant dolgusu, hap dolgusu, `üç` altçizgisi.
- `ikincil`, `kirmizi`, yeşil, gradyan, gölge, parlama, emoji YOK.
- `id="t2"`, `id="rz1"`, `id="ku-nokta"` kullanma (`hf_tema.py` bunlara özel kural yazar). Bütün id'ler tekil.

## 5. Kurallar
- Ekran metni yalnız şunlar: `üç farktan biri`, `üç farkın hepsi`, `Tam ders:`, `Simple Present`, `vs Present Continuous`,
  `dört buçuk dakikada`, `@ydspublishing`. Satır ≤ 24 karakter.
- Yazı tabanı ≥ 64 px (künye 56/36/40 ve altyazı 44 `yardim.py` HUD ölçüsü, istisna).
- Kinetik sözcük: `fromTo(opacity 0, y 24 → opacity 1, y 0, 0.22, back.out(1.6), immediateRender:false)`. TikTok karaoke yok (ölçek büyütme, renk değişimi yok).
- Clip ile yazım: örnekteki `cp()` + `yaz(id, [bas, sure], w)` kalıbı (clip rect x = yazı solu − 12, genişlik 0 → w + 24).
- Darbe: örnekteki `darbe(id, bas, sure)`; çok parçalı ikon için parçaları sırayla, süreyi `getTotalLength` oranıyla böl (tarayıcıda, deterministik).
- Bütün öğeler başlangıçta `opacity:0` (künye, zemin, altyazı kendi kuralıyla). Son karede görünenler: satır A (`üç farkın hepsi` + altçizgi),
  `Tam ders:`, bant (2 satır), ev + bavul, saat + `dört buçuk dakikada`, hap.
- Kuyrukta (kare 306–346) hareket yok.
- Python: type hint ekle (yeni işlevlerde), satır ≤ 120, girinti 4 (örnek dosyayla aynı).
- `__main__`: `(AD/"proje").mkdir(exist_ok=True)`, font kopyası, `index.html` + `zamanlar.json` yazımı, kısa özet `print`.

## 6. Kabul ölçütü (şef doğrular)
1. `cd <sahne> && /usr/bin/python3 uret.py` çıkış 0; `proje/index.html` ve `zamanlar.json` yazılır.
2. `zamanlar.json` `olaylar` 11 satır; bütün yerel zamanlar 0.4 ≤ t ≤ 10.2; kare < 347.
3. Sözcük `assert`'leri 18 sözcüğün sırasını doğrular (yanlış çapa = durur).
4. `index.html` içinde: `data-width="1080"`, `data-height="1920"`, `data-duration="11.5667"`, `id="kunye"`, `id="altyazi"`,
   `kanal` / `6 dk` / `dakika<` dizileri yok; `#ffe066`/`#1b2440` sabit yazılmamış (tema dönüştürür).
5. `bash araclar/qa-yerel.sh 02-04-ydt-temel-s1 03-hyperframes-cta 22.7,27.0,30.4 29.8 --hazirla` → kapı çıkış kodu 0 (şef koşturur).
