# 02-paperjs-ornek — RAPOR v2 (huni v2) · 02-04-ydt-temel-s2 Shorts · 15.11 · render yok

| Alan | Değer |
|---|---|
| Motor | Paper.js · 1080×1920 · 30 fps |
| Kare | 449 (içerik 437 + geçiş 12) · t_bas 2,84 · t_son 17,41 · cümle 2 |
| Yerleşim | huni v2 §2: kanal katmanı 280–350 · künye 360–450 · içerik 460–1380, x 60–960 · altyazı 1400–1550 |
| Tema | açık (varsayılan) + koyu (modül) |
| Kapı | `qa-yerel.sh … 2.84,10.1,17.35 14.9 --hazirla` → **çıkış 0** · `cakisma-kapisi.mjs --sahne 02-paperjs-ornek --port 41333 --sunucu 41022` → **çıkış 0, çakışma yok** (60 örnek, 4160 kutu) |
| Metin taraması | `tam ders|dakika` (html, js, py, json; `k/` hariç) → boş |
| Düzeltme turu | 0 (ilk koşu geçti) |
| mp4 | YOK (`calistir.sh` yalnız `ONIZLE_YALNIZ=1` ile koştu) |
| v1 yedeği | `~/Silinecekler/2026-11-15-huni-v2/02-04-ydt-temel-s2/sahneler/02-paperjs-ornek/` (`cp -a`); v1 kareleri `…/02-paperjs-ornek-k-v1-yerinde/` |

## Dosyalar

| Dosya | Yazan | Not |
|---|---|---|
| `sahne-02.js` | agy (`agy-filo tek --rol kod`, gemini-3.8-flash-high, 213 sn) | v1 yerinde uyarlandı; şef baştan sona okudu, düzeltme gerekmedi |
| `SPEC.md` | şef | v2 tasarımı (v1 SPEC yedekte) |
| `kalem-paper.js` | şef (3 küçük Edit) | `sahneKur({…, kunye})` kancası: `kunye(ctx, K)` zorunlu, `kunyeCiz` (v1 HUD) importu ve çağrısı kalktı |
| `sayfa.html`, `calistir.sh`, `nesneler.json` | değişmedi | `calistir.sh` zaten koşullu Homebrew PATH, `Y=$(yuk1)`, yakalama `1080 1920` |

agy koşu özeti: `/home/sef/.claude/canavar/agy-filo/20261115-185512`. Özetteki "değişen" listesinde başka paketlerin dosyaları
görünür (`02-04-ydt-temel-dikey/…`, `sozlesme.md`); bunlar paralel oturumların işidir (`agy-filo tek` bütün çalışma ağacını tarar).

## Ekran düzeni (y px)

```
 280–350  [logo x 53,2 y 291–339 h 48] @ydspublishing (Lexend 700 42, x 263, taban 330) — her karede, alfa 1
 360–450  Simple Present vs Present Continuous (Fredoka 700 34, x 60, taban 420) [YDT · BASIC] (hap 661–863, y 386–434)
 ~476–552 Genel mi, şu an mı?   (Caveat 700 72, x 60, taban 530; kare 0'dan hazır; 14,14'te mürekkep altçizgi)
 576–768  KART 1: She wears her coat / in the winter.   (Fredoka 64; mont sağ alt köşe; kutu çizgisi x 60–960)
 ~790–855 Simple Present (Lexend 500 64)  ……  GENERAL (Caveat 64, sağa hizalı, mürekkep sağ ucu ≈ 958)
 876–904  zaman çizgisi 1: eksen + ok · 4 gri kış bandı + kar tanesi · now noktası bantlar arasında (x 454)
 ~917–944 now
 920–1000 [MEANING] sarı hap, kart 2 üst çizgisinin sağ ucunda (x 585–936)
 960–1170 KART 2: She is wearing her / pink T-shirt today.   (tişört sağ alt köşe; today halkası)
 ~1190–1236 Present Continuous (Lexend 500 64, x 60)
 ~1256–1300            RIGHT NOW (Caveat 64, x ≈ 602) ← halkadan tek ince mürekkep ok
 1290–1342 zaman çizgisi 2: eksen + ok · gri today bandı + 2 uç çentiği · now noktası bandın içinde, nabız
 ~1343–1370 now
 1380 ─ içerik sonu · 1400–1536 altyazı (modül) · 0–280 ve 1570–1920 boş
```

## Olay listesi (kare = round((t − 2,84) × 30); t küresel sn)

| # | Olay | t (sn) | Kare | Çapa (cümle 2 sözcüğü) |
|---|---|---|---|---|
| 1 | Soru satırı hazır (sahne 01 devri) | — | 0 | — |
| 2 | Kart 1 kutusu | 3,24 | 12 | She − 10 (geçiş payı 12) |
| 3 | Kart 1 sözcükleri + karaoke | 3,39–4,67 | 17–55 | 2:0 She … 2:6 winter. |
| 4 | Mont kalemle | 4,27 | 43 | 2:3 coat |
| 5 | `odak` *in the winter* (sarı) | 4,47 | 49 | 2:4 in |
| 6 | `GENERAL` | 5,56 | 82 | 2:7 Genel → 2:8 durum: |
| 7 | Zaman çizgisi 1: eksen + ok ucu | 6,04 | 96 / 107 | 2:8 durum: |
| 8 | now noktası 1 / `now` | 6,31 / 6,44 | 104 / 108 | durum: + 8 / + 12 |
| 9 | `Simple Present` | 6,68 | 115 | 2:9 geniş |
| 10 | 4 kış bandı + kar tanesi | 7,00–7,47 | 125–143 | 2:10 zaman. |
| 11 | odak 1 söner | 8,37 | 166–174 | EN2 She |
| 12 | Kart 2 kutusu | 8,04 | 156 | EN2 She − 10 |
| 13 | Kart 2 sözcükleri + karaoke | 8,37–10,13 | 166–219 | EN2 (sabit dizi) |
| 14 | Tişört kalemle | 9,65 | 204 | EN2 T-shirt |
| 15 | `odak` *today* (sarı) | 10,13 | 219 | EN2 today. |
| 16 | today halkası (sarı; odak *today* söner) | 11,42 | 257 | 2:11 Today |
| 17 | `MEANING` hapı + soru altçizgisi; halka mürekkebe döner | 14,14 | 339 / 341 | 2:17 anlam |
| 18 | `RIGHT NOW` | 15,25–15,94 | 372–395 | 2:19 Konuşma → 2:20 anı: |
| 19 | Zaman çizgisi 2: eksen + ok ucu | 15,38 | 376 / 385 | Konuşma + 4 |
| 20 | Halka → `RIGHT NOW` oku | 15,73 | 387 | Konuşma bitişi |
| 21 | now noktası 2 + nabız / `now` | 15,81 | 389 / 392 / 395 | 2:20 anı: |
| 22 | `Present Continuous` | 16,49 | 410 | 2:21 şimdiki |
| 23 | today bandı + 2 uç çentiği | 16,62 | 414 / 418 / 421 | şimdiki + 4 |

Olaylar ve çapalar v1 ile aynı. Son hareket ≈ kare 426; modül zamanı 436'da dondurur. En uzun durağan aralık 2,25 sn (halka 11,89 → `MEANING` 14,14).
**EN2 çapaları:** `sozcukler.json`'da yok; BRIEF-S2 DİKKAT notundaki değerler sabit dizi (kaynak yorumu kodda: ElevenLabs önbellek
hizalaması `3e7a9af3….hiz.json` + parça başı 8,37). **Tek sarı zinciri:** karaoke 1 → odak *in the winter* → karaoke 2 → odak *today* →
halka → `MEANING`. `Simple Present`'e ok yok, kart 1'e bağ yok. Kanal katmanı ve künye `kanalCiz(ctx, K)` ile her karede canvas'a
çizilir; `__kalemKutu` kutuları `kunye:kanal`, `kunye:konu`, `kunye:rozet` (tür `kunye`). Çip (`Example`) yok.

## Kapı (son koşu)

```
== HAZIRLA
tema: acik
önizleme hazır
== KAPI
02-paperjs-ornek | çakışma yok (60 örnek, 4160 kutu)
== KARE (açık)
"png":"/home/sef/qa-kare/02-04-ydt-temel-s2/02-paperjs-ornek/02-paperjs-ornek-2.84.png"
"png":"/home/sef/qa-kare/02-04-ydt-temel-s2/02-paperjs-ornek/02-paperjs-ornek-10.1.png"
"png":"/home/sef/qa-kare/02-04-ydt-temel-s2/02-paperjs-ornek/02-paperjs-ornek-17.35.png"
== KARE (koyu)
"png":"/home/sef/qa-kare/02-04-ydt-temel-s2/02-paperjs-ornek/koyu/02-paperjs-ornek-14.9.png"
kapı çıkış kodu: 0
```
Ayrı koşu: `node araclar/cakisma-kapisi.mjs 02-04-ydt-temel-s2 --sahne 02-paperjs-ornek --port 41333 --sunucu 41022` →
`02-paperjs-ornek | çakışma yok (60 örnek, 4160 kutu)`, çıkış 0.

## Bakılan kareler (Read ile)

| Kare | Bulgu |
|---|---|
| `k/…-2.84.png` (kare 0) | kanal katmanı + künye + soru satırı (x 60, taban 530) + altyazı `Genel mi, şu an mı?`; içerik bandı boş |
| `k/ara/…-4.9.png` | kart 1 tam; karaoke ile odak *in the winter* aynı yerde (tek sarı alan); mont çiziliyor |
| `k/ara/…-7.6.png` | `Simple Present` / `GENERAL` tek satırda; kış bantları geliyor; tek sarı odak 1 |
| `k/…-10.1.png` | kart 2 karaokesi `T-shirt` altında; tişört çiziliyor; odak 1 sönmüş |
| `k/ara/…-12.png` | today halkası sarı, tek sarı öğe |
| `k/ara/…-14.6.png` | `MEANING` hapı tek sarı; halka mürekkep; soru satırı altçizgili |
| `k/ara/…-16.1.png` | `RIGHT NOW` yazıldı, ok halkanın sağından yazının üstüne iniyor; now 2 + nabız |
| `k/…-17.35.png` | son durum: iki kart, iki zaman çizgisi; ok `Present Continuous` sağ ucunun ≈ 40 px sağından geçer; `RIGHT NOW` eksen ok ucuna değmez |
| `k/koyu/…-14.9.png` | koyu tema: krem yazı, turuncu hap ve rozet (koyu yazı) okunur; logo şeffaf sürüm |

Kanal katmanı üç karede (2,84 · 10,1 · 17,35) aynı konumda. Taşma, kesik yazı, üst üste binme, okunmaz kontrast, boş kare, altyazıyla
çakışma yok. 0–280 ve 1570–1920 boş; içerik x 960'ın sağına geçmez (en sağ: `GENERAL` ≈ 958, kart çizgisi ≈ 958).

## Açık noktalar

1. **Satır B iki satır:** x 60–960 bandında `Present Continuous` (611 px) + `RIGHT NOW` (≈ 296 px) + 32 aralık sığmaz (999 > 960).
   `RIGHT NOW` `Present Continuous`'un altında, sağda, zaman çizgisi 2'nin üstüne alındı. Satır A (`Simple Present` + `GENERAL`) v1 gibi
   tek satır; iki blok bu yüzden simetrik değil. İstem bu durumu öngörmüyordu; şef kararı.
2. **Rozet hap iç payı 20 px** (genişlik = yazı + 40), yazı tabanı 419: istem ve BRIEF'te değer yok; S1 `ortak/kunye.js` `rozetPay: 20`,
   taban `386 + 24 + 9` ile birebir aynı. Konu boyu ölçümle 34 (hap x 661–863). BRIEF "Yerleşim" tablosuna yazılması önerilir (BRIEF'e dokunulmadı).
9. **Altyazı sağ taşması (paket `ortak/`):** S2 `ortak/kunye.js` `altyaziCiz` W/2 = 540 ortalı, genişlik 984 → uzun parça x ≈ 62–1018
   (koyu 14,9 karesi: "Today iki zamanda da geçebilir; farkı anlam"); 960–1080 platform arayüzü altında kalır. S1 aynı sorunu kendi
   `ortak/kunye.js`'inde çözdü (x 60–960, orta 510; sözleşme 15.11 02-04-s1 s02). S2 `ortak/` bu istemde yasak → şef ayrı istem açmalı.
3. **`kalem-paper.js` kancası:** sahnenin yerel kopyasında `sahneKur` `kunye(ctx, K)` ister; `ortak/kunye.js` değişmedi.
4. **Sahne 01 devri (kare 0):** soru satırı Caveat 700 72, mürekkep, x 60, taban 530, altçizgi yok. Sahne 01 v2 bu oturumda kontrol edilmedi.
5. **Sıkı dikey bütçe:** now 2 tabanı 1370 (bant sonu 1380). Bekçi `AXY2 + NOW_DY + 4 ≤ 1380`. Yazı 64 altına inmedi; kart 1 satır
   aralığı 80 (v1 84), kış bandı 100/200 (v1 110/230, 4 bant).
6. **"karaoke alt bantta":** alt bantta `kunye.js` düz altyazısı; karaoke kart sözcüğünün sarı çizgisiyle (v1 açık nokta 6 ile aynı).
7. **Birleştirme geçişi:** `birlestir.py --gecis BookFlip` sahne sınırında bütün kareyi çevirir; kanal katmanı "animasyon yok" kuralını
   bozar (V2-C-RAPOR açık nokta 4). Şef kararı.
8. `olaylar.json` / `zamanlar.json` render dalında üretilir; render yok. Kovan kaydı açılmadı (istem kapsamı dışı).
