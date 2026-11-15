# İstem D-V2 — simple-present-temel-s2 sahne 02-paperjs-deger (huni v2) · 15.11.2026

<!-- S2-C (15.11) yazdı. Şablon: K/projeler/02-04-ydt-temel-s1/uretim-tutanagi/istem/sahne-v2/D-02-paperjs-ornek.md. -->

MAKİNE: Linux x86_64 (srv21), kullanıcı sef. K=`/home/sef/01dev/_worktrees/kalem-0204` (git worktree, dal `sunucu/02-04-ydt-temel`),
D=`/home/sef/01dev/dijital-anlatim`. Node `~/.nvm/versions/node/v24.22.2/bin`. Python `/usr/bin/python3 -I`. Skill `~/.claude/skills/motion-grafik-ders/`.
KURALLAR: Yalnız bu sahnenin dizinine yaz: `K/projeler/simple-present-temel-s2/sahneler/02-paperjs-deger/` (klasör yeni; sen açarsın).
`ortak/kunye.js` hazırdır (S2-C: emsalin v2 kopyası; yalnız `KOK` ve `KUNYE.konu` = `Simple Present` değişti): içe aktar, DEĞİŞTİRME; değişiklik
gerekiyorsa dur ve raporla. Başka sahneye, `ortak/`a, `BRIEF-S2.md`'ye, `zaman.json`'a, ana derse (`simple-present-temel`) ve emsale
(`02-04-ydt-temel-s1`) dokunma (ikisi yalnız okunur); eksik görürsen raporla. Silme yok (`~/Silinecekler/2026-11-15-0204/simple-present-temel-s2/`
altına taşı). mp4 render YOK: `calistir.sh`'ı yalnız `ONIZLE_YALNIZ=1` ile koş. git commit yok. Claude alt ajanı açma.
Kanca atlama bayrağı OLUŞTURMA (`/tmp/conductor-*`, `~/.conductor/*`). Durdurma kancası sözleşme satırı isterse `K/.claude/docs/sozlesme.md`
dosyasına 1–2 satır EKLE (tek istisna).

## Kod yolu (kapı ve doktrin)
Kod yazma kapısı 15 satırdan uzun kod dosyasını sana kapatır; bayrak açmaya çalışma. Emsalden kopyalanan dosyalar (`sayfa.html`,
`kalem-paper.js`, `calistir.sh` varsa) `cp -p` + küçük Edit ile kurulur (paket yolu, sahne adı). Yeni içerik taşıyan kod (`sahne-02.js`):
tasarımı sahne dizininde `SPEC.md` olarak yaz (yazılacak dosyanın mutlak yolu, var olan kodun mutlak yolu ve oradan alınacak kalıp, olay
listesi olay · kare/küresel sn · cümle sözcüğü, yerleşim, ekran metni, kurallar, kabul ölçütü; tam kod YAZMA). Sonra
`agy-filo tek --rol kod --cwd /home/sef/01dev/_worktrees/kalem-0204 --zaman 25m -p "<SPEC.md mutlak yolunu oku ve uygula. Yalnız <dosya
mutlak yolu> dosyasını yaz. Başka dosyaya dokunma. Silme yok. Test, render, git yok.>"`. Kodu agy yazar; sen baştan sona okur, spec'e
uyuyor mu bakarsın, küçük düzeltmeyi Edit ile yaparsın, büyük düzeltmeyi agy'ye geri verirsin (en çok 2 tur). Tam kodu kendin yazıp
agy'ye birebir kopyalatmak YASAK.

## Okuma
1. `D/.claude/docs/huni-v2-standart.md` (tamamı; BAĞLAYICI: §1 kurallar, §2 yerleşim, §3 yapı, §5 "TR soluk", §7 kapı).
2. Skill `SKILL.md`, `references/kalem-hatti.md`, `stil-anayasasi.md`, `hareket-sozlugu.md`, `kliseler.md`.
3. Paket: `K/projeler/simple-present-temel-s2/BRIEF-S2.md` ("Yerleşim", "Kanal katmanı" tablosu, "Sahneler" satırı:
   `| 2 Değer | 02-paperjs-deger | Paper.js | 3,00–11,87 | 278 | öğretmen |`; "Sahne içeriği" 3,00–11,87 satırları), `zaman.json`,
   `ortak/anlatim/senaryo.json` + `sozcukler.json` + `baslar.json` + `altyazi.json` (cümle 1 sonu `zaman?` 2,92–3,48 yalnız altyazıda; cümle 2:
   `My` 3,95 · `usually` 4,59–4,91 · `goes` 4,99 · `bus.` 5,95–6,59 · `Alışkanlık` 6,84 · `işareti.` 7,52–8,52 · `Şu` 8,67 · `değil,` 9,07 ·
   `her` 9,79 · `sabah` 9,95 · `yedide` 10,31 · `kalkarım` 10,67 · `gibi.` 11,39–11,95), `uretim-tutanagi/S2-C-RAPOR.md`,
   `uretim-tutanagi/senaryo-taslak.md` §2 sahne 2.
4. Kod tabanı (yalnız okunur): emsal v2 `K/projeler/02-04-ydt-temel-s1/sahneler/02-paperjs-ornek/` (`sahne-02.js`, `kalem-paper.js`,
   `sayfa.html`, `SPEC.md`, `RAPOR.md`; kanal katmanı, künye, altyazı, kart kutusu kalıbı). Çizim dizisi: ana ders
   `K/projeler/simple-present-temel/sahneler/04-canvas-ornek2/sahne.js` (oturan figür, otobüs, gün kutuları; canvas → Paper.js'e taşınır).
5. Sözleşme `K/.claude/docs/sozlesme.md` huni v2 satırları ("Canvas huni v2 künyesi", "Paper.js huni v2 künyesi", `paperTopla` kutu kuralı).

## Kanal katmanı ve künye (bütün sahnelerde AYNI; değer değiştirme)
| Öğe | Değer |
|---|---|
| Logo | `ortak/logo/` (açık `yds-publishing-lacivert.svg`, koyu `yds-publishing-seffaf.svg`); yükseklik 48, genişlik 193,5; resim x 53,2 (görünür sol kenar x 60), y 291–339 |
| Yazı | `@ydspublishing`, Lexend 700 42 px, renk `murekkep`, x 263, taban y 330 |
| Davranış | 0. kareden son kareye; opaklık 1; giriş/çıkış animasyonu yok; uçuş/geçiş dokunmaz; kimlik `kanal`; `__kalemKutu` türü `kunye`, ad `kunye:kanal` |
| Künye | y 360–450: konu `Simple Present` (Fredoka 700, x 60, taban 420; boy ≤ 34, rozetle x 960'a sığan en büyük, alt sınır 28) + rozet `YDT · BASIC` (hap y 386–434, Lexend 700 26, dolgu `vurguDolgu`, yazı `pilMetin`, konu sonu + 20) |
| Bantlar | üst 0–280 boş (çip YOK) · içerik 460–1380, x 60–960 · altyazı 1400–1550 (en çok 2 satır) · alt 1570–1920 boş |

Canvas: `ortak/kunye.js` → `kunyeHazirla()`, `zeminCiz`, `kanalCiz(ctx, K)`, `kunyeCiz`, `altyaziCiz(ctx, altyaziMetin(K.altyazi, t))` (t = küresel sn).
Değerler BRIEF-S2 "Kanal katmanı" tablosuyla birebir; elle başka değer yazma.

## Yaz
Tek sütun; yazı tabanı ≥ 64 mantıksal px (künye, kanal ve altyazı hariç); satır ≤ 24 karakter; tek vurgu sarı (temaya göre), doğru
yeşil, kırmızı yok, emoji yok; sarı açık temada dolgu `vurguDolgu` (`#ffe066`); tema çifti (açık + koyu; koyu kare de QA'ya girer).
Yasak (standart §1): "Tam ders" sözü, süre sözü ("dakika"), QR, "izle" düğmesi taklidi.

Bu sahneye özel (sn KÜRESEL; yerel kare = round((t − 3,00) × 30)):
- Kare 0 (3,00): içerik bandı boş (sahne 01 devri); 3,00–3,40 boş kart çerçevesi girer (yazısız, tek hareket), x 60–960, y ≈ 480–660
  (sözleşme: el çizimi köşe taşması için `KX = kenar + 10`, `KW = 880`).
- 3,95–6,59 kart karaoke, Fredoka 64: `My brother usually` / `goes to school by bus.` sözcük zamanlı. `usually` çapasında (4,59) sarı el dairesi:
  sahnenin tek sarısı. Alt bölgede oturan figür (`ortak/cizim/open-peeps/sitting-4.svg`) + otobüs (`ortak/cizim/coco/bus.svg`) kalemle çizilir (3,95–6,59).
- 6,59: kartın altında soluk TR, seslendirilmez (Caveat 64, `ikincil`, 2 satır): `Kardeşim genellikle` / `okula otobüsle gider.`; y ≈ 690–830.
  (Taslaktaki Caveat 48 tek satır ≥ 64 px kuralına uymaz; S2-C 64 px iki satıra çekti.)
- 6,84: `alışkanlık` (Caveat 64) `Alışkanlık` çapasında, sarı daireden ince kalem okuyla, kartın sağ altında; ikinci ince ok `usually`
  dairesinden TR satırdaki `genellikle`ye (köprü; çizgi, yazı değil).
- 8,67: figür ve otobüs solar (alt bölge boşalır); `şu an` (Caveat 64, `ikincil`) yazılır, y ≈ 960–1030. 9,07: `değil,` çapasında `şu an`
  üstüne kalem çizgisi.
- 9,79–11,39: `Her sabah yedide` / `kalkarım.` (Caveat 64) sözcük zamanlı (`her` 9,79 · `sabah` 9,95 · `yedide` 10,31 · `kalkarım` 10,67),
  y ≈ 1060–1220; `her sabah` altına mürekkep altçizgi (sarı değil); altta 5 küçük gün kutusu (el çizimi) sırayla tik alır, 5/5 (her sabah),
  y ≈ 1250–1350.
- Bütün içerik x 60–960, y 460–1380; sığmazsa yazı boyu değil, kart iç payı ve görsel ölçeği küçülür (yazı ≥ 64).
- Altyazı + karaoke 1400–1550: 3,00–3,48 cümle 1'in sonu (`zaman?`), sonra cümle 2. Çip yok.

## Doğrula (zorunlu, geçmeden bitirme)
1. `cd K && bash araclar/qa-yerel.sh simple-present-temel-s2 02-paperjs-deger 3.05,7.45,11.80 7.45 --hazirla` → çıkış 0. t değerleri KÜRESEL
   anlatım saniyesidir (yerel değil): ilk kare 3,05, orta 7,45, son kare 11,80; koyu tema 7.45. qa-yerel ya da kapı dikey paketi ölçemiyorsa dur
   ve hatayı aynen raporla; aracı değiştirme.
2. Çakışma kapısı: `cd K && node araclar/cakisma-kapisi.mjs simple-present-temel-s2 --sahne 02-paperjs-deger --port 41333 --sunucu 41022`
   → çıkış 0, 0 uyarı.
3. Metin taraması: `grep -rniE 'tam ders|dakika' K/projeler/simple-present-temel-s2/sahneler/02-paperjs-deger/ --include=*.html --include=*.js --include=*.py` boş.
4. Kanal katmanı: QA karelerinin hepsinde görünür, konum ve boy tablodakiyle aynı (karede ölç; standart §7 madde 2).
Üretilen PNG'lere (`sahneler/02-paperjs-deger/k/`, `k/koyu/`) Read ile BAK: taşma, kesik yazı, üst üste binme, okunmaz kontrast, boş kare,
0–280 ve 1570–1920 boş mu, sağ 960–1080 bölgesinde içerik var mı. En çok 4 düzeltme turu; geçmezse dur ve raporla.

## Rapor
`sahneler/02-paperjs-deger/RAPOR.md`: olay listesi, kapı sonuçları (son satırlar), bakılan kareler ve bulgu, agy koşu özeti yolu, açık
noktalar. Son mesajın en çok 10 satır: kapı çıkış kodları, kare yolları, agy koşu özeti, açık noktalar.
