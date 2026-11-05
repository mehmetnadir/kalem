# Simple Past — DİKEY tam ders (9:16, YDT ADVANCED) · `projeler/simple-past-ileri-dikey`

Nadir 04.11 gece (ONAYLI): dikey sürüm = yatayla AYNI anlatım ve AYNI ses; sahne düzeni dikey için SIFIRDAN tasarlanır.
Yatay öğelerin döndürülmüş/responsive hâli YASAK. İzleyici telefondan bakar: 1080 px genişlik ekranda ≈ 390 CSS px olur
(ölçek 1/2,77). Bu BRIEF, ana `../simple-past-ileri/BRIEF.md` üstüne gelir: stil (§2), kalem darbesi, çizim kaynakları,
ses olayları, kabul (§7) oradan aynen; yerleşim ve ölçek burada.

## 0. Nadir'in 04.11 gece dikey bulguları (D1/S1 kare incelemesi, şef gözü — bunlar düzeltilmiş olmalı)
Kaynak: ../present-continuous-dikey/BRIEF-DIKEY.md §0 (tek kaynak, 05.11 karar 6b).

## 1. Teknik çerçeve
`zaman.json` hazır: 6 sahne, ana projeyle AYNI t_bas/t_son/kare (01 102 · 02 326 · 03 602 · 04 487 · 05 528 · 06 791), 1080×1920,
`gecis_kare` 12. Ses: `ortak/anlatim` → ana projeye sembolik bağ (`cumle-1..7.wav`, `anlatim.wav`, `sureler.json`,
`sozcukler.json`, `METIN.md`, `altyazi.json` [21 parça: {cumle, dil, t0, t1, metin, konusan}]). Yerel kare f ↔ küresel
`t_bas + f/30`. İlk/son 12 kare geçiş altında DURGUN. Kareler `ortak/yakala.py ... 1080 1920`. HyperFrames kökü
`data-width="1080" data-height="1920"`. Ortak dosyalar: `ortak/kunye.js` (dikey v2: `kunyeHazirla` → `{logo, grenler, altyazi}`,
`zeminCiz`, `kunyeCiz`, `altyaziMetin`, `altyaziCiz`), `ortak/kalem-canvas.js`, `ortak/tema.sh` (+ `tema_bitir` artık
`video-<tema>.mp4` de yazar), `ortak/hf_tema.py` (HyperFrames tema + canlı sürücü köprüsü), `ortak/{cizim,font,logo}`.
Şablon olarak D1 sahne kodu okunabilir (`../present-continuous-d1/sahneler/*`): motor kurulumu, yakala, olaylar, kontrol
aynı; YERLEŞİM ve ÖLÇEK oradan alınmaz (o sürüm hatalı).

## 2. Bantlar ve HUD (px, 1080×1920)
```
y    0 ┌──────────────────────────────┐
       │ [logo 387×96]        [çip 80] │  HUD 0–320: logo sol üst y48 · ders adı Fredoka 700 56 taban y212
       │ SIMPLE PAST                   │  rozet hapı y236 h72 (Lexend 700 36) · "şu an" çipi sağ üst y48 h80 (Lexend 700 40)
  320  ├──────────────────────────────┤
       │        İÇERİK 352–1392        │  tek sütun, kenar 48, genişlik 984; kart + çizim + not üst üste;
       │   (1040 px, DOLU kullanılır)  │  figür + nesne tek sahnede bant ortasında; kartlar tam genişlik
 1392  ├──────────────────────────────┤
 1400  │   ALTYAZI 1400–1536 (2 satır) │  konuşulan parça, Lexend 500 44, satır 56, ortalı, renk mürekkep
 1536  ├──────────────────────────────┤
       │   PLATFORM 1536–1920  BOŞ     │  hiçbir öğe girmez (Shorts/Reels arayüzü)
 1920  └──────────────────────────────┘
```
Çip metinleri (ana BRIEF §3 ile aynı): `Hook` · `Example 1 / 3` · `Example 2 / 3` · `Example 3 / 3` · `Question` → `Form`.
Sahne 01 künyeyi uçuşla kurar (kapak kalıbı); 02–06 kare 0'dan sabit çizer. HyperFrames sahneleri aynı sayıları CSS'te
uygular (logo `<img>` 387×96 sol üst; ders adı; rozet; çip; altyazı `div` 1400–1536).

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

## 4. Sahne sözleşmeleri (içerik ve zamanlar ana BRIEF §4'ten; burada yalnız dikey yerleşim)
| # | Klasör / motor / kare | Dikey yerleşim (içerik bandı 352–1392, üstten alta) |
|---|---|---|
| 01 | `01-hyperframes-giris` HF 102 | Kapak kalıbı: logo damgası sol üst → rozetler `YDT · ADVANCED` + `GRAMMAR` → başlık 2 satır `SIMPLE` / `PAST` (190 px, y ≈ 520/740, kalemle, 0,65–1,45) → cümle 1 `Ago varsa Perfect yok.` Caveat 80 sözcük zamanlı (1,00'dan, y ≈ 900), `Perfect` kırmızı çizili (2,64) → figür standing-3 + saat (y 980–1380) → 2,0–3,0 uçuş; altyazı bandı cümle 1 |
| 02 | `02-paperjs-kanca` Paper.js 326 | Cümle 1 yazısı Caveat 80 (y 400–560); ORTA: takvim + saat eskizi 480 px; alt: ajanda kartı `rule · time words · traps` (y 1260–1392); 9,72'den Fredoka 64 iki satır `A finished action at a definite time in the past.` |
| 03 | `03-paperjs-ornek1` Paper.js 602 | Çip `Example 1 / 3`; kart `Marie Curie won her second Nobel Prize in 1911, three years before the war began.` Fredoka 64 (4 satır, y 400–700) sözcük zamanlı; ORTA: figür + kitap 460 px, sonra zaman çizgisi `1911 — 3 years — war`; alt: `win → won`, `begin → began` 96 ve `begun` kırmızı çizili (31,32) |
| 04 | `04-canvas-ornek2` canvas 487 | Çip `Example 2 / 3`; kart `We used to live in a village, and we would walk to school every morning.` (4 satır); ORTA: ev + okul arası yol + figür 480 px; etiketler `durum` / `alışkanlık` Caveat 64; alt: `would + walk` ✓ / `would + live` ✗ Fredoka 96 |
| 05 | `05-canvas-ornek3` canvas 528 | Çip `Example 3 / 3`; `TRAP` Fredoka 150 kırmızı (50,51); kart `The manager resigned two weeks ago, and the board has not found a replacement yet.` (4 satır); ORTA: iki zaman çizgisi üst üste `ago → Simple Past` / `yet → Present Perfect` Fredoka 96; çıkış fade |
| 06 | `06-hyperframes-form` HF 791 | Çip `Question` → `Form` (71,06'da); üst: öğrenci balonu + Caveat 64 `Hocam, ago varken has resigned yazsam olmaz mıydı?` (66,19–70,51); `Olmaz.` Fredoka 150 kırmızı (71,06); ORTA: kart `A definite time word blocks the present perfect.` 72, iki sütun `ago · last year · in 1911` / `for · since · yet`; alt: kod kartı `ago → Past`, `since → Perfect` Fredoka 110 (86,86–89,82); son 1 sn durgun; altyazı: cümle 6 ve 7 |

## 5. Çalıştırma ve kabul (sahne başına)
1. Sahne klasörü: D1'deki ile aynı dosya düzeni (`calistir.sh` tema.sh'ı `. "$D/../../ortak/tema.sh" "$@"` ile çağırır,
   `KAREYI_TUT`, yük bekçisi, `kontrol.png`, `k/*.png`, `RAPOR.md`, `olaylar.json`). Yol sabitleri
   `/projeler/simple-past-ileri-dikey/...`. `calistir.sh --tema acik` sonra `--tema koyu` (ikisi de; `video-acik.mp4` +
   `video-koyu.mp4` oluşur, `video.mp4` son koşunun kopyasıdır).
2. Editör kapısı (sayfa = konsol hatası 0 + durum eval; HTTP 200 kanıt DEĞİL): `ortak-tarayici` + `cdpilot context create`
   ile başsız bağlamda `http://127.0.0.1:3012/p/simple-past-ileri-dikey/onizle.html?surum=dikey-tam&tema=acik&t=<sn>`
   açılır; `cdpilot console` hata 0; `cdpilot eval "JSON.stringify(window.EDITOR.durum())"` → ilgili slot `hazir:true, goster:true`.
   (Sahne sayfasını tek başına da aç: `/projeler/simple-past-ileri-dikey/sahneler/<klasor>/sayfa.html?canli=1&tema=acik`.)
3. Kare kapısı (AJAN KENDİ GÖZÜYLE bakar): `k/*.png` 3 tam kare + `kontrol.png` Read ile açılır; ayrıca telefon ölçeği:
   `ffmpeg -i video.mp4 -vf "fps=1,scale=360:640,tile=3x2" k/telefon-%02d.png` üretilir ve BAKILIR. Ölçüt: HUD okunuyor,
   içerik bandı dolu (alt yarı boş DEĞİL), ≥ 64 px yazı, figür ≥ 420 px, altyazı bandında metin, platform bandı boş,
   çakışma 0. Uymayan kare → düzelt → yeniden yakala (raporda "neden yeniden" satırı).
4. RAPOR.md: kare sayısı, tema ikisi de, olay sayısı, kapı sonuçları (eval çıktısı, kontrol/telefon kare adları), açık sorular.
