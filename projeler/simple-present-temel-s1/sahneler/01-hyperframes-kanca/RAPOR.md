# Sahne 01 · kanca (huni v2; HyperFrames DİKEY 1080×1920, 102 kare, 0,00–3,00 sn + 12 kare geçiş payı)

| Ölçüm | Değer |
|---|---|
| Durum | yazıldı (istem D-S1, 15.11.2026, srv21). Önizleme hazırlığı `ONIZLE_YALNIZ=1`. mp4 yok, commit yok |
| Tema | açık (koyu karelerle de denetlendi; `proje/` açık temada bırakıldı) |
| qa-yerel (tur 2, son) | çıkış 0 · `01-hyperframes-kanca \| çakışma yok (13 örnek, 6252 kutu)` (tur 1: 6199 kutu, karaokesiz) |
| Çakışma kapısı (ayrı koşu, tur 2) | çıkış 0 · 0 uyarı |
| Metin taraması (`tam[ ]ders\|dak[i]ka`) | boş (grep çıkış 1) |
| Altyazı karaokesi | okunan sözcüğe sarı altçizgi (03 ve 04 sahneleriyle aynı kalıp); kare 1,2 Kardeşim · 1,7 gider · 2,6 go · 2,95 mu |
| Kanal katmanı (piksel) | 11 karede birebir aynı: logo görünür x 60–239, mürekkep y 298–330 (resim 291–339); yazı x 264–596, y 296–339 (taban 330); emsal 02-04-s1 s01 ile aynı |
| Boş bantlar (piksel) | 0–280, 1570–1920 ve x 961–1080: 11 karede mürekkep yok |
| Kapak A | `kapak-a.png` = `kapak.png` (md5 `c0527f63…`), `k/koyu/kapak-a-koyu.png` (`cd7c1c01…`); 1080×1920; t 0,90 (kare 27); altyazısız |

Kod yolu: şef `SPEC.md` yazdı → agy 2 şerit paralel (A `yardim.py` §3 coco yükleyicisi, B `uret.py` §4) → şef okudu, koşturdu, kapıya soktu
→ tur 2: kardeş HF sahnelerinde altyazı karaokesi olduğu görüldü (sözleşme 15.11 notları) → SPEC §6 → agy şerit C (`yardim.py` karaoke
altyazı, 03-kaydet kalıbı, üst sınır `t1`) → şef Edit `uret.py` (3 değer açma, `veri.karaoke`, `V.karaoke.forEach`; sahne sonrası sözcük atlanır).
Emsal kopyası (`cp -p` + kısa Edit, şef): `yardim.py` (docstring, `KONU`, `KONU_PARCA`), `olay.py` (4 olay), `calistir.sh` (başlık, denetim
kareleri 0,2 / 0,9 / 2,2 / 2,95, kapak notu), `nesneler.json`. Şef yazdı: `zamanlar.json`. Şef Edit (agy çıktısı): `uret.py` devir `olcek` 2 → 5 basamak.

## İçerik
İlk kare = kapak: kanal katmanı (logo + `@ydspublishing`), künye satırında yalnız rozet `YDT · BASIC` (x 60), başlık `GO mu,` (B = 178,
orta 510, zemin konturu 12) / `GOES mu?` sarı hapta (x 60–960; hap genişliği B'yi sınırlar), altında solda genç figür (`standing-2`, kalem
çizgisi 4 px), sağda otobüs (`coco/bus`, aynalı: ön yüz solda, figüre doğru gider; çizgi 4,4 px), zemin çizgisi 80–950 (y 1372). Etiket yok.
`?` Fredoka glifi değil, kalem yolu (kanca + nokta, kalınlık 24,9 = Fredoka 700 sapı; açıkta pilMetin, koyuda zemin rengi üstünde pilMetin).
Uçuş 1,90–2,45: başlık 1 konu adının `Simple` yerine, hap `Present` yerine küçülür (±10 px dikey ayrım), rozet 1,90–2,20'de x 60 → 309,7
kayar; figür + otobüs + zemin grubu (80, 932)'den 0,29425 ölçekle x 700–956, y 465–595'e iner (çizgiler `non-scaling-stroke`: küçükte de 4 px).
Konu adı 2,33–2,45 açılır. 2,45 `Kardeşim gider:` (Caveat 700 72, x 60–438, taban 560) kırpmayla; 2,52 kart `go` (x 60–440, y 620–820,
Fredoka 700 120, taban 750) girer.

## Olay listesi (küresel sn = yerel sn)
| Olay | Kare / sn | Cümle sözcüğü |
|---|---|---|
| kapak tam görünür (kanal, rozet x 60, başlık, hap, figür, otobüs, zemin) | 0 / 0,00 | söz öncesi |
| `?` kanca kalemle (`cizgi`) | 9–20 / 0,30–0,68 | söz öncesi |
| `?` noktası | 21–24 / 0,70–0,80 | söz öncesi |
| KAPAK KARESİ (başlık tam, `?` çizili, altyazı yok) | 27 / 0,90 | — |
| altyazı dilimi (cümle 1, tek satır, orta x 510) | 29 / 0,95 → sahne sonu | Kardeşim (1,00) |
| karaoke altçizgisi: Kardeşim · gider: · go · mu, (0,15 sn çizilir, sonraki sözcükte söner) | 30 · 47 · 76 · 85 | sözcük `t0` (1,00 · 1,56 · 2,52 · 2,84) |
| rozet sağa kayar | 57–66 / 1,90–2,20 | — |
| uçuş: başlıklar → konu satırı (`parilti`) · grup sağ üste | 57–74 / 1,90–2,45 | — |
| başlıklar solar · konu adı açılır | 68–74 / 2,27–2,45 | — |
| `Kardeşim gider:` kırpmayla (`hisirti`) | 74–81 / 2,45–2,70 | gider: bitti (2,24) |
| kart `go` girer (`tik`) | 76–88 / 2,52–2,92 | go (2,52) |
| durgun; son 12 kare geçiş altında | 88–101 / 2,92–3,40 | `mu,` 2,84 → sahne 02 |

`olaylar.json`: 4 olay (kare 9, 57, 74, 76), hepsi < 90. `uret.py` 7 denetim maddesini assert eder (uçuş örneklemesi: bas1 × hap, bas1 × rz0,
hap × rz0, grup × bas1, grup × hap, bas1 × kanal, hap × kanal; bütün uçuş: grup × rz0, grup × kanal, grup × künye bandı). Şef ön simülasyonu
`ucus_olcek` 0,45'te hap × rz0 dokunuşu buldu (t 2,267, 6 px sınırda) → 0,40 seçildi; 0 çakışma.

## Kapı çıktısı (son koşu)
```
== HAZIRLA → olay 4 · önizleme hazır
== KAPI
01-hyperframes-kanca | çakışma yok (13 örnek, 6252 kutu)
== KARE (açık) 0 · 1.5 · 2.95   == KARE (koyu) 1.5
kapı çıkış kodu: 0
== ÇAKIŞMA KAPISI (ayrı): 01-hyperframes-kanca | çakışma yok (13 örnek, 6252 kutu) · kapı çıkış: 0
== METİN TARAMASI: boş (grep çıkış 1)
```
Komutlar: `bash araclar/qa-yerel.sh simple-present-temel-s1 01-hyperframes-kanca 0.00,1.50,2.95 1.50 --hazirla` ·
`node araclar/cakisma-kapisi.mjs simple-present-temel-s1 --sahne 01-hyperframes-kanca --port 41333 --sunucu 41022`.

## Bakılan kareler ve bulgu
| Tur | Kare | Bulgu | Düzeltme |
|---|---|---|---|
| 1 | k/…-0, k/…-1.5, k/…-2.95, k/koyu/…-1.5, k/ara/0.55, 0.9, 2.0, 2.1, 2.2, 2.3, 2.4, 2.5, 2.7, k/ara/koyu/2.2, 2.95 (kontak `k/ara/kontak-ucus.png`) | taşma, kesik yazı, üst üste binme, okunmaz kontrast, boş kare YOK; 0–280 ve 1570–1920 boş; x 961+ boş; uçuşta rozet başlık gelmeden kayar, grup başlıklara değmez; 2,3'te başlık parçaları ile konu adı çapraz solar (kapı eşiği 0,5, kasıtlı); 2,95'te konu + rozet tek satır, satır, kart, küçük grup tam | — |
| 2 (karaoke) | k/…-0, 1.5, 2.95, k/koyu/1.5, k/ara/1.2, 1.7, 2.6, k/ara/koyu/1.7 (şerit `k/ara/kontak-karaoke.png`) | altçizgi doğru sözcükte, sözcük altında 12 px, iki temada okunur; `gider` altçizgisi `g` kuyruğuna değer (kapı altçizgi muafiyeti, 03/04 ile aynı); başka bulgu yok | — |
| Kapak A | `k/ka-acik/at-0.9s.png`, `k/ka-koyu/at-0.9s.png` | altyazı yok; kanal, rozet, başlık, hap, `?`, figür, otobüs, zemin; iki temada okunur. Tur 2 koduyla yeniden çekim md5 birebir aynı (kopya `~/Silinecekler/2026-11-15-huni-v2/simple-present-temel-s1/sahne01-ka2/`) | — |

Kapak A yöntemi (S1-KAPAK-A): `ONIZLE_YALNIZ=1 bash calistir.sh --tema <t>` → `cp -a proje/. proje-ka/` → `proje-ka/index.html` ilk `</style>`
önüne `#altyazi{display:none}` → `hyperframes snapshot . --at 0.90 --no-end --keep -o k/ka-<t>` (koyu önce, açık sonra; `proje/` açık kalır).
Açık → paket kökü `kapak-a.png`, `cp -p` → `kapak.png`; koyu → `k/koyu/kapak-a-koyu.png`. Paket kökünde önceden kapak yoktu (taşınan dosya yok).

## agy koşu özeti
| Şerit | Dosya | Süre | Özet |
|---|---|---|---|
| A | `yardim.py` (§3) | 54 sn | `~/.claude/canavar/agy-filo/20261115-192724` |
| B | `uret.py` (§4) | 294 sn | `~/.claude/canavar/agy-filo/20261115-192727` |
| C (tur 2) | `yardim.py` (§6 karaoke) | 82 sn | `~/.claude/canavar/agy-filo/20261115-193700` |
Rol `kod` (gemini-3.8-flash-high). Üç çıktı da SPEC'e uydu; geri gönderme yok (tur 2 yeni gereksinimdir, düzeltme değil). "değişen" listesinde başka sahnelerin dosyaları göründü:
aynı worktree'deki paralel oturumlar; ajanlar yalnız hedef dosyayı yazdı.

## Sahne 02 devri (`devir.json`)
`satir` Caveat 700 72, x 60, taban 560, sağ uç 438,14 · `kart_go` dış kenar x 60, y 620, w 380, h 200, rx 28, çizgi 4, `go` Fredoka 700 120,
orta x 250, taban 750 · `grup` kutu [700, 465, 256, 130,06], ölçek 0,29425, figür kutusu [711,77, 465, 37,62, 129,47], otobüs kutusu
[776,51, 524,73, 176,55, 68,56], çizgi 4 / 4,4 / 4 px, otobüs aynalı · konu `Simple Present` 34, rozet x 309,67 w 203,57 · t 3,0.
İstem sabitleri (taban 560 · kart y 620–820 · `go` x 60–440 · figür + otobüs x 700–960, y 460–600) korundu; tek ayrıntı: grubun sağ ucu 956
(x 960'a 4 px pay), üst ucu 465.

## Açık noktalar
1. **Figür yönü.** `standing-2` SVG'sinde yüz izleyicinin sağına (figürün kendi soluna) döner; ayna yok, figür otobüse bakar. İstemdeki
   "sola dönük" izleyicinin solu demekse figür aynalanmalı (o zaman otobüse sırtını döner). Şef/Nadir kararı.
2. **Karaoke emsalde yok.** Emsal 02-04-s1 s01 altyazısı düzdür; bu sahne paketin 03/04 sahneleri gibi karaokeli. Sahne 02 (Paper.js,
   `kunye.js` altyazısı) karaokesizse 01 → 02 geçişinde altçizgi kaybolur; 02 istemi bunu bilmeli.
3. **Küçük figür ayrıntısı.** Küçük hâlde (≈ 38 × 129 px) 4 px çizgi figürü koyu bir siluete yaklaştırır; okunur. Sahne 02 figürü kendi
   çizgisiyle yeniden çizecekse kalınlık `devir.json` `cizgi_px` alanından okunmalı.
4. Son hal (2,92–3,00) içerik bandının alt yarısı (840–1380) boş: `goes` kartı ve EN cümle sahne 02'de gelir (BRIEF sırası).
5. `go` / `goes` okunuşu ve kanca süresi (cümle 1 4,12'de biter) S1-C-RAPOR açık noktalarında; bu sahne yalnız 0,00–3,00'ı taşır.
