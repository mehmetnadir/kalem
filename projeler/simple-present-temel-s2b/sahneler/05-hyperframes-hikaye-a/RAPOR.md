# Sahne 05 · hikâye karesi A, kural kartı — huni v2 (simple-present-temel-s2, HyperFrames 1080×1920, tek kare, ses yok) · 15.11.2026

Tema: acik

| Kapı | Sonuç |
|---|---|
| `calistir.sh --tema acik` | rc 0 · `png,1080,1920` · paket kökü `hikaye-a.png` + `hikaye.png` (`cp -p`, md5 ikisi de `59bbf8985b2d…`) |
| `calistir.sh --tema koyu` | rc 0 · `png,1080,1920` · `k/koyu/hikaye-a-koyu.png` (md5 `bfbbe834df4c…`) |
| `uret.py` assert'leri | rc 0 · `BX=230.9` · 7 blok, kesişim 0, dikey boşluk ≥ 12, içerik x 60–960 / y 460–1140, sarı `fill` tam 2 (rozet + hap) |
| Çakışma kapısı `node araclar/cakisma-kapisi.mjs simple-present-temel-s2 --sahne 05-hyperframes-hikaye-a --port 41333 --sunucu 41022` | çıkış 2 · `HATA sahne bulunamadı: 05-hyperframes-hikaye-a` (beklenen: araç yalnız `sahneler[]` okur); çakışma blok assert'i + gözle denetlendi |
| Metin taraması `grep -rniE 'tam ders\|dakika' … --include=*.html --include=*.js --include=*.py` | boş (grep çıkış 1) |
| İlk = orta = son (açık) | `hyperframes snapshot --at 0,0.5,0.966` → `k/qa/at-0s.png`, `at-0.5s.png`, `at-0.966s.png`; üçü ve teslim PNG aynı md5 `59bbf8985b2d…` |
| Kanal katmanı (piksel ölçümü, 4 kare: açık 3 + koyu) | 4 karede aynı: logo mürekkebi x 60–239, y 298–330 (resim kutusu 53,2–246,7 × 291–339) · `@ydspublishing` x 264–595, y 296–339 (taban 330). Emsal 02-04-s1/04 ve S2 sahne 03 ölçümüyle aynı |
| Boş bölgeler (piksel ölçümü, 4 kare; satır zemini x 0–40 medyanı, eşik 60) | 0–280 boş · 1150–1920 boş · sağ 961–1080 (y 280–1570) boş · içerik mürekkebi x 60–959, y 469–1130 |

Durum: yazıldı, iki temada tek kare yakalandı. mp4 yok, git yok. `zaman.json`, `BRIEF-S2.md`, `ortak/`, ana ders ve emsal değişmedi.

## Dosyalar
| Dosya | Kim | Not |
|---|---|---|
| `calistir.sh`, `olay.py`, `zamanlar.json` | emsal `02-04-ydt-temel-s1/sahneler/04-hyperframes-hikaye/` kopyası (`cp -p`) | şef Edit: yalnız başlık/belge satırları (sahne 05, paket adı). Çıktı adları emsalle aynı (`hikaye-a.png` + `hikaye.png`, `k/koyu/hikaye-a-koyu.png`) |
| `yardim.py` | aynı emsalin kopyası (`cp -p`) | şef Edit: `KONU = "Simple Present"` + belge dizgesi. `kunye_svg()` argümansız (kanal `<g id="kanal">` + `logoimg`, konu 34 px, rozet `YDT · BASIC`) |
| `SPEC.md` | şef | yerleşim, renk/tema tablosu, blok kutuları, 11 kural, kabul ölçütü; QA 1 düzeltmeleri işlendi |
| `uret.py` | agy-filo (rol kod, gemini-3.8-flash-high, 166 sn, 1 tur) | şef baştan sona okudu, SPEC'e uyuyordu; QA 1'de 2 küçük düzeltme (aşağıda) Edit ile |
| `proje/index.html`, `nesneler.json`, `olaylar.json` (`[]`) | `uret.py`, `olay.py` | 7 blok: kanal, kunye, soru, kart, ornek, otobus, kaydet |

## Öğe listesi (px)
| Öğe | Yazı · boy | Konum |
|---|---|---|
| Kanal + künye | logo + `@ydspublishing` Lexend 700 42 · `Simple Present` Fredoka 700 34 + `YDT · BASIC` | `Y.kunye_svg()`; y 291–434; rozet hapı x 309,7–513,2 |
| Soru | `Usually görünce hangi zaman?` · Caveat 700 72, mürekkep | x 60–796, taban 522 (mürekkep y 469–540) |
| Kural kartı | kâğıt `#fff9e6` (açık `#fffdf8`) + ince kenar `ikincil` 2 px + kalem kenarı 4,5 px (`pilMetin`) | kâğıt dış 60–960 × 556–863; kalem kenarı tabanı 76–944 × 568–851 (sabit kaydırma dizisi, tek `M`, sol üstte 14 px bindirme) |
| Kart yazısı | `Usually, always,` / `every day:` / `Simple Present.` · Fredoka 700 72 | blok ortalı, satırlar sola hizalı x 230,9; taban 635 / 719 / 811; hap x 230,9–789,1, y 749–837 (karenin tek sarısı; açık `#ffe066` + `#1b2440`, koyu `#f2a93b` + `#1b1a17`) |
| Örnek | `My brother usually goes` / `to school by bus.` · Fredoka 700 64, mürekkep | x 60, taban 925 / 1005 (blok 878–1021) |
| El altçizgisi | mürekkep, 5 px, iki `Q` eğrisi (sarı değil) | `usually` altında x 398,9–618,2, y ≈ 935–939 |
| Otobüs | `ortak/cizim/coco/bus.svg` (CC0), yalnız mürekkep yolu (beyaz dolgu atıldı) | x 786–954, y 948–1013 |
| Yer imi + `Kaydet` | Tabler `bookmark` yolu × 4,5, çizgi 6,3 px · Fredoka 700 88, mürekkep, hapsız | sağa yaslı: yazı sonu x 958, taban 1110; ikon x 588–648, y 1035–1123 |
| Boş zemin | — | y 1150–1920 (bağ çıkartması elle konur; kutu yok) |

## Bakılan kareler
| Kare | Bulgu |
|---|---|
| `hikaye-a.png` (QA 0) | açık; kalem kenarı kâğıdın kendi kenarında, `usually` altçizgisinin ucu `goes` `g` kuyruğuna 6 px |
| `k/koyu/hikaye-a-koyu.png` (QA 0) | **kusur:** kalem kenarı (`#1b1a17`) koyu zeminle birleşti; kart düz krem dikdörtgen gibi göründü, el çizimi kenar kayboldu |
| `hikaye-a.png` (QA 1, son) | kart sahne 03'teki gibi (kâğıt + içte kalem kenarı); altçizgi ile `goes` arası ≈ 11 px. Taşma, kesik yazı, binme yok; 0–280 ve 1150–1920 boş; sağ 960–1080 boş |
| `k/koyu/hikaye-a-koyu.png` (QA 1, son) | koyu zemin; krem kâğıt üstünde kalem kenarı görünür; hap `#f2a93b`; soru, örnek, otobüs, yer imi, `Kaydet` krem mürekkep; kontrast okunur |
| `k/qa/at-0s.png`, `at-0.5s.png`, `at-0.966s.png` | açık; üçü aynı md5, teslim PNG ile özdeş |

QA 1 düzeltmeleri (şef, `uret.py` Edit; SPEC de güncellendi):
1. Kâğıt dolgusu kalem kenarı yolundan ayrı `rect` oldu (dış 60–960 × 556–863, `#c9c2b3` 2 px); kalem kenarı tabanı 66–954 × 566–853 → 76–944 × 568–851.
   Kâğıt büyüdüğü için soru tabanı 528 → 522.
2. Altçizgi sağ ucu `usually` sonu + 6 → + 1.

## agy koşu özeti
- `uret.py`: `/home/sef/.claude/canavar/agy-filo/20261115-194236/ozet.md` (1/1 başarılı, gemini-3.8-flash-high, 166 sn).
- Özetteki "değişen" listesinde başka paket/sahne dosyaları var (`simple-present-temel-s1/07`, `/08`, `sozlesme.md`); bunlar aynı çalışma ağacındaki
  paralel oturumlarındır. Bu sahnede agy yalnız `uret.py` yazdı ve koşturdu (`proje/`, `nesneler.json`).

## Açık noktalar
1. **Soru satırı 28 karakter** (`Usually görünce hangi zaman?`): "satır ≤ 24 karakter" kuralını aşar. İstem bu metni tek satır bandında (460–560) ister; iki satır
   bu banda sığmaz. Genişlik 736 px ≤ 900 (assert ile çivili). Kısaltma (örn. `Usually → hangi zaman?`) kararı şefte.
2. **Bantlar BRIEF'ten kaydı:** üç satır Fredoka 72 + hap 88 olan kart 570–820 bandına sığmaz (en az ≈ 300 px). Kart 556–863, örnek 878–1021, Kaydet 1035–1131;
   içerik yine 460–1140 içinde, boşluklar 12–20 px (sıkışık ama binme yok). BRIEF tablosu güncellenmeli mi şef kararı (yazma kapsamı dışı).
3. **Çakışma kapısı ölçmüyor:** durağan kare `zaman.json → sahneler[]` dışında; araç çıkış 2 verir. Ölçüm: blok assert'i + piksel ölçümü + gözle.
4. **git:** `projeler/*/*.png` ve `k/` `.gitignore`'da; teslim commit'e girecekse `git add -f` gerekir. Commit yapılmadı.
5. Sözleşmeye 1 satır eklendi (`K/.claude/docs/sozlesme.md` son satır: kart bandı + koyu temada kalem kenarı dersi).
