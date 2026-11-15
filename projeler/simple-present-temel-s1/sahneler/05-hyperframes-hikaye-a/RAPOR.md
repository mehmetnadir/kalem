# Sahne 05 · hikâye karesi A (kural kartı), huni v2 · simple-present-temel-s1 (HyperFrames, 1080×1920, tek kare, ses yok; zaman çizelgesi dışı) · 15.11.2026

Tema: acik

| Kapı | Sonuç |
|---|---|
| `calistir.sh --tema acik` | rc 0 · `png,1080,1920` · `…/simple-present-temel-s1/hikaye-a.png` (+ `hikaye.png`, `cp -p`, aynı md5 `106d67883ada…`) |
| `calistir.sh --tema koyu` | rc 0 · `png,1080,1920` · `…/k/koyu/hikaye-a-koyu.png` (md5 `ddbf48a4ef86…`) |
| `ONIZLE_YALNIZ=1 calistir.sh --tema acik` | rc 0 · `index.html yazıldı 18676` · `olay 0` · `önizleme hazır` (son hazırlık AÇIK tema) |
| `uret.py` assert'leri | rc 0 · 7 blok, kesişim 0, dikey boşluk ≥ 16, içerik x 60–960 / y 460–1140, otobüs yolları kutuda, sarı 2 kez (hap + rozet), `→` glifi yok |
| Çakışma kapısı `node araclar/cakisma-kapisi.mjs simple-present-temel-s1 --sahne 05-hyperframes-hikaye-a --port 41333 --sunucu 41022` | çıkış 2 · `HATA sahne bulunamadı: 05-hyperframes-hikaye-a` (beklenen: araç yalnız `zaman.json → sahneler[]` okur; emsal S1-VAR §5). Çakışma blok assert'iyle ve karede gözle denetlendi |
| Metin taraması `grep -rniE 'tam[ ]ders\|dak[i]ka' … --include=*.html/js/py` | boş (grep çıkış 1) |
| Kanal katmanı (piksel ölçümü, iki tema) | logo mürekkebi x 60–239 (koyu 61–239), y 298–330 (resim kutusu 53,2–246,7 × 291–339) · `@ydspublishing` x 265–595, y 296–339 (taban 330) · künye x 60–512, y 386–433. Emsal 02-04 s04 ve sahne 03 ölçümüyle aynı |
| İlk = orta = son | `snapshot --at 0,0.5,0.966` (açık): üç kare md5 `106d67883ada…`, teslim PNG ile aynı (`k/qa/`) |
| Boş bölgeler (piksel ölçümü, iki tema) | 0–280 boş · 1150–1920 boş · sağ 961–1080 (y 280–1570) boş · sol 0–59 boş · içerik mürekkebi x 60–864, y 489–1137 |
| Renk | tek sarı `Kaydet` hapı: açık `#ffe066` + yazı `#1b2440`, koyu `#f2a93b` + `#1b1a17` (künye rozeti kanal tablosundan); yeşil, kırmızı, emoji yok |

Durum: yazıldı, iki temada tek kare yakalandı. mp4 yok, git yok; `zaman.json`, `BRIEF-S1.md`, `ortak/`, başka sahneler değişmedi.
Not: istemin "calistir.sh yalnız ONIZLE_YALNIZ=1" satırı mp4 render içindir. Bu sahnede `calistir.sh` mp4 üretmez, yalnız
`hyperframes snapshot` ile tek PNG çeker. Doğrula §1 tam koşuyu istediği için koşu yapıldı (emsal 02-04 s04 ile aynı).

## Dosyalar
| Dosya | Kim | Not |
|---|---|---|
| `SPEC.md` | şef | yerleşim, blok kutuları, kalem oku, yuva, otobüs, 11 kural, kabul ölçütü |
| `uret.py` | agy-filo (rol kod, gemini-3.8-flash-high, 184 sn, 1 tur) | şef baştan sona okudu; 1 küçük Edit (QA 0, aşağıda); md5 `a6a42ac650ca…` |
| `yardim.py` | aynı paketin `03-hyperframes-kaydet/yardim.py` v2 kopyası (`cp -p`, sha256 `669c8d50c659…`) | şef Edit yalnız belge dizgesi; `kunye_svg()` v2 (`#kanal` + `#logoimg`, `Simple Present` 34 px, `YDT · BASIC`), HUD v2 bantları |
| `calistir.sh`, `olay.py`, `zamanlar.json` | emsal `02-04-ydt-temel-s1/sahneler/04-hyperframes-hikaye/` (RAPOR "huni v2") `cp -p` | şef Edit: başlık yorumu, paket adı yorumu, olay.py belge dizgesi. Çıktı adları emsalle aynı (`hikaye-a.png` + `hikaye.png`, `k/koyu/hikaye-a-koyu.png`) |
| `nesneler.json`, `proje/index.html`, `olaylar.json` (boş liste) | uret.py, olay.py | 7 blok |

agy koşu özeti: `/home/sef/.claude/canavar/agy-filo/20261115-193542/ozet.md` (1/1 başarılı). Özetin "değişen" listesinde paralel
oturumların dosyaları da var (01-kanca, 02-deger, 02-04-s3, `sozlesme.md`). agy bu sahnede yalnız `uret.py` dosyasını yazdı ve bir kez koşturdu.
`yardim.py`, `calistir.sh` mtime değeri agy'den önceki (19:34).

## Olay listesi (tek kare)
| Olay | Kare / sn | Cümle sözcüğü |
|---|---|---|
| bütün öğeler görünür: kanal (logo + `@ydspublishing`) · künye (`Simple Present` + `YDT · BASIC`) · `He, she, it: s gelir;` / `I, you, we, they: s yok.` (Fredoka 64) · `he · she · it` → `goes` (`es` mürekkep alt çizgi, Fredoka 72) · `I · you · we · they` → `go` + soluk kesik yuva · `My brother = he` (Caveat 64, ikincil) + küçük otobüs (coco, kalem) · yer imi + `Kaydet` sarı hap | kare 0 (yakalama 0,5 sn; çizelge 1,0 sn) | — (anlatım yok; kural özeti BRIEF-S1 girişi) |

Yerleşim (blok kutusu y): kanal 291–339 · künye 386–434 · özet 488–636 · satır 1 716–790 · satır 2 846–918 · örnek 956–1030 · kaydet 1050–1138 · boş 1150–1920.
Sütun: ok x 616–688, fiil x 712 (iki satırda aynı; satır 2 yuvası satır 1 `es`'inin altında, x 797,5–862,9). Otobüs kutusu [470, 956, 220, 70], aynalı (ön yüz sola), çizgi 2,6.
Yazı boyları: özet 64, satırlar 72, Caveat 64, hap 64 (künye ve kanal hariç hepsi ≥ 64). En uzun satır `I, you, we, they: s yok.` (24).

## Bakılan kareler ve bulgu
| Tur | Kare | Bulgu | Yapılan |
|---|---|---|---|
| 0 | `hikaye-a.png`, `k/koyu/hikaye-a-koyu.png` | taşma, kesik yazı, çakışma yok; kontrast iki temada iyi. Satır 2'de `go`'nun `o`'su ile yuvanın kesik sol kenarı birbirine değiyor | `uret.py` Edit: yuva x + 6, genişlik − 6 (sağ uç `es` sonunda kalır) |
| 1 | aynı iki kare + `k/qa/at-{0,0.5,0.966}s.png` | yuva ayrık; içerik x 60–864; sağ 961–1080 ve 1150–1920 boş; üç kare özdeş | — (geçti) |

## Açık noktalar
1. **Çakışma kapısı ölçmüyor:** durağan kare `zaman.json → sahneler[]` dışında. Araç çıkış 2 verir. Ölçümü blok assert'i, piksel ölçümü ve gözle bakış yaptı.
2. **Satır 1 boşluğu:** ok ve fiil iki satırda aynı sütunda (x 616 / 712). Bu yüzden `he · she · it` ile ok arasında ≈ 215 px boşluk var. Tablo gibi okunur; istenirse ok `it`'in yanına çekilir, ama yuva `es`'in altına düşmez.
3. **`zaman.json → hikaye.cikti`** hâlâ `hikaye.png` der. Teslim `hikaye-a.png` + `hikaye.png` (aynı dosya). Alan güncellenmeli mi, şef karar verir (yazma kapsamı dışı; emsal 02-04 s04 açık nokta 4 ile aynı).
4. **git:** `projeler/*/*.png` ve `k/` `.gitignore`'da. Teslim commit'e girecekse `git add -f` gerekir.
5. Coco yükleyicisi `01-hyperframes-kanca/yardim.py` dosyasından `uret.py`'ye kopyalandı (`yardim.py` gate'ten geçmiş sahne 03 kopyası olarak kaldı). Sahne 01 yükleyiciyi değiştirirse bu kopya ayrı kalır.
