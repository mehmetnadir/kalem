# İstem D-V2 — simple-present-temel-s2 sahne 01-hyperframes-kanca (huni v2) · 15.11.2026

<!-- S2-C (15.11) yazdı. Şablon: K/projeler/02-04-ydt-temel-s1/uretim-tutanagi/istem/sahne-v2/D-01-hyperframes-kapak.md. -->

MAKİNE: Linux x86_64 (srv21), kullanıcı sef. K=`/home/sef/01dev/_worktrees/kalem-0204` (git worktree, dal `sunucu/02-04-ydt-temel`),
D=`/home/sef/01dev/dijital-anlatim`. Node `~/.nvm/versions/node/v24.22.2/bin`. Python `/usr/bin/python3 -I`. Skill `~/.claude/skills/motion-grafik-ders/`.
KURALLAR: Yalnız bu sahnenin dizinine yaz: `K/projeler/simple-present-temel-s2/sahneler/01-hyperframes-kanca/` (klasör yeni; sen açarsın). Ek çıktı
(kapak A, tek kare PNG): paket kökü `kapak-a.png` + `kapak.png` (aynı dosya, `cp -p`) ve `sahneler/01-hyperframes-kanca/k/koyu/kapak-a-koyu.png`.
Başka sahneye, `ortak/`a, `BRIEF-S2.md`'ye, `zaman.json`'a, ana derse (`simple-present-temel`) ve emsale (`02-04-ydt-temel-s1`) dokunma (ikisi
yalnız okunur); eksik görürsen raporla. Silme yok (`~/Silinecekler/2026-11-15-0204/simple-present-temel-s2/` altına taşı). mp4 render YOK:
`calistir.sh`'ı yalnız `ONIZLE_YALNIZ=1` ile koş; kapak A için `hyperframes snapshot` tek kare serbest. git commit yok. Claude alt ajanı açma.
Kanca atlama bayrağı OLUŞTURMA (`/tmp/conductor-*`, `~/.conductor/*`). Durdurma kancası sözleşme satırı isterse `K/.claude/docs/sozlesme.md`
dosyasına 1–2 satır EKLE (tek istisna).

## Kod yolu (kapı ve doktrin)
Kod yazma kapısı 15 satırdan uzun kod dosyasını sana kapatır; bayrak açmaya çalışma. Emsalden kopyalanan dosyalar (`calistir.sh`, `olay.py`,
`yardim.py`) `cp -p` + küçük Edit ile kurulur (paket adı, klasör adı, künye konu adı). Yeni içerik taşıyan kod (`uret.py`): tasarımı sahne
dizininde `SPEC.md` olarak yaz (yazılacak dosyanın mutlak yolu, var olan kodun mutlak yolu ve oradan alınacak kalıp, olay listesi olay ·
kare/küresel sn · cümle sözcüğü, yerleşim, ekran metni, kurallar, kabul ölçütü; tam kod YAZMA). Sonra
`agy-filo tek --rol kod --cwd /home/sef/01dev/_worktrees/kalem-0204 --zaman 25m -p "<SPEC.md mutlak yolunu oku ve uygula. Yalnız <dosya
mutlak yolu> dosyasını yaz. Başka dosyaya dokunma. Silme yok. Test, render, git yok.>"`. Kodu agy yazar; sen baştan sona okur, spec'e
uyuyor mu bakarsın, küçük düzeltmeyi Edit ile yaparsın, büyük düzeltmeyi agy'ye geri verirsin (en çok 2 tur). Tam kodu kendin yazıp
agy'ye birebir kopyalatmak YASAK.

## Okuma
1. `D/.claude/docs/huni-v2-standart.md` (tamamı; BAĞLAYICI: §1 kurallar, §2 yerleşim, §3 yapı, §6 türevler, §7 kapı).
2. Skill `SKILL.md`, `references/kalem-hatti.md`, `stil-anayasasi.md`, `hareket-sozlugu.md`, `kliseler.md`.
3. Paket: `K/projeler/simple-present-temel-s2/BRIEF-S2.md` ("Yerleşim", "Kanal katmanı" tablosu, "Sahneler" satırı:
   `| 1 Kanca | 01-hyperframes-kanca | HyperFrames | 0,00–3,00 | 102 | öğretmen |`; "Sahne içeriği" 0,00–3,00 satırları; "Kapak" bölümü),
   `zaman.json` (`sahneler[]`, `hikaye`, `duragan[]`), `ortak/anlatim/senaryo.json` + `sozcukler.json` + `baslar.json` + `altyazi.json`
   (cümle 1: `Usually` 1,00 · `görünce` 1,80 · `hangi` 2,60 · `zaman?` 2,92–3,48; olay söylendiği anda gelir, zaman sözcük çapasından),
   `uretim-tutanagi/S2-C-RAPOR.md`, `uretim-tutanagi/kapak-taslak.md` (§1, §3 ve en üstteki S2-C notu), `uretim-tutanagi/senaryo-taslak.md` §2 sahne 1.
4. Kod tabanı (yalnız okunur, emsal aynı rol, v2): `K/projeler/02-04-ydt-temel-s1/sahneler/01-hyperframes-kapak/` (`SPEC.md`, `uret.py`,
   `yardim.py`, `olay.py`, `calistir.sh`, `RAPOR.md`). İçerik farklı (başlık, takvim, figür); kanal katmanı, künye ve uçuş kalıbı oradan.
5. Sözleşme `K/.claude/docs/sozlesme.md` huni v2 satırları (kanal katmanı, kapak uçuşu: "HF huni v2 kapak uçuşu", `kunye_svg()`, `#logoimg`).

## Kanal katmanı ve künye (bütün sahnelerde AYNI; değer değiştirme)
| Öğe | Değer |
|---|---|
| Logo | `ortak/logo/` (açık `yds-publishing-lacivert.svg`, koyu `yds-publishing-seffaf.svg`); yükseklik 48, genişlik 193,5; resim x 53,2 (görünür sol kenar x 60), y 291–339 |
| Yazı | `@ydspublishing`, Lexend 700 42 px, renk `murekkep`, x 263, taban y 330 |
| Davranış | 0. kareden son kareye; opaklık 1; giriş/çıkış animasyonu yok; uçuş/geçiş dokunmaz; kimlik `kanal`; `__kalemKutu` türü `kunye`, ad `kunye:kanal` |
| Künye | y 360–450: konu `Simple Present` (Fredoka 700, x 60, taban 420; boy ≤ 34, rozetle x 960'a sığan en büyük, alt sınır 28) + rozet `YDT · BASIC` (hap y 386–434, Lexend 700 26, dolgu `vurguDolgu`, yazı `pilMetin`, konu sonu + 20) |
| Bantlar | üst 0–280 boş (çip YOK) · içerik 460–1380, x 60–960 · altyazı 1400–1550 (en çok 2 satır) · alt 1570–1920 boş |

Künye ortak dosyadan gelmez (HF sahnelerinin tek künye modülü yok): değerleri BRIEF-S2 "Kanal katmanı" tablosundan birebir al, elle başka değer
yazma. HyperFrames: emsalin v2 `yardim.py` `kunye_svg()` kopyasıyla kur: `<g id="kanal">` (logo `<image id="logoimg">` + `@ydspublishing` `<text>`)
+ künye satırı (y 360–450); konu adı `Simple Present`. `hf_tema.py` logo `href` değişimi `#logoimg` kimliğini arar (tema geçişi bozulmaz).

## Yaz
Tek sütun; yazı tabanı ≥ 64 mantıksal px (künye, kanal ve altyazı hariç); satır ≤ 24 karakter; tek vurgu sarı (temaya göre), doğru
yeşil, kırmızı yok, emoji yok; sarı hap açık temada dolgu `vurguDolgu` (`#ffe066`), yazı `pilMetin` (`#1b2440`); tema çifti (açık + koyu;
koyu kare de QA'ya girer). Yasak (standart §1): "Tam ders" sözü, süre sözü ("dakika"), QR, "izle" düğmesi taklidi.

Bu sahneye özel:
- 0. kare = kapak A, kanal katmanı + künye dahil tam görünür. Başlık `USUALLY` / `= ALIŞKANLIK` (satır 2 sarı hapta); 900 px'e sığan en büyük
  boy (üst sınır 190), iki satır aynı boy; y 460–800.
- Görsel y 820–1380, x 60–960: solda takvim yaprağı (`ortak/cizim/tabler/calendar.svg` biçimi, 5 gün kutusu el çizimi), sağda kalem çizgisi figür
  (`kadro.ogrenci`: kadın, genç, `LongBangs`, `GlassRound`; peeps-kit `ortak/cizim/peeps-kit/`) takvime işaret eder. Karakter görseli
  (`karakter.png`) bu sahnede YOK (S2-C: kapak C'ye geçti).
- 0,30–0,80: takvimde 5 kutudan 4'üne kalemle tik; 5. kutu boş kalır (`usually` ≠ her gün; jüri dil 1).
- Uçuş 2,40–3,00: başlık küçülerek künye satırının sağ boş bölümüne (konu + rozet sonrası, x ≈ 500–940, y ≈ 370–440) gider ve 3,00'te
  saydamlığı 0 olur; figür ve takvim aynı aralıkta solar. **Uçuşun bittiği yer** = bu sağ boş bölüm; **künyenin son metni** = `Simple Present`
  + `YDT · BASIC` (0. kareden beri yerinde, değişmez). Emsalden fark: emsalde künye konu adı uçuşla gelir; burada kapak A künyesi kapak B ve C
  ile aynıdır. Uçan başlık künye metni ve rozetle üst üste binmez (çakışma kapısı bu kareleri ölçer).
- Sahne 02 kare 0 (3,00) içerik bandı boştur (yalnız kanal + künye + altyazı); sahne 01'in son karesi buna uyar (devir: boş içerik bandı).
- Altyazı + karaoke 1400–1550 (cümle 1).
- Kapak A (QA geçtikten sonra): t 0,90 (kare 27: başlık tam, 4 tik bitmiş, ses başlamamış), altyazı katmanı gizli. Yöntem S1-KAPAK-A:
  `proje` kopyasında yalnız CSS `#altyazi{display:none}`, `hyperframes snapshot --at 0.90`, açık ve koyu ayrı. Açık → paket kökü `kapak-a.png`,
  `cp -p kapak-a.png kapak.png`; koyu → `k/koyu/kapak-a-koyu.png`. Karede kanal katmanı ve künye var.

## Doğrula (zorunlu, geçmeden bitirme)
1. `cd K && bash araclar/qa-yerel.sh simple-present-temel-s2 01-hyperframes-kanca 0.00,1.50,2.95 1.50 --hazirla` → çıkış 0. t değerleri KÜRESEL
   anlatım saniyesidir (yerel değil): ilk kare 0,00, orta 1,50, son kare 2,95; koyu tema 1.50. qa-yerel ya da kapı dikey paketi ölçemiyorsa dur
   ve hatayı aynen raporla; aracı değiştirme.
2. Çakışma kapısı: `cd K && node araclar/cakisma-kapisi.mjs simple-present-temel-s2 --sahne 01-hyperframes-kanca --port 41333 --sunucu 41022`
   → çıkış 0, 0 uyarı.
3. Metin taraması: `grep -rniE 'tam ders|dakika' K/projeler/simple-present-temel-s2/sahneler/01-hyperframes-kanca/ --include=*.html --include=*.js --include=*.py` boş.
4. Kanal katmanı: QA karelerinin hepsinde görünür, konum ve boy tablodakiyle aynı (karede ölç; standart §7 madde 2).
Üretilen PNG'lere (`sahneler/01-hyperframes-kanca/k/`, `k/koyu/`, paket kökü `kapak-a.png`) Read ile BAK: taşma, kesik yazı, üst üste binme,
okunmaz kontrast, boş kare, 0–280 ve 1570–1920 boş mu, sağ 960–1080 bölgesinde içerik var mı, 4 tik + 1 boş kutu. En çok 4 düzeltme turu;
geçmezse dur ve raporla.

## Rapor
`sahneler/01-hyperframes-kanca/RAPOR.md`: olay listesi, kapı sonuçları (son satırlar), bakılan kareler ve bulgu, agy koşu özeti yolu, açık
noktalar. Son mesajın en çok 10 satır: kapı çıkış kodları, kare yolları, agy koşu özeti, açık noktalar.
