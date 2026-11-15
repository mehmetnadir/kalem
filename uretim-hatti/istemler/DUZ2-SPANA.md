# İstem DUZ2-SPANA — `simple-present-temel` ve `simple-present-temel-dikey`: J2 özeti ana ders düzeltmeleri · 15.11.2026

MAKİNE: Linux x86_64 (srv21), kullanıcı sef. K=`/home/sef/01dev/_worktrees/kalem-0204` (worktree), D=`/home/sef/01dev/dijital-anlatim`.
SABİT KURALLAR: silme yok (`rm` yok; eski dosya `/home/sef/Silinecekler/2026-11-15-duz2-SPANA/` altına taşınır). mp4 render yok. git commit yok (şef
atar). Alt ajan yok, agy-filo yok. `.env`, `*.key` okuma; anahtar ya da jeton yazdırma. Kanca atlama bayrağı oluşturma. Arka plan işi beklerken
`pgrep -f` kullanma; komutu ön planda `timeout` ile koştur. Türkçe karakter tam. Yalnız şu iki pakete yaz: `K/projeler/simple-present-temel`,
`K/projeler/simple-present-temel-dikey`. Kısalara (`-s1` … `-s3b`) dokunma; onları ayrı oturumlar düzeltir. Yeni görsel üretme (imagen yok).

## Girdi (önce oku)
- Özet: `K/uretim-hatti/raporlar/J2-OZET-1511.md` — §3A "Ana derste aynı hata" tablosu (`simple-present-temel`, `simple-present-temel-dikey`
  satırları), §4.1 TD-1, TD-2, TD-3.
- Standartlar (D/.claude/docs): `kapak-standardi.md`, `juri-olcutleri.md` (§2b ders, §2c kapak KS-…), `sozlesme.md` K22 (kadro).
- Skill: `~/.claude/skills/motion-grafik-ders/SKILL.md` ("Bağlayıcı standartlar" tablosu).
- Paketlerin kendi kayıtları: `senaryo.json`, `METIN.md`, `altyazi.json`, `surumler.json`, `youtube.json`, `youtube-aciklama.md`, `ortak/kapak/KAYNAK.json`.

## İş
1. **Karakter (A2, TD-2).** Şef yeni karakteri üretti: `/home/sef/is/uretim-0204/girdi/sp-karakter-kadin.png` (1024×1024, şeffaf zemin; genç kadın
   öğrenci, uzun düz saç, uzun kâkül, yuvarlak gözlük, kazak; sol eliyle işaret eden "buldum" ifadesi; 02-04 dersindeki öğrenciyle aynı kişi).
   - Eski `ortak/kapak/karakter.png` dosyasını Silinecekler dizinine taşı; yenisini `ortak/kapak/karakter.png` olarak koy.
   - `ortak/kapak/KAYNAK.json` kaydını güncelle: `uretim_id` `f312969e-8b2f-4d67-bdb7-f94c3be81fdb`, `kaynak_uretim_id`
     `e0b6d5c6-02db-4b3f-93bc-1c6f9c41c73c`, referans `uretim:3c22184a-e98e-4fbd-892f-e0f028e2490d` (02-04 karakteri), tarif yukarıdaki cümle,
     model `nano-banana-2`, kalite `1k`, usd 0.04, tarih 2026-11-15.
   - Yatay kapakları (`kapak.png`, `kapak-koyu.png`) ve dikey paketin kapaklarını paketin kendi kapak üreticisiyle yeniden üret. Karakterin işaret
     yönü değiştiyse yerleşimi `kapak-standardi.md`'ye göre düzelt (karakter metne bakar ya da metni gösterir; metnin üstüne binmez). Dikey paket
     karakteri kopyayla taşıyorsa yeni dosyayı oraya da kopyala.
2. **Rozet (A1, TD-1).** `YDT · BASIC` → `YDT · TEMEL`: iki pakette kaynakta düzelt (`senaryo.json`, `ortak/kunye.js`, sahne üreticileri), rozeti
   gösteren sahneleri yeniden üret. `grep -rn "BASIC" <paket>` çıktısı üretim dosyalarında 0 olmalı (tutanak ve jüri dosyaları sayılmaz).
3. **Yanlış denklik (A3, TD-3).** Cümle 7 "Türkçedeki er eki gibi: git-er, go-es." yanlıştır: Türkçe geniş zaman eki her kişide gelir, İngilizce
   `-s` yalnız üçüncü tekil kişide gelir. Cümleyi kaynaktan bağımsız doğru, kısa bir cümleyle değiştir (ör. "He, she, it özneyse fiile s gelir:
   go, goes."). Kendi önerin daha doğruysa onu yaz ve gerekçele. Aynı denkliği taşıyan her yeri düzelt: `senaryo.json` (cümle + `meta.canAlici[0]`),
   `METIN.md`, `altyazi.json`, `surumler.json`, `youtube.json` ve `youtube-aciklama.md` (varsa aynı ifade), ekrandaki kart metni.
   - Ses: yalnız cümle 7 yeniden sentezlenir (`D/araclar/iki-dilli/el.py`; öteki cümleler önbellekten, sha256 değişmez). Whisper eşiği derste ≥ 0,85.
     Süre değişirse `sureler.json`, `sozcukler.json`, `zaman.json`, altyazı ve sonraki sahnelerin başlangıçları yeniden kurulur; `youtube.json`
     `bolumler` ve `bildirimler` anları yeni zamana göre düzeltilir (ders zamanı; giriş klibi eklenmez).
   - Dikey paket aynı sesi kullanıyorsa aynı dosyayı kopyala (sha256 eşit); yeniden sentezleme.
4. Kareler: değişen her sahnenin ve 4 kapağın (yatay açık + koyu, dikey açık + koyu) karelerini yeniden çek ve KENDİN bak: taşma, çakışma, okunmayan
   yazı, rozet, karakter. Çakışma kapısını koş; komutu ve çıkış kodunu yaz.
5. `surumler.json` sürüm kaydına düzeltme notu ekle (var olan alan düzenine uy).
6. Kanıt: `K/projeler/simple-present-temel/uretim-tutanagi/DUZ2-RAPOR.md` (dikey için aynı adla): düzeltme başına satır (kusur, dosya, önce → sonra,
   kanıt), cümle 7'nin eski ve yeni metni, yeni süre, Whisper tablosu, kapak kare yolları.

Son mesajın en çok 12 satır: cümle 7'nin yeni metni, süre (önce → sonra), Whisper en düşük, yeniden üretilen sahne ve kapak sayısı, kapı çıkış kodu,
karakter dosyasının sha256'sı (kısa oturumları bunu kopyalayacak), düzeltemediğin madde ve sebebi, rapor yolu.
