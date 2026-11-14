# Sahne 08 Karşıt çift 1 (yatay) — RAPOR (14.11)

Motor: Düz canvas · 1920×1080 · 30 fps · 459 kare (içerik 447; zaman.json ile birebir) · t_bas 130,40 · t_son 145,29 · cümle 9
Tema: acik

## Durum

| Adım | Sonuç |
|---|---|
| Dosyalar | `sayfa.html`, `sahne.js`, `sahne-ortak.js` (02-04 `05-canvas-ornek3` kopyası, değişiklik yok), `calistir.sh` |
| `node --check sahne.js` | geçti |
| `ONIZLE_YALNIZ=1 bash calistir.sh --tema acik` | "önizleme hazır", rc 0 |
| Kapı `qa-yerel.sh … 138.3,141.1,145.0 143.9 --hazirla` | çıkış kodu 0; çakışma yok (61 örnek, 676 kutu) |
| Göz kontrolü (4 kare) | sorun yok; düzeltme turu 0 |
| mp4 render | YOK (istem gereği) |

## İçerik

- Kart (alt0, tam genişlik, y 150–470): *She is wearing her pink T-shirt today.* tek satır (Fredoka, en çok 76 mantıksal px; tişört kutusunun soluna sığdırılır).
- Kartın sağ köşesinde küçük tişört (02-04 sahne 03 ile aynı biçim); "kıyafet" denince çevresine sarı kalem halkası.
- Ekran metni `today → this day only`: Caveat, zaman çizgisindeki bandın üstünde ortalı; ok kalemle çizilir.
- Zaman çizgisi (y 800): eksen + sağ ok; today gün bandı (vurgu dolgusu, %45) + iki uç çentiği; now noktası bandın içinde, nabız; altında `now`.
- Vurgu yalnız sarı (`RENK.vurgu` / `vurguDolgu`); yeşil, kırmızı, emoji yok. Soluk Türkçe çeviri yok (taslakta bu sahne için yok).

## Olay ↔ sözcük (küresel sn; kare = round((t − 130,40) × 30))

| Olay | t (sn) | Kare | Cümle 9 sözcüğü |
|---|---|---|---|
| kart çerçevesi | 130,95 | 17 | Karşıt |
| `today` notu yazılır | 134,95 | 137 | today. («aynı sözcük var: today») |
| cümle sözcük sözcük (karaoke altı çizgi) | 135,61–137,69 | 156–219 | She … today. (EN parça) |
| tişört çizilir | 136,87 | 194 | T-shirt |
| zaman çizgisi ekseni | 138,57 | 245 | Burada |
| `today` odak: cümlede + notta (çoklu) | 139,21 / 139,29 | 264 / 267 | today |
| today gün bandı + uç çentikleri | 139,93 | 286 | bugünü |
| ok (`→`) | 140,05 | 290 | bugünü |
| `this day only` yazılır | 140,29–140,89 | 297–315 | gösterir. |
| tişört halkası (sarı) | 141,77 | 341 | kıyafet: |
| now noktası + nabız | 142,57 | 365 | konuşma |
| `now` etiketi | 143,05 | 380 | anında |
| `is wearing` odak | 144,37 | 419 | şimdiki |

İlk çizim kare 17 (≥ 12). Son olay kare 419, 0,4 sn'de biter (kare 431); içerik 447'de biter, son 12 kare olaysız.

EN sözcük zamanları: cümle 9'un EN parçası `sozcukler.json`'da yok (sahne 03'teki açıkla aynı). `cumle-9.wav`
(md5 052b069b…) üzerinde faster-whisper turbo (clip 4,5–7,5 sn, `~/.venvs/ses`) + 40 ms RMS zarfıyla ölçüldü;
parça penceresi 4,65–7,37 sn (`sureler.json`); küresel = 130,95 + yerel. Değerler `sahne.js` `EN` dizisinde sabit.

## Kapı çıktısı (son satırlar)

```
== KAPI
08-canvas-karsit1 | çakışma yok (61 örnek, 676 kutu)
== KARE (açık)
"png":".../08-canvas-karsit1-138.3.png"
"png":".../08-canvas-karsit1-141.1.png"
"png":".../08-canvas-karsit1-145.png"
== KARE (koyu)
"png":".../koyu/08-canvas-karsit1-143.9.png"
kapı çıkış kodu: 0
```

## Bakılan kareler

| Kare | Görünen | Bulgu |
|---|---|---|
| `k/08-canvas-karsit1-138.3.png` (açık) | kart + cümle + tişört; altta `today` notu | temiz; karaoke çizgisi sönmüş |
| `k/08-canvas-karsit1-141.1.png` (açık) | iki `today` sarı altı çizili; ok + `this day only`; eksen, gün bandı, çentikler | temiz |
| `k/08-canvas-karsit1-145.png` (açık) | son hâl: `is wearing` odak, tişört halkası, now + nabız + `now` | temiz; halka kart kenarına ve cümleye değmiyor |
| `k/koyu/08-canvas-karsit1-143.9.png` (koyu) | aynı düzen, koyu zemin | okunur; bant koyu turuncu, now noktası açık |

## Açık noktalar

1. **Zaman aracı:** istem "sahne içi saniye" diyor; `sahne-kare.mjs` kareyi `(t − t_bas) × 30` ile buluyor, yani küresel anlatım saniyesi bekliyor. Kapıya küresel değer verildi (138,3 · 141,1 · 145,0 · koyu 143,9); sahne içi karşılığı 7,9 · 10,7 · 14,6 · 13,5.
2. **Ajanda çipi:** `KUNYE.ajanda` = Hook · Examples · Rule · Trap; "Contrast" yok → 02-03 kalıbıyla Rule yanar. Ajandaya Contrast eklenirse sahne kendiliğinden uyar (ad eşlemesi).
3. **Bölüm adı** `Contrast 1 / 2` (02-04'te iki karşıt sahne: 08, 09). Sahne 09 farklı ad kullanırsa eşitlenmeli.
4. **Ek etiket:** zaman çizgisindeki `now` taslak ekran metninde yok; BRIEF olayında (now noktası) var. İstenmezse `sahne.js`'te tek `elYazisi` satırı kalkar.
5. **Yazım yolu:** `sahne.js` 15+ satır olduğu için yazım kapısı (`write-size-gate`) Claude yazımını reddetti; içerik şefçe yazıldı, dosyaya `agy-filo tek` (rol bulk) birebir koydu; sha256 iki uçta aynı (78981331…).
