# İstem D-S1 — simple-present-temel-s1 sahne 05-hyperframes-hikaye-a (huni v2) · 15.11.2026

<!-- P0202-S1-C (15.11) yazdı. Şablon: K/projeler/02-04-ydt-temel-s1/uretim-tutanagi/istem/sahne-v2/D-04-hyperframes-hikaye.md. Paket yeni: sahne kodu yok. -->

MAKİNE: Linux x86_64 (srv21), kullanıcı sef. K=`/home/sef/01dev/_worktrees/kalem-0204` (git worktree, dal `sunucu/02-04-ydt-temel`),
D=`/home/sef/01dev/dijital-anlatim`. Node `~/.nvm/versions/node/v24.22.2/bin`. Python `/usr/bin/python3 -I`. Skill `~/.claude/skills/motion-grafik-ders/`.
KURALLAR: Yalnız bu sahnenin dizinine yaz: `K/projeler/simple-present-temel-s1/sahneler/05-hyperframes-hikaye-a/` (klasör yeni; sen açarsın). Çıktı: paket kökü `hikaye-a.png` + `hikaye.png` (aynı dosya, `cp -p`) ve `k/koyu/hikaye-a-koyu.png`. Başka sahneye, `ortak/`a,
`BRIEF-S1.md`'ye, `zaman.json`'a, emsale (`02-04-ydt-temel-s1`) ve ana derse (`simple-present-temel`) dokunma (yalnız okunur); eksik görürsen raporla.
Silme yok (`~/Silinecekler/2026-11-15-huni-v2/simple-present-temel-s1/` altına taşı). mp4 render YOK: `calistir.sh`'ı yalnız `ONIZLE_YALNIZ=1` ile koş. git commit yok. Claude alt ajanı açma.
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
3. Paket: `K/projeler/simple-present-temel-s1/BRIEF-S1.md` ("Yerleşim", "Kanal katmanı" tablosu, "Sahneler" satırı: `| — | 05-hyperframes-hikaye-a · 06-…-kapak-b · 07-…-kapak-c · 08-…-hikaye-b | HyperFrames | zaman çizelgesi dışı | 1 | — |`; "Hikâye kareleri" bölümü), `zaman.json`
   (`sahneler[]`, `hikaye`, `duragan[]`), `ortak/anlatim/senaryo.json` + `sozcukler.json` + `baslar.json` + `altyazi.json` (anlatım yok; kural özeti metni BRIEF-S1 girişinde),
   `uretim-tutanagi/S1-C-RAPOR.md`, `uretim-tutanagi/hikaye-taslak.md` §3–§4.
4. Kod tabanı (paket yeni): yapı ve v2 düzeni emsal `K/projeler/02-04-ydt-temel-s1/sahneler/04-hyperframes-hikaye/` (`uret.py`, `yardim.py`, `calistir.sh`); emsal v1'deki eski kapanış satırı ve çip ALINMAZ. Emsal sahnenin `RAPOR.md`'si "huni v2" diyorsa v2 hâlidir: onu taban al. Demiyorsa v1'dir: dosya yapısını al, v2 yerleşimini ve kanal katmanını bu istemle kur.

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
- Durağan kare: anlatımdan bağımsız, ses yok, altyazı yok, çip yok. Kanal katmanı + künye tablodaki gibi.
- Düzen A (kural kartı; B'den farklı), içerik y 460–1140: 470–650 kural özeti `He, she, it: s gelir;` / `I, you, we, they: s yok.` (Fredoka 700 64) · 690–800 `he · she · it → goes` (Fredoka 700 72; `es` kalın mürekkep alt çizgi) · 820–930 `I · you · we · they → go` (`go`'dan sonra soluk boş yuva) · 950–1030 Caveat 700 64 `My brother = he` (ikincil renk) + küçük otobüs (`ortak/cizim/coco/bus.svg`, kalem) · 1050–1140 yer imi simgesi (SVG yol, emoji değil) + `Kaydet` sarı hap.
- Tek sarı öğe `Kaydet` hapı (`es` vurgusu mürekkep alt çizgi). Satırlar ≤ 24 karakter.
- y 1150–1380 boş zemin (bağ çıkartması elle konur; kutu ya da çerçeve çizme). 1400–1920 boş.

## Doğrula (zorunlu, geçmeden bitirme)
1. `bash K/projeler/simple-present-temel-s1/sahneler/05-hyperframes-hikaye-a/calistir.sh --tema acik` ve `--tema koyu` → rc 0; `file` çıktısı 1080×1920 PNG (tek kare; zaman çizelgesi
   dışı, qa-yerel ölçmez). QA kareleri: açık tek kare (ilk = orta = son) + koyu tek kare; KÜRESEL anlatım saniyesi yoktur (durağan kare, zaman çizelgesi dışı).
2. Çakışma kapısı: `cd K && node araclar/cakisma-kapisi.mjs simple-present-temel-s1 --sahne 05-hyperframes-hikaye-a --port 41333 --sunucu 41022`. Araç yalnız
   `zaman.json → sahneler[]` okur; durağan kare için `HATA sahne bulunamadı` (çıkış 2) beklenir (emsal S1-VAR-RAPOR §5). Komutu yine koş,
   çıktıyı aynen RAPOR'a yaz; aracı değiştirme. Çakışmayı karede gözle denetle.
3. Metin taraması: `grep -rniE 'tam[ ]ders|dak[i]ka' K/projeler/simple-present-temel-s1/sahneler/05-hyperframes-hikaye-a/ --include=*.html --include=*.js --include=*.py` boş.
4. Kanal katmanı: QA karelerinin hepsinde görünür, konum ve boy tablodakiyle aynı (karede ölç; standart §7 madde 2).
Üretilen PNG'lere (`sahneler/05-hyperframes-hikaye-a/k/`, `k/koyu/`) Read ile BAK: taşma, kesik yazı, üst üste binme, okunmaz kontrast, boş kare,
0–280 ve 1570–1920 boş mu, sağ 960–1080 bölgesinde içerik var mı. En çok 4 düzeltme turu; geçmezse dur ve raporla.

## Rapor
`sahneler/05-hyperframes-hikaye-a/RAPOR.md`: olay listesi, kapı sonuçları (son satırlar), bakılan kareler ve bulgu, agy koşu özeti yolu, açık noktalar.
Son mesajın en çok 10 satır: kapı çıkış kodları, kare yolları, agy koşu özeti, açık noktalar.
