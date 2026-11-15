# İstem D-S2-V2 — 02-04-ydt-temel-s2 sahne 05-hyperframes-kapak-b (huni v2) · 15.11.2026

MAKİNE: Linux x86_64 (srv21), kullanıcı sef. K=`/home/sef/01dev/_worktrees/kalem-0204` (git worktree, dal `sunucu/02-04-ydt-temel`).
D=`/home/sef/01dev/dijital-anlatim`. Node `~/.nvm/versions/node/v24.22.2/bin`. Python `/usr/bin/python3 -I`. Skill `~/.claude/skills/motion-grafik-ders/`.
KURALLAR: Yalnız bu sahnenin dizinine yaz: `K/projeler/02-04-ydt-temel-s2/sahneler/05-hyperframes-kapak-b/`. İstisna: paket kökü `kapak-b.png` (tek kare PNG; eskileri V2 yedeğinde). Başka sahneye, `ortak/`a (istisna yukarıda yazılıysa yalnız o
dosya), `BRIEF-S2.md`'ye, `zaman.json`'a, ana derse (`02-04-ydt-temel`), S1 ve S3 paketlerine dokunma (eksik görürsen raporla).
Silme yok (`~/Silinecekler/2026-11-15-huni-v2/` altına taşı). mp4 render YOK: `calistir.sh`'ı yalnız `ONIZLE_YALNIZ=1` ile koş; tek kare PNG yakalama serbest (teslim PNG'dir; `video.mp4` ve birleştirme yok).
git commit yok. Claude alt ajanı açma.
Kanca atlama bayrağı OLUŞTURMA (/tmp/conductor-*, ~/.conductor/*). Sözleşme kancası isterse K/.claude/docs/sozlesme.md
dosyasına 1–2 satır EKLE (tek istisna).
Önce yedek: `mkdir -p ~/Silinecekler/2026-11-15-huni-v2/02-04-ydt-temel-s2/sahneler/ && cp -a K/projeler/02-04-ydt-temel-s2/sahneler/05-hyperframes-kapak-b ~/Silinecekler/2026-11-15-huni-v2/02-04-ydt-temel-s2/sahneler/` (kopya, taşıma değil); sonra yerinde düzenle.

## Kod yolu (kapı ve doktrin)
Kod yazma kapısı 15 satırdan uzun kod dosyasını sana kapatır; bayrak açmaya çalışma. Yol: tasarımı sahne dizininde `SPEC.md` olarak
yaz (yazılacak dosyanın mutlak yolu, örnek sahnenin mutlak yolu ve oradan alınacak kalıp, olay listesi olay · kare/küresel sn · cümle
sözcüğü, yerleşim, ekran metni, kurallar, kabul ölçütü; tam kod YAZMA). Sonra
`agy-filo tek --rol kod --cwd /home/sef/01dev/_worktrees/kalem-0204 --zaman 25m -p "<SPEC.md mutlak yolunu oku ve uygula. Yalnız <dosya
mutlak yolu> dosyasını yaz. Başka dosyaya dokunma. Silme yok. Test, render, git yok.>"`. Kodu agy yazar; sen baştan sona okur, spec'e
uyuyor mu bakarsın, küçük düzeltmeyi Edit ile yaparsın, büyük düzeltmeyi agy'ye geri verirsin (en çok 2 tur). Tam kodu kendin yazıp
agy'ye birebir kopyalatmak YASAK (kapıyı vekille dolanmaktır). Var olan sahne dosyasını kopyalayıp küçük Edit'le uyarlamak serbest.
Kısa dosyalar (`calistir.sh`, `sayfa.html`) Edit ile yazılabilir.

## Okuma
1. Skill `SKILL.md`, `references/kalem-hatti.md`, `stil-anayasasi.md`, `hareket-sozlugu.md`, `kliseler.md`.
2. BAĞLAYICI: `D/.claude/docs/huni-v2-standart.md` (§1 değişmez kurallar, §2 yerleşim, §3 yapı, §6 türevler, §7 kapı).
3. Paket: `K/projeler/02-04-ydt-temel-s2/BRIEF-S2.md` ("Yerleşim" tablosu ve altındaki kanal katmanı notu; "Sahneler" tablosunda `05-hyperframes-kapak-b` satırı (zaman çizelgesi dışı, 1 kare); "Kapak B ve Kapak C" bölümü B sütunu; ses yok),
   `zaman.json`, `ortak/anlatim/senaryo.json`, `uretim-tutanagi/V2-C-RAPOR.md`.
4. İçerik ve olay kaynağı: bu sahnenin v1 kodu, `SPEC.md` ve `RAPOR.md` (`K/projeler/02-04-ydt-temel-s2/sahneler/05-hyperframes-kapak-b/`; yedekten sonra). İçerik korunur, yerleşim v2'ye çekilir.
5. `uretim-tutanagi/kapak-taslak.md` §4, §6 B satırı; `D/.claude/docs/kapak-standardi.md` (çıkartma kenarı, karakter arkası).

## Kanal katmanı ve künye — bütün sahnelerde AYNI piksel (huni v2 §1 kural 1, §2)
Paketin ortak künye mekanizması kanal katmanını tek yerden VERMİYOR: Paper.js `ortak/kunye.js` v1 HUD çizer; HyperFrames sahneleri ayrı
`yardim.py` kopyası taşır (6 farklı dosya). Bu yüzden değerler burada yazılıdır; sahnenin kendi dosyasında çiz, başka değer icat etme.
- Kanal katmanı (y 280–350): logo resmi x 53,2 (SVG iç boşluğu 68/1920 düşülür, görünür sol kenar x 60), y 291–339,
  yükseklik 48, genişlik 193,5 (en-boy 1920/476,3). Açık tema
  `ortak/logo/yds-publishing-lacivert.svg`, koyu `ortak/logo/yds-publishing-seffaf.svg`. `@ydspublishing` Lexend 700 42 px, sol hizalı,
  x 263, taban y 330, tema mürekkebi (açık `#1b2440`, koyu `#f3efe6`). İlk kareden son kareye alfa 1; giriş/çıkış animasyonu yok;
  uçuş ve geçiş dokunmaz. Kimlik `kanal`; `__kalemKutu` türü `kunye`, ad `kunye:kanal`. Değerler S1 ile aynı (`../02-04-ydt-temel-s1/BRIEF-S1.md` tablosu).
- Künye (y 360–450): konu `Simple Present vs Present Continuous` Fredoka 700, x 60, taban y 420, boy ≤ 34 (rozetle x 960'a
  sığan en büyük, alt sınır 28); rozet hapı `YDT · BASIC` Lexend 700 26 px, y 386–434, konu sonu + 20, dolgu `vurguDolgu`, yazı `pilMetin`.
- Çip (sağ üst bölüm etiketi) YOK. v1 HUD değerleri (logo y 48, ders adı y 212 iki satır 56 px, rozet y 216, çip y 48) KULLANILMAZ.
- 0–280 ve 1570–1920 yalnız zemin. İçerik 460–1380, x 60–960 (sağ 960–1080 platform arayüzü altında). Altyazı 1400–1550.
HyperFrames: `yardim.py` `HUD` sözlüğü ve `kunye_svg` bu değerlere çekilir (sahnenin kendi kopyası; ortak dosya yok). Logo
`<image id="logoimg">` kimliği kalır (`ortak/hf_tema.py` tema değişiminde logoyu bu kimlikle değiştirir). Kanal katmanı ayrı grup
`<g id="kanal">`; hiçbir tween'e, opaklık ya da ölçek animasyonuna girmez.

## Yaz
`sahneler/05-hyperframes-kapak-b/` içinde v1 ile aynı dosya yapısı. Kurallar: tek sütun; yazı tabanı ≥ 64 mantıksal px (kanal katmanı ve künye hariç);
satır ≤ 24 karakter; tek vurgu sarı (rozet hapı künye öğesidir, vurgu sayılmaz); kırmızı yok, emoji yok; altyazı ve karaoke YOK (ses yok); 1400–1920 boş; tema çifti açık + koyu;
sarı hap açık temada dolgu `#ffe066`, yazı `#1b2440`; 9 sn'den uzun boş çerçeve yok; ekranda `T-shirt` tireli (seste `T shirt`).
Ekranda `Tam ders` sözü, süre sözü (`dakika`, `dk`), QR, oynat ya da "izle" düğmesi taklidi YOK (huni v2 §1 kural 4–5).
`calistir.sh`: `[ -d /opt/homebrew/bin ] && export PATH="/opt/homebrew/bin:$PATH"`, yük `Y=$(yuk1)`, yakalama `1080 1920`.

Bu sahneye özel (kapak B — soru; kapak görseli bu karede):
- Başlık 460–800: `TODAY VARSA` / `HANGİ ZAMAN?` mürekkep, hapsız, iki satır aynı boy (en geniş satır ≤ 900 px, üst sınır 190 px; motor
  ölçer). `HANGİ` noktalı İ.
- Sahne 820–1380: kapak görseli `K/projeler/02-04-ydt-temel-s2/ortak/kapak/karakter.png` (V2-S2-C kopyaladı; ana ders `ortak/kapak/karakter.png`, md5 `3d846e4b…`;
  genç kadın öğrenci, iki avuç açık "hangisi?"). `calistir.sh` logoyu nasıl kopyalıyorsa onu da `proje/assets/`'e kopyalar. Çıkartma kenarı:
  karakterin çevresinde 10 px krem kenar (CSS `drop-shadow`, dört yön, `#f3efe6`); açık temada arkasında krem daire, koyu temada daire yok
  (kapak-standardi satır 33–34). v1'deki çizilmiş düşünen öğretmen figürü bu görselle değişir.
- Karakterin yanında `today` yazan takvim yaprağı (kalem çizgisi); sağda büyük sarı `?` (tek vurgu). Görsel x 960 sağına taşmaz.
- Altyazı yok; 1400–1920 boş. v1'deki `Hook` çipi ve sol alt logo (y ≈ 1478) kalkar; logo yalnız kanal katmanında.
- Zaman çizelgesine girmez: `zaman.json` → `duragan` listesi.
- `calistir.sh` (v1 kalıbı): `--tema acik` paket köküne `kapak-b.png`, `--tema koyu` `k/koyu/kapak-b-koyu.png`.

## Doğrula (zorunlu, geçmeden bitirme)
1. Kareler: `ONIZLE_YALNIZ=1 bash calistir.sh` (önizleme hazırlığı), sonra `bash calistir.sh --tema acik` ve `bash calistir.sh --tema koyu`
   → `kapak-b.png` + `sahneler/05-hyperframes-kapak-b/k/koyu/kapak-b-koyu.png` (1080×1920; `ffprobe` ile boyut). Tek kare yakalanamıyorsa dur ve hatayı aynen raporla.
   QA kareleri: durağan karede ilk = orta = son kare (tek kare); açık + koyu tema. qa-yerel t değerleri KÜRESEL anlatım saniyesidir; bu
   sahnenin anlatımda saniyesi yoktur (`zaman.json` → `sahneler[]` dışında) → qa-yerel'i koşma.
2. Çakışma kapısı: `cd K && node araclar/cakisma-kapisi.mjs 02-04-ydt-temel-s2 --sahne 05-hyperframes-kapak-b --port 41333 --sunucu 41022`. Durağan sahnede
   `HATA sahne bulunamadı` (çıkış 2) beklenir (S1-VAR ölçümü 3/3): çıktıyı aynen rapora yaz, aracı değiştirme; çakışmayı karede gözle denetle.
3. Kanal katmanı açık ve koyu karede yerinde (huni v2 §7 madde 2): Read ile bak.
4. Metin taraması: `cd K && grep -rniE --include='*.html' --include='*.js' --include='*.py' --include='*.json' "tam ders|dakika" projeler/02-04-ydt-temel-s2/sahneler/05-hyperframes-kapak-b/ --exclude-dir=k` → boş (huni v2 §7 madde 3).
PNG'lere Read ile BAK: taşma, kesik yazı, üst üste binme, okunmaz kontrast, boş kare, 0–280 ve 1400–1920 boş mu, içerik x 960 sağına
taşıyor mu. En çok 4 düzeltme turu; geçmezse dur ve raporla.

## Rapor
`sahneler/05-hyperframes-kapak-b/RAPOR.md` (v1 RAPOR yedekte): olay listesi, kapı sonucu (son satırlar), bakılan kareler ve bulgu, agy koşu özeti yolu, açık noktalar.
Son mesajın en çok 10 satır: kapı çıkış kodu, kare yolları, agy koşu özeti, açık noktalar.
