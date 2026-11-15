# İstem D-S1 — 02-04-ydt-temel-s1 sahne 03-hyperframes-cta · 15.11.2026

MAKİNE: Linux x86_64 (srv21), kullanıcı sef. K=`/home/sef/01dev/_worktrees/kalem-0204` (git worktree, dal `sunucu/02-04-ydt-temel`).
Node `~/.nvm/versions/node/v24.22.2/bin`. Python `/usr/bin/python3 -I`. Skill `~/.claude/skills/motion-grafik-ders/`.
KURALLAR: Yalnız bu sahnenin dizinine yaz: `K/projeler/02-04-ydt-temel-s1/sahneler/03-hyperframes-cta/`. Başka sahneye, `ortak/`a,
`BRIEF-S1.md`'ye, `zaman.json`'a, ana derse (`02-04-ydt-temel`) ve dikey pakete dokunma (eksik görürsen raporla). Silme yok
(`~/Silinecekler/2026-11-15-0204/` altına taşı). mp4 render YOK: `calistir.sh`'ı yalnız `ONIZLE_YALNIZ=1` ile koş. git commit yok.
Claude alt ajanı açma.

## Kod yolu (kapı ve doktrin)
Kod yazma kapısı 15 satırdan uzun kod dosyasını sana kapatır; bayrak açmaya çalışma. Yol: tasarımı sahne dizininde `SPEC.md` olarak
yaz (yazılacak dosyanın mutlak yolu, örnek sahnenin mutlak yolu ve oradan alınacak kalıp, olay listesi olay · kare/küresel sn · cümle
sözcüğü, yerleşim, ekran metni, kurallar, kabul ölçütü; tam kod YAZMA). Sonra
`agy-filo tek --rol kod --cwd /home/sef/01dev/_worktrees/kalem-0204 --zaman 25m -p "<SPEC.md mutlak yolunu oku ve uygula. Yalnız <dosya
mutlak yolu> dosyasını yaz. Başka dosyaya dokunma. Silme yok. Test, render, git yok.>"`. Kodu agy yazar; sen baştan sona okur, spec'e
uyuyor mu bakarsın, küçük düzeltmeyi Edit ile yaparsın, büyük düzeltmeyi agy'ye geri verirsin (en çok 2 tur). Tam kodu kendin yazıp
agy'ye birebir kopyalatmak YASAK (kapıyı vekille dolanmaktır). Kısa dosyalar (`calistir.sh`, `sayfa.html`) Edit ile yazılabilir.

## Okuma
1. Skill `SKILL.md`, `references/kalem-hatti.md`, `stil-anayasasi.md`, `hareket-sozlugu.md`, `kliseler.md`.
2. Paket: `K/projeler/02-04-ydt-temel-s1/BRIEF-S1.md` (giriş, "Sahneler" tablosunda 3. satır: `| 03 | 03-hyperframes-cta | HyperFrames | 19.99–30.56 | 347 |`; "Sahne içeriği" tablosunun
   19,99–30,56 sn satırları; "Kapak" ve "Hikâye karesi" bölümleri), `zaman.json` (bu sahne 19,99–30,56 küresel sn),
   `ortak/anlatim/senaryo.json` + `sozcukler.json` + `baslar.json` + `altyazi.json` (cümle 3 (20,54–29,56): olay söylendiği anda gelir; zaman
   sözcük çapasından okunur, sabit saniyeden değil), `uretim-tutanagi/senaryo-taslak.md` §2 (görsel fikir), `uretim-tutanagi/S1-duzeltme.md`,
   `K/projeler/present-continuous-dikey/BRIEF-DIKEY.md` §0 ve §2–§3 (Nadir'in dikey bulguları, HUD ölçüleri).
3. İçerik kaynağı (ana ders yatay; içerik ve olay sırası; yerleşim DEĞİL): `/home/sef/01dev/_worktrees/kalem-0204/projeler/02-04-ydt-temel/sahneler/14-hyperframes-kapanis/` (ders bandı, kapanış dili) (kod + RAPOR.md).
4. Dikey S1 örneği (aynı motor; dosya yapısı, calistir.sh kalıbı, 1080×1920 kurulum): `/home/sef/01dev/_worktrees/kalem-0204/projeler/present-continuous-ileri-s1/sahneler/03-hyperframes-cta/`.
   Örneğin `calistir.sh`'ı `ONIZLE_YALNIZ`'ı tanımaz: önizleme hazırlığından sonra, render öncesine
   `[ -n "$ONIZLE_YALNIZ" ] && { echo "önizleme hazır"; exit 0; }` satırını ekle (kalıp: `/home/sef/01dev/_worktrees/kalem-0204/projeler/02-04-ydt-temel/sahneler/01-hyperframes-giris/calistir.sh` satır 18`).

## Yaz
`sahneler/03-hyperframes-cta/` içinde örnekle aynı dosya yapısı. Kurallar: tek sütun, kenar 48, içerik bandı 352–1392 (BRIEF-DIKEY §2); yazı tabanı
≥ 64 mantıksal px; satır ≤ 24 karakter; tek vurgu sarı (temaya göre), doğru şık yeşil, kırmızı yok, emoji yok; sabit px yerine oran ya da
BRIEF-DIKEY ölçüsü; altyazı + karaoke alt bantta (1400–1536); künye ve tema çifti (açık + koyu) `ortak/kunye.js` ile (çip
`KUNYE.cipler["03-hyperframes-cta"]`); sarı hap açık temada dolgu `RENK.vurguDolgu` (`#ffe066`), yazı `RENK.pilMetin` (`#1b2440`); 9 sn'den uzun boş
çerçeve yok; ekranda "İstanbul" noktalı (seste "Istanbul"); "kanal" sözü, QR ve süre "6 dk" yok.
`calistir.sh`: `[ -d /opt/homebrew/bin ] && export PATH="/opt/homebrew/bin:$PATH"`, yük `Y=$(yuk1)`, yakalama `1080 1920`.

Bu sahneye özel:
- Örnek CTA'daki `Tam ders kanalda · 6 dk` satırını ve "kanalda izle" dilini KOPYALAMA (kalıp hatası; S1-A-RAPOR açık nokta 5).
- Sıra BRIEF-S1 20,54–30,56 satırları: `üç farktan biri` Lexend (`üç` 21,02) → `Tam ders:` Caveat (22,77) → ders bandı Fredoka
  `Simple Present` (23,97) / `vs Present Continuous` (`vs` = sesteki `ve` çapası 24,77) → `üç farkın hepsi` (27,00) → saat (clock) +
  `dört buçuk dakikada` (28,36) → `@ydspublishing` sarı hap son sözle (`dakikada.` 28,84–29,64).
- 29,56–30,56 durgun kuyruk. Son karede ev ve bavul ikonu bandın iki yanında küçük → kapak karesine döngü (kalıp §1 kural 5).

## Doğrula (zorunlu, geçmeden bitirme)
`cd K && bash araclar/qa-yerel.sh 02-04-ydt-temel-s1 03-hyperframes-cta <açık t1,t2,t3> <koyu t> --hazirla`
t değerleri KÜRESEL anlatım saniyesidir (19,99 + sahne içi saniye); olayların bittiği 3 an + koyu için 1 an (öneri: açık `22.7,27.0,30.4`, koyu `29.8`). Çıkış kodu 0 olmalı.
qa-yerel ya da kapı dikey (1080×1920) paketi ölçemiyorsa dur ve hatayı aynen raporla; aracı değiştirme.
Üretilen PNG'lere (`sahneler/03-hyperframes-cta/k/`, `k/koyu/`) Read ile BAK: taşma, kesik yazı, üst üste binme, okunmaz kontrast, boş kare,
alt bantta altyazıyla çakışma, 1536 altı boş mu. En çok 4 düzeltme turu; geçmezse dur ve raporla.

## Rapor
`sahneler/03-hyperframes-cta/RAPOR.md`: olay listesi, kapı sonucu (son satırlar), bakılan kareler ve bulgu, agy koşu özeti yolu, açık noktalar.
Son mesajın en çok 10 satır: kapı çıkış kodu, kare yolları, agy koşu özeti, açık noktalar.
