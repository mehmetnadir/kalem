# İstem D-V2-S3 — 02-04-ydt-temel-s3 sahne 01-hyperframes-kapak (kanca) · huni v2 · 15.11.2026

MAKİNE: Linux x86_64 (srv21), kullanıcı sef. K=`/home/sef/01dev/_worktrees/kalem-0204` (git worktree, dal `sunucu/02-04-ydt-temel`).
Node `~/.nvm/versions/node/v24.22.2/bin`. Python `/usr/bin/python3 -I`. Skill `~/.claude/skills/motion-grafik-ders/`.
KURALLAR: Yalnız bu sahnenin dizinine yaz: `K/projeler/02-04-ydt-temel-s3/sahneler/01-hyperframes-kapak/`. İstisna: kapak dalı paket
köküne `kapak-a.png` ve `kapak.png` yazar (eski ikisi yedekte). Başka sahneye, `ortak/`a, `BRIEF-S3.md`'ye, `zaman.json`'a, ana derse
(`02-04-ydt-temel`) ve S1 paketine dokunma (eksik görürsen raporla). Silme yok. v1 sahne kodunun yedeği hazır:
`~/Silinecekler/2026-11-15-huni-v2/02-04-ydt-temel-s3/sahneler-v1/01-hyperframes-kapak/` (V2-S3-C aldı); yerinde düzenle, v1'e oradan bak.
mp4 render YOK: `calistir.sh`'ı yalnız `ONIZLE_YALNIZ=1` ile koş. git commit yok. Claude alt ajanı açma.
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
1. BAĞLAYICI: `/home/sef/01dev/dijital-anlatim/.claude/docs/huni-v2-standart.md` (§1, §2, §3, §6 kapak, §7).
2. Skill `SKILL.md`, `references/kalem-hatti.md`, `stil-anayasasi.md`, `hareket-sozlugu.md`, `kliseler.md`.
3. Paket `K/projeler/02-04-ydt-temel-s3/`: `BRIEF-S3.md` ("Yerleşim" tablosu; "Sahneler" 1. satırı `| 1 Kanca | 01-hyperframes-kapak |
   HyperFrames | 0.00–3.00 | 102 | öğretmen |`; "Sahne içeriği" 0,00–3,00 satırları; "Kapak A"), `zaman.json` (bu sahne 0,00–3,00 küresel
   sn, 102 kare), `ortak/anlatim/senaryo.json` + `sozcukler.json` + `baslar.json` + `altyazi.json` + `METIN.md` (cümle 1 başı: `The` 1,00 ·
   `Izmir` 1,64 · `leaves` 2,20 · `at` 2,56 · `seven` 2,80–2,92; `p.m.` 3,00'te sahne 02'de). Olay söylendiği anda gelir.
4. Başlangıç noktası: var olan v1 sahne kodu (`uret.py`, `yardim.py`, `SPEC.md`, `RAPOR.md`, `devir.json`, `proje-ka*`); kapak A yöntemi
   `uretim-tutanagi/S3-SON-RAPOR.md` "Kapak A yöntemi".
5. v1 istemi (içerik kaynağı; yerleşim GEÇERSİZ): `uretim-tutanagi/istem/sahne/D-01-hyperframes-kapak.md`.

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

## Bu sahneye özel (kanca, 0,00–3,00)
- İçerik v1 ile aynı (BRIEF 0,00–3,00): ilk kare = kapak A; başlık `TARİFE` / `≠ PLAN` (sarı hap); solda tren + saat (kollar yedide,
  rakamsız), etiket `leaves`; sağda bilet tutan öğretmen figürü, etiket `am going` (Caveat ≥ 72); `TARİFE` altçizgisi 0,30–0,80; kart 1
  satır 1 `The train to İzmir` 1,00'den, satır 2 `leaves at 7` sözcük zamanlı; uçuş 2,0–3,0.
- Yerleşim v2: başlık + çizim + kart 460–1380 içinde, x 60–960 (başlık 900 px'e sığan en büyük boy, üst sınır 190). Künye bandında 0.
  karede yalnız rozet (son konumunda); uçuşta başlık künye bandına iner, `Simple Present vs Present Continuous` (34 px) olur.
- Kart 1 devri (sahne 02 ile ortak sabit): Fredoka 700 64, sol x 97, taban y 568 ve 666 (v1 468/566 + 100). Uçuş sonunda kart 1 bu
  konumda durur; `devir.json`'a yazılır. Sahne 02 kare 0 aynı değeri kullanır.
- Kanal katmanı 0. kareden 102. kareye kadar sabit; uçuşta kıpırdamaz.
- Kapak A: render yok. Kapak dalı S3-SON yöntemi: `proje-ka` ve `proje-ka-koyu` kopyaları v2 `proje/`'den yeniden alınır; yalnız CSS
  `#altyazi{display:none !important}`; `hyperframes snapshot --at 1.97` → paket kökü `kapak-a.png` + `kapak.png` (açık, `cmp` aynı) ve
  `k/koyu/kapak-a-koyu.png`. Karede kanal katmanı görünür, altyazı görünmez. Eski kapaklar yedekte (`~/Silinecekler/2026-11-15-huni-v2/
  02-04-ydt-temel-s3/kapak-a.png`, `kapak.png`).

## Doğrula (zorunlu, geçmeden bitirme)
1. QA kareleri: `cd K && bash araclar/qa-yerel.sh 02-04-ydt-temel-s3 01-hyperframes-kapak 0.0,1.5,2.97 1.97 --hazirla` — açık: ilk kare
   0,00, orta 1,50, son kare 2,97; koyu 1,97. Çıkış kodu 0. qa-yerel t değerleri KÜRESEL anlatım saniyesidir (`zaman.json` t_bas 0,00 +
   sahne içi saniye), sahne içi saniye DEĞİLDİR.
2. Çakışma kapısı: `cd K && node araclar/cakisma-kapisi.mjs 02-04-ydt-temel-s3 --sahne 01-hyperframes-kapak --port 41333 --sunucu 41022`
   → 0 uyarı. Port doluysa (başka sahne oturumu) 1 dk bekle, yeniden koş.
3. Kanal katmanı (standart §7.2): üç açık karede ve koyu karede logo + `@ydspublishing` görünür, konum aynı (x 60, y 291–339).
4. Metin taraması: `grep -rniE "tam ders|dakika" K/projeler/02-04-ydt-temel-s3/sahneler/01-hyperframes-kapak/proje` → sonuç yok.
5. Kareleri (`k/`, `k/koyu/`, `kapak-a.png`, `k/koyu/kapak-a-koyu.png`) Read ile AÇ: taşma, kesik yazı, üst üste binme, kontrast, boş
   kare; 0–280 ve 1570–1920 boş mu; içerik x 960'ı aşıyor mu; altyazı 1400–1550 içinde mi. En çok 4 düzeltme turu; geçmezse dur, raporla.
qa-yerel ya da kapı paketi ölçemiyorsa dur ve hatayı aynen raporla; aracı değiştirme.

## Rapor
`sahneler/01-hyperframes-kapak/RAPOR.md`: olay listesi (olay · küresel sn · sözcük), kanal katmanı konum ölçümü, kart 1 devir değeri,
qa ve çakışma kapısı sonucu (son satırlar), bakılan kareler ve bulgu, agy koşu özeti yolu, açık noktalar. Son mesajın en çok 10 satır.
