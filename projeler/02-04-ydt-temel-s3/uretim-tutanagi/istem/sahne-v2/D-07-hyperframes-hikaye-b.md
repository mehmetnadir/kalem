# İstem D-V2-S3 — 02-04-ydt-temel-s3 sahne 07-hyperframes-hikaye-b (hikâye B) · huni v2 · 15.11.2026

MAKİNE: Linux x86_64 (srv21), kullanıcı sef. K=`/home/sef/01dev/_worktrees/kalem-0204` (git worktree, dal `sunucu/02-04-ydt-temel`).
Node `~/.nvm/versions/node/v24.22.2/bin`. Python `/usr/bin/python3 -I`. Skill `~/.claude/skills/motion-grafik-ders/`.
KURALLAR: Yalnız bu sahnenin dizinine yaz: `K/projeler/02-04-ydt-temel-s3/sahneler/07-hyperframes-hikaye-b/`. İstisna: paket köküne `hikaye-b.png` yazılır. Başka sahneye, `ortak/`a,
`BRIEF-S3.md`'ye, `zaman.json`'a, ana derse (`02-04-ydt-temel`, yalnız okunur) ve S1 paketine dokunma (eksik görürsen raporla).
Silme yok. v1 sahne kodunun yedeği hazır: `~/Silinecekler/2026-11-15-huni-v2/02-04-ydt-temel-s3/sahneler-v1/07-hyperframes-hikaye-b/` (V2-S3-C aldı);
eski PNG'ler `~/Silinecekler/2026-11-15-huni-v2/02-04-ydt-temel-s3/` altında; yerinde düzenle. mp4 ve `video.mp4` YOK; teslim tek
kare PNG'dir, tek kare yakalama serbest. git commit yok. Claude alt ajanı açma.
Kanca atlama bayrağı oluşturma (`/tmp/conductor-*`, `~/.conductor/*`); sözleşme kancası isterse `K/.claude/docs/sozlesme.md` dosyasına
1–2 satır ekle.

## Kod yolu (kapı ve doktrin)
Kod yazma kapısı 15 satırdan uzun kod dosyasını sana kapatır; bayrak açmaya çalışma. Yol: tasarımı sahne dizininde `SPEC.md` olarak
yaz (yazılacak dosyanın mutlak yolu, örnek sahnenin mutlak yolu ve oradan alınacak kalıp, olay listesi olay · kare/küresel sn · cümle
sözcüğü, yerleşim, ekran metni, kurallar, kabul ölçütü; tam kod YAZMA). Sonra
`agy-filo tek --rol kod --cwd /home/sef/01dev/_worktrees/kalem-0204 --zaman 25m -p "<SPEC.md mutlak yolunu oku ve uygula. Yalnız <dosya
mutlak yolu> dosyasını yaz. Başka dosyaya dokunma. Silme yok. Test, render, git yok.>"`. Kodu agy yazar; sen baştan sona okur, spec'e
uyuyor mu bakarsın, küçük düzeltmeyi Edit ile yaparsın, büyük düzeltmeyi agy'ye geri verirsin (en çok 2 tur). Tam kodu kendin yazıp
agy'ye birebir kopyalatmak YASAK. Kısa dosyalar (`calistir.sh`, `sayfa.html`) ve var olan dosyada küçük değişiklik Edit ile yapılır.

## Okuma
1. BAĞLAYICI: `/home/sef/01dev/dijital-anlatim/.claude/docs/huni-v2-standart.md` (§1, §2, §6 türevler, §7).
2. Skill `SKILL.md`, `references/kalem-hatti.md`, `stil-anayasasi.md`, `hareket-sozlugu.md`, `kliseler.md`.
3. Paket `K/projeler/02-04-ydt-temel-s3/`: `BRIEF-S3.md` ("Yerleşim" tablosu; "Hikâye karesi B" bölümü), `zaman.json` (`duragan` listesi, `cikti` `hikaye-b.png`; zaman çizelgesi dışı, kare 1;
   `sahneler[]`'e ekleme), `ortak/anlatim/senaryo.json` (`kadro`, `meta.canAlici`). Ses yok; anlatıma bağlı değil.
4. Başlangıç noktası: var olan v1 sahne kodu (`calistir.sh`, `uret.py`, `yardim.py`, `SPEC.md`, `RAPOR.md`).
5. v1 istemi (içerik kaynağı; yerleşim ve çağrı satırı GEÇERSİZ): `uretim-tutanagi/istem/sahne/D-07-hyperframes-hikaye-b.md` ve `uretim-tutanagi/hikaye-taslak.md` §3 (cevap: A — TARİFE).

## v2 yerleşim ve kanal katmanı (bütün sahnelerde AYNI piksel)
Künye ortak dosyadan GELMEZ: `ortak/kunye.js` ve sahnelerin `yardim.py` künyesi v1 HUD'dur (logo 48–144, ders adı 212, çip) ve v2 kanal
katmanını taşımaz. Aşağıdaki değerleri aynen kullan; ölçü icat etme. Değerler S1 ve S2 kısalarıyla aynı (`K/projeler/02-04-ydt-temel-s1/BRIEF-S1.md` "Kanal katmanı"). v1 HUD öğelerini (üst logo, 2 satır ders adı, çip) kaldır.

| Öğe | Değer |
|---|---|
| Üst boş | y 0–280 yalnız zemin |
| Kanal katmanı (kimlik `kanal`) | logo: tema logosu (açık `ortak/logo/yds-publishing-lacivert.svg`, koyu `yds-publishing-seffaf.svg`; sahnenin `assets/logo.svg` + `hf_tema.py` kalıbı), yükseklik 48, genişlik 193,5 (48 × 1920 / 476,3), resim x 53,2 (SVG iç boşluğu 68/1920 düşülür; görünür sol kenar x 60), y 291–339 · yazı `@ydspublishing` Lexend 700 42 px, renk `murekkep`, x 263, taban y 330 · ilk kareden son kareye opaklık 1; giriş, çıkış, uçuş, solma YOK · `__kalemKutu` türü `kunye`, ad `kunye:kanal` |
| Künye | y 360–450 tek satır: `Simple Present vs Present Continuous` Fredoka 700, x 60, taban y 420, boy ≤ 34 (rozetle x 960'a sığan en büyük, alt sınır 28) · rozet hapı `YDT · BASIC` Lexend 700 26 px, y 386–434, konu sonu + 20, dolgu `vurguDolgu`, yazı `pilMetin` · çip YOK |
| İçerik | y 460–1380, x 60–960; içerik yazısı ≥ 64 px (kanal ve künye standart §2 ölçüsünde) |
| Altyazı + karaoke `#altyazi` | y 1400–1550, x 60–960 (orta x 510), en çok 2 satır, Lexend 500 44 px (uzun parçada 40 → 36) |
| Alt boş | y 1570–1920 yalnız zemin; sağ şerit x 960–1080'e içerik girmez |

Ortak: tek vurgu sarı (açık temada hap dolgusu `#ffe066`, yazı `#1b2440`), doğru şık yeşil, kırmızı yok, emoji yok; satır ≤ 24 karakter;
9 sn'den uzun boş çerçeve yok; ekranda `İzmir` noktalı ve `7 pm`; tema çifti açık + koyu. Eski çağrı kalıbı ("tam ders"), süre sözü, QR,
"izle" düğmesi taklidi yok.


## Bu sahneye özel (hikâye B — soru + cevap düzeni)
- Standart §6: kanal katmanı + kural özeti + "Kaydet"; altyazı yok; y 1150–1380 yalnız boş zemin (boş kutu, çerçeve, ok çizme).
  Hikâye A'dan farklı düzen: soru sorulur, cevap karede açıktır (v1'de cevap gizliydi ve alt satır derse çağırıyordu; ikisi de kalkar).
- Bantlar (BRIEF "Hikâye karesi B"): 280–450 kanal katmanı + künye · 460–560 `Tarife mi, plan mı?` (Fredoka; 900 px'e sığan, üst sınır
  96) · 580–760 cümle kartı `The train to İzmir` / `leaves at 7 pm today.` (Fredoka 64) + tren + saat ikonu; `leaves` sarı altçizgi ·
  780–900 şıklar yan yana: `A` `TARİFE` doğru şık (yeşil çerçeve + kalem ✓) · `B` `PLAN` soluk (mürekkep çerçeve, alfa düşük); Fredoka 72 ·
  920–1060 kural özeti `Tren tarifeye uyar:` / `geniş zaman.` (Lexend 64; seste cümle 3) · 1070–1140 yer imi simgesi (SVG yol, emoji
  değil) + `Kaydet` (Fredoka 64) · 1150–1380 boş zemin · 1400–1920 boş.
- Aynı anda tek sarı vurgu (`leaves` altçizgisi); doğru şık yeşil; kırmızı yok.
- `calistir.sh`: `--tema acik` paket köküne `hikaye-b.png`; `--tema koyu` `k/koyu/hikaye-b-koyu.png`.

## Doğrula (zorunlu, geçmeden bitirme)
1. Tek kare: `bash calistir.sh --tema acik` ve `bash calistir.sh --tema koyu` → `hikaye-b.png` (paket kökü) + `k/koyu/hikaye-b-koyu.png` (1080×1920; `ffprobe` ile boyut). QA kareleri
   (ilk, orta, son kare) tek karede aynıdır: açık + koyu PNG. Bu sahne zaman çizelgesinde değildir; qa-yerel t değerleri (KÜRESEL anlatım
   saniyesi: `zaman.json` t_bas + sahne içi saniye) bu sahneye uygulanmaz, qa-yerel'i koşma.
2. Çakışma kapısı: `cd K && node araclar/cakisma-kapisi.mjs 02-04-ydt-temel-s3 --sahne 07-hyperframes-hikaye-b --port 41333 --sunucu 41022`. Kapı sahneyi
   `zaman.json` → `sahneler[]` içinde arar; bu sahne bilerek dışında. Çıkış 2 (ölçülemedi) araç sınırıdır: aracı değiştirme, çıktıyı
   RAPOR'a aynen yaz. Çıkış 0 ya da 1 ise 0 uyarı şartı geçerli. Port doluysa 1 dk bekle, yeniden koş.
3. Kanal katmanı (standart §7.2): açık ve koyu PNG'de logo + `@ydspublishing` görünür, konum x 60, y 291–339.
4. Metin taraması: `grep -rniE "tam ders|dakika" K/projeler/02-04-ydt-temel-s3/sahneler/07-hyperframes-hikaye-b/proje` → sonuç yok.
5. PNG'leri Read ile AÇ: taşma, kesik yazı, üst üste binme, kontrast, boş alan; 0–280 boş mu; içerik x 960'ı aşıyor mu; altyazı yok mu.
   En çok 4 düzeltme turu; geçmezse dur, raporla.
Betik tek kare yakalayamıyorsa dur ve hatayı aynen raporla; aracı değiştirme.

## Rapor
`sahneler/07-hyperframes-hikaye-b/RAPOR.md`: öğe listesi (öğe · y bandı · yazı boyu), kanal katmanı konum ölçümü, kapı sonucu (son satırlar), bakılan
kareler ve bulgu, agy koşu özeti yolu, açık noktalar. Son mesajın en çok 10 satır.
