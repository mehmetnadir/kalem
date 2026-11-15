# İstem D-S3 — 02-04-ydt-temel-s3 sahne 03-hyperframes-cta · 15.11.2026

MAKİNE: Linux x86_64 (srv21), kullanıcı sef. K=`/home/sef/01dev/_worktrees/kalem-0204` (git worktree, dal `sunucu/02-04-ydt-temel`).
Node `~/.nvm/versions/node/v24.22.2/bin`. Python `/usr/bin/python3 -I`. Skill `~/.claude/skills/motion-grafik-ders/`.
KURALLAR: Yalnız bu sahnenin dizinine yaz: `K/projeler/02-04-ydt-temel-s3/sahneler/03-hyperframes-cta/`. Başka sahneye, `ortak/`a,
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
2. Paket: `K/projeler/02-04-ydt-temel-s3/BRIEF-S3.md` (giriş, "Sahneler" tablosunda 3. satırı: `| 03 | 03-hyperframes-cta | HyperFrames | 15.99–26.56 | 347 |`; "Sahne içeriği" tablosunun 15,99–26,56 sn satırları),
   `zaman.json` (bu sahne 15,99–26,56 küresel sn), `ortak/anlatim/senaryo.json` + `sozcukler.json` + `baslar.json` + `altyazi.json` (cümle 4 (16,54–25,56); ses dosyası S1 cümle 3 ile birebir aynı (md5 `80e56127…`), küresel zaman S1'e göre −4,00 sn. Olay söylendiği anda gelir; zaman sözcük çapasından okunur, sabit saniyeden değil),
   `uretim-tutanagi/senaryo-taslak.md` §2 (görsel fikir), `kapak-taslak.md`,
   `hikaye-taslak.md`, `uretim-tutanagi/S3-duzeltme.md` (jüri düzeltmeleri: taslakla çelişirse düzeltme geçerli),
   `K/projeler/present-continuous-dikey/BRIEF-DIKEY.md` §0 ve §2–§3 (Nadir'in dikey bulguları, HUD ölçüleri).
3. İçerik kaynağı (ana ders yatay; içerik, çizim ve olay sırası; yerleşim DEĞİL): `/home/sef/01dev/_worktrees/kalem-0204/projeler/02-04-ydt-temel/sahneler/14-hyperframes-kapanis/` (ders bandı, kapanış dili) (kod + RAPOR.md).
4. Dikey örnek (aynı dersin bitmiş kısası S1; aynı motor; dosya yapısı, calistir.sh kalıbı, 1080×1920 kurulum): `/home/sef/01dev/_worktrees/kalem-0204/projeler/02-04-ydt-temel-s1/sahneler/03-hyperframes-cta/`.
   Örneğin `calistir.sh` dosyası `ONIZLE_YALNIZ` satırını zaten taşır. S1 içeriğini (ev, bavul, `YAŞIYORUM`, `I live`, S1 zamanları) taşıma.

## Yaz
`sahneler/03-hyperframes-cta/` içinde örnekle aynı dosya yapısı. Kurallar: tek sütun, kenar 48, içerik bandı 352–1392 (BRIEF-DIKEY §2); yazı tabanı
≥ 64 mantıksal px; satır ≤ 24 karakter; tek vurgu sarı (temaya göre), doğru şık yeşil, kırmızı yok, emoji yok; sabit px yerine oran ya da
BRIEF-DIKEY ölçüsü; altyazı + karaoke alt bantta (1400–1536); künye ve tema çifti (açık + koyu) `ortak/kunye.js` ile (çip
`KUNYE.cipler["03-hyperframes-cta"]`); sarı hap açık temada dolgu `RENK.vurguDolgu` (`#ffe066`), yazı `RENK.pilMetin` (`#1b2440`); 9 sn'den uzun boş
çerçeve yok; ekranda "İzmir" noktalı (seste "Izmir"); ekranda `7 pm` (seste *seven p.m.*); "kanal" sözü, QR ve süre "6 dk" yok.
`calistir.sh`: `[ -d /opt/homebrew/bin ] && export PATH="/opt/homebrew/bin:$PATH"`, yük `Y=$(yuk1)`, yakalama `1080 1920`.

Bu sahneye özel:
- Örnek S1 sahne 03 ile aynı ses dosyasıdır: düzen ve göreli çapalar aynen geçerli; yalnız küresel zaman (S1 − 4,00 sn) ve ikonlar
  değişir. Zamanı sözcük çapasından oku; S1 saniyesini sabit olarak kopyalama.
- Sıra BRIEF-S3 15,99–26,56 satırları: `üç farktan biri` Lexend (`üç` 17,02) → `Tam ders:` Caveat (`Tam` 18,77) → ders bandı Fredoka
  `Simple Present` (19,97) / `vs Present Continuous` (`vs` = sesteki `ve` çapası 20,77) → `üç farkın hepsi` (`Üç` 23,00) → saat (clock) +
  `dört buçuk dakikada` (`dört` 24,36) → `@ydspublishing` sarı hap son sözle (`dakikada.` 24,84–25,64).
- 25,56–26,56 durgun kuyruk. Son karede tren ve bilet ikonu bandın iki yanında küçük (S1'deki ev ve bavul yerine) → kapak A karesine
  döngü (kalıp §1 kural 5).
- "kanalda izle" dili ve `6 dk` yok (S1-A açık nokta 5).

## Doğrula (zorunlu, geçmeden bitirme)
`cd K && bash araclar/qa-yerel.sh 02-04-ydt-temel-s3 03-hyperframes-cta <açık t1,t2,t3> <koyu t> --hazirla`
Olayların bittiği 3 an + koyu için 1 an (sahne t_bas 15,99; öneri: açık `18.7,23.0,26.4`, koyu `25.8`). Çıkış kodu 0 olmalı.
qa-yerel ya da kapı dikey (1080×1920) paketi ölçemiyorsa dur ve hatayı aynen raporla; aracı değiştirme.
qa-yerel t değerleri KÜRESEL anlatım saniyesidir (`zaman.json` t_bas + sahne içi saniye), sahne içi saniye DEĞİLDİR.
Üretilen PNG'lere (`sahneler/03-hyperframes-cta/k/`, `k/koyu/`) Read ile BAK: taşma, kesik yazı, üst üste binme, okunmaz kontrast, boş kare,
alt bantta altyazıyla çakışma, 1536 altı boş mu. En çok 4 düzeltme turu; geçmezse dur ve raporla.

## Rapor
`sahneler/03-hyperframes-cta/RAPOR.md`: olay listesi, kapı sonucu (son satırlar), bakılan kareler ve bulgu, agy koşu özeti yolu, açık noktalar.
Son mesajın en çok 10 satır: kapı çıkış kodu, kare yolları, agy koşu özeti, açık noktalar.
