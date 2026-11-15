# İstem D-S2 — 02-04-ydt-temel-s2 sahne 02-paperjs-ornek · 15.11.2026

MAKİNE: Linux x86_64 (srv21), kullanıcı sef. K=`/home/sef/01dev/_worktrees/kalem-0204` (git worktree, dal `sunucu/02-04-ydt-temel`).
Node `~/.nvm/versions/node/v24.22.2/bin`. Python `/usr/bin/python3 -I`. Skill `~/.claude/skills/motion-grafik-ders/`.
KURALLAR: Yalnız bu sahnenin dizinine yaz: `K/projeler/02-04-ydt-temel-s2/sahneler/02-paperjs-ornek/`. Başka sahneye, `ortak/`a,
`BRIEF-S2.md`'ye, `zaman.json`'a, ana derse (`02-04-ydt-temel`), S1 paketine (`02-04-ydt-temel-s1`) ve dikey pakete dokunma (eksik
görürsen raporla). Silme yok (`~/Silinecekler/2026-11-15-0204/` altına taşı). mp4 render YOK: `calistir.sh`'ı yalnız `ONIZLE_YALNIZ=1`
ile koş. git commit yok. Claude alt ajanı açma.
Kanca atlama bayrağı OLUŞTURMA (/tmp/conductor-*, ~/.conductor/*). Durdurma kancası sözleşme satırı isterse K/.claude/docs/sozlesme.md
dosyasına 1–2 satır EKLE (tek istisna).

## Kod yolu (kapı ve doktrin)
Kod yazma kapısı 15 satırdan uzun kod dosyasını sana kapatır; bayrak açmaya çalışma. Yol: tasarımı sahne dizininde `SPEC.md` olarak
yaz (yazılacak dosyanın mutlak yolu, örnek sahnenin mutlak yolu ve oradan alınacak kalıp, olay listesi olay · kare/küresel sn · cümle
sözcüğü, yerleşim, ekran metni, kurallar, kabul ölçütü; tam kod YAZMA). Sonra
`agy-filo tek --rol kod --cwd /home/sef/01dev/_worktrees/kalem-0204 --zaman 25m -p "<SPEC.md mutlak yolunu oku ve uygula. Yalnız <dosya
mutlak yolu> dosyasını yaz. Başka dosyaya dokunma. Silme yok. Test, render, git yok.>"`. Kodu agy yazar; sen baştan sona okur, spec'e
uyuyor mu bakarsın, küçük düzeltmeyi Edit ile yaparsın, büyük düzeltmeyi agy'ye geri verirsin (en çok 2 tur). Tam kodu kendin yazıp
agy'ye birebir kopyalatmak YASAK (kapıyı vekille dolanmaktır). Örnek sahne dosyasını kopyalayıp küçük Edit'le uyarlamak serbest.
Kısa dosyalar (`calistir.sh`, `sayfa.html`) Edit ile yazılabilir.

## Okuma
1. Skill `SKILL.md`, `references/kalem-hatti.md`, `stil-anayasasi.md`, `hareket-sozlugu.md`, `kliseler.md`.
2. Paket: `K/projeler/02-04-ydt-temel-s2/BRIEF-S2.md` (giriş, "Sahneler" tablosunda 02. satır: 02 | 02-paperjs-ornek | Paper.js | 2.84–17.41 | 449 | video; "Sahne içeriği" tablosunun
   2,84–17,41 sn satırları ve altındaki DİKKAT notu; "Kapak" ve "Hikâye" bölümleri), `zaman.json` (bu sahne 2,84–17,41 küresel sn),
   `ortak/anlatim/senaryo.json` + `sozcukler.json` + `baslar.json` + `altyazi.json` (cümle 2 (3,39–17,41): olay söylendiği anda gelir; zaman
   sözcük çapasından okunur, sabit saniyeden değil), `uretim-tutanagi/senaryo-taslak.md` §2 (görsel fikir), `uretim-tutanagi/S2-duzeltme.md`,
   `K/projeler/present-continuous-dikey/BRIEF-DIKEY.md` §0 ve §2–§3 (Nadir'in dikey bulguları, HUD ölçüleri).
3. İçerik kaynağı (ana ders yatay; içerik ve olay sırası; yerleşim DEĞİL): `/home/sef/01dev/_worktrees/kalem-0204/projeler/02-04-ydt-temel/sahneler/03-paperjs-ornek1/` (iki kart, `SAT` kırılımı, MONT / TISORT, *wear* örneği) ve `/home/sef/01dev/_worktrees/kalem-0204/projeler/02-04-ydt-temel/sahneler/08-canvas-karsit1/` (today gün bandı, now noktası nabız) (kod + RAPOR.md).
4. Dikey örnek (aynı ders, aynı motor; dosya yapısı, `calistir.sh` kalıbı, 1080×1920 kurulum, `ONIZLE_YALNIZ` satırı): `/home/sef/01dev/_worktrees/kalem-0204/projeler/02-04-ydt-temel-s1/sahneler/02-paperjs-ornek/`.

## Yaz
`sahneler/02-paperjs-ornek/` içinde örnekle aynı dosya yapısı. Kurallar: tek sütun, kenar 48, içerik bandı 352–1392 (BRIEF-DIKEY §2); yazı tabanı
≥ 64 mantıksal px; satır ≤ 24 karakter; tek vurgu sarı (temaya göre), doğru şık yeşil, kırmızı yok, emoji yok; sabit px yerine oran ya da
BRIEF-DIKEY ölçüsü; altyazı + karaoke alt bantta (1400–1536); künye ve tema çifti (açık + koyu) `ortak/kunye.js` ile (çip
`KUNYE.cipler["02-paperjs-ornek"]`); sarı hap açık temada dolgu `RENK.vurguDolgu` (`#ffe066`), yazı `RENK.pilMetin` (`#1b2440`); 9 sn'den uzun boş
çerçeve yok; ekranda `T-shirt` tireli (seste `T shirt`); "kanal" sözü, QR ve süre "6 dk" yok.
`calistir.sh`: `[ -d /opt/homebrew/bin ] && export PATH="/opt/homebrew/bin:$PATH"`, yük `Y=$(yuk1)`, yakalama `1080 1920`.

Bu sahneye özel:
- Kare 0 = sahne 01'in son karesi: soru satırı `Genel mi, şu an mı?` (Caveat) içerik bandının üstünde, yerinde durur.
- Olaylar BRIEF-S2 "Sahne içeriği" 3,39–17,41 satırları. Kart 1 `She wears her coat` / `in the winter.` (`She` 3,39 · `coat` 4,27 mont
  kalemle · `in` 4,47 `odak`) · `GENERAL` (`Genel` 5,56) · `Simple Present` (`geniş` 6,68) · kart 1 altında `zaman_cizgisi` kış bantları.
- Kart 2 `She is wearing her` / `pink T-shirt today.` (`She` 8,37 · `T-shirt` 9,65 tişört kalemle · `today.` 10,13 `odak`). **DİKKAT:** bu
  parçanın çapaları `sozcukler.json`'da YOK; BRIEF-S2 DİKKAT notundaki değerleri sabit dizi olarak kullan, kaynağını kod yorumuna yaz.
- `today` sarı daire (`Today` 11,42) · `MEANING` sarı hap kart 2'nin sağında (`anlam` 14,14) + üst soru satırı mürekkep altçizgi; aynı anda
  `today` dairesi mürekkebe döner. `RIGHT NOW` (`Konuşma` 15,25) · `Present Continuous` (`şimdiki` 16,49) · `today` dairesinden `RIGHT NOW`'a
  tek ince kalem oku · kart 2 altında today gün bandı, now noktası bandın içinde nabız.
- YASAK (S2-duzeltme madde 2): `Simple Present` etiketine ok, kart 1'e herhangi bir bağ. Aynı anda en çok bir sarı öğe.
- Mont ve tişört ikonu kart köşelerinde küçük. Kartlar tek sütunda üst üste. Kart yazısı Fredoka 64; etiket Caveat ≥ 64; satır ≤ 24 karakter.
- Altyazı `ortak/anlatim/altyazi.json` (9 parça; paket içi üretici, parça sınırları doğru).

## Doğrula (zorunlu, geçmeden bitirme)
`cd K && bash araclar/qa-yerel.sh 02-04-ydt-temel-s2 02-paperjs-ornek <açık t1,t2,t3> <koyu t> --hazirla`
t değerleri KÜRESEL anlatım saniyesidir (2,84 + sahne içi saniye; sahne içi saniye DEĞİL); olayların bittiği 3 an + koyu için 1 an
(öneri: açık `7.9,14.9,17.3`, koyu `14.9`). Çıkış kodu 0 olmalı.
qa-yerel ya da kapı dikey (1080×1920) paketi ölçemiyorsa dur ve hatayı aynen raporla; aracı değiştirme.
Üretilen PNG'lere (`sahneler/02-paperjs-ornek/k/`, `k/koyu/`) Read ile BAK: taşma, kesik yazı, üst üste binme, okunmaz kontrast, boş kare,
alt bantta altyazıyla çakışma, 1536 altı boş mu. En çok 4 düzeltme turu; geçmezse dur ve raporla.

## Rapor
`sahneler/02-paperjs-ornek/RAPOR.md`: olay listesi, kapı sonucu (son satırlar), bakılan kareler ve bulgu, agy koşu özeti yolu, açık noktalar.
Son mesajın en çok 10 satır: kapı çıkış kodu, kare yolları, agy koşu özeti, açık noktalar.
