# Simple Past — DİKEY tam ders (9:16, YDT BASIC) · `projeler/simple-past-temel-dikey`

Nadir 04.11 gece (ONAYLI): dikey sürüm = yatayla AYNI anlatım ve AYNI ses; sahne düzeni dikey için SIFIRDAN tasarlanır.
Yatay öğelerin döndürülmüş/responsive hâli YASAK. İzleyici telefondan bakar: 1080 px genişlik ekranda ≈ 390 CSS px olur
(ölçek 1/2,77). Bu BRIEF, ana `../simple-past-temel/BRIEF.md` üstüne gelir: stil (§2), kalem darbesi, çizim kaynakları,
ses olayları, kabul (§7) oradan aynen; yerleşim ve ölçek burada.

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
`zaman.json` hazır: 6 sahne, ana projeyle AYNI t_bas/t_son/kare (01 102 · 02 366 · 03 448 · 04 566 · 05 521 · 06 901), 1080×1920,
`gecis_kare` 12. Ses: `ortak/anlatim` → ana projeye sembolik bağ (`cumle-1..7.wav`, `anlatim.wav`, `sureler.json`,
`sozcukler.json`, `METIN.md`, `altyazi.json` [26 parça: {cumle, dil, t0, t1, metin, konusan}]). Yerel kare f ↔ küresel
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
| 01 | `01-hyperframes-giris` HF 102 | Kapak kalıbı: logo damgası sol üst (0,0–0,4) → rozetler `YDT · BASIC` + `GRAMMAR` → başlık 2 satır `SIMPLE` / `PAST` (190 px, y ≈ 520/740, kalemle, 0,65–1,45) → cümle 1 `Dün akşam amcamlara gittim.` Caveat 80 sözcük zamanlı (1,00'dan, y ≈ 900) → figür standing-3 + televizyon (y 980–1380, bant ortası) → 2,0–3,0 uçuş: başlık künye ders adına küçülür, cümle yukarı kayar, figür solar; altyazı bandı cümle 1 |
| 02 | `02-paperjs-kanca` Paper.js 366 | Kanca cümlesi Caveat 80 iki satır (y 400–560), `gittim` sarı daire; altında `-di → biten iş` + takvim (y 620–720, 64 px); ORTA: figür ev yönünde + ev + hilal, 480 px (y 760–1240); alt: `I visited my uncle last night.` Fredoka 64 (6,02'de) ve ajanda kartı `form · time expressions · irregular verbs` üç satır (y 1260–1392), cümle 2 sözcük zamanında belirir; altyazı: cümle 2 parçaları |
| 03 | `03-paperjs-ornek1` Paper.js 448 | Çip `Example 1 / 3`; kart tam genişlik: `I watched a movie last night.` Fredoka 72 (3 satır, y 400–660) sözcük zamanlı; TR `Dün gece bir film izledim.` Caveat 64 (y 700); ORTA: oturan figür + televizyon 460 px (y 760–1220); alt: formül `watch + -ed` → `watched` Fredoka 110 (y 1240–1380); altyazı: cümle 3 parçaları |
| 04 | `04-canvas-ornek2` canvas 566 | Çip `Example 2 / 3`; kart `My uncle went to London two years ago.` (3 satır); TR Caveat 64; ORTA: figür + uçak 460 px; takvim şeridi `two years ago` (Caveat 64); alt: `go → went` 110, `-ed` kırmızı çizili |
| 05 | `05-canvas-ornek3` canvas 521 | Çip `Example 3 / 3`; kart `We didn't play football yesterday.`; TR Caveat 64; ORTA: figür + futbol topu üstü çarpı, 480 px; not `didn't + V1`; alt: `Did you play football?` Fredoka 72; çıkış fade |
| 06 | `06-hyperframes-form` HF 901 | Çip `Question` → `Form` (69,33'te); üst: öğrenci balonu (ogrenci-bas.svg, baş 160 px) + Caveat 64 `Hocam, birinde -ed var, ikisinde yok. Neden?` (64,78–68,78, y 400–640); ORTA: iki kolon `düzenli + -ed` / `düzensiz V2` Fredoka 96 (y 700–1060), sonra `didn't + V1` / `Did + özne + V1?`; alt: `izle-di = watch-ed` Fredoka 110 (82,03–83,07); zaman ifadeleri `yesterday · ago · last year` kutularda (84,34'ten); son 1 sn durgun; altyazı: cümle 6 ve 7 |

## 5. Çalıştırma ve kabul (sahne başına)
1. Sahne klasörü: D1'deki ile aynı dosya düzeni (`calistir.sh` tema.sh'ı `. "$D/../../ortak/tema.sh" "$@"` ile çağırır,
   `KAREYI_TUT`, yük bekçisi, `kontrol.png`, `k/*.png`, `RAPOR.md`, `olaylar.json`). Yol sabitleri
   `/projeler/simple-past-temel-dikey/...`. `calistir.sh --tema acik` sonra `--tema koyu` (ikisi de; `video-acik.mp4` +
   `video-koyu.mp4` oluşur, `video.mp4` son koşunun kopyasıdır).
2. Editör kapısı (sayfa = konsol hatası 0 + durum eval; HTTP 200 kanıt DEĞİL): `ortak-tarayici` + `cdpilot context create`
   ile başsız bağlamda `http://127.0.0.1:3012/p/simple-past-temel-dikey/onizle.html?surum=dikey-tam&tema=acik&t=<sn>`
   açılır; `cdpilot console` hata 0; `cdpilot eval "JSON.stringify(window.EDITOR.durum())"` → ilgili slot `hazir:true, goster:true`.
   (Sahne sayfasını tek başına da aç: `/projeler/simple-past-temel-dikey/sahneler/<klasor>/sayfa.html?canli=1&tema=acik`.)
3. Kare kapısı (AJAN KENDİ GÖZÜYLE bakar): `k/*.png` 3 tam kare + `kontrol.png` Read ile açılır; ayrıca telefon ölçeği:
   `ffmpeg -i video.mp4 -vf "fps=1,scale=360:640,tile=3x2" k/telefon-%02d.png` üretilir ve BAKILIR. Ölçüt: HUD okunuyor,
   içerik bandı dolu (alt yarı boş DEĞİL), ≥ 64 px yazı, figür ≥ 420 px, altyazı bandında metin, platform bandı boş,
   çakışma 0. Uymayan kare → düzelt → yeniden yakala (raporda "neden yeniden" satırı).
4. RAPOR.md: kare sayısı, tema ikisi de, olay sayısı, kapı sonuçları (eval çıktısı, kontrol/telefon kare adları), açık sorular.
