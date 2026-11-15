# Sahne 01 · kapak (HyperFrames DİKEY 1080×1920, 102 kare, 0,00–3,00 sn + 12 kare geçiş payı)

Durum: yazıldı (istem D-S1, 15.11.2026, srv21). Önizleme hazırlığı `ONIZLE_YALNIZ=1` ile koştu. Render yok, `kapak.png` yok, commit yok.
Tema: acik (koyu kareyle de denetlendi)

Kod yolu: şef `SPEC.md` yazdı → agy 3 şerit paralel (yardim.py değişikliği, uret.py, olay.py) → şef okudu, koşturdu, kapıya soktu,
küçük düzeltmeleri Edit ile yaptı (3 tur). Veri dosyaları (`zamanlar.json`, `nesneler.json`, `cizim/*`) ve `calistir.sh` şefin.

## İçerik
İlk kare = kapak (BRIEF-S1 "Kapak"): logo HUD sol üst, rozet `YDT · BASIC`, başlık `YAŞIYORUM` (B = 161 px, 952 px'e sığan en büyük boy;
190'da 1060 px olurdu) / `= İKİ ZAMAN` sarı hapta (hap 948 px), solda ev (Tabler home), sağda elinde bavul tutan öğretmen figürü
(react-peeps kit ShirtPantsWB + Short + Smile = `kadro.ogretmen`), etiketler `I live` / `I am living` (Caveat 72), altyazı bandı.
Cümle 1 Caveat 80, sözcük zamanlı. 2,00–2,85 uçuş: başlıklar künyedeki ders adına küçülür ve solar, rozet ders adının sağına kayar,
sahne grubu solar, iki cümle satırı içerik bandının üstüne çıkar (taban 452 / 600 = sahne 02 kare 0). Çip `Hook` uçuş sonunda açılır.

## Olay listesi (küresel sn = yerel sn)
| Olay | Kare / sn | Cümle sözcüğü |
|---|---|---|
| kapak tam görünür (logo, rozet x 48, başlık, hap, ev, figür, bavul, etiketler) | 0 / 0,00 | söz öncesi |
| `YOR` altına sarı el altçizgisi (`cizgi`) | 9–24 / 0,30–0,80 | söz öncesi |
| altyazı dilimi (cümle 1, 2 satır) | 29 / 0,95 → sahne sonu | İstanbul'da t0 − 0,05 |
| satır 1 `İstanbul'da` yazılır (`hisirti`) | 30–38 / 1,00–1,28 | İstanbul'da (1,00) |
| satır 1 `yaşı-yor-um.` yazılır (`hisirti`) | 49–58 / 1,64–1,92 | yaşıyorum. (1,64) |
| KAPAK KARESİ (çip yok, ders adı yok, satır 1 tam) | 59 / 1,97 | — |
| rozet sağa kayar · sahne grubu solar | 60–72 / 2,00–2,40 | — |
| uçuş: başlıklar → ders adı, satırlar yukarı (`parilti`) | 60–85 / 2,00–2,85 | — |
| başlıklar solar | 75–80 / 2,49–2,67 | — |
| satır 2 `Amcamla yaşı-yor-um.` tek süpürme (`hisirti`) | 76–87 / 2,52–2,90 | Amcamla (2,52) |
| ders adı açılır · çip `Hook` açılır (`tik` kare 85) | 79–85 / 2,62–2,85 | — |
| durgun; son 12 kare geçiş altında | 87–101 / 2,90–3,40 | 2. yaşıyorum. 3,08 → sahne 02 |

`olaylar.json`: 6 olay (cizgi, hisirti ×3, parilti, tik), hepsi kare < 90. `uret.py` 7 denetim maddesini assert eder (uçuş çakışma örneklemesi dahil).

## Kapı sonucu (son koşu, tur 4)
```
== HAZIRLA → olay 6 · önizleme hazır
== KAPI
01-hyperframes-kapak | çakışma yok (13 örnek, 3634 kutu)
== KARE (açık)  0.2 · 1.97 · 2.95
== KARE (koyu)  1.97
kapı çıkış kodu: 0
```
Komut: `bash araclar/qa-yerel.sh 02-04-ydt-temel-s1 01-hyperframes-kapak 0.2,1.97,2.95 1.97 --hazirla`

## Bakılan kareler ve bulgu
| Tur | Kare | Bulgu | Düzeltme |
|---|---|---|---|
| 1 | kapı 2,75 | başlıklar ders adıyla çapraz solarken ikisi de opaklık ≥ 0,5 (hata ×2); başlık 1 × hap 26 px (uyarı) | başlık solması 2,49–2,67, ders açılışı 2,62–2,85; hedefler ±16 px açıldı (`ucus_ayrik`); assert'e bas1 × bas2 eklendi |
| 2 | k/2.95 | satır 2 `…yaşı-yor-un` kesik (süpürme 2,97'de bitiyordu) | `satir2_son` 2,90 |
| 3 | k/ara/koyu/2.62 | doğrudan aramada (0 → 2,62) başlıklar geride, hap satır 1'in üstünde; sıralı aramada doğru | `svgOrigin` uçuştan önce bir kez `gsap.set` (`smoothOrigin: false`); tek atlama = sıralı arama doğrulandı |
| son | k/0.2, k/1.97, k/2.95, k/koyu/1.97, k/ara/0.55, 2.2, 2.45, 2.62, 2.75, k/ara/koyu/2.45, 2.62 | taşma, kesik yazı, üst üste binme, okunmaz kontrast, boş kare YOK; platform bandı boş; altyazı 2 satır; 1,97'de satır 1 tam, çip ve ders adı yok; 2,95'te iki satır tam, HUD tam. 2,62 / 2,75'te satır 2 yazım ortasında (beklenen). Tek atlamalı arama = sıralı arama | — |

Bayat kareler ve arama denemesi `~/Silinecekler/2026-11-15-0204/` altına taşındı (`s1-01-kapak-*`, `LISTE.md` satırları).

## agy koşu özeti
| Şerit | Dosya | Süre | Özet |
|---|---|---|---|
| A | `yardim.py` (§3) | 138 sn | `~/.claude/canavar/agy-filo/20261115-121115` |
| B | `uret.py` (§4) | 334 sn | `~/.claude/canavar/agy-filo/20261115-121119` |
| C | `olay.py` (§5) | 70 sn | `~/.claude/canavar/agy-filo/20261115-121122` |
Rol `kod` (gemini-3.8-flash-high). Şef Edit düzeltmeleri: `uret.py` uçuş hedefi ve solma zamanları, assert bas1 × bas2, `uc2` svgOrigin; `zamanlar.json`.
agy-filo "değişen" listesinde başka sahnelerin dosyaları göründü: aynı worktree'deki paralel oturumlar; ajanlar yalnız hedef dosyayı yazdı (yardim.py farkı yalnız §3).

## Sahne 02 devri (`devir.json`)
Caveat 700 80, `font-kerning:none`, sol 48, taban [452, 600], *yor* x aralığı [514,1–599,1] / [445,3–530,3], sağ uç [716,2 / 647,4], t 3,0.
Altyazı sahne 02 ile aynı kural (kunye.js `altyaziDilimle`): cümle 1 tek dilim, 2 satır.

## Açık noktalar
1. Logo: BRIEF-S1 "Kapak" ve `kapak-taslak.md` "logo sol alt y ≈ 1478" der; BRIEF-DIKEY §0 (Nadir bulgusu) "alt bantta logo yok, HUD sol üst 96 px" der.
   HUD sol üst uygulandı. BRIEF-S1 / kapak-taslak satırının düzeltilmesi şefte (yazma kapsamı dışı).
2. Satır 2 `yaşı-yor-um.` ekranda 2,90'da tam, seste 3,08: D-02 "kare 0 = iki satır tam" şartı. 0,2–0,6 sn erken görünür.
3. Bavul katalogda yok (`ortak/cizim`, Open Doodles): Tabler `luggage` (MIT, ortak kaynakla aynı unpkg yolu) `cizim/luggage.svg` olarak sahneye indirildi.
   Figür: `kadro.ogretmen` parçaları dijital-anlatim kit kataloğundan `cizim/ogretmen.json`'a çıkarıldı. Kaynak/lisans `cizim/KAYNAK.md`.
   İkisinin `ortak/cizim`'e alınması şef kararı.
4. `kapak-taslak.md` "baş eve dönük": kit figürü önden bakar; baş dönmedi.
5. Son hal (2,85–3,00) içerik bandının alt yarısı boş; BRIEF-S1 tasarımı (satırlar bandın üstüne, kartlar sahne 02'de). BRIEF-DIKEY §0 "%85 dolu" ölçütü bu 0,15 sn'de tutmaz.
6. Hap içinde `İ` noktaları hap üst kenarına ≈ 10 px; okunur, sıkışık değil.
7. Aynı `svgOrigin` kalıbı örnek `present-continuous-ileri-s1/sahneler/01-hyperframes-kapak/uret.py` `uc2()` içinde de var: çok işçili render ya da editörde
   rastgele aramada aynı kayma beklenir (orada denenmedi; kapsam dışı). Sözleşme adayı ders (yazma kapsamı dışı, şefe):
   "HF uçuşunda svgOrigin tween başına verilmez; bir kez `gsap.set`. Kapı çapraz solmayı opaklık ≥ 0,5 iki öğe olarak sayar."
8. mp4 render ve `kapak.png` yok (istem gereği); `calistir.sh` render dalı kare 59'u paket köküne yazar.
