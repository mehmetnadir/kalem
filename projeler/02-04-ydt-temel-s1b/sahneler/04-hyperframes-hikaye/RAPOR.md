# Sahne 04 · hikâye karesi A, huni v2 (HyperFrames, 1080×1920, tek kare, ses yok; zaman çizelgesi dışı) · 15.11.2026

Tema: acik

| Kapı | Sonuç |
|---|---|
| `calistir.sh --tema acik` | rc 0 · `png,1080,1920` · `…/02-04-ydt-temel-s1/hikaye-a.png` (+ `hikaye.png`, `cp -p`, aynı md5 `40d30b8d8303…`) |
| `calistir.sh --tema koyu` | rc 0 · `png,1080,1920` · `…/k/koyu/hikaye-a-koyu.png` (md5 `325ff6a66fbb…`) |
| `uret.py` assert'leri | rc 0 · `S=124` · 7 blok, kesişim 0, dikey boşluk ≥ 16, içerik x 60–960 / y 460–1140 |
| Çakışma kapısı `cakisma-kapisi.mjs … --sahne 04-hyperframes-hikaye --port 41333 --sunucu 41022` | çıkış 2 · `HATA sahne bulunamadı: 04-hyperframes-hikaye` (beklenen: araç yalnız `sahneler[]` okur, S1-VAR §5); çakışma gözle + blok assert'iyle denetlendi |
| Metin taraması `grep -rniE 'tam ders\|dakika' … --include=*.html/js/py` | boş (grep çıkış 1) |
| Kanal katmanı (piksel ölçümü) | açık + koyu aynı: logo mürekkebi x 60–239, y 298–330 (resim kutusu 53,2–246,7 × 291–339) · `@ydspublishing` x 265–595, y 296–339 (taban 330). Sahne 03 ölçümüyle aynı |
| İlk = orta = son | `snapshot --at 0,0.5,0.966` (açık): üç kare md5 `40d30b8d8303…`, teslim PNG ile aynı (`k/qa/`) |
| Boş bölgeler (piksel ölçümü, iki tema) | 0–280 boş · 1150–1920 boş · sağ 961–1080 (y 280–1570) boş · içerik mürekkebi x 60–959, y 476–1135 |

Durum: yazıldı, iki temada tek kare yakalandı. mp4 yok, git yok, `zaman.json` değişmedi.

## Dosyalar
| Dosya | Kim | Not |
|---|---|---|
| `SPEC.md` | şef | yerleşim, blok kutuları, kurallar, kabul ölçütü; QA 1 düzeltmeleri işlendi |
| `uret.py` | agy-filo (rol kod, gemini-3.8-flash-high, 208 sn, 1 tur) | şef baştan sona okudu; 3 küçük Edit (aşağıda) |
| `yardim.py` | sahne 03'ün v2 kopyası (`cp -p`) | `03-hyperframes-cta/yardim.py` sha256 `6f42605c38be…`; kapıdan geçmiş v2 `kunye_svg()` (kanal `<g id="kanal">` + `logoimg`, konu 34 px, rozet `YDT · BASIC`), `HUD` v2 bantları (kenar 60, içerik 460–1380, altyazı 1400–1550) |
| `calistir.sh` | şef Edit | çıktı `hikaye-a.png` + `hikaye.png` kopyası; koyu `k/koyu/hikaye-a-koyu.png` |
| `nesneler.json`, `proje/index.html` | uret.py | 7 blok: kanal, kunye, ek, kart1, kart2, ozet, kaydet |

agy koşu özeti: `/home/sef/.claude/canavar/agy-filo/20261115-190204/ozet.md` (1/1 başarılı). Özetteki "değişen" listesinde
paralel oturumların dosyaları da var (05/06 SPEC, 06 yardim.py, s2/s3, `sozlesme.md`); agy yalnız `uret.py` yazdı ve koşturdu
(`nesneler.json`, `proje/index.html`). `calistir.sh` ve `proje/assets/logo.svg` değişikliği şefin.

## Olay listesi (tek kare)
| Olay | Kare / sn | Cümle sözcüğü |
|---|---|---|
| bütün öğeler görünür: kanal (logo + `@ydspublishing`) · künye (`Simple Present vs Present Continuous` + `YDT · BASIC`) · `YAŞI-YOR-UM` (`YOR` sarı kutu, Fredoka 124) · kart 1 ev + `I live` + `PERMANENT` · kart 2 bavul + `I am living` + `TEMPORARY` · `Kalıcıysa geniş zaman,` / `geçiciyse şimdiki zaman.` (Fredoka 68) · yer imi + `Kaydet` sarı hap | kare 0 (yakalama 0,5 sn; çizelge 1,0 sn) | — (anlatım yok; kural özeti BRIEF-S1 girişi) |

Yerleşim (y): kanal 291–339 · künye 386–434 · ek 476–611 · kartlar 636–840 (x 60–498 / 522–960) · özet 873–1025 · kaydet 1048–1136 · boş 1150–1920.
Yazı boyları: ek 124, kart başlığı 64, etiket Caveat 64, özet 68, hap 64 (künye/kanal hariç hepsi ≥ 64). En uzun satır `geçiciyse şimdiki zaman.` (24).

## Bakılan kareler ve bulgu
| Tur | Kare | Bulgu | Yapılan |
|---|---|---|---|
| 0 | `hikaye-a.png`, `k/koyu/hikaye-a-koyu.png` | taşma, kesik yazı, çakışma yok; kontrast iki temada iyi; 0–280 ve 1150–1920 boş. Piksel ölçümü: kart 2 çerçeve çizgisi x 961'e, yer imi çizgisi x 57'ye taşıyor (çizgi kalınlığı merkezde) | kart rect x0+2 / 434 × 200 / rx 26; yer imi translate x 36 → 39 |
| 1 | aynı iki kare + `k/qa/at-{0,0.5,0.966}s.png` | içerik x 60–959; sağ 961–1080 boş; üç kare özdeş; tek vurgu sarı (açık `#ffe066` + `#1b2440`, koyu `#f2a93b` + `#1b1a17`), yeşil/kırmızı/emoji yok | — (geçti) |

Şef Edit'leri (uret.py): kart çerçevesi içeri (tur 0) · yer imi x (tur 0) · kural 8 (yasak söz assert'i) kaldırıldı: koddaki
literal `tam ders`/`dakika` listesi zorunlu grep taramasını kirletiyordu; denetim dış grep kapısında (standart §7.3).

## Açık noktalar
1. **Çakışma kapısı ölçmüyor:** durağan kare `zaman.json → sahneler[]` dışında; araç çıkış 2 verir. Ölçüm blok assert'i + piksel ölçümü + gözle.
2. **Çıkan satırlar:** `Türkçede tek sözcük` / `İngilizcede iki zaman` sığmadı (istemdeki izinle çıktı); v1 zaman bantları, `now` noktası ve altçizgi de yer için kalktı.
3. **İki kart yan yana:** tek sütun kuralına bu bantta istisna (istem bunu istiyor); `I am living` kart iç sınırına 6 px kalıyor (assert ile çivili).
4. **`zaman.json → hikaye.cikti`** hâlâ `hikaye.png` der; teslim `hikaye-a.png` + `hikaye.png` (aynı dosya). Alan güncellenmeli mi şef kararı (yazma kapsamı dışı).
5. **git:** `projeler/*/*.png` ve `k/` `.gitignore`'da; teslim commit'e girecekse `git add -f` gerekir.
6. **Ana ders yalnız okundu;** başka sahneye, `ortak/`a, `BRIEF-S1.md`'ye dokunulmadı.
