# KBC-0202S1 raporu — simple-present-temel-s1b (A/B kol b) · değişken `kanca` · 15.11.2026

| Ölçüm | Değer |
|---|---|
| Değer (kol a → kol b) | `kopru` → `yanlis-cumle` |
| Toplam süre | 24,00 → **24,33 sn** (`anlatim.m4a` ffprobe 24.330000; hedef 22–26, sınır 35) |
| Yeni sentezlenen | 1 cümle (2 parça, 43 karakter, ≈ 0,21 TL); cümle 2–4 önbellekten (8 / 10 parça kapı önbelleği) |
| Whisper en düşük | 1,00 (10 / 10 parça; eşik 0,90) |
| İlk söz | 1,00 sn |
| `diff -rq` | 82 satır: 81 beklenen sınıf · 1 sınıf dışı (`ortak/kunye.js` yol, açık nokta 1) |
| Çakışma kapısı (paket, 4 sahne) | çıkış 0 · 0 uyarı |
| Üretici model | Claude Opus 5.5 (`claude-opus-5-5`), tek oturum, alt ajan yok · jüri farklı modelle koşmalı |
| mp4 | yok (`find -name '*.mp4'` → 0) |

## 1. Kopya (adım 1)

- Yöntem: `cp -a --dereference` (kol a kökündeki her öğe, `uretim-tutanagi/` hariç). Kol a'nın 4 bağı (`ortak/cizim`, `font`, `logo`, `hf_tema.py` →
  `../../present-continuous/ortak/`) kol b'de gerçek dosya; kol b'de bağ 0.
- Kopya anında dosya sayısı: kol a 413 (bağ çözülmüş, `find -L`) · kol b 413. Git dışı varlık 215 (svg 90, png 64, woff2 10, pyc 10, js 8,
  css 7, wav 6 …): sha256 215 / 215 eşit.
- Grup türevleri çıkarıldıktan sonra kol b 293 dosya (tutanak hariç).

## 2. Değişen dosyalar

| Dosya | Değişiklik |
|---|---|
| `ortak/anlatim/senaryo.json` | cümle 1 → EN `My brother go to school by bus.` + TR `Hata nerede?`; `giris.satir1/2` ve `meta.kapak` → `MY BROTHER` / `GO.`, `canAlici` = ana ders `canAlici[3]` (kapak-taslak §4). Kadro, sesler, cümle 2–4 aynı |
| `ortak/anlatim/` ses zinciri | `cumle-1.wav` (yeni), `sentez.wav` + rapor, `sureler`, `sozcukler`, `baslar`, `anlatim.wav/.m4a/.imza`, `altyazi.json`, `METIN.md` |
| `ortak/anlatim/zaman_uret.py` | `hikaye` / `duragan` alanları çıktı (grup türevleri kol a'da; açık nokta 2) |
| `zaman.json` | 02 3,00–14,96 (371 kare) · 03 14,96–18,07 · 04 18,07–24,33; `hikaye`/`duragan` yok |
| `ortak/kunye.js` | `KOK` → `/projeler/simple-present-temel-s1b/ortak` (açık nokta 1) |
| `sahneler/01-hyperframes-kanca/` | `uret.py`, `olay.py`, `zamanlar.json`, `devir.json`, `proje/`, `proje-ka/`, `k/` kareleri, SPEC/RAPOR başına kol b notu |
| `sahneler/02-paperjs-deger/` | `sahne-02.js`, `kalem-paper.js` + `sayfa.html` (içe aktarım yolu), `calistir.sh` (N 371, paket, Silinecekler yolu), `k/`, SPEC/RAPOR notu |
| `sahneler/03-…`, `04-…/zamanlar.json` | küresel sn +0,33 (uret.py kaydı). `proje/` + `olaylar.json` kol b zamanıyla yeniden üretildi: kol a ile bayt aynı |
| `kapak-a.png` = `kapak.png` | kol b kanca karesi (md5 `c6c12ea7…`; kol a `c0527f63…`); koyu `sahneler/01-…/k/koyu/kapak-a-koyu.png` (`ad19e88e…`) |
| `aciklama-a.md`, `aciklama-b.md`, `aciklama.md` | yalnız `utm_content` `s1-a` → `s1b-a`, `s1-b` → `s1b-b` (5 bağ + tablo satırı / dosya) |
| `surumler.json` | `s1b` (ad `S1b Shorts (24,33 sn)`, önizleme `/p/simple-present-temel-s1b/onizle.html`, `varyant` b) · `s1b-kapak-a` · `s1b-aciklama-a/b`; kapak B/C, hikâye A/B satırı yok |
| kol a `surumler.json` | yalnız `s1` satırına `varyant {"grup":"s1","kol":"a","degisken":"kanca","deger":"kopru"}` (git diff: 1 satır → 7 satır) |
| Silinecekler | `~/Silinecekler/2026-11-15-kol-b/simple-present-temel-s1b/` (`LISTE.md`): grup türevleri (5 png + sahne 05–08), kol a kapak A kopyaları, eski `proje-ka`, 03/04 deneme ve özgün kopyaları |

## 3. Ses (adım 3)

`bash araclar/ses-sunucu.sh simple-present-temel-s1b` (el.py, eleven_v4, `HIZ_EN` 0,9, faster-whisper large-v3-turbo int8). Önbellek anahtarı
`[ses_metni, dil, önceki, sonraki, ses, model, tohum, hız]`; önceki/sonraki yalnız aynı cümlenin parçaları → cümle 1 değişimi 2–4'ü etkilemez.

| Cümle | Parça (söylenen) | Ses | Kaynak | `cumle-N.wav` sha256 a / b | Whisper duyulan | Benz. |
|---|---|---|---|---|---|---|
| 1 | EN `My brother go to school by bus.` | öğretmen `…xC4fwc` | **yeni** (tohum 0) | `e9fa0350…` / `9a113bfd…` | `My brother go to school by bus.` | 1,00 |
| 1 | TR `Hata nerede?` | öğretmen | **yeni** (tohum 0) | (cümle 1 dosyası) | `Hata nerede?` | 1,00 |
| 2 | 5 parça (`My brother goes …` · `He, she, it` · `ile fiile s gelir.` · `I, you, we, they` · `ile gelmez.`) | öğretmen | önbellek | `bb9402db…` / `bb9402db…` | 5 × birebir | 1,00 |
| 3 | TR `Sınavdan önce lazım olacak. Kaydet.` | öğretmen | önbellek | `9cb210d9…` / `9cb210d9…` | birebir | 1,00 |
| 4 | TR `Gerisi bizde.` · `Dersin tamamı YDS Publishing YouTube kanalında.` (ses metni `YeDeSe`, sözlükten) | öğrenci `…M29gjY` | önbellek | `dd50c6bc…` / `dd50c6bc…` | `… YEDESE Publishing …` | 1,00 |

Kasıtlı yanlış: Whisper `go` yazdı (dilbilgisini `goes`'a düzeltmedi; sözcük hizası `go` 1,56–1,64). Kulak kararı açık (açık nokta 4).

## 4. Süreler (kol a ↔ kol b, sn)

| Öğe | Kol a | Kol b | Fark |
|---|---|---|---|
| Cümle 1 (kanca) | 1,00–4,12 | 1,00–4,45 | +0,33 |
| Cümle 2 (değer) | 4,67–14,63 | 5,00–14,96 | kayma +0,33, süre aynı (9,96) |
| Cümle 3 (kaydet) | 15,18–17,74 | 15,51–18,07 | kayma +0,33 |
| Cümle 4 (çağrı, öğrenci) | 18,29–23,00 | 18,62–23,33 | kayma +0,33 |
| 01 kanca | 0,00–3,00 (102 kare) | 0,00–3,00 (102) | 0 |
| 02 değer | 3,00–14,63 (361) | 3,00–14,96 (371) | +10 kare (kanca kuyruğu 1,67 → 2,00 sn) |
| 03 kaydet | 14,63–17,74 (105) | 14,96–18,07 (105) | süre aynı |
| 04 çağrı | 17,74–24,00 (218) | 18,07–24,33 (218) | süre aynı |
| **Toplam** | **24,00** | **24,33** | **+0,33** (taslak tahmini 24,49) |

Kol b sözcük çapaları: `My` 1,00 · `brother` 1,24 · `go` 1,56 · `to` 1,72 · `school` 1,88 · `by` 2,28 · `bus.` 2,52–3,16 · `Hata` 3,41 · `nerede?` 3,81–4,45.

## 5. Değişen sahneler (adım 5)

**01 kanca (HyperFrames, 0,00–3,00).** Kapak düzeni, figür + otobüs, zemin, rozet, kanal katmanı, uçuş ve grup küçülmesi kol a ile aynı.
- Başlık `MY BROTHER` (Fredoka 700, B 147, x 60,7–959,3, taban 574,9) / `GO.` (hapsız, sola hizalı, taban 743,9; zemin konturu 12).
- Kırmızı kalem ✗ (iki darbe, SVG yol, `stroke="#e0473b"` → hf_tema `--kirmizi`; x ≈ 810–930): 0,30–0,52 ve 0,58–0,80. Kapak karesi 0,90.
- Uçuş 1,90–2,45: satır 1 → `Simple`, satır 2 (GO. + ✗) → `Present`; ✗ başlıkla söner. `ucus_ayrik` 10 → 14 (açık nokta 5).
- 2,45: yanlış cümle kartı (kalem kenarlı kutu = sahne 02 `kutuHazir(70, 630, 880, 220)`, ikincil 4 px; y 620–860) girer (0,40 sn);
  yazı `My brother go` / `to school by bus.` (Fredoka 700 72, x 110, taban 712 / 804) soldan kırpmayla 2,45–2,90. `bus.` 2,788'de
  görünür (çapa 2,52; ekran sesten önce değil; `uret.py` assert). Altyazı + karaoke kol a kalıbı.
- `olaylar.json`: 4 olay (kare 9 ✗, 57 uçuş, 74 kırpma, 74 kart). `uret.py` denetimleri (7 madde + kart ve ✗ maddeleri) geçti.

**02 değer (Paper.js, 3,00–14,96).** Kare 0 = sahne 01 son hâli (yanlış kart, küçük figür + otobüs).
- `nerede?` (kare 24): satır 1'in sağ boşluğunda kırmızı kalem ✗ (x 728–792); kare 44–54 kanca satırı 260 px aşağı kayar (kart + ✗).
- Değer kartı kutusu kare 54'ten, değer cümlesi karaoke ve otobüs çizimi kol a ile aynı (kayma +0,33).
- Kanca izi 1: cümledeki `goes` uçuşsuz, kol a ile aynı karede yazılır (kare 80). Yanlış kart kare 71–80'de söner; `go` sözcüğü
  sönmez.
- Kanca izi 2: kare 80'de `go` sözcüğü soluk go kartına devreder (aynı yer, aynı 72 px glif); kare 80–92 çerçeve belirir, kart
  sağ kenara (842, 949) gider; ölçek 0,6, saydamlık 0,4 (kol a ile aynı son hâl). ✗ kare 71–79'da söner.
- Kanca izi 3: soluk Caveat `Kardeşim gider:` (x 60, taban 560, ikincil) `goes` bitince (kare 84) belirir, sahne sonuna dek kalır; söylenmez.
- Kare 92'den sonrası (ok `= he`, çipler, `go-es`, satır B, `s` yuvası kırmızı) kol a ile aynı kod.

**03 kaydet, 04 çağrı:** `proje/` bayt aynı (kol b zamanıyla yeniden üretilip karşılaştırıldı).

## 6. `diff -rq` sınıflaması (adım 7)

Komut: `diff -rq K/projeler/simple-present-temel-s1 K/projeler/simple-present-temel-s1b` (bu rapor yazıldıktan sonra 82 satır).

| Sınıf | Satır | Dosyalar |
|---|---|---|
| Değişen sahne klasörü 01 / 02 | 37 | `01/{uret.py, olay.py, olaylar.json, zamanlar.json, devir.json, SPEC.md, RAPOR.md, proje/index.html, proje-ka/…, __pycache__, k/…}` · `02/{sahne-02.js, kalem-paper.js, sayfa.html, calistir.sh, SPEC.md, RAPOR.md, k/…}` |
| Senaryo ve zaman türevleri | 14 | `senaryo.json` · `altyazi.json`, `anlatim.m4a`, `.imza`, `anlatim.wav`, `baslar.json`, `METIN.md`, `sentez.wav`, `sentez.wav.rapor.json`, `sozcukler.json`, `sureler.json` · `zaman.json` · `03/zamanlar.json`, `04/zamanlar.json` (küresel sn) |
| Yeni ses | 1 | `cumle-1.wav` |
| Grup türevi çıkarımı | 10 | yalnız kol a: `kapak-b.png`, `kapak-c.png`, `hikaye.png`, `hikaye-a.png`, `hikaye-b.png`, `sahneler/05`–`08` · `zaman_uret.py` (`hikaye`/`duragan` çıktısı) |
| Kapak A (kanca karesi) | 2 | `kapak-a.png`, `kapak.png` |
| Açıklama utm | 3 | `aciklama-a.md`, `aciklama-b.md`, `aciklama.md` |
| `surumler.json` | 1 | kol b satırları + `varyant` |
| `uretim-tutanagi/` | 13 | kol b'nin kendi tutanağı (BK taslakları, `kol-b.json`, `ses-sentez.log`, bu rapor) · kol a tutanakları yalnız kol a'da |
| **Sınıf dışı** | **1** | `ortak/kunye.js` (`KOK` yolu; açık nokta 1) |

Değişmeyen cümle sesi (2–4) sha256 aynı · değer cümlesi, kanal katmanı, çekirdek cümle, ses kadrosu iki kolda aynı (AB-3) ·
03/04 `proje/`, `ortak/{cizim, font, logo, kapak, kalem-canvas.js, tema.sh, tema_damga.py, hf_tema.py}`, `BRIEF-S1.md`, `gorevler.json`,
`yorumlar.json`, `harita-konum.json` farksız.

## 7. Kapı ve kareler (adım 8)

```
$ node araclar/cakisma-kapisi.mjs simple-present-temel-s1b --port 41333 --sunucu 41022   → çıkış 0
01-hyperframes-kanca | çakışma yok (13 örnek, 6386 kutu)
02-paperjs-deger | çakışma yok (49 örnek, 2019 kutu)
03-hyperframes-kaydet | çakışma yok (14 örnek, 1547 kutu)
04-hyperframes-cagri | çakışma yok (26 örnek, 3880 kutu)
```
QA: `bash araclar/qa-yerel.sh simple-present-temel-s1b 01-hyperframes-kanca 0.00,0.55,0.90,2.20,2.65,2.95 2.65 --hazirla` (çıkış 0) ·
`… 02-paperjs-deger 3.05,4.25,4.62,5.50,5.80,6.20,8.80,14.90 4.25 --hazirla` (çıkış 0). Kareler `~/qa-kare/simple-present-temel-s1b/` ve sahne `k/`.

| Kare | Gördüğüm | Bulgu |
|---|---|---|
| 01: 0 · 0,55 · 0,90 | kapak; ✗ ilk darbe yarıda; ✗ tam, altyazı yok | taşma, çakışma yok |
| 01: 2,20 · 2,65 · 2,95 (+ koyu 2,65) | uçuş (başlıklar küçülür, grup sağ üste); kart yazısı yarı açık; son hâl | 0–280 ve 1570–1920 boş; x 960+ boş |
| Kapak A açık + koyu (t 0,90) | `MY BROTHER` / `GO.` + ✗, figür + otobüs, rozet, kanal | altyazı yok; iki temada okunur |
| 02: 3,05 · 4,25 (+ koyu) · 4,62 | dikiş karesi 01 ile eş; ✗ satır 1 sağında; kayış | — |
| 02: 5,50 · 5,80 · 6,20 | yanlış kart söner, `go` koyu kalır; go kartı yolda; soluk `Kardeşim gider:` | örtüşme yok |
| 02: 8,80 · 14,90 | `= he`, çipler; son hâl (go-es, satır B, `go` kartı + kırmızı `s`) | kol a son hâliyle aynı düzen |

Kanal katmanı mürekkep kutusu (y 270–360 bandı, 7 kare): HyperFrames x 61–595, Paper x 61–598, y 296–339; kapak A aynı. Kol a karelerinde de
aynı değerler (3 px HF/Paper farkı kol a'dan gelir; iki kolda aynı). Metin taraması (`tam[ ]ders|dak[i]ka`): ses, ekran, açıklama, kapak ve
`ortak/*.js` temiz; yalnız iç `SPEC.md`/`RAPOR.md` yasak alıntısı (kol a ile aynı). Emoji yok; ✗ kalem yolu.

## 8. Açık noktalar

1. **`ortak/kunye.js` sınıf dışı fark.** Sahne 02 (değişen sahne) sözcük zamanı ve altyazıyı `KOK` üzerinden okur. Kol a yolunda kalsaydı kol b
   önizlemesi kol a'nın zamanını ve altyazısını oynatırdı. Değişiklik yalnız `KOK` satırı (1 satır). Kardeş paket s2b'de sahne 02
   değişmediği için `KOK` kol a'da kaldı (sözleşme satırı); bu pakette değişmesi zorunlu.
2. **`zaman_uret.py`** `hikaye`/`duragan` alanlarını artık yazmaz (hedef klasörler kol b'de yok). Araçlar (`cakisma-kapisi`) yalnız `sahneler[]`
   okur; kayıt/editör bu alanları okuyorsa kol b için grup türevini kol a'dan almalı.
3. **Açıklama 4. satırı** `Sürüm: A (`s1-aciklama-a`)` kaldı ("yalnız utm_content" kuralı); `surumler.json` kimliği `s1b-aciklama-a`. Şef kararı.
4. **Kulak kararı (EK-11).** Whisper `My brother go …` duydu (1,00); dilbilgisi düzeltmesi yok. `go` / `goes` Nadir kulağıyla doğrulanmadı.
5. **`ucus_ayrik` 10 → 14** (yalnız kol b sahne 01). Satır 2 kutusu (GO. + ✗, 869 px) uçuşta 2,267 sn'de rozete 6 px pay içinde değiyordu;
   kol a'da hap 0 px ile sınırdaydı. Uçuş hareketi kanca karesinin parçası; başka zaman değeri değişmedi.
6. **Kanca 0–4,45 sn** (standart 0–4 sn, HV-12; kol a 4,12). Süre farkı +0,33 kanca değişkeninin sonucu.
7. **Değişmeyen kol a belgeleri:** `BRIEF-S1.md` ve `senaryo.json` `meta.kimlik` (`02-02-ydt-temel-s1`) kol a'yı anlatır; tek değişken için dokunulmadı.
8. **Jüri bakacak:** ✗'in küçük resimde görünürlüğü (1/6 ölçekte ≈ 20 px); söylenmeyen soluk `Kardeşim gider:`; kapakta kasıtlı yanlış
   İngilizce (✗ ile işaretli); rozet `YDT · BASIC` iki kolda aynı kaldı (standart §9 düzeltmesi iki kola birlikte uygulanmalı).
9. **Platform kapağı** (BK açık 6): Shorts kapağı B ya da C seçilirse iki kolda aynı seçilmeli.
10. Kopya `cp -a --dereference` ile yapıldı; kardeş oturum `-L` bayrağının kopya kapısınca bloklandığını yazdı, uzun biçim bloklanmadı.
