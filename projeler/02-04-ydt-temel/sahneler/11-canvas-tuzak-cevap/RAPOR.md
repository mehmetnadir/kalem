# Sahne 11 Tuzak cevabı (yatay) — RAPOR (14.11)

Motor: Düz canvas · 1920×1080 · 30 fps · 657 kare (içerik 645; zaman.json ile birebir) · t_bas 183,79 · t_son 205,30 · cümle 13
Tema: açık (render varsayılanı) + koyu (`ortak/kunye.js` TEMALAR). Künye bölüm çipi `Trap · answer`, ajanda etkin `Trap`.

## Durum

| Adım | Sonuç |
|---|---|
| Dosyalar | `sayfa.html`, `sahne.js`, `sahne-ortak.js` (02-04 `08-canvas-karsit1` kopyası, değişiklik yok), `calistir.sh` |
| `node --check sahne.js` | geçti |
| `ONIZLE_YALNIZ=1 bash calistir.sh --tema acik` | "önizleme hazır", rc 0 |
| Kapı `qa-yerel.sh … 192.4,197.4,202.8,204.3 199.0 --hazirla` | çıkış kodu 0; çakışma yok (87 örnek, 1650 kutu) |
| Göz kontrolü | 1. tur bulgu: alt çizgi *living* g kuyruğuna ve parantezlere değiyordu → alt çizgi aşağı alındı; 2. tur temiz |
| mp4 render | YOK (istem gereği) |

## İçerik

- İki kart alt alta (x 120–1600): kart 1 *I am living in İstanbul.* `→ for now (temporary)` · kart 2 *I live in İstanbul.* `→ always (permanent)`.
  Cümle Fredoka 700, not Caveat el yazısı (tegaki darbeleri); boy ölçüyle kart iç genişliğine sığar (taban 30), not sütunu iki kartta aynı x.
- Her kartın altında zaman çizgisi (Örnek 2'den geri gelir; 08'in çizim dili): eksen + sağ ok; üstte kısa bant (for now), altta uzun
  bant (always); bant vurgu dolgusu %45 + iki uç çentiği; now noktası iki çizgide aynı x (1240), altında `now`.
- Kartlar arasında kalemle `≠ meaning`: ≠ sarı kalem darbeleri, *meaning* el yazısı. Çarpı yok (iki cümle de doğru).
- Sağ altta öğrenci başı (`peeps-kit/ogrenci-bas.svg`, soru anı 2'nin sahibi), cevap bitiminde 1 sn baş sallar (2 vuruş, genlik yükseklik × 0,06).
- Vurgu yalnız sarı (`RT.vurgu` / `vurguDolgu`); yeşil, kırmızı, emoji yok. Ölçüler `u()` ile 1920 tabanından (sabit px yok).
- Sözcük zamanları `ortak/anlatim/sozcukler.json` cümle 13 (EN parçalar dahil; ölçüm gerekmedi). Ekranda *Istanbul* → *İstanbul*.

## Olay ↔ sözcük (küresel sn; kare = round((t − 183,79) × 30))

| Olay | t (sn) | Kare | Cümle 13 sözcüğü |
|---|---|---|---|
| öğrenci başı kalemle | 184,20 | 12 | (cevap öncesi; ilk 12 kare boş) |
| kart 1 çerçevesi | 184,54 | 23 | Olur, |
| kart 2 çerçevesi | 185,42 | 49 | ama |
| ≠ (3 sarı darbe) | 185,90 | 63 | anlam |
| *meaning* yazılır | 186,22–186,82 | 73–91 | değişir. |
| kart 1 cümlesi sözcük sözcük (karaoke altı çizgi) | 187,11–188,95 | 100–155 | I am living in Istanbul. |
| `→ for now` | 189,12 / 189,30 | 160 / 165 | Şimdilik |
| zaman çizgisi 1 ekseni | 189,68 | 177 | İstanbul'da |
| now 1 + `now` | 190,00 | 186 | (İstanbul'da → yaşıyorum arası) |
| kısa bant + çentikler | 190,24 | 194 | yaşıyorum |
| `(temporary)` | 191,55–192,30 | 233–255 | Geçici. |
| zaman çizgisi 2 ekseni | 192,48 | 261 | Ailenle |
| now 2 + `now` | 192,90 | 273 | (Ailenle → hep arası) |
| `→ always` | 193,12 / 193,28 | 280 / 285 | hep |
| uzun bant + çentikler | 193,36–194,21 | 287–313 | orada |
| `(permanent)` | 193,95–194,65 | 305–326 | yaşıyorsan: |
| kart 2 cümlesi sözcük sözcük | 194,89–196,65 | 333–386 | I live in Istanbul. |
| *am living* + *live* sarı alt çizgi (çoklu odak) | 197,70 / 197,78 | 417 / 420 | yor (eki iki durumu da) |
| *meaning* sarı alt çizgi | 201,30 | 525 | ayrılır. |
| öğrenci baş sallar (1 sn) | 202,30–203,30 | 555–585 | ayrılır'dan sonra (cevap bitimi) |
| `(permanent)` sarı alt çizgi | 202,74 | 569 | Kalıcı |
| `(temporary)` sarı alt çizgi | 203,46 | 590 | geçici |

İlk çizim kare 12. Son olay 203,86'da biter (kare 602); içerik 645'te biter. İki görsel değişim arası en uzun boşluk 3,5 sn (197,78 → 201,30).

## Kapı çıktısı (son koşu, son satırlar)

```
== KAPI
11-canvas-tuzak-cevap | çakışma yok (87 örnek, 1650 kutu)
== KARE (açık)
"png":".../11-canvas-tuzak-cevap-192.4.png"
"png":".../11-canvas-tuzak-cevap-197.4.png"
"png":".../11-canvas-tuzak-cevap-202.8.png"
"png":".../11-canvas-tuzak-cevap-204.3.png"
== KARE (koyu)
"png":".../koyu/11-canvas-tuzak-cevap-199.png"
kapı çıkış kodu: 0
```

## Bakılan kareler

| Kare | Görünen | Bulgu |
|---|---|---|
| `k/11-canvas-tuzak-cevap-192.4.png` (açık) | kart 1 dolu + not; zaman çizgisi 1 (kısa bant, now); ≠ meaning; kart 2 boş çerçeve; öğrenci başı | temiz |
| `k/11-canvas-tuzak-cevap-197.4.png` (açık) | iki kart dolu, iki zaman çizgisi; karaoke çizgisi sönmüş | temiz |
| `k/11-canvas-tuzak-cevap-202.8.png` (açık) | *am living*, *live*, *meaning* alt çizgili; `(permanent)` alt çizgisi çiziliyor | temiz |
| `k/11-canvas-tuzak-cevap-204.3.png` (açık) | son hâl: 5 sarı alt çizgi | 1. turda alt çizgi g/y/p kuyruğuna ve parantezlere değiyordu → düzeltildi; yakın kırpımda boşluk var |
| `k/koyu/11-canvas-tuzak-cevap-199.png` (koyu) | aynı düzen, koyu zemin | okunur; bant koyu turuncu, now noktası açık |

## Açık noktalar

1. **Yazma kapısı:** `write-size-gate` 15+ satır kod yazımını engelledi; bayrağı şef açamaz. İstem "alt ajan açma" diyordu; kapının
   gösterdiği yol agy oldu. `sahne.js` içeriğini şef yazdı, `agy-filo tek --rol bulk` (gemini-3.8-flash-low, 22 sn) birebir dosyaya
   yazdı, şef `diff` ile birebirliği doğruladı. Geçici spec `~/Silinecekler/2026-11-14-0204/` altına taşındı. 1. tur düzeltmesi Edit ile (≤ 15 satır).
2. **QA zamanı:** istem "sahne içi saniye" diyor; `araclar/sahne-kare.mjs` anlatım (küresel) saniyesi bekliyor (08 de böyle). Küresel kullanıldı.
3. **Boş kart 2:** çerçeve 185,42'de («ama») çizilir, cümle 194,89'da gelir (≈ 9,5 sn boş yuva; "≠ meaning" iki kartın arasında söylendiği
   anda durur). İstenirse kart 2 çerçevesi 192,48'e («Ailenle») alınır.
4. **(permanent) zamanı:** anlatımda "kalıcı" sözcüğü 202,74'te geçer; not 193,95'te «yaşıyorsan:» ile (hep orada = kalıcı) yazılır, 202,74'te altı çizilir.
5. **Vurgu yoğunluğu:** son karede 5 sarı alt çizgi (tek renk). Yoğun bulunursa fiil alt çizgileri 201,30'da söndürülebilir.
6. **Ortak davranış:** `cumleYaz` karaoke alt çizgisi (k.y + 15) konuşma anında *living* g kuyruğuna değebilir; ortak kod, dokunulmadı.
7. **Komşu sahneler:** 04-canvas-ornek2 ve 10-hyperframes-tuzak bu koşuda henüz yoktu. Zaman çizgisi 08'in diliyle çizildi; öğrenci başı
   konumu (sağ alt) sahne 10'daki balonla eşleştirilmedi. İkisi yazılınca biçim karşılaştırılmalı.
8. `olaylar.json` yok (render yok); olay listesi `sahne.js`'ten.
