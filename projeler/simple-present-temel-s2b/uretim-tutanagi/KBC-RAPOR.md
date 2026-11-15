# KBC-RAPOR — simple-present-temel-s2b (A/B kol b, değişken `kapanis`) · 15.11.2026 (istem KBC-0202S2)

| Ölçüm | Kol a (`simple-present-temel-s2`) | Kol b (`simple-present-temel-s2b`) |
|---|---|---|
| Değer (`varyant.deger`) | `kaydet` (`Bu kuralı kaybetme. Kaydet.` · `Bitmedi, gel.`) | `ekran-goruntusu` (`Ekran görüntüsü al, sınav günü bak.` · `Konu burada bitmiyor.`) |
| Toplam süre | 25,73 sn | 25,73 sn (`anlatim.m4a` ffprobe 25.730000; taslak tahmini 26,29) |
| Yeni sentez | — | 2 cümle (3, 4) · 4 parça · 149 karakter (≈ 0,73 TL) |
| Whisper en düşük | 1,00 | 0,92 (parça 2·3, önbellek wav'ı kol a ile aynı; açık nokta 2) |
| `diff -rq` satırı | — | 70 (bu rapor dahil); beklenmeyen 0 |
| Çakışma kapısı | — | çıkış 0 (4 sahne, çakışma yok) |
| Üretici model | — | Claude Opus 5.5 (`claude-opus-5-5`); jüri başka modelle koşmalı (juri-olcutleri §1e) |

## 1. Değişen dosyalar (kol b)

| Dosya | Değişiklik |
|---|---|
| paket (tamamı) | kol a'nın `cp -a` kopyası, `uretim-tutanagi/` hariç; 402 ↔ 402 dosya; git dışı 91 varlık sha256 eşit (`kopya-denetim.txt`) |
| `ortak/{cizim,font,logo,hf_tema.py}`, `ortak/logo/yds-publishing-koyu-zemin.svg` | simge bağı → gerçek kopya (bağ Silinecekler'de); paket içinde bağ 0 |
| `ortak/anlatim/senaryo.json` | cümle 3 parça 2 ve cümle 4 parça 1 (+ iki `metin` alanı); kadro, sesler, öteki cümleler aynı |
| `ortak/anlatim/` türevleri | `sentez.wav` (+ rapor), `cumle-3.wav`, `cumle-4.wav`, `sozcukler.json`, `sureler.json`, `anlatim.wav`, `anlatim.m4a` (+ imza), `altyazi.json`, `METIN.md`; `baslar.json` ve kök `zaman.json` bayt aynı |
| `sahneler/03-hyperframes-kaydet/` | `uret.py` (çapalar `al,`; yer imi → 4 köşe parantezi, 4 ayrı yol, saat yönünde 0,12 sn × 4, aralık 0,06; `Kaydet` → `Ekran görüntüsü al`), `proje/index.html`, `zamanlar.json`, `olaylar.json`, `k/` |
| `sahneler/04-hyperframes-cagri/` | `uret.py` (giriş `Konu` · `burada` · `bitmiyor.` 3 kinetik adım, Fredoka 700 89 px; 96 px'te 900'ü aşar), `proje/index.html`, `zamanlar.json`, `k/`; `olaylar.json` bayt aynı |
| `surumler.json` | 3 satır: `s2b` (kısa, `varyant`, önizleme `/p/simple-present-temel-s2b/onizle.html`), `s2b-aciklama-a`, `s2b-aciklama-b`; kapak ve hikâye satırları çıktı |
| `aciklama.md`, `aciklama-a.md`, `aciklama-b.md` | yalnız `utm_content` değeri: `s2-a` → `s2b-a`, `s2-b` → `s2b-b` (adreslerde ve UTM tablosunda); `aciklama.md` = A (`cmp` eşit) |
| kök `kapak*.png` (4), `hikaye*.png` (3) | `~/Silinecekler/2026-11-15-kol-b/simple-present-temel-s2b/grup-turevleri/` (grup türevi, yinelenmez) |
| kol a `surumler.json` | yalnız `s2` satırına `varyant: {"grup": "s2", "kol": "a", "degisken": "kapanis", "deger": "kaydet"}` (`git diff` 7 satır ekleme) |

Kol b `varyant`: `{"grup": "s2", "kol": "b", "degisken": "kapanis", "deger": "ekran-goruntusu"}`. İki JSON `json.load` ile ayrıştı; `deger` `[a-z0-9-]`.

## 2. Ses tablosu (`sentez.wav.rapor.json`; tohum hepsi 0; önbellek `~/.local/share/elevenlabs-onbellek`)

| Cümle · parça | Konuşan (ses …son 4) | Metin | Kaynak | Parça wav sha256 | Whisper |
|---|---|---|---|---|---|
| 1·1 | öğretmen …4fwc | Usually görünce hangi zaman? | önbellek (kol a anahtarı) | `b09860c315d7` | 1,00 |
| 2·1 | öğretmen …4fwc | My brother usually goes to school by bus. | önbellek | `d21b2887a2c0` | 1,00 |
| 2·2 | öğretmen …4fwc | Alışkanlık işareti. | önbellek | `2019d4f5a70e` | 1,00 |
| 2·3 | öğretmen …4fwc | Şu an değil, her sabah yedide kalkarım gibi. | önbellek | `454264347e90` | 0,92 |
| 3·1 | öğretmen …4fwc | Usually, always, every day: Simple Present. | yeni (metin aynı, sonraki parça değişti) | `9e7f8c9f1ce5` | 1,00 |
| 3·2 | öğretmen …4fwc | Ekran görüntüsü al, sınav günü bak. | yeni | `a551efeb488f` | 1,00 (duyulan `Ekran görüntüsü al. Sınav günü bak.`) |
| 4·1 | öğrenci …9gjY | Konu burada bitmiyor. | yeni | `76f803a33785` | 1,00 |
| 4·2 | öğrenci …9gjY | Dersin tamamı YDS Publishing YouTube kanalında. | yeni (metin aynı, önceki parça değişti) | `2f2e6595e1ea` | 1,00 (ses metni `YeDeSe`, duyulan `YEDESE Publishing`) |

| Cümle dosyası | Kol a sha256 | Kol b sha256 | Sonuç |
|---|---|---|---|
| `cumle-1.wav` | `3128f4881413` | `3128f4881413` | aynı |
| `cumle-2.wav` | `c102637639ac` | `c102637639ac` | aynı |
| `cumle-3.wav` | `9142f8fe5573` | `3fa5c40623a7` | yeni (değişken) |
| `cumle-4.wav` | `b192db36b66b` | `4201e1dfc0f9` | yeni (değişken) |

İlk söz 1,00 sn (`baslar.json` aynı). Günlük: `ses-sentez.log` (el.py rc 0, kapı önbelleği 4 / 8, sözcük zamanı eksik 0).

## 3. Süreler (sn)

| Öğe | Kol a | Kol b |
|---|---|---|
| Toplam | 25,73 | 25,73 |
| Sahne 01 · 02 | 0,00–3,00 · 3,00–11,87 | aynı |
| Sahne 03 kaydet | 11,87–19,07 (228 kare) | aynı |
| Sahne 04 çağrı | 19,07–25,73 (230 kare) | aynı |
| Parça 3·1 · 3·2 | 4,08 · 2,32 | 4,00 · 2,40 |
| Parça 4·1 · 4·2 | 1,44 · 3,52 | 1,44 · 3,52 |
| Kart sabit (sahne 03) | 15,86–19,07 (3,21) | 15,78–19,07 (3,29) |
| Simge + yazı (sahne 03) | 18,47 · 18,57 (`Kaydet.`) | 17,63 · 17,73 (`al,`) |
| Giriş adımları (sahne 04) | 19,62 · 20,58 | 19,62 · 19,94 · 20,34 |
| `@ydspublishing` · `YouTube` | 22,49 · 23,61 | aynı |

## 4. Tek değişken kanıtı (`diff -rq simple-present-temel-s2 simple-present-temel-s2b`, 70 satır)

| Sınıf | Satır | İçerik |
|---|---|---|
| değişen sahne `03-hyperframes-kaydet` | 14 | `uret.py`, `proje/index.html`, `zamanlar.json`, `olaylar.json`; `k/` 10 satır (kol a karesi Silinecekler'de, kol b karesi yeni) |
| değişen sahne `04-hyperframes-cagri` | 16 | `uret.py`, `proje/index.html`, `zamanlar.json`; `k/` 13 satır |
| senaryo | 1 | `ortak/anlatim/senaryo.json` |
| yeni ses | 7 | `cumle-3.wav`, `cumle-4.wav`, `sentez.wav`, `sentez.wav.rapor.json`, `anlatim.wav`, `anlatim.m4a`, `anlatim.m4a.imza` |
| zaman ve söz türevleri | 4 | `sozcukler.json`, `sureler.json`, `altyazi.json`, `METIN.md` |
| `surumler.json` | 1 | kol b satırları + `varyant` |
| açıklamada `utm_content` | 3 | `aciklama.md`, `aciklama-a.md`, `aciklama-b.md` |
| çıkarılan grup türevleri | 7 | `Only in` kol a: `kapak.png`, `kapak-a/b/c.png`, `hikaye.png`, `hikaye-a/b.png` |
| `uretim-tutanagi/` | 17 | iki kolun ayrı tutanağı (bu rapor dahil) |
| **Beklenmeyen** | **0** | — |

Sahne 01, 02, 05–08 ve `ortak/` (anlatım dışı) satır vermedi: bayt aynı. Satırları düzenli ifade kurallarıyla bir betik sınıfladı; kural dışı satır 0.
Not: kol a `uretim-tutanagi/juri/J2-hukum.md` bu oturumda başka bir oturumdan geldi (git `??`); kol a tutanağıdır, bu işin yazımı değil.

## 5. Kapı ve kareler

```
node araclar/cakisma-kapisi.mjs simple-present-temel-s2b --port 41333 --sunucu 41022   → çıkış 0
01-hyperframes-kanca | çakışma yok (13 örnek, 6133 kutu)
02-paperjs-deger | çakışma yok (37 örnek, 1969 kutu)
03-hyperframes-kaydet | çakışma yok (30 örnek, 3867 kutu)
04-hyperframes-cagri | çakışma yok (28 örnek, 4220 kutu)
```

| Sahne | Açık kareler (küresel sn) | Koyu | Gözle bakış (Read) |
|---|---|---|---|
| 03 | 11,88 (ilk) · 15,50 · 17,70 · 18,30 · 19,05 (son) | 18,30 | taşma yok, çakışma yok; çerçeve 4 köşe + yazı x 144–876, y 960–1060; 17,70'te ilk köşe çiziliyor; altyazı 2 satır (EN parça, kol a ile aynı) |
| 04 | 19,08 (ilk) · 20,10 · 21,40 · 24,20 · 25,70 (video son karesi) | 24,20 | giriş tek satır x 60–954; kapak kartı, hap, `· YouTube` yerinde; koyu temada ana kapak koyu sürümü |

Kareler: `sahneler/0{3,4}-*/k/` ve `~/qa-kare/simple-present-temel-s2b/` (kontak `kontak/03-acik-4.png`, `04-acik-4.png`). Kanal katmanı + künye
bandı (y 280–450) aynı anda kol a karesiyle piksel aynı: 19,00 ↔ 19,05 ve 25,68 ↔ 25,70 (2 / 2). Emoji 0 (sahne 03/04 HTML, senaryo). mp4 0.
Yüzey taraması (`Tam ders`, `dakika`, `dk`: senaryo, altyazı, METIN, açıklama, sahne HTML/JS, `ortak/*.js`, `surumler.json`) boş.

## 6. Açık noktalar

1. **Ses birebirliği (AB-3):** 3·1 (kural özeti) ve 4·2 (çekirdek) metni kol a ile aynı, ama `el.py` anahtarı komşu parçayı içerir; iki parça yeniden sentezlendi. Süre 4,08 → 4,00 ve 3,52 → 3,52. Var olan araçta parça düzeyinde kol a wav'ını alma yolu yok.
2. **Whisper 2·3 = 0,92:** wav kol a ile aynı (kol a raporu 1,00). Sebep `el.py` (D): kapı önbelleği isabetinde `kontrol()` koşmaz, `DIL` genel değişkeni varsayılan `en` kalır; `7'de` İngilizce sayıya çevrilir. Eşik (0,90) geçti. Düzeltme `D/araclar/iki-dilli/el.py` işidir (yazma alanı dışı).
3. **Rozet `YDT · BASIC`:** standart §9 "ilk dokunuşta düzelt" der; tek değişken için kol b'de değişmedi. İki kolda birlikte düzeltilmeli.
4. **Mutlak yol:** değişmeyen sahne 02 (`kalem-paper.js`, `sahne-02.js`, `sayfa.html`) ve `ortak/kunye.js` `KOK` kol a'yı `/projeler/simple-present-temel-s2/` yoluyla yükler. Bayt aynılığı için dokunulmadı; kol a panelde yoksa kol b sahne 02 kırılır. Kol a kendi `ortak/` bağlarını hâlâ taşır (panel bağı reddeder); kol a'ya dokunulmadı.
5. **Açıklama başlık satırları:** kod bloğu dışındaki üst bilgi kol a sürüm kimliğini (`s2-aciklama-a/b`), paket adını ve `Eşleşen kapak: kapak-b.png` satırını taşır; istem "YALNIZ `utm_content`" dediği için değişmedi.
6. **HV-13 okuması:** kol b kaydet sahnesinde yer imi ve `Kaydet` yazısı yok; yerine çerçeve simgesi ve `Ekran görüntüsü al` (değişkenin kendisi, taslak onaylı). Açıklamanın ilk satırı (`Sınav günü bakmak için kaydet.`) gruba ait, değişmedi.
7. **Ölçü yanlılığı (taslak açık nokta 1):** ekran görüntüsü platformun kaydetme sayacına girmez; sözleşme §6 sırasında kaydetme bu değişkende kol b aleyhine eğilir. Şef kararı.
8. **`kol-b.json` `varyant.deger`** taslakta cümle dizesidir; `surumler.json` istemin sözlüğünü (`ekran-goruntusu`) kullanır. Taslak dosyası değişmedi.
9. **Jüri koşmadı:** D-0338 teslim kapısı için görsel + dil jürisi başka modelle koşmalı. Video ilk karesi (0 sn, sahne 01) yeniden çekilmedi: sahne 01 bayt aynı; çekmek değişmeyen klasörün `k/` dizinine yazardı.
10. Kovan kaydı yazılmadı (yazma alanı paket dizini). Sözleşme kancası için `K/.claude/docs/sozlesme.md` dosyasına 1 satır eklendi.
