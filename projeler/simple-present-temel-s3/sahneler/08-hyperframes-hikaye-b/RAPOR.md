# Sahne 08 · hikâye karesi B, huni v2 (HyperFrames, 1080×1920, tek kare, ses yok; zaman çizelgesi dışı) · 15.11.2026

Tema: acik + koyu

| Kapı | Sonuç |
|---|---|
| `calistir.sh --tema acik` | rc 0 · `png,1080,1920` · `…/simple-present-temel-s3/hikaye-b.png` (md5 `3715a8a90e81…`) |
| `calistir.sh --tema koyu` | rc 0 · `png,1080,1920` · `…/08-hyperframes-hikaye-b/k/koyu/hikaye-b-koyu.png` (md5 `28958f5af1c5…`) |
| `uret.py` assert'leri | rc 0 · `index.html yazıldı` · 8 blok; kesişim 0; ardışık boşluk ≥ 16 (şık A → B ≥ 12); her blok kendi istem bandında; kırmızı 0, sarı 2 (rozet + hap), yeşil 0; sahne SVG'sinde `_`, `✗`, `✓` yok |
| Çakışma kapısı `node araclar/cakisma-kapisi.mjs simple-present-temel-s3 --sahne 08-hyperframes-hikaye-b --port 41333 --sunucu 41022` | çıkış 2 · `HATA sahne bulunamadı: 08-hyperframes-hikaye-b` (beklenen: araç yalnız `zaman.json → sahneler[]` okur; S1-VAR §5). Çakışmayı blok assert'i, piksel ölçümü ve göz denetledi |
| Metin taraması `grep -rniE 'tam ders\|dakika' … --include=*.html --include=*.js --include=*.py` | boş (grep çıkış 1) |
| Kanal katmanı (piksel, iki tema aynı) | logo mürekkebi x 60–239, y 298–330 (resim kutusu 53,2–246,7 × 291–339) · `@ydspublishing` x 264–595, y 296–339 (taban 330) · künye x 60–512, y 386–433. Sahne 05 ölçümüyle aynı |
| İlk = orta = son | `snapshot --at 0,0.5,0.966` (açık, `k/qa/`): üç kare md5 `3715a8a90e81…`, teslim PNG ile aynı |
| Boş bölgeler (piksel, iki tema) | 0–280 boş · 1150–1920 boş (bağ çıkartması alanı dahil; kutu yok) · sağ 961–1080 (y 280–1570) boş |
| Renk (piksel örneği) | hap açıkta (255, 224, 102) = `#ffe066`, koyuda (242, 169, 59) = `#f2a93b`; yazılar `murekkep` |

Durum: yazıldı, iki temada tek kare alındı. mp4 yok, git yok; `zaman.json`, `ortak/`, `BRIEF-S3.md`, ana ders ve emsal paket değişmedi.

## Dosyalar
| Dosya | Kim | Not |
|---|---|---|
| `SPEC.md` | şef | sabitler, yerleşim, kimlikler, blok kutuları, 11 kural, kabul ölçütü |
| `uret.py` | agy-filo (rol kod, gemini-3.8-flash-high, 176 sn, 1 tur) | şef baştan sona okudu; SPEC'e uyuyor; 1 Edit: 131 karakterlik `for` satırı `siklar` değişkenine bölündü |
| `yardim.py` | emsal `02-04-ydt-temel-s1/sahneler/07-hyperframes-hikaye-b/yardim.py` (`cp -p`) | belge satırı ve `KONU = "Simple Present"` değişti; sahne 05 kopyasıyla belge satırı dışında aynı (`diff`) |
| `calistir.sh`, `olay.py`, `zamanlar.json` | emsalden kopya | `calistir.sh`: başlık ve paket adı yorumu; çıktı adları (`hikaye-b.png`, `hikaye-b-koyu.png`) emsalle aynı |
| `nesneler.json`, `proje/index.html`, `olaylar.json` | `uret.py`, `olay.py` | 8 blok; olaylar boş liste |

agy koşu özeti: `/home/sef/.claude/canavar/agy-filo/20261115-195024/ozet.md` (1/1 başarılı). Özetteki "değişen" listesinde paralel
oturumların dosyaları da var (`sozlesme.md`, simple-present-temel-s1 s07); agy yalnız `uret.py` yazdı ve bir kez koşturdu.

## Olay listesi (tek kare)
| Olay | Kare / sn | Cümle sözcüğü |
|---|---|---|
| bütün öğeler görünür: kanal (logo + `@ydspublishing`) · künye (`Simple Present` + `YDT · BASIC`) · `Hangisi doğru?` (Fredoka 700 88) · kök `Does she` + kalem boşluk çizgisi (200 px) / `to school?` (Fredoka 700 64) · şık kartı `A) go` · şık kartı `B) goes` (Fredoka 700 64, dolgusuz çerçeve, aynı biçim, sarı yok) · `Does varsa fiil yalın.` (Fredoka 700 56) · yer imi + `Kaydet` hapı (Lexend 700 52) | kare 0 (yakalama 0,5; çizelge 1,0); küresel sn yok (zaman çizelgesi dışı) | — (anlatım yok) |

Yerleşim (y, ölçülen mürekkep): başlık 480–564 · kök 605–733 · şık A 772–857 (yazı 783–846) · şık B 872–957 (yazı 883–946) ·
özet 986–1039 · kaydet 1060–1139 · boş 1150–1920. İçerik x 60–959. En uzun satır `Does varsa fiil yalın.` (22).
Cevap karede yok (doğru şık A; yalnız `hikaye-taslak.md` §4 ve açıklama notunda).

## Bakılan kareler ve bulgu
| Tur | Kare | Bulgu | Yapılan |
|---|---|---|---|
| 0 | `hikaye-b.png`, `k/koyu/hikaye-b-koyu.png` | taşma, kesik yazı, üst üste binme yok; iki temada kontrast iyi; boşluk çizgisi (y 655–663) `to school?` satırına değmiyor (satır üstü 685, ara 22 px); şık yazısı kartta ortalı (üst 7, alt 8 px iç pay); boş bantlar boş | — (geçti) |
| 1 | `k/qa/at-{0,0.5,0.966}s.png` | üç kare özdeş, teslim PNG ile aynı | — |

## Açık noktalar
1. **Çakışma kapısı ölçmüyor:** durağan kare `sahneler[]` dışında; araç çıkış 2 verir (beklenen). Ölçüm blok assert'i + piksel + göz.
2. **Şık kartları tam genişlik (900 px), yazı kısa:** kartın sağ kısmı boş kalıyor. İstem bantları alt alta iki şık istiyor; S1 s08'deki
   yan yana 420 px kartlar başka bir düzen. Değişiklik şef/Nadir kararı.
3. **Şık biçimi `A) go` düz yazı:** S2 hikâye B harf dairesi kullanıyordu; istem `A) go` metnini verdiği için daire yok.
4. **git:** `projeler/*/*.png` ve `k/` `.gitignore`'da (emsal not); teslim commit'e girecekse `git add -f` gerekir.
