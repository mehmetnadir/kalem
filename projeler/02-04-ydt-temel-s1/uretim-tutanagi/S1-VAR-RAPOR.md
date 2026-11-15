# S1-VAR raporu — 02-04-ydt-temel-s1 huni sürümleri (kapak B/C, hikâye B, açıklama B) · 15.11.2026

| Ölçü | Değer |
|---|---|
| Yeni PNG (açık, paket kökü) | `kapak-b.png`, `kapak-c.png`, `hikaye-b.png` — üçü 1080×1920 (`file`) |
| Koyu kareler | `sahneler/05…/k/koyu/kapak-b-koyu.png`, `06…/k/koyu/kapak-c-koyu.png`, `07…/k/koyu/hikaye-b-koyu.png` — 1080×1920 |
| A kopyaları | `kapak-a.png` = `kapak.png` (sha256 `0df9d59e7737…`), `hikaye-a.png` = `hikaye.png` (`0196fdb33b15…`), `aciklama-a.md` |
| Yeni açıklama | `aciklama-b.md` (`utm_content=s1-b`) |
| Huni satırları | `uretim-tutanagi/huni-surumler.json` — 7 satır, `durum: inceleme` |
| agy koşusu | 3 (paralel), 3/3 başarılı, 1 tur; şef düzeltmesi 1 (kapak B) |
| mp4, ses, commit | yok |

## 1. Dosyalar

| Dosya | Durum | Yazan |
|---|---|---|
| `uretim-tutanagi/kapak-taslak.md` | §5 (B), §6 (C), §7 (A/B/C farkı) eklendi; eski metin aynı | şef |
| `uretim-tutanagi/hikaye-taslak.md` | §6 (B) eklendi | şef |
| `uretim-tutanagi/aciklama-taslak.md` | §8 (B seti) eklendi | şef |
| `aciklama-a.md` | `aciklama.md` kopyası; fark: başlık "SET A", 1 kaynak satırı, `utm_content=s1` → `s1-a` (5 bağlantı + tablo), `kapak-a.png` / `hikaye-a.png` adları | şef (sed, diff ile denetlendi) |
| `aciklama-b.md` | yeni | şef |
| `kapak-a.png`, `hikaye-a.png` | kopya (`cp -p`); özgün dosyalar yerinde | şef |
| `zaman.json` | `duragan` listesi eklendi (05, 06, 07; `klasor`, `motor`, `kare 1`, `cikti`, `ad`, `not`). Eski alanlar birebir (Python ile karşılaştırıldı). `birlestir.py` / `kur.py` yalnız `sahneler[]` okur | şef |
| `surumler.json` | kısa video satırı `kimlik`: `shorts` → `s1` (ad aynı) | şef |
| `uretim-tutanagi/huni-surumler.json` | 7 satır: `s1-kapak-a/b/c`, `s1-hikaye-a/b`, `s1-aciklama-a/b`. Önceki 3 satır `~/Silinecekler/2026-11-15-0204/s1-huni-surumler.onceki.json` | şef |
| `sahneler/05-hyperframes-kapak-b/` | `SPEC.md` (şef) · `uret.py` (agy + 1 şef Edit) · `yardim.py`, `cizim/` (sahne 01 kopyası) · `calistir.sh`, `olay.py`, `zamanlar.json` (sahne 04 kopyası, çıktı adı uyarlandı) | |
| `sahneler/06-hyperframes-kapak-c/` | aynı düzen; `uret.py` agy, şef Edit yok | |
| `sahneler/07-hyperframes-hikaye-b/` | aynı düzen (`cizim/` yok); `uret.py` agy, şef Edit yok | |
| `uretim-tutanagi/kontak/s1-var-yanyana.png` | kapak A·B·C + hikâye A·B yan yana (her biri 360 px) | ffmpeg |

## 2. Sürüm farkları

| | Kapak A | Kapak B | Kapak C |
|---|---|---|---|
| Başlık | `YAŞIYORUM` / `= İKİ ZAMAN` | `YAŞIYORUM` / `NASIL DENİR?` (S 153) | `I LIVE` / `I AM LIVING` (S 173) |
| Kip | Türkçe yargı | Türkçe soru (cevap yok) | İngilizce karşıt çift |
| Tek vurgu | satır 2 sarı hap | `YOR` sarı kutu | `AM LIVING` sarı kutu |
| Kısa kod | EN etiket | EN soru balonu `I live?` / `I am living?` (Caveat 88) | TR etiket `kalıcı` / `geçici` (Caveat 88) |
| Sahne | ev · bavullu figür | figür · düşünce izi · 2 balon (ev, bavul) | ev · figür · bavul |

| | Hikâye A | Hikâye B |
|---|---|---|
| Kip | kural kartı | soru kartı (cevap yok; doğru cevap B, karede ve açıklamada yazmaz) |
| İçerik | `YAŞI-YOR-UM` + PERMANENT/TEMPORARY kartları | `Şimdilik amcamla` / `yaşıyorum.` · `Hangisi doğru?` hapı · A `I live / with my uncle.` · B `I am living / with my uncle.` |
| Çağrı | `Tam ders:` / `profildeki bağlantı` | `Cevap tam derste:` / `profildeki bağlantı` (örnek ana derste var: `02-04-ydt-temel` senaryo "I am living with my uncle … şimdilik") |
| Çip | `Full lesson` | `Quiz` |

| | Açıklama A (`s1-a`) | Açıklama B (`s1-b`) |
|---|---|---|
| Açılış | yargı: "Türkçede yaşıyorum tek sözcük…" | soru: "Yaşıyorum İngilizcede nasıl denir: I live mı, I am living mi?" + "İkisi de doğru; seçimi anlam yapar." |
| YouTube başlığı | `Yaşıyorum: I live mı, I am living mi? \| YDT İngilizce #Shorts` | `"Yaşıyorum" İngilizcede nasıl denir? \| YDT İngilizce #Shorts` |
| Ortak | süre 4 dk 26 sn, sıradaki ders, etiketler, yer tutucular, `utm_campaign` | aynı |

## 3. Bakılan kareler

| Tur | Kare | Bulgu | Yapılan |
|---|---|---|---|
| 1 | `hikaye-b.png`, `k/koyu/hikaye-b-koyu.png` | taşma, kesik yazı, çakışma yok; 1536 altı boş; iki kart birebir aynı, cevap belirtisi yok; `ğ` kuyruğu hap içinde; koyuda kontrast iyi | — (geçti) |
| 1 | `kapak-b.png`, koyu | başlık 2 satır, kontur görünür, `YOR` kutusu harflere değmiyor; balon yazıları içeride. Düşünce noktaları iki ayrı iz, dağınık; baştan balona akış okunmuyor | uret.py: iki iz → tek iz (3 daire r 8/12/16), baştan iki balonun arasına (348, 1080); figür ve balon payı assert'li |
| 2 | `kapak-b.png`, koyu | iz baştan balonlara akıyor; başka bulgu yok | — (geçti) |
| 1 | `kapak-c.png`, koyu | iki `I` alt alta; kutu `I`'ya değmiyor, sağ kenar 1013 < 1016; etiketler ikonların üstünde; koyuda kontrast iyi. Etiketler farklı yükseklikte (ikon boyu farkı) | — (kabul; etiket kendi nesnesinin üstünde durur) |
| — | `kontak/s1-var-yanyana.png` | A/B/C başlık dili, vurgu ve sahne düzeni ayrı; 360 px küçük boyda da başlıklar okunur | — |

## 4. agy koşuları

| Sahne | Model | Süre | Sonuç | Özet |
|---|---|---|---|---|
| 05 kapak B | gemini-3.8-flash-high (rol kod) | 306 sn | başarılı, 1 tur | `~/.claude/canavar/agy-filo/20261115-122746/` |
| 06 kapak C | gemini-3.8-flash-high | 364 sn | başarılı, 1 tur | `…/20261115-122749/` |
| 07 hikâye B | gemini-3.8-flash-high | 140 sn | başarılı, 1 tur | `…/20261115-122752/` |

Şef üç `uret.py`'yi okudu; SPEC'e uygun (`duragan` doğrulaması, tek `set` çizelgesi, tema kuralları, blok assert'leri, tür ipuçları).
Kapsam denetimi: paket içinde 12:27:40 sonrası değişen dosyaların hepsi bu işin (find -newer). agy özetindeki "değişen" sayısı paralel
oturumların dosyalarını da sayar.

## 5. Kapılar

| Kapı | Sonuç |
|---|---|
| `uret.py` assert'leri (kesişim, sınır, boy ≥ 64, satır ≤ 24) | 3/3 geçti (`calistir.sh` içinde) |
| `calistir.sh --tema acik` / `--tema koyu` | 6/6 rc 0, `png,1080,1920` |
| Çakışma kapısı `node araclar/cakisma-kapisi.mjs 02-04-ydt-temel-s1 --sahne <klasör> --port 41333 --sunucu 41022` | ÖLÇEMEDİ: 3/3 `HATA sahne bulunamadı: <klasör>` (çıkış 2). Araç yalnız `zaman.json → sahneler[]` okur (`cakisma-kapisi.mjs` satır 50–56); durağan kareler bilerek dışarıda. Araç değiştirilmedi |

## 6. Açık noktalar

1. **Kapak C 5 sözcük:** istem C'yi `I live` / `I am living` olarak tanımlar; kalıp §4 "en çok 4 sözcük" der. 4 sözcüklü seçenek
   `I LIVE` / `I'M LIVING` (derste geçmeyen kısaltma). Karar Nadir (`kapak-taslak.md` §6).
2. **Profil bağlantısı tek:** Instagram/TikTok `bio` bağlantısı aynı anda tek `utm_content` taşır; A/B ayrımı UTM ile yalnız YouTube
   açıklamasında ölçülür, Instagram/TikTok'ta platform istatistiğiyle (`aciklama-b.md` §4).
3. **`hikaye-taslak.md` §5** hâlâ `utm_content=s1` yazar (var olan metin değişmedi); set değerleri `aciklama-a.md` `s1-a`, `aciklama-b.md` `s1-b`.
4. **Çip `Quiz`:** `ortak/kunye.js` `cipler`'de 05–07 satırı yok; hikâye B çipi sahne sabiti. Kapak B/C'de çip yok (kapak A gibi).
5. **Kapak B/C logo yeri:** kalıp §4 "logo alt sol" der; A gibi HUD sol üst (BRIEF-DIKEY §0 Nadir bulgusu).
6. **`aciklama.md` (özgün)** `utm_content=s1` ile duruyor; hangi set yayına girerse o dosya kullanılmalı.
7. **git:** yeni PNG'ler `.gitignore` (`projeler/*/*.png`, `k/`) ile yok sayılır; commit'e girecekse `git add -f` gerekir. Paket dizini zaten izlenmiyor (`??`).
8. **Paralel oturum izi:** `02-04-ydt-temel/sahneler/07-hyperframes-kural/proje/index.html` (12:20) ve `12-hyperframes-ozet/proje/index.html`
   (12:27:31) git'te değişmiş görünüyor (tema CSS'i yok). İkisi de bu işin agy koşularından (12:27:46+) önce; bu işe ait değil, dokunulmadı.
9. **Taşınan:** `07-hyperframes-hikaye-b/cizim/` (kullanılmayan kopya) → `~/Silinecekler/2026-11-15-0204/s1-07/` (LISTE.md satırı yazıldı).
   Önceki `surumler.json` ve `huni-surumler.json` aynı klasörde.

- 15.11 Kapak A altyazısız: `kapak-a.png`, `kapak.png` (açık) ve `sahneler/01-hyperframes-kapak/k/koyu/kapak-a-koyu.png` yeniden çekildi; altyazı bandı (İstanbul'da yaşıyorum…) kareden çıktı, 1080×1920.
- Yöntem: sahne 01 `proje` kopyasında yalnız CSS `#altyazi{display:none}` eklendi (sahne kodu değişmedi), `hyperframes snapshot --at 1.97` (sahne 05 kalıbı), açık ve koyu tema ayrı.
- Bakılan kareler: 3 PNG'ye Read ile bakıldı (açık, koyu; kapak.png = kapak-a.png aynı dosya). Eskiler `~/Silinecekler/2026-11-15-0204/` altında.
