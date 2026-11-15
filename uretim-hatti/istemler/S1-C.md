# İstem S1-C — 02-04-ydt-temel-s1 paket + ses + zaman + sahne istemleri + açıklama · 15.11.2026

BAĞLAYICI STANDART: üretimden önce `D/.claude/docs/` altından oku — `huni-v2-standart.md` (kısa), `kapak-standardi.md` (kapak, hikâye), `youtube-surumu-standart.md` (YouTube sürümü), `huni-ab-sozlesme.md` (A/B kolu). Bu istemdeki eski (v1) söz bunlarla çelişirse standart geçer. mp4 yalnız Nadir'in açık sözüyle. D=`/home/sef/01dev/dijital-anlatim`.

MAKİNE: Linux x86_64 (srv21), kullanıcı sef. K=`/home/sef/01dev/_worktrees/kalem-0204` (worktree, dal `sunucu/02-04-ydt-temel`),
D=`/home/sef/01dev/dijital-anlatim`. Python `/usr/bin/python3 -I`; ses venv `~/.venvs/ses`. Node `~/.nvm/versions/node/v24.22.2/bin`.
KURALLAR: Yalnız isteneni yaz. Silme yok (`~/Silinecekler/2026-11-15-0204/` altına taşı). Render yok, sahne kodu yok, git commit yok,
Claude alt ajanı yok. Yazma yalnız `K/projeler/02-04-ydt-temel-s1/` altında. ElevenLabs YALNIZ `araclar/ses-sunucu.sh` ile (kayit vekili;
anahtar görmezsin; başka yoldan çağrı yok). Kod yazma kapısı 15+ satır kod dosyasını kapatır: betikleri örnek paketten KOPYALA ve
küçük Edit'le uyarla; yeni uzun betik gerekiyorsa SPEC.md + `agy-filo tek --rol kod …` yolu (tam kodu yazıp agy'ye kopyalatmak yasak).

Girdi (jüriden geçti ya da düzeltildi): `K/projeler/02-04-ydt-temel-s1/uretim-tutanagi/` — `senaryo-taslak.md`, `kapak-taslak.md`,
`hikaye-taslak.md`, `aciklama-taslak.md`, `S1-A-RAPOR.md`, jüri `juri/s1.dil.md`, `juri/s1.kaynak-kural.md`.
Örnek paket (biçim tek kaynağı): `K/projeler/present-continuous-ileri-s1/`. Ana ders: `K/projeler/02-04-ydt-temel/`.
Ses zinciri örneği (yatay ders, sunucuda koştu): `~/is/uretim-0204/ses-zinciri.sh`.

## Adımlar
1. Jüri maddelerini uygula: DÜZELT maddelerini taslaklara işle, `uretim-tutanagi/S1-duzeltme.md`'ye madde → yapılan → kanıt yaz.
   Jüri kararıyla çelişen ya da Nadir kararı gerektiren madde varsa uygulama, raporla.
2. İskelet: present-continuous-ileri-s1 yapısı (`ortak/` bağları ve dosyaları, `gorevler.json`, `yorumlar.json`, `harita-konum.json`,
   `BRIEF-S1.md`). Künye verisi 02-04'e göre.
3. `ortak/anlatim/senaryo.json`: örnekle aynı şema; ses kimliği ana dersin öğretmen sesi; ham sözcük, rakam yok.
4. Ses: `cd K && bash araclar/ses-sunucu.sh 02-04-ydt-temel-s1` (el.py, faster-whisper turbo kapısı). Sonra örnek paketteki ses betikleri
   (`ortak/anlatim/*.py`) ve yatay zincirdeki adımlarla: sözcük zamanı, kur (m4a + imza), altyazı, METIN. Kapı geçmezse dur ve raporla
   (aynı cümle 2 kez düşerse yeniden deneme yok).
5. `zaman.json`: 1080×1920, 30 fps, gecis_kare 12; 4 sahne: `01-hyperframes-kapak`, `02-<motor>-ornek`, `03-hyperframes-cta`
   (örnekteki gibi, sürelerin toplamı = anlatım) ve `04-hyperframes-hikaye` (hikâye karesi: anlatımdan bağımsız, 1 kare yeter; zaman
   çizelgesine girmez — zaman.json'da ayrı `hikaye` alanı ya da sahne listesinin dışında; birleştirmeyi bozmayacak biçimi seç ve yaz).
6. `BRIEF-S1.md`: örnek biçiminde (çıktı, kaynaklar, sahne tablosu, kapak ve hikâye karesi tarifi, çalıştırma).
7. `aciklama.md` (paket kökü): jüriden geçmiş açıklama metni; YouTube / Instagram / TikTok bölümleri; yer tutucular açık ve listeli.
8. `surumler.json`: present-continuous-ileri-s1 biçiminde, `video.kimlik` = `02-04-ydt-temel`. YALNIZ bu sürüm:
   `{"kimlik":"shorts","tur":"shorts","ad":"S1 Shorts (<ölçülen> sn)","durum":"uretimde","onizleme":"/p/02-04-ydt-temel-s1/onizle.html","seviye":"temel","kaynak":"ana-yatay"}`.
   Huni satırları (aşağıdaki 3 satır) şimdilik `uretim-tutanagi/huni-surumler.json` dosyasına (`{"surumler":[…]}`) yazılır,
   surumler.json'a GİRMEZ: kayit'in yeni sürümü yayına alınmadan içe alma bu türleri tanımaz, yatay video sanar (şef sonra taşır):
   `{"kimlik":"kapak","tur":"kapak","ad":"Kapak (1080x1920)","durum":"uretimde","dosya":"kapak.png","seviye":"temel","kaynak":"ana-yatay"}`,
   `{"kimlik":"hikaye","tur":"hikaye","ad":"Hikâye karesi (1080x1920)","durum":"uretimde","dosya":"hikaye.png","seviye":"temel","kaynak":"ana-yatay"}`,
   `{"kimlik":"aciklama","tur":"aciklama","ad":"Açıklama + UTM","durum":"hazir","dosya":"aciklama.md","seviye":"temel","kaynak":"ana-yatay"}`.
9. Sahne istemleri `uretim-tutanagi/istem/sahne/D-<klasör>.md` × 4: şablon `~/is/uretim-0204/D-dikey-sablon.md`'yi pakete kopyala ve
   S1'e uyarla (paket adı `02-04-ydt-temel-s1`, BRIEF-S1 satırı, örnek sahne present-continuous-ileri-s1 içinden; kapak sahnesi
   `kapak.png`'yi örnekteki gibi üretir; hikâye sahnesi `hikaye.png` üretir).
10. `uretim-tutanagi/S1-C-RAPOR.md`: yazılanlar, ses kapısı sonucu (cümle başına benzerlik), anlatım süresi, açık noktalar.

Son mesajın en çok 12 satır.
