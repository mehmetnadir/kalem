# İstem D-S1 — 02-04-ydt-temel-s1 sahne 02-paperjs-ornek · 15.11.2026

MAKİNE: Linux x86_64 (srv21), kullanıcı sef. K=`/home/sef/01dev/_worktrees/kalem-0204` (git worktree, dal `sunucu/02-04-ydt-temel`).
Node `~/.nvm/versions/node/v24.22.2/bin`. Python `/usr/bin/python3 -I`. Skill `~/.claude/skills/motion-grafik-ders/`.
KURALLAR: Yalnız bu sahnenin dizinine yaz: `K/projeler/02-04-ydt-temel-s1/sahneler/02-paperjs-ornek/`. Başka sahneye, `ortak/`a,
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
2. Paket: `K/projeler/02-04-ydt-temel-s1/BRIEF-S1.md` (giriş, "Sahneler" tablosunda 2. satır: `| 02 | 02-paperjs-ornek | Paper.js | 3.00–19.99 | 522 |`; "Sahne içeriği" tablosunun
   3,00–19,99 sn satırları; "Kapak" ve "Hikâye karesi" bölümleri), `zaman.json` (bu sahne 3,00–19,99 küresel sn),
   `ortak/anlatim/senaryo.json` + `sozcukler.json` + `baslar.json` + `altyazi.json` (cümle 1'in sonu (3,08'den) ve cümle 2 (6,91–19,99): olay söylendiği anda gelir; zaman
   sözcük çapasından okunur, sabit saniyeden değil), `uretim-tutanagi/senaryo-taslak.md` §2 (görsel fikir), `uretim-tutanagi/S1-duzeltme.md`,
   `K/projeler/present-continuous-dikey/BRIEF-DIKEY.md` §0 ve §2–§3 (Nadir'in dikey bulguları, HUD ölçüleri).
3. İçerik kaynağı (ana ders yatay; içerik ve olay sırası; yerleşim DEĞİL): `/home/sef/01dev/_worktrees/kalem-0204/projeler/02-04-ydt-temel/sahneler/02-paperjs-kanca/` (iki TR satır, `ek_ayir`, iki kart), `/home/sef/01dev/_worktrees/kalem-0204/projeler/02-04-ydt-temel/sahneler/04-canvas-ornek2/` (live: kalıcı / geçici) ve zaman çizgisi görseli için `/home/sef/01dev/_worktrees/kalem-0204/projeler/02-04-ydt-temel/sahneler/11-canvas-tuzak-cevap/` (kod + RAPOR.md).
4. Dikey S1 örneği (aynı motor; dosya yapısı, calistir.sh kalıbı, 1080×1920 kurulum): `/home/sef/01dev/_worktrees/kalem-0204/projeler/present-continuous-ileri-s1/sahneler/02-paperjs-ornek/`.
   Örneğin `calistir.sh`'ı `ONIZLE_YALNIZ`'ı tanımaz: önizleme hazırlığından sonra, render öncesine
   `[ -n "$ONIZLE_YALNIZ" ] && { echo "önizleme hazır"; exit 0; }` satırını ekle (kalıp: `/home/sef/01dev/_worktrees/kalem-0204/projeler/02-04-ydt-temel/sahneler/02-paperjs-kanca/calistir.sh` satır 10`).

## Yaz
`sahneler/02-paperjs-ornek/` içinde örnekle aynı dosya yapısı. Kurallar: tek sütun, kenar 48, içerik bandı 352–1392 (BRIEF-DIKEY §2); yazı tabanı
≥ 64 mantıksal px; satır ≤ 24 karakter; tek vurgu sarı (temaya göre), doğru şık yeşil, kırmızı yok, emoji yok; sabit px yerine oran ya da
BRIEF-DIKEY ölçüsü; altyazı + karaoke alt bantta (1400–1536); künye ve tema çifti (açık + koyu) `ortak/kunye.js` ile (çip
`KUNYE.cipler["02-paperjs-ornek"]`); sarı hap açık temada dolgu `RENK.vurguDolgu` (`#ffe066`), yazı `RENK.pilMetin` (`#1b2440`); 9 sn'den uzun boş
çerçeve yok; ekranda "İstanbul" noktalı (seste "Istanbul"); "kanal" sözü, QR ve süre "6 dk" yok.
`calistir.sh`: `[ -d /opt/homebrew/bin ] && export PATH="/opt/homebrew/bin:$PATH"`, yük `Y=$(yuk1)`, yakalama `1080 1920`.

Bu sahneye özel:
- Kare 0 = sahne 01'in son karesi: iki TR satır (`İstanbul'da yaşı-yor-um.` / `Amcamla yaşı-yor-um.`) uçuş sonrası konumda, yerinde sürer.
- Olaylar BRIEF-S1 "Sahne içeriği" 3,08–19,99 satırları: `yaşıyorum.` karaokesi 3,08 · `ek_ayir` 3,96 (iki satırda *yor* sarı
  kutuda, 5,56) · `ayrılır.` 8,19 TR satırlar yukarı solar, iki *yor* kutusu kalır · `bag` *yor* kutularından kartlara kalem çizgisi.
- Kart 1 `I live in İstanbul.` (9,08; `live` 9,32 `odak`) · soluk TR `Hep orada.` (11,17) · `PERMANENT` (12,37) · uzun bant (13,25).
- Kart 2 `I am living` / `with my uncle.` (14,70; `living` 15,02 `odak`; 26 karakter → 2 satır) · soluk TR `Şimdilik.` (17,03) ·
  `TEMPORARY` (18,07) · kısa bant (19,03). Kartlar tek sütunda üst üste; `zaman_cizgisi` now noktası iki bandın içinde.
- Ev ikonu kart 1 köşesinde, bavul ikonu kart 2 köşesinde küçük. Kart yazısı Fredoka 64; etiket Caveat ≥ 64.

## Doğrula (zorunlu, geçmeden bitirme)
`cd K && bash araclar/qa-yerel.sh 02-04-ydt-temel-s1 02-paperjs-ornek <açık t1,t2,t3> <koyu t> --hazirla`
t değerleri KÜRESEL anlatım saniyesidir (3,00 + sahne içi saniye); olayların bittiği 3 an + koyu için 1 an (öneri: açık `6.0,13.8,19.6`, koyu `16.0`). Çıkış kodu 0 olmalı.
qa-yerel ya da kapı dikey (1080×1920) paketi ölçemiyorsa dur ve hatayı aynen raporla; aracı değiştirme.
Üretilen PNG'lere (`sahneler/02-paperjs-ornek/k/`, `k/koyu/`) Read ile BAK: taşma, kesik yazı, üst üste binme, okunmaz kontrast, boş kare,
alt bantta altyazıyla çakışma, 1536 altı boş mu. En çok 4 düzeltme turu; geçmezse dur ve raporla.

## Rapor
`sahneler/02-paperjs-ornek/RAPOR.md`: olay listesi, kapı sonucu (son satırlar), bakılan kareler ve bulgu, agy koşu özeti yolu, açık noktalar.
Son mesajın en çok 10 satır: kapı çıkış kodu, kare yolları, agy koşu özeti, açık noktalar.
