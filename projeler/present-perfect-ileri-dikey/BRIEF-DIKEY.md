# Present Perfect — DİKEY tam ders (9:16, YDT ileri) · `projeler/present-perfect-ileri-dikey`

Dikey sürüm = yatayla AYNI anlatım ve AYNI ses; sahne düzeni dikey için SIFIRDAN tasarlanır (yatay öğelerin döndürülmüş hâli YASAK).
İzleyici telefondan bakar: 1080 px ≈ 390 CSS px (ölçek 1/2,77). Bu BRIEF, ana `../present-perfect-ileri/BRIEF.md` üstüne gelir: stil, kalem darbesi,
çizim kaynakları, ses olayları, kabul oradan aynen; yerleşim ve ölçek burada. Kod `ING-YDT-GR-02-06-I-D`. Yaklaşım: tümdengelim: formül önce, 3 YDT kökü (since+Simple Past, for, ago tuzağı), EN payı ≈ %40, öğrenci yanlış kavramı.

## 0. Nadir'in 04.11 gece dikey bulguları (D1/S1 kare incelemesi, şef gözü — bunlar düzeltilmiş olmalı)
| Sorun (D1/S1) | Kural (bu projede) |
|---|---|
| İçerik üst %55'e yığılı, alt yarı boş | içerik bandı 352–1392 (1040 px) DOLDURULUR; her sahne bitiminde bandın ≥ %85'i kullanılmış |
| Logo 48 px, boşlukta yüzüyor (y 1464) | logo HUD sol üst, 96 px yüksek (en 387); alt bantta logo yok |
| Ders adı 36, rozet 24, çip 26 px → telefonda 9–13 CSS px, okunmaz | ders adı 56 · rozet yazısı 36 (hap 72) · çip yazısı 40 (hap 80) |
| Caveat notlar 56–60 px gri (`ikincil`) → soluk | içerik yazısı en az 64 px; `ikincil` renk yalnız ≥ 72 px'te; TR çeviri Caveat 64 `murekkep` |
| Figür + nesne küçük (≈ 250 px), köşede | figür 420–560 px yüksek, nesneyle birlikte bant ortasında tek sahne; kalınlık w 4,0–4,8 |
| Altyazı bandı boş | 1400–1536 bandında konuşulan parça (altyazi.json), Lexend 500 44, ≤ 2 satır, ortalı |

## 1. Teknik çerçeve
`zaman.json` hazır: 6 sahne, ana projeyle AYNI t_bas/t_son/kare (01 102 · 02 461 · 03 490 · 04 533 · 05 532 · 06 785), 1080×1920,
`gecis_kare` 12. Ses: `ortak/anlatim` → ana projeye sembolik bağ (`cumle-1..7.wav`, `anlatim.wav`, `sureler.json`,
`sozcukler.json`, `METIN.md`, `altyazi.json` [parça başına {cumle, dil, t0, t1, metin, konusan}]). Yerel kare f ↔ küresel
`t_bas + f/30`. İlk/son 12 kare geçiş altında DURGUN. Kareler `ortak/yakala.py ... 1080 1920`. HyperFrames kökü
`data-width="1080" data-height="1920"`. Ortak dosyalar: `ortak/kunye.js` (dikey v2), `ortak/kalem-canvas.js`, `ortak/tema.sh`,
`ortak/hf_tema.py`, `ortak/{cizim,font,logo}`. Çizim listesi: ana BRIEF §1 (yalnız `ortak/cizim/` içinde VAR olanlar).
Şablon olarak `../present-continuous-dikey/sahneler/*` okunabilir (yerleşim oradan alınmaz).

## 2. Bantlar ve HUD (px, 1080×1920)
```
y    0 ┌──────────────────────────────┐
       │ [logo 387×96]        [çip 80] │  HUD 0–320: logo sol üst y48 · ders adı Fredoka 700 56 taban y212
       │ PRESENT PERFECT            │  rozet hapı y236 h72 (Lexend 700 36) · "şu an" çipi sağ üst y48 h80 (Lexend 700 40)
  320  ├──────────────────────────────┤
       │        İÇERİK 352–1392        │  tek sütun, kenar 48, genişlik 984; kart + çizim + not üst üste;
       │   (1040 px, DOLU kullanılır)  │  figür + nesne tek sahnede bant ortasında; kartlar tam genişlik
 1392  ├──────────────────────────────┤
 1400  │   ALTYAZI 1400–1536 (2 satır) │  konuşulan parça, Lexend 500 44, satır 56, ortalı, renk mürekkep
 1536  ├──────────────────────────────┤
       │   PLATFORM 1536–1920  BOŞ     │  hiçbir öğe girmez (Shorts/Reels arayüzü)
 1920  └──────────────────────────────┘
```
Çip metinleri: `Hook` · `Rule` · `Exam Q 1 / 3` · `Exam Q 2 / 3` · `Trap 3 / 3` · `Question` → `Rule`.
Sahne 01 künyeyi uçuşla kurar (kapak kalıbı); 02–06 kare 0'dan sabit çizer. HyperFrames sahneleri aynı sayıları CSS'te
uygular (logo `<img>` 387×96 sol üst; ders adı; rozet; çip; altyazı `div` 1400–1536).

## 3. Ölçek (telefon kuralı — altına inilmez)
| Rol | Yazı | Boy (px) | Renk |
|---|---|---|---|
| İngilizce örnek cümle (kart içinde, sözcük zamanlı) | Fredoka 700 | 72 (3 satıra sığmazsa 64) | mürekkep; okunan sözcük altı sarı |
| Türkçe çeviri / kanca cümlesi | Caveat 700 | 64–80 | mürekkep |
| El notu, ok etiketi ("şimdiki zaman", "= iş sürüyor") | Caveat 700 | 64 (ikincil yalnız ≥ 72) | vurgu ya da mürekkep |
| Formül / anahtar sözcük (`have + V3`, `S + have / has + V3`, `ago → Simple Past`) | Fredoka 700 | 110–160 | mürekkep + vurgu |
| Kapak başlığı (sahne 01) | Fredoka 700 | 190–230, 2 satır, kontur 12 | mürekkep / vurgu |
| Kart | kenar 4 px kalem çizgisi, iç boşluk 40, genişlik 984 | | |
| Figür / nesne | 420–560 px yüksek; kalınlık figür 4,0–4,8, nesne 4,0; belirteç (daire/altı/ok) w 9–12 | | |
Satır başına en çok 24 karakter (Caveat 64'te 984 px'e sığar). Güvenli alan: kenar 48, HUD/altyazı bandına 0 taşma.
Hareket kuralları ana BRIEF §2.6 (ease-out, ≤ 4 sn durağanlık, çakışma 0 px, hiçbir öğe kaybolmaz — yer açmak için
yukarı toplanır ve küçülür, ama küçülünce de ≥ 48 px kalır).

## 4. Sahne sözleşmeleri (içerik ve zamanlar ana BRIEF §4'ten; burada yalnız dikey yerleşim)
| # | Klasör / motor / kare | Dikey yerleşim (içerik bandı 352–1392, üstten alta) |
|---|---|---|
| 01 | `01-hyperframes-giris` HF 102 | Kapak kalıbı: logo damgası sol üst → rozetler `YDT · ADVANCED` + `GRAMMAR` → başlık 2 satır `PRESENT` / `PERFECT` (190 px, y ≈ 520/740, kalemle, 0,65–1,45) → cümle 1 `Ago varsa Present Perfect yok.` Caveat 80 sözcük zamanlı (1,00'dan, y ≈ 900; `Ago` kırmızı alt çizgi) → uçak + saat (y 980–1380) → 2,0–3,0 uçuş; altyazı bandı cümle 1 |
| 02 | `02-paperjs-kanca` Paper.js 461 | Çip `Rule`; ORTA büyük formül kartı `S + have / has + V3` Fredoka 110 (y 500–900), EN formül cümlesi altyazıda; üstte 3 madde (`formula` · `since / for` · `Simple Past trap`) Fredoka 64 tik zamanlı (4,91 / 6,19 / 7,79); alt: üç mini kutu `1 · 2 · 3` (15,57'de) |
| 03 | `03-paperjs-ornek1` Paper.js 490 | Çip `Exam Q 1 / 3`; kart `Ever since the company launched its new app, the number of users has doubled.` Fredoka 64 (4 satır, y 400–720) sözcük zamanlı, `since` / `launched` sarı daire; TR Caveat 64; ORTA: telefon + büyüyen sütun grafik 460 px; alt: `since + Simple Past → Present Perfect` Fredoka 72 iki satır |
| 04 | `04-canvas-ornek2` canvas 533 | Çip `Exam Q 2 / 3`; kart `Selim has worked at this bank for thirty years, so he knows every customer.` (4 satır, `for thirty years` sarı); TR Caveat 64; ORTA: figür (sitting-5) + dizüstü 460 px; takvim şeridi `30 years`; alt: `for + süre` / `since + başlangıç` Fredoka 96 |
| 05 | `05-canvas-ornek3` canvas 532 | Çip `Trap 3 / 3`; kart `The plane took off two hours ago, but it hasn't landed yet.` (`two hours ago` kırmızı alt çizgi, `hasn't landed yet` sarı daire); TR Caveat 64; ORTA: uçak 480 px kalkış eğrisi + `finished | now | unfinished` çizgisi; alt: iki etiket `ago → Simple Past` (kırmızı) / `yet → Present Perfect` (sarı) Fredoka 72; çıkış fade |
| 06 | `06-hyperframes-form` HF 785 | Çip `Question` → `Rule` (73,62'de); üst: öğrenci balonu + Caveat 64 `Hocam, ago varken de has landed diyemez miyiz?` (69,15–73,07), `has landed` kırmızı çarpı; ORTA: 3 kırmızı etiket `ago` · `yesterday` · `last year` (78,35 / 79,27 / 80,27) yasak çizgili; iki sütun `Finished → Simple Past` / `Unfinished → Present Perfect` Fredoka 80 (82,12 / 84,68); alt: kod kartı `ago → Simple Past` / `yet → Present Perfect` Fredoka 110 (87,09); son 1 sn durgun; altyazı: cümle 6 ve 7 |

## 5. Çalıştırma ve kabul (sahne başına)
1. Sahne klasörü: D1'deki ile aynı dosya düzeni (`calistir.sh` tema.sh'ı `. "$D/../../ortak/tema.sh" "$@"` ile çağırır,
   `KAREYI_TUT`, yük bekçisi, `kontrol.png`, `k/*.png`, `RAPOR.md`, `olaylar.json`). Yol sabitleri
   `/projeler/present-perfect-ileri-dikey/...`. `calistir.sh --tema acik` sonra `--tema koyu` (ikisi de; `video-acik.mp4` +
   `video-koyu.mp4` oluşur, `video.mp4` son koşunun kopyasıdır).
2. Editör kapısı (sayfa = konsol hatası 0 + durum eval; HTTP 200 kanıt DEĞİL): `ortak-tarayici` + `cdpilot context create`
   ile başsız bağlamda `http://127.0.0.1:3012/p/present-perfect-ileri-dikey/onizle.html?surum=dikey-tam&tema=acik&t=<sn>`
   açılır; `cdpilot console` hata 0; `cdpilot eval "JSON.stringify(window.EDITOR.durum())"` → ilgili slot `hazir:true, goster:true`.
   (Sahne sayfasını tek başına da aç: `/projeler/present-perfect-ileri-dikey/sahneler/<klasor>/sayfa.html?canli=1&tema=acik`.)
3. Kare kapısı (AJAN KENDİ GÖZÜYLE bakar): `k/*.png` 3 tam kare + `kontrol.png` Read ile açılır; ayrıca telefon ölçeği:
   `ffmpeg -i video.mp4 -vf "fps=1,scale=360:640,tile=3x2" k/telefon-%02d.png` üretilir ve BAKILIR. Ölçüt: HUD okunuyor,
   içerik bandı dolu (alt yarı boş DEĞİL), ≥ 64 px yazı, figür ≥ 420 px, altyazı bandında metin, platform bandı boş,
   çakışma 0. Uymayan kare → düzelt → yeniden yakala (raporda "neden yeniden" satırı).
4. RAPOR.md: kare sayısı, tema ikisi de, olay sayısı, kapı sonuçları (eval çıktısı, kontrol/telefon kare adları), açık sorular.
