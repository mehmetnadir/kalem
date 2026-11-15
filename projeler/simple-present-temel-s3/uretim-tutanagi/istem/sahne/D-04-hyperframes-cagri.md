# İstem D — simple-present-temel-s3 sahne 04-hyperframes-cagri (huni v2) · 15.11.2026

<!-- P0202-S3-C (15.11) yazdı. Şablon: emsal `K/projeler/02-04-ydt-temel-s1/uretim-tutanagi/istem/sahne-v2/D-03-hyperframes-cta.md`. -->

MAKİNE: Linux x86_64 (srv21), kullanıcı sef. K=`/home/sef/01dev/_worktrees/kalem-0204` (git worktree, dal `sunucu/02-04-ydt-temel`),
D=`/home/sef/01dev/dijital-anlatim`. Node `~/.nvm/versions/node/v24.22.2/bin`. Python `/usr/bin/python3 -I`. Skill `~/.claude/skills/motion-grafik-ders/`.
KURALLAR: Yalnız bu sahnenin dizinine yaz: `K/projeler/simple-present-temel-s3/sahneler/04-hyperframes-cagri/` (klasör yeni; sen açarsın). Başka sahneye, `ortak/`a,
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
üzerine yazman gerekirse önce `~/Silinecekler/2026-11-15-0204/simple-present-temel-s3/sahneler/04-hyperframes-cagri/` altına kopyala.

## Okuma
1. `D/.claude/docs/huni-v2-standart.md` (tamamı; BAĞLAYICI: §1 kurallar, §2 yerleşim, §3 yapı, §6 türevler, §7 kapı).
2. Skill `SKILL.md`, `references/kalem-hatti.md`, `stil-anayasasi.md`, `hareket-sozlugu.md`, `kliseler.md`.
3. Paket: `K/projeler/simple-present-temel-s3/BRIEF-S3.md` ("Yerleşim", "Kanal katmanı" tablosu, "Sahneler" satırı: `| 4 Çağrı | 04-hyperframes-cagri | HyperFrames | 18,10–25,08 | 239 | öğrenci |`; "Sahne içeriği" 18,10–25,08 satırları), `zaman.json`
   (`sahneler[]`, `hikaye`, `duragan[]`), `ortak/anlatim/senaryo.json` + `sozcukler.json` + `baslar.json` + `altyazi.json` (cümle 4 (öğrenci sesi): `Bu` 18,65 · `sadece` 18,89 · `başlangıç.` 19,45 · `Dersin` 20,56 · `tamamı` 21,12 · `YDS` 21,84 · `Publishing` 22,32 · `YouTube` 22,96 · `kanalında.` 23,36–24,08),
   `uretim-tutanagi/S3-C-RAPOR.md`, `uretim-tutanagi/S3-duzeltme.md`, `uretim-tutanagi/senaryo-taslak.md` §2 sahne 4 satırı, `D/.claude/docs/kapak-standardi.md` (ana kapak dosyası).
4. Kod tabanı (emsal v2, yalnız okunur): `K/projeler/02-04-ydt-temel-s1/sahneler/03-hyperframes-cta/` (v2 çağrı sahnesi: ana kapak kartı, öğrenci cümlesi; `calistir.sh`, `olay.py`, `yardim.py`, `uret.py`, `zamanlar.json`, `nesneler.json`, `olaylar.json`). `calistir.sh`, `olay.py`, `yardim.py` kopyalanır (paket, klasör, çıktı adı ve konu metni Edit ile); `uret.py` içerik farklı → SPEC + agy.

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
- ÖNCE kapak: `K/projeler/simple-present-temel-s3/ortak/kapak/ana-kapak.png` ve `ana-kapak-koyu.png` var mı bak (S3-C kopyaladı; kaynak
  `K/projeler/simple-present-temel/kapak.png`, `kapak-koyu.png`, 1920×1080; md5 `b51ced1b…` açık). Biri yoksa DUR: başka dosya yazma,
  `RAPOR.md`'ye ve son mesaja "ana kapak bekliyor" yaz (standart §7 madde 5). Ana derse yazma.
- 18,65–19,45: `Bu sadece başlangıç.` Fredoka 700 (≈ 64–96, 900 px'e sığan), y ≈ 470–590, sözcük zamanlı (`Bu` 18,65 · `sadece` 18,89 ·
  `başlangıç.` 19,45). Öğrenci sesi.
- 20,56 `Dersin`: ana kapak 16:9 kart 900×506, x 60–960, y 620–1126 (jüri kaynak 5: 920 değil); köşe yarıçapı 24, `murekkep` kenar 4 px kalemle
  çizilir, iç görsel 0,3 sn'de belirir, sonra sabit; tema uyumlu (açık → `ana-kapak.png`, koyu → `ana-kapak-koyu.png`; `hf_tema.py` logo
  geçişi gibi `href` değişimi).
- 21,84 `YDS`: `@ydspublishing` sarı hap (Lexend 700 ≈ 56; tek vurgu), y ≈ 1180–1260. 22,96 `YouTube`: hapın yanında `· YouTube` (Lexend 700, `murekkep`).
- Altyazı 1400–1550: öğrenci cümlesi konuşma balonu biçiminde (ana ders sahne 06 öğrenci balonu; ses değişimi gözle görünür). Figür yok.
- 24,08–25,08 durgun kuyruk. Yasak: "Tam ders", süre, saat simgesi, oynat/izle düğmesi taklidi, YouTube logosu taklidi, QR. Çip yok.

## Doğrula (zorunlu, geçmeden bitirme)
1. `cd K && bash araclar/qa-yerel.sh simple-present-temel-s3 04-hyperframes-cagri 18.15,21.60,25.00 25.00 --hazirla` → çıkış 0. t değerleri KÜRESEL anlatım saniyesidir (yerel değil;
   yerel kare = round((t − 18,10) × 30)): ilk kare 18,15, orta 21,60, son kare 25,00; koyu tema 25.00. qa-yerel ya da kapı dikey paketi ölçemiyorsa dur ve hatayı aynen
   raporla; aracı değiştirme.
2. Çakışma kapısı: `cd K && node araclar/cakisma-kapisi.mjs simple-present-temel-s3 --sahne 04-hyperframes-cagri --port 41333 --sunucu 41022` → çıkış 0, 0 uyarı.
3. Metin taraması: `grep -rniE 'tam ders|dakika' K/projeler/simple-present-temel-s3/sahneler/04-hyperframes-cagri/ --include=*.html --include=*.js --include=*.py` boş.
4. Kanal katmanı: QA karelerinin hepsinde görünür, konum ve boy tablodakiyle aynı (karede ölç; standart §7 madde 2).
Üretilen PNG'lere (`sahneler/04-hyperframes-cagri/k/`, `k/koyu/`) Read ile BAK: taşma, kesik yazı, üst üste binme, okunmaz kontrast, boş kare,
0–280 ve 1570–1920 boş mu, sağ 960–1080 bölgesinde içerik var mı. En çok 4 düzeltme turu; geçmezse dur ve raporla.

## Rapor
`sahneler/04-hyperframes-cagri/RAPOR.md`: olay listesi, kapı sonuçları (son satırlar), bakılan kareler ve bulgu, agy koşu özeti yolu, açık noktalar.
Son mesajın en çok 10 satır: kapı çıkış kodları, kare yolları, agy koşu özeti, açık noktalar.
