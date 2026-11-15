# Sahne 01 · kapak (HyperFrames DİKEY 1080×1920, 97 kare, 0,00–2,84 sn + 12 kare geçiş payı)

Durum: yazıldı (istem D-S2, 15.11.2026, srv21). Önizleme hazırlığı `ONIZLE_YALNIZ=1` ile koştu. Render yok, `kapak-a.png` /
`kapak.png` yok, commit yok. Tema: acik (koyu kareyle de denetlendi).

Kod yolu: şef `SPEC.md` yazdı → agy tek şerit `uret.py` → şef okudu, koşturdu, kapıya soktu, 2 küçük düzeltmeyi Edit ile yaptı.
`yardim.py` (S1 sahne 01 birebir kopyası, yalnız docstring), `olay.py` ve `calistir.sh` (S1 kopyası + Edit), veri dosyaları
(`zamanlar.json`, `nesneler.json`, `cizim/*`) şefin.

## İçerik
İlk kare = kapak A: logo HUD sol üst, rozet `YDT · BASIC` (x 48), `GENEL` (B = 190 px, üst sınır; 952 px sınırı 300 px verirdi),
sarı hap `≠ ŞU AN` (hap x 166–914; `≠` Fredoka'da yok → 3 kalem çizgisi, `pilMetin`), solda askıda mont (ana ders `MONT`), ortada
işaret eden öğretmen (peeps-kit `PointingFingerWB` + `Short` + `Smile`, 500 px), sağda askıda tişört (ana ders `TISORT`),
etiketler `wears` / `is wearing` (Caveat 700 72), yer çizgisi. Cümle 1 yalnız altyazı bandında sözcük zamanlı + sarı karaoke çizgisi.
2,24–2,82 uçuş: `GENEL` ders adı 1. satırına, hap 2. satırına küçülür (56 px boyu) ve solar; rozet ders adının sağına kayar; sahne grubu
solar; soru satırı `Genel mi, şu an mı?` (Caveat 700 80, sol 48, taban 440) kalemle yazılır. Çip `Hook` uçuş sonunda açılır.

## Olay listesi (küresel sn = yerel sn)
| Olay | Kare / sn | Cümle sözcüğü |
|---|---|---|
| kapak tam görünür (logo, rozet x 48, GENEL, hap + ŞU AN, mont, figür, tişört, etiketler, yer) | 0 / 0,00 | söz öncesi |
| `≠` kalemle: üst çubuk → alt çubuk → eğik (`cizgi`) | 9–24 / 0,30–0,80 | söz öncesi |
| KAPAK KARESİ (≠ bitmiş, altyazı yok, çip yok, ders adı yok) | 27 / 0,90 | — |
| altyazı sözcükleri açılır + karaoke çizgisi | 29 · 43 · 62 · 67 · 74 / 0,95 · 1,43 · 2,07 · 2,23 · 2,47 | Genel 1,00 · mi, 1,48 · şu 2,12 · an 2,28 · mı? 2,52 |
| rozet sağa kayar | 65–76 / 2,18–2,54 | — |
| sahne grubu solar | 67–76 / 2,24–2,54 | — |
| uçuş: GENEL → ders 1, hap → ders 2 (`parilti` kare 67) | 67–85 / 2,24–2,82 | — |
| soru satırı kırpmayla yazılır, `power1.in` (`hisirti` kare 73) | 73–83 / 2,42–2,78 | şu an mı? |
| başlıklar solar · ders adı açılır · çip `Hook` (`tik` kare 84) | 75–85 / 2,50–2,82 | — |
| durgun (son hal = sahne 02 kare 0); son 12 kare geçiş altında | 85–96 / 2,83–3,24 | mı? biter 2,92 |

`olaylar.json`: 4 olay (cizgi, parilti, hisirti, tik), hepsi kare < 85. `uret.py` 8 denetim maddesini assert eder (uçuş çakışma
örneklemesi: bas1 × rozet, bas2 × rozet, bas1 × bas2, bas1 × soru, bas2 × soru; en dar ara bas2 × soru ≈ 21 px, t 2,61).

## Kapı sonucu (son koşu, tur 2)
```
== HAZIRLA → olay 4 · önizleme hazır
== KAPI
01-hyperframes-kapak | çakışma yok (13 örnek, 4265 kutu)
== KARE (açık)  0.2 · 0.9 · 2.5 · 2.6 · 2.8
== KARE (koyu)  0.9
kapı çıkış kodu: 0
```
Komut: `bash araclar/qa-yerel.sh 02-04-ydt-temel-s2 01-hyperframes-kapak 0.2,0.9,2.5,2.6,2.8 0.9 --hazirla`

## Bakılan kareler ve bulgu
| Tur | Kare | Bulgu | Düzeltme |
|---|---|---|---|
| 1 | k/2.8 | soru satırı `Genel mi, şu an m` (kırpma 2,82'de bitiyordu) | `soru` [2,42, 0,36] → 2,78'de tam |
| 1 | k/0.9 | `≠` ile `Ş` arası 23 px, bitişik okunuyor | `GAP` 0,12·B → 0,20·B (hap 732 → 747 px) |
| son | k/0.2, 0.9, 2.5, 2.6, 2.8, koyu/0.9 | taşma, kesik yazı, üst üste binme, okunmaz kontrast, boş kare YOK; 1536 altı boş; 0,9'da `≠` tam, altyazı/çip/ders adı yok; 2,6'da hap soru satırının üstünde (kesişim yok), başlıklar solarken; 2,8'de soru satırı tam, HUD tam (logo, ders 2 satır, rozet, çip `Hook`), altyazı tam satır. 0,2'de `≠` yeri boş (çizim 0,30'da başlar; BRIEF gereği) | — |

## agy koşu özeti
| Şerit | Dosya | Süre | Özet |
|---|---|---|---|
| tek | `uret.py` (SPEC §3) | 252 sn | `~/.claude/canavar/agy-filo/20261115-125455` |
Rol `kod` (gemini-3.8-flash-high), 1/1 başarılı, tek turda SPEC'e uydu. Şef Edit düzeltmeleri: `uret.py` GAP (B formülü dahil),
`zamanlar.json` soru zamanı. agy-filo "değişen" listesinde başka sahnelerin dosyaları göründü (aynı worktree'deki paralel oturumlar);
ajan yalnız `uret.py` yazdı.

## Sahne 02 devri (`devir.json`)
Caveat 700 80, `font-kerning:none`, sol 48, taban 440 (üst 370,9 · alt 457,0), sağ uç 566,1, metin `Genel mi, şu an mı?`, t 2,84.
Altyazı: cümle 1 tek satır, Lexend 500 44, taban 1484, ortalı (kunye.js `altyaziCiz` ile aynı yer). Sahne 02 kare 0 bu konumu kullanmalı.

## Açık noktalar
1. Figür gövdesi: `kadro.ogretmen` = `ShirtPantsWB` (işaret etmez). İstem "işaret pozunda" dediği için aynı kitin `PointingFingerWB` gövdesi
   + kadro saç `Short` / yüz `Smile` kullanıldı (erkek, K22 korunur). Giysi kadrodan farklı; kadro kaydının güncellenmesi şefte.
2. Logo: BRIEF-S2 "Kapak A" ve `kapak-taslak.md` "logo sol alt y ≈ 1478" der; BRIEF-DIKEY §0 (Nadir) "alt bantta logo yok, HUD sol üst".
   HUD sol üst uygulandı (S1 kapak ve S3 kapak B ile aynı). BRIEF satırının düzeltilmesi şefte.
3. "Pembe tişört" mürekkep çizgiyle çizildi (ana ders `sahne-03.js` ile aynı); pembe dolgu tek vurgu kuralını bozar.
4. 0,00–0,30'da hap içinde `≠` yeri boş (BRIEF: `≠` 0,30–0,80'de çizilir). Kapak PNG'si kare 27 (0,90) olduğu için kapakta tam.
5. Mont, tişört, askı `ortak/cizim` kataloğunda yok; ana ders dizileri ve şefin askısı `cizim/giysi.json`'da (kaynak `cizim/KAYNAK.md`).
   Figür verisi `cizim/ogretmen.json` (dijital-anlatim kit kataloğundan). İkisinin `ortak/cizim`'e alınması şef kararı.
6. Son hal (2,83) içerik bandında yalnız soru satırı var; kartlar sahne 02'de. BRIEF-DIKEY §0 "%85 dolu" ölçütü bu 0,0x sn'de tutmaz (S1 ile aynı).
7. Soru satırı `power1.in` ile yazılır: son harfler hızlı gelir (hap yolundan çekilene kadar kalem yavaş başlar).
8. mp4 render, `kapak-a.png`, `kapak.png` yok (istem gereği); `calistir.sh` render dalı kare 27'yi paket köküne `kapak-a.png` yazar
   ve `kapak.png` olarak kopyalar (yalnız tema açık).
