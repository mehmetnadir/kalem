# İstem D — simple-present-temel-s3 sahne 03-hyperframes-kaydet (huni v2) · 15.11.2026

<!-- P0202-S3-C (15.11) yazdı. Şablon: emsal `K/projeler/02-04-ydt-temel-s1/uretim-tutanagi/istem/sahne-v2/D-08-hyperframes-kaydet.md`. -->

MAKİNE: Linux x86_64 (srv21), kullanıcı sef. K=`/home/sef/01dev/_worktrees/kalem-0204` (git worktree, dal `sunucu/02-04-ydt-temel`),
D=`/home/sef/01dev/dijital-anlatim`. Node `~/.nvm/versions/node/v24.22.2/bin`. Python `/usr/bin/python3 -I`. Skill `~/.claude/skills/motion-grafik-ders/`.
KURALLAR: Yalnız bu sahnenin dizinine yaz: `K/projeler/simple-present-temel-s3/sahneler/03-hyperframes-kaydet/` (klasör yeni; sen açarsın). Başka sahneye, `ortak/`a,
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
üzerine yazman gerekirse önce `~/Silinecekler/2026-11-15-0204/simple-present-temel-s3/sahneler/03-hyperframes-kaydet/` altına kopyala.

## Okuma
1. `D/.claude/docs/huni-v2-standart.md` (tamamı; BAĞLAYICI: §1 kurallar, §2 yerleşim, §3 yapı, §6 türevler, §7 kapı).
2. Skill `SKILL.md`, `references/kalem-hatti.md`, `stil-anayasasi.md`, `hareket-sozlugu.md`, `kliseler.md`.
3. Paket: `K/projeler/simple-present-temel-s3/BRIEF-S3.md` ("Yerleşim", "Kanal katmanı" tablosu, "Sahneler" satırı: `| 3 Kaydet | 03-hyperframes-kaydet | HyperFrames | 12,84–18,10 | 170 | öğretmen |`; "Sahne içeriği" 12,84–18,10 satırları), `zaman.json`
   (`sahneler[]`, `hikaye`, `duragan[]`), `ortak/anlatim/senaryo.json` + `sozcukler.json` + `baslar.json` + `altyazi.json` (cümle 3: `Does` 13,39 · `varsa` 13,71 · `fiil` 14,35 · `yalın.` 14,75 · `Bir` 15,46 · `arkadaşına` 15,70 · `gönder;` 16,26 · `o` 17,02 · `karıştırıyor.` 17,30–18,10),
   `uretim-tutanagi/S3-C-RAPOR.md`, `uretim-tutanagi/S3-duzeltme.md`, `uretim-tutanagi/senaryo-taslak.md` §2 sahne 3 satırı.
4. Kod tabanı (emsal v2, yalnız okunur): `K/projeler/02-04-ydt-temel-s1/sahneler/08-hyperframes-kaydet/` (aynı tür v2 sahne; koşu anında yoksa dosya yapısı için `K/projeler/02-04-ydt-temel-s1/sahneler/03-hyperframes-cta/`): `calistir.sh`, `olay.py`, `yardim.py`, `uret.py`, `zamanlar.json`, `nesneler.json`, `olaylar.json`. `calistir.sh`, `olay.py`, `yardim.py` kopyalanır (paket, klasör, çıktı adı ve konu metni Edit ile); `uret.py` içerik farklı → SPEC + agy. Sahne `zaman.json`'da var (no 3, kare 170 = içerik 158 + geçiş 12); `zaman.json`'a dokunma.

## Kanal katmanı ve künye (bütün sahnelerde AYNI; değer değiştirme)
| Öğe | Değer |
|---|---|
| Logo | `ortak/logo/` (açık `yds-publishing-lacivert.svg`, koyu `yds-publishing-seffaf.svg`); yükseklik 48, genişlik 193,5; resim x 53,2 (görünür sol kenar x 60), y 291–339 |
| Yazı | `@ydspublishing`, Lexend 700 42 px, renk `murekkep`, x 263, taban y 330 |
| Davranış | 0. kareden son kareye; opaklık 1; giriş/çıkış animasyonu yok; uçuş/geçiş dokunmaz; kimlik `kanal`; `__kalemKutu` türü `kunye`, ad `kunye:kanal` |
| Künye | y 360–450: konu `Simple Present` (Fredoka 700, x 60, taban 420; boy ≤ 34, rozetle x 960'a sığan en büyük, alt sınır 28) + rozet `YDT · BASIC` (hap y 386–434, Lexend 700 26, dolgu `vurguDolgu`, yazı `pilMetin`, konu sonu + 20) |
| Bantlar | üst 0–280 boş (çip YOK) · içerik 460–1380, x 60–960 · altyazı 1400–1550 (en çok 2 satır) · alt 1570–1920 boş |

Künye ortak dosyadan gelmez (paketin tek künye modülü yok): değerleri BRIEF-S3 "Kanal katmanı" tablosundan birebir al, elle başka değer yazma.
HyperFrames: kanal katmanını ve künye satırını emsal sahnenin v2 `yardim.py`'sinden kur (`kunye_svg()`: `<g id="kanal">` = logo `<image>` + `@ydspublishing` `<text>`; künye satırı y 360–450; v2 bant sabitleri). Kopyada yalnız konu metni (`Simple Present`), paket
adı ve yollar değişir. `hf_tema.py` logo `href` değişimi `#logoimg` kimliğini arar: kanal logosunun kimliği `logoimg` kalır.

## Yaz
Tek sütun; yazı tabanı ≥ 64 mantıksal px (künye, kanal ve altyazı hariç; ikincil satır ve etiket ≥ 50); satır ≤ 24 karakter; tek vurgu
sarı (temaya göre); kırmızı yok; emoji yok (`✗`, `✓`, `?` ve simgeler SVG kalem çizimidir); sarı hap açık temada dolgu `vurguDolgu`
(`#ffe066`), yazı `pilMetin` (`#1b2440`); tema çifti (açık + koyu). Yasak (standart §1): "Tam ders" sözü, süre sözü ("dakika"), QR,
"izle" düğmesi taklidi.

Bu sahneye özel:
- 12,84'te başlar (ilk 12 kare geçiş payı), 18,10'da biter.
- Kural özeti kartı, tek cümle iki satır: `Does varsa` / `fiil yalın.` (Fredoka 700 88; 900 px'e sığmazsa küçülür, alt sınır 64). Kâğıt kart +
  kalem kenarı (çerçeve 0,4 sn'de çizilir), x 60–960, y ≈ 560–900. Karaoke `Does` 13,39'dan; kart `yalın.` sonunda (15,31) tam;
  15,31–18,10 sabit, hareketsiz (2,79 sn; standart "≥ 2 sn sabit"). Kart içinde sarı yok.
- 15,46 `Bir`: yer imi simgesi (SVG yol; Tabler `bookmark` biçimi: dikdörtgen gövde + alt V çentik; yolu sahne içinde yaz; emoji değil)
  kalem darbesiyle ≤ 0,4 sn + yanında `Kaydet` sarı hap (Fredoka 700 64; sahnenin tek sarısı).
- 16,26 `gönder;`: kâğıt uçak simgesi (SVG yol; Tabler `send` biçimi; emoji değil) ≤ 0,4 sn + `Gönder` (Lexend 700 ≥ 50, `murekkep`, hapsız).
  `Kaydet` ve `Gönder` kartın altında yan yana, y ≈ 1000–1140, x 60–960 içinde.
- Hareket yalnız simgelerde; kart durgun. Sahne 02'nin örnek satırı (`doesn't go · Does she go?`) bu sahnede YOK (jüri kaynak 7).
- Altyazı + karaoke 1400–1550 (cümle 3). Çip yok.

## Doğrula (zorunlu, geçmeden bitirme)
1. `cd K && bash araclar/qa-yerel.sh simple-present-temel-s3 03-hyperframes-kaydet 12.90,16.60,18.00 16.60 --hazirla` → çıkış 0. t değerleri KÜRESEL anlatım saniyesidir (yerel değil;
   yerel kare = round((t − 12,84) × 30)): ilk kare 12,90, orta 16,60, son kare 18,00; koyu tema 16.60. qa-yerel ya da kapı dikey paketi ölçemiyorsa dur ve hatayı aynen
   raporla; aracı değiştirme.
2. Çakışma kapısı: `cd K && node araclar/cakisma-kapisi.mjs simple-present-temel-s3 --sahne 03-hyperframes-kaydet --port 41333 --sunucu 41022` → çıkış 0, 0 uyarı.
3. Metin taraması: `grep -rniE 'tam ders|dakika' K/projeler/simple-present-temel-s3/sahneler/03-hyperframes-kaydet/ --include=*.html --include=*.js --include=*.py` boş.
4. Kanal katmanı: QA karelerinin hepsinde görünür, konum ve boy tablodakiyle aynı (karede ölç; standart §7 madde 2).
Üretilen PNG'lere (`sahneler/03-hyperframes-kaydet/k/`, `k/koyu/`) Read ile BAK: taşma, kesik yazı, üst üste binme, okunmaz kontrast, boş kare,
0–280 ve 1570–1920 boş mu, sağ 960–1080 bölgesinde içerik var mı. En çok 4 düzeltme turu; geçmezse dur ve raporla.

## Rapor
`sahneler/03-hyperframes-kaydet/RAPOR.md`: olay listesi, kapı sonuçları (son satırlar), bakılan kareler ve bulgu, agy koşu özeti yolu, açık noktalar.
Son mesajın en çok 10 satır: kapı çıkış kodları, kare yolları, agy koşu özeti, açık noktalar.
