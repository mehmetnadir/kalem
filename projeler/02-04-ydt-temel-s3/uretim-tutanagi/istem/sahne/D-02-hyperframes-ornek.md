# İstem D-S3 — 02-04-ydt-temel-s3 sahne 02-hyperframes-ornek · 15.11.2026

MAKİNE: Linux x86_64 (srv21), kullanıcı sef. K=`/home/sef/01dev/_worktrees/kalem-0204` (git worktree, dal `sunucu/02-04-ydt-temel`).
Node `~/.nvm/versions/node/v24.22.2/bin`. Python `/usr/bin/python3 -I`. Skill `~/.claude/skills/motion-grafik-ders/`.
KURALLAR: Yalnız bu sahnenin dizinine yaz: `K/projeler/02-04-ydt-temel-s3/sahneler/02-hyperframes-ornek/`. Başka sahneye, `ortak/`a,
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
2. Paket: `K/projeler/02-04-ydt-temel-s3/BRIEF-S3.md` (giriş, "Sahneler" tablosunda 2. satırı: `| 02 | 02-hyperframes-ornek | HyperFrames | 3.00–15.99 | 402 |`; "Sahne içeriği" tablosunun 3,00–15,99 sn satırları),
   `zaman.json` (bu sahne 3,00–15,99 küresel sn), `ortak/anlatim/senaryo.json` + `sozcukler.json` + `baslar.json` + `altyazi.json` (cümle 1'in sonu (`p.m.` 3,00'ten), cümle 2 (7,00–10,76, öğrenci, soru anı) ve cümle 3 (11,51–15,99). Olay söylendiği anda gelir; zaman sözcük çapasından okunur, sabit saniyeden değil),
   `uretim-tutanagi/senaryo-taslak.md` §2 (görsel fikir), `kapak-taslak.md`,
   `hikaye-taslak.md`, `uretim-tutanagi/S3-duzeltme.md` (jüri düzeltmeleri: taslakla çelişirse düzeltme geçerli),
   `K/projeler/present-continuous-dikey/BRIEF-DIKEY.md` §0 ve §2–§3 (Nadir'in dikey bulguları, HUD ölçüleri).
3. İçerik kaynağı (ana ders yatay; içerik, çizim ve olay sırası; yerleşim DEĞİL): `/home/sef/01dev/_worktrees/kalem-0204/projeler/02-04-ydt-temel/sahneler/05-canvas-ornek3/` (iki kart, tren ve bilet çizimleri), `/home/sef/01dev/_worktrees/kalem-0204/projeler/02-04-ydt-temel/sahneler/06-hyperframes-soru1/` (balon `ogrenci-bas.svg` + `hw-text-cloud`, öğretmen figürü işaret pozu, `bag`; cümle 6–7) ve zaman çizgisi için `/home/sef/01dev/_worktrees/kalem-0204/projeler/02-04-ydt-temel/sahneler/09-canvas-karsit2/` (`7 pm` `isaret` dairesi) (kod + RAPOR.md).
4. Dikey örnek (aynı dersin bitmiş kısası S1; aynı motor; dosya yapısı, calistir.sh kalıbı, 1080×1920 kurulum): `/home/sef/01dev/_worktrees/kalem-0204/projeler/02-04-ydt-temel-s1/sahneler/03-hyperframes-cta/` (S1'in sese bağlı HyperFrames sahnesi). Kart düzeni ve karaoke için S1 sahne 02 (Paper.js) yalnız okunur: `/home/sef/01dev/_worktrees/kalem-0204/projeler/02-04-ydt-temel-s1/sahneler/02-paperjs-ornek/`.
   Örneğin `calistir.sh` dosyası `ONIZLE_YALNIZ` satırını zaten taşır. S1 içeriğini (ev, bavul, `YAŞIYORUM`, `I live`, S1 zamanları) taşıma.

## Yaz
`sahneler/02-hyperframes-ornek/` içinde örnekle aynı dosya yapısı. Kurallar: tek sütun, kenar 48, içerik bandı 352–1392 (BRIEF-DIKEY §2); yazı tabanı
≥ 64 mantıksal px; satır ≤ 24 karakter; tek vurgu sarı (temaya göre), doğru şık yeşil, kırmızı yok, emoji yok; sabit px yerine oran ya da
BRIEF-DIKEY ölçüsü; altyazı + karaoke alt bantta (1400–1536); künye ve tema çifti (açık + koyu) `ortak/kunye.js` ile (çip
`KUNYE.cipler["02-hyperframes-ornek"]`); sarı hap açık temada dolgu `RENK.vurguDolgu` (`#ffe066`), yazı `RENK.pilMetin` (`#1b2440`); 9 sn'den uzun boş
çerçeve yok; ekranda "İzmir" noktalı (seste "Izmir"); ekranda `7 pm` (seste *seven p.m.*); "kanal" sözü, QR ve süre "6 dk" yok.
`calistir.sh`: `[ -d /opt/homebrew/bin ] && export PATH="/opt/homebrew/bin:$PATH"`, yük `Y=$(yuk1)`, yakalama `1080 1920`.

Bu sahneye özel:
- Kare 0 = sahne 01'in son karesi: kart 1 (`The train to İzmir` / `leaves at 7`) uçuş sonrası konumda, tren ikonu kart köşesinde; yerinde sürer.
- Cümle 1 sonu: `pm` (= *p.m.* 3,00) · `today.` (3,40). `today.` çapasında zaman çizgisi: now noktası → `7 pm` çentiğine kalem oku;
  `7 pm` sarı daire (`isaret`); nokta altına etiket `gelecek · V-s` (S3-duzeltme madde 6).
- Kart 2 `I am going to the` / `movie theater tonight.` sözcük zamanlı (`I` 4,45 · `going` 4,81 · `tonight.` 5,93); `tonight.` çapasında
  çizgide now'ın sağına `tonight` noktası, etiket `gelecek · am + V-ing`. Bilet ikonu kart 2 köşesinde. Kartlar tek sütunda üst üste.
- Soru anı (cümle 2, öğrenci; `soru-ani.md`): balon kart sütununun altına girer, kartlar üstte küçülür. Balon `Hocam, tren de plana` /
  `göre kalkmıyor mu?` / `Neden -ing yok?` sözcük zamanlı (`Hocam,` 7,00 · `Neden` 9,72 · `-ing` 10,08 · `yok?` 10,33). `Neden` çapasında
  sarı nokta: balon → kart 1 `leaves`. 10,76–11,51 duraklama: balon durur. Öğrenci figürü `kadro.ogrenci` (K22: figür sesle eşleşir).
- Cevap (cümle 3): balon solar, öğretmen figürü girer (ayakta, işaret pozu). `Planı` (11,51) çapasında `bag`: figür → `am going`,
  `am going` `odak`; kart 2 altında `person → plan`. `Tren` (13,43) çapasında `bag`: tren ikonu → `leaves`; kart 1 altında
  `train → timetable` (`tarifeye` 13,83). `geniş` (15,19) çapasında `leaves` `odak` (sarı). Aynı anda tek sarı vurgu.
- Kart yazısı Fredoka 64; etiket Caveat ≥ 64. En uzun satır `movie theater tonight.` = 22.

## Doğrula (zorunlu, geçmeden bitirme)
`cd K && bash araclar/qa-yerel.sh 02-04-ydt-temel-s3 02-hyperframes-ornek <açık t1,t2,t3> <koyu t> --hazirla`
Olayların bittiği 3 an + koyu için 1 an (sahne t_bas 3,00; öneri: açık `6.6,10.9,15.9`, koyu `13.5`). Çıkış kodu 0 olmalı.
qa-yerel ya da kapı dikey (1080×1920) paketi ölçemiyorsa dur ve hatayı aynen raporla; aracı değiştirme.
qa-yerel t değerleri KÜRESEL anlatım saniyesidir (`zaman.json` t_bas + sahne içi saniye), sahne içi saniye DEĞİLDİR.
Üretilen PNG'lere (`sahneler/02-hyperframes-ornek/k/`, `k/koyu/`) Read ile BAK: taşma, kesik yazı, üst üste binme, okunmaz kontrast, boş kare,
alt bantta altyazıyla çakışma, 1536 altı boş mu. En çok 4 düzeltme turu; geçmezse dur ve raporla.

## Rapor
`sahneler/02-hyperframes-ornek/RAPOR.md`: olay listesi, kapı sonucu (son satırlar), bakılan kareler ve bulgu, agy koşu özeti yolu, açık noktalar.
Son mesajın en çok 10 satır: kapı çıkış kodu, kare yolları, agy koşu özeti, açık noktalar.
