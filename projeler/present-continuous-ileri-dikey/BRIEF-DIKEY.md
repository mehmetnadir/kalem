# Present Continuous — DİKEY tam ders (9:16, YDT İLERİ) · `projeler/present-continuous-ileri-dikey`

Nadir 04.11 gece (ONAYLI): dikey sürüm = yatayla AYNI anlatım ve AYNI ses; sahne düzeni dikey için SIFIRDAN tasarlanır.
Yatay öğelerin döndürülmüş/responsive hâli YASAK. İzleyici telefondan bakar: 1080 px genişlik ekranda ≈ 390 CSS px olur
(ölçek 1/2,77). Bu BRIEF, ana `../present-continuous-ileri/BRIEF.md` üstüne gelir: stil (§2), kalem darbesi, çizim kaynakları,
ses olayları, kabul (§7) oradan aynen; yerleşim ve ölçek burada.

## 0. Nadir'in 04.11 gece dikey bulguları (D1/S1 kare incelemesi, şef gözü — bunlar düzeltilmiş olmalı)
Kaynak: ../present-continuous-dikey/BRIEF-DIKEY.md §0 (tek kaynak, 05.11 karar 6b).

## 1. Teknik çerçeve
`zaman.json` hazır: 6 sahne, ana ileri projeyle AYNI t_bas/t_son/kare (01 102 · 02 380 · 03 442 · 04 387 · 05 372 · 06 956), 1080×1920,
`gecis_kare` 12. Ses: `ortak/anlatim` → ana projeye sembolik bağ (`../../present-continuous-ileri/ortak/anlatim`: `cumle-1..7.wav`, `anlatim.wav`, `sureler.json`,
`sozcukler.json`, `METIN.md`, `altyazi.json` [21 parça: {cumle, dil, t0, t1, metin, konusan}]). Yerel kare f ↔ küresel
`t_bas + f/30`. İlk/son 12 kare geçiş altında DURGUN. Kareler `ortak/yakala.py ... 1080 1920`. HyperFrames kökü
`data-width="1080" data-height="1920"`. Ortak dosyalar: `ortak/kunye.js` (dikey v2: `kunyeHazirla` → `{logo, grenler, altyazi}`,
`zeminCiz`, `kunyeCiz`, `altyaziMetin`, `altyaziCiz`), `ortak/kalem-canvas.js`, `ortak/tema.sh` (+ `tema_bitir` artık
`video-<tema>.mp4` de yazar), `ortak/hf_tema.py` (HyperFrames tema + canlı sürücü köprüsü), `ortak/{cizim,font,logo}`.
Şablon olarak D1 sahne kodu okunabilir (`../present-continuous-d1/sahneler/*`): motor kurulumu, yakala, olaylar, kontrol
aynı; YERLEŞİM ve ÖLÇEK oradan alınmaz (o sürüm hatalı).

## 2. Bantlar ve HUD (px, 1080×1920)
Kaynak: ../present-continuous-dikey/BRIEF-DIKEY.md §2 (tek kaynak, 05.11 karar 6b).

## 3. Ölçek (telefon kuralı — altına inilmez)
| Rol | Yazı | Boy (px) | Renk |
|---|---|---|---|
| İngilizce örnek cümle (kart içinde, sözcük zamanlı) | Fredoka 700 | 72 (3 satıra sığmazsa 64) | mürekkep; okunan sözcük altı sarı |
| Türkçe çeviri / kanca cümlesi | Caveat 700 | 64–80 | mürekkep |
| El notu, ok etiketi ("şimdiki zaman", "= iş sürüyor") | Caveat 700 | 64 (ikincil yalnız ≥ 72) | vurgu ya da mürekkep |
| Formül / anahtar sözcük (`be + V-ing`, `-yor = -ing`, `go → go-ing`) | Fredoka 700 | 110–160 | mürekkep + vurgu |
| Kapak başlığı (sahne 01) | Fredoka 700 | 190–230, 2 satır, kontur 12 | mürekkep / vurgu |
| Kart | kenar 4 px kalem çizgisi, iç boşluk 40, genişlik 984 | | |
| Figür / nesne | 420–560 px yüksek; kalınlık figür 4,0–4,8, nesne 4,0; belirteç (daire/altı/ok) w 9–12 | | |
Satır başına en çok 24 karakter (Caveat 64'te 984 px'e sığar). Güvenli alan: kenar 48, HUD/altyazı bandına 0 taşma.
Hareket kuralları ana BRIEF §2.6 (ease-out, ≤ 4 sn durağanlık, çakışma 0 px, hiçbir öğe kaybolmaz — yer açmak için
yukarı toplanır ve küçülür, ama küçülünce de ≥ 48 px kalır).

## 4. Sahne sözleşmeleri (içerik ve zamanlar ileri ana BRIEF §4'ten; burada yalnız dikey yerleşim)
| # | Klasör / motor / kare | Dikey yerleşim (içerik bandı 352–1392, üstten alta) |
|---|---|---|
| 01 | `01-hyperframes-giris` HF 102 | Kapak kalıbı: logo damgası sol üst (0,0–0,4) → rozetler `YDT · ADVANCED` + `GRAMMAR` → başlık 2 satır `PRESENT` / `CONTINUOUS` (190 px, y ≈ 520/740, kalemle, 0,65–1,45) → cümle 1 `YDT'nin -ing tuzağına düşme.` Caveat 80 sözcük zamanlı (1,00–3,0; `-ing` 1,80 sarı daire; y ≈ 900) → figür standing-3 + telefon (phone) (y 980–1380, bant ortası) → 2,0–3,0 uçuş: başlık künye ders adına küçülür, cümle yukarı kayar, figür solar; altyazı bandı cümle 1 |
| 02 | `02-paperjs-kanca` Paper.js 380 | Cümle 1 yazısı Caveat 80 iki satır (y 400–560), `-ing` sarı daire; ORTA: formül kartı tam genişlik (y 640–1000): `Subject` (5,32) · `am / is / are` Fredoka 110 (6,84 / 7,68 / 8,32) · `V-ing` (9,40) üç satırda alt alta; alt (y 1040–1392): saat (clock) + `6 min` (10,93), üç kutu `1 2 3` (12,57–13,65) ve kırmızı ünlemli `1 tuzak` kutusu (14,05); altyazı: cümle 2 parçaları |
| 03 | `03-paperjs-ornek1` Paper.js 442 | Çip `Example 1 / 3`; kart tam genişlik: `Please be quiet! The baby is sleeping in the next room while I am talking on the phone.` Fredoka 64 (4 satır, y 400–740) sözcük zamanlı; TR `Bebek uyuyor, ben telefonda konuşuyorum.` Caveat 64 (y 780); ORTA: telefonda konuşan figür (sitting-4) + duvar + uyuyan figür (sitting-6) 460 px (y 860–1240); alt: `is sleep-ing` / `am talk-ing` formül 110 (`while` 20,13 sarı kutu); altyazı: cümle 3 parçaları |
| 04 | `04-canvas-ornek2` canvas 387 | Çip `Example 2 / 3`; kart `Because the roof is leaking, we are staying at my uncle's house this week.` (4 satır); TR Caveat 64; ORTA: ev (home) + 3 damla (rain) + ikinci küçük ev 460 px; not `geçici → this week` Caveat 64 + takvim şeridi; alt: `is leak-ing` / `are stay-ing` 110 |
| 05 | `05-canvas-ornek3` canvas 372 | Çip `Example 3 / 3`; kart `We are taking the bus to Izmir tomorrow morning, so I am packing my bag tonight.` (4 satır); TR Caveat 64; ORTA: otobüs (bus) + yolcu figürü (standing-4) 480 px; not `yarın = planlı gelecek` Caveat 64 + takvim + saat (bilet kutusu); alt: `are tak-ing` / `am pack-ing` 110; çıkış fade |
| 06 | `06-hyperframes-form` HF 956 | Çip `Question` → `Form` (60,40'ta); üst: öğrenci balonu (kadro başı `peeps-kit/ogrenci-bas.svg`, baş 160 px) + balon metni Caveat 64 `Hocam, bilmek de sürüyor. I am knowing the answer olmaz mıydı?` (54,63–59,85, y 400–700); 60,40 kırmızı çarpı; ORTA: durum fiilleri listesi `know / believe / own / belong` Fredoka 96 (y 760–1100, 61,60–64,64) + `-ing` üstü çizili (65,80); `I know the answer.` (66,81) ve `biliyor-um ↔ know` köprüsü (68,58–73,14) Caveat 72; `He is always losing his keys.` (73,39) kart; alt: kod `olay = -ing` / `durum ≠ -ing` Fredoka 150 (80,72–83,96); son 1 sn durgun; altyazı: cümle 6 (öğrenci) ve 7 |

## 5. Çalıştırma ve kabul (sahne başına)
1. Sahne klasörü: D1'deki ile aynı dosya düzeni (`calistir.sh` tema.sh'ı `. "$D/../../ortak/tema.sh" "$@"` ile çağırır,
   `KAREYI_TUT`, yük bekçisi, `kontrol.png`, `k/*.png`, `RAPOR.md`, `olaylar.json`). Yol sabitleri
   `/projeler/present-continuous-ileri-dikey/...`. `calistir.sh --tema acik` sonra `--tema koyu` (ikisi de; `video-acik.mp4` +
   `video-koyu.mp4` oluşur, `video.mp4` son koşunun kopyasıdır).
2. Editör kapısı (sayfa = konsol hatası 0 + durum eval; HTTP 200 kanıt DEĞİL): `ortak-tarayici` + `cdpilot context create`
   ile başsız bağlamda `http://127.0.0.1:3012/p/present-continuous-ileri-dikey/onizle.html?surum=dikey-tam&tema=acik&t=<sn>`
   açılır; `cdpilot console` hata 0; `cdpilot eval "JSON.stringify(window.EDITOR.durum())"` → ilgili slot `hazir:true, goster:true`.
   (Sahne sayfasını tek başına da aç: `/projeler/present-continuous-ileri-dikey/sahneler/<klasor>/sayfa.html?canli=1&tema=acik`.)
3. Kare kapısı (AJAN KENDİ GÖZÜYLE bakar): `k/*.png` 3 tam kare + `kontrol.png` Read ile açılır; ayrıca telefon ölçeği:
   `ffmpeg -i video.mp4 -vf "fps=1,scale=360:640,tile=3x2" k/telefon-%02d.png` üretilir ve BAKILIR. Ölçüt: HUD okunuyor,
   içerik bandı dolu (alt yarı boş DEĞİL), ≥ 64 px yazı, figür ≥ 420 px, altyazı bandında metin, platform bandı boş,
   çakışma 0. Uymayan kare → düzelt → yeniden yakala (raporda "neden yeniden" satırı).
4. RAPOR.md: kare sayısı, tema ikisi de, olay sayısı, kapı sonuçları (eval çıktısı, kontrol/telefon kare adları), açık sorular.
