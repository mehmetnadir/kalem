# İstem D-S2-V2 — 02-04-ydt-temel-s2 sahne 01-hyperframes-kapak (huni v2) · 15.11.2026

MAKİNE: Linux x86_64 (srv21), kullanıcı sef. K=`/home/sef/01dev/_worktrees/kalem-0204` (git worktree, dal `sunucu/02-04-ydt-temel`).
D=`/home/sef/01dev/dijital-anlatim`. Node `~/.nvm/versions/node/v24.22.2/bin`. Python `/usr/bin/python3 -I`. Skill `~/.claude/skills/motion-grafik-ders/`.
KURALLAR: Yalnız bu sahnenin dizinine yaz: `K/projeler/02-04-ydt-temel-s2/sahneler/01-hyperframes-kapak/`. İstisna: paket kökü `kapak-a.png` ve `kapak.png` (kapak A, tek kare PNG; eskileri V2 yedeğinde). Başka sahneye, `ortak/`a (istisna yukarıda yazılıysa yalnız o
dosya), `BRIEF-S2.md`'ye, `zaman.json`'a, ana derse (`02-04-ydt-temel`), S1 ve S3 paketlerine dokunma (eksik görürsen raporla).
Silme yok (`~/Silinecekler/2026-11-15-huni-v2/` altına taşı). mp4 render YOK: `calistir.sh`'ı yalnız `ONIZLE_YALNIZ=1` ile koş.
git commit yok. Claude alt ajanı açma.
Kanca atlama bayrağı OLUŞTURMA (/tmp/conductor-*, ~/.conductor/*). Sözleşme kancası isterse K/.claude/docs/sozlesme.md
dosyasına 1–2 satır EKLE (tek istisna).
Önce yedek: `mkdir -p ~/Silinecekler/2026-11-15-huni-v2/02-04-ydt-temel-s2/sahneler/ && cp -a K/projeler/02-04-ydt-temel-s2/sahneler/01-hyperframes-kapak ~/Silinecekler/2026-11-15-huni-v2/02-04-ydt-temel-s2/sahneler/` (kopya, taşıma değil); sonra yerinde düzenle.

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
3. Paket: `K/projeler/02-04-ydt-temel-s2/BRIEF-S2.md` ("Yerleşim" tablosu ve altındaki kanal katmanı notu; "Sahneler" tablosunda 01. satır (0.00–2.84, 97 kare, kanca); "Sahne içeriği" 0,00–2,84 satırları; "Kapak A" bölümü; `sozcukler.json` cümle 1: `Genel` 1,00 · `şu` 2,12 · `mı?` 2,52),
   `zaman.json`, `ortak/anlatim/senaryo.json`, `uretim-tutanagi/V2-C-RAPOR.md`.
4. İçerik ve olay kaynağı: bu sahnenin v1 kodu, `SPEC.md` ve `RAPOR.md` (`K/projeler/02-04-ydt-temel-s2/sahneler/01-hyperframes-kapak/`; yedekten sonra). İçerik korunur, yerleşim v2'ye çekilir.
5. Kapak A yöntemi: `K/projeler/02-04-ydt-temel-s1/uretim-tutanagi/S1-VAR-RAPOR.md` son 3 satır (S1-KAPAK-A).

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
`sahneler/01-hyperframes-kapak/` içinde v1 ile aynı dosya yapısı. Kurallar: tek sütun; yazı tabanı ≥ 64 mantıksal px (kanal katmanı ve künye hariç);
satır ≤ 24 karakter; tek vurgu sarı (rozet hapı künye öğesidir, vurgu sayılmaz); kırmızı yok, emoji yok; altyazı + karaoke alt bantta (1400–1550; `ortak/anlatim/altyazi.json`); tema çifti açık + koyu;
sarı hap açık temada dolgu `#ffe066`, yazı `#1b2440`; 9 sn'den uzun boş çerçeve yok; ekranda `T-shirt` tireli (seste `T shirt`).
Ekranda `Tam ders` sözü, süre sözü (`dakika`, `dk`), QR, oynat ya da "izle" düğmesi taklidi YOK (huni v2 §1 kural 4–5).
`calistir.sh`: `[ -d /opt/homebrew/bin ] && export PATH="/opt/homebrew/bin:$PATH"`, yük `Y=$(yuk1)`, yakalama `1080 1920`.

Bu sahneye özel (kanca, 0–4 sn kuralı; ilk söz 1,00):
- İçerik v1 ile aynı (BRIEF-S2 0,00–2,84 satırları). Değişen yerleşim: başlık `GENEL` / `≠ ŞU AN` (en geniş satır ≤ 900 px, üst sınır 190 px;
  motor ölçer), figür, mont, tişört ve etiketler (`wears`, `is wearing`, Caveat ≥ 72) 460–1380 içinde.
- Kanal katmanı kare 0'dan. Künye satırında kare 0'da yalnız rozet; konu adı uçuşla gelir: 2,24–2,84 başlık küçülerek künye satırındaki
  konu adına iner, figür ve iki nesne solar, soru satırı `Genel mi, şu an mı?` Caveat 72, sol x 60, taban y 530 (sahne 01 son karesi = sahne 02 kare 0; iki istemde aynı değer) kalemle yazılır.
- `≠` kalem hareketi 0,30–0,80 (hapın içinde). Cümle 1 yalnız altyazı bandında sözcük zamanlı.
- v1'deki `Hook` çipi kalkar.
- Kapak A: sahne `proje` kopyasında yalnız CSS `#altyazi{display:none}`, `hyperframes snapshot --at 0.9` (kare 27; `≠` bitmiş). Açık tema →
  paket kökü `kapak-a.png` + kopyası `kapak.png` (`cmp` aynı); koyu → `sahneler/01-hyperframes-kapak/k/koyu/kapak-a-koyu.png`. Altyazıyı piksel boyayarak
  ya da kırparak silme. `calistir.sh` render dalının kare 27 satırı da aynı kareyi altyazısız yazacak biçimde kalır.
- Sahne kare sayısı 97 (içerik 85 + geçiş 12).

## Doğrula (zorunlu, geçmeden bitirme)
1. QA kareleri: `cd K && bash araclar/qa-yerel.sh 02-04-ydt-temel-s2 01-hyperframes-kapak 0.0,1.5,2.8 0.9 --hazirla`
   t değerleri KÜRESEL anlatım saniyesidir (0,00 + sahne içi saniye; sahne içi saniye DEĞİL): ilk kare 0.0, orta 1.5, son kare 2.8;
   koyu tema 0.9. Çıkış kodu 0 olmalı.
2. Çakışma kapısı: `cd K && node araclar/cakisma-kapisi.mjs 02-04-ydt-temel-s2 --sahne 01-hyperframes-kapak --port 41333 --sunucu 41022` → 0 uyarı
   (huni v2 §7 madde 1).
3. Kanal katmanı ilk, orta ve son karede aynı konumda görünür (huni v2 §7 madde 2): üç kareye Read ile bak.
4. Metin taraması: `cd K && grep -rniE --include='*.html' --include='*.js' --include='*.py' --include='*.json' "tam ders|dakika" projeler/02-04-ydt-temel-s2/sahneler/01-hyperframes-kapak/ --exclude-dir=k` → boş (huni v2 §7 madde 3).
qa-yerel ya da kapı dikey (1080×1920) paketi ölçemiyorsa dur ve hatayı aynen raporla; aracı değiştirme.
Üretilen PNG'lere (`sahneler/01-hyperframes-kapak/k/`, `k/koyu/`) Read ile BAK: taşma, kesik yazı, üst üste binme, okunmaz kontrast, boş kare,
altyazıyla çakışma, 0–280 ve 1570–1920 boş mu, içerik x 960 sağına taşıyor mu. En çok 4 düzeltme turu; geçmezse dur ve raporla.
Ek: `kapak-a.png`, `kapak.png`, `kapak-a-koyu.png` Read ile bak (altyazı yok, kanal katmanı var); `file` ile 1080×1920.

## Rapor
`sahneler/01-hyperframes-kapak/RAPOR.md` (v1 RAPOR yedekte): olay listesi, kapı sonucu (son satırlar), bakılan kareler ve bulgu, agy koşu özeti yolu, açık noktalar.
Son mesajın en çok 10 satır: kapı çıkış kodu, kare yolları, agy koşu özeti, açık noktalar.
