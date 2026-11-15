# İstem D-S2 — 02-04-ydt-temel-s2 sahne 01-hyperframes-kapak · 15.11.2026

MAKİNE: Linux x86_64 (srv21), kullanıcı sef. K=`/home/sef/01dev/_worktrees/kalem-0204` (git worktree, dal `sunucu/02-04-ydt-temel`).
Node `~/.nvm/versions/node/v24.22.2/bin`. Python `/usr/bin/python3 -I`. Skill `~/.claude/skills/motion-grafik-ders/`.
KURALLAR: Yalnız bu sahnenin dizinine yaz: `K/projeler/02-04-ydt-temel-s2/sahneler/01-hyperframes-kapak/`. `calistir.sh`'ın render dalı paket köküne `kapak-a.png` ve kopyası `kapak.png` yazar (S1 örnekteki gibi); bu istemde render yok, ikisi oluşmaz. Başka sahneye, `ortak/`a,
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
2. Paket: `K/projeler/02-04-ydt-temel-s2/BRIEF-S2.md` (giriş, "Sahneler" tablosunda 01. satır: 01 | 01-hyperframes-kapak | HyperFrames | 0.00–2.84 | 97 | video + kapak-a.png (+ kapak.png); "Sahne içeriği" tablosunun
   0,00–2,84 sn satırları ve altındaki DİKKAT notu; "Kapak" ve "Hikâye" bölümleri), `zaman.json` (bu sahne 0,00–2,84 küresel sn),
   `ortak/anlatim/senaryo.json` + `sozcukler.json` + `baslar.json` + `altyazi.json` (cümle 1 (1,00–2,84): olay söylendiği anda gelir; zaman
   sözcük çapasından okunur, sabit saniyeden değil), `uretim-tutanagi/senaryo-taslak.md` §2 (görsel fikir), `uretim-tutanagi/S2-duzeltme.md`,
   `K/projeler/present-continuous-dikey/BRIEF-DIKEY.md` §0 ve §2–§3 (Nadir'in dikey bulguları, HUD ölçüleri).
3. İçerik kaynağı (ana ders yatay; içerik ve olay sırası; yerleşim DEĞİL): `/home/sef/01dev/_worktrees/kalem-0204/projeler/02-04-ydt-temel/sahneler/01-hyperframes-giris/` (giriş, figür) ve nesneler için `/home/sef/01dev/_worktrees/kalem-0204/projeler/02-04-ydt-temel/sahneler/03-paperjs-ornek1/sahne-03.js` (MONT, TISORT kalem dizileri) (kod + RAPOR.md).
4. Dikey örnek (aynı ders, aynı motor; dosya yapısı, `calistir.sh` kalıbı, 1080×1920 kurulum, `ONIZLE_YALNIZ` satırı): `/home/sef/01dev/_worktrees/kalem-0204/projeler/02-04-ydt-temel-s1/sahneler/01-hyperframes-kapak/`.

## Yaz
`sahneler/01-hyperframes-kapak/` içinde örnekle aynı dosya yapısı. Kurallar: tek sütun, kenar 48, içerik bandı 352–1392 (BRIEF-DIKEY §2); yazı tabanı
≥ 64 mantıksal px; satır ≤ 24 karakter; tek vurgu sarı (temaya göre), doğru şık yeşil, kırmızı yok, emoji yok; sabit px yerine oran ya da
BRIEF-DIKEY ölçüsü; altyazı + karaoke alt bantta (1400–1536); künye ve tema çifti (açık + koyu) `ortak/kunye.js` ile (çip
`KUNYE.cipler["01-hyperframes-kapak"]`); sarı hap açık temada dolgu `RENK.vurguDolgu` (`#ffe066`), yazı `RENK.pilMetin` (`#1b2440`); 9 sn'den uzun boş
çerçeve yok; ekranda `T-shirt` tireli (seste `T shirt`); "kanal" sözü, QR ve süre "6 dk" yok.
`calistir.sh`: `[ -d /opt/homebrew/bin ] && export PATH="/opt/homebrew/bin:$PATH"`, yük `Y=$(yuk1)`, yakalama `1080 1920`.

Bu sahneye özel:
- İlk kare = kapak A: başlık 0. karede tam görünür (BRIEF-S2 "Kapak A"; `uretim-tutanagi/kapak-taslak.md` §1–§3). Rozet `YDT · BASIC`;
  başlık `GENEL` (952 px'e sığan en büyük boy, üst sınır 190 px; motor ölçer) / `≠ ŞU AN` sarı hapta.
- Kalem hareketi: `≠` işareti hapın içinde 0,30–0,80. Uçuş 2,24–2,84: başlık üst bant ders adına, figür ve iki nesne solar; soru satırı
  `Genel mi, şu an mı?` (Caveat) içerik bandının üstüne kalemle yazılır. Satırın uçuş sonrası konumu sahne 02 kare 0 ile aynı (S1 örnek `uret.py` kalıbı).
- Sahne: solda askıda mont (`coat`), ortada işaret pozunda öğretmen figürü (`senaryo.json` → `kadro.ogretmen`, `giris.sahne`), sağda askıda
  pembe tişört (`t-shirt`); etiketler mont altında `wears`, tişört altında `is wearing` (Caveat ≥ 72). Mont ve tişört için ana ders
  `sahne-03.js` MONT / TISORT kalem dizileri; `ortak/cizim` kataloğunda karşılık yoksa Open Doodles / Tabler taranır; bulunamazsa raporla.
- Cümle 1 yalnız altyazı bandında sözcük zamanlı (`Genel` 1,00 · `şu` 2,12 · `mı?` 2,52). Kapak başlığı sesi tekrarlamaz; soru satırı uçuşta gelir.
- Çip kapak bitene kadar gizli (örnekteki gibi). `calistir.sh` render dalı kare 27'yi (t 0,90; `≠` bitmiş, altyazı yok) paket köküne
  `kapak-a.png` yazar ve `kapak.png` olarak kopyalar (tema açık; S1 örnek `calistir.sh` kare 59 satırı kalıbı, kare numarası 27).
  Denetim kareleri: 0,2 · 0,9 · 2,5 · 2,8 sn. Sahne kare sayısı 97 (içerik 85 + geçiş 12).

## Doğrula (zorunlu, geçmeden bitirme)
`cd K && bash araclar/qa-yerel.sh 02-04-ydt-temel-s2 01-hyperframes-kapak <açık t1,t2,t3> <koyu t> --hazirla`
t değerleri KÜRESEL anlatım saniyesidir (0,00 + sahne içi saniye; sahne içi saniye DEĞİL); olayların bittiği 3 an + koyu için 1 an
(öneri: açık `0.2,0.9,2.8`, koyu `0.9`). Çıkış kodu 0 olmalı.
qa-yerel ya da kapı dikey (1080×1920) paketi ölçemiyorsa dur ve hatayı aynen raporla; aracı değiştirme.
Üretilen PNG'lere (`sahneler/01-hyperframes-kapak/k/`, `k/koyu/`) Read ile BAK: taşma, kesik yazı, üst üste binme, okunmaz kontrast, boş kare,
alt bantta altyazıyla çakışma, 1536 altı boş mu. En çok 4 düzeltme turu; geçmezse dur ve raporla.

## Rapor
`sahneler/01-hyperframes-kapak/RAPOR.md`: olay listesi, kapı sonucu (son satırlar), bakılan kareler ve bulgu, agy koşu özeti yolu, açık noktalar.
Son mesajın en çok 10 satır: kapı çıkış kodu, kare yolları, agy koşu özeti, açık noktalar.
