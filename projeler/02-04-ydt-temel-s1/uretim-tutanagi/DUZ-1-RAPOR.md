# DUZ-1 raporu — huni v2 bağımsız inceleme bulgularının düzeltmesi · 15.11.2026

Yazan: şef oturumu (b8c1151c). İstem DUZ-1. Ses sentezi, ElevenLabs, mp4, commit, ayna yüklemesi, alt ajan YOK.

| # | Paket | Bulgu | Durum | Kanıt |
|---|---|---|---|---|
| 1 | 02-04-ydt-temel-s1 | Hikâye B doğru cümleyi üstü çizili gösteriyor | düzeltildi, iki tema yeniden çekildi | çakışma kapısı çıkış 0; Read ile bakıldı |
| 2 | 02-04-ydt-temel-s1 | "konusu püf noktası", küçük harf `utm_campaign`, `aciklama.md` `utm_content=s1` | düzeltildi | grep sayımları aşağıda |
| 3 | simple-present-temel-s1 | "geniş zaman eki = İngilizcedeki s" yanlış denkliği | düzeltildi; seste ve ekranda yoktu | grep 0 (adı geçen 5 dosya) |
| 4 | simple-present-temel-s2 | `always` için istisnasız kural | açıklama yumuşatıldı | önce/sonra tablosu |

## 1. Hikâye B (`sahneler/07-hyperframes-hikaye-b`)

Değişen: `uret.py`, `SPEC.md` (üst not + §3, §3.2, §3.3, yeni §3.3a, §3.6, §3.7, §4, §5, §6), `nesneler.json` (7 → 9 blok),
`proje/index.html` (uret.py + hf_tema yazar), paket kökü `hikaye-b.png`, `k/koyu/hikaye-b-koyu.png` (ikisi git dışı; ayna).

**Önce:** sol üstte yeşil çerçeveli tam genişlik kart (`I am living` / `with my uncle.`, sağda tik); altında tek satır soluk
`I live with my uncle.` ve üstünden geçen gri çizgi. Okunuş: "bu cümle hatalı".

**Sonra:** iki şık yan yana. Sol: yeşil çerçeveli kart (x 60–628), `I am living with` / `my uncle.` (Fredoka 72), tik 2. satırın
sağında. Sağ: soluk (0,45) `I live with` / `my uncle.` (Fredoka 64), satır tabanları kartla ortak, üstü çizgi YOK. Altlarında aynı
satırda (taban 914) küçük etiketler, Caveat 700 48: kartın altında yeşil `şimdilik → geçici` (ok SVG kalem çizgisi; yazı tiplerinde
U+2192 yok), soluk şıkkın altında gri `kalıcıysa`. Türkçe cümle, kural özeti, kanal katmanı, künye, `Kaydet` yer ve biçim olarak aynı.

Tasarım kararları (şef):
- Satır ≤ 24 kuralı (`I am living with my uncle.` = 26) şıkkı tek satıra izin vermez. Alt alta düzende iki etiket satırı 864–984
  arasına sığmaz (özet 1140 sınırına dayalı). Bu yüzden yan yana düzen; satır kırılımı iki şıkta aynı (`… with` / `my uncle.`).
- Etiket boyu 48 (istem "küçük etiket"); assert ≥ 44. Ana yazı boyları ≥ 64 aynen.
- Koyu tema yeşil yazı için CSS'e `#root:not(.tema-acik) [fill="#167a4a"]{fill:#4fbf85}` eklendi (hf_tema yeşili tanımaz).
- Ok ile "şimdilik" arası 12 px'te Caveat eğik `k` oka yaklaşıyordu → 18 px (1. tur kare, düzeltilip yeniden çekildi).

Kanıt:
```
$ /usr/bin/python3 uret.py                       → index.html yazıldı 7905 (assert'ler geçti: kesişim 0, boşluklar, satır ≤ 24, kimlikler)
$ bash calistir.sh --tema acik                   → png,1080,1920 · …/02-04-ydt-temel-s1/hikaye-b.png
$ bash calistir.sh --tema koyu                   → png,1080,1920 · …/k/koyu/hikaye-b-koyu.png
$ bash calistir.sh --tema acik                   → (son çekim açık: RAPOR.md "Tema:", logo.svg, index.html varsayılan açıkta kalsın)
$ node araclar/cakisma-kapisi.mjs 02-04-ydt-temel-s1 --sahne 07-hyperframes-hikaye-b --port 41333 --sunucu 41022
HATA sahne bulunamadı: 07-hyperframes-hikaye-b    (çıkış 2; araç yalnız zaman.json sahneler[] okur, durağan kare orada yok)
$ KALEM_KOK=~/Silinecekler/2026-11-15-huni-v2/duz1-kapi-kok SAHNE_KARE_BETIK=$PWD/araclar/sahne-kare.mjs \
  node araclar/cakisma-kapisi.mjs 02-04-ydt-temel-s1 --sahne 07-hyperframes-hikaye-b --port 41333 --sunucu 41022
07-hyperframes-hikaye-b | çakışma yok (3 örnek, 333 kutu)    (çıkış 0)
```
Geçici kök: repo dosyasına dokunmadan, gerçek `zaman.json` kopyası + `sahneler[]` içine bu sahne (HyperFrames, t 0–0,5, kare 30) +
`sahneler` symlink'i. Önizleme sunucusu (41022) gerçek kökü sunar; ölçülen sayfa gerçek `proje/index.html`.
Read ile bakılan kareler: `hikaye-b.png` (açık), `k/koyu/hikaye-b-koyu.png` (koyu) → üstü çizgi yok, iki etiket okunuyor, taşma yok,
x 960 sağı ve 1150–1920 boş, koyu temada yeşil `#4fbf85`. Son açık çekim md5 `f52753bb7223…` (gözle bakılan kareyle aynı).
Önceki (çizgili) dosyalar: `~/Silinecekler/2026-11-15-huni-v2/02-04-ydt-temel-s1/sahneler/07-hyperframes-hikaye-b/v2-cizgili/`.

## 2. S1 açıklama metni

Değişen: `aciklama-a.md`, `aciklama-b.md`, `aciklama.md`. Aynı dosyalarda `utm_campaign` tablo satırı da düzeltildi ("küçük harf;
huni-plan §6'dan sapma" notu yanlış kalacaktı) → S2 ile aynı söz: "ana ders kodu olduğu gibi; huni-plan §6 şeması". `aciklama.md`
`utm_content` tablo satırı `s1` → `s1-a`.
```
aciklama-a.md ING=5 ing=0 konusu=0
aciklama-b.md ING=5 ing=0 konusu=0
aciklama.md   ING=5 ing=0 konusu=0
(ING = grep -c "utm_campaign=ING-YDT-GR-02-04-T" · ing = grep -c "utm_campaign=ing-" · konusu = grep -c "konusu püf")
grep -c "konusunun püf" → aciklama-a.md 1 · aciklama.md 1   (aciklama-b.md bu cümleyi taşımıyor)
aciklama.md: utm_content=s1 (yalın) → 0; aciklama-a.md satır 4 "tek fark `utm_content=s1` → `s1-a`" tarih notu, URL değil
```

## 3. simple-present-temel-s1 yanlış denklik

Değişen: `aciklama-a.md`, `aciklama-b.md`, `aciklama.md` (satır `Simple Present (ING-YDT-GR-02-02-T): …`), `surumler.json`
(`video.canAlici[0]`; dosyada ayrı açıklama alanı yok, cümle yalnız burada), `ortak/anlatim/senaryo.json` (`meta.kapak.canAlici`,
`meta.canAlici[0]`). Yeni metin: `Gider = goes; ama yalnız he, she, it ile. I, you, we, they ile go.`
SES ve EKRAN cümlelerinde cümle YOKTU (senaryo.json'da yalnız meta satırları 126, 135) → ses yeniden gerekmez.
```
json.load: surumler.json OK · ortak/anlatim/senaryo.json OK (biçim korunarak dizgi değişimi; git diff: senaryo.json 2 satır, surumler.json 1 satır)
grep -c "eki = İngilizcedeki": aciklama-a.md 0 · aciklama-b.md 0 · aciklama.md 0 · surumler.json 0 · ortak/anlatim/senaryo.json 0
```
**DİKKAT:** paket genelinde grep 0 DEĞİL. Adı geçmeyen dosyalara dokunulmadı: `BRIEF-S1.md` 1, `uretim-tutanagi/aciklama-taslak.md` 3,
`kapak-taslak.md` 1, `S1-duzeltme.md` 1, `juri/s1.dil.md` 1. Bunlar tutanak/brif; jüri notu eski cümleyi alıntı olarak taşır.
Şef karar verirse BRIEF ve taslaklar ayrı istemle düzeltilir.

## 4. simple-present-temel-s2 `always` (yalnız açıklama)

Değişen: `aciklama-a.md`, `aciklama.md` (4'er satır, iki dosya aynı), `aciklama-b.md` (3 satır). Video, ses, ekran, kapak DEĞİŞMEDİ.

| Dosya | Önce | Sonra |
|---|---|---|
| a + aciklama | `Usually, always, every day = Simple Present \| YDT İngilizce #Shorts` | `Usually, always, every day görürsen: çoğunlukla Simple Present \| YDT İngilizce #Shorts` |
| a + aciklama | `… püf nokta: usually, always, every day alışkanlık işaretidir.` | `… püf nokta: usually, always, every day çoğunlukla alışkanlık işaretidir.` |
| a + aciklama | `Usually, always, every day: alışkanlık işareti. Alışkanlık: Simple Present.` | `Usually, always, every day: çoğunlukla alışkanlık işareti. Alışkanlık: Simple Present.` |
| a + aciklama | `Usually, always, every day: Simple Present. My brother …` | `Usually, always, every day: çoğunlukla Simple Present. My brother …` |
| b | `… hangi zaman? Alışkanlık işareti: Simple Present. Şu an olan iş değil.` | `… hangi zaman? Çoğunlukla alışkanlık işareti: Simple Present. Şu an olan iş değil.` |
| b | `Usually, always, every day: alışkanlık işareti. İlk akla gelen: Simple Present.` | `Usually, always, every day: çoğunlukla alışkanlık işareti. İlk akla gelen: Simple Present.` |
| b | `Always varsa hangi zaman? Usually, always, every day: alışkanlık. İlk akla gelen: …` | `Always varsa hangi zaman? Usually, always, every day: çoğunlukla alışkanlık. İlk akla gelen: …` |

Dokunulmadı: `aciklama-b.md` satır 60 cevap notu (`usually` + örnek cümle; bağlamlı, doğru).

## Dokunulmayan benzer kusurlar (görüldü)

- `simple-present-temel-s3`, `simple-present-temel` (ana ders), `deneme-kupur`: `surumler.json` + `ortak/anlatim/senaryo.json`
  aynı "eki = İngilizcedeki s" `canAlici` cümlesini taşır.
- `simple-present-temel-s1` ve `-s2` `surumler.json`, `-s2` `senaryo.json`: `usually, always, every day = tekrar eden iş sinyali`
  (`canAlici`; madde 4 ile aynı kesinlik).
- `02-04-ydt-temel-s2` `aciklama*.md` satır 91/96 ve `02-04-ydt-temel-s3` `aciklama*.md` `utm_campaign` satırı: "S1 küçük harf
  kullanır" notu artık bayat.
- `02-04-ydt-temel-s1/uretim-tutanagi/aciklama-taslak.md`, `hikaye-taslak.md`: eski küçük harf `utm_campaign`.
- `02-04-ydt-temel-s1/BRIEF-S1.md` satır 76: hikâye B tarifi eski düzen (doğru kart üstte, soluk şık altta).
- `02-04-ydt-temel-s1/sahneler/07-hyperframes-hikaye-b/RAPOR.md` eski (çizgili) sürümü anlatır; istem güncelleme istemedi.
- `araclar/cakisma-kapisi.mjs` durağan kareyi (`duragan`) okumaz; bütün hikâye B / kapak B-C karelerinde çıkış 2 (S1/S2/S3 raporları).

## Değiştirilen dosyalar (tam liste)

Git'te izlenen:
- `.claude/docs/sozlesme.md` (sona 1 satır: hikâye B, bağlama uymayan doğru cümle çizilmez + kapı geçici kökü); dosyada oturum öncesinden 6 satırlık commit'lenmemiş ekleme de var
- `projeler/02-04-ydt-temel-s1/aciklama-a.md`
- `projeler/02-04-ydt-temel-s1/aciklama-b.md`
- `projeler/02-04-ydt-temel-s1/aciklama.md`
- `projeler/02-04-ydt-temel-s1/sahneler/07-hyperframes-hikaye-b/uret.py`
- `projeler/02-04-ydt-temel-s1/sahneler/07-hyperframes-hikaye-b/SPEC.md`
- `projeler/02-04-ydt-temel-s1/sahneler/07-hyperframes-hikaye-b/nesneler.json`
- `projeler/02-04-ydt-temel-s1/sahneler/07-hyperframes-hikaye-b/proje/index.html`
- `projeler/02-04-ydt-temel-s1/uretim-tutanagi/DUZ-1-RAPOR.md` (yeni, bu dosya)
- `projeler/simple-present-temel-s1/aciklama-a.md`
- `projeler/simple-present-temel-s1/aciklama-b.md`
- `projeler/simple-present-temel-s1/aciklama.md`
- `projeler/simple-present-temel-s1/surumler.json`
- `projeler/simple-present-temel-s1/ortak/anlatim/senaryo.json`
- `projeler/simple-present-temel-s2/aciklama-a.md`
- `projeler/simple-present-temel-s2/aciklama-b.md`
- `projeler/simple-present-temel-s2/aciklama.md`

Git dışı (`.gitignore`; aynaya yüklenecek):
- `projeler/02-04-ydt-temel-s1/hikaye-b.png`
- `projeler/02-04-ydt-temel-s1/sahneler/07-hyperframes-hikaye-b/k/koyu/hikaye-b-koyu.png` (ve `k/at-0.5s.png`, `k/koyu/at-0.5s.png`)

**DİKKAT (commit):** çalışma ağacında bu istem dışı değişiklikler de var: `huni-konu.{json,md}` (oturum başında vardı),
`ortak/youtube/`, `projeler/02-04-ydt-temel-s2b/`, `projeler/simple-present-temel-s2b/` (eş-oturum). Commit'te `git commit --only`
ile yalnız yukarıdaki liste.
