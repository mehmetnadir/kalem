# Sahne 04 · Hikâye A — bilgi kartı (HyperFrames, 1080×1920, tek kare, ses yok; zaman çizelgesi dışı)

Tema: koyu

Durum: yazıldı, iki temada tek kare yakalandı. mp4 yok, birleştirme yok, `zaman.json` değişmedi (`hikaye` alanı, `sahneler[]` dışında).

| Çıktı | Yol | Boyut |
|---|---|---|
| açık (teslim) | `projeler/02-04-ydt-temel-s2/hikaye-a.png` | 1080×1920 (ffprobe) · sha256 `a2374a5ff8f0…` |
| açık kopya | `projeler/02-04-ydt-temel-s2/hikaye.png` | `cmp` ile `hikaye-a.png`'ye bayt bayt eşit |
| koyu | `sahneler/04-hyperframes-hikaye/k/hikaye-a-koyu.png` | 1080×1920 (ffprobe) · sha256 `abb11e815377…` |
| ham yakalama | `k/at-0.5s.png` (açık) · `k/koyu/at-0.5s.png` (koyu) | 1080×1920 |

## Dosyalar
| Dosya | Kim yazdı | Not |
|---|---|---|
| `SPEC.md` | şef | yerleşim, ölçüler, tema kuralları, kabul ölçütü; QA tur 1 düzeltmesi işlendi (§4.4 eksen) |
| `uret.py` | agy-filo (rol kod, gemini-3.8-flash-high, 228 sn, 1 tur) | şef baştan sona okudu; SPEC'e uyuyor. Şef 2 küçük Edit yaptı (QA tur 1, eksen) |
| `yardim.py` | S1 örneğinden birebir kopya (sha256 `2cddbe805c13…`) | `kunye_svg`/`altyazi_*` kullanılmaz |
| `calistir.sh` | S1 örneğinden kopya + şef Edit | `HEDEF` açıkta `hikaye-a.png` + kopya `hikaye.png`, koyuda `k/hikaye-a-koyu.png`; `GEN=1080; YUK=1920` + ffprobe boyut denetimi (uymazsa çıkış 1); `Y=$(yuk1)`, homebrew satırı koşullu |
| `olay.py`, `zamanlar.json` | S1 örneğinden birebir kopya | `olaylar.json` = `[]`; çizelge 1,0 sn, yakalama 0,5 sn |
| `nesneler.json` | uret.py | 10 blok kutusu (hud, ust, kart1, kart2, today, not1, not2, cg1, cg2, hap) |

agy koşu özeti: `/home/sef/.claude/canavar/agy-filo/20261115-124841/ozet.md` (1/1 başarılı). Özetteki "değişen 122" listesinde
paralel oturumların dosyaları da var (S2 sahne 01, 02, 03, 06, 07; `sozlesme.md`). Bu sahnede agy yalnız `uret.py`, `nesneler.json`,
`proje/index.html` (ve `__pycache__`) yazdı (mtime 12:49–12:51).

## Olay listesi (tek kare)
| Olay | Kare / sn | Cümle sözcüğü |
|---|---|---|
| bütün öğeler görünür: HUD (logo, `SIMPLE PRESENT vs` / `PRESENT CONTINUOUS`, rozet `YDT · BASIC`, çip `Full lesson`) · `Genel mi, şu an mı?` · kart 1 mont + `She wears her coat` / `in the winter.` + `GENERAL` + 4 kış bandı (kar tanesi) + now noktası bantların dışında · kart 2 tişört + `She is wearing her` / `pink T-shirt today.` + `RIGHT NOW` + today bandı, now noktası içinde · `today` sarı hap · `iki zamanda da geçebilir` · `Farkı anlam yapar.` · `Tam ders:` / `profildeki bağlantı` · `@ydspublishing` hapı | kare 0 (yakalama 0,5 sn; çizelge 1,0 sn); küresel sn yok | — (anlatım yok; metin `hikaye-taslak.md` §3) |

Ölçüler: kart cümlesi Fredoka 700 64, etiket Caveat 700 64, düz satırlar Lexend 500/700 64, çağrı Caveat 72, hap Fredoka 64.
Bloklar (y): ust 376–440 · kart1 468–740 · kart2 760–1032 · today 1064–1148 · not1 1164–1228 · not2 1248–1312 · çağrı 1364–1520.
İçerik bandı kullanımı 376–1312 / 352–1392 = %90. En uzun satır `iki zamanda da geçebilir` (24). Eksen `AX0` 408 → 988, now x 698 (iki kartta aynı).
Tek sarı öğe `today` hapı (künye: rozet, çip, `@ydspublishing` hapı). Bantlar sarı değil (mürekkep %14 dolgu + mürekkep çizgi), kartta odak yok,
`today`'den karta bağ yok. Kırmızı, yeşil, emoji, "kanal", QR, süre yok (uret.py assert).

## Kapı sonucu (son satırlar)
qa-yerel / çakışma kapısı / sahne-kare koşmadı: üçü `zaman.json → sahneler[]` arar, bu sahne bilerek dışında (istem).
Çakışma denetimini `uret.py` assert'leri yapar (blok kesişimi 0, dikey boşluk ≥ 16, x ∈ [48, 1032], y < 1536, satır ≤ 24, kart içi kurallar SPEC §6.6).
```
ONIZLE_YALNIZ=1 bash calistir.sh               → "önizleme hazır", rc_onizle=0
bash calistir.sh --tema acik                   → png,1080,1920 · …/02-04-ydt-temel-s2/hikaye-a.png · …/hikaye.png · rc_acik=0
bash calistir.sh --tema koyu                   → png,1080,1920 · …/k/hikaye-a-koyu.png · rc_koyu=0
```

## Bakılan kareler ve bulgu
| Tur | Kare | Bulgu | Yapılan |
|---|---|---|---|
| 1 | `hikaye-a.png`, `k/hikaye-a-koyu.png` | taşma, kesik yazı, binme yok; 1536 altı boş; alt bantta altyazı yok; iki temada kontrast iyi. Kusur: zaman ekseni bantların içinden geçiyor → kar tanesi ✳ yerine ⊕ gibi, today bandında çizgi now noktasını kesiyor | `uret.py` 2 Edit: eksen her bant aralığında kesilir (kart 1: 4 kış bandı, kart 2: today bandı). SPEC §4.4'e işlendi |
| 2 | aynı iki kare | kar tanesi temiz ✳, today bandı yalnız noktayı taşıyor; künye, kart, hap, çağrı bandı yerinde; açıkta hap `#ffe066` + `#1b2440`, koyuda `#f2a93b` + `#1b1a17` | — (geçti) |

## Açık noktalar
1. **Logo yeri:** BRIEF-S2 Hikâye A satırı ve `hikaye-taslak.md` §3 "logo sol alt y ≈ 1478" der; BRIEF-DIKEY §0 (Nadir bulgusu) "logo HUD sol üst 96 px, alt bantta logo yok" der. Nadir bulgusu uygulandı (S1 hikâye ile aynı karar). BRIEF-S2 / taslak satırı güncellenmeli (yazma kapsamı dışı).
2. **`today` hapı sola hizalı:** taslak §3 "Fredoka 64, ortalı" der. Hap sol kenara (x 48) kondu: alttaki `iki zamanda da geçebilir` satırının öznesi olarak okunur ve tek sütunla hizalıdır (her şey ortalı klişesi #7'den kaçınır). Nadir isterse ortalanır (tek sabit).
3. **Bant tarifi:** BRIEF-S2 kart 1 "tekrar eden kış bantları", kart 2 "today bandı" der; bant rengi yazmaz. Tek sarı kuralı yüzünden bantlar mürekkep %14 dolgu + çizgi; ana dersteki sarı today bandından farklıdır.
4. **`now` yazısı yok:** kartta 64 px'lik `now` için yer yok; nokta iki kartta aynı x'te (698), karşılaştırma görselden okunur.
5. **Çağrı bandı iki sütun:** 1344–1536 bandına `Tam ders:` / `profildeki bağlantı` (Caveat 72) + hap (64 px) alt alta sığmaz; yazı solda 2 satır, hap sağa hizalı (S1 ile aynı istisna).
6. **git:** `hikaye-a.png`, `hikaye.png` `.gitignore` (`projeler/*/*.png`) ve `k/` ile yok sayılır. Teslim commit'e girecekse `git add -f` gerekir.
7. **Yan etki:** `.claude/docs/sozlesme.md`'ye 1 satır eklendi (bant rengi + eksen kesme dersi; istemdeki tek istisna).
