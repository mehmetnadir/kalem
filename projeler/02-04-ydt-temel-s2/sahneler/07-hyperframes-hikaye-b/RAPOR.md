# Sahne 07 · Hikâye B v2 — soru kartı (huni v2; HyperFrames, 1080×1920, tek kare, ses yok; zaman çizelgesi dışı)

Tema: acik

Durum: v2 yazıldı. Tek kare iki temada yakalandı. mp4 yok, birleştirme yok. `zaman.json` değişmedi (`duragan` listesi, `sahneler[]` dışında).
v1 (SPEC, RAPOR, uret.py, yardim.py, kareler) yedekte: `~/Silinecekler/2026-11-15-huni-v2/02-04-ydt-temel-s2/sahneler/07-hyperframes-hikaye-b/`
(`cp -a`). Eski kök `hikaye-b.png` V2 yedeğinde: `~/Silinecekler/2026-11-15-huni-v2/02-04-ydt-temel-s2/hikaye-b.png`.

| Çıktı | Yol | Boyut · sha256 |
|---|---|---|
| açık (teslim) | `projeler/02-04-ydt-temel-s2/hikaye-b.png` | 1080×1920 (ffprobe, calistir.sh denetimi) · `c74a416c9697…` |
| koyu | `sahneler/07-hyperframes-hikaye-b/k/koyu/hikaye-b-koyu.png` | 1080×1920 · `763243891980…` |
| ham yakalama | `k/at-0.5s.png` (açık) · `k/koyu/at-0.5s.png` (koyu) | 1080×1920 |
| QA yakın kırpım | `k/qa/yakin-kok-sik*.png` | kök + şık bandı, 1,5× |

## Dosyalar
| Dosya | Kim yazdı | Not |
|---|---|---|
| `SPEC.md` | şef | v2 tasarım: yerleşim, ölçüler, tema kuralları, kabul ölçütü; QA tur 1 değerleri işlendi (§3, §4.3.2, §4.3.3) |
| `uret.py` | agy-filo (rol kod, gemini-3.8-flash-high, 250 sn, 1 tur) | şef baştan sona okudu; SPEC'e uyuyor. Şef QA tur 1'de küçük Edit yaptı: `DAIRE_R` 34 → 36, `HARF_KAYMA` 19, `BOS_KAYMA` 6, harf–daire uzaklık assert'i, `_norm_sik` harf tabanı |
| `yardim.py` | şef kopyası: `sahneler/04-hyperframes-hikaye/yardim.py` (S2 v2; sha256 `3d1ac3d54474…`, s03 ile aynı) | kanal katmanı + künye `Y.kunye_svg()`; `HUD` istemdeki değerlerle aynı |
| `calistir.sh` | v1 + şef Edit | `GEN=1080; YUK=1920` + ffprobe boyut denetimi eklendi (s04 kalıbı); `uret.py && olay.py` iki satıra bölündü (sözleşme dersi: `set -e` zincirde uret.py hatasını yutar); homebrew koşullu, `Y=$(yuk1)` zaten vardı. Bölmeden sonra açık kare yeniden yakalandı: sha256 aynı |
| `olay.py`, `zamanlar.json` | v1, değişmedi | `olaylar.json` = `[]`; çizelge 1,0 sn, yakalama 0,5 sn |
| `nesneler.json` | uret.py | 8 blok + `tisort` |

agy koşu özeti: `/home/sef/.claude/canavar/agy-filo/20261115-191804/ozet.md` (1/1 başarılı). Özetteki "değişen 276" listesi ortak worktree'deki
paralel oturumların dosyalarını da sayar (02-03 s90, `sozlesme.md` vb.). Bu koşu bu sahnede `uret.py`, `nesneler.json`, `proje/index.html` yazdı (mtime 19:21).

## Yerleşim (ölçülen kutular, px; nesneler.json)
| Blok | y | x | İçerik |
|---|---|---|---|
| kanal | 291–341 | 53–602 | logo `#logoimg` 193,5×48 x 53,15 y 291 · `@ydspublishing` Lexend 700 42 x 263 taban 330 (`<g id="kanal">`, `#kunye` içinde; tween dışı) |
| kunye | 386–434 | 60–868 | `Simple Present vs Present Continuous` Fredoka 700 34 taban 420 · rozet `YDT · BASIC` Lexend 700 26 |
| baslik | 470–558 | 60–645 | `Hangisi doğru?` Fredoka 700 88, taban 536 |
| kok | 570–736 | 60–960 | çerçeve rect x 62 w 896 rx 28 · `Look! She` + boşluk kalem çizgisi (200 px, y 640) + `her` / `pink T-shirt today.` Fredoka 700 64, taban 634 · 704 · küçük tişört x 844–934 y 615–691 (mürekkep çizgi) |
| kA | 748–840 | 60–960 | daire r 36 + `A` (Fredoka 64) · `wears` Fredoka 700 64 |
| kB | 852–944 | 60–960 | kA ile birebir aynı biçim (assert) · `B` · `is wearing` |
| ipucu | 956–1023 | 60–474 | `Genel mi, şu an mı?` Caveat 700 64 |
| kaydet | 1036–1138 | 60–434 | Tabler `bookmark` yer imi SARI dolgu + mürekkep çizgi 6 · `Kaydet` Fredoka 700 88, SOLA yaslı |
| boş | 1150–1920 | — | bağ çıkartması (1150–1380) + altyazı/platform bandı; hiçbir şey çizilmez |

Tek sarı öğe yer imi dolgusu (künye rozeti hariç; uret.py `#icerik` içinde `fill="#f2a93b"` = 1, `stroke` = 0; kök ve şık gruplarında sarı yok).
Dolgu `clipPath` ile kırpılmış `<rect>`: hf_tema yalnız `rect|circle` sarısını açık temada `#ffe066` (vurguDolgu) yapar; `<path fill>` `#d9900f` olurdu.
Açıkta dolgu `#ffe066`, koyuda `#f2a93b`. Cevap yok: şıklarda vurgu, tik, yeşil yok; kökte `wears` / `is wearing` yok; `Look!` vurgusuz.
Kaldırılanlar (v1): `Cevap ve neden:` / `tam derste`, ikinci `@ydspublishing` hapı, `Full lesson` çipi, v1 HUD (logo y 48, ders adı 2 satır).
Yer imi kaynağı: Tabler Icons `bookmark` (MIT), 24×24 yol `M18 7v14l-6 -4l-6 4v-14a4 4 0 0 1 4 -4h4a4 4 0 0 1 4 4z` (uret.py `YERIMI_D`).

## Olay listesi (tek kare)
| Olay | Kare / küresel sn | Cümle sözcüğü |
|---|---|---|
| bütün öğeler görünür: kanal katmanı + künye · `Hangisi doğru?` · kök kartı · şık A · şık B · ipucu · yer imi (sarı) + `Kaydet` | kare 0 (yakalama 0,5 sn; çizelge 1,0 sn); küresel sn yok | — (anlatım yok; metin BRIEF-S2 Hikâye B, `hikaye-taslak.md` §4, `S2-duzeltme.md` madde 1) |

## Kapı sonucu (son satırlar)
```
ONIZLE_YALNIZ=1 bash calistir.sh   → index.html yazıldı 8538 · baslik=470-558 kok=570-736 kA=748-840 kB=852-944 ipucu=956-1023 kaydet=1036-1138 · önizleme hazır · rc_onizle=0
bash calistir.sh --tema acik       → png,1080,1920 · …/02-04-ydt-temel-s2/hikaye-b.png · rc_acik=0
bash calistir.sh --tema koyu       → png,1080,1920 · …/k/koyu/hikaye-b-koyu.png · rc_koyu=0
node araclar/cakisma-kapisi.mjs 02-04-ydt-temel-s2 --sahne 07-hyperframes-hikaye-b --port 41333 --sunucu 41022
  → HATA sahne bulunamadı: 07-hyperframes-hikaye-b   (rc=2; beklenen: sahne zaman.json sahneler[] dışında, araç değiştirilmedi)
grep -rniE … "tam ders|dakika" projeler/02-04-ydt-temel-s2/sahneler/07-hyperframes-hikaye-b/ --exclude-dir=k
  → boş (grep_rc=1)
```
qa-yerel koşmadı (istem: t değerleri küresel anlatım saniyesidir; bu sahnenin anlatımda saniyesi yok).
Çakışmayı uret.py assert'leri (blok kesişimi 0, dikey boşluk ≥ 12, x ∈ [53, 960], içerik y ∈ [460, 1150], kök/şık/kaydet iç kuralları,
harf–daire ≥ 4 px, tek sarı, cevap yok, yasak söz) ve gözle denetim karşılar.
Piksel ölçümü (satırda sol kenar x 0–40 medyanından > 40 sapan piksel olan satır sayısı), iki temada: 0–280 → 0 · 1150–1920 → 0 ·
x 962–1080 (y 460–1380) → 0 · kanal bandı 285–345 (x 53–620) → 44 dolu satır (kanal katmanı çizili).

## Bakılan kareler ve bulgu
| Tur | Kare | Bulgu | Yapılan |
|---|---|---|---|
| 1 | `hikaye-b.png` + yakın kırpım | taşma, kesik yazı, binme yok; kanal katmanı + künye yerinde; 0–280 ve 1150–1920 boş; x 960 sağı boş. Kusur 1: şık `A` harfinin ayakları daire çizgisine değiyor. Kusur 2: boşluk çizgisi (L1 + 12) alt satır `today` harflerine ≈ 8 px | uret.py: daire r 34 → 36, harf tabanı cy + 22 → cy + 19 (+ dairenin iç kenarına ≥ 4 px assert'i), boşluk çizgisi L1 + 6. SPEC'e işlendi |
| 2 | `hikaye-b.png`, `k/koyu/hikaye-b-koyu.png` + iki yakın kırpım | `A` ve `B` daire içinde ayrık; boşluk çizgisi `She` tabanında, alt satırdan ayrık; kontrast iki temada iyi (açık lacivert/krem, yer imi `#ffe066` + lacivert çizgi; koyu krem çizgi, yer imi `#f2a93b`); kanal katmanı iki temada yerinde | — (geçti) |

## Açık noktalar
1. **Bant aşımı:** istem kök + şıklar + ipucu için 570–1000 der. İki satır kök (Fredoka 64) + iki şık kartı (64) + ipucu (Caveat 64) kutu modeliyle
   430 px'e sığmaz; ipucu 956–1023 (23 px aşım). Kaydet 1036–1138 (1010–1140 bandında), 1150 altı boş. Hikâye A (s04) aynı yolu seçti (19 px aşım).
2. **Yer imi sarısı (sahne 08 için):** sarı dolgu `<path fill>` ile yazılırsa açık temada `#d9900f` çıkar; bu sahne `clipPath` + `<rect>` ile `#ffe066`
   aldı. Sahne 08 (kaydet, henüz yok) aynı yer imini sarı yapacak: aynı yöntem tutarlılık verir. `ortak/hf_tema.py`'ye `path` seçicisi kapsam dışı.
3. **Künye satırı 36 karakter:** `Simple Present vs Present Continuous` 24 karakter sınırını aşar; BRIEF tek satır ve 34 px ister; uret.py saymaz.
4. **uret.py satır 15–17:** s04 kalıbıyla iki site-packages yolu eklenir (`-I` kipinde fontTools için). `calistir.sh` `-I` kullanmaz; zararsız.
5. **Tişört rengi:** "pembe tişört" çizimi mürekkep çizgi; pembe palet dışı (tek vurgu), v1 ile aynı.
6. **git:** `hikaye-b.png` `.gitignore:27` (`projeler/*/*.png`), koyu kare `.gitignore:36` (`k/`) ile yok sayılır. Teslim commit'e girecekse `git add -f`.
7. **Instagram test çıkartması** (taslak §4 notu): elle konursa 1150–1380 boş bandına konmalı; şık kartlarını örtmez.
8. `tema_damga.py` bu dosyanın `Tema:` satırını son koşuya göre yazar (son koşu açık = teslim; `proje/index.html` açık temada).
