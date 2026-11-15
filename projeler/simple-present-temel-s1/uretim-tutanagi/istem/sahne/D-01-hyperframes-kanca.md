# İstem D-S1 — simple-present-temel-s1 sahne 01-hyperframes-kanca (huni v2) · 15.11.2026

<!-- P0202-S1-C (15.11) yazdı. Şablon: K/projeler/02-04-ydt-temel-s1/uretim-tutanagi/istem/sahne-v2/D-01-hyperframes-kapak.md. Paket yeni: sahne kodu yok. -->

MAKİNE: Linux x86_64 (srv21), kullanıcı sef. K=`/home/sef/01dev/_worktrees/kalem-0204` (git worktree, dal `sunucu/02-04-ydt-temel`),
D=`/home/sef/01dev/dijital-anlatim`. Node `~/.nvm/versions/node/v24.22.2/bin`. Python `/usr/bin/python3 -I`. Skill `~/.claude/skills/motion-grafik-ders/`.
KURALLAR: Yalnız bu sahnenin dizinine yaz: `K/projeler/simple-present-temel-s1/sahneler/01-hyperframes-kanca/` (klasör yeni; sen açarsın). Ek çıktı (kapak A, tek kare PNG): paket kökü `kapak-a.png` + `kapak.png` (aynı dosya, `cp -p`) ve `sahneler/01-hyperframes-kanca/k/koyu/kapak-a-koyu.png`. Başka sahneye, `ortak/`a,
`BRIEF-S1.md`'ye, `zaman.json`'a, emsale (`02-04-ydt-temel-s1`) ve ana derse (`simple-present-temel`) dokunma (yalnız okunur); eksik görürsen raporla.
Silme yok (`~/Silinecekler/2026-11-15-huni-v2/simple-present-temel-s1/` altına taşı). mp4 render YOK: `calistir.sh`'ı yalnız `ONIZLE_YALNIZ=1` ile koş; kapak A için `hyperframes snapshot` tek kare serbest. git commit yok. Claude alt ajanı açma.
Kanca atlama bayrağı OLUŞTURMA (`/tmp/conductor-*`, `~/.conductor/*`). Durdurma kancası sözleşme satırı isterse `K/.claude/docs/sozlesme.md`
dosyasına 1–2 satır EKLE (tek istisna).

## Kod yolu (kapı ve doktrin)
Kod yazma kapısı 15 satırdan uzun kod dosyasını sana kapatır; bayrak açmaya çalışma. Yol: tasarımı sahne dizininde `SPEC.md` olarak
yaz (yazılacak dosyanın mutlak yolu, kopyalanacak emsal kodun mutlak yolu ve oradan alınacak kalıp, olay listesi olay · kare/küresel sn · cümle
sözcüğü, yerleşim, ekran metni, kurallar, kabul ölçütü; tam kod YAZMA). Sonra
`agy-filo tek --rol kod --cwd /home/sef/01dev/_worktrees/kalem-0204 --zaman 25m -p "<SPEC.md mutlak yolunu oku ve uygula. Yalnız <dosya
mutlak yolu> dosyasını yaz. Başka dosyaya dokunma. Silme yok. Test, render, git yok.>"`. Kodu agy yazar; sen baştan sona okur, spec'e
uyuyor mu bakarsın, küçük düzeltmeyi Edit ile yaparsın, büyük düzeltmeyi agy'ye geri verirsin (en çok 2 tur). Tam kodu kendin yazıp
agy'ye birebir kopyalatmak YASAK. Emsal dosyaları `cp -p` ile kopyalanır ve kısa Edit ile kurulur (paket adı, klasör adı, çıktı adı);
kısa dosyalar (`calistir.sh`, `sayfa.html`) Edit ile yazılabilir. Emsalde v1'den kalan "çevir" adımları bu pakette "kur" adımıdır:
eski sürüm yok, yedek gerekmez.

## Okuma
1. `D/.claude/docs/huni-v2-standart.md` (tamamı; BAĞLAYICI: §1 kurallar, §2 yerleşim, §3 yapı, §6 türevler, §7 kapı).
2. Skill `SKILL.md`, `references/kalem-hatti.md`, `stil-anayasasi.md`, `hareket-sozlugu.md`, `kliseler.md`.
3. Paket: `K/projeler/simple-present-temel-s1/BRIEF-S1.md` ("Yerleşim", "Kanal katmanı" tablosu, "Sahneler" satırı: `| 1 Kanca | 01-hyperframes-kanca | HyperFrames | 0,00–3,00 | 102 | öğretmen |`; "Sahne içeriği" 0,00–2,52 satırları; "Kapak" bölümü), `zaman.json`
   (`sahneler[]`, `hikaye`, `duragan[]`), `ortak/anlatim/senaryo.json` + `sozcukler.json` + `baslar.json` + `altyazi.json` (cümle 1: `Kardeşim` 1,00 · `gider:` 1,56–2,24 · `go` 2,52 · `mu,` 2,84 (02'de); olay söylendiği anda gelir, zaman sözcük çapasından),
   `uretim-tutanagi/S1-C-RAPOR.md`, `uretim-tutanagi/senaryo-taslak.md` §2 sahne 1, `uretim-tutanagi/kapak-taslak.md` §2–§3 ve §6.
4. Kod tabanı (paket yeni): yapı ve v2 düzeni emsal `K/projeler/02-04-ydt-temel-s1/sahneler/01-hyperframes-kapak/` (`uret.py`, `yardim.py`, `olay.py`, `calistir.sh`, `SPEC.md`; kapak A yöntemi `proje-ka/`); bu dersin eski kısa kapağı `~/Silinecekler/2026-11-15-huni-v2/simple-present-temel-s1-eski/sahneler/01-hyperframes-kapak/` yalnız içerik ve varlık kaynağıdır (eski başlık `GİDER` / `= GOES` ALINMAZ). Emsal sahnenin `RAPOR.md`'si "huni v2" diyorsa v2 hâlidir: onu taban al. Demiyorsa v1'dir: dosya yapısını al, v2 yerleşimini ve kanal katmanını bu istemle kur.

## Kanal katmanı ve künye (bütün sahnelerde AYNI; değer değiştirme)
| Öğe | Değer |
|---|---|
| Logo | `ortak/logo/` (açık `yds-publishing-lacivert.svg`, koyu `yds-publishing-seffaf.svg`); yükseklik 48, genişlik 193,5; resim x 53,2 (görünür sol kenar x 60), y 291–339 |
| Yazı | `@ydspublishing`, Lexend 700 42 px, renk `murekkep`, x 263, taban y 330 |
| Davranış | 0. kareden son kareye; opaklık 1; giriş/çıkış animasyonu yok; uçuş/geçiş dokunmaz; kimlik `kanal`; `__kalemKutu` türü `kunye`, ad `kunye:kanal` |
| Künye | y 360–450: konu `Simple Present` (Fredoka 700, x 60, taban 420; boy ≤ 34, rozetle x 960'a sığan en büyük, alt sınır 28) + rozet `YDT · BASIC` (hap y 386–434, Lexend 700 26, dolgu `vurguDolgu`, yazı `pilMetin`, konu sonu + 20) |
| Bantlar | üst 0–280 boş (çip YOK) · içerik 460–1380, x 60–960 · altyazı 1400–1550 (en çok 2 satır) · alt 1570–1920 boş |

Değerleri BRIEF-S1 "Kanal katmanı" tablosundan birebir al; elle başka değer yazma.

HyperFrames: emsalden kopyaladığın `yardim.py`'de `kunye_svg()` v2 düzeninde kurulur: `<g id="kanal">` (logo `<image id="logoimg">` + `@ydspublishing` `<text>`) ve künye satırı (y 360–450); bantlar v2 (kenar 60, sağ sınır 960, içerik 460–1380, altyazı 1400–1550). `hf_tema.py` logo `href` değişimi `#logoimg` kimliğini arar (tema geçişi bozulmaz).

## Yaz
Tek sütun; yazı tabanı ≥ 64 mantıksal px (künye, kanal ve altyazı hariç); satır ≤ 24 karakter; tek vurgu sarı (temaya göre), doğru
yeşil, kırmızı yalnız sahne 02'deki `s` yuvası çizgisi (ana ders `K/projeler/simple-present-temel/BRIEF.md` satır 159), emoji yok; sarı hap açık
temada dolgu `vurguDolgu` (`#ffe066`), yazı `pilMetin` (`#1b2440`); tema çifti zorunlu: açık + koyu (koyu tema QA karesi ayrı bakılır).
Yasak (standart §1): kural 4'teki eski kapanış sözü, süre sözü, QR, "izle" düğmesi taklidi, YouTube logosu taklidi.

Bu sahneye özel:
- Başlık `GO mu,` / `GOES mu?` (satır 2 sarı hap); 900 px'e sığan en büyük boy, üst sınır 190; `mu` küçük harf. Altında solda genç figür (`ortak/cizim/open-peeps/standing-2.svg`, kalem çizimi, sola dönük), sağda otobüs (`ortak/cizim/coco/bus.svg`, sola gider); etiket yok (ekran metni sesten önce gelmez; tek istisna başlık). Başlık + görsel y 460–1380, x 60–960; künye satırında 0. karede yalnız rozet.
- 0,30–0,80: başlıktaki `?` kalemle çizilir; başka kalem hareketi yok. Kanal katmanı 0. karede tam görünür (kapak = ilk kare); uçuşta oynamaz.
- 1,90–2,45 uçuş: başlık künye konu adına (`Simple Present`, y 360–450) döner; figür + otobüs küçülür (yükseklik ≤ 140), x 700–960, y 460–600.
- 2,45: Caveat 700 72 `Kardeşim gider:` (mürekkep, x 60, taban y 560). 2,52 (`go` çapası): kart `go` (Fredoka 700 ≥ 96; x 60–440, y 620–820).
- Uçuş sonu durum = sahne 02 kare 0 (02 istemi aynı sabitleri kullanır: `Kardeşim gider:` taban 560 · kart satırı y 620–820 · `go` x 60–440 · figür + otobüs x 700–960, y 460–600). Değer değiştirirsen RAPOR'a yaz.
- Altyazı + karaoke 1400–1550 (cümle 1).
- Kapak A (QA geçtikten sonra): kanca karesi t 0,90 (kare 27: başlık tam, `?` çizilmiş, ilk söz ve altyazı yok; sahne değiştiyse başlık + görselin tam göründüğü ve altyazının olmadığı son kare), altyazı katmanı gizli. Yöntem S1-KAPAK-A: `proje` kopyasında yalnız CSS `#altyazi{display:none}`, `hyperframes snapshot --at <t>`, açık ve koyu ayrı (emsal `uretim-tutanagi/S1-VAR-RAPOR.md` satır 101). Açık → paket kökü `kapak-a.png`, `cp -p kapak-a.png kapak.png`; koyu → `k/koyu/kapak-a-koyu.png`. Karede kanal katmanı var.

## Doğrula (zorunlu, geçmeden bitirme)
1. `cd K && bash araclar/qa-yerel.sh simple-present-temel-s1 01-hyperframes-kanca 0.00,1.50,2.95 1.50 --hazirla` → çıkış 0. t değerleri KÜRESEL anlatım
   saniyesidir (yerel değil; yerel kare = round((t − t_bas) × 30)): ilk kare 0,00, orta 1,50, son kare 2,95; koyu tema 1.50.
   qa-yerel ya da kapı dikey paketi ölçemiyorsa dur ve hatayı aynen raporla; aracı değiştirme.
2. Çakışma kapısı: `cd K && node araclar/cakisma-kapisi.mjs simple-present-temel-s1 --sahne 01-hyperframes-kanca --port 41333 --sunucu 41022` → çıkış 0, 0 uyarı.
3. Metin taraması: `grep -rniE 'tam[ ]ders|dak[i]ka' K/projeler/simple-present-temel-s1/sahneler/01-hyperframes-kanca/ --include=*.html --include=*.js --include=*.py` boş.
4. Kanal katmanı: QA karelerinin hepsinde görünür, konum ve boy tablodakiyle aynı (karede ölç; standart §7 madde 2).
Üretilen PNG'lere (`sahneler/01-hyperframes-kanca/k/`, `k/koyu/`) Read ile BAK: taşma, kesik yazı, üst üste binme, okunmaz kontrast, boş kare,
0–280 ve 1570–1920 boş mu, sağ 960–1080 bölgesinde içerik var mı. En çok 4 düzeltme turu; geçmezse dur ve raporla.

## Rapor
`sahneler/01-hyperframes-kanca/RAPOR.md`: olay listesi, kapı sonuçları (son satırlar), bakılan kareler ve bulgu, agy koşu özeti yolu, açık noktalar.
Son mesajın en çok 10 satır: kapı çıkış kodları, kare yolları, agy koşu özeti, açık noktalar.
