# İstem D-V2-S3 — 02-04-ydt-temel-s3 sahne 02-hyperframes-ornek (değer) · huni v2 · 15.11.2026

MAKİNE: Linux x86_64 (srv21), kullanıcı sef. K=`/home/sef/01dev/_worktrees/kalem-0204` (git worktree, dal `sunucu/02-04-ydt-temel`).
Node `~/.nvm/versions/node/v24.22.2/bin`. Python `/usr/bin/python3 -I`. Skill `~/.claude/skills/motion-grafik-ders/`.
KURALLAR: Yalnız bu sahnenin dizinine yaz: `K/projeler/02-04-ydt-temel-s3/sahneler/02-hyperframes-ornek/`. Başka sahneye, `ortak/`a,
`BRIEF-S3.md`'ye, `zaman.json`'a, ana derse (`02-04-ydt-temel`) ve S1 paketine dokunma (eksik görürsen raporla). Silme yok. v1 sahne
kodunun yedeği hazır: `~/Silinecekler/2026-11-15-huni-v2/02-04-ydt-temel-s3/sahneler-v1/02-hyperframes-ornek/` (V2-S3-C aldı); yerinde
düzenle, v1'e oradan bak. mp4 render YOK: `calistir.sh`'ı yalnız `ONIZLE_YALNIZ=1` ile koş. git commit yok. Claude alt ajanı açma.
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
1. BAĞLAYICI: `/home/sef/01dev/dijital-anlatim/.claude/docs/huni-v2-standart.md` (§1, §2, §3 değer sahnesi, §5, §7).
2. Skill `SKILL.md`, `references/kalem-hatti.md`, `stil-anayasasi.md`, `hareket-sozlugu.md`, `kliseler.md`, `soru-ani.md`.
3. Paket `K/projeler/02-04-ydt-temel-s3/`: `BRIEF-S3.md` ("Yerleşim" tablosu; "Sahneler" 2. satırı `| 2 Değer | 02-hyperframes-ornek |
   HyperFrames | 3.00–15.99 | 402 | öğretmen + öğrenci sorusu |`; "Sahne içeriği" 3,00–15,99 satırları), `zaman.json` (bu sahne
   3,00–15,99 küresel sn, 402 kare), `ortak/anlatim/senaryo.json` + `sozcukler.json` + `baslar.json` + `altyazi.json` + `METIN.md`
   (cümle 1 sonu `p.m.` 3,00'ten; cümle 2 7,00–10,76 öğrenci, soru anı; cümle 3 11,51–15,99). Ses v1 ile birebir aynı (cümle 1–3
   md5 değişmedi); sözcük çapaları v1 ile aynı. Olay söylendiği anda gelir.
4. Başlangıç noktası: var olan v1 sahne kodu (`uret.py`, `yardim.py`, `SPEC.md`, `RAPOR.md`). Kart 1 devri sahne 01 ile ortak (aşağıda).
5. v1 istemi (içerik kaynağı; yerleşim GEÇERSİZ): `uretim-tutanagi/istem/sahne/D-02-hyperframes-ornek.md`.

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


## Bu sahneye özel (değer, 3,00–15,99)
- İçerik v1 ile aynı (BRIEF 3,00–15,99): kart 1 sürer, `pm` · `today.`; zaman çizgisi now → `7 pm` (`isaret`), etiket `gelecek · V-s`;
  kart 2 `I am going to the` / `movie theater tonight.` sözcük zamanlı, `tonight` noktası, etiket `gelecek · am + V-ing`; soru anı
  (balon, öğrenci figürü `kadro.ogrenci`, `Neden` çapasında sarı nokta → `leaves`); 10,76–11,51 duraklama; cevap: öğretmen figürü,
  `Planı` çapasında `bag` → `am going` + `person → plan`; `Tren` çapasında `bag` → `leaves` + `train → timetable`; `geniş` çapasında
  `leaves` `odak`. Aynı anda tek sarı vurgu.
- Yerleşim v2: bütün öğeler 460–1380 içinde, x 60–960 (v1 bandı 352–1392 idi; 120 px daha dar). Kart yazısı Fredoka 64, etiket Caveat
  ≥ 64. Kalabalıkta (S3-C açık nokta 4) balon girerken zaman çizgisi etiketleri solabilir; kartlar küçülür, yazı 64'ün altına inmez.
- Kare 0 = sahne 01'in son karesi: kart 1 Fredoka 700 64, sol x 97, taban y 568 ve 666 (sahne 01 ile ortak sabit; `sahneler/
  01-hyperframes-kapak/devir.json` v2 değeriyle aynı olmalı, sahne 01 bitmişse karşılaştır, farklıysa raporla); tren ikonu kart köşesinde.
- Künye kare 0'dan itibaren tam (`Simple Present vs Present Continuous` + rozet); kanal katmanı 402 kare boyunca sabit.
- Altyazı `altyazi.json`'dan küresel t ile; 1400–1550 bandında, x 60–960.

## Doğrula (zorunlu, geçmeden bitirme)
1. QA kareleri: `cd K && bash araclar/qa-yerel.sh 02-04-ydt-temel-s3 02-hyperframes-ornek 3.0,9.5,15.96 13.5 --hazirla` — açık: ilk
   kare 3,00, orta 9,50, son kare 15,96; koyu 13,50. Çıkış kodu 0. qa-yerel t değerleri KÜRESEL anlatım saniyesidir (`zaman.json` t_bas
   3,00 + sahne içi saniye), sahne içi saniye DEĞİLDİR.
2. Çakışma kapısı: `cd K && node araclar/cakisma-kapisi.mjs 02-04-ydt-temel-s3 --sahne 02-hyperframes-ornek --port 41333 --sunucu 41022`
   → 0 uyarı. Port doluysa (başka sahne oturumu) 1 dk bekle, yeniden koş.
3. Kanal katmanı (standart §7.2): üç açık karede ve koyu karede logo + `@ydspublishing` görünür, konum aynı (x 60, y 291–339).
4. Metin taraması: `grep -rniE "tam ders|dakika" K/projeler/02-04-ydt-temel-s3/sahneler/02-hyperframes-ornek/proje` → sonuç yok.
5. Kareleri (`k/`, `k/koyu/`) Read ile AÇ: taşma, kesik yazı, üst üste binme, kontrast, boş kare; 0–280 ve 1570–1920 boş mu; içerik
   x 960'ı aşıyor mu; altyazı 1400–1550 içinde mi. En çok 4 düzeltme turu; geçmezse dur, raporla.
qa-yerel ya da kapı paketi ölçemiyorsa dur ve hatayı aynen raporla; aracı değiştirme.

## Rapor
`sahneler/02-hyperframes-ornek/RAPOR.md`: olay listesi (olay · küresel sn · sözcük), kanal katmanı konum ölçümü, kart 1 devir
karşılaştırması, qa ve çakışma kapısı sonucu (son satırlar), bakılan kareler ve bulgu, agy koşu özeti yolu, açık noktalar. Son mesajın
en çok 10 satır.
