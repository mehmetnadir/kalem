# Sahne 01 · kapak, huni v2 (HyperFrames DİKEY 1080×1920, 97 kare = içerik 85 + geçiş 12, 0,00–2,84 sn)

| Ölçüm | Sonuç |
|---|---|
| `qa-yerel.sh … 0.0,1.5,2.8 0.9 --hazirla` | çıkış 0 |
| Çakışma kapısı (ayrı koşu, `--port 41333 --sunucu 41022`) | çıkış 0 · `çakışma yok (13 örnek, 4059 kutu)` · 0 uyarı |
| Metin taraması (`tam ders\|dakika`, `k/` hariç) | boş (grep çıkış 1) |
| Kapak A | `kapak-a.png` = `kapak.png` (cmp aynı) · `k/koyu/kapak-a-koyu.png` · üçü 1080×1920 |
| Render | yok (istem gereği; yalnız `ONIZLE_YALNIZ=1`) · commit yok |

Durum: yazıldı (istem D-S2-V2, 15.11.2026, srv21). Tema: acik (koyu kareyle de denetlendi). v1 yedeği (SPEC, RAPOR, kod, kareler):
`~/Silinecekler/2026-11-15-huni-v2/02-04-ydt-temel-s2/sahneler/01-hyperframes-kapak/`. Geçici kapak kopyaları (`proje-ka-acik`, `proje-ka-koyu`)
ve v1'den kalan bayat kareler: `…/01-hyperframes-kapak-gecici/`.

Kod yolu: şef `SPEC.md` (v2) yazdı → agy 2 paralel şerit (A `yardim.py`, B `uret.py`) → şef iki dosyayı baştan sona okudu, SPEC'e uygun;
tek Edit: `yardim.py` docstring satırı 120 karakteri aşıyordu, ikiye bölündü. `calistir.sh` şef Edit (başlık, `GEN/YUK` yakalama 1080 1920 +
ffprobe boyut denetimi, denetim kareleri 0,0/0,9/1,5/2,5/2,8). `olay.py`, `zamanlar.json`, `nesneler.json`, `cizim/*` değişmedi.

## Değişen yerleşim (içerik v1 ile aynı)
- Kanal katmanı `<g id="kanal">` (`#kunye` içinde, tween yok): logo `#logoimg` x 53,15 y 291–339 (48 × 193,49) + `#kanal-ad` `@ydspublishing`
  Lexend 700 42, x 263, taban 330. Kare 0'dan son kareye alfa 1.
- Künye: `#ku-konu` `Simple Present vs Present Continuous` Fredoka 700 34 (rozetle 960'a sığan en büyük), x 60, taban 420 (kapakta gizli);
  `#rz0` `YDT · BASIC` hap x 664,63 w 203,57 y 386–434 (iç boşluk 20/yan; eş sahne 03 SPEC ile aynı). Kapakta rozet x 60'ta, konu yok.
  Çip YOK; v1 HUD (logo y 48, ders y 212, çip) kalktı.
- Başlık SOLA YASLI x 60: `GENEL` B 190 (taban 599, üst 466), hap `≠ ŞU AN` x 60–807, y 633–861. Mont x 60–270, figür 400–620 (440 px,
  parmak tişörte), tişört 710–950, kancalar ≥ 891, `wears` / `is wearing` Caveat 72 taban 1280, yer çizgisi 60–960 y 1372.
- Uçuş: `GENEL` → "Simple Present" üstüne (o1 360,6/532,5 → h1 174,8/408,1), hap → "Present Continuous" üstüne (o2 433,6/747,2 →
  h2 492,7/409,1), ölçek 34/190. Soru satırı Caveat 700 72, x 60, taban 530 (sağ 526,27, üst 467,79, alt 545,26).
- Altyazı + karaoke v1 ile aynı (Lexend 500 44, taban 1484, ortalı 540).

## Olay listesi (küresel sn = yerel sn)
| Olay | Kare / sn | Cümle sözcüğü |
|---|---|---|
| kapak tam görünür (kanal, rozet x 60, GENEL, hap + ŞU AN, mont, figür, tişört, etiketler, yer) | 0 / 0,00 | söz öncesi |
| `≠` kalemle: üst → alt → eğik (`cizgi`) | 9–24 / 0,30–0,80 | söz öncesi |
| KAPAK KARESİ (`≠` bitmiş, altyazı yok, konu yok) | 27 / 0,90 | — |
| altyazı sözcükleri + karaoke çizgisi | 29 · 43 · 62 · 67 · 74 / 0,95 · 1,43 · 2,07 · 2,23 · 2,47 | Genel 1,00 · mi, 1,48 · şu 2,12 · an 2,28 · mı? 2,52 |
| rozet sağa kayar x 60 → 664,6 | 65–76 / 2,18–2,54 | — |
| sahne grubu solar | 67–76 / 2,24–2,54 | — |
| uçuş GENEL → Simple Present, hap → Present Continuous (`parilti` kare 67) | 67–85 / 2,24–2,82 | — |
| soru satırı kırpmayla yazılır (`hisirti` kare 73) | 73–83 / 2,42–2,78 | şu an mı? |
| başlıklar solar · konu açılır (`tik` kare 84) | 75–85 / 2,50–2,82 | — |
| durgun (son hal = sahne 02 kare 0); son 12 kare geçiş altında | 85–96 / 2,83–3,24 | mı? biter 2,92 |

`uret.py` 9 denetim maddesini assert eder. Uçuş örneklemesi (1/30 sn) en dar aralar: bas1 × bas2 24,4 px (t 2,24), bas1 × rozet 26,0 (2,24),
bas1 × soru 27,8 (2,607). `olaylar.json`: 4 olay, hepsi kare < 85.

## Kapı sonucu (son satırlar)
```
== HAZIRLA → devir {… "boy": 72, "sol": 60, "taban": 530 …} · olay 4 · önizleme hazır
== KAPI
01-hyperframes-kapak | çakışma yok (13 örnek, 4059 kutu)
== KARE (açık) 0 · 1.5 · 2.8      == KARE (koyu) 0.9
kapı çıkış kodu: 0
(ayrı koşu) 01-hyperframes-kapak | çakışma yok (13 örnek, 4059 kutu) · rc 0
```

## Bakılan kareler ve bulgu
| Kare | Bulgu |
|---|---|
| `k/…-0.png` (0,0) | kanal + rozet + başlık + sahne; `≠` yeri boş (çizim 0,30'da başlar, BRIEF gereği); 0–280 ve 1400–1920 boş |
| `k/…-1.5.png` | `≠` tam; altyazı `Genel mi,` + karaoke çizgisi; kanal aynı yerde |
| `k/…-2.4.png`, `2.5`, `2.6` (uçuş) | GENEL sola-yukarı, hap sağa-yukarı ayrışır; rozet önceden çekilir; soru satırı soldan açılır; binme yok |
| `k/…-2.8.png` (son) | kanal · konu + rozet · soru satırı tam · altyazı tam; içerik bandında yalnız soru satırı |
| `k/koyu/…-0.9.png` | koyu tema okunur; hap turuncu (koyu `vurguDolgu`), yazı zemin rengi |
| `kapak-a.png`, `kapak.png`, `k/koyu/kapak-a-koyu.png` | altyazı yok, kanal katmanı var, `≠` bitmiş, konu yok; 1080×1920 |
Hepsinde: taşma, kesik yazı, üst üste binme, okunmaz kontrast, boş kare YOK; içerik x ≤ 960; altyazıyla çakışma yok.

Kapak A yöntemi (S1-KAPAK-A): `ONIZLE_YALNIZ=1 bash calistir.sh --tema koyu|acik` → `proje` → `proje-ka` kopyası → yalnız CSS
`#altyazi{display:none}` → `hyperframes snapshot proje-ka --at 0.9 --no-end --keep`. Render dalının kare 27 satırı aynı kalır: ilk altyazı sözcüğü
0,95'te açılır (denetim 8), kare 27 altyazısızdır.

## agy koşu özeti
| Şerit | Dosya | Süre | Özet |
|---|---|---|---|
| A | `yardim.py` (SPEC §2) | 72 sn | `~/.claude/canavar/agy-filo/20261115-185332` |
| B | `uret.py` (SPEC §3) | 203 sn | `~/.claude/canavar/agy-filo/20261115-185335` |
Rol `kod` (gemini-3.8-flash-high), 2/2 başarılı, ikisi de tek turda SPEC'e uydu. agy-filo "değişen" listesinde başka sahnelerin dosyaları
göründü (aynı worktree'deki paralel oturumlar); şeritler yalnız kendi dosyasını yazdı.

## Sahne 02 devri (`devir.json`)
Caveat 700 72, `font-kerning:none`, sol 60, taban 530 (üst 467,79 · alt 545,26), sağ uç 526,27, metin `Genel mi, şu an mı?`, t 2,84.
Künye son hali: kanal katmanı + konu (Fredoka 700 34, x 60, taban 420) + rozet (x 664,63–868,20, y 386–434). Altyazı v1 ile aynı.

## Açık noktalar
1. Rozet iç boşluğu (20/yan → genişlik 203,57) istemde yazmıyor; eş sahne 03 SPEC değeri alındı. Diğer sahneler aynı değeri almalı.
2. Altyazı Lexend 44 px: "≥ 64" kuralı içerik yazısı içindir; altyazı `ortak/kunye.js` `altyaziCiz` ile aynı tutuldu (sahne 02 ile süreklilik).
3. Başlık sola yaslı (v1 ortalı); gerekçe: kanal, künye ve soru satırı x 60'ta, uçuş tek yöne akar. Nadir ortalı isterse yalnız t1x/hap_x değişir.
4. Tişört mürekkep çizgi (pembe dolgu yok, tek vurgu kuralı; v1 ile aynı). Figür `PointingFingerWB` (kadro `ShirtPantsWB` değil; v1 açık noktası).
5. Başlıklar 2,50–2,66 solar, uçuş 2,82'de biter: iniş anı görünmez, konu 2,62–2,82'de açılır (çapraz geçiş; v1 zamanlaması korundu).
6. Kanal katmanı tek ortak dosyadan gelmiyor (bu sahne kendi `yardim.py` kopyasında çizer); değerler BRIEF "Yerleşim" ile birebir.
