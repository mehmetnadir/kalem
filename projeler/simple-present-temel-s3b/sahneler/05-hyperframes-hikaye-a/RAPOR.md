# Sahne 05 · hikâye karesi A, huni v2 (HyperFrames, 1080×1920, tek kare, ses yok; zaman çizelgesi dışı) · 15.11.2026

Tema: acik + koyu

| Kapı | Sonuç |
|---|---|
| `calistir.sh --tema acik` | rc 0 · `png,1080,1920` · `…/simple-present-temel-s3/hikaye-a.png` + `hikaye.png` (`cp -p`, md5 ikisi `e0356160a7fd…`) |
| `calistir.sh --tema koyu` | rc 0 · `png,1080,1920` · `…/05-hyperframes-hikaye-a/k/koyu/hikaye-a-koyu.png` (md5 `924289b2f213…`) |
| `uret.py` assert'leri | rc 0 · `index.html yazıldı` · 8 blok; kesişim 0; dikey boşluk ≥ 16; her blok kendi istem bandında; kırmızı 2 (yalnız `yanlis`), sarı 2 (rozet + hap) |
| Çakışma kapısı `node araclar/cakisma-kapisi.mjs simple-present-temel-s3 --sahne 05-hyperframes-hikaye-a --port 41333 --sunucu 41022` | çıkış 2 · `HATA sahne bulunamadı: 05-hyperframes-hikaye-a` (beklenen: araç yalnız `zaman.json → sahneler[]` okur; S1-VAR §5). Çakışma blok assert'iyle + piksel ölçümüyle + gözle denetlendi |
| Metin taraması `grep -rniE 'tam ders\|dakika' … --include=*.html/js/py` | boş (grep çıkış 1) |
| Kanal katmanı (piksel ölçümü, iki tema aynı) | logo mürekkebi x 60–239, y 298–330 (resim kutusu 53,2–246,7 × 291–339) · `@ydspublishing` x 265–595, y 296–339 (taban 330) · künye x 60–512, y 386–433. Emsal S1 s04 ölçümüyle aynı |
| İlk = orta = son | `snapshot --at 0,0.5,0.966` (açık, `k/qa/`): üç kare md5 `e0356160a7fd…`, teslim PNG ile aynı |
| Boş bölgeler (piksel ölçümü, iki tema) | 0–280 boş · 1150–1920 boş (bağ çıkartması alanı dahil; kutu yok) · sağ 961–1080 (y 280–1570) boş · içerik mürekkebi x 60–959, y 481–1139 |
| Renk (açık tema piksel örneği) | `✗` (214, 69, 58) = `#d6453a` · hap (255, 224, 102) = `#ffe066`; koyuda `#e0473b` / `#f2a93b` |

Durum: yazıldı, iki temada tek kare alındı. mp4 yok, git yok; `zaman.json`, `ortak/`, `BRIEF-S3.md`, ana ders ve emsal paket değişmedi.

## Dosyalar
| Dosya | Kim | Not |
|---|---|---|
| `SPEC.md` | şef | yerleşim, kimlikler, blok kutuları, 10 kural, kabul ölçütü; QA 1 değerleri işlendi |
| `uret.py` | agy-filo (rol kod, gemini-3.8-flash-high, 192 sn, 1 tur) | şef baştan sona okudu; SPEC'e uyuyor; 3 küçük Edit (aşağıda) |
| `yardim.py` | emsal `02-04-ydt-temel-s1/sahneler/04-hyperframes-hikaye/yardim.py` (`cp -p`, sha256 `6f42605c38be…`) | yalnız belge satırı ve `KONU = "Simple Present"` değişti (S3 s03/s04 kopyalarıyla aynı fark) |
| `calistir.sh`, `olay.py`, `zamanlar.json` | emsalden kopya | `calistir.sh`: başlık, paket adı, `uret.py`/`olay.py` iki satır (sözleşme: `a && b` + `set -e` hatayı yutar) |
| `nesneler.json`, `proje/index.html`, `olaylar.json` | `uret.py`, `olay.py` | 8 blok; olaylar boş liste |

agy koşu özeti: `/home/sef/.claude/canavar/agy-filo/20261115-193821/ozet.md` (1/1 başarılı). Özetteki "değişen" listesinde paralel
oturumların dosyaları da var (`sozlesme.md`, s1 kanca, 02-04-s2/s3 `kunye.js`); agy yalnız `uret.py` yazdı ve bir kez koşturdu.

## Olay listesi (tek kare)
| Olay | Kare / sn | Cümle sözcüğü |
|---|---|---|
| bütün öğeler görünür: kanal (logo + `@ydspublishing`) · künye (`Simple Present` + `YDT · BASIC`) · `Sınav tuzağı` (Caveat 64, ikincil) · kural kartı `Does varsa` / `fiil yalın.` (Fredoka 700 88, kâğıt kart + çerçeve) · `✗ He doesn't go`+çizili `es`+`.` (Fredoka 56, ikincil) · `✓ He doesn't go.` · `✓ Does she go?` (Fredoka 64) · yer imi + `Kaydet` sarı hap (Lexend 700 52) | kare 0 (yakalama 0,5 sn; çizelge 1,0 sn) | — (anlatım yok) |

Yerleşim (y, ölçülen): etiket 481–538 · kart 560–759 (yazı 578–742) · yanlış 794–851 · doğru 1 884–945 · doğru 2 974–1035 ·
kaydet 1060–1139 · boş 1150–1920. Sol simge sütunu x 60–112, yazı sütunu x 132. En uzun satır `He doesn't goes.` (16).

## Bakılan kareler ve bulgu
| Tur | Kare | Bulgu | Yapılan |
|---|---|---|---|
| 0 | `hikaye-a.png`, `k/koyu/hikaye-a-koyu.png` | taşma, kesik yazı, çakışma yok; iki temada kontrast iyi; boş bantlar boş. Yakın kırpım: `es` çizgisinin uçları `o`ya ve noktaya değiyor. Ölçüm: kart yazısı 581–745 (üst pay 17, alt 11) | çizgi uçları `x_es + 1 … x_es + w_es − 1`; kart tabanları 642/726 → 639/723 |
| 1 | aynı iki kare + `k/qa/at-{0,0.5,0.966}s.png` | çizgi yalnız `es` üstünde; kart payı 14/14; üç kare özdeş; tek sarı (hap), kırmızı yalnız `✗` + çizgi; yeşil ve emoji yok | — (geçti) |

Şef Edit'leri (uret.py): kural 6'daki boş assert'ler (`assert 64 >= 64`) boy sabitleri tablosuna çevrildi · kart tabanları (tur 0) ·
`es` çizgisi uçları (tur 0). SPEC aynı değerlerle güncellendi; tur 0 yedeği `~/Silinecekler/2026-11-15-0204/simple-present-temel-s3/sahneler/05-hyperframes-hikaye-a/tur0/`.

## Açık noktalar
1. **Çakışma kapısı ölçmüyor:** durağan kare `sahneler[]` dışında; araç çıkış 2 verir (beklenen). Ölçüm blok assert'i + piksel + gözle.
2. **Koyu temada "soluk" farkı az:** yanlış satır `ikincil` (`#c9c2b3`), mürekkep `#f3efe6`; açıkta fark belirgin (`#5a6275` / `#1b2440`). Kırmızı `✗` ve çizgi yanlışı yine açıkça işaretler; istenirse koyuda opaklık eklenir (şef/Nadir kararı).
3. **`✓` mürekkep, yeşil değil:** istem böyle istiyor (tek vurgu sarı); BRIEF-S3 renk listesindeki "doğru yeşil" bu karede kullanılmadı.
4. **`zaman.json → hikaye.cikti`** `hikaye-a.png` diyor; teslim `hikaye-a.png` + `hikaye.png` (aynı dosya). Uyumlu.
5. **git:** `projeler/*/*.png` ve `k/` `.gitignore`'da (emsal not); teslim commit'e girecekse `git add -f` gerekir.
6. Sağ yarı (x 540–960, y 780–1140) boş kalıyor: satırlar sol hizalı tek sütun, yazı boyu istemde sabit.
