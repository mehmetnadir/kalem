# İstem D-V2 — simple-present-temel-s2 sahne 06-hyperframes-kapak-b (huni v2, durağan kare) · 15.11.2026

<!-- S2-C (15.11) yazdı. Şablon: K/projeler/02-04-ydt-temel-s1/uretim-tutanagi/istem/sahne-v2/D-05-hyperframes-kapak-b.md. -->

MAKİNE: Linux x86_64 (srv21), kullanıcı sef. K=`/home/sef/01dev/_worktrees/kalem-0204` (git worktree, dal `sunucu/02-04-ydt-temel`),
D=`/home/sef/01dev/dijital-anlatim`. Node `~/.nvm/versions/node/v24.22.2/bin`. Python `/usr/bin/python3 -I`. Skill `~/.claude/skills/motion-grafik-ders/`.
KURALLAR: Yalnız bu sahnenin dizinine yaz: `K/projeler/simple-present-temel-s2/sahneler/06-hyperframes-kapak-b/` (klasör yeni; sen açarsın).
Çıktı: paket kökü `kapak-b.png` ve `k/koyu/kapak-b-koyu.png`. Başka sahneye, `ortak/`a, `BRIEF-S2.md`'ye, `zaman.json`'a, ana derse
(`simple-present-temel`) ve emsale (`02-04-ydt-temel-s1`) dokunma (ikisi yalnız okunur); eksik görürsen raporla. Silme yok
(`~/Silinecekler/2026-11-15-0204/simple-present-temel-s2/` altına taşı). mp4 render YOK (tek kare PNG serbest: `calistir.sh --tema acik|koyu`).
git commit yok. Claude alt ajanı açma.
Kanca atlama bayrağı OLUŞTURMA (`/tmp/conductor-*`, `~/.conductor/*`). Durdurma kancası sözleşme satırı isterse `K/.claude/docs/sozlesme.md`
dosyasına 1–2 satır EKLE (tek istisna).

## Kod yolu (kapı ve doktrin)
Kod yazma kapısı 15 satırdan uzun kod dosyasını sana kapatır; bayrak açmaya çalışma. Emsalden kopyalanan dosyalar (`calistir.sh`, `olay.py`,
`yardim.py`) `cp -p` + küçük Edit ile kurulur (paket adı, klasör adı, çıktı adı, künye konu adı). Yeni içerik taşıyan kod (`uret.py`): tasarımı
sahne dizininde `SPEC.md` olarak yaz (yazılacak dosyanın mutlak yolu, var olan kodun mutlak yolu ve oradan alınacak kalıp, öğe listesi,
yerleşim, ekran metni, kurallar, kabul ölçütü; tam kod YAZMA). Sonra
`agy-filo tek --rol kod --cwd /home/sef/01dev/_worktrees/kalem-0204 --zaman 25m -p "<SPEC.md mutlak yolunu oku ve uygula. Yalnız <dosya
mutlak yolu> dosyasını yaz. Başka dosyaya dokunma. Silme yok. Test, render, git yok.>"`. Kodu agy yazar; sen baştan sona okur, spec'e
uyuyor mu bakarsın, küçük düzeltmeyi Edit ile yaparsın, büyük düzeltmeyi agy'ye geri verirsin (en çok 2 tur). Tam kodu kendin yazıp
agy'ye birebir kopyalatmak YASAK.

## Okuma
1. `D/.claude/docs/huni-v2-standart.md` (tamamı; BAĞLAYICI: §2 yerleşim, §6 kapak, §7 kapı).
2. Skill `SKILL.md`, `references/kalem-hatti.md`, `stil-anayasasi.md`, `kliseler.md`.
3. Paket: `K/projeler/simple-present-temel-s2/BRIEF-S2.md` ("Yerleşim", "Kanal katmanı" tablosu, "Kapak" bölümü B), `zaman.json` → `duragan[]`
   (klasör `06-hyperframes-kapak-b`, çıktı `kapak-b.png`), `uretim-tutanagi/kapak-taslak.md` §1, §2, §4, `uretim-tutanagi/S2-C-RAPOR.md`.
4. Kod tabanı (yalnız okunur): emsal v2 `K/projeler/02-04-ydt-temel-s1/sahneler/05-hyperframes-kapak-b/` (soru kapağı: başlık, balonlar,
   kanal katmanı, `calistir.sh --tema`). Öğrenci başı çizimi: ana ders `K/projeler/simple-present-temel/sahneler/06-hyperframes-form/uret.py`
   (`peeps-kit/ogrenci-bas.svg` kullanımı).
5. Sözleşme `K/.claude/docs/sozlesme.md` huni v2 satırları (kanal katmanı, `#logoimg`, durağan kapak kalıbı).

## Kanal katmanı ve künye (bütün sahnelerde AYNI; değer değiştirme)
| Öğe | Değer |
|---|---|
| Logo | `ortak/logo/` (açık `yds-publishing-lacivert.svg`, koyu `yds-publishing-seffaf.svg`); yükseklik 48, genişlik 193,5; resim x 53,2 (görünür sol kenar x 60), y 291–339 |
| Yazı | `@ydspublishing`, Lexend 700 42 px, renk `murekkep`, x 263, taban y 330 |
| Davranış | kimlik `kanal`; `__kalemKutu` türü `kunye`, ad `kunye:kanal`; durağan karede tam görünür |
| Künye | y 360–450: konu `Simple Present` (Fredoka 700, x 60, taban 420; boy ≤ 34, rozetle x 960'a sığan en büyük, alt sınır 28) + rozet `YDT · BASIC` (hap y 386–434, Lexend 700 26, dolgu `vurguDolgu`, yazı `pilMetin`, konu sonu + 20) |
| Bantlar | üst 0–280 boş (çip YOK) · içerik 460–1380, x 60–960 · 1400–1920 boş (kapakta altyazı yok) |

Künye ortak dosyadan gelmez: değerleri BRIEF-S2 "Kanal katmanı" tablosundan birebir al. HyperFrames: emsalin v2 `yardim.py` `kunye_svg()`
kopyasıyla kur; konu adı `Simple Present`; kanal logosunun kimliği `logoimg` (`hf_tema.py` tema geçişi).

## Yaz
Tek sütun; yazı tabanı ≥ 64 mantıksal px (künye ve kanal hariç); satır ≤ 24 karakter; tek vurgu sarı (temaya göre), kırmızı yok, emoji yok;
tema çifti (açık + koyu; koyu kare de QA'ya girer). Kapak kuralı: başlık 2 satır, ≤ 4 sözcük, kalın kontur; üçüncü satır, rakam, kalabalık yok.
Yasak (standart §1): "Tam ders" sözü, süre sözü ("dakika"), QR, "izle" düğmesi taklidi.

Bu sahneye özel:
- Durağan kare: anlatımdan bağımsız, ses yok, altyazı yok, çip yok. Kanal katmanı + künye tablodaki gibi.
- Başlık y 460–800: `ALWAYS VARSA` / `HANGİ ZAMAN?` (mürekkep, hapsız; iki satır aynı boy, 900 px'e sığan en büyük, üst sınır 190; `HANGİ` İ noktalı).
- Görsel y 820–1380, x 60–960: solda öğrenci başı (`ortak/cizim/peeps-kit/ogrenci-bas.svg`, kalem çizgisi; `kadro.ogrenci`) + el çizimi
  konuşma balonu `always?` (Fredoka 72) · sağda büyük sarı `?` (karenin tek sarısı).
- Karakter görseli (`karakter.png`) bu kapakta YOK (S2-C: kapak C'de). Cevap karede yok (videoda verilir).

## Doğrula (zorunlu, geçmeden bitirme)
1. `bash K/projeler/simple-present-temel-s2/sahneler/06-hyperframes-kapak-b/calistir.sh --tema acik` ve `--tema koyu` → rc 0; `file` çıktısı
   1080×1920 PNG (tek kare; zaman çizelgesi dışı, qa-yerel ölçmez). QA kareleri: açık tek kare (ilk = orta = son) + koyu tek kare.
2. Çakışma kapısı: `cd K && node araclar/cakisma-kapisi.mjs simple-present-temel-s2 --sahne 06-hyperframes-kapak-b --port 41333 --sunucu 41022`.
   Araç yalnız `zaman.json → sahneler[]` okur; durağan kare için `HATA sahne bulunamadı` (çıkış 2) beklenir. Komutu yine koş, çıktıyı aynen
   RAPOR'a yaz; aracı değiştirme. Çakışmayı karede gözle denetle.
3. Metin taraması: `grep -rniE 'tam ders|dakika' K/projeler/simple-present-temel-s2/sahneler/06-hyperframes-kapak-b/ --include=*.html --include=*.js --include=*.py` boş.
4. Kanal katmanı: QA karelerinin hepsinde görünür, konum ve boy tablodakiyle aynı (karede ölç; standart §7 madde 2).
Üretilen PNG'lere (`sahneler/06-hyperframes-kapak-b/k/`, `k/koyu/`, paket kökü `kapak-b.png`) Read ile BAK: taşma, kesik yazı, üst üste binme,
okunmaz kontrast, boş kare, 0–280 ve 1400–1920 boş mu, sağ 960–1080 bölgesinde içerik var mı. En çok 4 düzeltme turu; geçmezse dur ve raporla.

## Rapor
`sahneler/06-hyperframes-kapak-b/RAPOR.md`: öğe listesi, kapı sonuçları (son satırlar), bakılan kareler ve bulgu, agy koşu özeti yolu, açık
noktalar. Son mesajın en çok 10 satır: kapı çıkış kodları, kare yolları, agy koşu özeti, açık noktalar.
