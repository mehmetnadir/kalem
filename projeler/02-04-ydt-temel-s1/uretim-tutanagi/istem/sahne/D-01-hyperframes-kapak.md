# İstem D-S1 — 02-04-ydt-temel-s1 sahne 01-hyperframes-kapak · 15.11.2026

MAKİNE: Linux x86_64 (srv21), kullanıcı sef. K=`/home/sef/01dev/_worktrees/kalem-0204` (git worktree, dal `sunucu/02-04-ydt-temel`).
Node `~/.nvm/versions/node/v24.22.2/bin`. Python `/usr/bin/python3 -I`. Skill `~/.claude/skills/motion-grafik-ders/`.
KURALLAR: Yalnız bu sahnenin dizinine yaz: `K/projeler/02-04-ydt-temel-s1/sahneler/01-hyperframes-kapak/`. `calistir.sh`'ın render dalı paket köküne `kapak.png` yazar (örnekteki gibi); bu istemde render yok, `kapak.png` oluşmaz. Başka sahneye, `ortak/`a,
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
2. Paket: `K/projeler/02-04-ydt-temel-s1/BRIEF-S1.md` (giriş, "Sahneler" tablosunda 1. satır: `| 01 | 01-hyperframes-kapak | HyperFrames | 0.00–3.00 | 102 |`; "Sahne içeriği" tablosunun
   0,00–3,00 sn satırları; "Kapak" ve "Hikâye karesi" bölümleri), `zaman.json` (bu sahne 0,00–3,00 küresel sn),
   `ortak/anlatim/senaryo.json` + `sozcukler.json` + `baslar.json` + `altyazi.json` (cümle 1'in başı: `İstanbul'da` 1,00 · `yaşıyorum.` 1,64 · `Amcamla` 2,52: olay söylendiği anda gelir; zaman
   sözcük çapasından okunur, sabit saniyeden değil), `uretim-tutanagi/senaryo-taslak.md` §2 (görsel fikir), `uretim-tutanagi/S1-duzeltme.md`,
   `K/projeler/present-continuous-dikey/BRIEF-DIKEY.md` §0 ve §2–§3 (Nadir'in dikey bulguları, HUD ölçüleri).
3. İçerik kaynağı (ana ders yatay; içerik ve olay sırası; yerleşim DEĞİL): `/home/sef/01dev/_worktrees/kalem-0204/projeler/02-04-ydt-temel/sahneler/01-hyperframes-giris/` ve cümle 1 ekran metni için `/home/sef/01dev/_worktrees/kalem-0204/projeler/02-04-ydt-temel/sahneler/02-paperjs-kanca/` (kod + RAPOR.md).
4. Dikey S1 örneği (aynı motor; dosya yapısı, calistir.sh kalıbı, 1080×1920 kurulum): `/home/sef/01dev/_worktrees/kalem-0204/projeler/present-continuous-ileri-s1/sahneler/01-hyperframes-kapak/`.
   Örneğin `calistir.sh`'ı `ONIZLE_YALNIZ`'ı tanımaz: önizleme hazırlığından sonra, render öncesine
   `[ -n "$ONIZLE_YALNIZ" ] && { echo "önizleme hazır"; exit 0; }` satırını ekle (kalıp: `/home/sef/01dev/_worktrees/kalem-0204/projeler/02-04-ydt-temel/sahneler/01-hyperframes-giris/calistir.sh` satır 18`).

## Yaz
`sahneler/01-hyperframes-kapak/` içinde örnekle aynı dosya yapısı. Kurallar: tek sütun, kenar 48, içerik bandı 352–1392 (BRIEF-DIKEY §2); yazı tabanı
≥ 64 mantıksal px; satır ≤ 24 karakter; tek vurgu sarı (temaya göre), doğru şık yeşil, kırmızı yok, emoji yok; sabit px yerine oran ya da
BRIEF-DIKEY ölçüsü; altyazı + karaoke alt bantta (1400–1536); künye ve tema çifti (açık + koyu) `ortak/kunye.js` ile (çip
`KUNYE.cipler["01-hyperframes-kapak"]`); sarı hap açık temada dolgu `RENK.vurguDolgu` (`#ffe066`), yazı `RENK.pilMetin` (`#1b2440`); 9 sn'den uzun boş
çerçeve yok; ekranda "İstanbul" noktalı (seste "Istanbul"); "kanal" sözü, QR ve süre "6 dk" yok.
`calistir.sh`: `[ -d /opt/homebrew/bin ] && export PATH="/opt/homebrew/bin:$PATH"`, yük `Y=$(yuk1)`, yakalama `1080 1920`.

Bu sahneye özel:
- İlk kare = kapak: başlık 0. karede tam görünür (BRIEF-S1 "Kapak"; `uretim-tutanagi/kapak-taslak.md`). Rozet `YDT · BASIC`;
  başlık `YAŞIYORUM` (952 px'e sığan en büyük boy, üst sınır 190 px; motor ölçer) / `= İKİ ZAMAN` sarı hapta.
- Kalem hareketi: `YOR` altına sarı el altçizgisi 0,30–0,80. Uçuş 2,0–3,0: başlık üst bant ders adına, figür ve ev solar.
- Sahne: solda ev (`house`), sağda elinde bavul (`suitcase`) tutan öğretmen figürü (`senaryo.json` → `kadro.ogretmen`, `giris.sahne`);
  etiketler ev yanında `I live`, bavul yanında `I am living` (Caveat ≥ 72). İkon `ortak/cizim` kataloğunda yoksa Open Doodles /
  Tabler taranır; bulunamazsa raporla.
- Cümle 1: `İstanbul'da yaşı-yor-um.` 1,00'den sözcük zamanlı; ikinci satır `Amcamla yaşı-yor-um.` `Amcamla` çapasında (2,52).
  Sahne 01 iki satır taşır (S1-duzeltme madde 1). Satırların uçuş sonrası konumu sahne 02 kare 0 ile aynı (örnek `uret.py` satır 25 kalıbı).
- Çip kapak bitene kadar gizli (örnekteki gibi). `calistir.sh` render dalı kare 59'u (t 1,97) paket köküne `kapak.png` yazar
  (tema açık; örnek `calistir.sh` satır 34–36).

## Doğrula (zorunlu, geçmeden bitirme)
`cd K && bash araclar/qa-yerel.sh 02-04-ydt-temel-s1 01-hyperframes-kapak <açık t1,t2,t3> <koyu t> --hazirla`
t değerleri KÜRESEL anlatım saniyesidir (0,00 + sahne içi saniye); olayların bittiği 3 an + koyu için 1 an (öneri: açık `0.2,1.97,2.95`, koyu `1.97`). Çıkış kodu 0 olmalı.
qa-yerel ya da kapı dikey (1080×1920) paketi ölçemiyorsa dur ve hatayı aynen raporla; aracı değiştirme.
Üretilen PNG'lere (`sahneler/01-hyperframes-kapak/k/`, `k/koyu/`) Read ile BAK: taşma, kesik yazı, üst üste binme, okunmaz kontrast, boş kare,
alt bantta altyazıyla çakışma, 1536 altı boş mu. En çok 4 düzeltme turu; geçmezse dur ve raporla.

## Rapor
`sahneler/01-hyperframes-kapak/RAPOR.md`: olay listesi, kapı sonucu (son satırlar), bakılan kareler ve bulgu, agy koşu özeti yolu, açık noktalar.
Son mesajın en çok 10 satır: kapı çıkış kodu, kare yolları, agy koşu özeti, açık noktalar.
