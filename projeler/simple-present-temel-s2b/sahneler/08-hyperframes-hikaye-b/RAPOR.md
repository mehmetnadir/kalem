# Sahne 08 · hikâye karesi B, soru kartı — huni v2 (simple-present-temel-s2, HyperFrames 1080×1920, tek kare, ses yok) · 15.11.2026

Tema: acik

| Kapı | Sonuç |
|---|---|
| `calistir.sh --tema acik` | rc 0 · `png,1080,1920` · paket kökü `hikaye-b.png` (md5 `19bbf0b7e3f9…`); `hikaye.png` = A dokunulmadı (md5 `59bbf8985b2d…` = `hikaye-a.png`) |
| `calistir.sh --tema koyu` | rc 0 · `png,1080,1920` · `k/koyu/hikaye-b-koyu.png` (md5 `10a06b38bff6…`) |
| `uret.py` assert'leri | rc 0 · `baslik=471-557 kok=587-729 otobus=668-722 sikA=770-870 sikB=890-990 kural=1047-1113 kaydet=1030-1111` · 9 blok, kesişim 0, bant ve dikey boşluk ≥ 12, şık normalleştirme eşit, `#f2a93b` tam 1 (künye rozeti) |
| Çakışma kapısı `node araclar/cakisma-kapisi.mjs simple-present-temel-s2 --sahne 08-hyperframes-hikaye-b --port 41333 --sunucu 41022` | çıkış 2 · `HATA sahne bulunamadı: 08-hyperframes-hikaye-b` (beklenen: araç yalnız `zaman.json → sahneler[]` okur); çakışma blok assert'i + gözle denetlendi |
| Metin taraması `grep -rniE 'tam ders\|dakika' … --include=*.html --include=*.js --include=*.py` | boş (grep çıkış 1) |
| İlk = orta = son (açık) | `hyperframes snapshot --at 0,0.5,0.966` → `k/qa/at-0s.png`, `at-0.5s.png`, `at-0.966s.png`; üçü, `k/at-0.5s.png` ve teslim PNG aynı md5 `19bbf0b7e3f9…` |
| Kanal katmanı (piksel ölçümü, 4 kare: açık 3 + koyu) | 4 karede aynı: logo mürekkebi x 60–239, y 298–330 (resim kutusu 53,2–246,7 × 291–339) · `@ydspublishing` x 264/265–595, y 296–339 (taban 330). Hikâye A (`hikaye-a.png`) ölçümüyle aynı |
| Boş bölgeler (piksel ölçümü, 4 kare; satır zemini x 0–40 medyanı, eşik 60) | 0–280 boş · 1150–1920 boş · sağ 961–1080 (y 280–1570) boş · içerik mürekkebi x 60–957, y 472–1110 |

Durum: yazıldı, iki temada tek kare yakalandı. mp4 yok, git yok. `zaman.json`, `BRIEF-S2.md`, `ortak/`, başka sahneler, ana ders ve emsaller değişmedi.

## Dosyalar
| Dosya | Kim | Not |
|---|---|---|
| `calistir.sh`, `olay.py`, `zamanlar.json` | emsal `02-04-ydt-temel-s1/sahneler/04-hyperframes-hikaye/` kopyası (`cp -p`) | şef Edit: başlık/belge satırları; çıktı adı `hikaye-b.png`, `k/koyu/hikaye-b-koyu.png`; emsalin `hikaye.png` kopya satırı KALDIRILDI (`hikaye.png` = A kalır) |
| `yardim.py` | aynı emsalin kopyası (`cp -p`) | şef Edit: `KONU = "Simple Present"` + belge dizgesi. `kunye_svg()` argümansız (kanal `<g id="kanal">` + `logoimg`, konu 34 px, rozet `YDT · BASIC`) |
| `SPEC.md` | şef | sabitler, yerleşim şeması, öğe tablosu, blok kutuları, 14 kural, kabul ölçütü |
| `uret.py` | agy-filo (rol kod, gemini-3.8-flash-high, 307 sn, 1 tur) | şef baştan sona okudu; SPEC'e uyuyor, düzeltme gerekmedi |
| `proje/index.html`, `nesneler.json`, `olaylar.json` (`[]`) | `uret.py`, `olay.py` | 9 blok: kanal, kunye, baslik, kok, otobus, sikA, sikB, kural, kaydet |

## Öğe listesi (px)
| Öğe | Yazı · boy | Konum |
|---|---|---|
| Kanal + künye | logo + `@ydspublishing` Lexend 700 42 · `Simple Present` Fredoka 700 34 + `YDT · BASIC` | `Y.kunye_svg()`; y 291–434; rozet hapı x 309,7–513,2 (karenin tek sarısı) |
| Başlık | `Hangisi doğru?` · Fredoka 700 88, mürekkep | x 60, taban 536 (kutu 471–557) |
| Kök | `My brother usually` / `to school by bus.` · Fredoka 700 64, mürekkep; kart yok, `usually` vurgusuz | x 60, taban 634 / 714 (kutu 587–729) |
| Boşluk | kalem çizgisi `Q` eğrisi, 5 px, mürekkep | x 636,2–808,2, y 640–645 (genişlik 180: `goes` ≈ 134, `is going` ≈ 218; cevabı ele vermez) |
| Otobüs | `ortak/cizim/coco/bus.svg` (CC0), yalnız mürekkep yolu | x 818–956, y 668–722 (kökün sağ alt köşesi) |
| Şık A / B | el çizimi kart (tek `M`+`L` kalem yolu, 4 px, iki kartta aynı kaydırma dizisi) · harf rozeti (daire r 36, 4 px) + harf Fredoka 700 64 · metin `goes` / `is going` Fredoka 700 64; hepsi mürekkep | taban dikdörtgeni x 65–955 × 775–865 / 895–985; harf x 125 taban 839 / 959; metin x 186 taban 842 / 962 |
| Kural özeti | `usually = alışkanlık` · Caveat 700 64, mürekkep, sola yaslı | x 60, taban 1094 (kutu 1047–1113) |
| Yer imi + `Kaydet` | Tabler `bookmark` yolu × 4, çizgi 6 px, dolgusuz · Fredoka 700 72, mürekkep | sağa yaslı: yazı sonu x 958, taban 1094; ikon x 648–702, y 1030–1108 |
| Boş zemin | — | y 1150–1920 (bağ ya da test çıkartması elle konur; kutu yok) |

Cevap karede yok: tik, renk, dolgu farkı yok; iki şık normalleştirince aynı dize (assert). Doğru şık A yalnız `aciklama-b.md` satır 60'ta.

## Bakılan kareler
| Kare | Bulgu |
|---|---|
| `hikaye-b.png` (açık, teslim) | taşma, kesik yazı, binme yok; boşluk çizgisi `usually`dan ayrı, 2. satıra değmiyor; otobüs kök köşesinde, boşluktan ve şık A'dan ayrı; şıklar birebir aynı biçim; içerikte sarı yok; 0–280 ve 1150–1920 boş; sağ 960–1080 boş |
| `k/koyu/hikaye-b-koyu.png` | koyu zemin; bütün içerik krem mürekkep, kontrast okunur; rozet `#f2a93b`; kart kenarları ve yer imi görünür |
| `k/qa/at-0s.png`, `at-0.5s.png`, `at-0.966s.png` | açık; üçü aynı md5, teslim PNG ile özdeş |

Düzeltme turu: 0 (ilk koşu kabul ölçütünü geçti).

## agy koşu özeti
- `uret.py`: `/home/sef/.claude/canavar/agy-filo/20261115-195547/ozet.md` (1/1 başarılı, gemini-3.8-flash-high, 307 sn).
- Özetteki "değişen" listesinde başka sahne dosyaları var (`simple-present-temel-s1/06`, `sozlesme.md`); bunlar aynı çalışma ağacındaki paralel
  oturumlarındır. Bu sahnede agy yalnız `uret.py` yazdı ve koşturdu (`proje/`, `nesneler.json`); `yardim.py`, `calistir.sh`, `olay.py`,
  `zamanlar.json` zaman damgaları agy koşusundan önceki.

## Açık noktalar
1. **Şık metni:** istem `A) goes` · `B) is going` yazar ve "harf rozeti mürekkep" der; karede harf dairede, parantez yok (emsal 02-04-s2/07
   biçimi). Parantez istenirse yalnız `secenek_karti_svg` metni değişir.
2. **Kök kartsız:** istem kökü kart olarak tanımlamaz (yalnız şıklar "el çizimi kart"); kök hikâye A'nın örnek bloğu gibi düz yazı, otobüs köşede.
   Emsal 02-04-s2/07'de kök çerçeveliydi; istenirse çerçeve 580–740 bandına sığar.
3. **Şık kartı köşeleri** sivri (hikâye A kalem kenarı yapısı); kaydırma küçük olduğundan el çizimi etkisi hafif.
4. Paket kökü `hikaye-b.png` `.gitignore` satır 27 (`projeler/*/*.png`) ile izlenmez (hikâye A ile aynı); teslim dosyası diskte.
5. Yayın öncesi gerçek ekranda platform arayüzü ölçümü (standart §2) yapılmadı.
