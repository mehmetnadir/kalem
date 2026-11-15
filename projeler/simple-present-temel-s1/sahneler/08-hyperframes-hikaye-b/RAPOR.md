# Sahne 08 · hikâye karesi B (soru kartı), huni v2 · simple-present-temel-s1 (HyperFrames, 1080×1920, tek kare, ses yok; zaman çizelgesi dışı) · 15.11.2026

Tema: acik

| Kapı | Sonuç |
|---|---|
| `calistir.sh --tema acik` | rc 0 · `png,1080,1920` · `…/simple-present-temel-s1/hikaye-b.png` (md5 `bc254cfd5011…`) |
| `calistir.sh --tema koyu` | rc 0 · `png,1080,1920` · `…/k/koyu/hikaye-b-koyu.png` (md5 `15ffd0dd0c9b…`) |
| `ONIZLE_YALNIZ=1 calistir.sh --tema acik` | rc 0 · `index.html yazıldı 7294` · `olay 0` · `önizleme hazır` (son hazırlık AÇIK tema) |
| `uret.py` assert'leri | rc 0 · 8 blok, kesişim 0, dikey boşluk ≥ 16, içerik x 60–960 / y 460–1140, kaydet y 1400–1520, SVG'de yeşil çizgi 2, sarı 2 (hap + rozet), kırmızı 0, `_` ve `→` glifi yok |
| Çakışma kapısı `node araclar/cakisma-kapisi.mjs simple-present-temel-s1 --sahne 08-hyperframes-hikaye-b --port 41333 --sunucu 41022` | çıkış 2 · `HATA sahne bulunamadı: 08-hyperframes-hikaye-b` (beklenen: araç yalnız `zaman.json → sahneler[]` okur; emsal S1-VAR §5). Çakışma blok assert'iyle, piksel ölçümüyle ve karede gözle denetlendi |
| Metin taraması `grep -rniE 'tam[ ]ders\|dak[i]ka' … --include=*.html/js/py` | boş (grep çıkış 1) |
| Kanal katmanı (piksel ölçümü, iki tema) | logo mürekkebi x 60–239, y 298–330 (resim kutusu 53,2–246,7 × 291–339) · `@ydspublishing` x 265–595, y 296–339 (taban 330) · künye x 60–512, y 386–433. Sahne 05 ve emsal 02-04 s07 ölçümüyle aynı |
| İlk = orta = son | `snapshot --at 0,0.5,0.966` (açık): üç kare md5 `bc254cfd5011…`, teslim PNG ile aynı (`k/qa/`) |
| Boş bölgeler (piksel ölçümü, iki tema) | 0–280 boş · 1145–1390 boş · 1570–1920 boş · sağ 961–1080 (y 280–1570) boş · sol 0–59 boş · içerik x 60–959, y 477–1064 (B kartının soluk çerçevesi x 540–959, y 790–889) · kaydet x 60–415, y 1416–1503 |

Durum: yazıldı, iki temada tek kare yakalandı. mp4 yok, git yok; `zaman.json`, `BRIEF-S1.md`, `ortak/`, başka sahneler, emsal ve ana ders
değişmedi (salt okundu). Not: istemdeki "calistir.sh yalnız `ONIZLE_YALNIZ=1`" satırı mp4 render içindir. Bu sahnede `calistir.sh` mp4
üretmez; yalnız `hyperframes snapshot` ile tek PNG çeker. Doğrula §1 tam koşuyu istediği için tam koşu yapıldı (sahne 05 ve emsal ile aynı).

## Dosyalar
| Dosya | Kim | Not |
|---|---|---|
| `SPEC.md` | şef | yerleşim, blok kutuları, 11 kural, kabul ölçütü; QA 1 düzeltmesi (özet tabanı 970 / 1050) işlendi |
| `uret.py` | agy-filo (rol kod, gemini-3.8-flash-high, 154 sn, 1 tur) | şef baştan sona okudu; SPEC'e uyuyor; 1 küçük Edit (QA 1, aşağıda); md5 `055542cd8f12…` |
| `yardim.py` | emsal `02-04-ydt-temel-s1/sahneler/07-hyperframes-hikaye-b/yardim.py` (RAPOR "huni v2") `cp -p` | şef Edit: belge dizgesi + `KONU = "Simple Present"`. Sonuç sahne 05'in `yardim.py`'si ile işlev olarak aynı (yalnız belge dizgesi farklı). `kunye_svg()` v2 (`#kanal` + `#logoimg`, konu 34 px, `YDT · BASIC`), HUD v2 bantları |
| `calistir.sh`, `olay.py`, `zamanlar.json` | emsal 07 v2 `cp -p` | şef Edit: başlık yorumu, paket adı yorumu, olay.py belge dizgesi. Çıktı adları emsalle aynı (`hikaye-b.png`, `k/koyu/hikaye-b-koyu.png`); `uret.py` ve `olay.py` ayrı satırda (hata yutma onarımı emsalde var) |
| `nesneler.json`, `proje/index.html`, `olaylar.json` (boş liste) | uret.py, olay.py | 8 blok |
| `k/calistir-acik.log`, `k/koyu/calistir-koyu.log`, `k/qa/` | şef | koşu günlükleri ve QA kareleri |

Eski sürüm yok (paket yeni; `hikaye-b.png` önceden yoktu), yedek gerekmedi.

agy koşu özeti: `/home/sef/.claude/canavar/agy-filo/20261115-194603/ozet.md` (1/1 başarılı). Özetteki "değişen" listesinde paralel
oturumların dosyaları da var (`sozlesme.md`, S1 06/07, S2 05); agy bu sahnede yalnız `uret.py` yazdı.

## Olay listesi (tek kare)
| Olay | Kare / sn | Cümle sözcüğü |
|---|---|---|
| bütün öğeler görünür: kanal (logo + `@ydspublishing`) · künye (`Simple Present` + `YDT · BASIC`) · `Hangisi doğru?` (Fredoka 80) · `My parents` + kalem boşluğu / `to work by bus.` (Fredoka 72) · `A) go` kartı (yeşil çerçeve 6 + yeşil kalem tik) · `B) goes` kartı (opaklık 0,45, ikincil çerçeve 4) · `He, she, it: s gelir;` / `I, you, we, they: s yok.` (Fredoka 64) · yer imi + `Kaydet` sarı hap | kare 0 (yakalama 0,5 sn; çizelge 1,0 sn) | — (anlatım yok; kural özeti BRIEF-S1 girişi) |

Yerleşim (blok kutuları, y): kanal 291–339 · künye 386–434 · soru 475–555 · kök 596–758 · şıklar 790–890 (A x 60–480, B x 540–960) ·
özet 922–1066 · boş 1066–1416 (1150–1380 bağ çıkartması) · kaydet 1416–1504 · boş 1570–1920. En uzun satır `I, you, we, they: s yok.` (24).
Kök boşluğu: `_` glifi değil, sabit kübik kalem yolu (x 450,8–666,8, y 652–662, çizgi 7, yuvarlak uç).
Renk: açık tema yeşil `#167a4a`, koyu tema `#4fbf85` (sahne CSS'i `#root:not(.tema-acik) [stroke="#167a4a"]`); sarı yalnız `Kaydet` hapı
(açık `#ffe066` + yazı `#1b2440`; künye rozeti kanal tablosundan); kırmızı ve emoji yok. Doğru cevap A) go (özne *my parents* = they).

## Bakılan kareler ve bulgu
| Tur | Kare | Bulgu | Yapılan |
|---|---|---|---|
| 0 | `hikaye-b.png`, `k/koyu/hikaye-b-koyu.png` | taşma, kesik yazı, üst üste binme yok; kontrast iki temada iyi; bölgeler boş. Ritim zayıf: kök → kart boşluğu 35 px, kart → özet boşluğu 27 px (özet kartlara yapışık duruyor) | özet tabanları 962 / 1042 → 970 / 1050 (`uret.py` şef Edit, 4 sayı; SPEC eşlendi). Özet kutusu 922–1066: istemin 910–1060 bandını 6 px aşar, içerik sınırı 1140 içinde kalır |
| 1 | aynı iki kare + `k/qa/at-{0,0.5,0.966}s.png` | taşma, kesik yazı, binme yok; kart → özet boşluğu 35 px (kök → kart ile eşit); 0–280, 1150–1380, 1570–1920 ve sağ 961–1080 boş; üç kare özdeş | — (geçti) |

## Açık noktalar
1. **`Kaydet` 1400–1520 bandında:** istemin 1070–1140 bandı 70 px. 64 px yazılı 88 px'lik hap bu banda sığmadı (`y` alt uzantısı kenara
   değer). İstemin izniyle hap ve yer imi y 1416–1504'e indi (emsal 02-04 s07 v2 ile aynı). Sahne 05 (hikâye A) `Kaydet`'i 1050–1138'de
   tutar; iki hikâye karesinde `Kaydet` farklı yükseklikte durur. Şef kararı.
2. **Çakışma kapısı ölçmüyor:** durağan kare `zaman.json → sahneler[]` dışında; araç çıkış 2 verir. Ölçüm blok assert'i, piksel ölçümü ve gözle yapıldı.
3. **Yeşil temaya göre iki değer:** `ortak/hf_tema.py` yeşil değişkeni taşımaz; sahne kendi CSS satırıyla koyu temada `#4fbf85` verir (emsal 07 ile aynı).
4. **Kök cümle [YENİ]:** `My parents go to work by bus.` ana derste yok (hikaye-taslak §5: "jüri bakacak"). Jüri kaydı görülmedi.
5. **Instagram test çıkartması:** cevapsız sürüm (A yeşilsiz) bu istemde üretilmedi (hikaye-taslak §5).
6. **Günlük dosyası yanlış yere yazıldı, taşındı:** ilk açık tema koşusunun günlüğü bir an `uretim-tutanagi/.s08-acik.log` adıyla yazıldı.
   Aynı dakikada `k/calistir-acik.log` yoluna taşındı; `uretim-tutanagi/` içinde iz kalmadı.
7. **git:** `projeler/*/*.png` ve `k/` `.gitignore`'da; teslim commit'e girecekse `git add -f` gerekir. `sozlesme.md`'ye 1 satır eklendi (izinli istisna).
