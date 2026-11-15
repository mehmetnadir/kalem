# V2-S1-C raporu — 02-04-ydt-temel-s1 huni v2 çevirisi · 15.11.2026

| Ölçüm | Değer |
|---|---|
| Yedek | `~/Silinecekler/2026-11-15-huni-v2/02-04-ydt-temel-s1/` (`ortak/anlatim/`, `zaman.json`, `surumler.json`, `BRIEF-S1.md`, `aciklama*.md`, 7 PNG; `cp -a`) |
| Ses kapısı (el.py, faster-whisper turbo, eşik 0,85) | 10 / 10 parça; cümle 1 → 1,00 · 2 → 0,96 · 3 → 1,00 · 4 → 1,00 |
| Ses kimliği | cümle 1–3 öğretmen `…4fwc` · cümle 4 öğrenci `…9gjY` (önbellek anahtarı doğrulandı: yalnız `…9gjY` anahtarlı wav var) |
| Marka adı | Whisper "YEDESE Publishing" duydu; kıyas metni (sözlük `YDS` → `YeDeSe`) 1,00; ekran metni "YDS Publishing" ile 0,97 |
| Anlatım | 31,75 sn (`anlatim.m4a` ffprobe 31.750000; imza `a565d944…`); ElevenLabs 125 karakter (≈ 0,61 TL), cümle 1–2 önbellekten |
| Zaman çizelgesi | 01 0,00–3,00 (102) · 02 3,00–19,99 (522) · 08 19,99–25,49 (177) · 03 25,49–31,75 (218); `hikaye` + `duragan[]` (05–07) yerinde |

Değişen cümleler (1 ve 2 aynı): eski cümle 3 "Bu, üç farktan yalnız biri. Tam ders: Simple Present ve Present Continuous. Üç farkın hepsi
dört buçuk dakikada." → cümle 3 (öğretmen) "Bu, üç farktan yalnız biri. Sınavdan önce lazım olacak. Kaydet." + cümle 4 (öğrenci)
"Gerisi bizde. Dersin tamamı YDS Publishing YouTube kanalında." `sesler`/`kadro` ← ana ders `ogrenci` kaydı (kopya).
Yazılanlar: `senaryo.json` · `zaman_uret.py` (2 Edit: 4 sahne, `duragan[]` taşıma) · ses zinciri çıktıları (`ses-sentez-v2.log`) · `zaman.json` ·
`BRIEF-S1.md` (yerleşim §2, kanal tablosu, 4 sahne, kaydet/çağrı satırları) · `aciklama.md`, `-a`, `-b` (ilk satır §4; yasak sözler ve süre
satırları çıktı; Shorts 31,75 sn) · `surumler.json` (yalnız `s1` adı: `S1 Shorts (31,75 sn)`) · `ortak/kapak/karakter.png` (ana ders kopyası) ·
`K/.claude/docs/sozlesme.md` (1 satır). Metin taraması: senaryo, altyazı, METIN, açıklama temiz; v1 sahne kodunda 03, 04, 07 hâlâ yasak söz taşır.

Kanal katmanı: tek modül YOK (canvas `ortak/kunye.js` yalnız 02'de; HF sahneleri kendi `yardim.py` kopyası) → değerler BRIEF "Kanal katmanı"
tablosunda ve 8 istemde birebir (logo h 48, resim x 53,2 / görünür x 60, y 291–339; `@ydspublishing` Lexend 700 42, x 263, taban 330). 02 istemi
`ortak/kunye.js`'i v2'ye çevirme iznini alır. Sahne istemleri `istem/sahne-v2/`: D-01 (+ kapak A), D-02, D-08 (yeni), D-03, D-04, D-05, D-06, D-07.

Açık noktalar:
1. Süre 31,75 sn: standart ≈ 22–26, S2-C eşiği 30 → aşıldı; değer cümlesi 13,08 sn (metin korunacağı için). Yeniden sentez yok; karar şefte.
2. Ana ders `kapak.png` / `kapak-koyu.png` YOK (18:30): D-03 oturumu "ana kapak bekliyor" diye durur (standart §7 madde 5).
3. Çağrı kartı 900×506 (standart ≈ 920×518): içerik bölgesi x 60–960 sınırı için. Çip kalktı (üst 0–280 boş).
4. Hikâye B cevapsız soru kartından soru–cevap + kural özeti düzenine geçer (§6 "kural özeti + Kaydet"); kapak B karakter görselini taşır.
5. Durağan kareler (04–07) çakışma kapısıyla ölçülemez (çıkış 2 beklenir, S1-VAR §5); istemlerde gözle denetim.
6. Söyleniş "YeDeSe Publishing" Nadir kulağıyla kesinleşir (standart §4); `I am living` 0,96 (v1 ile aynı, "I'm").
