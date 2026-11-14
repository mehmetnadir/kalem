# Sahne 14 — Kapanış (02-04 YDT temel, HyperFrames, 431 kare, t_bas 251,27; cümle 18; son sahne, geçişsiz)

Durum: P2 yazıldı. `ONIZLE_YALNIZ=1` hazırlığı koşuldu, son koşu AÇIK tema. Render yok. Kapı GEÇTİ (çıkış kodu 0, çakışma yok).
Tema: acik (koyu kare ayrıca çekildi).
Dosyalar: `uret.py` · `olay.py` · `yardim.py` · `calistir.sh` · `proje/index.html` · `olaylar.json` (16 ses olayı, 6 çizgi).

## İçerik (BRIEF §3 No 14)

| Öğe | Biçim |
|---|---|
| MEANING FIRST | Fredoka 700, 112 px, mürekkep; sözcük sözcük kinetik (`back.out(1.6)`); altında sarı el çizgisi (sahne 07 belirtecinin geri dönüşü) |
| Numara halkaları 1 · 2 · 3 | "üç soru" derken kalemle; ikincil çizgi, numara mürekkep |
| 3 soru satırı | Caveat 700, 88 px; `general or now?` · `permanent or temporary?` · `timetable or plan?`; seçenekler mürekkep, `or` ikincil; her parça söylendiği anda soldan yazılır |
| Sonraki ders kartı (02-05) | el kutusu (ikincil) · `Next lesson` (Lexend 500, 36 px, ikincil) · `Stative Verbs` (Fredoka 700, 72 px) · sarı ok |
| Künye | sol üst `SIMPLE PRESENT vs PRESENT CONTINUOUS · YDT BASIC`, sağ üst `Next lesson`, ajanda etkin Trap (02-03 sahne 14 ile aynı) |

Renk: tek vurgu (`RENK["vurgu"]`, temaya göre `hf_tema.py` çevirir): alt çizgi ve ok. Yeşil yok (doğru şık yok), kırmızı yok, emoji yok.
Ölçüler `u()` ile oran; en küçük yazı 36 px (taban 30). Ekran metni senaryo §78 "ekran metni" sütunuyla aynı.
Yerleşim: sol blok (başlık + 3 satır, x 220) · sağda kart (x 1220–1780, satır bloğunun dikey ortası). Tek kolon ortalama yok (klişe 7).

## Olay listesi (kare = sahne içi; sn = yerel (küresel))

| Olay | Kare · zaman | Cümle 18 sözcüğü (sıra) |
|---|---|---|
| MEANING (kinetik) | 16 · 0.55 (251.82) | Dil (0) |
| FIRST (kinetik) | 26 · 0.87 (252.14) | sınavında (1) |
| sarı alt çizgi MEANING FIRST | 40 · 1.35 (252.62) | boşluğu (2) |
| numara halkaları 1-2-3 (0,12 sn ara) | 69 · 2.31 (253.58) | üç (4) |
| soru 1: general | 105 · 3.51 (254.78) | Genel (7) |
| soru 1: or | 117 · 3.91 (255.18) | mi, (8) |
| soru 1: now? | 132 · 4.39 (255.66) | şu (9) |
| soru 2: permanent | 158 · 5.27 (256.54) | Kalıcı (12) |
| soru 2: or | 172 · 5.75 (257.02) | mı, (13) |
| soru 2: temporary? | 184 · 6.15 (257.42) | geçici (14) |
| soru 3: timetable | 211 · 7.03 (258.30) | Tarife (16) |
| soru 3: or | 228 · 7.59 (258.86) | mi, (17) |
| soru 3: plan? | 240 · 7.99 (259.26) | plan (18) |
| kart çerçevesi | 271 · 9.03 (260.30) | Sonraki (20) |
| Next lesson | 283 · 9.43 (260.70) | derste (21) |
| Stative | 297 · 9.91 (261.18) | -ing (22) |
| Verbs | 324 · 10.79 (262.06) | fiilleri (24) |
| sarı ok (ileri) | 337 · 11.23 (262.50) | görüyoruz. (25) |

Sapma 0,00 sn: her olay sözcüğün t0'ında (`T(i, bas)` sözcük kayarsa durur). Hareket 0,55–11,53 sn; ilk 12 ve son 12 kare durgun
(`Y.kontrol`). Yazma süreleri bir sonraki parçadan önce biter. Anlatım 264,14'te biter, son hareket 262,80'de durur; "Görüşürüz."
(263,42) olaysız (karşılığı olan görsel yok).

## Kapı

Komut: `bash araclar/qa-yerel.sh 02-04-ydt-temel 14-hyperframes-kapanis 256.0,260.1,263.6 262.9 --hazirla`
Son çıktı satırları:

```
== KAPI
14-hyperframes-kapanis | çakışma yok (55 örnek, 5890 kutu)
...
kapı çıkış kodu: 0
```

1. koşu (rc 0, 3 uyarı): `q00 × q01` 12×36 px, `q10 × q11` ve `q20 × q21` 10×36 px. Sebep: `" or "` parçası boşlukla başlıyordu; ölçüm
   kutusu boşluktan başlar, önceki sözcüğün son harf kuyruğu (Caveat `l`, `t`, `e`) oraya taşar. Düzeltme: parçalar boşluksuz,
   aralık `SORU_ARA` = Caveat boşluk genişliği + 8 px. 2. koşu: çakışma yok.

## Bakılan kareler ve bulgu

| Kare | Ne görünür | Bulgu |
|---|---|---|
| `k/14-hyperframes-kapanis-256.png` | başlık + alt çizgi, 3 halka, 1. satır tam | sorun yok |
| `k/14-hyperframes-kapanis-260.1.png` | 3 satır tam, kart yok | sorun yok |
| `k/14-hyperframes-kapanis-263.6.png` | son düzen: 3 satır + kart + ok | sorun yok; 2. satır ile kart arası ~90 px |
| `k/koyu/14-hyperframes-kapanis-262.9.png` | koyu tema son düzen | kontrast yeterli, sorun yok |

Taşma, kesilen yazı, üst üste binme, boş kare yok. Düzeltme turu: 1 (kapı uyarısı).

## Açık noktalar

1. **sahne-kare zamanı küresel saniyedir.** İstem "sahne içi saniye" der; `araclar/sahne-kare.mjs` `t`'yi anlatım saniyesi alır
   (sahne 07 raporundaki bulgu). Komuta küresel değer verildi (yerel 4,73 / 8,83 / 12,33 / koyu 11,63).
2. **Kod yazım yolu.** Yazma kapısı (`write-size-gate.sh`) 15+ satırlık `.py` yazımını engeller. `uret.py` şef taslağı
   (`/tmp/kalem0204-s14/uret.spec.md`) olarak yazıldı, taslak dosya yazmadan çalıştırılıp denendi, `agy-filo tek --rol kod`
   dosyaya geçirdi (gemini-3.8-flash-high, 32 sn), `cmp` bayt bayt eşit. Sonraki düzeltme (boşluk) küçük Edit ile yapıldı.
   İstemdeki "alt ajan açma" kuralı: Claude alt ajanı açılmadı; kapının gösterdiği agy yolu kullanıldı (sahne 07 ile aynı).
3. `yardim.py` 02-04 sahne 07 kopyası (değişiklik yok); `olay.py` 02-04 sahne 07 kopyası (değişiklik yok).
4. `zaman.json` bu sahnede `kare` 431, `icerik_kare` 401 (13,37 sn = anlatım sonu + 0,5 sn kuyruk). `uret.py` süreyi `kare`den alır
   (02-03 sahne 14 kalıbı); 401. kareden sonrası durgun son düzendir. Birleştirme kuyruğu 0,5 sn keserse görüntü değişmez.
5. Sağ üst bölüm etiketi ve kart başlığı ikisi de `Next lesson` (02-03 sahne 14 ile aynı). İstenirse sağ üst başka bir şablon
   sözcüğüne çevrilir (ör. bölüm adı); şimdilik örnekle tutarlı bırakıldı.
6. Birim testi yok (02-03 / 02-04 HF sahneleri test taşımıyor); doğrulama kapı + kare. Render yapılmadı (`video.mp4`, `kontrol.png` yok).
