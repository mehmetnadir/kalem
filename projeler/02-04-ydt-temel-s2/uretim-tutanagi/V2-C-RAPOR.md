# V2-S2-C raporu — 02-04-ydt-temel-s2 huni v2 çevirisi · 15.11.2026

| Ölçüm | Değer |
|---|---|
| Ses kapısı (large-v3-turbo, eşik 0,85; standart ≥ 0,9) | 10 / 10 parça 1,00, tohum 0; 6 parça önbellek (cümle 1–2), 4 parça yeni (117 karakter ≈ 0,57 TL, `ses-sunucu.sh`) |
| Çağrı sesi | öğrenci `…9gjY` (`oPC5I9GKjMReiaM29gjY`, ana ders `kadro.ogrenci` kopyası); kanıt: parça önbellek anahtarı öğrenci kimliğiyle var, öğretmen `…4fwc` ile yok |
| Anlatım | 29,41 sn (`anlatim.m4a` ffprobe 29.410000, imza `1be57daa…`); v1 27,98. Standart hedef 22–26 (§3) aşıldı, 30 altında |
| Cümle başı–bitişi | 1: 1,00–2,84 · 2: 3,39–17,41 · 3: 17,96–22,75 · 4: 23,30–28,41 · kuyruk 1,0 |
| Zaman çizelgesi | 01 kapak 0,00–2,84 (97) → 02 örnek 2,84–17,41 (449) → 08 kaydet 17,41–22,75 (172) → 03 çağrı 22,75–29,41 (230); 04–07 `hikaye`/`duragan` yerinde |
| Yedek | `~/Silinecekler/2026-11-15-huni-v2/02-04-ydt-temel-s2/` (`cp -a`: `ortak/anlatim/`, `zaman.json`, `surumler.json`, BRIEF, açıklamalar, 7 PNG; `diff -rq` aynı) |
Değişen cümleler (cümle 1–2 metni aynı):
- 3 (öğretmen) eski: "Bu, üç farktan yalnız biri. Tam ders: Simple Present ve Present Continuous. Üç farkın hepsi dört buçuk dakikada."
  → yeni 3 (öğretmen): "Bu, üç farktan yalnız biri." + "Bu kuralı kaybetme. Kaydet." · yeni 4 (öğrenci): "Bitmedi, gel." + "Dersin tamamı YDS Publishing YouTube kanalında."
- Whisper: "Bu 3 farktan yalnız biri." 1,00 · "Bu kuralı kaybetme, kaydet." 1,00 · "Bitmedi, gel." 1,00 · "Dersin tamamı YEDESE Publishing YouTube kanalında." 1,00
  (kıyas ses metniyle `YeDeSe`; ekran metni `YDS` ile 0,97). Senaryoda `Tam ders`, `dakika`, rakam yok.

Yazılanlar: `senaryo.json` (`sesler`/`kadro` + öğrenci), `zaman_uret.py` (SAHNE 4 satır), ses zinciri çıktıları (log `ses-sentez-v2.log`), `zaman.json`,
`BRIEF-S2.md` (yerleşim §2, sahne tablosu, 08/03 içerik, kapak/hikâye bölgeleri), `aciklama-a|b.md` + `aciklama.md` (= A), `surumler.json`
(yalnız `S2 Shorts (29,41 sn)`), `ortak/kapak/karakter.png` (ana ders kopyası, md5 `3d846e4b…`), `istem/sahne-v2/D-*.md` × 8. Paket dışı: sözleşmeye 1 satır.

Kanal katmanı: ortak mekanizma tek yerden VERMİYOR (Paper.js `ortak/kunye.js` v1 HUD; HyperFrames 6 ayrı `yardim.py`). Değerler BRIEF "Yerleşim"
tablosunda ve 8 istemde aynı, S1 BRIEF ile eşit: logo x 53,2 y 291–339 h 48 · `@ydspublishing` Lexend 700 42 x 263 taban 330 · kimlik `kanal`.
İstemler: 01 kapak (+ kapak A altyazısız) · 02 örnek · 08 kaydet (yeni) · 03 çağrı (ana kapak) · 04 hikâye A · 05 kapak B (karakter) · 06 kapak C · 07 hikâye B.
Açık noktalar:
1. Süre 29,41 > hedef 22–26; kısaltma senaryo kararı (ör. "Bu, üç farktan yalnız biri." çıkar ≈ −2,3 sn). Şef/Nadir.
2. Ana kapak yok: `02-04-ydt-temel/kapak.png`, `kapak-koyu.png`. Sahne 03 istemi kopyalamadan önce durur ("ana kapak bekliyor").
3. Rozet `YDT · BASIC` (paket + S1); standart örneği `YDT · TEMEL`. Dil kararı Nadir'de.
4. `birlestir.py --gecis BookFlip` sahne sınırında bütün kareyi çevirir; kanal katmanı §1 kural 1 ("animasyon yok") bozulur. Birleştirmede geçiş seçimi şefte.
5. Ana kapak kartı 900×506 (standart ≈ 920×518): sağ 960–1080 platform arayüzü altında. Durağan 04–07'de çakışma kapısı "sahne bulunamadı" (araç sınırı).
6. "YeDeSe Publishing" söylenişi Nadir dinleyince kesinleşir (§4). `METIN.md` başlığı "sahne 01 3 sn" eski sabit metin (gerçek 2,84).
