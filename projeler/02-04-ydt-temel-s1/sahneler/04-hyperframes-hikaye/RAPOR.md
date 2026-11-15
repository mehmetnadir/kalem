# Sahne 04 · hikâye karesi (HyperFrames, 1080×1920, tek kare, ses yok; zaman çizelgesi dışı)

Tema: koyu

Durum: yazıldı, iki temada tek kare yakalandı. mp4 yok, birleştirme yok, `zaman.json` değişmedi (`hikaye` alanı, `sahneler[]` dışında).

| Çıktı | Yol | Boyut |
|---|---|---|
| açık (teslim) | `projeler/02-04-ydt-temel-s1/hikaye.png` | 1080×1920 (ffprobe) · sha256 `0196fdb33b15…` |
| koyu | `sahneler/04-hyperframes-hikaye/k/hikaye-koyu.png` | 1080×1920 (ffprobe) · sha256 `22153bcebae8…` |
| ham yakalama | `k/at-0.5s.png` (açık) · `k/koyu/at-0.5s.png` (koyu) | 1080×1920 |

## Dosyalar
| Dosya | Kim yazdı | Not |
|---|---|---|
| `SPEC.md` | şef | yerleşim, ölçüler, tema kuralları, kabul ölçütü; QA düzeltmeleri işlendi |
| `uret.py` | agy-filo (rol kod, gemini-3.8-flash-high, 255 sn, 1 tur) | şef baştan sona okudu; 5 küçük Edit (aşağıda) |
| `yardim.py` | örnekten birebir kopya | `present-continuous-ileri-s1/sahneler/03-hyperframes-cta/yardim.py` (sha256 `2cddbe805c13…`); `kunye_svg`/`altyazi_*` kullanılmaz |
| `calistir.sh`, `olay.py`, `zamanlar.json` | şef | üret → [`ONIZLE_YALNIZ` çıkışı] → `hyperframes snapshot --at 0.5 --no-end --keep` → PNG kopyası |
| `nesneler.json` | uret.py | 9 blok kutusu (hud, ust, ek, kart1, kart2, alt, cg1, cg2, hap) |
| `olaylar.json` | olay.py | `[]` (ses yok) |

agy koşu özeti: `/home/sef/.claude/canavar/agy-filo/20261115-120335/ozet.md` (1/1 başarılı). Özetteki "değişen 46"
listesinde paralel oturumların dosyaları da var (dikey paket, S1 sahne 01–03, `sozlesme.md`); mtime + sahne SPEC'iyle ayrıldı:
agy yalnız `uret.py`, `nesneler.json`, `proje/index.html` yazdı. git'e giren başka değişiklik yok; agy'nin doğrulaması
`ortak/__pycache__/hf_tema.cpython-310.pyc` önbelleğini yazmış olabilir (12:07:37, gitignore'da).

## Olay listesi (tek kare)
| Olay | Kare / sn | Cümle sözcüğü |
|---|---|---|
| bütün öğeler görünür: HUD (logo, `SIMPLE PRESENT vs` / `PRESENT CONTINUOUS`, rozet `YDT · BASIC`, çip `Full lesson`) · `Türkçede tek sözcük` · `YAŞI-YOR-UM` (`YOR` sarı kutuda) · kart 1 ev + `I live` + `PERMANENT` + uzun bant · kart 2 bavul + `I am living` + `TEMPORARY` + kısa bant · `İngilizcede iki zaman` · `Tam ders:` / `profildeki bağlantı` · `@ydspublishing` hapı | kare 0 (yakalama 0,5 sn; çizelge 1,0 sn) | — (anlatım yok; metin `hikaye-taslak.md` §3) |

Ölçüler: `YAŞI-YOR-UM` Fredoka 700 **137** (952 px'e sığan en büyük), kart başlığı Fredoka 80, etiket Caveat 64, düz satırlar
Lexend 500 64, çağrı Caveat 72, hap Fredoka 64. En uzun satır `İngilizcede iki zaman` (21). HUD ölçüleri `ortak/kunye.js` ile aynı.

## Kapı sonucu (son satırlar)
qa-yerel / çakışma kapısı / sahne-kare koşmadı: üçü `zaman.json → sahneler[]` arar, bu sahne bilerek dışında (istem).
Çakışma denetimini `uret.py` assert'leri yapar (blok kesişimi 0, dikey boşluk ≥ 16, x ∈ [48, 1032], y < 1536, satır ≤ 24).
```
ONIZLE_YALNIZ=1 bash calistir.sh --tema acik   → "önizleme hazır", rc=0
bash calistir.sh --tema acik                   → S=137 · png,1080,1920 · …/02-04-ydt-temel-s1/hikaye.png · rc_acik=0
bash calistir.sh --tema koyu                   → S=137 · png,1080,1920 · …/k/hikaye-koyu.png · rc_koyu=0
```

## Bakılan kareler ve bulgu
| Tur | Kare | Bulgu | Yapılan |
|---|---|---|---|
| 1 | `k/at-0.5s.png`, `k/koyu/at-0.5s.png` | taşma, kesik yazı, çakışma yok; 1536 altı boş; iki temada kontrast iyi. (a) tire 2 `UM`'ye yapışık (`-UM`), sol tire açık: dengesiz. (b) `PERMANENT` son T çerçeveye 18 px. | (a) tire 2 ile `UM` arasına bir `ara` (0,08 em), S 139 → 137. (b) etiket x 1000 → 980 |
| 2 | `hikaye.png`, `k/hikaye-koyu.png` | tireler dengeli; etiketler çerçeveden açık; altçizgi `living` g kuyruğuna değmiyor; hap/rozet/`YOR` açıkta `#ffe066` + `#1b2440`, koyuda `#f2a93b` + `#1b1a17`; kırmızı, yeşil, emoji yok | — (geçti) |

Şef Edit'leri (uret.py): altçizgi taban + 14 → taban + 0,48 × boy (`.claude/docs/sozlesme.md` satır 35; SPEC'e agy başladıktan sonra girdi) ·
`top` formülü 3 yerde + `UM` x (tur 1 a) · etiket x (tur 1 b). `calistir.sh`: çıktıya `chmod 644` (snapshot 0600 yazıyordu).

## Açık noktalar
1. **Logo yeri:** BRIEF-S1 ve `hikaye-taslak.md` §3 "logo sol alt y ≈ 1478" der; BRIEF-DIKEY §0 (Nadir bulgusu) "logo HUD sol üst 96 px, alt bantta logo yok" der. Nadir bulgusu uygulandı (logo HUD'da). Taslak ve BRIEF-S1 satırı güncellenmeli (yazma kapsamı dışı).
2. **Çağrı bandı iki sütun:** 1344–1536 (192 px) bandına `Tam ders:` / `profildeki bağlantı` (Caveat 72) + hap (≥ 64 px) alt alta sığmaz. Yazı solda 2 satır, hap sağa hizalı. Tek sütun kuralına bu bantta istisna.
3. **`now` yazısı yok:** kartta 64 px'lik `now` için yer yok; nokta iki kartta aynı x'te (540), karşılaştırma görselden okunur.
4. **BRIEF-S1 bant tablosu ile fark:** taslak "300–420 üst satır" der; istem içerik bandını 352'den başlatır. `Türkçede tek sözcük` tabanı 424 (üst 376).
5. **git:** `hikaye.png` `.gitignore` satır 27 (`projeler/*/*.png`), `k/` satır 36 ile yok sayılır. Teslim commit'e girecekse `git add -f projeler/02-04-ydt-temel-s1/hikaye.png` gerekir (örnek: `present-continuous-s1/kapak.png` izleniyor).
6. **Önbellek yan etkisi:** snapshot denemesi `02-04-ydt-temel/sahneler/12-hyperframes-ozet/proje/.hyperframes/` önbelleğini güncelledi (gitignore'da, git değişikliği yok).
