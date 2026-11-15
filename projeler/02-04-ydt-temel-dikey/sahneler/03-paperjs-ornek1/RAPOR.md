# 03-paperjs-ornek1 (DİKEY) — RAPOR (15.11, render yok)

Motor: Paper.js · 1080×1920 · 30 fps · 721 kare (içerik 709 + 12 geçiş) · t_bas 20,22 · t_son 43,85 · cümle 3.
Tema: koyu

| Dosya | Yazan | Not |
|---|---|---|
| `SPEC.md` | şef | yerleşim, olay listesi, kurallar, kabul |
| `kalem-paper.js` | agy (§A) | taban yatay 02-04 s03; dikey künye + altyazı, `kucul`, `yazi/cumle/altCizgi` → öğe, `desc`, `donus` |
| `sahne-03.js` | agy (§B) | içerik; şef düzeltmesi (tur 1): altçizgi payı ve satır aralığı |
| `calistir.sh`, `sayfa.html` | şef | 02 kalıbı (homebrew koşullu, `Y=$(yuk1)`, `ONIZLE_YALNIZ`, yakalama 1080 1920) |

## Ekran düzeni

```
y 352 ┌ ÜST ŞERİT (32,2'den) ──────────────────────────────┐  wears → GENERAL        [mont 83×100]
  472 └─────────────────────────────────────────────────────┘
  380 ┌ KART A (20,77 → 32,2 söner) ┐      490 ┌ KART B (32,15'ten) ─────────┐
      │ She wears her coat     478  │          │ She is wearing her     588  │
      │ in the winter.         570  │          │ pink T-shirt today.    680  │
      │ Kışın montunu giyer.   680  │          │ Bugün pembe tişörtünü… 790  │
  724 └─────────────────────────────┘      830 └─────────────────────────────┘
  750  MONT 367×440                        871  TİŞÖRT 420×378
 1296  GENERAL (Caveat 80) + altı          1340 RIGHT NOW (Caveat 80) + altı
```

Çift kart kuralı (BRIEF-DIKEY §2.5): kart A grubu 350–360. karede üst şeride doğru küçülür (pivot 48,380, ölçek 0,3) ve söner;
şerit `wears → GENERAL` + mont simgesi 354–373. karede çizilir. Kart A grubu sönünce opaklığı 0 kalır (çakışma kapısı saymaz).

## Olay listesi (yerel kare = round((t − 20,22) × 30))

| # | Olay | Kare | t (sn) | Cümle sözcüğü |
|---|---|---|---|---|
| 1 | kart A kutusu | 17 | 20,77 | 3:0 Birinci |
| 2 | kart A cümle sözcük sözcük + karaoke | 120–167 | 24,22–25,78 | 3:5 She … 3:11 winter. |
| 3 | mont çizimi (11 darbe) | 144 | 25,02 | 3:8 coat |
| 4 | TR 1 el yazısı | 197 | 26,79 | 3:12 Kışın … 3:14 giyer. |
| 5 | odak *in the winter* | 250 | 28,55 | 3:15 Her |
| 6 | GENERAL el yazısı | 303 | 30,31 | 3:18 Genel |
| 7 | GENERAL altçizgisi | 334 (biter 348) | 31,35 | 3:20 geniş |
| 8 | kart A küçülür + söner | 350–360 | 31,89–32,22 | 3:21 zaman. bitişi |
| 9 | şerit kutusu | 354 | 32,02 | — |
| 10 | şerit mont simgesi | 356 | 32,09 | — |
| 11 | kart B kutusu | 358 (biter 366) | 32,15 | EN2 She öncesi 0,26 sn |
| 12 | şerit `wears` | 361 | 32,25 | — |
| 13 | şerit ok | 363 | 32,32 | — |
| 14 | şerit GENERAL | 364 | 32,35 | — |
| 15 | kart B cümle + karaoke | 366–417 | 32,41–34,13 | EN2 (yatay ölçüm) |
| 16 | tişört çizimi (4 darbe) | 402 | 33,63 | EN2 T-shirt |
| 17 | TR 2 el yazısı | 454 | 35,37 | 3:22 Bugün … 3:25 giyiyor. |
| 18 | odak *today* (678'de `ikincil`e döner) | 539 | 38,17 | 3:28 bugüne |
| 19 | RIGHT NOW el yazısı | 565 | 39,05 | 3:30 konuşma |
| 20 | RIGHT NOW altçizgisi | 637 | 41,45 | 3:33 Şimdiki |
| 21 | *is* altçizgisi | 678 | 42,81 | 3:35 is |
| 22 | *-ing* altçizgisi | 685 (biter 699) | 43,05 | 3:36 wearing. |

Bütün olaylar cümle 3 içinde ve SON = 708'den önce biter. Son karede 3 sarı belirteç (RIGHT NOW, *is*, *-ing*).

## Kapı (`araclar/qa-yerel.sh 02-04-ydt-temel-dikey 03-paperjs-ornek1 31.85,38.9,43.6 43.6 --hazirla`)

Tur 2 (son), çıkış kodu 0:
```
== HAZIRLA
önizleme hazır
== KAPI
03-paperjs-ornek1 | çakışma yok (96 örnek, 5434 kutu)
== KARE (açık)  31.85 · 38.9 · 43.6
== KARE (koyu)  43.6
kapı çıkış kodu: 0
```

| Tur | Sonuç | Düzeltme |
|---|---|---|
| 1 | rc 0, çakışma yok | gözle: *today* altçizgisi y kuyruğuna, *-ing* altçizgisi g kuyruğuna ≈ 2 px → pay `desc + 8` → `desc + 13` (kalem-paper `altCizgi` + sahne `altY`); kart satır aralığı 86 → 92 (1. satır kuyruk altçizgisi 2. satırın T/t üstüne değmesin) |
| 2 | rc 0, çakışma yok | kusur yok |

## Bakılan kareler

| Kare | Bulgu |
|---|---|
| `k/03-paperjs-ornek1-31.85.png` | kart A tam: 2 satır cümle, *in the winter* altı, TR 1; mont 440 px bant ortasında; GENERAL + sarı altı; altyazı cümle 3 TR dilimi. Taşma yok. |
| `k/03-paperjs-ornek1-38.9.png` | şerit `wears → GENERAL` + mont simgesi; kart B + TR 2; *today* sarı altı; tişört 420 px. Altyazı "Bu yalnız bugüne ait…" (düzeltilmiş dilim). |
| `k/03-paperjs-ornek1-43.6.png` | son düzen; RIGHT NOW + altı, *is* ve *-ing* altı sarı, *today* altı gri. Altçizgiler kuyruğa ve alt satıra değmiyor (yakın kırpma ile bakıldı). Bant 352–1365 dolu, 1536 altı boş. |
| `k/koyu/03-paperjs-ornek1-43.6.png` | koyu tema: krem mürekkep, turuncu vurgu; okunur. |
| ek (scratchpad): 20,9 · 25,4 · 32,0 · 32,15 · 32,3 · 32,6 · 34,0 · 42,0 | kart A çizimi, karaoke + mont darbesi, geçişte kart A küçülüp söner, şerit ve kart B sırayla çizilir; boş kare yok. |

## agy koşu özetleri

- §A `kalem-paper.js`: `/home/sef/.claude/canavar/agy-filo/20261115-121129` (gemini-3.8-flash-high, 274 sn, başarılı).
- §B `sahne-03.js`: `/home/sef/.claude/canavar/agy-filo/20261115-121132` (gemini-3.8-flash-high, 172 sn, başarılı).
- İki koşunun "değişen" listesinde başka sahnelerin dosyaları da görünür; bunlar aynı ağaçta eşzamanlı çalışan öbür oturumların
  yazımıdır (05, s1, s3). Bu sahnenin koşuları yalnız kendi dosyasını yazdı (diff ile bakıldı).

## Açık noktalar

1. **Ortak altyazı kayması (ortak açığı):** `ortak/anlatim/altyazi.json` cümle 3'te EN `She is wearing her pink T-shirt today.`
   35,37–38,49 yazılı (gerçek 32,41–34,55); TR parçası 38,65'te başlıyor (gerçek `Bugün` 35,37). Kaynak: `sozcukler.json`'da cümle 3
   parça 4 yok. Sahne `S.K.altyazi`yı kendi içinde düzeltti (EN2 + `s3` zamanlarıyla 4 dilim). Kalıcı çözüm `altyazi.json` /
   `sozcuk_uret.py` tarafında; düzelince sahnedeki blok kaldırılabilir. Sahne 08 (cümle 9) aynı açığa düşer.
2. **Kart A çerçevesi 3,45 sn boş:** BRIEF §3 kartı 20,77'de (`Birinci`) ister; ilk sözcük 24,22. 4 sn sınırının altında, §0'daki
   "en çok 0,6 sn önce" kuralının üstünde. BRIEF satırı uygulandı; Nadir isterse kutu 23,6'ya çekilir.
3. **Satır aralığı 92:** BRIEF §2.6 86 der; kuyruklu sözcük altçizgisi alt satıra değdiği için 92 seçildi (iki kartta aynı).
4. **olaylar.json yok:** `ONIZLE_YALNIZ=1` yakalama yapmaz; ses olayları render koşusunda üretilir.
5. Sözleşme (`.claude/docs/sozlesme.md`) güncellenmedi: istem kapsamı yalnız sahne dizini. Eklenmeye değer: Paper.js çift kart
   geçişi `oge({kucul, alfa})` + `yazi({oge})` (öğe grubuna `kalemTur` yazılmaz); altçizgi payı `desc + 13`.
