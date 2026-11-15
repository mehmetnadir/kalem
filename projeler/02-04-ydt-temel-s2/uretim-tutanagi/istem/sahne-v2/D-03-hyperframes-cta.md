# İstem D-S2-V2 — 02-04-ydt-temel-s2 sahne 03-hyperframes-cta (huni v2) · 15.11.2026

MAKİNE: Linux x86_64 (srv21), kullanıcı sef. K=`/home/sef/01dev/_worktrees/kalem-0204` (git worktree, dal `sunucu/02-04-ydt-temel`).
D=`/home/sef/01dev/dijital-anlatim`. Node `~/.nvm/versions/node/v24.22.2/bin`. Python `/usr/bin/python3 -I`. Skill `~/.claude/skills/motion-grafik-ders/`.
KURALLAR: Yalnız bu sahnenin dizinine yaz: `K/projeler/02-04-ydt-temel-s2/sahneler/03-hyperframes-cta/`. İstisna: `ortak/kapak/ana-kapak.png` ve `ortak/kapak/ana-kapak-koyu.png` (yalnız bu iki kopya). Başka sahneye, `ortak/`a (istisna yukarıda yazılıysa yalnız o
dosya), `BRIEF-S2.md`'ye, `zaman.json`'a, ana derse (`02-04-ydt-temel`), S1 ve S3 paketlerine dokunma (eksik görürsen raporla).
Silme yok (`~/Silinecekler/2026-11-15-huni-v2/` altına taşı). mp4 render YOK: `calistir.sh`'ı yalnız `ONIZLE_YALNIZ=1` ile koş.
git commit yok. Claude alt ajanı açma.
Kanca atlama bayrağı OLUŞTURMA (/tmp/conductor-*, ~/.conductor/*). Sözleşme kancası isterse K/.claude/docs/sozlesme.md
dosyasına 1–2 satır EKLE (tek istisna).
Önce yedek: `mkdir -p ~/Silinecekler/2026-11-15-huni-v2/02-04-ydt-temel-s2/sahneler/ && cp -a K/projeler/02-04-ydt-temel-s2/sahneler/03-hyperframes-cta ~/Silinecekler/2026-11-15-huni-v2/02-04-ydt-temel-s2/sahneler/` (kopya, taşıma değil); sonra yerinde düzenle.

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
3. Paket: `K/projeler/02-04-ydt-temel-s2/BRIEF-S2.md` ("Yerleşim" tablosu ve altındaki kanal katmanı notu; "Sahneler" tablosunda 4. sıradaki satır (`03-hyperframes-cta`, 22.75–29.41, 230 kare, çağrı); "Sahne içeriği" 22,75–29,41 satırları; `sozcukler.json` + `altyazi.json` cümle 4 (23,30–28,41, `konusan` `ogrenci`)),
   `zaman.json`, `ortak/anlatim/senaryo.json`, `uretim-tutanagi/V2-C-RAPOR.md`.
4. Dosya yapısı: bu sahnenin v1 kodu (`K/projeler/02-04-ydt-temel-s2/sahneler/03-hyperframes-cta/`; yedekten sonra). v1 içeriği (`üç farktan biri`, `Tam ders:`, ders bandı, saat,
   `dört buçuk dakikada`, mont/tişört kuyruğu) TAMAMEN çıkar; yalnız dosya yapısı, `calistir.sh`, altyazı ve kanal kalıbı kalır.
5. `D/.claude/docs/kapak-standardi.md` (ana kapak dosyaları).

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
`sahneler/03-hyperframes-cta/` içinde v1 ile aynı dosya yapısı. Kurallar: tek sütun; yazı tabanı ≥ 64 mantıksal px (kanal katmanı ve künye hariç);
satır ≤ 24 karakter; tek vurgu sarı (rozet hapı künye öğesidir, vurgu sayılmaz); kırmızı yok, emoji yok; altyazı + karaoke alt bantta (1400–1550; `ortak/anlatim/altyazi.json`); tema çifti açık + koyu;
sarı hap açık temada dolgu `#ffe066`, yazı `#1b2440`; 9 sn'den uzun boş çerçeve yok; ekranda `T-shirt` tireli (seste `T shirt`).
Ekranda `Tam ders` sözü, süre sözü (`dakika`, `dk`), QR, oynat ya da "izle" düğmesi taklidi YOK (huni v2 §1 kural 4–5).
`calistir.sh`: `[ -d /opt/homebrew/bin ] && export PATH="/opt/homebrew/bin:$PATH"`, yük `Y=$(yuk1)`, yakalama `1080 1920`.

Bu sahneye özel (çağrı, huni v2 §3 sahne 4; ses ÖĞRENCİ: "Bitmedi, gel. Dersin tamamı YDS Publishing YouTube kanalında."):
- ÖNCE ana kapak: `cp -a K/projeler/02-04-ydt-temel/kapak.png K/projeler/02-04-ydt-temel-s2/ortak/kapak/ana-kapak.png` ve
  `cp -a K/projeler/02-04-ydt-temel/kapak-koyu.png K/projeler/02-04-ydt-temel-s2/ortak/kapak/ana-kapak-koyu.png`. Kaynak dosyalardan biri yoksa DUR: kod yazma,
  `RAPOR.md`'ye ve son mesaja "ana kapak bekliyor" yaz (V2-S2-C ölçümü 15.11: ikisi de yoktu).
- 22,75 kare 0: kanal katmanı + künye; içerik boş.
- `Bitmedi,` 23,30: giriş sözü `Bitmedi, gel.` Fredoka 700 ≈ 96 px, x 60, y ≈ 480–600, sözcük zamanlı (`gel.` 24,26).
- `Dersin` 24,89: ana dersin kapağı 16:9 kart, 900×506, x 60–960, y 627–1133 (standart "≈ 920×518, y ≈ 620–1140"; sağ 960–1080 platform
  arayüzü altında kaldığı için 900). İnce mürekkep çerçeve, köşe 24, yumuşak giriş (0,4 sn). Tema uyumlu: açık `ana-kapak.png`, koyu
  `ana-kapak-koyu.png` (iki `<image>` + tema CSS'iyle görünürlük; `ortak/hf_tema.py` yalnız logoyu değiştirir).
- `YDS` 26,17: kartın altında (y ≈ 1170–1250) `@ydspublishing` sarı hap (tek vurgu) + ` · YouTube` Lexend 700 mürekkep.
- 28,41–29,41 durgun kuyruk; kapak kartı ve satırlar yerinde.
- YASAK: `Tam ders`, süre sözü, ders bandı, saat, oynat üçgeni, "izle" düğmesi taklidi, YouTube logosu, ekranda "kanal" sözü.
- Altyazı cümle 4 (2 parça: 23,30–24,74 · 24,89–28,41), öğrenci sesi. v1'deki `Full lesson` çipi kalkar.
- Sahne kare sayısı 230 (içerik 200 + kuyruk 30).

## Doğrula (zorunlu, geçmeden bitirme)
1. QA kareleri: `cd K && bash araclar/qa-yerel.sh 02-04-ydt-temel-s2 03-hyperframes-cta 22.75,26.5,29.35 28.5 --hazirla`
   t değerleri KÜRESEL anlatım saniyesidir (22,75 + sahne içi saniye; sahne içi saniye DEĞİL): ilk kare 22.75, orta 26.5, son kare 29.35;
   koyu tema 28.5. Çıkış kodu 0 olmalı.
2. Çakışma kapısı: `cd K && node araclar/cakisma-kapisi.mjs 02-04-ydt-temel-s2 --sahne 03-hyperframes-cta --port 41333 --sunucu 41022` → 0 uyarı
   (huni v2 §7 madde 1).
3. Kanal katmanı ilk, orta ve son karede aynı konumda görünür (huni v2 §7 madde 2): üç kareye Read ile bak.
4. Metin taraması: `cd K && grep -rniE --include='*.html' --include='*.js' --include='*.py' --include='*.json' "tam ders|dakika" projeler/02-04-ydt-temel-s2/sahneler/03-hyperframes-cta/ --exclude-dir=k` → boş (huni v2 §7 madde 3).
qa-yerel ya da kapı dikey (1080×1920) paketi ölçemiyorsa dur ve hatayı aynen raporla; aracı değiştirme.
Üretilen PNG'lere (`sahneler/03-hyperframes-cta/k/`, `k/koyu/`) Read ile BAK: taşma, kesik yazı, üst üste binme, okunmaz kontrast, boş kare,
altyazıyla çakışma, 0–280 ve 1570–1920 boş mu, içerik x 960 sağına taşıyor mu. En çok 4 düzeltme turu; geçmezse dur ve raporla.
Ek: son karede ana kapak kartı görünür (huni v2 §7 madde 5); kapak dosyası yoksa sahne "bekliyor" kalır.

## Rapor
`sahneler/03-hyperframes-cta/RAPOR.md` (v1 RAPOR yedekte): olay listesi, kapı sonucu (son satırlar), bakılan kareler ve bulgu, agy koşu özeti yolu, açık noktalar.
Son mesajın en çok 10 satır: kapı çıkış kodu, kare yolları, agy koşu özeti, açık noktalar.
