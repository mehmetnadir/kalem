# İstem DUZ2-@KOD@ — `@PA@` ve kol b'si `@PB@`: J2 özeti A sınıfı düzeltmeleri · 15.11.2026

MAKİNE: Linux x86_64 (srv21), kullanıcı sef. K=`/home/sef/01dev/_worktrees/kalem-0204` (worktree), D=`/home/sef/01dev/dijital-anlatim`.
SABİT KURALLAR: silme yok (`rm` yok; gereksiz dosya `/home/sef/Silinecekler/2026-11-15-duz2-@KOD@/` altına taşınır). mp4 render yok. git commit yok
(şef atar). Alt ajan yok, agy-filo yok. `.env`, `*.key` okuma; anahtar ya da jeton yazdırma. Kanca atlama bayrağı oluşturma. Arka plan işi beklerken
`pgrep -f` kullanma; komutu ön planda `timeout` ile koştur. Türkçe karakter tam. Yalnız şu iki pakete yaz: `K/projeler/@PA@`, `K/projeler/@PB@`.
Ana ders paketine, öteki kısalara ve `K/ortak/` altına dokunma. Yeni görsel üretme (imagen yok).

## Girdi (önce oku)
- Özet: `K/uretim-hatti/raporlar/J2-OZET-1511.md` — §3A (kusurlar ve "A3 ayrıntısı" tablosu), §4.1 (toplu düzeltmeler), §4.2 satır **@RK@**, §4 "Sıra".
- Hükümler: `K/projeler/@PA@/uretim-tutanagi/juri/J2-hukum.md`; kol b için `K/projeler/@PB@/uretim-tutanagi/juri/KBJ-hukum.md` (varsa) ve
  `K/projeler/@PB@/uretim-tutanagi/KBC-RAPOR.md`.
- Standartlar (D/.claude/docs): `huni-v2-standart.md`, `huni-ab-sozlesme.md` (§4 tek değişken), `kapak-standardi.md`, `juri-olcutleri.md` (15.11
  akşam güncellendi: HV-13, HV-17, HV-19, HV-20a/b, HV-24, HV-25, AB-8, AB-9).
- Skill: `~/.claude/skills/motion-grafik-ders/SKILL.md` ("Bağlayıcı standartlar" tablosu).

## Şef kararları (uygula)
- Rozet `YDT · TEMEL` (TD-1). Kaynakta düzelt (senaryo, BRIEF, `ortak/kunye.js`, sahne üreticileri), sonra kareleri yeniden üret.
- @KARAKTER@
- Hikâye B kural özeti taşır (A6; istisna yok).
- A3 / A4 cümleleri raporun "Önerilen" sütunundaki metinle değişir. Öneriyi dil bilgisi açısından kendin de denetle: cümle kaynaktan bağımsız
  doğru olmalı. Öneri de yanlış ya da kapsamsızsa daha doğru kısa cümleyi yaz ve raporda gerekçele. Kart, kapak, hikâye ve açıklama metni sesle
  aynı terimi taşır.
- Ölçüt hatası (B sınıfı) ve yayın sonrası maddelere (AB-4, AB-5, AB-7) dokunma.

## İş
1. Kol a (`@PA@`): rapor §4.2'deki **@RK@** satırındaki bütün işleri ve bu pakete düşen toplu düzeltmeleri (TD-1 … TD-4) yap. Sıra raporun "Sıra"
   listesidir: önce ses, sonra metin ve kart, sonra kareler TEK koşuda.
2. Ses değişiyorsa: yalnız değişen cümleyi sentezle (`D/araclar/iki-dilli/el.py`; öteki cümleler önbellekten gelir, sha256 değişmez). `sureler.json`,
   `sozcukler.json`, `zaman.json`, altyazı ve karaoke zamanları yeniden kurulur. Whisper eşiği kısa videoda ≥ 0,90. Toplam süre ≤ 35 sn (hedef
   22–26). İlk söz anını ve kanca cümlesi bitişini yeniden ölç; sınırı aşan değeri raporda yaz.
3. Kol b (`@PB@`): aynı düzeltmeler birebir uygulanır. Tek değişken kuralı korunur:
   - İki kolda metni aynı olan cümlenin ses dosyası kol a'dan KOPYALANIR (sha256 eşit; AB-9). Kol b'de yeniden sentez yalnız değişken cümlesi içindir.
   - Değişken dışındaki sahneler iki kolda aynı içerikle ve aynı göreli anda başlar (AB-3).
   - Kol b bağımsız kopyadır (AB-8): kol b'nin hiçbir sahnesi ve `ortak/kunye.js` içindeki `KOK` kol a yolunu göstermez. Şu çıktıyı rapora yaz:
     `grep -rn "@PA@/" K/projeler/@PB@ --include=*.js --include=*.html --include=*.json --include=*.py` (kalabilecek tek başvuru: `surumler.json`
     `varyant` alanı).
   - KBJ hükmündeki GERÇEK hataları da düzelt (ör. kol a'dan kopya kareler: kol b'nin bütün sahne kareleri kol b'den yeniden çekilir). Ölçüt
     hatası olanları (HV-13 kapanış değişkeni, HV-17, kol b'de HV-20 ve HV-21, AB-4/5/7) raporda "ölçüt" diye işaretle, dokunma.
   - Sonunda `diff -rq K/projeler/@PA@ K/projeler/@PB@` çıktısını sınıfla (beklenen / beklenmeyen). Beklenmeyen 0 olmalı ya da tek tek gerekçeli.
4. Kareler: iki pakette bütün sahnelerin ve türevlerin (kapak A/B/C, hikâye, açık + koyu; kol b'de yalnız var olan türevler) karelerini yeniden çek
   ve KENDİN bak: taşma, çakışma, okunmayan yazı, rozet metni, karakter, altyazı. Paketin çakışma kapısını koş; komutu ve çıkış kodunu yaz.
5. `surumler.json` sürüm kaydına düzeltme notu ekle (var olan alan düzenine uy; yeni alan icat etme).
6. Kanıt dosyası: `K/projeler/@PA@/uretim-tutanagi/DUZ2-RAPOR.md` ve kol b'de aynı adla: düzeltme başına satır (kusur kimliği, dosya, önce → sonra,
   kanıt: komut çıktısı ya da kare yolu), yeni süre ve Whisper tablosu, diff sınıflaması, düzeltilmeyen madde ve sebebi.

Son mesajın en çok 12 satır: düzeltilen kusur kimlikleri, yeniden sentezlenen cümle sayısı, yeni süreler (a / b), Whisper en düşük, diff beklenmeyen
sayısı, kapı çıkış kodu, düzeltemediğin madde ve sebebi, rapor yolu.
