# İstem D-V2 — simple-present-temel-s2 sahne 04-hyperframes-cagri (huni v2) · 15.11.2026

<!-- S2-C (15.11) yazdı. Şablon: K/projeler/02-04-ydt-temel-s1/uretim-tutanagi/istem/sahne-v2/D-03-hyperframes-cta.md. -->

MAKİNE: Linux x86_64 (srv21), kullanıcı sef. K=`/home/sef/01dev/_worktrees/kalem-0204` (git worktree, dal `sunucu/02-04-ydt-temel`),
D=`/home/sef/01dev/dijital-anlatim`. Node `~/.nvm/versions/node/v24.22.2/bin`. Python `/usr/bin/python3 -I`. Skill `~/.claude/skills/motion-grafik-ders/`.
KURALLAR: Yalnız bu sahnenin dizinine yaz: `K/projeler/simple-present-temel-s2/sahneler/04-hyperframes-cagri/` (klasör yeni; sen açarsın).
Ana ders kapağı hazırdır (S2-C kopyaladı): `ortak/kapak/ana-kapak.png` ve `ana-kapak-koyu.png` (kaynak `K/projeler/simple-present-temel/kapak.png`,
`kapak-koyu.png`, 1920×1080); sahne kendi `assets/` dizinine kopyalayabilir. Başka sahneye, `ortak/`a, `BRIEF-S2.md`'ye, `zaman.json`'a, ana derse
(`simple-present-temel`) ve emsale (`02-04-ydt-temel-s1`) dokunma (ikisi yalnız okunur); eksik görürsen raporla. Silme yok
(`~/Silinecekler/2026-11-15-0204/simple-present-temel-s2/` altına taşı). mp4 render YOK: `calistir.sh`'ı yalnız `ONIZLE_YALNIZ=1` ile koş.
git commit yok. Claude alt ajanı açma.
Kanca atlama bayrağı OLUŞTURMA (`/tmp/conductor-*`, `~/.conductor/*`). Durdurma kancası sözleşme satırı isterse `K/.claude/docs/sozlesme.md`
dosyasına 1–2 satır EKLE (tek istisna).

## Kod yolu (kapı ve doktrin)
Kod yazma kapısı 15 satırdan uzun kod dosyasını sana kapatır; bayrak açmaya çalışma. Emsal çağrı sahnesi aynı düzendedir: dosyaları
(`calistir.sh`, `olay.py`, `yardim.py`, `uret.py`, `assets/`) `cp -p` ile kopyala, küçük Edit ile kur (paket adı, metin `Gerisi bizde.` →
`Bitmedi, gel.`, sözcük çapaları, kapak yolu). Değişiklik küçük Edit'i aşarsa (yeni düzen, yeni olay mantığı): tasarımı sahne dizininde
`SPEC.md` olarak yaz (yazılacak dosyanın mutlak yolu, var olan kodun mutlak yolu ve oradan alınacak kalıp, olay listesi olay · kare/küresel sn ·
cümle sözcüğü, yerleşim, ekran metni, kurallar, kabul ölçütü; tam kod YAZMA). Sonra
`agy-filo tek --rol kod --cwd /home/sef/01dev/_worktrees/kalem-0204 --zaman 25m -p "<SPEC.md mutlak yolunu oku ve uygula. Yalnız <dosya
mutlak yolu> dosyasını yaz. Başka dosyaya dokunma. Silme yok. Test, render, git yok.>"`. Kodu agy yazar; sen baştan sona okur, spec'e
uyuyor mu bakarsın, küçük düzeltmeyi Edit ile yaparsın, büyük düzeltmeyi agy'ye geri verirsin (en çok 2 tur). Tam kodu kendin yazıp
agy'ye birebir kopyalatmak YASAK.

## Okuma
1. `D/.claude/docs/huni-v2-standart.md` (tamamı; BAĞLAYICI: §1 kural 2, 3, 7; §2 yerleşim; §3 "4 Çağrı"; §4 söz kalıpları; §7 kapı 4–5).
2. Skill `SKILL.md`, `references/kalem-hatti.md`, `stil-anayasasi.md`, `hareket-sozlugu.md`, `kliseler.md`.
3. Paket: `K/projeler/simple-present-temel-s2/BRIEF-S2.md` ("Yerleşim", "Kanal katmanı" tablosu, "Sahneler" satırı:
   `| 4 Çağrı | 04-hyperframes-cagri | HyperFrames | 19,07–25,73 | 230 | öğrenci |`; "Sahne içeriği" 19,07–25,73 satırları), `zaman.json`,
   `ortak/anlatim/senaryo.json` + `sozcukler.json` + `baslar.json` + `altyazi.json` (cümle 4, öğrenci sesi: `Bitmedi,` 19,62 · `gel.` 20,58–21,06 ·
   `Dersin` 21,21 · `tamamı` 21,77 · `YDS` 22,49 · `Publishing` 22,97 · `YouTube` 23,61 · `kanalında.` 24,01–24,81; cümle bitişi 24,73),
   `uretim-tutanagi/S2-C-RAPOR.md`, `uretim-tutanagi/senaryo-taslak.md` §2 sahne 4.
4. Kod tabanı (yalnız okunur): emsal v2 `K/projeler/02-04-ydt-temel-s1/sahneler/03-hyperframes-cta/` (aynı düzen: ana kapak kartı, giriş sözü,
   `@ydspublishing · YouTube`; `RAPOR.md` kapı sonuçları).
5. Sözleşme `K/.claude/docs/sozlesme.md` huni v2 satırları (ana kapak iki `<image>` + `.tema-acik #id`; `#root.tema-acik` dizgisi yazılmaz).

## Kanal katmanı ve künye (bütün sahnelerde AYNI; değer değiştirme)
| Öğe | Değer |
|---|---|
| Logo | `ortak/logo/` (açık `yds-publishing-lacivert.svg`, koyu `yds-publishing-seffaf.svg`); yükseklik 48, genişlik 193,5; resim x 53,2 (görünür sol kenar x 60), y 291–339 |
| Yazı | `@ydspublishing`, Lexend 700 42 px, renk `murekkep`, x 263, taban y 330 |
| Davranış | 0. kareden son kareye; opaklık 1; giriş/çıkış animasyonu yok; uçuş/geçiş dokunmaz; kimlik `kanal`; `__kalemKutu` türü `kunye`, ad `kunye:kanal` |
| Künye | y 360–450: konu `Simple Present` (Fredoka 700, x 60, taban 420; boy ≤ 34, rozetle x 960'a sığan en büyük, alt sınır 28) + rozet `YDT · BASIC` (hap y 386–434, Lexend 700 26, dolgu `vurguDolgu`, yazı `pilMetin`, konu sonu + 20) |
| Bantlar | üst 0–280 boş (çip YOK) · içerik 460–1380, x 60–960 · altyazı 1400–1550 (en çok 2 satır) · alt 1570–1920 boş |

Künye ortak dosyadan gelmez (HF sahnelerinin tek künye modülü yok): değerleri BRIEF-S2 "Kanal katmanı" tablosundan birebir al, elle başka değer
yazma. HyperFrames: emsalin v2 `yardim.py` `kunye_svg()` kopyasıyla kur; konu adı `Simple Present`. `hf_tema.py` logo `href` değişimi `#logoimg`
kimliğini arar (tema geçişi bozulmaz).

## Yaz
Tek sütun; yazı tabanı ≥ 64 mantıksal px (künye, kanal ve altyazı hariç); satır ≤ 24 karakter; tek vurgu sarı (temaya göre), doğru
yeşil, kırmızı yok, emoji yok; sarı hap açık temada dolgu `vurguDolgu` (`#ffe066`), yazı `pilMetin` (`#1b2440`); tema çifti (açık + koyu;
koyu kare de QA'ya girer). Yasak (standart §1): "Tam ders" sözü, süre sözü ("dakika"), QR, "izle" düğmesi taklidi.

Bu sahneye özel (sn KÜRESEL):
- ÖNCE kapak: `K/projeler/simple-present-temel-s2/ortak/kapak/ana-kapak.png` ve `ana-kapak-koyu.png` var mı bak (S2-C 19:03'te kopyaladı).
  Biri yoksa DUR: başka dosya yazma, `RAPOR.md`'ye ve son mesaja "ana kapak bekliyor" yaz.
- Kart: ana kapak 16:9, 900×506, x 60–960, y 620–1126 (standart ≈ 920×518; x 960 sınırı için 900); köşe yarıçapı 24, `murekkep` kenar 4 px;
  tema uyumlu (açık → `ana-kapak.png`, koyu → `ana-kapak-koyu.png`). Giriş 19,07–19,62 tek hareket (ölçek 0,94 → 1 + saydamlık), sonra sabit.
- `Bitmedi, gel.` Fredoka 700 (≈ 96 px, 900 px'e sığan), y ≈ 470–590, sözcük zamanlı (`Bitmedi,` 19,62 · `gel.` 20,58).
- `@ydspublishing · YouTube` Lexend 700 ≈ 56, y ≈ 1160–1240, `YDS` çapasında (22,49); `@ydspublishing` sarı hapta (tek vurgu), `YouTube` mürekkep.
- Yasak: "Tam ders", süre, saat simgesi, oynat/izle düğmesi taklidi, YouTube logosu taklidi, QR.
- Altyazı + karaoke 1400–1550 (cümle 4). Kuyruk 24,73–25,73 durgun. Çip yok.

## Doğrula (zorunlu, geçmeden bitirme)
1. `cd K && bash araclar/qa-yerel.sh simple-present-temel-s2 04-hyperframes-cagri 19.15,23.00,25.68 25.68 --hazirla` → çıkış 0. t değerleri
   KÜRESEL anlatım saniyesidir (yerel değil): ilk kare 19,15, orta 23,00, son kare 25,68; koyu tema 25.68. qa-yerel ya da kapı dikey paketi
   ölçemiyorsa dur ve hatayı aynen raporla; aracı değiştirme.
2. Çakışma kapısı: `cd K && node araclar/cakisma-kapisi.mjs simple-present-temel-s2 --sahne 04-hyperframes-cagri --port 41333 --sunucu 41022`
   → çıkış 0, 0 uyarı.
3. Metin taraması: `grep -rniE 'tam ders|dakika' K/projeler/simple-present-temel-s2/sahneler/04-hyperframes-cagri/ --include=*.html --include=*.js --include=*.py` boş.
4. Kanal katmanı: QA karelerinin hepsinde görünür, konum ve boy tablodakiyle aynı (karede ölç; standart §7 madde 2). Son karede ana ders
   kapağı görünür (standart §7 madde 5).
Üretilen PNG'lere (`sahneler/04-hyperframes-cagri/k/`, `k/koyu/`) Read ile BAK: taşma, kesik yazı, üst üste binme, okunmaz kontrast, boş kare,
0–280 ve 1570–1920 boş mu, sağ 960–1080 bölgesinde içerik var mı. En çok 4 düzeltme turu; geçmezse dur ve raporla.

## Rapor
`sahneler/04-hyperframes-cagri/RAPOR.md`: olay listesi, kapı sonuçları (son satırlar), bakılan kareler ve bulgu, agy koşu özeti yolu, açık
noktalar. Son mesajın en çok 10 satır: kapı çıkış kodları, kare yolları, agy koşu özeti, açık noktalar.
