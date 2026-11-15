# İstem D — simple-present-temel-s3 sahne 02-paperjs-deger (huni v2) · 15.11.2026

<!-- P0202-S3-C (15.11) yazdı. Şablon: emsal `K/projeler/02-04-ydt-temel-s1/uretim-tutanagi/istem/sahne-v2/D-02-paperjs-ornek.md`. -->

MAKİNE: Linux x86_64 (srv21), kullanıcı sef. K=`/home/sef/01dev/_worktrees/kalem-0204` (git worktree, dal `sunucu/02-04-ydt-temel`),
D=`/home/sef/01dev/dijital-anlatim`. Node `~/.nvm/versions/node/v24.22.2/bin`. Python `/usr/bin/python3 -I`. Skill `~/.claude/skills/motion-grafik-ders/`.
KURALLAR: Yalnız bu sahnenin dizinine yaz: `K/projeler/simple-present-temel-s3/sahneler/02-paperjs-deger/` (klasör yeni; sen açarsın). Başka sahneye, `ortak/`a,
`BRIEF-S3.md`'ye, `zaman.json`'a, ana derse (`simple-present-temel`) ve emsal pakete (`02-04-ydt-temel-s1`) dokunma (ikisi yalnız okunur);
eksik görürsen raporla. Silme yok (`~/Silinecekler/2026-11-15-0204/simple-present-temel-s3/` altına taşı). mp4 render YOK: `calistir.sh`'ı yalnız `ONIZLE_YALNIZ=1` ile koş. git commit yok. Claude alt ajanı açma.
Kanca atlama bayrağı OLUŞTURMA (`/tmp/conductor-*`, `~/.conductor/*`). Durdurma kancası sözleşme satırı isterse `K/.claude/docs/sozlesme.md`
dosyasına 1–2 satır EKLE (tek istisna).

## Kod yolu (kapı ve doktrin)
Kod yazma kapısı 15 satırdan uzun kod dosyasını sana kapatır; bayrak açmaya çalışma. Yol: tasarımı sahne dizininde `SPEC.md` olarak
yaz (yazılacak dosyanın mutlak yolu, var olan kodun mutlak yolu ve oradan alınacak kalıp, olay listesi olay · kare/küresel sn · cümle
sözcüğü, yerleşim, ekran metni, kurallar, kabul ölçütü; tam kod YAZMA). Sonra
`agy-filo tek --rol kod --cwd /home/sef/01dev/_worktrees/kalem-0204 --zaman 25m -p "<SPEC.md mutlak yolunu oku ve uygula. Yalnız <dosya
mutlak yolu> dosyasını yaz. Başka dosyaya dokunma. Silme yok. Test, render, git yok.>"`. Kodu agy yazar; sen baştan sona okur, spec'e
uyuyor mu bakarsın, küçük düzeltmeyi Edit ile yaparsın, büyük düzeltmeyi agy'ye geri verirsin (en çok 2 tur). Tam kodu kendin yazıp
agy'ye birebir kopyalatmak YASAK. Kısa dosyalar (`calistir.sh`, `sayfa.html`) kopyalanır ve Edit ile uyarlanır. Klasör yeni; bir dosyanın
üzerine yazman gerekirse önce `~/Silinecekler/2026-11-15-0204/simple-present-temel-s3/sahneler/02-paperjs-deger/` altına kopyala.

## Okuma
1. `D/.claude/docs/huni-v2-standart.md` (tamamı; BAĞLAYICI: §1 kurallar, §2 yerleşim, §3 yapı, §6 türevler, §7 kapı).
2. Skill `SKILL.md`, `references/kalem-hatti.md`, `stil-anayasasi.md`, `hareket-sozlugu.md`, `kliseler.md`.
3. Paket: `K/projeler/simple-present-temel-s3/BRIEF-S3.md` ("Yerleşim", "Kanal katmanı" tablosu, "Sahneler" satırı: `| 2 Değer | 02-paperjs-deger | Paper.js | 3,89–12,84 | 281 | öğretmen |`; "Sahne içeriği" 3,89–12,84 satırları), `zaman.json`
   (`sahneler[]`, `hikaye`, `duragan[]`), `ortak/anlatim/senaryo.json` + `sozcukler.json` + `baslar.json` + `altyazi.json` (cümle 2: `Olumsuzda` 4,44 · `does` 6,28 · `s` 7,24 · `ona` 7,56 · `Fiile` 8,51 · `s` 8,99 · `gelmez.` 9,23 · `He` 10,36 · `doesn't` 10,60 · `go.` 11,16 · `Does` 11,96 · `she` 12,20 · `go?` 12,36–12,84),
   `uretim-tutanagi/S3-C-RAPOR.md`, `uretim-tutanagi/S3-duzeltme.md`, `uretim-tutanagi/senaryo-taslak.md` §2 sahne 2 satırları.
4. Kod tabanı (emsal v2, yalnız okunur): `K/projeler/02-04-ydt-temel-s1/sahneler/02-paperjs-ornek/` (`sahne-02.js`, `kalem-paper.js`, `sayfa.html`, `calistir.sh`, `nesneler.json`, `SPEC.md`, `RAPOR.md`). `kalem-paper.js`, `sayfa.html`, `calistir.sh` kopyalanır (paket, klasör ve sahne dosyası adı Edit ile); `sahne-02.js` içerik farklı → SPEC + agy. Ev ve bavul ikonları YOK.

## Kanal katmanı ve künye (bütün sahnelerde AYNI; değer değiştirme)
| Öğe | Değer |
|---|---|
| Logo | `ortak/logo/` (açık `yds-publishing-lacivert.svg`, koyu `yds-publishing-seffaf.svg`); yükseklik 48, genişlik 193,5; resim x 53,2 (görünür sol kenar x 60), y 291–339 |
| Yazı | `@ydspublishing`, Lexend 700 42 px, renk `murekkep`, x 263, taban y 330 |
| Davranış | 0. kareden son kareye; opaklık 1; giriş/çıkış animasyonu yok; uçuş/geçiş dokunmaz; kimlik `kanal`; `__kalemKutu` türü `kunye`, ad `kunye:kanal` |
| Künye | y 360–450: konu `Simple Present` (Fredoka 700, x 60, taban 420; boy ≤ 34, rozetle x 960'a sığan en büyük, alt sınır 28) + rozet `YDT · BASIC` (hap y 386–434, Lexend 700 26, dolgu `vurguDolgu`, yazı `pilMetin`, konu sonu + 20) |
| Bantlar | üst 0–280 boş (çip YOK) · içerik 460–1380, x 60–960 · altyazı 1400–1550 (en çok 2 satır) · alt 1570–1920 boş |

Künye ortak dosyadan gelmez (paketin tek künye modülü yok): değerleri BRIEF-S3 "Kanal katmanı" tablosundan birebir al, elle başka değer yazma.
Canvas: `ortak/kunye.js` v2 olarak kurulu (S3-C kopyaladı; konu `Simple Present`, `KOK` = `/projeler/simple-present-temel-s3/ortak`; `kanalCiz`,
`kunyeCiz`, `altyaziCiz`, `KUNYE` v2 bantları). Sahne kodu onu içe aktarır; `ortak/kunye.js`'e dokunma (değişiklik gerekirse dur, raporla).

## Yaz
Tek sütun; yazı tabanı ≥ 64 mantıksal px (künye, kanal ve altyazı hariç; ikincil satır ve etiket ≥ 50); satır ≤ 24 karakter; tek vurgu
sarı (temaya göre); kırmızı (`#d6453a`) YALNIZ yanlış işaretinde: üstü çizili `es` ve `✗`; emoji yok (`✗`, `✓`, `?` ve simgeler SVG kalem çizimidir); sarı hap açık temada dolgu `vurguDolgu`
(`#ffe066`), yazı `pilMetin` (`#1b2440`); tema çifti (açık + koyu). Yasak (standart §1): "Tam ders" sözü, süre sözü ("dakika"), QR,
"izle" düğmesi taklidi.

Bu sahneye özel:
- Kare 0 (3,89): kart `He doesn't goes.` x 60, y 480–640, Fredoka 80: sahne 01 son karesiyle aynı konum ve boy (D-01 aynı sabiti yazar).
- 6,28 `does`: karttaki `doesn't` içinde `does` sarı kalem dairesi.
- 7,24 `s`: `goes`'un `es` ekinden `does`'a kavisli kalem oku; ekranda ayırım `go-es` → `do-es` (ana ders `go-es` ayırımı). Ok `es`'ten çıkar,
  yalnız `s`'ten DEĞİL (jüri dil 1 + kaynak 1).
- 8,99 `s` (cümlenin ikinci `s`'i): `goes` içindeki `es` eki BİRLİKTE kırmızı kalemle üstü çizilir (`go` + çizili `es`; kartta asla `goe` kalmaz).
  9,23 `gelmez.`: kartın sağında kırmızı kalem `✗` (SVG). `does` dairesi mürekkebe döner.
- 10,36 `He`: çizili `es` düşer ve solar; `✗` silinir. Kart 1 `He doesn't go.` (Fredoka 72) + altında soluk TR `O gitmez.` (Caveat 52, ikincil),
  y ≈ 480–700. Kart karaoke EN parçada (`He` 10,36 · `doesn't` 10,60 · `go.` 11,16); 11,16'da `go` altına sarı kalem altçizgisi.
- 11,96 `Does`: kart 2 `Does she go?` (Fredoka 72) + soluk TR `O gider mi?` (Caveat 52), y ≈ 760–980; karaoke `Does` 11,96 · `she` 12,20 ·
  `go?` 12,36; sarı altçizgi kart 2'nin `go`'suna geçer (aynı anda tek sarı).
- Yerleşim: bütün içerik x 60–960, y 460–1380. Kartlar 900 px'e sığar; sığmazsa yazı boyu değil kart iç payı küçülür (yazı ≥ 64, soluk TR ≥ 50).
  Küçük üstü çizili `goes` notu YOK (jüri kaynak 7).
- Altyazı + karaoke 1400–1550 (TR parçalar: `Olumsuzda … geçer.`, `Fiile s gelmez.`). Çip yok.

## Doğrula (zorunlu, geçmeden bitirme)
1. `cd K && bash araclar/qa-yerel.sh simple-present-temel-s3 02-paperjs-deger 3.95,8.40,12.75 8.40 --hazirla` → çıkış 0. t değerleri KÜRESEL anlatım saniyesidir (yerel değil;
   yerel kare = round((t − 3,89) × 30)): ilk kare 3,95, orta 8,40, son kare 12,75; koyu tema 8.40. qa-yerel ya da kapı dikey paketi ölçemiyorsa dur ve hatayı aynen
   raporla; aracı değiştirme.
2. Çakışma kapısı: `cd K && node araclar/cakisma-kapisi.mjs simple-present-temel-s3 --sahne 02-paperjs-deger --port 41333 --sunucu 41022` → çıkış 0, 0 uyarı.
3. Metin taraması: `grep -rniE 'tam ders|dakika' K/projeler/simple-present-temel-s3/sahneler/02-paperjs-deger/ --include=*.html --include=*.js --include=*.py` boş.
4. Kanal katmanı: QA karelerinin hepsinde görünür, konum ve boy tablodakiyle aynı (karede ölç; standart §7 madde 2).
Üretilen PNG'lere (`sahneler/02-paperjs-deger/k/`, `k/koyu/`) Read ile BAK: taşma, kesik yazı, üst üste binme, okunmaz kontrast, boş kare,
0–280 ve 1570–1920 boş mu, sağ 960–1080 bölgesinde içerik var mı. En çok 4 düzeltme turu; geçmezse dur ve raporla.

## Rapor
`sahneler/02-paperjs-deger/RAPOR.md`: olay listesi, kapı sonuçları (son satırlar), bakılan kareler ve bulgu, agy koşu özeti yolu, açık noktalar.
Son mesajın en çok 10 satır: kapı çıkış kodları, kare yolları, agy koşu özeti, açık noktalar.
