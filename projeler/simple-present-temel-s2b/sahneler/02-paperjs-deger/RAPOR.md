# 02-paperjs-deger — RAPOR (15.11, istem D-V2 huni v2; render yok)

| Ölçüm | Değer |
|---|---|
| Motor | Paper.js · 1080×1920 · 30 fps · 278 kare · t_bas 3,00 · t_son 11,87 (`zaman.json`) |
| `qa-yerel.sh … 3.05,7.45,11.80 7.45 --hazirla` | çıkış 0 (4 tur; tur 1–3 görsel düzeltme, kapı her turda 0) |
| `cakisma-kapisi.mjs … --sahne 02-paperjs-deger --port 41333 --sunucu 41022` | çıkış 0 · "çakışma yok (37 örnek, 1969 kutu)" · "uyar" satırı 0 |
| Metin taraması (`tam ders|dakika`, html/js/py) | boş (grep çıkış 1) |
| Kanal katmanı (3 açık + 1 koyu karede piksel ölçümü) | 4 / 4 karede yerinde |
| Halka ↔ `usually` mürekkebi | en yakın 4 px (açık), 5 px (koyu); değme yok |

## Yapım

| Adım | Kim | Çıktı |
|---|---|---|
| Kopya | şef (`cp -p` + Edit) | `sayfa.html` (sahne yolu, 278 kare), `kalem-paper.js` (2 içe aktarma yolu S2 `ortak/`, baş yorum), `calistir.sh` (N 278, klasör, paket, `GLOBAL_SN`, Silinecekler alt dizini), `nesneler.json` (`[]`) — kaynak emsal `02-04-ydt-temel-s1/sahneler/02-paperjs-ornek/` |
| Tasarım | şef | `SPEC.md` (bantlar, sözcük tablosu, sabitler, `okYol`, 21 olay, 10 bekçi, beklenen konumlar) |
| `sahne-02.js` | agy-filo `tek --rol kod` (gemini-3.8-flash-high, 220 sn, 1 tur, başarılı) | 472 satır · özet `/home/sef/.claude/canavar/agy-filo/20261115-192702/ozet.md` |
| İnceleme | şef | dosya baştan sona okundu; SPEC'e uyuyor; `node --check` geçti (`.mjs` kopyasıyla) |
| Şef Edit (kare turu 1–3) | şef | halka ölçüsü, kart satır aralığı, ok 1 koridoru (tablo `SPEC.md` "Şef düzeltmeleri") |

agy özetindeki "değişen" listesi paralel oturumların dosyalarını da sayar (`02-04-ydt-temel-s2/…`, `sozlesme.md`); bu koşu yalnız `sahne-02.js` yazdı
(sahne dizini `git status` ile yeni; başka dosya bu oturumda değişmedi).

## Olay listesi (yerel kare = round((t − 3,00) × 30); zaman `sozcukler.json`'dan `al()` ile)

| # | Olay | Kare | Cümle 2 sözcüğü (küresel sn) | Konum |
|---|---|---|---|---|
| 1 | Boş kart çerçevesi (yazısız, kalemle) | 0–12 | — (3,00–3,40) | kutu 70–950 × 480–676; kare 0 içerik bandı boş |
| 2 | Kart satır 1 `My brother` | 29 / 36 | My 3,95 · brother 4,19 | Fredoka 64, taban 556, x 110 |
| 3 | `usually` | 48 | usually 4,59 | taban 556, `brother` + boşluk + 40 |
| 4 | Oturan figür (kalem; `open-peeps/sitting-4.svg`) | 29–80 | My 3,95 | 70–400 × 900–1350 |
| 5 | Halka `usually` (tek sarı, `RT.vurgu`) | 52–64 | usually 4,59 (+4 kare: sözcük açıldıktan sonra) | ≈ 448–738 × 496–588 |
| 6 | Kart satır 2 `goes to school by bus.` | 60 / 67 / 72 / 81 / 89 | goes 4,99 … bus. 5,95 | taban 648 |
| 7 | Otobüs (kalem; `coco/bus.svg`) | 60–93 | goes 4,99 | ≈ 450–930 × 1157–1343 |
| 8 | Zemin çizgisi | 89–104 | bus. 5,95 | y 1358 |
| 9 | Soluk TR `Kardeşim genellikle` / `okula otobüsle gider.` (Caveat 64, `ikincil`) | 108 / 112 | bus. sonu 6,59 | x 84, taban 752 / 832 |
| 10 | Ok 1 (ince, `ikincil`): halka → `alışkanlık` | 115–125 | Alışkanlık 6,84 | sağ koridor x ≈ 890–910 |
| 11 | `alışkanlık` (Caveat 64, mürekkep) | 121–135 | Alışkanlık 6,84 | ≈ 738–940, taban 832 |
| 12 | Ok 2 (köprü): halka → TR `genellikle` | 136–150 | işareti. 7,52 | kart satır 2'nin sağından (x ≈ 790–800) geçer, `genellikle` sonuna sola bakar |
| 13 | Figür + otobüs + zemin solar | 170–174 | Şu 8,67 | grup saydamlığı 1 → 0 (4 kare) |
| 14 | `şu an` (Caveat 64, `ikincil`) | 174–184 | Şu 8,67 (+4: solma bitince) | x 84, taban 1015 |
| 15 | `şu an` üstüne kalem çizgisi | 184–191 | değil, 9,07 (yazı bitince) | mürekkep |
| 16 | `Her sabah yedide` (sözcük zamanlı) | 204–228 | her 9,79 · sabah 9,95 · yedide 10,31 | taban 1112 |
| 17 | 5 gün kutusu (yazısız) | 204–225 | her 9,79 (3 kare ara) | 84–716 × 1262–1338 |
| 18 | `her sabah` altçizgi (mürekkep) | 218–226 | sabah sonu 10,27 | y ≈ 1122 |
| 19 | `kalkarım.` | 230–245 | kalkarım 10,67 | taban 1188 |
| 20 | 5 tik (mürekkep), 5/5 | 219 / 225 / 231 / 237 / 243 | yedide 10,31 … | kutu ortaları |

Durgun: 253–265 (`SON` 265 = 11,83). Sarı yalnız 5. olay; altyazı karaokesi `kunye.js`'te.

## Kanal katmanı ve künye (karede ölçüm; eşik: sol kenar satır medyanından sapma > 90)

| Öğe | Tablo | Ölçülen (4 karede aynı) |
|---|---|---|
| Logo | resim x 53,2, görünür x 60, y 291–339 | görünür x 60/61–239, y 298–330 (SVG iç boşluğu; emsal ile aynı) |
| `@ydspublishing` | Lexend 700 42, x 263, taban 330 | x 264–598, y 296–339 (taban 330, `y`/`p` kuyruğu 339) |
| Künye | y 360–450, sağ uç ≤ 960 | x 60–510, y 386–433 |

## Bantlar (karede ölçüm, tur 4)

| Kare | 0–280 | İçerik (455–1395) | Altyazı | 1570–1920 | x 961–1080 |
|---|---|---|---|---|---|
| 3,05 açık | boş | x 64–192, y 479–483 (kart üst kenarı çiziliyor) | x 179–842, y 1448–1493 | boş | boş |
| 7,45 açık | boş | x 62–957, y 470–1362 | x 329–689 | boş | boş |
| 11,80 açık | boş | x 62–957, y 470–1346 | x 88–930, 2 satır | boş | boş |
| 7,45 koyu | boş | x 62–957, y 470–1362 | x 329–689 | boş | boş |

## Bakılan kareler (Read ile; `k/`, `k/koyu/`)

| Kare | Bulgu |
|---|---|
| `k/02-paperjs-deger-3.05.png` | kare 2: içerik bandı boş, kart üst kenarı kalemle başlıyor; altyazı cümle 1 sonu (`Usually görünce hangi zaman?`) |
| `k/02-paperjs-deger-7.45.png` | kart + halka, soluk TR 2 satır, ok 1 bitti, `alışkanlık` yazılıyor (`alışkanl`), figür + otobüs + zemin; üst üste binme yok |
| `k/02-paperjs-deger-11.8.png` | son durum: kart, halka, iki ok, `alışkanlık`, çizili `şu an`, `Her sabah yedide` (altçizgili) / `kalkarım.`, 5 tikli kutu; taşma ve kesik yazı yok |
| `k/koyu/02-paperjs-deger-7.45.png` | koyu tema: krem yazı ve çizgi, turuncu halka ve rozet, şeffaf logo; okunur |

Tur 1 bulguları: halka `usually`nin 2. `l` tepesine ve `y` koluna değiyordu (piksel haritası, 1 px); ok 1 kart sağ kenarına 10 px yaklaşıyordu.
Tur 2 (eğim +0,06): `y` kuyruğu kurtuldu, temas sürdü. Tur 3: halka büyüdü (rx +36, ry 0,72 boy, eğim 0), `EK` 40, satır aralığı 92 → temas yok.
Kareler her turda aynı adla üzerine yazıldı (`qa-yerel` kopyası).

## Açık noktalar

1. **Karaoke altçizgisi yok:** emsalin sarı `altCizgi`'si kullanılmadı; istem "halka sahnenin tek sarısı" der. Kart sözcükleri söylendiği karede
   açılır (sözcük zamanlı), altyazı bandı karaokeyi taşır. Sarı kayan çizgi istenirse ikinci sarı olur (istemle çelişir).
2. **Soluk TR kalemle değil, saydamlıkla açılır** (`yazi()`, 8 kare): seslendirilmez; `alışkanlık` kalemi 6,84'te başlarken ikinci kalem çalışmasın.
3. **`alışkanlık` konumu:** "kartın sağ altı" = TR satır 2 hizasında sağda (x ≈ 738–940). Köprü oku (ok 2) kart satır 2'yi kesmesin diye koridordan
   (`bus.` sağı) dolanır; düz ok `school`/`by` üstünden geçerdi.
4. **Gün kutularında gün adı yok:** ana derste Lexend 28 `Pzt…Cum` vardı; ≥ 64 px kuralı yüzünden alınmadı, kutu + tik 5/5 kaldı.
5. **`usually` önü boşluk 56 px** (boşluk + 40): halkanın `brother`a değmemesi için; satır biraz açık görünür. Daha dar istenirse halka yerine altçizgi
   (hareket sözlüğü 13.11) — istem halka istediği için uygulanmadı.
6. **Geçiş:** 11,87–12,27 sahne 02 öğelerinin solması birleştirmenin işi (`birlestir.py` geçişi); sahne içinde solma yok.
