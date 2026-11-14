# 02-paperjs-kanca — RAPOR (14.11, P2; render yok)

Motor: Paper.js · 1920×1080 · 30 fps · 529 kare (içerik 517 + geçiş 12) · t_bas 3,00 · t_son 20,22 · cümle 1 (sonu) + cümle 2.
Tema: acik

## Yapım

| Adım | Kim | Çıktı |
|---|---|---|
| Tasarım + spec | şef (Claude) | `SPEC.md` (olay, yerleşim, API, kabul) |
| Kalem modülü | şef | `kalem-paper.js` (02-03 kopyası, 02-04 yolları + 4 ek, aşağıda) |
| Sahne betiği | agy-filo `tek --rol kod` (gemini-3.8-flash-high, 200 sn, başarılı) | `sahne-02.js`; özet `/home/sef/.claude/canavar/agy-filo/20261114-221618/ozet.md` |
| İnceleme | şef | 2 düzeltme (Edit/sed): kart metni "Istanbul." → "İstanbul." (ekran sütunu); bant ve "=" çizgilerine uç inceltme (`uc0/uc1/amp`) |
| Kapı + kare | şef | `araclar/qa-yerel.sh` çıkış 0 (ilk koşuda) |

agy özetindeki "değişen" listesinde `04-canvas-ornek2/sahne.js` ve `06-hyperframes-soru1/SPEC.md` var: filo düzeyinde atıf;
ikisi de paralel oturumların kendi SPEC'li işidir (mtime 22:19, kendi SPEC.md'leri). Bu sahneden dışarı yazım yok.

`kalem-paper.js` ekleri (yalnız bu sahnenin kopyası): `yazi` ve `svgCiz` kapı etiketi (`kalemTur` yazi/cizim), `altCizgi` isaret
etiketi; `yazi(o.matris, o.son)` kareye bağlı dönüşüm ve gizlenme; `sahneKur({dersGoster})` künye ders yazısını iniş anına kadar kırpar
ve kapı kutusundan çıkarır; `KUNYE` dışa aktarımı.

## Olay ↔ sözcük t0 (yerel kare = round((t − 3,00) × 30))

| # | Olay | Kare | Cümle:sözcük (t0 sn) |
|---|---|---|---|
| 1 | İki Türkçe satır hazır (01'den gelir), 1. satır *yor* sarı kutuda | 0 | — |
| 2 | 2. satır *yor* sarı kutu | 12 (geçiş sonrası; sözcük 2) | 1:3 yaşıyorum. (3,08) |
| 3 | "=" üst çizgi (satırlar arası) | 55 | 1:5 ikisi (4,84) |
| 4 | "=" alt çizgi | 67 | 1:6 de (5,24) |
| 5 | Sol kart kutusu kalemle | 103 | 2:0 I (6,91) − 14 kare |
| 6 | Sol kart sözcükleri + karaoke altı çizgi | 117–136 | 2:0–3 I live in Istanbul. |
| 7 | bag oku: sol *yor* → *live* | 168 | 2:4 Biri (8,60) |
| 8 | SIMPLE / PRESENT (sol kart altı) | 182 / 192 | 2:5 geniş (9,08) · 2:6 zaman. (9,40) |
| 9 | Sağ kart kutusu | 217 | 2:7 I (10,69) − 14 |
| 10 | Sağ kart sözcükleri + karaoke | 231–262 | 2:7–12 I am living with my uncle. |
| 11 | bag oku: sağ *yor* → *am living* | 296 | 2:13 Öteki (12,86) |
| 12 | PRESENT / CONTINUOUS (sağ kart altı) | 315 / 328 | 2:14 şimdiki (13,50) · 2:15 zaman. (13,94) |
| 13 | `vs` ortada | 385 | 2:18 iki (15,82) |
| 14 | Başlık künyeye uçar (5 parça kendi künye yerine) → künye ders yazısı açılır | 392–410 | 2:19 zamanın (15,98) |
| 15 | İki uçlu sarı fark oku (kartların altı) | 428 | 2:22 farkını (17,26) |
| 16 | MEANING + sarı belirteç (yazının alt yarısı) | 483 / 488 | 2:25 anlam (19,26) · belirteç 2:26 belirler. (19,58)'de biter |

Son 12 kare (517–528) durgun.

## Kapı (son çıktı)

```
== HAZIRLA
önizleme hazır
== KAPI
02-paperjs-kanca | çakışma yok (70 örnek, 1725 kutu)
kapı çıkış kodu: 0
```
Komut: `bash araclar/qa-yerel.sh 02-04-ydt-temel 02-paperjs-kanca 5.8,9.9,14.6,16.9,20.1 14.6 --hazirla`.
Not: `sahne-kare.mjs` zamanı ANLATIM saniyesi olarak alır (t_bas…t_son); istemdeki "sahne içi saniye" yerine bu yüzden anlatım
saniyesi verildi (5,8 = yerel 2,8 sn).

## Bakılan kareler

| Kare | Görülen | Bulgu |
|---|---|---|
| `k/02-paperjs-kanca-5.8.png` | iki TR satırı, iki *yor* kutusu, "=" | temiz |
| `k/02-paperjs-kanca-9.9.png` | sol kart, bag oku, SIMPLE PRESENT | temiz |
| `k/02-paperjs-kanca-14.6.png` | iki kart, iki bag oku, iki ad | temiz; ok uçları fiilin üstünde |
| `k/02-paperjs-kanca-16.9.png` | künye ders yazısı yerinde, adlar gitti | temiz |
| `k/02-paperjs-kanca-20.1.png` | fark oku + MEANING belirteçli | temiz |
| `k/koyu/02-paperjs-kanca-14.6.png` | koyu tema, 14,6 | okunur; *yor* bandı koyu turuncu, yazı krem |
| `k/ek/02-paperjs-kanca-7.5.png` | karaoke (*in* altı sarı) | temiz |
| `k/ek/02-paperjs-kanca-16.2.png` | uçuşun başı | parçalar kart alt kenarından geçer (0,6 sn hareket, kapı saymaz) |
| `k/ek/02-paperjs-kanca-16.66.png` | inişten 1 kare önce | künye yerine ~4 px yakın; sonraki karede künye ile değişir |
| `k/ek/koyu/02-paperjs-kanca-20.1.png` | koyu MEANING | okunur |

Taşma, kesik yazı, üst üste binme, boş kare yok. Düzeltme turu: 0 (kapı ilk koşuda geçti; inceleme düzeltmeleri kapıdan önce).

## Açık noktalar

1. Sahne 01'in son karesi bilinmiyor (paralel üretim): bu sahne iki TR satırını iki sütunda, 1. *yor* kutusu hazır başlatır. 01
   satırları üst üste bitiriyorsa BookFlip geçişi farkı örter; birleştirmede bakılmalı.
2. Künye (logo, ajanda, "Hook") sahne başından görünür; yalnız sol üst ders yazısı başlık inene kadar (kare 410) gizli.
3. Koyu temada *yor* bandı üstünde krem yazı karşıtlığı orta (göz kararı okunur, ölçülmedi).
4. Uçuş başında adlar kart alt kenarından geçiyor; istenirse uçuş önce yukarı değil yana açılacak biçimde eğrilir.
