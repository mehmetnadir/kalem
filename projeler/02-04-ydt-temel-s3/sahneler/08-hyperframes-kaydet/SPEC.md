# SPEC — 02-04-ydt-temel-s3 sahne 08 Kaydet (HyperFrames, DİKEY 1080×1920, huni v2) · 15.11.2026

> DUZ2 (15.11): kart satır 2 `kesin düzenleme → am going.` (A3); satırlar 64 px, sol x 96; karttaki tren/bilet simgesi kalktı; altyazı karaoke tspan (ikincil → mürekkep); kol b için cümle no veriden (KAYMA). Kaynak `uret.py`.
> DUZ2 (16.11, KBJ EK-7): `leaves` hap geçişi: hap yazısı ve hap virgülü anında söner, mürekkep `leaves,` anında gelir, yalnız hap zemini 0,10 sn'de söner; `#leaves-hap` mürekkep yazının altına alındı. Eski 0,20 sn çapraz geçişte koyu temada hap yazısı soluk hap üstünde 2,1:1 kalıyordu; yeni geçiş karesi (yerel 3,57) açık mürekkep 7,1:1.


Yazan: şef (istem D-V2-S3 + şef notu 19:00). Uygulayan: `agy-filo tek --rol kod`. K = `/home/sef/01dev/_worktrees/kalem-0204`.
Sahne dizini D = `K/projeler/02-04-ydt-temel-s3/sahneler/08-hyperframes-kaydet/`. Paket P = `K/projeler/02-04-ydt-temel-s3/`.
Bağlayıcı: `/home/sef/01dev/dijital-anlatim/.claude/docs/huni-v2-standart.md` §1–§3 · `P/BRIEF-S3.md` "Yerleşim" + "Sahne içeriği" 15,99–21,33.

## 1. Yazılacak dosya
- YAZ (yeni): `/home/sef/01dev/_worktrees/kalem-0204/projeler/02-04-ydt-temel-s3/sahneler/08-hyperframes-kaydet/uret.py`
- Başka dosyaya dokunma. Silme yok. Test, render, git yok.
- Hazır (şef koydu; DOKUNMA): `D/yardim.py` (S1 sahne 08 kopyası; v2 kanal katmanı `Y.kunye_svg()` içinde), `D/olay.py`, `D/calistir.sh`.

## 2. Kalıp (oku, yapıyı al; kodu birebir kopyalama)
| Kalıp | Mutlak yol | Ne alınır |
|---|---|---|
| İskelet | `/home/sef/01dev/_worktrees/kalem-0204/projeler/02-04-ydt-temel-s1/sahneler/08-hyperframes-kaydet/uret.py` | `AD`, `sys.path.insert`, `import yardim as Y`, `PAKET`, `SAH` (`zaman.json` → `sahneler[]`, `klasor == AD.name`), `T_BAS`, `KARE`, `SURE = round(KARE / 30, 4)`; `SOZ`/`ALT` okuma; `yerel`, `T`, `E`; `BEKLENEN_SOZLER` denetimi; `uret() -> tuple[str, dict[str, Any]]`; HTML kabuğu (`Y.font_css()`, `Y.ZEMIN_CSS`, `#root` öznitelikleri, `Y.zemin_html()`, tek `<svg id="sahne">`, `lib/gsap.min.js`, `ac()`, altyazı + karaoke döngüleri, `window.__timelines["main"]`); `darbe` kalıbı (`#kaydet-imi` bloğu: dasharray L, offset L → 0); `__main__` (font_kopyala, index.html, zamanlar.json, iki print) |
| İkon verisi + ok | `/home/sef/01dev/_worktrees/kalem-0204/projeler/02-04-ydt-temel-s3/sahneler/04-hyperframes-hikaye/uret.py` | satır 36–145: `_kutu`, `TREN`, `_bilet`, `BILET`, `_kutusu`, `_daire_yolu`, `ikon_yollari` BİREBİR (koordinat değişmez; `import math` gerekir). Satır 291–367 `kart_svg()`: tren/bilet renk–kalınlık kuralı, ok çizimi (`dx_ok`, `dy_ok`, `x_ok0`, `x_ok1`, `y_ok`), parça kimlikleri. Hikâye A ile aynı kart dili (döngü tutarlılığı) |

ALINMAYACAK: S1'deki `#uc` üst yazısı, kâğıt dolgusu `#kagit`, `kart_kenar_yolu()`, `Kaydet` hapı, kart ölçek girişi; hikâye uret.py'deki
`kunye_svg` (burada `Y.kunye_svg()` kullanılır), başlık, `kaydet_svg`, blok/nesneler.json.

## 3. Zaman ve sözcük (cümle 4, öğretmen)
- `SOZ` = `P/ortak/anlatim/sozcukler.json` içinde `cumle == 4`; `ALT` = `P/ortak/anlatim/altyazi.json` içinde `cumle == 4`.
- `assert len(SOZ) == 11`, `assert len(ALT) == 2`. `BEKLENEN_SOZLER = [(0,"Bu"), (1,"üç"), (2,"farktan"), (3,"yalnız"), (4,"biri"),
  (5,"Bir"), (6,"arkadaşına"), (7,"gönder"), (8,"o"), (9,"da"), (10,"karıştırıyor")]`.
- `T_BAS` 15,99 · `KARE` 172 · `SURE` 5,7333 · `ICERIK = SAH["icerik_kare"] / 30` (5,3333; son 12 kare geçiş) ·
  `ALT_SON = round(SAH["t_son"] - T_BAS, 3)` (5,34).
- Altyazı: `Y.altyazi_svg(T_BAS, ALT_SON, ALT)` (ikinci argüman SURE DEĞİL): ikinci parça (t1 21,41) 21,33'te kapanır (istem).
- Zaman her yerde `T(i, bas)` / `yerel(...)` ile hesaplanır; sabit saniye yazma (yalnız aşağıdaki +0,06 / +0,10 / +0,16 kaydırmaları).

## 4. Olay listesi (yerel = küresel − 15,99; kare = round(yerel × 30))
| olay | yerel formül | yerel | kare | küresel | sözcük | hareket |
|---|---|---|---|---|---|---|
| `kart_ciz` | `yerel(T(0,"Bu"))` | 0,55 | 16 | 16,54 | `Bu,` | `#kart-kenar` darbe 0,40 sn `sine.inOut` |
| `satir1` | `yerel(T(0)) + 0.06` | 0,61 | 18 | 16,60 | `Bu,` | `tren_i` hepsi darbe 0,30 sn `power1.out`; `#s1` opaklık 0 → 1, 0,25 sn `power2.out`; `#kart-s1-ok` darbe 0,20 sn (+0,05) |
| `satir2` | `yerel(T(0)) + 0.16` | 0,71 | 21 | 16,70 | `Bu,` | `bilet_i` darbe 0,30 sn; `#s2` opaklık 0 → 1, 0,25 sn; `#kart-s2-ok` darbe 0,20 sn (+0,05) |
| `gonder_ciz` | `yerel(T(5,"Bir"))` | 2,78 | 83 | 18,77 | `Bir` | `#gonder-dolgu` + `#gonder-cizgi` darbe 0,40 sn `sine.inOut` |
| `imi_ciz` | `yerel(T(5)) + 0.10` | 2,88 | 86 | 18,87 | `Bir` | `#kaydet-imi` darbe 0,40 sn; `#kaydet-yazi` opaklık 0 → 1, 0,25 sn |
| `arkadasina` | `yerel(T(6,"arkadaşına"))` | 3,02 | 91 | 19,01 | `arkadaşına` | `#gonder-yazi1` opaklık 0 → 1 + y 12 → 0, 0,25 sn `power3.out` |
| `gonder_yaz` | `yerel(T(7,"gönder"))` | 3,54 | 106 | 19,53 | `gönder;` | `#gonder-yazi2` aynı hareket |
| `sari_gecis` | `yerel(T(7,"gönder"))` | 3,54 | 106 | 19,53 | `gönder;` | `#gonder-dolgu` `fillOpacity` 0 → 1, 0,25 sn; `#leaves-hap` opaklık 1 → 0, 0,25 sn; `#leaves-alti` darbe 0,30 sn |
| `kuyruk_durgun` | `ICERIK` | 5,333 | 160 | 21,323 | sahne sonu | hareket yok |

- Kart 17,00'de (yerel 1,01) tamamlanır, 21,33'e kadar konumu ve boyu değişmez (≈ 4,3 sn). Kartta ölçek/konum tween'i YOK;
  `sari_gecis` yalnız hap → altçizgi değişimidir (aynı anda tek sarı).
- Ses olayları (`zamanlar["olaylar"]`, `[yerel, tur, guc]`): `[0.55, "cizgi", 0.5]`, `[2.78, "cizgi", 0.5]`, `[3.54, "tik", 0.5]`
  (değer `yerel(T(...))`'ten). `olay.py` 12 ≤ kare < 160 denetler.
- `zamanlar` şeması S1 ile aynı: `fps`, `kare`, `sure`, `t_bas`, her olay `[yerel_bas, süre]`, `olaylar`, `olay_listesi`
  (her satır `olay`, `kare`, `yerel`, `kuresel`, `sozcuk`). `assert`: son tween bitişi ≤ `ICERIK` (yerel 5,333).

## 5. Yerleşim (px; içerik x 60–960, y 460–1380; 0–280 ve 1570–1920 boş)
| Öğe | Kimlik | Değer |
|---|---|---|
| Kanal + künye | `#kunye` | `Y.kunye_svg()` (argümansız); y 291–434; kare 0'dan opaklık 1; tween YOK |
| Kart çerçevesi | `#kart-kenar` (`<path>`, `style="opacity:0"`) | tek alt yol, saat yönünde yuvarlak dikdörtgen x 62–958, y 562–898, r 28: `M100 562 H930 A28 28 0 0 1 958 590 V870 A28 28 0 0 1 930 898 H90 A28 28 0 0 1 62 870 V590 A28 28 0 0 1 90 562 L114 564` (sonda el izi bindirmesi); `fill="none"`, `stroke=R["murekkep"]`, `stroke-width="4"`, round cap/join. Dış kenar 60–960 × 560–900. Kâğıt dolgusu YOK |
| Satır 1 | `#s1` (`<g style="opacity:0">`) | taban `T1 = 705`: `#kart-s1-sol` `Tarife` · `#leaves-yazi` `leaves` (mürekkep) · `#leaves-hap` · `#kart-s1-virgul` `,` |
| Satır 2 | `#s2` (`<g style="opacity:0">`) | taban `T2 = 801`: `#kart-s2-sol` `plan` · `#kart-s2-sag` `am going.` |
| Oklar | `#kart-s1-ok`, `#kart-s2-ok` (`style="opacity:0"`) | grubun DIŞINDA (darbe için); hikâye kalıbı |
| Tren | `<g id="kart-tren">`, parçalar `tren_0…` (`style="opacity:0"`) | `ikon_yollari(TREN, 154, T1 - 0.30*72, 136, 64)` (satır 1 başı) |
| Bilet | `<g id="kart-bilet" transform="rotate(-3 154 {T2-0.30*72})">`, parçalar `bilet_0…` | `ikon_yollari(BILET, 154, T2 - 0.30*72, 132, 60)` (satır 2 başı; istem: iki ikon da satır başında) |
| Gönder satırı | `#gonder` | simge + `Arkadaşına` + `gönder`; y ≈ 971–1056; §7 |
| Kaydet satırı | `#kaydet` | yer imi + `Kaydet`; y ≈ 1089–1156; §7 |
| Altyazı | `#altyazi` | `<g id="altyazi">` + `Y.altyazi_svg(...)`; y 1400–1550 |

Kart yazısı Fredoka 700 72, `R["murekkep"]`, `xml:space="preserve"`. Metin kolonu `TX = 242`.
- Satır 1: `x_ok0 = TX + gen("Tarife") + 0.22*72`, `x_ok1 = x_ok0 + 0.70*72`; `LX = x_ok1 + 0.22*72 + 14` (hap iç boşluğu);
  `#leaves-yazi` x `LX`; virgül x `LX + gen("leaves") + 16`.
- `#leaves-hap` = `<g id="leaves-hap"><rect x=LX-14 y=T1-0.80*72 width=gen("leaves")+28 height=72 rx=36 fill=R["vurgu"]/>`
  `<text x=LX y=T1 ... fill=R["zemin"]>leaves</text></g>` (`#leaves-yazi`'nın ÜSTÜNDE; hap solunca alttaki mürekkep yazı görünür).
- `#leaves-alti` (`#s1` DIŞINDA, `style="opacity:0"`): `M{LX-4} {T1+12} Q{LX+gen/2} {T1+15} {LX+gen+4} {T1+11}`, `stroke=R["murekkep"]`,
  `stroke-width="6"`, round cap, `fill="none"`.
- QA turu 1 düzeltmesi (şef, Edit): `#leaves-yazi` metni `leaves,` (virgül bitişik) ve `style="opacity:0"`; `sari_gecis`'te
  `#leaves-hap` + `#kart-s1-virgul` 0,20 sn söner, `#leaves-yazi` +0,10'da 0,20 sn gelir (iki yazı aynı anda 0,5 opaklığı
  aşmaz; kapı yazı × yazı uyarısı kalktı). Çerçeve yolu sonu `L114 562` (bindirme izi kusur gibi görünüyordu).
- Satır 2: `x_ok0`, `x_ok1` aynı formül (`plan`); `am going.` x `x_ok1 + 0.22*72`.
- Ok: hikâye kalıbı (gövde + uç, `y_ok = taban - 0.28*72`, `dx = 18*cos(0.5)`, `dy = 18*sin(0.5)`, stroke 6). `→` karakteri HTML'de YOK.
- `gen(s) = Y.genislik("Fredoka", 700, s, 72)`. CSS: `#sahne text{font-kerning:none;}` (ölçüm kerning'siz).

## 6. Renk ve tema (koyu değer yazılır; `P/ortak/hf_tema.py` çevirir)
| Öğe | Yazılan | Açık temada |
|---|---|---|
| yazı, çerçeve, ok, altçizgi, simge çizgisi | `R["murekkep"]` `#f3efe6` | `#1b2440` |
| tren ray (son parça), bilet `ince` | `R["ikincil"]` | `#5a6275` |
| `#leaves-hap` rect | `fill=R["vurgu"]` `#f2a93b` | `#ffe066` (rect kuralı) |
| hap yazısı | `text fill=R["zemin"]` `#1b1a17` | `#1b2440` (pilMetin) |
| `#gonder-dolgu` dolgusu | `fill=R["vurgu"]` + `fill-opacity="0"` + CSS `#root #gonder-dolgu{fill:var(--vurguDolgu,#f2a93b);}` | `#ffe066` (path kuralı `--vurgu` koyu turuncu verirdi; CSS ezer) |

`uret.py` metninde `#root.tema-acik` dizgesi OLMAZ (hf_tema "çevrildi" sanar). Kırmızı, yeşil, gradyan, gölge, emoji YOK.
Sarı sırası: 16,60–19,53 `leaves` hapı; 19,53'ten sonra `#gonder-dolgu`. Aynı anda tek içerik sarısı (künye rozeti ve karaoke çizgisi ortak parça).

## 7. Gönder + Kaydet satırları (şef notu 19:00: iki eylem birlikte; büyük gönder, küçük kaydet)
Simge yolları literal yazılır (Tabler, MIT; dosyadan okuma). Simge sütunu x 60–132 (orta 96); yazı sütunu x 156.
- `#gonder-ikon` = `<g transform="translate(48 962) scale(4)" fill="none" stroke=R["murekkep"] stroke-width="1.5"
  stroke-linecap="round" stroke-linejoin="round">` içinde:
  `<path id="gonder-dolgu" d="M21 3l-6.5 18a.55 .55 0 0 1 -1 0l-3.5 -7l-7 -3.5a.55 .55 0 0 1 0 -1l18 -6.5" fill=R["vurgu"] fill-opacity="0" style="opacity:0"/>`
  `<path id="gonder-cizgi" d="M10 14l11 -11" style="opacity:0"/>` (görünür 6 px çizgi; simge x 60–132, y 974–1046).
- `#gonder-yazi1` `Arkadaşına` x 156, taban 1038, Fredoka 700 80, mürekkep, `style="opacity:0"`;
  `#gonder-yazi2` `gönder` x `156 + Y.genislik("Fredoka", 700, "Arkadaşına ", 80)` (boşluk dahil), aynı taban/boy.
  `assert` satır sağ ucu ≤ 960 (beklenen ≈ 841).
- `#kaydet-ikon` = `<g transform="translate(57.6 1081.6) scale(3.2)" fill="none" stroke=R["murekkep"] stroke-width="1.5" ...>`
  `<path id="kaydet-imi" d="M18 7v14l-6 -4l-6 4v-14a4 4 0 0 1 4 -4h4a4 4 0 0 1 4 4z" style="opacity:0"/>` (simge x 77–115, y 1091–1149).
- `#kaydet-yazi` `Kaydet` x 156, taban 1142, Fredoka 700 64, mürekkep, hap YOK, `style="opacity:0"`.
- Paylaş/QR/düğme taklidi YOK; yalnız bu iki satır.

## 8. Kurallar (assert ile)
1. Satır ≤ 24 karakter: `Tarife → leaves,`, `plan → am going.`, `Arkadaşına gönder`, `Kaydet`.
2. İçerik yazı boyu ≥ 64 (kart 72, gönder 80, kaydet 64).
3. Kutu sınırları: kart 60–960 × 560–900; satır 1/2 sağ uç ≤ 934; tren ve bilet ölçekli kutusu x ∈ [86, TX − 16], y ∈ [566, 894];
   gönder satırı y ∈ [960, 1060]; kaydet satırı y ∈ [1080, 1160]; hepsi x ∈ [60, 960].
4. Ok gövdesi sol sözcükten ≥ 10, hap/sağ sözcükten ≥ 10 uzak.
5. HTML'de YOK (büyük/küçük duyarsız): yasak çağrı sözleri (standart §1 kural 4–5; listeyi koda literal yazma, dış grep kirlenir),
   `→`, `≠`, `id="rz1"`, `id="t2"`, `id="ku-nokta"`, U+1F000 üstü karakter.
6. 0. sn'de içerik bandı boş: kanal/künye dışındaki her öğe `style="opacity:0"` ile başlar. Bütün tween'lerde `immediateRender: false`.
7. Son 12 kare (yerel ≥ 5,333) tween yok.
8. Python: tür ipuçları zorunlu, girinti 4 boşluk (S1 dosyası gibi), satır ≤ 120, `from __future__ import annotations`.

## 9. Kabul ölçütü (agy koşmaz; şef koşar)
1. `cd D && /usr/bin/python3 uret.py` çıkış 0; `proje/index.html` + `zamanlar.json` yazılır; `zamanlar.json` 3 ses olayı, `kare` 172, `t_bas` 15.99.
2. `ONIZLE_YALNIZ=1 bash calistir.sh --tema acik` → `önizleme hazır`; `olaylar.json` 3 satır.
3. `bash araclar/qa-yerel.sh 02-04-ydt-temel-s3 08-hyperframes-kaydet 15.99,18.66,21.3 19.6 --hazirla` → çıkış 0.
4. `node araclar/cakisma-kapisi.mjs 02-04-ydt-temel-s3 --sahne 08-hyperframes-kaydet --port 41333 --sunucu 41022` → 0 uyarı.
5. Karede: 15,99 yalnız kanal + künye; 18,66 kart tam + altyazı; 21,30 kart (`leaves` altçizgili) + sarı gönder simgesi + `Arkadaşına gönder` + yer imi + `Kaydet`.
