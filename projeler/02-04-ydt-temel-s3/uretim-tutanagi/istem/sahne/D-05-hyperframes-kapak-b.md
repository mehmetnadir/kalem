# İstem D-S3 — 02-04-ydt-temel-s3 sahne 05-hyperframes-kapak-b · 15.11.2026

MAKİNE: Linux x86_64 (srv21), kullanıcı sef. K=`/home/sef/01dev/_worktrees/kalem-0204` (git worktree, dal `sunucu/02-04-ydt-temel`).
Node `~/.nvm/versions/node/v24.22.2/bin`. Python `/usr/bin/python3 -I`. Skill `~/.claude/skills/motion-grafik-ders/`.
KURALLAR: Yalnız bu sahnenin dizinine yaz: `K/projeler/02-04-ydt-temel-s3/sahneler/05-hyperframes-kapak-b/`. İstisna: `calistir.sh` paket köküne yalnız `kapak-b.png` yazar (tek kare PNG; sahnenin teslimi budur). Başka sahneye, `ortak/`a,
`BRIEF-S3.md`'ye, `zaman.json`'a, ana derse (`02-04-ydt-temel`), S1 paketine (`02-04-ydt-temel-s1`, yalnız okunur) ve dikey pakete
dokunma (eksik görürsen raporla). Silme yok (`~/Silinecekler/2026-11-15-0204/` altına taşı). mp4 render YOK: `calistir.sh`'ı yalnız
`ONIZLE_YALNIZ=1` ile koş. git commit yok. Claude alt ajanı açma.
Kanca atlama bayrağı OLUŞTURMA (/tmp/conductor-*, ~/.conductor/*). Durdurma kancası sözleşme satırı isterse K/.claude/docs/sozlesme.md
dosyasına 1–2 satır EKLE (tek istisna).

## Kod yolu (kapı ve doktrin)
Kod yazma kapısı 15 satırdan uzun kod dosyasını sana kapatır; bayrak açmaya çalışma. Yol: tasarımı sahne dizininde `SPEC.md` olarak
yaz (yazılacak dosyanın mutlak yolu, örnek sahnenin mutlak yolu ve oradan alınacak kalıp, olay listesi olay · kare/küresel sn · cümle
sözcüğü, yerleşim, ekran metni, kurallar, kabul ölçütü; tam kod YAZMA). Sonra
`agy-filo tek --rol kod --cwd /home/sef/01dev/_worktrees/kalem-0204 --zaman 25m -p "<SPEC.md mutlak yolunu oku ve uygula. Yalnız <dosya
mutlak yolu> dosyasını yaz. Başka dosyaya dokunma. Silme yok. Test, render, git yok.>"`. Kodu agy yazar; sen baştan sona okur, spec'e
uyuyor mu bakarsın, küçük düzeltmeyi Edit ile yaparsın, büyük düzeltmeyi agy'ye geri verirsin (en çok 2 tur). Tam kodu kendin yazıp
agy'ye birebir kopyalatmak YASAK (kapıyı vekille dolanmaktır). Kısa dosyalar (`calistir.sh`, `sayfa.html`) Edit ile yazılabilir.
Örnek sahnedeki dosyaları kopyalayıp küçük Edit'le uyarlamak serbesttir (15+ satırlık yeni gövde gerekiyorsa SPEC.md + agy yolu).

## Okuma
1. Skill `SKILL.md`, `references/kalem-hatti.md`, `stil-anayasasi.md`, `hareket-sozlugu.md`, `kliseler.md`, `soru-ani.md` (soru sahnesiyse).
2. Paket: `K/projeler/02-04-ydt-temel-s3/BRIEF-S3.md` (giriş, "Sahneler" tablosunda kapak B satırı: `| — | 05-hyperframes-kapak-b | HyperFrames | zaman çizelgesi dışı | 1 (kapak-b.png) |`; "Kapak B ve C" bölümü (B satırı); ortak öğeler için "Kapak A"),
   `zaman.json` (`duragan` listesi: zaman çizelgesi dışı, kare 1, `cikti` `kapak-b.png`), `ortak/anlatim/senaryo.json` + `sozcukler.json` + `baslar.json` + `altyazi.json` (anlatım yok: kapak B sese bağlı değildir; metin `uretim-tutanagi/kapak-taslak.md` §2 (B)),
   `uretim-tutanagi/senaryo-taslak.md` §2 (görsel fikir), `kapak-taslak.md`,
   `hikaye-taslak.md`, `uretim-tutanagi/S3-duzeltme.md` (jüri düzeltmeleri: taslakla çelişirse düzeltme geçerli),
   `K/projeler/present-continuous-dikey/BRIEF-DIKEY.md` §0 ve §2–§3 (Nadir'in dikey bulguları, HUD ölçüleri).
3. İçerik kaynağı (ana ders yatay; içerik, çizim ve olay sırası; yerleşim DEĞİL): `/home/sef/01dev/_worktrees/kalem-0204/projeler/02-04-ydt-temel/sahneler/06-hyperframes-soru1/` (soru dili, öğretmen figürü işaret pozu) ve çizimler için `/home/sef/01dev/_worktrees/kalem-0204/projeler/02-04-ydt-temel/sahneler/05-canvas-ornek3/` (tren, saat) (kod + RAPOR.md).
4. Dikey örnek (aynı dersin bitmiş kısası S1; aynı motor; dosya yapısı, calistir.sh kalıbı, 1080×1920 kurulum): `/home/sef/01dev/_worktrees/kalem-0204/projeler/02-04-ydt-temel-s1/sahneler/05-hyperframes-kapak-b/`.
   Örneğin `calistir.sh` dosyası `ONIZLE_YALNIZ` satırını zaten taşır. S1 içeriğini (ev, bavul, `YAŞIYORUM`, `I live`, S1 zamanları) taşıma.

## Yaz
`sahneler/05-hyperframes-kapak-b/` içinde örnekle aynı dosya yapısı. Kurallar: tek sütun, kenar 48, içerik bandı 352–1392 (BRIEF-DIKEY §2); yazı tabanı
≥ 64 mantıksal px; satır ≤ 24 karakter; tek vurgu sarı (temaya göre), doğru şık yeşil, kırmızı yok, emoji yok; sabit px yerine oran ya da
BRIEF-DIKEY ölçüsü; altyazı + karaoke alt bantta (1400–1536); künye ve tema çifti (açık + koyu) `ortak/kunye.js` ile (çip
`KUNYE.cipler["05-hyperframes-kapak-b"]`); sarı hap açık temada dolgu `RENK.vurguDolgu` (`#ffe066`), yazı `RENK.pilMetin` (`#1b2440`); 9 sn'den uzun boş
çerçeve yok; ekranda "İzmir" noktalı (seste "Izmir"); ekranda `7 pm` (seste *seven p.m.*); "kanal" sözü, QR ve süre "6 dk" yok.
`calistir.sh`: `[ -d /opt/homebrew/bin ] && export PATH="/opt/homebrew/bin:$PATH"`, yük `Y=$(yuk1)`, yakalama `1080 1920`.

Bu sahneye özel:
- Tek kare, durağan, ses yok; videoya girmez. Tarif BRIEF-S3 "Kapak B ve C" (B) + `uretim-tutanagi/kapak-taslak.md` §1–§3 (B): rozet
  `YDT · BASIC`; başlık `NEDEN -ING` / `YOK?` (`YOK?` sarı hap; iki satır aynı boy, 952 px'e sığan en büyük değer, üst sınır 190 px).
- Sahne bandı 864–1344: ortada tren + saat (kollar yedide, rakamsız), trenin üstünde el çizimi sarı `?`; altında tek kart
  `The train leaves …` (Fredoka 72), `leaves` altında sarı altçizgi; sağda öğretmen figürü (`kadro.ogretmen`) trene işaret eder.
- Can alıcı `canAlici[1]`, kısa kod `leaves` (kartın altçizgili sözcüğü; S3-duzeltme madde 5). Cevap karede yazmaz.
- `-ING` Latin büyük I: başlığı elle büyük harf yaz, `text-transform` kullanma (Türkçe yerelde `-İNG` olur). Logo sol alt; 1344–1920 boş.
- Çip gizli (kapak A gibi); altyazı ve karaoke yok (Yaz kuralındaki altyazı maddesi geçersiz). mp4 yok; tek kare PNG serbest (teslim
  PNG'dir). `calistir.sh` (S1 örneği kalıbı): `--tema acik` paket köküne `kapak-b.png`, `--tema koyu` `k/koyu/kapak-b-koyu.png`.
- Zaman çizelgesine girmez: `zaman.json` → `duragan` listesi; `sahneler[]`'e ekleme.

## Doğrula (zorunlu, geçmeden bitirme)
`qa-yerel.sh`, `cakisma-kapisi.mjs` ve `sahne-kare.mjs` sahneyi `zaman.json` → `sahneler[]` içinde arar; bu sahne bilerek dışındadır
ve anlatım zamanı yoktur. Bu yüzden qa-yerel'i koşma. Doğrulama: `bash calistir.sh --tema acik` ve `bash calistir.sh --tema koyu` →
`kapak-b.png` (paket kökü) + `k/koyu/kapak-b-koyu.png` (1080×1920; `ffprobe` ile boyut). Betik tek kare yakalayamıyorsa dur ve hatayı
aynen raporla; aracı değiştirme.
qa-yerel t değerleri KÜRESEL anlatım saniyesidir (`zaman.json` t_bas + sahne içi saniye), sahne içi saniye DEĞİLDİR.
Üretilen PNG'lere (`sahneler/05-hyperframes-kapak-b/k/`, `k/koyu/`) Read ile BAK: taşma, kesik yazı, üst üste binme, okunmaz kontrast, boş kare,
alt bantta altyazıyla çakışma, 1536 altı boş mu. En çok 4 düzeltme turu; geçmezse dur ve raporla.

## Rapor
`sahneler/05-hyperframes-kapak-b/RAPOR.md`: olay listesi, kapı sonucu (son satırlar), bakılan kareler ve bulgu, agy koşu özeti yolu, açık noktalar.
Son mesajın en çok 10 satır: kapı çıkış kodu, kare yolları, agy koşu özeti, açık noktalar.
