# Sahne 01 · kapak v2 (huni v2; HyperFrames DİKEY 1080×1920, 102 kare, 0,00–3,00 sn + 12 kare geçiş payı)

| Ölçüm | Değer |
|---|---|
| Durum | yazıldı (istem D-V2, 15.11.2026, srv21). Önizleme hazırlığı `ONIZLE_YALNIZ=1`. mp4 yok, commit yok |
| Tema | açık (koyu kareyle de denetlendi) |
| qa-yerel (tur 2) | çıkış 0 · `01-hyperframes-kapak \| çakışma yok (13 örnek, 3528 kutu)` |
| Çakışma kapısı (ayrı koşu) | çıkış 0 · 0 uyarı |
| Metin taraması (`tam ders\|dakika`) | boş (grep çıkış 1) |
| Kanal katmanı | 10 karede birebir aynı: logo görünür x 60, mürekkep y 298–330 (resim 291–339); yazı x 264–596, y 296–339 (taban 330) |
| Kapak A | `kapak-a.png` = `kapak.png` (md5 `d802d84f…`), `k/koyu/kapak-a-koyu.png` (`0837174f…`); 1080×1920; t 1,97; altyazısız |

Eski dosyalar (v1 SPEC, uret.py, yardim.py, RAPOR.md, calistir.sh, zamanlar.json, devir.json, k/, proje-ka/):
`~/Silinecekler/2026-11-15-huni-v2/02-04-ydt-temel-s1/sahneler/01-hyperframes-kapak/`.

Kod yolu: şef `SPEC.md` (v2) yazdı → agy 2 şerit paralel (A `yardim.py` §3, B `uret.py` §4) → şef okudu, koşturdu, kapıya soktu.
Şef Edit'leri: `yardim.py` 2 hata metni (Türkçe karakter); `uret.py` E2 x 954 (tur 1 bulgusu); `zamanlar.json` `ucus_ayrik` 16 → 10;
`calistir.sh` render dalı artık `kapak.png` yazmaz (kare 59 altyazılı).

## İçerik (v1 ile aynı; değişen yerleşim + kanal katmanı)
İlk kare = kapak: kanal katmanı (logo + `@ydspublishing`), rozet `YDT · BASIC` x 60, başlık `YAŞIYORUM` (B = 152, 900 px'e sığan en büyük) /
`= İKİ ZAMAN` sarı hapta (x 62–958), solda ev, sağda bavullu öğretmen figürü, etiketler `I live` / `I am living` (Caveat 72), yer çizgisi 1372.
Cümle 1 Caveat 80, x 84, sözcük zamanlı. Uçuş 2,00–2,85: başlık 1 konu adının sol parçasına (`Simple Present vs`, sol uç x 60), hap sağ
parçasına (`Present Continuous`, sağ uç x 645) küçülür ve solar; rozet x 60 → 665 kayar; sahne grubu solar; satırlar 920/1040 → 560/680
(sahne 02 v2 `Y_L1`/`Y_L2`, `SOL` = 84). Konu adı (Fredoka 34, taban 420) 2,62'de açılır. Çip YOK.

## Olay listesi (küresel sn = yerel sn)
| Olay | Kare / sn | Cümle sözcüğü |
|---|---|---|
| kapak tam görünür (kanal, rozet x 60, başlık, hap, ev, figür, bavul, etiketler) | 0 / 0,00 | söz öncesi |
| `YOR` altına sarı el altçizgisi (`cizgi`) | 9–24 / 0,30–0,80 | söz öncesi |
| altyazı dilimi (cümle 1, 2 satır, orta x 510) | 29 / 0,95 → sahne sonu | İstanbul'da t0 − 0,05 |
| satır 1 `İstanbul'da` (`hisirti`) | 30–38 / 1,00–1,28 | İstanbul'da (1,00) |
| satır 1 `yaşı-yor-um.` (`hisirti`) | 49–58 / 1,64–1,92 | yaşıyorum. (1,64) |
| KAPAK KARESİ (satır 1 tam, konu adı yok) | 59 / 1,97 | — |
| rozet sağa kayar · sahne grubu solar | 60–72 / 2,00–2,40 | — |
| uçuş: başlıklar → konu satırı, satırlar yukarı (`parilti`) | 60–85 / 2,00–2,85 | — |
| başlıklar solar | 75–80 / 2,49–2,67 | — |
| satır 2 `Amcamla yaşı-yor-um.` tek süpürme (`hisirti`) | 76–87 / 2,52–2,90 | Amcamla (2,52) |
| konu adı açılır (`tik` kare 85) | 79–85 / 2,62–2,85 | — |
| durgun; son 12 kare geçiş altında | 87–101 / 2,90–3,40 | 2. yaşıyorum. 3,08 → sahne 02 |

`olaylar.json`: 6 olay, hepsi kare < 90. `uret.py` 7 denetim maddesini assert eder (uçuş çakışma örneklemesi: bas1 × hap, bas1 × bas2t,
bas1 × rz0, hap × rz0, hap × r1, başlıklar × kanal, r1 × kanal, r1 × künye bandı).

## Kapı çıktısı (son koşu)
```
== HAZIRLA → olay 6 · önizleme hazır
== KAPI
01-hyperframes-kapak | çakışma yok (13 örnek, 3528 kutu)
== KARE (açık) 0 · 1.5 · 2.95   == KARE (koyu) 1.5
kapı çıkış kodu: 0
== ÇAKIŞMA KAPISI (ayrı): 01-hyperframes-kapak | çakışma yok (13 örnek, 3528 kutu) · kapı çıkış: 0
```
Komutlar: `bash araclar/qa-yerel.sh 02-04-ydt-temel-s1 01-hyperframes-kapak 0.00,1.50,2.95 1.50 --hazirla` ·
`node araclar/cakisma-kapisi.mjs 02-04-ydt-temel-s1 --sahne 01-hyperframes-kapak --port 41333 --sunucu 41022`.

## Bakılan kareler ve bulgu
| Tur | Kare | Bulgu | Düzeltme |
|---|---|---|---|
| 1 | k/0, k/1.5, k/koyu/1.5 | `I am living` g kuyruğu x 961–965 (sağ 960–1080 bölgesi; piksel ölçümü) | E2 `text-anchor="end"` x 960 → 954 |
| 2 | k/0, k/1.5, k/2.95, k/koyu/1.5, k/ara/1.97, 2.2, 2.45, 2.55, 2.62, 2.75, k/ara/koyu/2.45 (kontak `k/ara/kontak-ucus.png`) | taşma, kesik yazı, üst üste binme, okunmaz kontrast, boş kare YOK; 0–280 ve 1570–1920 boş; x 961+ boş; altyazı x 81–936, y 1416–1522; kanal katmanı her karede aynı yer ve boy; uçuşta başlıklar yan yana iner (2,55: başlık 1 sağ ucu ↔ hap sol ucu ≈ 42 px); 2,95'te konu + rozet tek satır, iki satır tam | — |
| Kapak A | `k/ka-acik/at-1.97s.png`, `k/ka-koyu/at-1.97s.png` | altyazı yok; kanal, rozet, başlık, hap, cümle 1 tam, figür, ev, etiketler; iki temada okunur | — |

Kapak A yöntemi (S1-KAPAK-A): `ONIZLE_YALNIZ=1 bash calistir.sh --tema <t>` → `cp -a proje/. proje-ka/` → `proje-ka/index.html` ilk `</style>`
önüne `#altyazi{display:none}` → `hyperframes snapshot . --at 1.97 --no-end --keep -o k/ka-<t>` (koyu önce, açık sonra; `proje/` açık kalır).
Açık → paket kökü `kapak-a.png`, `cp -p` → `kapak.png`; koyu → `k/koyu/kapak-a-koyu.png`. Eski kapaklar `~/Silinecekler/2026-11-15-huni-v2/02-04-ydt-temel-s1/`.

## agy koşu özeti
| Şerit | Dosya | Süre | Özet |
|---|---|---|---|
| A | `yardim.py` (§3) | 98 sn | `~/.claude/canavar/agy-filo/20261115-185132` |
| B | `uret.py` (§4) | 142 sn | `~/.claude/canavar/agy-filo/20261115-185136` |
Rol `kod` (gemini-3.8-flash-high). "değişen" listesinde başka sahnelerin dosyaları göründü: aynı worktree'deki paralel oturumlar; ajanlar yalnız hedef dosyayı yazdı.

## Sahne 02 devri (`devir.json`)
Caveat 700 80, `font-kerning:none`, sol 84, taban [560, 680], *yor* x [550,1–635,1] / [481,3–566,3], sağ uç [752,2 / 683,4], t 3,0.
Sahne 02 v2 (`sahne-02.js`): `SOL = KUNYE.kenar + 24` = 84, `Y_L1` 560, `Y_L2` 680 → birebir. Rozet (pay 20, Lexend 26, y 386–434),
konu boyu 34 ve altyazı ortası 510 canvas `ortak/kunye.js` v2 ile aynı.

## Açık noktalar
1. HF kutu adları `kunye:kanal:image0` / `kunye:kanal:text0` (tür `kunye`): `hf-kutu.mjs` grup içinde 2 öğe olunca adı böler; tek `kunye:kanal` adı canvas kancasının adıdır.
2. Satır 2 `yaşı-yor-um.` ekranda 2,90'da tam, seste 3,08 (v1 ile aynı; sahne 02 "kare 0 = iki satır tam" şartı).
3. Son hal (2,85–3,00) içerik bandının alt yarısı boş (v1 ile aynı; kartlar sahne 02'de).
4. Rozet iç payı (20) ve konu iki parça hedefi BRIEF'te yazılı değil; değerler canvas künyeyle eşit seçildi.
5. Süre 31,75 sn standart hedefini (≈ 22–26) aşar (V2-C-RAPOR açık nokta 1); bu sahneyi etkilemez.
