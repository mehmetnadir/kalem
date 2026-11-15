# İstem D — simple-present-temel-s3 sahne 07-hyperframes-kapak-c (huni v2) · 15.11.2026

<!-- P0202-S3-C (15.11) yazdı. Şablon: emsal `K/projeler/02-04-ydt-temel-s1/uretim-tutanagi/istem/sahne-v2/D-06-hyperframes-kapak-c.md`. -->

MAKİNE: Linux x86_64 (srv21), kullanıcı sef. K=`/home/sef/01dev/_worktrees/kalem-0204` (git worktree, dal `sunucu/02-04-ydt-temel`),
D=`/home/sef/01dev/dijital-anlatim`. Node `~/.nvm/versions/node/v24.22.2/bin`. Python `/usr/bin/python3 -I`. Skill `~/.claude/skills/motion-grafik-ders/`.
KURALLAR: Yalnız bu sahnenin dizinine yaz: `K/projeler/simple-present-temel-s3/sahneler/07-hyperframes-kapak-c/` (klasör yeni; sen açarsın). Çıktı: paket kökü `kapak-c.png` ve `k/koyu/kapak-c-koyu.png`. Başka sahneye, `ortak/`a,
`BRIEF-S3.md`'ye, `zaman.json`'a, ana derse (`simple-present-temel`) ve emsal pakete (`02-04-ydt-temel-s1`) dokunma (ikisi yalnız okunur);
eksik görürsen raporla. Silme yok (`~/Silinecekler/2026-11-15-0204/simple-present-temel-s3/` altına taşı). mp4 render YOK (tek kare PNG serbest: `calistir.sh --tema acik|koyu`). git commit yok. Claude alt ajanı açma.
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
üzerine yazman gerekirse önce `~/Silinecekler/2026-11-15-0204/simple-present-temel-s3/sahneler/07-hyperframes-kapak-c/` altına kopyala.

## Okuma
1. `D/.claude/docs/huni-v2-standart.md` (tamamı; BAĞLAYICI: §1 kurallar, §2 yerleşim, §3 yapı, §6 türevler, §7 kapı).
2. Skill `SKILL.md`, `references/kalem-hatti.md`, `stil-anayasasi.md`, `hareket-sozlugu.md`, `kliseler.md`.
3. Paket: `K/projeler/simple-present-temel-s3/BRIEF-S3.md` ("Yerleşim", "Kanal katmanı" tablosu, "Sahneler" satırı: `| — | 05-hyperframes-hikaye-a · 06-…-kapak-b · 07-…-kapak-c · 08-…-hikaye-b | HyperFrames | zaman çizelgesi dışı | 1 | — |`; "Kapak" bölümü), `zaman.json`
   (`sahneler[]`, `hikaye`, `duragan[]`), `ortak/anlatim/senaryo.json` + `sozcukler.json` + `baslar.json` + `altyazi.json` (anlatım yok; durağan kare),
   `uretim-tutanagi/S3-C-RAPOR.md`, `uretim-tutanagi/S3-duzeltme.md`, `uretim-tutanagi/kapak-taslak.md` §1, §2, §5.
4. Kod tabanı (emsal v2, yalnız okunur): `K/projeler/02-04-ydt-temel-s1/sahneler/06-hyperframes-kapak-c/` (`SPEC.md`, `uret.py`, `yardim.py`, `olay.py`, `calistir.sh`, `nesneler.json`). `calistir.sh`, `olay.py`, `yardim.py` kopyalanır (paket, klasör, çıktı adı ve konu metni Edit ile); `uret.py` içerik farklı → SPEC + agy. Sahne `zaman.json`'da `sahneler[]` dışındadır; `zaman.json`'a dokunma.

## Kanal katmanı ve künye (bütün sahnelerde AYNI; değer değiştirme)
| Öğe | Değer |
|---|---|
| Logo | `ortak/logo/` (açık `yds-publishing-lacivert.svg`, koyu `yds-publishing-seffaf.svg`); yükseklik 48, genişlik 193,5; resim x 53,2 (görünür sol kenar x 60), y 291–339 |
| Yazı | `@ydspublishing`, Lexend 700 42 px, renk `murekkep`, x 263, taban y 330 |
| Davranış | 0. kareden son kareye; opaklık 1; giriş/çıkış animasyonu yok; uçuş/geçiş dokunmaz; kimlik `kanal`; `__kalemKutu` türü `kunye`, ad `kunye:kanal` |
| Künye | y 360–450: konu `Simple Present` (Fredoka 700, x 60, taban 420; boy ≤ 34, rozetle x 960'a sığan en büyük, alt sınır 28) + rozet `YDT · BASIC` (hap y 386–434, Lexend 700 26, dolgu `vurguDolgu`, yazı `pilMetin`, konu sonu + 20) |
| Bantlar | üst 0–280 boş (çip YOK) · içerik 460–1380, x 60–960 · altyazı 1400–1550 (en çok 2 satır; bu karede altyazı YOK) · alt 1570–1920 boş |

Künye ortak dosyadan gelmez (paketin tek künye modülü yok): değerleri BRIEF-S3 "Kanal katmanı" tablosundan birebir al, elle başka değer yazma.
HyperFrames: kanal katmanını ve künye satırını emsal sahnenin v2 `yardim.py`'sinden kur (`kunye_svg()`: `<g id="kanal">` = logo `<image>` + `@ydspublishing` `<text>`; künye satırı y 360–450; v2 bant sabitleri). Kopyada yalnız konu metni (`Simple Present`), paket
adı ve yollar değişir. `hf_tema.py` logo `href` değişimi `#logoimg` kimliğini arar: kanal logosunun kimliği `logoimg` kalır.

## Yaz
Tek sütun; yazı tabanı ≥ 64 mantıksal px (künye, kanal ve altyazı hariç; ikincil satır ve etiket ≥ 50); satır ≤ 24 karakter; tek vurgu
sarı (temaya göre); kırmızı (`#d6453a`) YALNIZ yanlış kartında: üstü çizili `es` ve `✗`; emoji yok (`✗`, `✓`, `?` ve simgeler SVG kalem çizimidir); sarı hap açık temada dolgu `vurguDolgu`
(`#ffe066`), yazı `pilMetin` (`#1b2440`); tema çifti (açık + koyu). Yasak (standart §1): "Tam ders" sözü, süre sözü ("dakika"), QR,
"izle" düğmesi taklidi.

Bu sahneye özel:
- Durağan kare: anlatımdan bağımsız, ses yok, altyazı yok, çip yok. Kanal katmanı + künye tablodaki gibi.
- Başlık `DOES VARSA` / `FİİL YALIN` (`FİİL` noktalı İ; `DOES` İngilizce), y ≈ 470–800: Fredoka 700, `murekkep`, hap YOK; iki satır aynı boy,
  900 px'e sığan en büyük değer (üst sınır 190; motor ölçer), zemin renginde 10 px kontur.
- Kart 1 y ≈ 840–1060 (soluk): `He doesn't goes.` (Fredoka 72); `goes` içinde `es` eki birlikte kırmızı üstü çizili (`go` + çizili `es`;
  asla yalnız `s` değil); sağda kırmızı kalem `✗`.
- Kart 2 y ≈ 1100–1320: `He doesn't go.` (Fredoka 72, `murekkep`); sağda `✓` (`murekkep`); `go` altında sarı el altçizgisi (tek sarı öğe).
- Figür ve karakter görseli YOK. İçerik x 60–960 (en uzun satır `He doesn't goes.` ≈ 640 px); y 1400–1920 boş.

## Doğrula (zorunlu, geçmeden bitirme)
1. `bash K/projeler/simple-present-temel-s3/sahneler/07-hyperframes-kapak-c/calistir.sh --tema acik` ve `--tema koyu` → rc 0; `file` çıktısı 1080×1920 PNG (tek kare; zaman
   çizelgesi dışı, qa-yerel ölçmez). QA kareleri: açık tek kare (ilk = orta = son) + koyu tek kare.
2. Çakışma kapısı: `cd K && node araclar/cakisma-kapisi.mjs simple-present-temel-s3 --sahne 07-hyperframes-kapak-c --port 41333 --sunucu 41022`. Araç yalnız `zaman.json →
   sahneler[]` okur; durağan kare için `HATA sahne bulunamadı` (çıkış 2) beklenir (emsal S1-VAR-RAPOR §5). Komutu yine koş, çıktıyı aynen
   RAPOR'a yaz; aracı değiştirme. Çakışmayı karede gözle denetle.
3. Metin taraması: `grep -rniE 'tam ders|dakika' K/projeler/simple-present-temel-s3/sahneler/07-hyperframes-kapak-c/ --include=*.html --include=*.js --include=*.py` boş.
4. Kanal katmanı: QA karelerinin hepsinde görünür, konum ve boy tablodakiyle aynı (karede ölç; standart §7 madde 2).
Üretilen PNG'lere (`sahneler/07-hyperframes-kapak-c/k/`, `k/koyu/`) Read ile BAK: taşma, kesik yazı, üst üste binme, okunmaz kontrast, boş kare,
0–280 ve 1570–1920 boş mu, sağ 960–1080 bölgesinde içerik var mı, y 1150–1380 boş zemin mi (kutu yok). En çok 4 düzeltme turu; geçmezse dur ve raporla.

## Rapor
`sahneler/07-hyperframes-kapak-c/RAPOR.md`: olay listesi, kapı sonuçları (son satırlar), bakılan kareler ve bulgu, agy koşu özeti yolu, açık noktalar.
Son mesajın en çok 10 satır: kapı çıkış kodları, kare yolları, agy koşu özeti, açık noktalar.
