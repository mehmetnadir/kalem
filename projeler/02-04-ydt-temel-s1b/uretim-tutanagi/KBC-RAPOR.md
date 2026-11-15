# KBC-0204S1 raporu — 02-04-ydt-temel-s1b (A/B kol b, değişken `kanca`) · 15.11.2026

| Ölçüm | Değer |
|---|---|
| Değer | kol a `kopru` → kol b `soru` |
| Yeni kanca | "Bu iki yaşıyorum aynı mı?" (öğretmen `…4fwc`, 2,00 sn, Whisper 1,00) |
| Süre | kol a 31,75 → kol b 27,89 sn (`anlatim.m4a` ffprobe; ≤ 35 ✓, hedef 22–26 ✗) |
| İlk söz | kol a 1,00 → kol b 0,50 sn |
| Yeni sentez | 1 cümle (25 karakter); cümle 2–4 önbellekten, sha256 kol a ile aynı |
| Whisper en düşük | 0,96 (cümle 2 `I am living with my uncle.`, önbellek, kol a ile aynı); yeni cümle 1,00 |
| diff -rq | 96 satır: 77 beklenen · 19 açık (tek neden: sahne 02 baş kırpımı) · sınıfsız 0 |
| Çakışma kapısı | çıkış 0 (1 uyarı, kol a'dan miras; §5) |
| Üretici model | Claude Opus 5.5 (`claude-opus-5-5`); jüri farklı modelle koşmalı (juri-olcutleri §1e) |
| mp4 | yok (0 dosya) |

## 1. Değişen dosyalar

| Dosya | Değişiklik |
|---|---|
| `ortak/anlatim/senaryo.json` | yalnız cümle 1 (`parcalar`, `metin`); kadro, ses kimliği, öteki cümleler aynı |
| `ortak/anlatim/sozcuk_uret.py` | `ILK = 1.00` → `0.50` (taslak §4 ilk söz) |
| `ortak/anlatim/` türevleri | `cumle-1.wav` (yeni), `sentez.wav(.rapor.json)`, `sureler.json`, `sozcukler.json`, `baslar.json`, `altyazi.json`, `METIN.md`, `anlatim.wav/.m4a/.imza`; günlük `uretim-tutanagi/ses-sentez.log` |
| `zaman.json` | 4 sahne yeniden (`zaman_uret.py` değişmedi) |
| `sahneler/01-hyperframes-kapak/` | `uret.py`, `zamanlar.json`, `olay.py`, `olaylar.json`, `calistir.sh`, `devir.json`, `proje/`, `proje-ka/`, `k/`, `RAPOR.md`, `SPEC.md` başı |
| `sahneler/02-paperjs-ornek/` | `sahne-02.js` (yol, `KARE 421`, `T_BAS 2.5`, cümle 1 çapaları ve karaoke kalktı, `yor` kutuları `HAZIR`/sessiz), `kalem-paper.js` + `sayfa.html` (yol), `calistir.sh` (sabitler), `k/`, `RAPOR.md`/`SPEC.md` başı |
| `ortak/kunye.js` | `KOK` → `/projeler/02-04-ydt-temel-s1b/ortak` (sahne 02 kendi sözcük ve altyazısını okur) |
| `kapak-a.png` = `kapak.png` | yeni kanca karesi (t 1,75); koyu `sahneler/01-…/k/koyu/kapak-a-koyu.png` |
| `surumler.json` | 4 satır: `s1b` (`varyant` b/soru), `s1b-kapak-a`, `s1b-aciklama-a`, `s1b-aciklama-b`; kapak B/C ve hikâye satırları çıktı |
| `aciklama.md`, `-a`, `-b` | yalnız `utm_content` (`s1-a` → `s1b-a`, `s1-b` → `s1b-b`; URL'ler ve utm tablosu) |
| kol a `surumler.json` | yalnız `s1` satırına `varyant` (a/kopru); `git diff`: 7 ekleme, 1 satır virgül |
| Taşınan (silme yok) | `~/Silinecekler/2026-11-15-kol-b/02-04-ydt-temel-s1b/`: 5 simge bağı, grup türevleri (kapak-b/c, hikaye-a/b, hikaye.png), kol a QA kareleri ve `proje-ka` |

Kopya denetimi (`kopya-denetim.txt`): kol a 410 dosya (bağlar açık) = kol b 410; simge bağı 0; git dışı 203 varlığın 203'ü aynı sha256.

## 2. Ses

| Cümle | Konuşan | Kaynak | sha256 (a → b) | Whisper (parça) |
|---|---|---|---|---|
| 1 "Bu iki yaşıyorum aynı mı?" | öğretmen | yeni (el.py, 25 karakter) | `35974df2f7f2` → `2f914435214e` | 1,00 |
| 2 "İngilizcede ikisi ayrılır. … şimdiki zaman." | öğretmen | önbellek | `a363311cf849` = | 1,00 · 1,00 · 1,00 · 0,96 · 1,00 |
| 3 "Bu, üç farktan yalnız biri. Sınavdan önce lazım olacak. Kaydet." | öğretmen | önbellek | `0c3ba8612d3b` = | 1,00 · 1,00 |
| 4 "Gerisi bizde. Dersin tamamı YDS Publishing YouTube kanalında." | öğrenci `…9gjY` | önbellek | `dd50c6bcd452` = | 1,00 · 1,00 (duyulan "YEDESE Publishing"; sözlük `YDS` → `YeDeSe`) |

el.py: "kapı önbelleği 9 / 10 parça · 10 / 10 parça kapıdan geçti". Kapı eşiği el.py'de 0,85; bütün parçalar ≥ 0,90 (huni v2 §7.4).

## 3. Süreler (küresel sn; kare = içerik + geçiş)

| Sahne | Kol a | Kol b | Not |
|---|---|---|---|
| 01 kanca | 0,00–3,00 (102) | 0,00–2,50 (87) | kanca sözü 5,36 → 2,00 sn |
| 02 değer | 3,00–19,99 (522) | 2,50–16,13 (421) | baş kırpımı: kol a yerel 0–3,36 sn yok |
| 08 kaydet | 19,99–25,49 (177) | 16,13–21,63 (177) | yerel sözcük ve altyazı zamanları aynı |
| 03 çağrı | 25,49–31,75 (218) | 21,63–27,89 (218) | yerel sözcük ve altyazı zamanları aynı |
| Toplam | 31,75 | 27,89 | −3,86 |

## 4. Tek değişken kanıtı (`diff-siniflama.txt`, satır satır)

| Sınıf | Satır | Durum |
|---|---|---|
| Değişen sahne 01 (kanca; kod, proje, QA kareleri, pyc) | 30 | beklenen |
| Senaryo (cümle 1) | 1 | beklenen |
| Yeni ses (`cumle-1.wav`) | 1 | beklenen |
| Senaryo ve zaman türevleri (`zaman.json`, anlatım türevleri, `sozcuk_uret.py`) | 12 | beklenen |
| `surumler.json` | 1 | beklenen |
| Açıklamada utm | 3 | beklenen |
| Kapak A (`kapak-a.png`, `kapak.png`) | 2 | beklenen |
| Çıkarılan grup türevleri | 5 | beklenen |
| `uretim-tutanagi/` | 22 | beklenen |
| Sahne 02 baş kırpımı (4 kod, 2 belge başı, 12 QA karesi) | 18 | **açık** |
| `ortak/kunye.js` KOK (sahne 02 yolu) | 1 | **açık** |

Değişmeyen: `08-hyperframes-kaydet/`, `03-hyperframes-cta/` (proje dahil bayt bayt), `04`–`07` klasörleri, `BRIEF-S1.md`, `ortak/` (kunye.js dışı).
Sahne 02 içerik eşdeğerliği (kol b t ↔ kol a t + 3,86; fark > 24 düzey piksel): 2,50 ↔ 6,36 altyazı üstü 0 (yalnız altyazı bandı,
söz farkı) · 3,04 ↔ 6,90 0 · 6,00 ↔ 9,86 77 · 10,00 ↔ 13,86 0 · 14,00 ↔ 17,86 236 · 16,24 ↔ 20,10 0 (77 ve 236: 1 karelik yuvarlama).
Kanal katmanı (y 280–350) kol a ↔ kol b: 0. sn 0 piksel · orta en büyük fark 1 düzey (zemin greni) · son kare 0 piksel.
Sahne 01 → 02 ek yeri: satır bandı 5.567 piksel ↔ kol a 01 → 02 ek yeri 5.591 (HF ↔ canvas yazı işlemesi; kanal ve künye sayıları birebir aynı).

## 5. Kapı çıktısı (`kapi-cikti.txt`)

```
node araclar/cakisma-kapisi.mjs 02-04-ydt-temel-s1b --port 41333 --sunucu 41022
01-hyperframes-kapak | çakışma yok (11 örnek, 2674 kutu)
02-paperjs-ornek | 4.50-4.50 sn | -um. × yor çip 1 | kesişim 72x11 px | uyari
08-hyperframes-kaydet | çakışma yok (23 örnek, 2780 kutu)
03-hyperframes-cta | çakışma yok (26 örnek, 3880 kutu)
çıkış kodu: 0
```

Uyarı kol a'dan mirastır: kol a sahne 02 kare kare (`--sikilik 30`) `8.37-8.43 sn | -um. × yor çip 1 | 72x12 px | uyari` verir. Kol a'nın
4/sn ızgarası (3,00 + k/4) bu anı atlar; kol b'ninki (2,50 + k/4) 4,50'de yakalar. Düzeltmek sahne 02 içeriğini değiştirir (ikinci değişken).

QA kareleri (Read ile bakıldı; kontak `kontak-kbc.png`): sahne 01 açık 0 · 0,9 · 1,3 · 1,75 · 2,2 · 2,5, koyu 1,75 · 2,2, kapak A açık + koyu;
sahne 02 açık 2,5 · 3,04 · 6 · 10 · 14 · 16,13, koyu 2,5 · 10; sahne 03 son kare 27,85. Taşma, çakışma, okunmayan yazı yok; 0–280 ve
1570–1920 boş; kanal katmanı her karede aynı yer. Metin taraması: "Tam ders" ve "dakika" yalnız `BRIEF-S1.md` kural cümlesinde (kol a ile aynı iç belge).

## 6. Açık noktalar

1. **Sahne 02 baş kırpımı (19 diff satırı).** `kol-b.json` sahne 02'yi `ayni_sahneler`de tutar; bayt eşitliği olanaksız: `sahne-02.js` kol a yollarını,
   `T_BAS 3.0`/`KARE 522` sabitlerini ve cümle 1 sözcük bekçisini (`Türkçede`) taşır. İçerik cümle 2'den sona kol a ile piksel düzeyinde aynı (§4).
2. **Süre hedefi.** 27,89 sn; hedef 22–26 aşılır (değer cümlesi 13,08 sn, metin değişmez). Kol a'dan 3,86 sn kısa: ortalama izlenen yüzde kol b lehine kayar (BK-RAPOR §e 2).
3. **Başlık boyu 152'ye sabitlendi.** Formül dar `AYNI MI?` ile 161 verir, satır 1'e 5 px kalır (≥ 24 kuralı). Kol a boyu korundu (kapak-taslak §2).
4. **Ekran sözden önce.** `YAŞIYORUM` / `AYNI MI?` 0. karede; "aynı mı" 1,86'da söylenir ve başlık o anda solar. İki Türkçe satır seslendirilmez (`Bu`, `iki` çapası). Jüri bakacak (EK-12).
5. **Kapak karesinde 4 yazı satırı** (başlık 2 + cümle 2; klişe "≤ 3 satır"). Jüri bakacak.
6. **`senaryo.json` `giris` / `meta`** kol a değerlerini taşır (`satir2: "= İKİ ZAMAN"`, `kimlik: 02-04-ydt-temel-s1`); okuyan araç yok; istem "yalnız değişen cümleler" dediği için dokunulmadı.
7. **Açıklama başlık notları** kol a künyesini taşır (`Sürüm: A (s1-aciklama-a)`, `Shorts: …-S1, 31,75 sn`); istem gereği yalnız utm değişti. `surumler.json` satırları `s1b-aciklama-a/b`.
8. **`zaman.json` `hikaye` / `duragan`** grup sahnelerini (04–07) anar; klasörler kol b'de duruyor (kol a ile aynı), PNG türevleri çıkarıldı.
9. **Rozet `YDT · BASIC`** iki kolda aynı kaldı (huni v2 §9 açık işi `YDT · TEMEL`; tek kolda değiştirmek ikinci değişken olur).
10. **Kutu biçimi.** Sahne 01 `yor` kutusu SVG yamuk; sahne 02 Paper kalem darbesi (uçlar biraz yuvarlak). 12 karelik geçişte fark küçük.
11. Sahne 08/03 üretim betiklerinin ilk satır yorumu kol a adını taşır (kod paket göreli; `proje/` bayt bayt aynı kalsın diye dokunulmadı).
