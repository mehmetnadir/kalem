# 02-paperjs-ornek — RAPOR (15.11, istem D-S1; render yok)

Motor: Paper.js · 1080×1920 · 30 fps · 522 kare (içerik 510 + geçiş 12) · t_bas 3,00 · t_son 19,99 · cümle 1 (sonu) + cümle 2.
Tema: acik + koyu (kapı açık; kare koyu 16,0)

## Yapım

| Adım | Kim | Çıktı |
|---|---|---|
| Tasarım + spec | şef | `SPEC.md` (yerleşim, 24 olay, API, kurallar, kabul) |
| Kalem modülü | şef | `kalem-paper.js` (present-continuous-ileri-s1 kopyası; değişiklikler aşağıda) |
| `sayfa.html`, `calistir.sh`, `bavul.svg`, `nesneler.json` | şef | `ONIZLE_YALNIZ=1` dalı satır 10; bavul = ana ders 04 `BAVUL_SVG` |
| Sahne betiği | agy-filo `tek --rol kod` (gemini-3.8-flash-high, 302 sn, 1 tur, başarılı) | `sahne-02.js`; özet `/home/sef/.claude/canavar/agy-filo/20261115-120738/ozet.md` |
| İnceleme | şef | baştan sona okundu, spec'e uyuyor; 2 küçük Edit (aşağıda) |
| Kapı + kare | şef | `qa-yerel.sh` 2 koşu, ikisi de çıkış 0 |

`kalem-paper.js` değişiklikleri (yalnız bu kopya): yollar `02-04-ydt-temel-s1` · altyazı `kunye.js` `altyaziMetin` (dilimleme
kunye.js'te; örneğin yerel `altyaziSec`'i kalktı, sahne 01/03 ile aynı altyazı) · `yazi` kapı etiketi (`kalemTur: yazi`) + `oge`
grubuna bağlanma (öğe kayınca yazı kayar) · `svgCiz` "/" ile başlayan tam yol · `altCizgi` `alt` payı + kapı etiketi `isaret` ·
`KUNYE` dışa aktarımı.

Şef Edit'leri (`sahne-02.js`): 1) çip yazı öğelerine kapı etiketi (`metinOge.g.data`): grup içindeki yazının kutusu yerel
koordinatta kalıyordu, kapı kaymış çipi yanlış yerde ölçerdi. 2) Kare turu 1 bulgusu: 8,42 sn'de çip 1 sönen `yaşı-` parçasının
üstünden geçiyordu → sönme `[G0, G0+8]`, kayma `GK0 = G0+6`'da başlar (`SPEC.md` §5 notu).

agy özetindeki "değişen" listesinde bu sahne dışı 11 dosya var (`02-04-ydt-temel-dikey/...`, `01-hyperframes-kapak/...`,
`.claude/docs/sozlesme.md`): filo düzeyinde atıf, paralel oturumların işi. Bu sahne dizininde agy yalnız `sahne-02.js` yazdı
(öteki dosyaların mtime'ı agy koşusundan önce).

## Olay ↔ sözcük (yerel kare = round((t − 3,00) × 30); zaman `sozcukler.json`'dan `al()` ile)

| # | Olay | Kare | Cümle:sözcük (t0 sn) |
|---|---|---|---|
| 1 | İki TR satırı hazır (sahne 01'den), Caveat 80 | 0 | — |
| 2 | Karaoke altçizgi: satır 2 `yaşı-yor-um.` | 12 (geçiş sonrası) | 1:3 yaşıyorum. (3,08) |
| 3 | ek_ayir: satır 1 *yor* sarı kutu | 29 | 1:4 Türkçede (3,96) |
| 4 | ek_ayir: satır 2 *yor* sarı kutu | 86 | 1:7 yaşıyorum. (5,56) + 9 kare (*yor* hecesi) |
| 5 | TR parçaları yukarı solar · iki çip ayrılır (çip 1 kart 1'in, çip 2 kart 2'nin üstüne) | 156–164 / 162–177 | 2:2 ayrılır. (8,19) |
| 6 | Kart 1 kutusu | 172 | 2:3 I (9,08) − 10 |
| 7 | `I live in İstanbul.` sözcük zamanlı + karaoke altçizgi | 182 · 190 · 194 · 199 | 2:3–6 I live in Istanbul. |
| 8 | `odak` *live* (kalıcı sarı altçizgi) | 190 | 2:4 live (9,32) |
| 9 | `bag` çip 1 → *live* | 194 | 2:5 in (9,48) |
| 10 | Ev ikonu (kart 1 sağ üst, 100 px) | 199 | 2:6 Istanbul. (9,64) |
| 11 | Soluk TR `Hep orada.` (kalemle) | 245–279 | 2:7–8 Hep orada: (11,17–12,29) |
| 12 | `PERMANENT` | 281 | 2:9 kalıcı (12,37) |
| 13 | Zaman çizgisi 1: eksen + ok | 293 | 2:10 durum, (12,77) |
| 14 | now noktası / `now` | 301 / 305 | durum, + 8 / + 12 |
| 15 | Uzun bant, now bandın içinde | 308 | 2:11 geniş (13,25) |
| 16 | Kart 2 kutusu | 341 | 2:13 I (14,70) − 10 |
| 17 | `I am living` / `with my uncle.` + karaoke | 351 · 357 · 361 · 370 · 375 · 382 | 2:13–18 |
| 18 | `odak` *am living* | 361 | 2:15 living (15,02) |
| 19 | `bag` çip 2 → *am living* | 370 | 2:16 with (15,34) |
| 20 | Bavul ikonu (kart 2 sağ üst, 100 px) | 382 | 2:18 uncle. (15,74) |
| 21 | Soluk TR `Şimdilik.` | 391–420 | 2:19 Şimdilik: (17,03–17,99) |
| 22 | `TEMPORARY` | 422 | 2:20 geçici (18,07) |
| 23 | Zaman çizgisi 2: eksen + ok · now · `now` | 434 / 442 / 446 | 2:21 durum, (18,47) |
| 24 | Kısa bant + 2 uç çentiği, now bandın içinde | 451 / 457 · 460 | 2:22 şimdiki (19,03) |

Son hareket kare 465'te biter; kare 509–521 durgun. İki görsel değişim arası en uzun boşluk 2,6 sn (5,86 → 8,19).

## Kapı (son koşu, son satırlar)

```
== HAZIRLA
önizleme hazır
== KAPI
02-paperjs-ornek | çakışma yok (69 örnek, 3249 kutu)
== KARE (açık)
"png":"/home/sef/qa-kare/02-04-ydt-temel-s1/02-paperjs-ornek/02-paperjs-ornek-6.png"
"png":"/home/sef/qa-kare/02-04-ydt-temel-s1/02-paperjs-ornek/02-paperjs-ornek-13.8.png"
"png":"/home/sef/qa-kare/02-04-ydt-temel-s1/02-paperjs-ornek/02-paperjs-ornek-19.6.png"
== KARE (koyu)
"png":"/home/sef/qa-kare/02-04-ydt-temel-s1/02-paperjs-ornek/koyu/02-paperjs-ornek-16.png"
kapı çıkış kodu: 0
```

## Bakılan kareler (Read ile)

| Kare | Bulgu |
|---|---|
| `k/ara/…-3.png` (kare 0) | yalnız iki TR satırı + HUD + altyazı; sahne 01 son karesiyle eşleşmesi gereken durum |
| `k/ara/…-3.5.png` | karaoke altçizgi satır 2 `yaşı-yor-um.` altında; harfe değmiyor |
| `k/…-6.png` | satır 1 *yor* kutusu tam, satır 2 kutusu çiziliyor (beklenen) |
| `k/ara/…-8.3.png`, `…-8.5.png`, `…-8.7.png` | 2. tur: TR parçaları sönerken çipler yerinde; kayma yazı söndükten sonra; üst üste binme yok |
| `k/ara/…-9.95.png` | kart 1 cümlesi, odak + karaoke altçizgi, bag oku *live* üstünde, ev çiziliyor |
| `k/…-13.8.png` | kart 1 bloğu tam; çip 2 kart 2 yerinde bekliyor |
| `k/ara/…-15.75.png` | kart 2 sözcük zamanlı geliyor; bag 2 çiziliyor |
| `k/…-19.6.png`, `k/ara/…-19.95.png` | son durum: iki kart, iki zaman çizgisi; içerik 378–1366 (bandın %94'ü); 1536 altı boş; altyazı bandında yalnız altyazı |
| `k/koyu/…-16.png` | koyu tema: krem yazı, turuncu belirteçler okunur; bavul çiziliyor |

Taşma, kesik yazı, üst üste binme, okunmaz kontrast, boş kare yok. 1. tur bulgusu (8,42 sn çip × sönen yazı) 2. turda düzeldi;
1. tur karesi `~/Silinecekler/2026-11-15-0204/02-paperjs-ornek-8.42-tur1.png` altına taşındı.

## Açık noktalar

1. **Sahne 01'e devir (kare 0):** iki satır `İstanbul'da yaşı-yor-um.` / `Amcamla yaşı-yor-um.` · Caveat 700 80 px · `RENK.murekkep` ·
   sol x 72 · taban y 470 / 590 · *yor* kutusu YOK, altçizgi YOK. Sahne 01'in uçuş sonrası konumu bu ölçüye uymalı (sahne 01 dizini bu
   istem sırasında boştu; ölçü sahne 02'de tanımlandı, örnek `uret.py` kalıbı).
2. **"karaoke alt bantta" yorumu:** alt bantta `kunye.js` altyazısı (düz; kunye.js karaoke çizmez). Karaoke kart sözcüğünün sarı
   altçizgisiyle (03.11 kararı: karaoke şeridi yok). Alt bantta sözcük vurgusu istenirse `ortak/kunye.js` işi (kapsam dışı).
3. **Altyazı kaynağı:** dikey örnek sahne içi `altyaziSec` kullanıyordu; burada `kunye.js` `altyaziMetin` (cümle 1 altyazısı iki satır
   tüm cümle). Sahne 01 ve 03 aynı kaynağı kullanırsa geçişte altyazı sıçramaz.
4. **İkon boyu:** ev ve bavul 100 px (istem: "kart köşesinde küçük"); BRIEF-DIKEY §3 figür/nesne 420–560 kuralı uygulanmadı.
5. **Kapı ölçüm riski (modül geneli):** `paperTopla` grup içindeki öğenin kutusunu grubun yerel koordinatında okur; `kay` alan
   öğede kutu kaymayı görmez. Bu sahnede çip öğesi etiketlendi; ortak örneklerde de aynı risk var.
6. `olaylar.json` / `zamanlar.json` render dalında üretilir; render yok, dosyalar yok.
