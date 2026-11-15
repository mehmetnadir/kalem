# DUZ3-0201I — `present-continuous-ileri-dikey` (dikey tam ders) düzeltmeleri · 16.11.2026

> Ana rapor: `../present-continuous-ileri/uretim-tutanagi/DUZ3-RAPOR.md` (cümle tablosu, ses, Whisper, yayın verisi, kısa video).
> Bu belge yalnız dikey pakete özgü işi yazar. Render yok, mp4 yok, alt ajan yok, silinen dosya yok.

## 1. Ses

Dikey paket sesi ana paketten alır: `ortak/anlatim` → `../../present-continuous-ileri/ortak/anlatim` (sembolik bağ, 14.11).
Ayrı kopya yok; dosyalar aynı dosyadır (sha256 eşitliği kendiliğinden; `anlatim.wav` `56d4c991e45c`, `anlatim.m4a` `8bc542bcf7f9`).
Yeniden sentez yok. Ders süresi 84,96 → 88,16 sn.

## 2. Düzeltme tablosu

| # | Konu | Dosya | Önce → sonra |
|---|---|---|---|
| 1 | Zaman | `zaman.json` | 03 kare 442 → 472 (15,25–30,58) · 04 30,58–43,07 · 05 43,07–55,08 · 06 kare 956 → 1022 (55,08–88,16); ana paketle aynı |
| 2 | c3 (jüri) | `sahneler/03-paperjs-ornek1/sahne-03.js`, `calistir.sh` | sözcük zamanları yeni sese; while vurgusu 27,74; sahne toplanması 27,78–28,56; `aynı anda` el yazısı (Caveat 64, sarı, x 770, sözcük zamanlı 28,58–29,02) toplanan sahnenin sağ boşluğunda; formül kartı 28,90, `is sleep-ing` 29,20, `am talk-ing` 29,54; `N=472` |
| 3 | Kayma | `sahneler/04-canvas-ornek2/sahne.js`, `05-canvas-ornek3/sahne.js` | `kayma: -1.0` (sahne eski çerçevede; yerel kareler aynı) |
| 4 | Altyazı kayması | `04-canvas-ornek2/sahne-ortak.js`, `05-canvas-ornek3/sahne-ortak.js` | altyazı zamanı `zm(f) - kayma` (yeni çerçeve); `02-04-ydt-temel-dikey` 05 ile aynı kalıp |
| 5 | c7 (jüri) | `sahneler/06-hyperframes-form/uret.py`, `zamanlar.json`, `calistir.sh` | c7 dizinleri kaydırıldı (38 dizin); `tc1`, `tc2` sabitleri sözcüğe bağlandı (`I − 0,31`, `He − 0,84`); R4 iki satır `always + V-ing` / `çoğu zaman şikâyet` (tek satır 864 px figüre binerdi); çip 3 `always + V-ing: çoğu zaman şikâyet` (771 px); Kod `olay + -ing ✓` / `durum + -ing ✗` ve üstte `genellikle` (Caveat 48) |
| 6 | Altyazı taşması | `sahneler/06-hyperframes-form/uret.py` | yeni son parça (`Always artı -ing … durum genellikle almaz.`) 3 satır tutuyordu; `altyazi_svg` 3. satırı 2.'ye ekleyip taşırıyordu. `alt_bol`: 2 satırı aşan parça cümle sınırından bölünür, dilim ilk sözcüğünde açılır (`altyazi-bol.js` kuralı). Son parça 78,16 ve 83,56'da iki dilim |
| 7 | Rozet (HV-24) | `ortak/kunye.js`, `sahneler/01-hyperframes-giris/{uret.py, yardim.py}`, `sahneler/06-hyperframes-form/yardim.py`, `BRIEF-DIKEY.md` | `YDT · ADVANCED` → `YDT · İLERİ` |
| 8 | c1 eski metin (kendi bulgum) | `sahneler/01-hyperframes-giris/uret.py`, `zamanlar.json`; `sahneler/02-paperjs-kanca/sahne-02.js` | 13.11 c1 düzeltmesi (`Dil sınavındaki -ing tuzağına düşme.`, kalem `accccbb`) yalnız ana pakete girmişti. Dikeyde: altyazı sabit metni `YDT'nin -ing tuzağına düşme.` idi; satır dizisi `[[0, 1], [2, 3]]` 4 sözcükte kalıyor, `düşme.` hiç yazılmıyordu; sarı halka `-ing` yerine `sınavındaki`yi sarıyordu; sahne 02 kartı `YDT'nin -ing / tuzağına düşme.` idi. Şimdi: satırlar `[[0, 1], [2, 3, 4]]`, halka `-ing` sözcüğünden aranır (ana paketteki yöntem), halka zamanı 1,92 (ses), altyazı ve 02 kartı yeni metin |

## 3. Kareler (kendim baktım)

Komut: `node araclar/sahne-kare.mjs present-continuous-ileri-dikey <sahne> <t,…> <dizin> --tema acik --port 41333 --sunucu 41022`.
Dizin: `sahneler/<sahne>/k/duz3/` (git dışı).

| Sahne | Anlar (sn) | Gözlem |
|---|---|---|
| 01 | 1,2 · 2,1 · 2,9 | hap `YDT · İLERİ` + `GRAMMAR`; c1 iki satır tam, halka `-ing` üstünde; altyazı `Dil sınavındaki -ing tuzağına düşme.` |
| 02 | 3,4 · 9,0 · 15,0 | 01 sonuyla aynı yer ve metin; künye rozeti `YDT · İLERİ` |
| 03 | 19,5 · 26,6 · 28,3 · 29,1 · 30,5 | `aynı anda` figürlere ve formül kartına binmez; altyazı `Burada while, aynı anda süren iki işi bağlar.` |
| 04 | 33,4 · 38,0 · 42,9 | 33,4'te `is leaking` çiziliyor; altyazı aynı anda İngilizce kökü gösterir (kayma düzeltmesi doğru) |
| 05 | 46,2 · 52,5 · 54,9 | 52,5'te `yarın` dairesi; altyazı `Yarın sabah İzmir'e gidiyoruz. Planlı gelecek. …` |
| 06 | 59,0 · 63,5 · 68,7 · 72,6 · 77,0 · 80,9 · 83,0 · 85,3 · 87,0 · 88,1 | R4 iki satır figürün solunda; `always + V-ing` kutusu temiz; altyazı her karede 2 satır; Kod kartı ve `genellikle` okunur |

## 4. Çakışma kapısı

```
$ node araclar/cakisma-kapisi.mjs present-continuous-ileri-dikey --port 41333 --sunucu 41022 --json ~/is/duz3-0201I/kapi-dikey.json
02: çakışma yok
01: cg:path0 × cg:text1 (-ing halkası × satır 2) hata — kasıtlı halka (ana pakette de aynı çift)
03: aynı anda × cizgi (790,1038 157×36) hata — ölçüm yanlış pozitifi, aşağıda
04: ev × uncle's, kucuk-ev × uncle's hata; are stay-ing × is leak-ing uyarı — sahne içeriği değişmedi (kayma yerel kareyi korur)
05: 50,07–55,07 arası 7 hata, 4 uyarı (takvim, otobüs, kart sözcükleri) — sahne içeriği değişmedi
06: bw × xk (yanlış cümle × kırmızı çarpı) 5 hata; ing × s1:path2/3 (-ing × üstündeki çarpı) 2 hata; kn1/kn2 × s2:path3 (know-ing × üstü çizgi) 2 hata;
    br, al2 × al3 renk dilimleri uyarı; k2b × k2g uyarı → `genellikle` 22 px yukarı alındı, yeniden koşu (`--sahne 06`): k2b × k2g yok
→ çıkış 1
```

Sahne 03 yanlış pozitifi: kapı Paper.js kutularını `window.__kalemKutu.paperTopla()` ile toplar; bu kanca `item.bounds` kullanır ve
`topla` ile 0,42'ye küçülen grubun dönüşümünü uygulamaz. Ölçüm (`sahne-kare.mjs --png 0 --olc`, t 30,0): konuşan figürün çizgileri
`{x 635, y 1022, w 312, h 350}` olarak bildirildi; karede figür x 560–735, y 940–1120 aralığındadır, `aynı anda` (x 776–996) ile arasında
boşluk vardır (`k/duz3/03-paperjs-ornek1-30.5.png`). Toplanan grubun ölçeksiz kutusu orta bandın tamamını (x 80–1000, y 936–1370)
kapladığı için kart dışındaki her yazı bu kuralı tetikler. Düzeltme yeri ölçüm kancasıdır (grup dönüşümü); istem kapsamı dışında.

## 5. Açık kalanlar

| Madde | Sebep |
|---|---|
| mp4 bayat | render yasak; `calistir.sh` güncel (03 `N=472`, 06 `KARE=1022`) |
| `paperTopla` grup dönüşümü | ölçüm aracı kusuru; sahne 03 yanlış pozitifi |
| 04, 05 eski çakışmaları | sahne içeriği bu işte değişmedi |
| `youtube.json`, `youtube-aciklama.md` | yatayla aynı (ana rapor §6); `utm_content=dikey-tam` korundu |

---
Son Güncelleme: 16.11.2026 (DUZ3-0201I oturumu).
