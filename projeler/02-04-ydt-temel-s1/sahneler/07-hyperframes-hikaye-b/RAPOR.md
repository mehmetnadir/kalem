# Sahne 07 · hikâye karesi B, huni v2 (HyperFrames, 1080×1920, tek kare, ses yok; zaman çizelgesi dışı) · 15.11.2026

Tema: acik

| Kapı | Sonuç |
|---|---|
| `calistir.sh --tema acik` | rc 0 · `png,1080,1920` · `…/02-04-ydt-temel-s1/hikaye-b.png` (md5 `59400053e5ec…`) |
| `calistir.sh --tema koyu` | rc 0 · `png,1080,1920` · `…/k/koyu/hikaye-b-koyu.png` (md5 `42281655490…`) |
| `uret.py` assert'leri | rc 0 · `index.html yazıldı 7183` · 7 blok, kesişim 0, dikey boşluk ≥ 16, içerik x 60–960 / y 460–1140, kaydet y 1400–1520 |
| Çakışma kapısı `cakisma-kapisi.mjs 02-04-ydt-temel-s1 --sahne 07-hyperframes-hikaye-b --port 41333 --sunucu 41022` | çıkış 2 · `HATA sahne bulunamadı: 07-hyperframes-hikaye-b` (beklenen: araç yalnız `sahneler[]` okur, S1-VAR §5); çakışma blok assert'i + piksel ölçümü + gözle denetlendi |
| Metin taraması `grep -rniE 'tam ders\|dakika' … --include=*.html/js/py` | boş (grep çıkış 1) |
| Kanal katmanı (piksel ölçümü) | açık + koyu aynı: logo mürekkebi x 60–239, y 298–330 (resim kutusu 53,2–246,7 × 291–339) · `@ydspublishing` x 265–595, y 296–339 (taban 330). Sahne 03 ve 04 ölçümüyle aynı |
| İlk = orta = son | `snapshot --at 0,0.5,0.966` (açık): üç kare md5 `59400053e5ec…`, teslim PNG ile aynı (`k/qa/`) |
| Boş bölgeler (piksel ölçümü, iki tema) | 0–280 boş · 1150–1380 boş · 1570–1920 boş · sağ 961–1080 (y 280–1570) boş · künye x 60–867, y 386–433 · içerik x 60–959, y 482–1132 · kaydet x 60–415, y 1416–1503 |

Durum: yazıldı, iki temada tek kare yakalandı. mp4 yok, git yok, `zaman.json` değişmedi.

## Dosyalar
| Dosya | Kim | Not |
|---|---|---|
| `SPEC.md` | şef | yerleşim, blok kutuları, kurallar, kabul ölçütü; QA 1 düzeltmesi (yeşil sayımı) işlendi |
| `uret.py` | agy-filo (rol kod, gemini-3.8-flash-high, 118 sn, 1 tur) | şef baştan sona okudu; SPEC'e uyuyor; 1 küçük Edit (aşağıda) |
| `yardim.py` | sahne 04'ün v2 kopyası (`cp -p`) | sha256 `6f42605c38be…` (03 ve 04 ile aynı, kapıdan geçmiş): `kunye_svg()` → `<g id="kanal">` (`#logoimg` + `#kanal-yazi`) + konu 34 px + rozet `YDT · BASIC`; `HUD` v2 bantları (kenar 60, içerik 460–1380, altyazı 1400–1550) |
| `calistir.sh` | şef Edit | başlık yorumu v2; `uret.py` ile `olay.py` ayrı satır (aşağıda, hata yutma onarımı) |
| `nesneler.json`, `proje/index.html` | uret.py | 7 blok: kanal, kunye, tr, dogru, yanlis, ozet, kaydet |

Eski sürüm yedeği: `~/Silinecekler/2026-11-15-huni-v2/02-04-ydt-temel-s1/sahneler/07-hyperframes-hikaye-b/v1/` (SPEC, uret.py, yardim.py,
calistir.sh, json'lar, `proje/index.html`, `k/`); eski `hikaye-b.png` paket yedeğinde zaten vardı. `LISTE.md`'ye satır eklendi.

agy koşu özeti: `/home/sef/.claude/canavar/agy-filo/20261115-191424/ozet.md` (1/1 başarılı). Özetteki "değişen" listesinde paralel
oturumların dosyaları da var (`sozlesme.md`, 02-03 kapak fontları); agy yalnız `uret.py` yazdı.

## Olay listesi (tek kare)
| Olay | Kare / sn | Cümle sözcüğü |
|---|---|---|
| bütün öğeler görünür: kanal (logo + `@ydspublishing`) · künye (`Simple Present vs Present Continuous` + `YDT · BASIC`) · `Şimdilik amcamla` / `yaşıyorum.` (Fredoka 76) · doğru şık kartı `I am living` / `with my uncle.` (Fredoka 72, yeşil çerçeve 6 px + yeşil tik) · yanlış şık `I live with my uncle.` (Fredoka 64, opaklık 0,45, gri üstü çizgi) · `Kalıcıysa geniş zaman,` / `geçiciyse şimdiki zaman.` (Fredoka 68) · yer imi + `Kaydet` sarı hap | kare 0 (yakalama 0,5 sn; çizelge 1,0 sn) | — (anlatım yok; kural özeti BRIEF-S1 girişi) |

Yerleşim (y): kanal 291–339 · künye 386–434 · tr 481–641 · doğru kartı 664–864 (x 60–960) · yanlış 888–952 · özet 984–1134 ·
boş 1150–1380 · kaydet 1416–1504 · boş 1570–1920. En uzun satır `geçiciyse şimdiki zaman.` (24).
Renk: açık tema yeşil `#167a4a`, koyu tema `#4fbf85` (sahne CSS'i `#root:not(.tema-acik) [stroke="#167a4a"]`); sarı yalnız `Kaydet` hapı
(+ künye rozeti, kalıbın parçası); kırmızı ve emoji yok.

## Bakılan kareler ve bulgu
| Tur | Kare | Bulgu | Yapılan |
|---|---|---|---|
| 0 | `hikaye-b.png`, `k/koyu/hikaye-b-koyu.png` | **v1 karesi çıktı** (Quiz çipi, A/B kartları), yine rc 0. Kök: `uret.py` assert'i düştü (`stroke="#167a4a"` 3 ≠ 2; CSS seçicisi de sayıldı, SPEC hatası) ve `calistir.sh` içindeki `uret.py && olay.py` zinciri hatayı yuttu, eski `index.html` yakalandı | assert yalnız `<svg id="sahne">` sonrasını sayar (şef Edit); `calistir.sh` iki ayrı satır (şef Edit) |
| 1 | aynı iki kare + `k/qa/at-{0,0.5,0.966}s.png` | taşma, kesik yazı, üst üste binme yok (üstü çizgi yanlış şıkta bilerek); kontrast iki temada iyi; 0–280, 1150–1380, 1570–1920 ve sağ 961–1080 boş; üç kare özdeş | — (geçti) |

## Açık noktalar
1. **Aynı hata yutma 6 sahnede daha var** (yazma kapsamı dışı, dokunulmadı): `01-hyperframes-kapak`, `03-hyperframes-cta`,
   `04-hyperframes-hikaye`, `05-hyperframes-kapak-b`, `06-hyperframes-kapak-c`, `08-hyperframes-kaydet` → `calistir.sh` içinde
   `uret.py >&2 && olay.py >&2`. uret.py düşerse eski kare rc 0 ile teslim olur. Önerim: aynı iki satırlık onarım; sözleşmeye satır yazıldı.
2. **Çakışma kapısı ölçmüyor:** durağan kare `zaman.json → sahneler[]` dışında; araç çıkış 2 verir. Ölçüm blok assert'i + piksel ölçümü + gözle.
3. **Yeşil temaya göre iki değer:** `ortak/hf_tema.py` yeşil değişkeni taşımaz; sahne kendi CSS satırıyla koyu temada `#4fbf85` verir.
   Beceri notu (kalem-hatti 13.11 QA) "ham yeşil yok, vurgu dolgusu" diyordu; istem ve BRIEF-S1 "doğru yeşil" dediği için istem uygulandı. Şef kararı.
4. **`Kaydet` 1400–1520 bandında:** içerik 460–1140'a beş öğe ≥ 64 px ile sığmadı; istemin izniyle hap ve yer imi y 1416–1504'e indi.
5. **git:** `projeler/*/*.png` ve `k/` `.gitignore`'da; teslim commit'e girecekse `git add -f` gerekir.
6. **Ana ders yalnız okundu;** başka sahneye, `ortak/`a, `BRIEF-S1.md`'ye, `zaman.json`'a dokunulmadı. `sozlesme.md`'ye 1 satır eklendi (izinli istisna).
