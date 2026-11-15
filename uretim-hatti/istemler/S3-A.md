# İstem S3-A — 02-04-ydt-temel-s3 kısa video senaryo taslağı + çok sürümlü kapak, hikâye karesi, açıklama · 15.11.2026

BAĞLAYICI STANDART: üretimden önce `D/.claude/docs/` altından oku — `huni-v2-standart.md` (kısa), `kapak-standardi.md` (kapak, hikâye), `youtube-surumu-standart.md` (YouTube sürümü), `huni-ab-sozlesme.md` (A/B kolu). Bu istemdeki eski (v1) söz bunlarla çelişirse standart geçer. mp4 yalnız Nadir'in açık sözüyle. D=`/home/sef/01dev/dijital-anlatim`.

MAKİNE: Linux x86_64 (srv21), kullanıcı sef. K=`/home/sef/01dev/_worktrees/kalem-0204` (worktree), D=`/home/sef/01dev/dijital-anlatim`.
Python `/usr/bin/python3 -I`. Skill `~/.claude/skills/motion-grafik-ders/`.
KURALLAR: Yalnız isteneni yaz. Silme yok. Ses sentezi yok, ElevenLabs çağrısı yok, render yok, sahne kodu yok, git commit yok,
alt ajan yok. Yazma yalnız `K/projeler/02-04-ydt-temel-s3/uretim-tutanagi/` altında (dizini sen aç).
Nadir 15.11: huni çok sürümlü üretilecek — ders başına 3 kısa (dersin üç farkı), kısa başına 3 kapak, 2 hikâye karesi, 2 açıklama seti.
Bu kısa: **S3 — tarifeli gelecek / planlanmış gelecek (The train to İzmir leaves at 7 pm today · I am going to the movie theater tonight); öğrencinin sorusu "tren de plana göre kalkmıyor mu?"**. Ana dersteki kaynağı: cümle 5–7 (örnek 3 + soru anı 1), cümle 10; sahne 05, 06, 09.

## Okuma
1. Ana ders: `K/projeler/02-04-ydt-temel/` — `ortak/anlatim/senaryo.json`, `sozcukler.json`, `surumler.json` (`video.canAlici`, `kod`),
   `BRIEF.md`, `uretim-tutanagi/juri.md`. Ana ders süresi ölçüldü: 265,7 sn ("dört buçuk dakika").
2. Jüriden geçmiş emsal (biçim ve kararların TEK kaynağı): `K/projeler/02-04-ydt-temel-s1/` — `uretim-tutanagi/senaryo-taslak.md`,
   `kapak-taslak.md`, `hikaye-taslak.md`, `aciklama-taslak.md`, `S1-duzeltme.md` (jürinin 7 maddesi: tekrarlama), `BRIEF-S1.md`,
   `aciklama.md`, `uretim-tutanagi/S1-C-RAPOR.md`. S1 ile aynı kimlik, aynı kapanış ilkesi, aynı künye renkleri (`ortak/kunye.js`).
3. Kalıp: `D/.claude/docs/dikey-senaryo-kalibi.md` §4–§5; `D/.claude/docs/huni-plan-1211.md` §4–§7.

## Yaz
1. `senaryo-taslak.md` — 3 sahne (kapak · örnek · tam ders çağrısı), HEDEF 24–28 sn (S1 30,56 sn çıktı: tahmini ana dersin ölçülmüş
   konuşma hızından yap ve 28 sn'yi aşma). Tablo: sahne, konuşan, ses metni (TR/EN parçalar), ekran metni, görsel fikir. İlk söz ≤ 1 sn.
   Ana dersin cümlesiyle birebir aynı cümle varsa belirt (ses önbellekten gelir). Ekran metni sesten ÖNCE gelmez, sahne sınırı sözcük
   zamanına göre. Kapanış S1 ile aynı kalıpta ("üç farktan biri" + tam ders çağrısı + süre; "kanal" ve QR yok, `@ydspublishing`).
   Rakam yazma. Yeni Türkçe cümleleri "ana derste yok, jüri bakacak" diye işaretle.
2. `kapak-taslak.md` — 3 kapak sürümü (A, B, C), 1080×1920. Sürümler gerçekten farklı olsun: A = can alıcı kod (S1 kalıbı),
   B = soru/merak başlığı, C = karşıt çift (iki cümle üst üste, tek vurgu). Her biri: başlık (≤ 4 sözcük, 2 satır), can alıcı, görsel,
   rozet. Kalıp §4 yasakları geçerli.
3. `hikaye-taslak.md` — 2 hikâye karesi sürümü (A = bilgi kartı, B = soru kartı "hangisi doğru?"), 1080×1920 durağan.
4. `aciklama-taslak.md` — 2 açıklama seti (A = kısa/doğrudan, B = soru ile açılan); her sette YouTube / Instagram / TikTok metni,
   UTM huni-plan §6 şemasıyla (`utm_campaign` = ders kodu, olduğu gibi; `utm_content` = `s3-a` / `s3-b`). S1'deki yer tutucular aynen.
   Dil kararı D-0278: Instagram/TikTok öğretmene ve YDT öğrencisine; veli dili yok.
5. `S3-A-RAPOR.md` — yazılanlar, süre tahmini (hesabıyla), sürümler arası fark özeti, açık noktalar.

Son mesajın en çok 12 satır.
