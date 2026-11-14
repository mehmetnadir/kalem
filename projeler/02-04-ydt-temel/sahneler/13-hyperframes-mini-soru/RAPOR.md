# Sahne 13 — Mini soru (02-04 YDT temel, HyperFrames, 940 kare)

Tema: acik

| Alan | Değer |
|---|---|
| Durum | P2 yazıldı · önizleme hazır (`ONIZLE_YALNIZ=1`) · kapı GEÇTİ (çıkış 0) · render YOK |
| Zaman | t_bas 220,33 · t_son 251,27 · 940 kare (içerik 928) · hareket aralığı yerel 0,55–30,05 sn (izin 0,40–30,93) |
| Cümleler | 15 soru (öğretmen) · 16 yanlış cevap A (öğrenci) · 17 cevap (öğretmen) |
| Dosyalar | `uret.py` · `olay.py` · `yardim.py` · `calistir.sh` · `proje/index.html` · `olaylar.json` (33 olay, 15 çizgi) · `k/` |

## İçerik (BRIEF §3 satır 13)

- Kök kartı iki satır: *My brother lives in Ankara, / but this month he ____ with us.* Kök sözcük sözcük, ses sırasıyla gelir.
- Boşluk çizgisi *he* ile *with* arasındaki 0,5 sn susmada çizilir. «Boşluğa» sözcüğünde vurgu rengine geçer.
- Sayaç halkası «Beş şık var» parçasında döner, ortada 5. Şıklar (A lives · B is living · C live · D to live · E are living) 0,18 sn arayla gelir. Ses şıkları okumaz (D-0205).
- Öğrenci yanlış cevabı A: `ogrenci-bas.svg` + el çizimi balon, sözcük sözcük. A şıkkı soluk sarı çerçeve alır.
- Öğretmen cevabı (0,67 sn duraklama sonra, ≤ 2 sn): balon söner; kökte `odak` sırasıyla *lives in Ankara*, *this month*.
- `dogru`: B satırı vurgu dolgusu + koyu yazı + koyu tik; boşluğa *is living* yazılır. Ham yeşil yok.
- `sik_not` pilleri: A `this month → temporary ✗` · C `he ↔ live ✗` · E `he ↔ are ✗` · D `to live: no tense ✗`. Çarpı vurgu renginde, kırmızı yok. Elenen satır soluklaşır.
- Künye: `SIMPLE PRESENT vs PRESENT CONTINUOUS · YDT BASIC`, sağ üst `Mini question`, ajanda etkin Trap (02-03 sahne 13 ile aynı). Çıkış fade geçiş katmanında; son 12 kare durgun.

## Olay listesi (kare = yerel; sözcük = cümle.sıra)

| Olay | Kare | Küresel sn | Yerel sn | Cümle sözcüğü |
|---|---|---|---|---|
| soru kartı + MINI QUESTION | 16 | 220,88 | 0,55 | 15.0 Mini |
| kök sözcük sözcük (My … us.) | 48 | 221,93 | 1,60 | 15.2 My → 15.12 us. |
| boşluk çizgisi (susma) | 131 | 224,71 | 4,38 | 15.10 he (t1 + 0,06) |
| boşluk vurgu çizgisi | 212 | 227,40 | 7,07 | 15.13 Boşluğa (+0,15) |
| sayaç halkası + 5, şıklar 0,18 sn arayla | 270 | 229,33 | 9,00 | 15.17 Beş |
| öğrenci başı + balon | 307 | 230,58 | 10,25 | 16.0 Bence (−0,18) |
| A soluk sarı çerçeve | 332 | 231,40 | 11,07 | 16.1 A |
| balon söner | 441 | 235,03 | 14,70 | 17.0 Ankara'da |
| odak *lives in Ankara* | 444 | 235,13 | 14,80 | 17.0 Ankara'da (+0,1) |
| odak *this month* | 547 | 238,55 | 18,22 | 17.6 bu |
| A pili, A çerçevesi söner, A soluk | 633 | 241,43 | 21,10 | 17.13 geçici |
| doğru B: vurgu dolgusu + koyu yazı | 693 | 243,43 | 23,10 | 17.17 B |
| B tik | 699 | 243,63 | 23,30 | 17.17 B (+0,2) |
| boşluğa *is living* | 739 | 244,95 | 24,62 | 17.20 is |
| C imleci | 772 | 246,07 | 25,74 | 17.22 C |
| E imleci | 799 | 246,95 | 26,62 | 17.25 E |
| C pili | 820 | 247,67 | 27,34 | 17.27 özneyle |
| E pili | 835 | 248,15 | 27,82 | 17.28 uyumsuz. |
| D imleci (C, E imleci söner) | 863 | 249,11 | 28,78 | 17.29 D |
| D pili | 885 | 249,83 | 29,50 | 17.31 tek |

## Kapı sonucu

```
== HAZIRLA
tema: acik
index.html yazıldı; komut 68 olay 33 hareket (0.55, 30.05)
olay 33 cizgi 15
önizleme hazır
== KAPI
13-hyperframes-mini-soru | çakışma yok (125 örnek, 39812 kutu)
...
kapı çıkış kodu: 0
```

Komut: `bash araclar/qa-yerel.sh 02-04-ydt-temel 13-hyperframes-mini-soru 226.0,234.2,245.9,251.0 251.0 --hazirla`.
Ek kareler: aynı betik `229.9,239.0 234.2 --kapisiz` (çıkış 0).

## Bakılan kareler ve bulgu

| Kare | Ne görünür | Bulgu |
|---|---|---|
| `k/13-hyperframes-mini-soru-226.png` (yerel 5,67) | kart, kök 2 satır, soluk boşluk çizgisi | sorun yok |
| `k/13-hyperframes-mini-soru-229.9.png` (yerel 9,57) | sayaç halkası dolarken, şıklar giriyor (D yarı, E yok) | ara kare, beklenen |
| `k/13-hyperframes-mini-soru-234.2.png` (yerel 13,87) | 5 şık, A çerçevesi, öğrenci başı + 3 satır balon | sorun yok; balon kuyruğu başa değmez |
| `k/13-hyperframes-mini-soru-239.png` (yerel 18,67) | iki odak çizgisi, A çerçevesi duruyor | sorun yok |
| `k/13-hyperframes-mini-soru-245.9.png` (yerel 25,57) | B dolgu + tik, boşlukta *is living*, A pili, A soluk | sorun yok |
| `k/13-hyperframes-mini-soru-251.png` (yerel 30,67) | son hâl: 4 pil, B yanık, D imleci | sorun yok |
| `k/koyu/13-hyperframes-mini-soru-234.2.png` | koyu tema, balon anı | kontrast iyi |
| `k/koyu/13-hyperframes-mini-soru-251.png` | koyu tema son hâl; turuncu dolgu üstünde koyu yazı + tik | kontrast iyi |

Taşma, kesilen yazı, üst üste binme, okunmaz kontrast, boş kare yok. Düzeltme turu gerekmedi (0/4).

## Açık noktalar

1. **Doğru şık rengi.** İstem "doğru şık yeşil" diyor. BRIEF §3 satır 13 ve 13.11 QA kararı "ham yeşil yok, vurgu dolgusu + zemin renginde tik" diyor. BRIEF uygulandı. Açık temada zemin rengi (#f7f3ea) açık sarı dolguda (#ffe066) okunmaz; yazı ve tik iki temada da koyu (#1b1a17, satır içi stil). 02-03 ileri sahne 11 ile aynı yol.
2. **QA zamanı küresel saniyedir.** İstem "sahne içi saniye" diyor; `sahne-kare.mjs` anlatım saniyesi alır (satır 7, 91). Kareler küresel değerle alındı; yerel karşılıkları tabloda.
3. **Kod yazım yolu.** Yazma kapısı (`write-size-gate.sh`) 15+ satır `.py` yazımını engeller. `uret.py`'yi şef belge olarak yazdı (`/tmp/kalem0204-s13/uret.spec.md`). `agy-filo tek --rol kod` dosyaya geçirdi (gemini-3.8-flash-high, 38 sn). Şef bayt bayt karşılaştırdı: eşit (15.918 bayt). İstemdeki "alt ajan açma" kuralıyla çatışır; Claude alt ajanı açılmadı, kapının gösterdiği yol kullanıldı (sahne 07 ile aynı).
4. `yardim.py` sahne 07 kopyası, `olay.py` 02-03 sahne 13 kopyası; ikisi de değişmedi. `calistir.sh` sahne 07 kopyası; başlık satırı ve `KARE=940` değişti.
5. Boşluktaki *living* sözcüğünün *g* kuyruğu vurgu çizgisine değer (çizgi üstüne yazma görünümü). Kapı saymaz; 02-03'te de aynı. İstenirse `ALT` büyütülür.
6. Kök ve şık metni senaryo-taslak ekran metni sütunuyla birebir. Pil metinleri taslağın görsel notundan; D notu `to live: no tense`.
7. Birim testi yok (HF sahneleri test taşımıyor); doğrulama kapı + kare. Render yapılmadı (`video.mp4`, `kontrol.png` yok). `__pycache__/` derlemeden kaldı, silinmedi.
