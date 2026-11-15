# Sahne 04 · hikâye karesi A (HyperFrames, 1080×1920, tek kare, ses yok; zaman çizelgesi dışı)

Tema: koyu

Durum: yazıldı, iki temada tek kare yakalandı (son koşu koyu). mp4 yok, birleştirme yok, `zaman.json` değişmedi (`hikaye` alanı, `sahneler[]` dışında).

| Çıktı | Yol | Boyut (ffprobe) · sha256 |
|---|---|---|
| açık (teslim) | `projeler/02-04-ydt-temel-s3/hikaye-a.png` | 1080×1920 · `65c4e68d3bec…` |
| açık kopya | `projeler/02-04-ydt-temel-s3/hikaye.png` | 1080×1920 · `65c4e68d3bec…` (`cmp` aynı) |
| koyu | `sahneler/04-hyperframes-hikaye/k/hikaye-a-koyu.png` | 1080×1920 · `b0c276568648…` |
| ham yakalama | `k/at-0.5s.png` (açık) · `k/koyu/at-0.5s.png` (koyu) | 1080×1920 |

## Dosyalar
| Dosya | Kim yazdı | Not |
|---|---|---|
| `SPEC.md` | şef | yerleşim, ölçüler, ≠ renk köprüsü, ikon kaynakları, kabul ölçütü |
| `uret.py` | agy-filo (rol kod, gemini-3.8-flash-high, 278 sn, 1 tur) | şef baştan sona okudu; SPEC'e uyuyor, düzeltme gerekmedi |
| `yardim.py` | S1 sahne 04'ten birebir kopya | sha256 `2cddbe805c13…` |
| `calistir.sh` | S1 kopyası + şef Edit | çıktı adları `hikaye-a.png` + kopya `hikaye.png` / `k/hikaye-a-koyu.png`; ffprobe `png,1080,1920` değilse çıkış 3 |
| `olay.py`, `zamanlar.json` | S1 kopyası | `olaylar.json` = `[]`; çizelge 1,0 sn, yakalama 0,5 sn |
| `nesneler.json` | uret.py | 9 blok kutusu |

agy koşu özeti: `/home/sef/.claude/canavar/agy-filo/20261115-124713/` (1/1 başarılı). Özetteki "değişen 116" listesinde paralel oturumların
dosyaları var (S2 paketi, S3 sahne 01/03/05/06/07, `sozlesme.md`). 12:47–12:52 penceresinde mtime + sahne SPEC'iyle ayrıldı: agy yalnız
`uret.py`, `nesneler.json`, `proje/index.html` yazdı (+ `__pycache__`, gitignore'da).

## Olay listesi (tek kare)
| Olay | Kare / küresel sn | Cümle · sözcük |
|---|---|---|
| bütün öğeler görünür: HUD (logo, `SIMPLE PRESENT vs` / `PRESENT CONTINUOUS`, rozet `YDT · BASIC`, çip `Full lesson`) · `İkisi geleceği anlatıyor` · `TARİFE` / `≠ PLAN` (sarı hap, ≠ kalemle) · kart 1 `The train leaves …` (`leaves` sarı altçizgi) + `train → timetable` + tren + saat (7:00) · kart 2 `I am going …` (`am going` sarı altçizgi) + `person → plan` + bilet · `Tren tarifeye uyar` · `Tam ders:` / `profildeki bağlantı` · `@ydspublishing` hapı | kare 0 (yakalama 0,5 sn; çizelge 1,0 sn) / küresel sn yok | — (anlatım yok; metin `hikaye-taslak.md` §2) |

Ölçüler: başlık Fredoka 700 **S = 124** (yükseklik sınırlar; §Açık 1) · kart cümlesi Fredoka 64 · etiket Caveat 64 · düz satırlar Lexend 500 64 ·
çağrı Caveat 72 · hap Fredoka 64. En uzun satır `İkisi geleceği anlatıyor` (24, sınırda). Blok kutuları (`nesneler.json`): ust 356–420 ·
bas 444–723 · kart1 748–976 · kart2 996–1224 · alt 1248–1312 · cg1/cg2/hap 1364–1520 · 1536 altı boş.

## Kapı sonucu (son satırlar)
qa-yerel / çakışma kapısı / sahne-kare koşmadı: üçü `zaman.json → sahneler[]` arar, bu sahne bilerek dışında (istem).
Çakışma denetimini `uret.py` assert'leri yapar (blok kesişimi 0, dikey boşluk ≥ 16, x ∈ [48, 1032], y < 1536, satır ≤ 24, kart içi sınırlar).
```
ONIZLE_YALNIZ=1 bash calistir.sh --tema acik  → S=124 · olay 0 · "önizleme hazır" · rc=0
bash calistir.sh --tema acik                  → png,1080,1920 · …/02-04-ydt-temel-s3/hikaye.png · …/hikaye-a.png · rc_acik=0
bash calistir.sh --tema koyu                  → png,1080,1920 · …/k/hikaye-a-koyu.png · rc_koyu=0
cmp hikaye-a.png hikaye.png                   → aynı
```

## Bakılan kareler ve bulgu
| Tur | Kare | Bulgu | Yapılan |
|---|---|---|---|
| 1 | `hikaye-a.png` (açık), `k/hikaye-a-koyu.png` (koyu) | taşma, kesik yazı, üst üste binme yok; altyazı yok, 1344–1536 yalnız çağrı; 1536 altı boş (yalnız vinyet, parlaklık 217–237 / 16–24); iki temada kontrast iyi. Piksel: açıkta ≠ ve `PLAN` `#1b2440`, hap `#ffe066`; koyuda ≠ ve `PLAN` `#1b1a17`, hap `#f2a93b`. Altçizgiler `going` g kuyruğuna değmiyor. Saat 7:00 (akrep 7, yelkovan 12). Kırmızı, yeşil, emoji, "kanal", QR, süre yok | — (geçti) |

## Açık noktalar
1. **Başlık boyu:** BRIEF "952 px'e sığan en büyük boy" der; aynı tablo başlığa 440–700 bandını (260 px) verir. İki satır bu yükseklikte en çok
   S ≈ 124 olur (genişlik sınırı 237). Bant 444–724 alındı. Daha büyük başlık kartları küçültmeyi ister (Nadir kararı).
2. **Logo yeri:** BRIEF-S3 ve `hikaye-taslak.md` §2 "logo sol alt y ≈ 1478" der; BRIEF-DIKEY §0 (Nadir bulgusu) "logo HUD sol üst, alt bantta
   logo yok" der. S1 hikâye karesi gibi Nadir bulgusu uygulandı. BRIEF-S3 satırı güncellenmeli (yazma kapsamı dışı).
3. **Ders adı yazımı:** BRIEF tablosu `Simple Present vs Present Continuous` der; `ortak/kunye.js` `SIMPLE PRESENT vs` / `PRESENT CONTINUOUS`
   (büyük harf) verir. İstem gereği kunye.js uygulandı.
4. **≠ ve → glifi yok:** Fredoka, Lexend, Caveat dosyalarında U+2260 ve U+2192 yok (fontTools ile ölçüldü). İkisi SVG kalem çizgisiyle çizildi.
   ≠ rengi sözleşmedeki kalıpla `#root #esitdegil path{stroke:var(--pilMetin)}` (hf_tema `[stroke="#1b1a17"]`'yi zemine boyar).
5. **Yakalama boyutu:** `hyperframes snapshot` boyut bayrağı almaz; 1080×1920 kompozisyondan (`data-width/height`) gelir, calistir.sh ffprobe ile denetler.
6. **git:** `hikaye-a.png`, `hikaye.png` `.gitignore` satır 27 (`projeler/*/*.png`), `k/` satır 36 ile yok sayılır. Teslim commit'e girecekse
   `git add -f projeler/02-04-ydt-temel-s3/hikaye-a.png projeler/02-04-ydt-temel-s3/hikaye.png` gerekir.
