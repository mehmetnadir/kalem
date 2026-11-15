# Sahne 01 · kapak (kanca) · huni v2 — HyperFrames DİKEY 1080×1920, 102 kare, 0,00–3,00 sn + 12 kare geçiş payı

Durum: yazıldı (istem D-V2-S3, 15.11.2026, srv21). Önizleme hazırlığı `ONIZLE_YALNIZ=1` ile koştu. mp4 yok, commit yok.
Kapak A yazıldı: paket kökü `kapak-a.png` + `kapak.png` (cmp aynı), `k/koyu/kapak-a-koyu.png`. Tema: açık (koyu kareyle de denetlendi).
v1 kod, SPEC, RAPOR ve eski kapaklar: `~/Silinecekler/2026-11-15-huni-v2/02-04-ydt-temel-s3/` (kök kapaklar ve koyu kapak yedekle cmp aynıydı).

## Kod yolu

| Adım | Kim | Dosya |
|---|---|---|
| tasarım | şef | `SPEC.md` (v2, delta listesi + ölçü tablosu + uçuş benzetimi) · `zamanlar.json` (`rozet_kay`, `ucus_ayrik` kalktı; `sahne_sol` 0,30) |
| kod | agy tek şerit, rol `kod` (gemini-3.8-flash-high), 323 sn | `uret.py` (v1 yerinde düzenlendi, 1006 satır) |
| okuma + kapı | şef | uret.py baştan sona okundu, SPEC'e uyuyor; düzeltme gerekmedi (0 Edit) |
| küçük değişiklik | şef (Edit) | `calistir.sh`: render dalı artık `kapak-a.png` yazmıyor (mp4 karesinde altyazı var) |

agy koşu özeti: `/home/sef/.claude/canavar/agy-filo/20261115-185456`. "değişen" listesinde `.claude/docs/sozlesme.md` ve
`02-04-ydt-temel-dikey/90-…` dosyaları göründü. Bu dosyaların izni 664; agy 644 ile yazar (`uret.py` 644). Sonuç: aynı worktree'de
paralel oturum yazdı, ajan yalnız `uret.py`'ye dokundu.

## Yerleşim (v2)

```
  291–339  kanal: logo (x 53,15 · w 193,49 · h 48) + @ydspublishing (Lexend 700 42, x 263, taban 330) — 0→102 sabit
  386–434  rozet YDT · BASIC (x 664,6 · w 203,6), 0. kareden son konumda
  466–902  TARİFE (Fredoka 700, B 190, orta 510) · altçizgi 671 · hap ≠ PLAN 700–902
  927–1000 The train to İzmir (taban 986) → uçuşla 568
 1036–1378 saat + leaves + tren (x 60–490) | figür + bilet + am going (x 600–956)
 1400–1550 altyazı (Lexend 500 44, orta 510, taban 1490, tek satır)
Son hal: künye `Simple Present vs Present Continuous` (Fredoka 34, taban 420) + rozet · kart kutu(71, 472, 878, 254) ·
satır 1 taban 568 · satır 2 `leaves at 7` taban 666 · tren [712, 494, 927, 586].
```

## Olay listesi (küresel sn = yerel sn)

| Olay | Küresel sn (kare) | Sözcük |
|---|---|---|
| kapak tam: kanal, rozet, `TARİFE`, hap `≠ PLAN`, saat + tren + `leaves`, bilet tutan figür + `am going` | 0,00 (0) | söz öncesi |
| `TARİFE` altçizgisi (kalem, `sine.inOut`; ses `cizgi`) | 0,30–0,80 (9–24) | söz öncesi |
| altyazı dilimi açılır (`The train to İzmir leaves at 7 pm today.`) | 0,95 (29) | The − 0,05 |
| satır 1 kırpmayla: `The` · `train` · `to` · `İzmir` (`hisirti` 30, 49) | 1,00 · 1,28 · 1,48 · 1,64–1,92 | The 1,00 · train 1,28 · to 1,48 · Izmir 1,64 |
| KAPAK A karesi | 1,97 (59) | — |
| kapak sahnesi solar (`power1.in`) | 2,00–2,30 (60–69) | — |
| uçuş: `TARİFE` → konu ilk yarısı, hap → ikinci yarı, tren → kart köşesi, satırlar −418 (`parilti` 60) | 2,00–2,85 (60–85) | — |
| satır 2: `leaves` · `at` · `7` (`hisirti` 66) | 2,20 · 2,56 · 2,80–2,92 | leaves 2,20 · at 2,56 · seven 2,80 |
| başlıklar solar · konu adı açılır (`tik` 85) | 2,49–2,67 · 2,62–2,85 | — |
| kart 1 çerçevesi 4 kenar (`cizgi` 79) | 2,62–2,90 (79–87) | — |
| durgun; son 12 kare geçiş altında | 2,92–3,40 (88–101) | `p.m.` 3,00 → sahne 02 |

Uçuş eksen ease'leri: `TARİFE` x `power3.out`, y `power3.inOut`; hap x/y `power3.inOut`; tren x `power3.inOut`, y `power2.inOut`.
Tek ease ile şef benzetimi iki çakışma buldu (`TARİFE × hap` 2,47–2,53; `tren × satır 1` 2,50). Bu ease'lerle en dar aralık 24 px.

## Kanal katmanı ölçümü (karede piksel ölçümü, zemine göre mürekkep kutusu)

| Kare | Logo mürekkebi | `@ydspublishing` mürekkebi |
|---|---|---|
| açık 0,00 · 1,50 · 2,97 | x 60–239 · y 298–330 | x 264–595 · y 296–339 |
| koyu 1,97 | x 60–239 · y 298–330 | x 264–595 · y 296–339 |
| `kapak-a.png` · `kapak-a-koyu.png` | x 60–239 · y 298–330 | x 264–595 · y 296–339 |

Görünür sol kenar x 60; logo resmi y 291–339 içinde; yazı tabanı 330 (alt uzantı 339). Altı karede konum aynı. Kodda `#kanal`
hiçbir tween ya da set hedefi değil. Kapıda tür `kunye`, ad `kunye:kanal:image0` / `kunye:kanal:text0` (grupta 2 öğe olduğu için).

## Kart 1 devri (`devir.json`)
Fredoka 700 64, `font-kerning:none`, sol x 97, taban [568, 666]; tam satırlar `The train to İzmir` / `leaves at 7 pm today.`, görünen
`leaves at 7`; 9 sözcüğün x aralığı v1 ile aynı (`pm` 428,8–514,1 · `today.` 529,1–714,3). Kart çerçevesi `kutu(71, 472, 878, 254,
tohum 71)`, çizgi 4. Tren son kutusu [712, 494, 927, 586] (yerel kutu [−10, −24, 420, 158], iç `translate(70 1218)`, uçuş ölçeği 0,5).
Ek alanlar: `kanal`, `kunye` (konu, boy 34, rozet [664,6, 386, 203,6, 48]), `altyazi` (x 510, boy 44, taban [1490]), `altyazi_ekran`.

## Kapı sonuçları

1. QA (`bash araclar/qa-yerel.sh 02-04-ydt-temel-s3 01-hyperframes-kapak 0.0,1.5,2.97 1.97 --hazirla`):
```
== HAZIRLA → olay 7 · önizleme hazır
== KAPI
01-hyperframes-kapak | çakışma yok (13 örnek, 4847 kutu)
== KARE (açık) 0 · 1.5 · 2.97   == KARE (koyu) 1.97
kapı çıkış kodu: 0
```
2. Çakışma kapısı (`--port 41333 --sunucu 41022`): 0 uyarı (yukarıdaki KAPI satırı aynı komut). Ek: `--sikilik 30` (her kare)
   → `çakışma yok (91 örnek, 35062 kutu)`, çıkış 0.
3. Metin taraması `grep -rniE "tam ders|dakika" …/01-hyperframes-kapak/proje` → sonuç yok (rc 1).
4. `uret.py` 7 denetim maddesi assert ile geçti; `olaylar.json` 7 olay (kare 9, 30, 49, 60, 66, 79, 85), hepsi < 90.

## Kapak A
`proje-ka` ve `proje-ka-koyu` v2 `proje/`'den yeniden alındı. Açık kopya `proje/`'den yalnız `#altyazi{display:none !important}` satırıyla
ayrılır (diff 0 satır). Koyu kopya: aynı CSS + `hf_tema.py … koyu` + şeffaf logo (`yds-publishing-seffaf.svg`; snapshot canlı kip
değildir, logo değişimi JS'te kalır). `hyperframes snapshot --at 1.97 --no-end` → `kapak-a.png`, `kapak.png` (cmp aynı),
`k/koyu/kapak-a-koyu.png`; 1080×1920.

## Bakılan kareler (Read) ve bulgu

| Kare | Bulgu |
|---|---|
| `k/01-…-0.png` | kapak tam; taşma, kesik yazı, binme yok; 0–280 ve 1570–1920 boş; x 960 sağı boş |
| `k/01-…-1.5.png` | `The train t` yazım ortasında (beklenen); altyazı tek satır 1457–1501 |
| `k/01-…-2.97.png` | künye satırı + rozet, kart çerçevesi, `leaves at 7`, tren köşede; içerik bandının alt yarısı boş (kart 2 sahne 02'de) |
| `k/koyu/01-…-1.97.png` | koyu tema okunur; kanal yazısı açık renkte |
| kontak (2,1 · 2,2 · 2,3 · 2,45 · 2,62 · 2,75; `~/qa-kare/…/kontak-ucus.png`) | uçuş temiz; 2,2'de tren dumanı solan `leaves` etiketine ≈ 10 px yakın, binme yok (her kare kapısı 0) |
| `kapak-a.png`, `k/koyu/kapak-a-koyu.png` | altyazı yok, kanal var, satır 1 ve altçizgi tam |

Piksel ölçümü (4 QA karesi + 2 kapak): y 0–280 ve 1570–1920 boş; x 962–1080 (y 280–1570) boş. Düzeltme turu gerekmedi.
k/ içindeki v1 kalıntıları (0.2, açık 1.97, 2.95, `ara/*`, `ara/koyu/*`) aynı adla v2 kareleriyle yeniden çekildi.

## Açık noktalar
1. Sahne 02 kare 0 (salt okundu, 19:05): sahne 02 `uret.py` (19:00) bu sahnenin değerlerini kullanıyor — kart `kutu(71, 472, 878,
   254, 71)`, tren [712, 494,5, 927, 585,5] (`translate(717 506.5) scale(0.5)`, non-scaling-stroke), altyazı x 510 / taban 1490.
   Sahne 02 `SPEC.md` (18:52) hâlâ eski seçimi yazar (`kutu(70, 472, 880, 254)`, tren [719, 492, 934, 583]); kod doğru, belge bayat.
2. Rozet iç boşluğu 20 + 20 (genişlik 203,6): BRIEF ve istem yazmıyor; sözleşmedeki S1 kaydı da pay 20 (taban 419; burada 419,4).
3. Altyazı: x 510, Lexend 500 44, taban 1490; sözcük vurgusu yok (sözcük zamanı karttaki kırpmayla). Sahne 02 aynı dilimi aynı
   biçimde göstermeli (`devir.json` `altyazi`); ortak `altyazi.json` hâlâ ses metni (`Izmir`, `seven p.m.`), dönüşüm sahne içinde.
4. Koyu temada hap ve rozet dolgusu `#f2a93b` (tema değeri `vurguDolgu`); açık temada `#ffe066`.
5. v1 koyu kapak lacivert logo taşıyordu (koyu zeminde zayıf); v2'de şeffaf logo.
6. `zaman.json`, `ortak/`, BRIEF ve başka sahnelere dokunulmadı.
