# İstem S3-C — 02-04-ydt-temel-s3 paket + ses + zaman + sahne istemleri + açıklama · 15.11.2026

BAĞLAYICI STANDART: üretimden önce `D/.claude/docs/` altından oku — `huni-v2-standart.md` (kısa), `kapak-standardi.md` (kapak, hikâye), `youtube-surumu-standart.md` (YouTube sürümü), `huni-ab-sozlesme.md` (A/B kolu). Bu istemdeki eski (v1) söz bunlarla çelişirse standart geçer. mp4 yalnız Nadir'in açık sözüyle. D=`/home/sef/01dev/dijital-anlatim`.

MAKİNE: Linux x86_64 (srv21), kullanıcı sef. K=`/home/sef/01dev/_worktrees/kalem-0204` (worktree, dal `sunucu/02-04-ydt-temel`),
D=`/home/sef/01dev/dijital-anlatim`. Python `/usr/bin/python3 -I`; ses venv `~/.venvs/ses`. Node `~/.nvm/versions/node/v24.22.2/bin`.
KURALLAR: Yalnız isteneni yaz. Silme yok (`~/Silinecekler/2026-11-15-0204/` altına taşı). Render yok, sahne kodu yok, git commit yok,
Claude alt ajanı yok. Yazma yalnız `K/projeler/02-04-ydt-temel-s3/` altında. ElevenLabs YALNIZ `araclar/ses-sunucu.sh` ile (kayit vekili;
anahtar görmezsin; başka yoldan çağrı yok). Kod yazma kapısı 15+ satır kod dosyasını kapatır: betikleri örnek paketten KOPYALA ve
küçük Edit'le uyarla; yeni uzun betik gerekiyorsa SPEC.md + `agy-filo tek --rol kod …` yolu (tam kodu yazıp agy'ye kopyalatmak yasak).

Girdi (jüriden geçti ya da düzeltildi): `K/projeler/02-04-ydt-temel-s3/uretim-tutanagi/` — `senaryo-taslak.md`, `kapak-taslak.md`,
`hikaye-taslak.md`, `aciklama-taslak.md`, `S3-A-RAPOR.md`, jüri `juri/s3.dil.md`, `juri/s3.kaynak-kural.md`.
Örnek paket (biçim tek kaynağı, aynı dersin bitmiş kısası): `K/projeler/02-04-ydt-temel-s1/` (iskelet, ortak/, senaryo.json şeması, zaman_uret.py, BRIEF-S1.md, sahne istemleri `uretim-tutanagi/istem/sahne/`). Ana ders: `K/projeler/02-04-ydt-temel/`.
Ses zinciri örneği (yatay ders, sunucuda koştu): `~/is/uretim-0204/ses-zinciri.sh`.

## Adımlar
1. Jüri maddelerini uygula: DÜZELT maddelerini taslaklara işle, `uretim-tutanagi/S3-duzeltme.md`'ye madde → yapılan → kanıt yaz.
   Jüri kararıyla çelişen ya da Nadir kararı gerektiren madde varsa uygulama, raporla.
2. İskelet: 02-04-ydt-temel-s1 yapısı (`ortak/` bağları ve dosyaları, `gorevler.json`, `yorumlar.json`, `harita-konum.json`,
   `BRIEF-S3.md`). Künye verisi 02-04'e göre.
3. `ortak/anlatim/senaryo.json`: örnekle aynı şema; ses kimliği ana dersin öğretmen sesi; ham sözcük, rakam yok.
4. Ses: `cd K && bash araclar/ses-sunucu.sh 02-04-ydt-temel-s3` (el.py, faster-whisper turbo kapısı). Sonra örnek paketteki ses betikleri
   (`ortak/anlatim/*.py`) ve yatay zincirdeki adımlarla: sözcük zamanı, kur (m4a + imza), altyazı, METIN. Kapı geçmezse dur ve raporla
   (aynı cümle 2 kez düşerse yeniden deneme yok).
5. `zaman.json`: 1080×1920, 30 fps, gecis_kare 12; 4 sahne: `01-hyperframes-kapak`, `02-<motor>-ornek`, `03-hyperframes-cta`
   (örnekteki gibi, sürelerin toplamı = anlatım) ve `04-hyperframes-hikaye` (hikâye karesi: anlatımdan bağımsız, 1 kare yeter; zaman
   çizelgesine girmez — zaman.json'da ayrı `hikaye` alanı ya da sahne listesinin dışında; birleştirmeyi bozmayacak biçimi seç ve yaz).
6. `BRIEF-S3.md`: örnek biçiminde (çıktı, kaynaklar, sahne tablosu, kapak ve hikâye karesi tarifi, çalıştırma).
7. `aciklama.md` (paket kökü): jüriden geçmiş açıklama metni; YouTube / Instagram / TikTok bölümleri; yer tutucular açık ve listeli.
8. `surumler.json`: 02-04-ydt-temel-s1 biçiminde, `video.kimlik` = `02-04-ydt-temel`. YALNIZ bu sürüm:
   `{"kimlik":"shorts","tur":"shorts","ad":"S1 Shorts (<ölçülen> sn)","durum":"uretimde","onizleme":"/p/02-04-ydt-temel-s3/onizle.html","seviye":"temel","kaynak":"ana-yatay"}`.
   Huni satırları (aşağıdaki 3 satır) şimdilik `uretim-tutanagi/huni-surumler.json` dosyasına (`{"surumler":[…]}`) yazılır,
   surumler.json'a GİRMEZ: kayit'in yeni sürümü yayına alınmadan içe alma bu türleri tanımaz, yatay video sanar (şef sonra taşır):
   `{"kimlik":"kapak","tur":"kapak","ad":"Kapak (1080x1920)","durum":"uretimde","dosya":"kapak.png","seviye":"temel","kaynak":"ana-yatay"}`,
   `{"kimlik":"hikaye","tur":"hikaye","ad":"Hikâye karesi (1080x1920)","durum":"uretimde","dosya":"hikaye.png","seviye":"temel","kaynak":"ana-yatay"}`,
   `{"kimlik":"aciklama","tur":"aciklama","ad":"Açıklama + UTM","durum":"hazir","dosya":"aciklama.md","seviye":"temel","kaynak":"ana-yatay"}`.
9. Sahne istemleri `uretim-tutanagi/istem/sahne/D-<klasör>.md` × 4: şablon `~/is/uretim-0204/D-dikey-sablon.md`'yi pakete kopyala ve
   S1'e uyarla (paket adı `02-04-ydt-temel-s3`, BRIEF-S3 satırı, örnek sahne 02-04-ydt-temel-s1 içinden; kapak sahnesi
   `kapak.png`'yi örnekteki gibi üretir; hikâye sahnesi `hikaye.png` üretir).
10. `uretim-tutanagi/S3-C-RAPOR.md`: yazılanlar, ses kapısı sonucu (cümle başına benzerlik), anlatım süresi, açık noktalar.

Son mesajın en çok 12 satır.

## Çok sürüm (Nadir 15.11) — bu istemin üstündeki tek sürümlü tarifin yerine geçer
- Kapak 3 sürüm: A zaman çizelgesindeki `01-hyperframes-kapak` sahnesinin karesi (`kapak-a.png`; `kapak.png` de aynı dosyanın kopyası),
  B ve C durağan kare sahneleri (`05-hyperframes-kapak-b` → `kapak-b.png`, `06-hyperframes-kapak-c` → `kapak-c.png`).
- Hikâye 2 sürüm: `04-hyperframes-hikaye` → `hikaye-a.png` (+ `hikaye.png` kopyası), `07-hyperframes-hikaye-b` → `hikaye-b.png`.
- Açıklama 2 set: `aciklama-a.md`, `aciklama-b.md` (paket kökü; `aciklama.md` = A kopyası).
- `zaman.json`: 3 sahne + durağan kareler `sahneler[]` DIŞINDA (S1'deki `hikaye` alanı biçimi; birden çok kare için `duragan` listesi).
- `surumler.json`: yalnız kısa video satırı, `kimlik` = `s3`, `tur` `shorts`, ad `S3 Shorts (<ölçülen> sn)`.
- `uretim-tutanagi/huni-surumler.json`: `s3-kapak-a|b|c` (`tur` `kapak`, `dosya` `kapak-a.png` …), `s3-hikaye-a|b`, `s3-aciklama-a|b`;
  ad `S3 Kapak A` biçiminde; durum `uretimde` (açıklama `inceleme`).
- Sahne istemleri × 7: 01 kapak, 02 örnek, 03 CTA, 04 hikâye A, 05 kapak B, 06 kapak C, 07 hikâye B. Her isteme şu satırı ekle:
  "Kanca atlama bayrağı OLUŞTURMA (/tmp/conductor-*, ~/.conductor/*). Durdurma kancası sözleşme satırı isterse K/.claude/docs/sozlesme.md
  dosyasına 1–2 satır EKLE (tek istisna)." ve qa-yerel t değerlerinin KÜRESEL anlatım saniyesi olduğunu yaz.
- Süre hedefi 24–28 sn; sentez sonrası 30 sn'yi aşarsa raporla (yeniden sentez yok).
- Bu oturum için de geçerli: kanca atlama bayrağı oluşturma; sözleşme kancası isterse `K/.claude/docs/sozlesme.md`'ye 1–2 satır ekle.
