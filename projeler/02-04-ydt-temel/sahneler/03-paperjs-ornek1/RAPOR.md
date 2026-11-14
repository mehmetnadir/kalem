# 03-paperjs-ornek1 — RAPOR (14.11, P2; render yok)

Motor: Paper.js · 1920×1080 · 30 fps · 721 kare (içerik 709 + 12 geçiş) · t_bas 20,22 · t_son 43,85 · cümle 3.
Tema: acik
Dosyalar: `sayfa.html` · `sahne-03.js` · `kalem-paper.js` (02-03 sahne 03 kopyası; yollar 02-04, `yazi()` kutusu kapıya görünür) ·
`calistir.sh` (homebrew koşullu, `Y=$(yuk1)`, geçici kareler `~/Silinecekler/2026-11-14-0204/`).

## Ekran düzeni

```
┌ sol kart (120–940) ───────────────┐ ┌ sağ kart (980–1800) ───────────────┐
│ [mont]   GENERAL                   │ │ [tişört]  RIGHT NOW                │
│          ‾‾‾‾‾‾‾ (geniş)           │ │           ‾‾‾‾‾‾‾‾‾ (Şimdiki)      │
│ She wears her coat                 │ │ She is wearing her                 │
│ in the winter.                     │ │ pink T-shirt today.                │
│ ‾‾‾‾‾‾‾‾‾‾‾‾‾ (Her kış)            │ │    ‾‾    ‾‾‾      ‾‾‾‾‾ (is·ing·bugüne) │
│ Kışın montunu giyer. (soluk)       │ │ Bugün pembe tişörtünü giyiyor.     │
└────────────────────────────────────┘ └────────────────────────────────────┘
```

Ekran metni senaryo §4 satır 3 ile aynıdır: 2 EN cümle, 2 soluk TR çeviri, GENERAL / RIGHT NOW (Caveat). Ek metin yok.
Ölçüler `u()` ile mantıksal px; EN Fredoka 700 sığdırmalı (≤ 64), TR Caveat ≤ 46, etiket Caveat ≤ 84; taban 30'un üstünde.
Renk: metin ve çizim `murekkep`, TR `ikincil`, altçizgiler tek vurgu `RENK.vurgu`, karaoke `vurguDolgu`. Kırmızı, yeşil, emoji yok.

## Olay listesi (yerel kare = round((t − 20,22) × 30))

| Olay | Kare | t (sn) | Cümle sözcüğü |
|---|---|---|---|
| sol kart kutusu (kalem) | 17 | 20,77 | 3:0 Birinci |
| sağ kart kutusu | 57 | 22,13 | 3:2 Fiil |
| `kart` sol: sözcük sözcük + karaoke altçizgi | 120–167 | 24,22–25,78 | 3:5 She … 3:11 winter. |
| `cizim` mont (11 darbe) | 144 | 25,02 | 3:8 coat |
| TR 1 el yazısı (sözcük penceresi) | 197–248 | 26,79 | 3:12 Kışın … 3:14 giyer. |
| `odak` *in the winter* | 250 | 28,55 | 3:15 Her (kış) |
| GENERAL (Caveat) | 303–334 | 30,31 | 3:18 Genel |
| GENERAL altçizgisi | 334 | 31,35 | 3:20 geniş |
| `kart` sağ: sözcük sözcük + karaoke | 366–417 | 32,41–34,13 | parça 4 She … today. (ölçüm, aşağıda) |
| `cizim` tişört (4 darbe) | 402 | 33,63 | parça 4 T-shirt (ölçüm) |
| TR 2 el yazısı | 454–517 | 35,37 | 3:22 Bugün … 3:25 giyiyor. |
| `odak` *today* | 539 | 38,17 | 3:28 bugüne |
| RIGHT NOW (Caveat) | 565–596 | 39,05 | 3:30 konuşma · 3:31 anında |
| RIGHT NOW altçizgisi | 637 | 41,45 | 3:33 Şimdiki |
| `yakin_cekim` *is* (altçizgi; dar öbek, 13.11 QA) | 678 | 42,81 | 3:35 is |
| *-ing* altçizgisi | 685 (biter 699) | 43,05 | 3:36 wearing. |

Bütün olaylar cümle 3 içinde ve SON = 708'den önce biter. Son 12 kare durgun.

## Kapı (araclar/qa-yerel.sh … 32.2,37.6,43.6 43.6 --hazirla)

Tur 3 (son), çıkış kodu 0:
```
== HAZIRLA
önizleme hazır
== KAPI
03-paperjs-ornek1 | çakışma yok (96 örnek, 7091 kutu)
== KARE (açık)  32.2 · 37.6 · 43.6
== KARE (koyu)  43.6
kapı çıkış kodu: 0
```
Not: araç `t` değerini anlatım saniyesi (t_bas…t_son) olarak okur (`sahne-kare.mjs` f = (t − t_bas) × 30). Sahne içi
saniye verilirse kare 0'a düşer; bu yüzden 32.2 / 37.6 / 43.6 (yerel kare 359 / 521 / 701) verildi.

| Tur | Sonuç | Düzeltme |
|---|---|---|
| 1 | ölçüm hatası, "sahne hazır olmadı" | `daire()` `tur` alanını dönüş sayısı sayar; düğmeye `tur: "cizim"` verilince nokta dizisi boş kaldı → düğme kendi noktalarıyla `ciz()` |
| 2 | rc 0, çakışma yok | gözle 2 kusur: 3. düğme sol cebe değiyor; *today* ve *wearing* altçizgisi y/g kuyruğunun içinden geçiyor → cepler y 96, düğmeler 48/64/80; altçizgi taban + 0,3 em |
| 3 | rc 0, çakışma yok | kusur yok |

## Bakılan kareler

| Kare | Bulgu |
|---|---|
| `k/03-paperjs-ornek1-32.2.png` | sol kart tam: mont, GENERAL + altçizgi, cümle 2 satır, *in the winter* odak, TR; sağ kart boş çerçeve. Taşma yok. |
| `k/03-paperjs-ornek1-37.6.png` | sağ cümle, tişört, TR 2 tamam; etiket henüz yok (konuşma anında gelir). |
| `k/03-paperjs-ornek1-43.6.png` | son durum: iki etiket, *is* ve *-ing* altçizgisi, *today* odak. Altçizgiler kuyruğa değmiyor. |
| `k/koyu/03-paperjs-ornek1-43.6.png` | koyu tema: krem mürekkep, turuncu vurgu, TR soluk ama okunur. |
| ek (`/tmp`): 25.3 · 34.4 | çizim sürüyor, karaoke okunan sözcükte; boş kare yok. |

## Açık noktalar

1. **Ortak açığı (sözcük zamanı):** `sozcukler.json`'da "She is wearing her pink T-shirt today." 2 yerde yok: cümle 3 parça 4
   (bu sahne) ve cümle 9 parça 2 (sahne 08). Bu sahnede başlar `cumle-3.wav` (md5 4658616c44b6…) üzerinde faster-whisper turbo
   sözcük zamanı + 40 ms RMS zarfıyla ölçüldü, `sahne-03.js` `EN2` sabitine yazıldı (She 32,41 · is 32,63 · wearing 32,77 · her 33,07 ·
   pink 33,35 · T-shirt 33,63 · today. 34,13; konuşma 34,55'te biter). Kalıcı çözüm `sozcuk_uret.py` / sentez tarafında.
2. **Karaoke altçizgisi** (`kalem-paper.js altCizgi`, taban + 0,16 em) *today* sözcüğünde y kuyruğunu 1 sn geçer. Paket ortak
   davranışı olduğu için değiştirilmedi; odak altçizgileri kuyruğun altına alındı.
3. **Pakette mont/tişört çizimi yok** (`ortak/cizim`): iki giysi sahne içinde kalem darbesiyle çizildi (`MONT`, `TISORT`).
4. **`kalem-paper.js` notu:** 02-03 sürümünde `yazi()` metni çakışma kapısına görünmüyordu (kutu türü yok); bu kopyada `yazi` türüyle
   ölçülür. `daire()` içindeki `tur` (dönüş sayısı) ile `ciz()` `tur`u (kutu türü) aynı adı taşır; sahnede `daire()` kullanılmadı.
5. **Süreç notu:** yazma kapısı 15 satırdan uzun kod yazımını engelledi; kodu şef yazdı (`/tmp` metin), `agy-filo tek` dosyayı birebir
   kopyaladı, `cmp` aynı. İstemdeki "alt ajan açma" kuralıyla çelişki; sonraki düzeltmeler 15 satır altında doğrudan yapıldı.
6. Sözleşme (`.claude/docs/sozlesme.md`) güncellenmedi: istem kapsamı yalnız sahne dizini. Eklenmeye değer: Paper.js sahnesinde
   `yazi()` kapı türü, `qa-yerel.sh` t = anlatım saniyesi.
