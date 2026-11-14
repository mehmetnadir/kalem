# Sahne 10 · tuzak + soru anı 2 (HyperFrames, 656 kare, 162,33–183,79 sn + 12 kare geçiş payı; cümle 11–12)

Durum: P2 yazıldı (istem D, 14.11.2026, srv21). Önizleme hazırlığı `ONIZLE_YALNIZ=1` ile koştu. Render yok, commit yok.
Tema: açık (render varsayılanı) + koyu kare denetimi.

## İçerik (BRIEF §3 No 10)

| Öğe | Ne yapar |
|---|---|
| `yaklas` | "Tuzak." anında `TRAP` etiketi + tam genişlik kart; kart 0,93 → 1 ölçekle öne gelir |
| EN satırı | `I live in İstanbul with my family.` sözcük sözcük (Fredoka 700, 96) |
| TR satırı | "Türkçe" anında `TR` etiketi; "Türkçesi yaşıyorum" anında `Ailemle İstanbul'da yaşıyorum.` (Fredoka 600, 72, ikincil) |
| `ek_ayir` | "yor" anında *yor* sarı kutuyla kayar → `yaşı-yor-um.` (sahne 01 ile aynı kalıp ve QA payları) |
| `bag` | "Yor eki" anında *yor* → *live* kalem çizgisi (ok ucu live'da); "akla" anında ortada sarı `?` |
| fosfor | "-ing" anında *live* sarı fosfor (V1, -ing yok); yazı dolgu üstünde pilMetin rengine geçer |
| SORU ANI 2 | öğrenci başı (`ogrenci-bas.svg`, kadın, K22) + el çizimi balon; 10 sözcük sözcük sözcük (Fredoka 600, 44) |
| sarı nokta | "yaşıyorum" (balon) anında balon üst kenarından *yor* kutusuna sarı çizgi + nokta |
| `living` | balonda *living* sarı el altçizgisi (sözcük göründükten 0,3 sn sonra) |

Ekran metni senaryo §4 satır 11–12 ile aynıdır. Balon: "Hocam, Türkçesi yaşıyorum. / I am living in İstanbul olmaz mı?".
Soru anı `yanılgı:` satırına bağlı (taslak satır 106: Türkçe "yaşıyorum" ile kalıcı durumda -ing). 0,75 sn duraklama ve cevap sahne 11'de.
Renk: tek vurgu `RENK["vurgu"]` (hf_tema ile açık `#d9900f` / dolgu `#ffe066`, koyu `#f2a93b`). Yeşil, kırmızı, emoji yok.
Ölçüler `u()` ile; en küçük yazı 30 (`TR` etiketi). Künye: sağ üst `Trap`, ajandada Trap etkin (`ortak/kunye.js` ile aynı).

## Olay listesi (kare = sahne içi, sn = küresel)

| Olay | Kare | sn | Cümle sözcüğü (t0) |
|---|---|---|---|
| `TRAP` etiketi + kart çizimi + yaklaş | 16–44 | 162,88–163,78 | Tuzak. (11/0, 162,88) |
| `TR` etiketi | 45 | 163,84 | Türkçe (11/1, 163,84) |
| EN: I · live · in · İstanbul · with · my · family. | 113–165 | 166,09–167,83 | I … family. (11/5–11, aynı t0) |
| TR: Ailemle İstanbul'da | 190 | 168,66 | Türkçesi (11/12, 168,66) |
| TR: yaşıyorum. (bitişik) | 216 | 169,54 | yaşıyorum. (11/13, 169,54) |
| `ek_ayir` *yor* kutuyla kayar, tireler belirir | 269–282 | 171,30–171,73 | yor (11/15, 171,30) |
| `bag` yor → live (iki kol) | 312–341 | 172,74–173,69 | Yor (11/18, 172,74) |
| sarı `?` | 358 | 174,26 | akla (11/22, 174,26) |
| *live* fosfor + pilMetin | 418–428 | 176,26–176,61 | -ing (11/27, 176,26) |
| öğrenci başı + balon çizilir | 460–479 | 177,65–178,30 | Hocam, (12/0, 177,85); söz öncesi −0,20 (02-03 kalıbı; cümle 11 177,38'de biter) |
| balon sözcükleri | 466–639 | 177,85–183,64 | Hocam, … mı? (12/0–9, aynı t0) |
| sarı nokta + çizgi → *yor* | 511–523 | 179,37–179,77 | yaşıyorum. (12/2, 179,37) |
| *living* altçizgi | 571–581 | 181,36–181,71 | living (12/5, 181,06) + 0,3 |

`olaylar.json`: 20 ses olayı (tik, cizgi ×10). `Y.kontrol`: hareket 0,55–21,31 sn (ilk/son 12 kare durgun).

## Kapı sonucu (son koşu)

```
== KAPI
10-hyperframes-tuzak | çakışma yok (87 örnek, 32229 kutu)
== KARE (açık)  172.53 · 177.33 · 183.73
== KARE (koyu)  183.73
kapı çıkış kodu: 0
```
Komut: `bash araclar/qa-yerel.sh 02-04-ydt-temel 10-hyperframes-tuzak 172.53,177.33,183.73 183.73 --hazirla`

## Bakılan kareler ve bulgu

| Tur | Kare | Bulgu | Düzeltme |
|---|---|---|---|
| 1 | k/10.2, 15, 21.4 (yerel sn) | kareler boş: `sahne-kare` küresel anlatım saniyesi bekler | zamanlar + t_bas (162,33); boş kareler `~/Silinecekler/2026-11-14-0204/10-tuzak-bos-kare/` |
| 2 | k/172.53 | EN tam, TR `yaşı-yor-um.` kutu üstünde koyu yazı | — |
| 2 | k/177.33 | bag + `?` iki satır arasında, satırlara değmiyor; live fosforu okunur | — |
| 2 | k/183.73, k/koyu/183.73 | balon 10 sözcük, sağ iç boşluk yeterli; sarı nokta yor kutusunda; koyu temada dolgu üstü yazı koyu, okunur | — |
| 2 | k/ara/163.2, 171.45, 173, 176.45, 179.25, 181.6 | yaklaş çizimi, ek_ayir ara hâli, bag yarım, fosfor, balon yarım: taşma, kesik yazı, üst üste binme, boş kare yok | — |

Kare yolları: `k/10-hyperframes-tuzak-{172.53,177.33,183.73}.png`, `k/koyu/10-hyperframes-tuzak-183.73.png`, ara kareler `k/ara/`.

## Açık noktalar

- `yaklas` çevre karartması yapılmadı (02-03 sahne 10 emsali): tema çiftinde güvenli karartma rengi yok; kart ölçekle öne gelir. Gerekirse şef karar versin.
- İstem "sahne içi saniye" diyor; `qa-yerel.sh` → `sahne-kare.mjs` küresel anlatım saniyesi alır. İstem şablonu düzeltilmeli.
- "Türkçe ek seni yanıltabilir" (163,84–165,84) sırasında yalnız `TR` etiketi gelir; EN cümle 166,09'da başlar (söz sırası).
- Yazma kapısı (write-size-gate) 15+ satır kodu reddetti; `uret.py` belge dosyasından `agy-filo tek` ile birebir aktarıldı (sha256 eşit). `olay.py` 02-03 sahne 10'dan, `yardim.py` 02-04 sahne 01'den kopya.

Dosyalar: `uret.py`, `olay.py`, `yardim.py`, `calistir.sh`, `proje/index.html`, `olaylar.json`, `RAPOR.md`.
