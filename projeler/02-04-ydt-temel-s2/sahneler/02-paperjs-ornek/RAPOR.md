# 02-paperjs-ornek — RAPOR (02-04-ydt-temel-s2 Shorts · 15.11 · render yok)

| Alan | Değer |
|---|---|
| Motor | Paper.js · 1080×1920 · 30 fps |
| Kare | 449 (içerik 437 + geçiş 12) · t_bas 2,84 · t_son 17,41 · cümle 2 |
| Tema | açık (varsayılan) + koyu (modül) |
| Kapı | `qa-yerel.sh … 7.9,14.9,17.3 14.9 --hazirla` → **çıkış 0**, çakışma yok (60 örnek, 4220 kutu) |
| Düzeltme turu | 2 (tur 1 bekçi, tur 2 göz) |
| mp4 | YOK (istem gereği; `calistir.sh` yalnız `ONIZLE_YALNIZ=1` ile koştu) |

## Dosyalar

| Dosya | Yazan | Not |
|---|---|---|
| `sahne-02.js` | agy (`agy-filo tek --rol kod`, gemini-3.8-flash-high, 294 sn) + şef Edit | şef düzeltmeleri: `BET` 72 → 64, today halkası, ok yolu, bir yorum satırı |
| `SPEC.md` | şef | tasarım; son koda göre güncel |
| `kalem-paper.js` | şef | S1 sahne 02 kopyası; yalnız iki import yolu `02-04-ydt-temel-s2` |
| `sayfa.html`, `calistir.sh`, `nesneler.json` | şef | S1 kopyası; 449 kare, t_bas 2.84, paket adı |

agy koşu özeti: `/home/sef/.claude/canavar/agy-filo/20261115-125352`. Özetteki "değişen" listesinde başka sahnelerin dosyaları da
görünür; bunlar paralel oturumların işidir (sözleşme: `agy-filo tek` bütün çalışma ağacını tarar). Bu koşu yalnız `sahne-02.js`'i yazdı.

## Ekran düzeni

```
 352 ─ HUD altı
 ~360–455  Genel mi, şu an mı?  (Caveat 700 80, x 72, taban 430; 14,14'te mürekkep altçizgi)
 478–678   KART 1: She wears her coat / in the winter.   (Fredoka 64; mont sağ alt köşe)
 700–770   Simple Present (Lexend 500 64)  ……  GENERAL (Caveat 64, sağa hizalı)
 806–834   zaman çizgisi 1: eksen + ok · 4 gri kış bandı + kar tanesi · now noktası bantlar arasında
 ~850–886  now
 872–952   [MEANING] sarı hap, kart 2 üst çizgisinin sağ ucunda
 912–1122  KART 2: She is wearing her / pink T-shirt today.   (tişört sağ alt köşe; today halkası)
 1146–1200 Present Continuous  ……  RIGHT NOW · halkadan RIGHT NOW'a tek ince mürekkep oku
 1224–1280 zaman çizgisi 2: eksen + ok · gri today bandı + 2 uç çentiği · now noktası bandın içinde, nabız
 ~1290–1318 now
1392 ─ içerik sonu · 1400–1536 altyazı (modül) · 1536–1920 boş
```

İçerik 360–1318: bandın %92'si. Tek sütun, kenar 48, satır ≤ 24 karakter, en küçük yazı 64 px.

## Olay listesi (kare = round((t − 2,84) × 30))

| # | Olay | t (sn) | Kare | Çapa |
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
| 10 | 4 kış bandı + kar tanesi | 7,00–7,49 | 125–145 | 2:10 zaman. |
| 11 | odak 1 söner | 8,37 | 166–174 | EN2 She |
| 12 | Kart 2 kutusu | 8,04 | 156 | EN2 She − 10 |
| 13 | Kart 2 sözcükleri + karaoke | 8,37–10,13 | 166–219 | EN2 (sabit dizi, aşağıda) |
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

Son hareket kare ≈ 426'da biter; modül zamanı 436'da dondurur, 437–448 durgun. En uzun durağan aralık 2,25 sn (halka
11,89'da biter → 14,14 `MEANING`; ses "iki zamanda da geçebilir").

**EN2 çapaları (kart 2):** `sozcukler.json`'da yok. Değerler BRIEF-S2 DİKKAT notundan: ElevenLabs önbellek hizalaması
`~/.local/share/elevenlabs-onbellek/3e7a9af3….hiz.json` + parça başı 8,37 (`sureler.json` cümle 2 `parcalar[2][0]` 4,98 + 3,39).
`her` 9,21 değeri aynı hizalamadan türetildi (brief tablosunda yok). Kaynak kod yorumunda yazılı.

**Tek sarı zinciri:** karaoke 1 (odak 1 ile aynı yerde birleşir) → odak *in the winter* → karaoke 2 → odak *today* → today halkası
→ `MEANING`. Her sarı, bir sonrakinin başladığı karede 8 karede söner. Bantlar, eksenler, kar, now noktası, oklar ve soru
altçizgisi sarı değil. `Simple Present`'e ok yok, kart 1'e bağ yok.

## Kapı (son koşu, tur 3)

```
== HAZIRLA
tema: acik
önizleme hazır
== KAPI
02-paperjs-ornek | çakışma yok (60 örnek, 4220 kutu)
== KARE (açık)
"png":"/home/sef/qa-kare/02-04-ydt-temel-s2/02-paperjs-ornek/02-paperjs-ornek-7.9.png"
"png":"/home/sef/qa-kare/02-04-ydt-temel-s2/02-paperjs-ornek/02-paperjs-ornek-14.9.png"
"png":"/home/sef/qa-kare/02-04-ydt-temel-s2/02-paperjs-ornek/02-paperjs-ornek-17.3.png"
== KARE (koyu)
"png":"/home/sef/qa-kare/02-04-ydt-temel-s2/02-paperjs-ornek/koyu/02-paperjs-ornek-14.9.png"
kapı çıkış kodu: 0
```

| Tur | Sonuç | Düzeltme |
|---|---|---|
| 1 | rc 2, "sahne hazır olmadı (sayaç yok)" | CDP ile `/log` gövdesi okundu: bekçi `Present Continuous ile RIGHT NOW çakışıyor (714,9 > 687,1)`. Lexend 500 64 = 611 px, Caveat 72 `RIGHT NOW` = 333 px → `BET` 72 → 64 (iki etiket paralel kalsın) |
| 2 | rc 0, çakışma yok | gözle 2 kusur: today elipsi `T-shirt`'ün son `t`'sini kesiyor; ok başı `RIGHT`'ın `I`'sına düşüyor (`RÎGHT` okunuyor) → süper elips halka + ok halkanın sağından yukarı bombe yapıp yazının üstüne iner |
| 3 | rc 0, çakışma yok | kusur yok |

## Bakılan kareler (Read ile)

| Kare | Bulgu |
|---|---|
| `k/ara/…-2.84.png` (kare 0) | yalnız soru satırı + HUD + altyazı `Genel mi, şu an mı?`; sahne 01 son karesiyle eşleşmesi gereken durum |
| `k/ara/…-4.9.png` | kart 1 tam, karaoke ile odak *in the winter* aynı yerde (tek sarı alan); mont çiziliyor |
| `k/…-7.9.png` | kart 1 bloğu tam: `Simple Present` / `GENERAL`, kış bantları + kar, now bantlar arasında; tek sarı odak 1 |
| `k/ara/…-10.6.png` | kart 2 tam, tişört çizildi; odak *today* `y` kuyruğunun ≈ 2 px altında (büyütülmüş kesitle ölçüldü, değmiyor) |
| `k/ara/…-12.png` | today halkası sarı (açık temada `RT.vurgu` tonu), tek sarı öğe; odak 1 ve 2 sönmüş |
| `k/…-14.9.png` | `MEANING` hapı kart 2 çizgisinin üstünde, tek sarı; halka mürekkep; soru satırı mürekkep altçizgili |
| `k/ara/…-16.1.png` | `RIGHT NOW` yazıldı, ok yazıya değmeden üstüne iniyor; now noktası + nabız halkası; `now` yazılıyor |
| `k/…-17.3.png` | son durum: iki kart, iki zaman çizgisi, today bandı now'ı sarıyor; 1536 altı boş; altyazı bandında yalnız altyazı |
| `k/koyu/…-14.9.png` | koyu tema: krem yazı, turuncu hap (koyu yazı) okunur; gri bantlar görünür |

Taşma, kesik yazı, üst üste binme, okunmaz kontrast, boş kare, altyazı bandına giren öğe yok.

## Açık noktalar

1. **Sahne 01'e devir (kare 0):** soru satırı `Genel mi, şu an mı?` · Caveat 700 80 px · `RENK.murekkep` · sol x 72 · taban y 430 ·
   altçizgi YOK. Sahne 01'in uçuş sonrası konumu bu ölçüye uymalı. Sahne 01 dizini bu oturumda başka bir oturumun elindeydi
   (`01-hyperframes-kapak/SPEC.md`, `uret.py`); dokunulmadı.
2. **"today sarı daire" biçimi:** halka yuvarlak köşeli kutuya yakın süper elips. Sebep: `T-shirt` ile `today.` arasında yalnız
   ≈ 16 px boşluk var; sözcüğü saran elips komşu harfi kesiyor. Gerçek daire istenirse sözcük aralığı açılmalı (kart cümlesi değişir).
3. **Bant rengi:** kış bantları ve today bandı `RT.ikincil` %35 (ana ders sahne 08'de sarıydı). Sebep: tek sarı kuralı; 16,62'de
   `MEANING` hapı sarıyken today bandı sarı olsaydı ikinci sarı olurdu.
4. **Etiket boyu:** `GENERAL` / `RIGHT NOW` Caveat 64 (alt sınırda). 72'de satır B sığmıyor (bekçi ölçümü).
5. **Vurgu tonu:** odaklar ve hap `RT.vurguDolgu` (açık `#ffe066`), halka `RT.vurgu` (açık `#d9900f`, `daire()` kalemiyle aynı).
   İkisi aynı sarı ailesindendir, aynı anda görünmez.
6. **"karaoke alt bantta":** alt bantta `kunye.js` düz altyazısı (karaoke çizmez); karaoke kart sözcüğünün sarı çizgisiyle (S1 açık nokta 2).
7. `olaylar.json` / `zamanlar.json` render dalında üretilir; render yok, dosyalar yok.
8. srv21 kovan defteri Mac kopyasının eski hâli (D-0096'da biter); ayrışmasın diye bu iş için kayıt açılmadı.
