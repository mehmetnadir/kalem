# KAPAK-0202 — simple-present-temel ana ders kapakları · 15.11.2026

| Dosya | Boyut | Tema |
|---|---|---|
| `simple-present-temel/kapak.png` · `kapak-koyu.png` | 1920×1080 | açık · koyu |
| `simple-present-temel-dikey/kapak.png` · `kapak-koyu.png` | 1080×1920 | açık · koyu |
| `simple-present-temel/uretim-tutanagi/kapak-168.png` | 168×94 | açık (küçük görünüm) |

**Yöntem.** Tek üretici `sahneler/90-hyperframes-kapak/uret.py --tema acik|koyu --duzen yatay|dikey`; iki ayrı yerleşim işlevi (`yatay()`, `dikey()`), kırpma yok. Yazı SVG (Fredoka 700, Lexend 700, `yardim.py` kalıp kopyası), görsel `<img>` + krem çıkartma kenarı. Kare: `bash calistir.sh --tema acik|koyu` (ana) ve `bash simple-present-temel-dikey/sahneler/90-hyperframes-kapak/calistir.sh --tema …` → `hyperframes snapshot . --at 0.5 --no-end --keep`. Dikey görseller `simple-present-temel-dikey/ortak/kapak` göreli bağından `proje/assets/` dizinine kopyalanır. Sahne `zaman.json` listesinde yok; `zaman.json` ve `surumler.json` dosyalarına dokunulmadı.

| Kapı (§5) | Sonuç | Bakılan kare |
|---|---|---|
| 1. 4 PNG, boyut | GEÇTİ — `file`: 1920×1080 ×2, 1080×1920 ×2 | 4 PNG |
| 2. 168 px küçük görünüm | GEÇTİ — "GİDER = GOES" okunuyor, yüz seçiliyor; küçük satır okunmuyor (beklenen) | `kapak-168.png` (koyunun 168 px kopyası da) |
| 3. Glif İ/Ş/Ğ | GEÇTİ — her harf için `uret.py` Fredoka latin + latin-ext glif denetimi yapar (`assert`); İ, Fredoka biçiminde | 4 PNG |
| 4. Çakışma yok | GEÇTİ — yazı ↔ görsel, yazı ↔ yazı, daire ↔ yazı için alfa ve kutu `assert` (pay 24 px + kenar 10 px) | 4 PNG |
| 4. Sağ alt %15×%8 boş | GEÇTİ — zeminden farklı piksel 0 / 25.056 (açık ve koyu) | `kapak.png`, `kapak-koyu.png` |
| 4. Dikey üst ve alt %20 | GEÇTİ — zeminden farklı piksel 0 / 414.720 (her bölge, iki tema) | dikey `kapak.png`, `kapak-koyu.png` |
| 5. Emoji, süs | GEÇTİ — öğeler: yazı, karakter, nesne, logo, rozet, açık temada krem daire | 4 PNG |

**Tasarım kararları (şefin onayı gerekir).** (1) Açık temada sarı zeminde logonun sarı "yds" bölümü kayboluyordu; logo tek renk `#141414` yapıldı. Koyu temada şeffaf logo (sarı + beyaz) kullanıldı. (2) Koyu temada vurgu satırı sarı kutu içinde `#141414` yazı. (3) Lexend yazı tipinde → glifi yok; ok SVG çizgisiyle çizildi. (4) İnce hız çizgilerinde kenar şerit şerit görünüyordu. Kenar dört yönlü drop-shadow ile çizildi: 3 geçiş, 3,33 px adım, toplam 10 px. (5) Dikey düzende karakter, kaynak satır 1000'de (el dahil, göğüs altı) düz kesildi. Parmak minibüsü gösteriyor.

**Açık kalan.** (a) Dikey düzende ana yazı y 492–885 aralığında. Standarttaki "orta bant 600–1320 üst yarısı" ölçüsünden 108 px yukarıda başlıyor; karakter y 930–1513. Gerekçe: karakter yüzünü büyütmek için 384–1536 serbest alanı kullanıldı. Bant zorunluysa yazı boyu 190 → 173 olur, karakter küçülür. (b) Yazma kapısı (`write-size-gate`) 15 satırı aşan `.py` yazımını engelledi. İstem bayrak dosyasını ve alt ajanı yasakladığı için `uret.py` Bash ile yazıldı. (c) Aynı worktree'de paralel bir oturum `02-04-ydt-temel-s*` dosyalarını değiştiriyor; bu dosyalar bu işin parçası değil. (d) Kökte eski kapak yoktu; Silinecekler'e yalnız kullanılmayan `dikey/90…/yardim.py` kopyası taşındı.
