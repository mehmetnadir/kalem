# İstem S1-VAR — 02-04-ydt-temel-s1 huni sürümleri: kapak B/C, hikâye B, açıklama B · 15.11.2026

BAĞLAYICI STANDART: üretimden önce `D/.claude/docs/` altından oku — `huni-v2-standart.md` (kısa), `kapak-standardi.md` (kapak, hikâye), `youtube-surumu-standart.md` (YouTube sürümü), `huni-ab-sozlesme.md` (A/B kolu). Bu istemdeki eski (v1) söz bunlarla çelişirse standart geçer. mp4 yalnız Nadir'in açık sözüyle. D=`/home/sef/01dev/dijital-anlatim`.

MAKİNE: Linux x86_64 (srv21), kullanıcı sef. K=`/home/sef/01dev/_worktrees/kalem-0204` (worktree), D=`/home/sef/01dev/dijital-anlatim`.
Node `~/.nvm/versions/node/v24.22.2/bin`. Python `/usr/bin/python3 -I`. Skill `~/.claude/skills/motion-grafik-ders/`.
KURALLAR: Yazma yalnız `K/projeler/02-04-ydt-temel-s1/` altında. Var olan sahne kodlarına (01–04) dokunma. Silme yok
(`~/Silinecekler/2026-11-15-0204/`). mp4 render YOK. Ses yok. git commit yok. Claude alt ajanı yok.
Kod yolu: 15+ satır kod dosyasını kapı sana kapatır → sahne dizininde `SPEC.md` (tasarım; tam kod yok) + `agy-filo tek --rol kod
--cwd /home/sef/01dev/_worktrees/kalem-0204 --zaman 25m -p "<SPEC.md mutlak yolunu oku ve uygula. Yalnız <dosya> yaz…>"`; kodu agy
yazar, sen okur ve doğrularsın. Tam kodu yazıp agy'ye kopyalatmak yasak. Örnek dosyayı kopyalayıp küçük Edit'le uyarlamak serbest.

Nadir 15.11: huni çok sürümlü — kısa başına 3 kapak (A/B/C), 2 hikâye karesi (A/B), 2 açıklama seti (A/B). S1'de A sürümleri var
(sahne 01 → `kapak.png`, sahne 04 → `hikaye.png`, `aciklama.md`). Bu iş B/C sürümlerini ekler.

## Okuma
`BRIEF-S1.md`, `uretim-tutanagi/{kapak-taslak,hikaye-taslak,aciklama-taslak}.md`, jüri `uretim-tutanagi/juri/`, `S1-duzeltme.md`,
sahne 01 ve 04'ün kodu + RAPOR.md (kalıp), `D/.claude/docs/dikey-senaryo-kalibi.md` §4, `D/.claude/docs/huni-plan-1211.md` §4–§7.

## Yaz
1. Taslaklara ekle (var olan metni değiştirme, yeni bölüm): kapak B = soru/merak başlığı, kapak C = karşıt çift (I live / I am living
   üst üste, tek vurgu); hikâye B = soru kartı ("hangisi doğru?" iki seçenek, cevap yok); açıklama B = soru ile açılan set
   (YouTube / Instagram / TikTok; `utm_content` = `s1-b`; A setinde `s1-a`). Başlık ≤ 4 sözcük, 2 satır; kalıp §4 yasakları; künye
   renkleri `ortak/kunye.js`; dil kararı: öğretmen + YDT öğrencisi.
2. Durağan kare sahneleri (zaman çizelgesi dışı, sahne 04 kalıbı): `sahneler/05-hyperframes-kapak-b/` → paket kökünde `kapak-b.png`,
   `06-hyperframes-kapak-c/` → `kapak-c.png`, `07-hyperframes-hikaye-b/` → `hikaye-b.png` (1080×1920, açık tema; koyu tema karesi de
   `k/koyu/` altına). `zaman.json`'a `hikaye` alanının yanına `durağan` listesi ekleme gerekiyorsa birleştirmeyi bozmayan biçimde yaz.
3. A sürümlerini adlandır (kopya; özgün dosyalar kalır): `kapak.png` → `kapak-a.png`, `hikaye.png` → `hikaye-a.png`,
   `aciklama.md` → `aciklama-a.md`; yeni `aciklama-b.md`. `kapak.png` ya da `hikaye.png` henüz yoksa (sahne 01/04 oturumu sürüyor
   olabilir) 10 dk'ya kadar bekle; yine yoksa raporla.
4. `surumler.json`: kısa video satırının `kimlik`'i `s1` olsun (ad aynı). Huni satırlarını `uretim-tutanagi/huni-surumler.json`'a yaz
   (`{"surumler":[…]}`; surumler.json'a GİRMEZ, şef taşır): `{"kimlik":"s1-kapak-a","tur":"kapak","ad":"S1 Kapak A","durum":"inceleme",
   "dosya":"kapak-a.png","seviye":"temel","kaynak":"ana-yatay"}` biçiminde 3 kapak, 2 hikâye (`s1-hikaye-a/b`, `hikaye-a/b.png`),
   2 açıklama (`s1-aciklama-a/b`, `aciklama-a/b.md`).
5. Doğrula: her yeni PNG'ye Read ile BAK (taşma, kesik yazı, kontrast, boş alan, başlık 2 satır); `file` ile 1080×1920 olduğunu
   doğrula; A/B/C yan yana gerçekten farklı mı. Çakışma kapısı bu sahneleri ölçebiliyorsa koş (`node araclar/cakisma-kapisi.mjs
   02-04-ydt-temel-s1 --sahne <klasör> --port 41333 --sunucu 41022`); ölçemiyorsa hatayı raporla, aracı değiştirme. En çok 3 düzeltme turu.
6. `uretim-tutanagi/S1-VAR-RAPOR.md`: dosyalar, sürüm farkları, bakılan kareler, agy koşu özetleri, açık noktalar.

Son mesajın en çok 12 satır.
