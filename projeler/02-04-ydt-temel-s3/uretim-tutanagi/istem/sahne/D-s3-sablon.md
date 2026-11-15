# İstem D-S3 — 02-04-ydt-temel-s3 sahne {SAHNE} · 15.11.2026

<!-- Şablon: ~/is/uretim-0204/D-dikey-sablon.md kopyası, S3'e uyarlandı (S3-C, 15.11; uyarlama kalıbı S1 `D-s1-sablon.md`).
Yer tutucular: {SAHNE} {NO} {SATIR} {BOLUM} {ZAMAN} {CUMLE} {YATAY} {ORNEK} {CIKTI} {OZEL} {DOGRULA}. Doldurulmuş istemler: D-<klasör>.md. -->

MAKİNE: Linux x86_64 (srv21), kullanıcı sef. K=`/home/sef/01dev/_worktrees/kalem-0204` (git worktree, dal `sunucu/02-04-ydt-temel`).
Node `~/.nvm/versions/node/v24.22.2/bin`. Python `/usr/bin/python3 -I`. Skill `~/.claude/skills/motion-grafik-ders/`.
KURALLAR: Yalnız bu sahnenin dizinine yaz: `K/projeler/02-04-ydt-temel-s3/sahneler/{SAHNE}/`.{CIKTI} Başka sahneye, `ortak/`a,
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
2. Paket: `K/projeler/02-04-ydt-temel-s3/BRIEF-S3.md` (giriş, "Sahneler" tablosunda {NO} satırı: {SATIR}; {BOLUM}),
   `zaman.json` ({ZAMAN}), `ortak/anlatim/senaryo.json` + `sozcukler.json` + `baslar.json` + `altyazi.json` ({CUMLE}),
   `uretim-tutanagi/senaryo-taslak.md` §2 (görsel fikir), `kapak-taslak.md`,
   `hikaye-taslak.md`, `uretim-tutanagi/S3-duzeltme.md` (jüri düzeltmeleri: taslakla çelişirse düzeltme geçerli),
   `K/projeler/present-continuous-dikey/BRIEF-DIKEY.md` §0 ve §2–§3 (Nadir'in dikey bulguları, HUD ölçüleri).
3. İçerik kaynağı (ana ders yatay; içerik, çizim ve olay sırası; yerleşim DEĞİL): {YATAY} (kod + RAPOR.md).
4. Dikey örnek (aynı dersin bitmiş kısası S1; aynı motor; dosya yapısı, calistir.sh kalıbı, 1080×1920 kurulum): `{ORNEK}`.
   Örneğin `calistir.sh` dosyası `ONIZLE_YALNIZ` satırını zaten taşır. S1 içeriğini (ev, bavul, `YAŞIYORUM`, `I live`, S1 zamanları) taşıma.

## Yaz
`sahneler/{SAHNE}/` içinde örnekle aynı dosya yapısı. Kurallar: tek sütun, kenar 48, içerik bandı 352–1392 (BRIEF-DIKEY §2); yazı tabanı
≥ 64 mantıksal px; satır ≤ 24 karakter; tek vurgu sarı (temaya göre), doğru şık yeşil, kırmızı yok, emoji yok; sabit px yerine oran ya da
BRIEF-DIKEY ölçüsü; altyazı + karaoke alt bantta (1400–1536); künye ve tema çifti (açık + koyu) `ortak/kunye.js` ile (çip
`KUNYE.cipler["{SAHNE}"]`); sarı hap açık temada dolgu `RENK.vurguDolgu` (`#ffe066`), yazı `RENK.pilMetin` (`#1b2440`); 9 sn'den uzun boş
çerçeve yok; ekranda "İzmir" noktalı (seste "Izmir"); ekranda `7 pm` (seste *seven p.m.*); "kanal" sözü, QR ve süre "6 dk" yok.
`calistir.sh`: `[ -d /opt/homebrew/bin ] && export PATH="/opt/homebrew/bin:$PATH"`, yük `Y=$(yuk1)`, yakalama `1080 1920`.

Bu sahneye özel:
{OZEL}

## Doğrula (zorunlu, geçmeden bitirme)
{DOGRULA}
qa-yerel t değerleri KÜRESEL anlatım saniyesidir (`zaman.json` t_bas + sahne içi saniye), sahne içi saniye DEĞİLDİR.
Üretilen PNG'lere (`sahneler/{SAHNE}/k/`, `k/koyu/`) Read ile BAK: taşma, kesik yazı, üst üste binme, okunmaz kontrast, boş kare,
alt bantta altyazıyla çakışma, 1536 altı boş mu. En çok 4 düzeltme turu; geçmezse dur ve raporla.

## Rapor
`sahneler/{SAHNE}/RAPOR.md`: olay listesi, kapı sonucu (son satırlar), bakılan kareler ve bulgu, agy koşu özeti yolu, açık noktalar.
Son mesajın en çok 10 satır: kapı çıkış kodu, kare yolları, agy koşu özeti, açık noktalar.
