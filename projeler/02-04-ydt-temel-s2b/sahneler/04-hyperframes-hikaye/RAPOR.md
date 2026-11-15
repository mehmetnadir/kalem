# Sahne 04 · Hikâye A v2 — kural kartı (huni v2; HyperFrames, 1080×1920, tek kare, ses yok; zaman çizelgesi dışı)

Tema: acik

Durum: v2 yazıldı. Tek kare iki temada yakalandı. mp4 yok, birleştirme yok. `zaman.json` değişmedi (`hikaye` alanı, `sahneler[]` dışında).
v1 (SPEC, RAPOR, uret.py, yardim.py, kareler) yedekte: `~/Silinecekler/2026-11-15-huni-v2/02-04-ydt-temel-s2/sahneler/04-hyperframes-hikaye/`
(`cp -a`). Eski kök PNG'ler (`hikaye-a.png`, `hikaye.png`) V2 yedeğinde: `~/Silinecekler/2026-11-15-huni-v2/02-04-ydt-temel-s2/`.

| Çıktı | Yol | Boyut · sha256 |
|---|---|---|
| açık (teslim) | `projeler/02-04-ydt-temel-s2/hikaye-a.png` | 1080×1920 (ffprobe) · `22e42668fb54…` |
| açık kopya | `projeler/02-04-ydt-temel-s2/hikaye.png` | `cmp` ile `hikaye-a.png`'ye bayt bayt eşit |
| koyu | `sahneler/04-hyperframes-hikaye/k/hikaye-a-koyu.png` | 1080×1920 (ffprobe) · `6668bc085d1c…` |
| ham yakalama | `k/at-0.5s.png` (açık) · `k/koyu/at-0.5s.png` (koyu) | 1080×1920 |

Üç koşuda (QA tur 2 ve tarama düzeltmesinden sonra) PNG sha256 aynı: yakalama belirlenimci.

## Dosyalar
| Dosya | Kim yazdı | Not |
|---|---|---|
| `SPEC.md` | şef | v2 tasarım: yerleşim, ölçüler, tema kuralları, kabul ölçütü. QA tur 1 değerleri işlendi (§3, §4.3.1, §6.5) |
| `uret.py` | agy-filo (rol kod, gemini-3.8-flash-high, 252 sn, 1 tur) | şef baştan sona okudu; SPEC'e uyuyor. Şef 2 küçük Edit yaptı: QA tur 1 (hap ölçüsü + satır 2–3 tabanı), yasak söz denetimi düzenli ifadeye |
| `yardim.py` | şef kopyası: `sahneler/03-hyperframes-cta/yardim.py` (S2 v2; sha256 `3d1ac3d54474…`) | kanal katmanı + künye `Y.kunye_svg()`; `HUD` sözlüğü istemdeki değerlerle aynı |
| `calistir.sh`, `olay.py`, `zamanlar.json` | v1, değişmedi | homebrew koşullu, `Y=$(yuk1)`, `GEN=1080; YUK=1920` + ffprobe boyut denetimi; `olaylar.json` = `[]`; çizelge 1,0 sn, yakalama 0,5 sn |
| `nesneler.json` | uret.py | 6 blok: kanal, kunye, soru, kart, eslesme, kaydet |

agy koşu özeti: `/home/sef/.claude/canavar/agy-filo/20261115-190231/ozet.md` (1/1 başarılı). Özetteki "değişen 158" listesi ortak
worktree'deki paralel oturumların dosyalarını da sayar (S1 s04, `sozlesme.md` vb.). Bu koşu bu sahnede `uret.py`, `nesneler.json`,
`proje/index.html` ve `__pycache__` yazdı (mtime 19:02–19:06).

## Yerleşim (ölçülen kutular, px)
| Blok | y | x | İçerik |
|---|---|---|---|
| kanal | 291–341 | 53–602 | logo `#logoimg` 193,49×48 x 53,15 y 291 · `@ydspublishing` Lexend 700 42 x 263 taban 330 (`<g id="kanal">`, `#kunye` içinde) |
| kunye | 386–434 | 60–868 | `Simple Present vs Present Continuous` Fredoka 700 34 taban 420 · rozet `YDT · BASIC` Lexend 700 26, x 664,6 |
| soru | 476–552 | 60–526 | `Genel mi, şu an mı?` Caveat 700 72 |
| kart | 568–864 | 60–960 | çerçeve rect x 62 w 896 rx 32 (dış kenar 60–960) · `Today` sarı hap (594–682) + `iki zamanda` / `da geçebilir;` / `farkı anlam yapar.` Fredoka 700 72, taban 658 · 744 · 826 |
| eslesme | 878–1019 | 60–776 | küçük mont + `wears` → `GENERAL` · küçük tişört + `is wearing` → `RIGHT NOW` (Caveat 700 64; ok kalem çizgisi, ikincil; ok uçları x 460'ta hizalı) |
| kaydet | 1033–1138 | 581–960 | Tabler `bookmark` yer imi (mürekkep çizgi 6, dolgu yok) + `Kaydet` Fredoka 700 88, sağ kenar 960 |
| boş | 1150–1920 | — | bağ çıkartması (1150–1380) + altyazı/platform bandı; hiçbir şey çizilmez |

Tek sarı öğe `Today` hapı (künye rozeti hariç; uret.py `#icerik` içinde `fill="#f2a93b"` = 1 assert). Açıkta hap `#ffe066` + yazı `#1b2440`,
koyuda `#f2a93b` + `#1b1a17`. Kırmızı, emoji, QR, süre sözü yok. Kanal katmanı GSAP dışında: iki `tl.set` yalnız `#icerik`'i hedefler.
Yer imi kaynağı: Tabler Icons `bookmark` (MIT), 24×24 yol `M18 7v14l-6 -4l-6 4v-14a4 4 0 0 1 4 -4h4a4 4 0 0 1 4 4z` (uret.py `YERIMI_D`).

## Olay listesi (tek kare)
| Olay | Kare / küresel sn | Cümle sözcüğü |
|---|---|---|
| bütün öğeler görünür: kanal katmanı + künye · soru · kural kartı (`Today` sarı hap) · eşleşme 2 satır · yer imi + `Kaydet` | kare 0 (yakalama 0,5 sn; çizelge 1,0 sn); küresel sn yok | — (anlatım yok; metin BRIEF-S2 Hikâye A, `hikaye-taslak.md` §3) |

## Kapı sonucu (son satırlar)
```
ONIZLE_YALNIZ=1 bash calistir.sh   → "önizleme hazır", rc_onizle=0
bash calistir.sh --tema acik       → png,1080,1920 · …/02-04-ydt-temel-s2/hikaye-a.png · …/hikaye.png · rc_acik=0 · cmp_ayni
bash calistir.sh --tema koyu       → png,1080,1920 · …/k/hikaye-a-koyu.png · rc_koyu=0
node araclar/cakisma-kapisi.mjs 02-04-ydt-temel-s2 --sahne 04-hyperframes-hikaye --port 41333 --sunucu 41022
  → HATA sahne bulunamadı: 04-hyperframes-hikaye   (rc=2; beklenen: sahne zaman.json sahneler[] dışında, araç değiştirilmedi)
grep -rniE … "tam ders|dakika" projeler/02-04-ydt-temel-s2/sahneler/04-hyperframes-hikaye/ --exclude-dir=k
  → boş (grep_rc=1)
```
qa-yerel koşmadı (istem: t değerleri küresel anlatım saniyesidir; bu sahnenin anlatımda saniyesi yok).
Çakışmayı uret.py assert'leri (blok kesişimi 0, dikey boşluk ≥ 12, x ∈ [53, 960], içerik y ∈ [460, 1150], kart ve eşleşme iç kuralları) ve gözle denetim karşılar.
Boş bant piksel ölçümü (satır medyanından > 40 sapan piksel olan satır sayısı): iki temada 0–280 → 0, 1150–1920 → 0, x 962–1080 (y 460–1380) → 0.

## Bakılan kareler ve bulgu
| Tur | Kare | Bulgu | Yapılan |
|---|---|---|---|
| 1 | `hikaye-a.png`, `k/hikaye-a-koyu.png` | taşma, kesik yazı, binme yok; kanal katmanı + künye iki temada yerinde; 0–280 ve 1150–1920 boş; içerik x 960'ı geçmiyor. Kusur: `Today` hapında `y` kuyruğu hap alt kenarına değiyor (yakın kırpım) | uret.py: hap üstü taban − 64 (−66 idi), yükseklik 88 (84), rx 44; satır 2–3 tabanı 744 / 826 (740 / 822). SPEC'e işlendi |
| 2 | aynı iki kare + yakın kırpım | `y` kuyruğu hapın içinde; satır 2 ile hap arası açık; kart alt payı 18 px. Açık ve koyu kontrast iyi | — (geçti) |
| — | metin taraması | ilk koşuda tek eşleşme uret.py'nin kendi yasak listesi (`"tam ders", "dakika"` literal) | liste düzenli ifadeye çevrildi (`tam\s+ders`, `dak[iı]ka`, `\bqr\b`); kareler değişmedi (sha aynı) |

## Açık noktalar
1. **Eşleşme bandı:** istem "570–1000 kural kartı + altında iki satır" der. 3 satır Fredoka 72 kart + 2 satır Caveat 64, 430 px'e kutu modeliyle sığmıyor; eşleşme 878–1019 (19 px aşım), Kaydet 1033–1138 (1010–1140 bandı içinde), 1150 altı boş. Kart satır aralığı 82 → 78 olursa sığar, ama hap ile satır 2 arası 6 px'e iner. Okunurluk seçildi.
2. **Künye satırı 36 karakter:** `Simple Present vs Present Continuous` 24 karakter sınırını aşar; BRIEF tek satır ve 34 px ister. uret.py satır denetiminde künyeyi saymaz.
3. **uret.py satır 15–17:** agy `/usr/local/lib/python3.10/dist-packages` ve `~/.local/lib/python3.10/site-packages` yollarını ekledi. `/usr/bin/python3 -I` kipinde fontTools yalnız bu yolla bulunur; `calistir.sh` `-I` kullanmaz. Mac'te yol yok, ekleme zararsız. Kalıcı çözüm paket düzeyinde (yazma kapsamı dışı).
4. **yardim.py kopyası:** paket HyperFrames sahnelerinde 6 ayrı `yardim.py` var; bu sahne S2 s03 v2 kopyasını taşır. Ortak dosya yok (BRIEF notu).
5. **Kanal kutu adı:** çakışma kapısı bu durağan kareyi ölçmedi. Grup yapısı (`#kunye > #kanal`) hf-kutu.mjs'de `kunye:kanal` grubunu verir; S2 s03 RAPOR madde 4'e göre kapı öğe adını `kunye:kanal:image0` / `text0` yazar.
6. **git:** `hikaye-a.png`, `hikaye.png` `.gitignore` (`projeler/*/*.png`) ve `k/` ile yok sayılır. Teslim commit'e girecekse `git add -f` gerekir.
7. **Yan etki:** `.claude/docs/sozlesme.md`'ye 1 satır eklendi (satır içi hap ölçüsü + `-I` fontTools notu; istemdeki tek istisna). `tema_damga.py` bu dosyanın `Tema:` satırını son koşuya göre yazar (son koşu koyu; teslim açık).
