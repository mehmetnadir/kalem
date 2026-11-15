# İstem D-V2-S3 — 02-04-ydt-temel-s3 sahne 08-hyperframes-kaydet (kaydet, YENİ) · huni v2 · 15.11.2026

MAKİNE: Linux x86_64 (srv21), kullanıcı sef. K=`/home/sef/01dev/_worktrees/kalem-0204` (git worktree, dal `sunucu/02-04-ydt-temel`).
Node `~/.nvm/versions/node/v24.22.2/bin`. Python `/usr/bin/python3 -I`. Skill `~/.claude/skills/motion-grafik-ders/`.
KURALLAR: Yalnız bu sahnenin dizinine yaz: `K/projeler/02-04-ydt-temel-s3/sahneler/08-hyperframes-kaydet/` (yeni dizin; sen açarsın).
Başka sahneye, `ortak/`a, `BRIEF-S3.md`'ye, `zaman.json`'a, ana derse (`02-04-ydt-temel`) ve S1 paketine dokunma (eksik görürsen
raporla). Silme yok. mp4 render YOK: `calistir.sh`'ı yalnız `ONIZLE_YALNIZ=1` ile koş. git commit yok. Claude alt ajanı açma.
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
1. BAĞLAYICI: `/home/sef/01dev/dijital-anlatim/.claude/docs/huni-v2-standart.md` (§1, §2, §3 kaydet sahnesi, §4 kaydet kalıbı, §7).
2. Skill `SKILL.md`, `references/kalem-hatti.md`, `stil-anayasasi.md`, `hareket-sozlugu.md`, `kliseler.md`.
3. Paket `K/projeler/02-04-ydt-temel-s3/`: `BRIEF-S3.md` ("Yerleşim" tablosu; "Sahneler" 3. satırı `| 3 Kaydet | 08-hyperframes-kaydet
   (YENİ) | HyperFrames | 15.99–21.33 | 172 | öğretmen |`; "Sahne içeriği" 15,99–21,33 satırları), `zaman.json` (bu sahne 15,99–21,33
   küresel sn, 172 kare = 160 içerik + 12 geçiş; `sahneler[]` 3. sıra), `ortak/anlatim/senaryo.json` + `sozcukler.json` + `baslar.json` +
   `altyazi.json` + `METIN.md` (cümle 4, öğretmen, 16,54–21,33: `Bu,` 16,54 · `üç` 17,06 · `farktan` 17,22 · `yalnız` 17,74 · `biri.`
   18,22 · `Bir` 18,77 · `arkadaşına` 19,01 · `gönder;` 19,53 · `o` 20,33 · `da` 20,41 · `karıştırıyor.` 20,53). Olay söylendiği anda gelir.
4. Dosya yapısı örneği (zaman çizelgesi sahnesi, aynı motor; `calistir.sh`, `uret.py`, `yardim.py`, `olay.py` kalıbı; içeriğini taşıma):
   v1 çağrı sahnesinin yedeği `~/Silinecekler/2026-11-15-huni-v2/02-04-ydt-temel-s3/sahneler-v1/03-hyperframes-cta/` (canlı
   `sahneler/03-hyperframes-cta/` başka oturumda değişiyor; ona bakma). Çizimler: `sahneler-v1/02-hyperframes-ornek/cizim` (tren, bilet).

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


## Bu sahneye özel (kaydet, 15,99–21,33)
- Kare 0'dan: kanal katmanı + künye (`Simple Present vs Present Continuous` + rozet) tam; içerik bandı boş zemin.
- `Bu,` (16,54) çapasında kural özeti kartı kalemle çizilir (çerçeve ≤ 0,5 sn; y ≈ 560–900, x 60–960). Kart içinde tek cümle, 2 satır:
  `Tarife → leaves,` / `plan → am going.` (Fredoka 72; `leaves`, `am going` İngilizce). Tek sarı vurgu `leaves` (sarı hap). Satır başında
  küçük tren (satır 1) ve küçük bilet (satır 2) ikonu. `→` glifi fontta yoksa kalemle çiz (v1 `≠` kalıbı).
- Kart çizildikten sonra hiç kımıldamaz (standart §3: en az 2 sn sabit; burada ≈ 4,5 sn).
- `Bir` (18,77) çapasında kartın altında (y ≈ 960–1100) yer imi simgesi (SVG yol, kalemle çizilir ≈ 0,4 sn; emoji DEĞİL) + `Kaydet`
  (Fredoka 72). `gönder;` (19,53) çapasında yer imi sarıyla dolar; aynı anda `leaves` hapı mürekkep altçizgiye döner (aynı anda tek sarı).
- Seste "Bir arkadaşına gönder" geçer; ekranda yalnız `Kaydet` yazar (standart §3); paylaş simgesi ekleme.
- Altyazı `altyazi.json`'dan küresel t ile (cümle 4: 16,54–18,62 ve 18,77–21,41); 1400–1550 bandında, x 60–960. İkinci parça 21,33'te
  sahne sınırını 0,08 sn aşar: bu sahnede 21,33'e kadar göster.
- Son kare (21,30) = kart + yer imi + `Kaydet` tam; birleştirme geçişi buradan çağrı sahnesine gider.

## Doğrula (zorunlu, geçmeden bitirme)
1. QA kareleri: `cd K && bash araclar/qa-yerel.sh 02-04-ydt-temel-s3 08-hyperframes-kaydet 15.99,18.66,21.3 19.6 --hazirla` — açık: ilk
   kare 15,99, orta 18,66, son kare 21,30; koyu 19,60. Çıkış kodu 0. qa-yerel t değerleri KÜRESEL anlatım saniyesidir (`zaman.json` t_bas
   15,99 + sahne içi saniye), sahne içi saniye DEĞİLDİR.
2. Çakışma kapısı: `cd K && node araclar/cakisma-kapisi.mjs 02-04-ydt-temel-s3 --sahne 08-hyperframes-kaydet --port 41333 --sunucu 41022`
   → 0 uyarı. Port doluysa (başka sahne oturumu) 1 dk bekle, yeniden koş.
3. Kanal katmanı (standart §7.2): üç açık karede ve koyu karede logo + `@ydspublishing` görünür, konum aynı (x 60, y 291–339).
4. Metin taraması: `grep -rniE "tam ders|dakika" K/projeler/02-04-ydt-temel-s3/sahneler/08-hyperframes-kaydet/proje` → sonuç yok.
5. Kareleri (`k/`, `k/koyu/`) Read ile AÇ: taşma, kesik yazı, üst üste binme, kontrast, boş kare; 0–280 ve 1570–1920 boş mu; içerik
   x 960'ı aşıyor mu; altyazı 1400–1550 içinde mi; yer imi emoji değil, SVG mi. En çok 4 düzeltme turu; geçmezse dur, raporla.
qa-yerel ya da kapı paketi ölçemiyorsa dur ve hatayı aynen raporla; aracı değiştirme.

## Rapor
`sahneler/08-hyperframes-kaydet/RAPOR.md`: olay listesi (olay · küresel sn · sözcük), kanal katmanı konum ölçümü, kartın sabit kaldığı
aralık, qa ve çakışma kapısı sonucu (son satırlar), bakılan kareler ve bulgu, agy koşu özeti yolu, açık noktalar. Son mesajın en çok
10 satır.

## Şef notu (15.11 19:00)
Seste "Bir arkadaşına gönder; o da karıştırıyor." deniyor. Ekranda bu sahnede iki eylem birlikte görünür: büyük "Arkadaşına gönder" (gönder simgesi, SVG) ve yanında küçük "Kaydet" (yer imi simgesi, SVG). Ses ile ekran çelişmez.
