# KBC-RAPOR — 02-04-ydt-temel-s3b (A/B kol b, değişken `kanca`) · 15.11.2026 (istem KBC-0204S3)

| Ölçüm | Kol a (`02-04-ydt-temel-s3`) | Kol b (`02-04-ydt-temel-s3b`) |
|---|---|---|
| Değer (`varyant.deger`) | `kopru` (`TARİFE ≠ PLAN`, `leaves` / `am going`) | `yanlis-cumle` (ses "Hata nerede?" + ekranda `is leave at 7 pm today.`) |
| Toplam süre | 28,31 sn | 29,31 sn (`anlatim.m4a` ffprobe 29.310000; taslak tahmini 29,46) |
| İlk söz | 1,00 sn | 0,41 sn |
| Yeni sentez | — | 1 cümle · 1 parça · 12 karakter (≈ 0,06 TL) |
| Whisper en düşük | 0,98 (V2-C raporu) | 0,92 (parça 2·1, önbellek wav'ı kol a ile aynı; açık nokta 2) · yeni parça 1,00 |
| `diff -rq` satırı | — | 90 (bu rapor dahil); beklenmeyen 0 (`siniflama.txt`) |
| Çakışma kapısı | — | çıkış 0, 4 sahne çakışma yok (`kapi-cikti.txt`) |
| Üretici model | — | Claude Opus 5.5 (`claude-opus-5-5`); jüri başka modelle koşmalı (juri-olcutleri §1e) |

## 1. Değişen dosyalar (kol b)

| Dosya | Değişiklik |
|---|---|
| paket (tamamı) | kol a'nın `cp -a` kopyası, `uretim-tutanagi/` hariç; 445 ↔ 445 dosya; git dışı 215 varlık sha256 eşit, fark 0 (`kopya-denetim.txt`) |
| `ortak/{cizim,font,logo,hf_tema.py}`, `ortak/logo/yds-publishing-koyu-zemin.svg` | simge bağı → gerçek kopya (`cp -a <hedef>`; bağlar `~/Silinecekler/2026-11-15-kol-b/02-04-ydt-temel-s3b/bag/`); paket içinde bağ 0 |
| `ortak/anlatim/senaryo.json` | cümle 1 olarak kanca eklendi (`ogretmen`, TR `Hata nerede?`); `giris` (satır `HATA` / `NEREDE?`, sahne: tren, saat, figür; bilet yok) ve `meta.kapak` (`HATA` / `NEREDE?`, `is leave → leaves (tarife: V-s)`) kapak taslağı §3'ten. Kadro, sesler, kol a cümle 1–5 metni aynı (kol b'de 2–6) |
| `ortak/anlatim/sozcuk_uret.py` | `ILK` 1,00 → 0,41 (kayma tam 1,00 sn = 30 kare) |
| `ortak/anlatim/zaman_uret.py` | sahne son cümle no 1/3/4/5 → 2/4/5/6; `GIRIS_SN` = cümle 2 başı + 2,00 (kol a 3,00 = 1,00 + 2,00) |
| `ortak/anlatim/metin_uret.py` | METIN başlık satırı: sahne 01 4 sn, ilk söz 0,41 |
| `ortak/anlatim/` türevleri | `sentez.wav` (+ rapor), `cumle-1…6.wav`, `sureler.json`, `sozcukler.json`, `baslar.json`, `anlatim.wav`, `anlatim.m4a` (+ imza `ea6a7584…`), `altyazi.json` (9 parça), `METIN.md`; kök `zaman.json` |
| `sahneler/01-hyperframes-kapak/` | `uret.py` (kanca: başlık `HATA` / hap `NEREDE?`; satır 1 `Hata` sözüyle, yanlış satır 2 `nerede?` sözüyle kırpmayla; el çizimi `?` mürekkep; `Izmir` sözünde `is leave` üstü çizilir; yanlış satır `leaves` öncesi söner; başlık uçmaz, solar; tren uçuşu, satır kayması, `leaves at 7`, konu adı, kart çerçevesi kol a + 1,00 sn; figür 250 px aynalı, bilet ve `leaves` / `am going` etiketi yok), `zamanlar.json` (132 kare), `olay.py` (9 olay), `olaylar.json`, `calistir.sh` (KARE 132, denetim zamanları), `devir.json` (yalnız `t` 3,0 → 4,0), `proje/index.html`, `proje-ka*/` (kapak A kopyaları), `k/` (yeni QA kareleri), `SPEC.md` / `RAPOR.md` (başa kol b notu), `__pycache__` |
| `kapak-a.png`, `kapak.png` | kanca karesi 1,80 sn (kare 54), altyazı gizli (`proje-ka`, kol a yöntemi); `cmp` eşit; koyu `sahneler/01-…/k/koyu/kapak-a-koyu.png` |
| `surumler.json` | 4 satır: `s3b` (kısa, ad `S3b Shorts (29,31 sn)`, önizleme `/p/02-04-ydt-temel-s3b/onizle.html`, `varyant`), `s3b-kapak-a`, `s3b-aciklama-a`, `s3b-aciklama-b`; kapak B/C ve hikâye satırları çıktı |
| `aciklama.md`, `aciklama-a.md`, `aciklama-b.md` | yalnız `utm_content`: `s3-a` → `s3b-a`, `s3-b` → `s3b-b` (adresler + UTM tablosu; A 6, B 7 satır); `aciklama.md` = A (`cmp` eşit) |
| kök `kapak-b.png`, `kapak-c.png`, `hikaye.png`, `hikaye-a.png`, `hikaye-b.png` | `~/Silinecekler/2026-11-15-kol-b/02-04-ydt-temel-s3b/grup-turevleri/` (grup türevi) |
| kol a `surumler.json` | yalnız `s3` satırına `varyant: {"grup": "s3", "kol": "a", "degisken": "kanca", "deger": "kopru"}` (`git diff` 7 ekleme, 1 satır virgül) |

Kol b `varyant`: `{"grup": "s3", "kol": "b", "degisken": "kanca", "deger": "yanlis-cumle"}`. İki JSON `json.load` ile ayrıştı; `deger` `[a-z0-9-]`.
Kol a'nın değiştirilen kopyaları (kapak A, sahne 01 `k/`, `proje-ka*`): `~/Silinecekler/2026-11-15-kol-b/02-04-ydt-temel-s3b/kol-a-kopyasi/`.

## 2. Ses tablosu (`sentez.wav.rapor.json`; tohum hepsi 0; önbellek `~/.local/share/elevenlabs-onbellek`; el.py rc 0, kapı önbelleği 8 / 9)

| Kol b cümle | Konuşan (ses …son 4) | Metin | Kaynak | Kol a dosyası → sha256 | Kol b dosyası → sha256 | Whisper (parça) |
|---|---|---|---|---|---|---|
| 1 | öğretmen …4fwc | Hata nerede? | yeni | — | `cumle-1.wav` `142d55e5bbd0` | 1,00 (duyulan `Hata nerede?`) |
| 2 | öğretmen …4fwc | The train to Izmir leaves at seven p.m. today. · I am going to the movie theater tonight. | önbellek | `cumle-1.wav` `af9343e6d690` | `cumle-2.wav` `af9343e6d690` | 0,92 · 1,00 |
| 3 | öğrenci …9gjY | Hocam, tren de plana göre kalkmıyor mu? Neden -ing yok? | önbellek | `cumle-2.wav` `a65bb1e43a13` | `cumle-3.wav` `a65bb1e43a13` | 0,98 |
| 4 | öğretmen …4fwc | Planı bir kişi yapar. Tren tarifeye uyar: geniş zaman. | önbellek | `cumle-3.wav` `d71bacefe538` | `cumle-4.wav` `d71bacefe538` | 1,00 |
| 5 | öğretmen …4fwc | Bu, üç farktan yalnız biri. · Bir arkadaşına gönder; o da karıştırıyor. | önbellek | `cumle-4.wav` `9b7e70ce36dc` | `cumle-5.wav` `9b7e70ce36dc` | 1,00 · 1,00 |
| 6 | öğrenci …9gjY | Bu sadece başlangıç. · Dersin tamamı YDS Publishing YouTube kanalında. | önbellek | `cumle-5.wav` `6a9927c66d00` | `cumle-6.wav` `6a9927c66d00` | 1,00 · 1,00 (ses metni `YeDeSe`, duyulan `YEDESE Publishing`) |

Ön benzetim (ağsız, `el.py` anahtar + kayıtlı duyulan): kanca dışında 8 / 8 parça önbellekte, en düşük 0,92 ≥ 0,85 → ikinci tohum (yeni sentez) tetiklenmez; sonuç benzetimle aynı.
Sözcük zamanı: kanca `Hata` 0,41–0,81 · `nerede?` 0,93–1,45. Kol b cümle 2–6 sözcükleri ve altyazı parçaları kol a + 1,000 sn (56 / 56 sözcük, 8 / 8 parça; en büyük sapma 2e-15).

## 3. Süreler (sn)

| Öğe | Kol a | Kol b |
|---|---|---|
| Toplam | 28,31 | 29,31 |
| Cümle başları | 1,00 · 7,00 · 11,51 · 16,54 · 21,88 | 0,41 (kanca) · 2,00 · 8,00 · 12,51 · 17,54 · 22,88 |
| Sahne 01 kanca | 0,00–3,00 (102 kare) | 0,00–4,00 (132 kare) |
| Sahne 02 değer | 3,00–15,99 (402) | 4,00–16,99 (402) |
| Sahne 08 kaydet | 15,99–21,33 (172) | 16,99–22,33 (172) |
| Sahne 03 çağrı | 21,33–28,31 (239) | 22,33–29,31 (239) |
| Kapak A karesi | 1,97 (kare 59) | 1,80 (kare 54) |

Kol b sahne 01 olayları (küresel = yerel sn): altçizgi 0,30–0,80 · satır 1 0,41–0,71 · yanlış satır 2 0,93–1,33 · `?` 1,40–1,65 (+ nokta 1,70) ·
kapak karesi 1,80 · üstü çizme 2,64–2,84 (`Izmir`), `?` solar · yanlış satır söner 2,90–3,15 · başlık solar 3,00–3,18 · saat + figür solar 3,00–3,30 ·
tren uçuşu ve satır kayması 3,00–3,85 · `leaves` 3,20 · `at` 3,56 · `7` 3,80 · konu adı 3,62–3,85 · kart çerçevesi 3,62–3,90 · son hal 3,92–4,00.

## 4. Tek değişken kanıtı (`diff -rq 02-04-ydt-temel-s3 02-04-ydt-temel-s3b`, 90 satır; `diff-rq.txt`, `siniflama.txt`)

| Sınıf | Satır | İçerik |
|---|---|---|
| değişen sahne `01-hyperframes-kapak` | 37 | `uret.py`, `zamanlar.json`, `olay.py`, `olaylar.json`, `calistir.sh`, `devir.json`, `proje/index.html`, `proje-ka*/` (index + `.hyperframes`), `k/` (kol a kareleri Silinecekler'de, kol b kareleri yeni), `SPEC.md`, `RAPOR.md`, `__pycache__` |
| senaryo | 1 | `ortak/anlatim/senaryo.json` |
| yeni ses | 11 | `cumle-1…5.wav` (ad kayması: içerik kol a N ↔ kol b N+1 sha256 aynı, §2), `cumle-6.wav` (yalnız kol b), `sentez.wav` (+ rapor), `anlatim.wav`, `anlatim.m4a` (+ imza) |
| zaman ve söz türevleri | 9 | `zaman.json`, `sozcukler.json`, `sureler.json`, `baslar.json`, `altyazi.json`, `METIN.md`, `sozcuk_uret.py`, `zaman_uret.py`, `metin_uret.py` |
| `surumler.json` | 1 | kol b satırları + `varyant` |
| açıklamada `utm_content` | 3 | `aciklama.md`, `aciklama-a.md`, `aciklama-b.md` |
| kapak A (kanca) | 2 | `kapak-a.png`, `kapak.png` |
| çıkarılan grup türevleri | 5 | `Only in` kol a: `kapak-b.png`, `kapak-c.png`, `hikaye.png`, `hikaye-a.png`, `hikaye-b.png` |
| `uretim-tutanagi/` | 21 | iki kolun ayrı tutanağı (bu rapor dahil) |
| **Beklenmeyen** | **0** | — |

Sahne 02, 08, 03, 04–07 ve `ortak/` (anlatım dışı) satır vermedi: bayt aynı. Satırları düzenli ifade kurallarıyla bir betik sınıfladı; kural dışı satır 0.
Değişmeyen sahnelerin yerel zamanı korunur: `uret.py` yerel = küresel − `t_bas`, kol b'de iki taraf da +1,00 kayar.

## 5. Kapı ve kareler

```
node araclar/cakisma-kapisi.mjs 02-04-ydt-temel-s3b --port 41333 --sunucu 41022   → çıkış 0
01-hyperframes-kapak | çakışma yok (17 örnek, 5338 kutu)
02-hyperframes-ornek | çakışma yok (53 örnek, 27834 kutu)
08-hyperframes-kaydet | çakışma yok (23 örnek, 4940 kutu)
03-hyperframes-cta | çakışma yok (29 örnek, 5038 kutu)
```

| Kare (sn) | Gözle bakış (Read; açık tema) |
|---|---|
| 0,00 (ilk) | kanal katmanı, rozet, `HATA`, hap `NEREDE?` (x 72–948), saat + tren, figür; kart yeri boş; 0–280 ve 1570–1920 boş |
| 0,60 · 1,20 | satır 1 ve yanlış satır 2 kırpmayla yazılıyor; altyazı `Hata nerede?` tek satır |
| 1,80 (kapak karesi) | `The train to İzmir ?` / `is leave at 7 pm today.`; `?` satır 2'ye ve hapa değmez; taşma yok |
| 2,80 | `is leave` üstü çizili, `?` sönüyor; altyazı cümle 2 |
| 3,10 | başlık ve yanlış satır soluk, tren kalkıyor |
| 3,45 | satırlar yükseliyor, `leaves` yazılıyor, tren köşeye gidiyor; binme yok |
| 3,97 (son) | künye + rozet, kart, `leaves at 7`, tren köşede: kol a 2,97 karesiyle tam kare piksel farkı 0 (devir dikişsiz) |
| koyu 1,80 · `kapak-a.png` · `kapak-a-koyu.png` | iki tema okunur; kapakta altyazı yok, kanal var |

Kanal + künye bandı (y 280–350) kol a ile piksel aynı: 0 ↔ 0, 1,5 ↔ 1,8, 2,97 ↔ 3,97, `kapak-a.png` (4 / 4). Kareler `sahneler/01-hyperframes-kapak/k/`
ve `~/qa-kare/02-04-ydt-temel-s3b/01-hyperframes-kapak/`. Emoji 0 (senaryo, sahne 01 HTML, `surumler.json`, açıklamalar); kırmızı, yeşil, ✗ yok. mp4 0.
Yüzey taraması (`Tam ders`, `dakika`, `dk`: senaryo, altyazı, METIN, açıklama, sahne HTML, `ortak/*.js`, `surumler.json`) boş.

## 6. Açık noktalar

1. **Süre +1,00 sn (karışık değişken):** 29,31 ≤ 35 ama hedef 22–26 aşılır (kol a da 28,31). Sesli her kanca kol a'nın kanca sesi olan değer cümlesinin önüne girer; ortalama izlenen yüzde kendiliğinden kol a lehine eğilir (sözleşme §6 okumasında ayrılmalı).
2. **Whisper 2·1 = 0,92:** wav kol a ile aynı (kol a 1,00). Sebep `el.py`: yeni TR kanca parçasının `kontrol()`'ü `DIL`'i `tr` yapar; önbellek EN parçasında `kontrol()` koşmaz, `7` Türkçe sayıya çevrilir. Eşik 0,90 geçti; düzeltme `D/araclar/iki-dilli/el.py` işidir (yazma alanı dışı).
3. **Kulak denetimi yok:** kanca 2 sözcük, Whisper 1,00; kısa sözde Whisper yanılabilir (taslak §5). Nadir dinlemeli.
4. **İlk söz iki kolda farklı (1,00 → 0,41):** `sozlesme.md` s1b satırı "ilk söz iki kolda aynı" der; aynı tutulursa toplam 29,90 olur ve kanca 4 sn'yi aşar. Kanca bölgesindedir (taslak açık nokta 7). Şef kararı.
5. **Figür:** taslak "işaret eden figür kol a kapak B" der; kapak B'de kit figürü yok (karakter görseli). Kadro gövdesi sabit (`ShirtPantsWB`) → kol a figürü 250 px, yatay aynalı (el trene dönük), işaret pozu yok, bilet yok.
6. **Kapak karesinde 4 yazı satırı** (başlık 2 + kart 2); klişe "≤ 3 satır". Hap `NEREDE?` B 190'da 877 px (x 72–948). Kol b A kapağı grubun kapak B'sine (`NEDEN -ING` / `YOK?`, `?`, tren) yakın. Jüri bakacak.
7. **Değişmeyen `08`/`03` `uret.py` cümle numarasını sabit okur (4, 5):** kol b'de cümleler +1 kaydı; bu sahneler kol b'de yeniden koşturulursa yanlış cümleyi okur. Bayt aynılığı için dokunulmadı; yeniden üretim gerekirse 5 / 6 yapılır.
8. **senaryo.json üst bilgi:** `meta.kimlik` (`02-04-ydt-temel-s3`), `meta.kod` (`…-S3`) ve `zaman.giris` (`sure 3`, `ilkSoz 1`) kol a değerinde kaldı (istem: yalnız taslaktaki değişiklik). `BRIEF-S3.md` kol a planını anlatır.
9. **`zaman.json` `hikaye` / `duragan`:** `zaman_uret.py` kol a girdilerini yazar (04–07 sahne klasörleri bayt aynı); çıktı PNG'leri gruba ait olduğu için kol b kökünde yok.
10. **Açıklama üst bilgisi** `s3-aciklama-a/b` sürüm kimliğini taşır (satır 4); istem "YALNIZ `utm_content`" dediği için değişmedi.
11. **Rozet `YDT · BASIC`:** standart §9 "ilk dokunuşta düzelt" der; tek değişken için kol b'de değişmedi, iki kolda birlikte düzeltilmeli. Kol a kendi `ortak/` bağlarını hâlâ taşır (kol a'ya dokunulmadı).
12. **`calistir.sh` zinciri:** `uret.py && olay.py` assert'te `set -e` ile durmaz (kol a ile aynı); ilk denemede assert sonrası eski `index.html`'e tema uygulandı, düzeltmeden sonra yeniden üretildi.
13. **Jüri koşmadı:** D-0338 teslim kapısı için dil + görsel jüri başka modelle koşmalı. Kovan kaydı yazılmadı (yazma alanı paket). Sözleşme kancası için `K/.claude/docs/sozlesme.md` dosyasına 1 satır eklendi.
14. **Kol a `surumler.json` commit'i:** bu işin eklediği `varyant` satırı (7 ekleme), aynı worktree'deki paralel bir oturumun `e51b486` commit'ine girdi ("chore(huni): kol b paketleri (s1b, s2b) …", 15.11 23:3x). Bu iş commit atmadı; kol b paketi (`??`) ve `sozlesme.md` satırı commit'siz.
