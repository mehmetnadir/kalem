# İstem D-V2 — simple-present-temel-s2 sahne 07-hyperframes-kapak-c (huni v2, durağan kare) · 15.11.2026

<!-- S2-C (15.11) yazdı. Şablon: K/projeler/02-04-ydt-temel-s1/uretim-tutanagi/istem/sahne-v2/D-06-hyperframes-kapak-c.md. -->

MAKİNE: Linux x86_64 (srv21), kullanıcı sef. K=`/home/sef/01dev/_worktrees/kalem-0204` (git worktree, dal `sunucu/02-04-ydt-temel`),
D=`/home/sef/01dev/dijital-anlatim`. Node `~/.nvm/versions/node/v24.22.2/bin`. Python `/usr/bin/python3 -I`. Skill `~/.claude/skills/motion-grafik-ders/`.
KURALLAR: Yalnız bu sahnenin dizinine yaz: `K/projeler/simple-present-temel-s2/sahneler/07-hyperframes-kapak-c/` (klasör yeni; sen açarsın).
Çıktı: paket kökü `kapak-c.png` ve `k/koyu/kapak-c-koyu.png`. Karakter görseli hazırdır: `ortak/kapak/karakter.png` (S2-C kopyaladı; kaynak
`K/projeler/simple-present-temel/ortak/kapak/karakter.png`, 896×1200 RGBA; sahne kendi `assets/` dizinine kopyalayabilir). Başka sahneye,
`ortak/`a, `BRIEF-S2.md`'ye, `zaman.json`'a, ana derse (`simple-present-temel`) ve emsale (`02-04-ydt-temel-s1`) dokunma (ikisi yalnız okunur);
eksik görürsen raporla. Silme yok (`~/Silinecekler/2026-11-15-0204/simple-present-temel-s2/` altına taşı). mp4 render YOK (tek kare PNG serbest:
`calistir.sh --tema acik|koyu`). git commit yok. Claude alt ajanı açma.
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
1. `D/.claude/docs/huni-v2-standart.md` (tamamı; BAĞLAYICI: §2 yerleşim, §6 kapak "en az biri karakter", §7 kapı) ve
   `D/.claude/docs/kapak-standardi.md` (krem çıkartma kenarı).
2. Skill `SKILL.md`, `references/kalem-hatti.md`, `stil-anayasasi.md`, `kliseler.md`.
3. Paket: `K/projeler/simple-present-temel-s2/BRIEF-S2.md` ("Yerleşim", "Kanal katmanı" tablosu, "Kapak" bölümü C), `zaman.json` → `duragan[]`
   (klasör `07-hyperframes-kapak-c`, çıktı `kapak-c.png`), `uretim-tutanagi/kapak-taslak.md` (en üstteki S2-C notu, §1, §2, §5),
   `uretim-tutanagi/S2-duzeltme.md` madde 4 (başlık), `uretim-tutanagi/S2-C-RAPOR.md`.
4. Kod tabanı (yalnız okunur): emsal v2 `K/projeler/02-04-ydt-temel-s1/sahneler/06-hyperframes-kapak-c/` (durağan kapak düzeni, kanal katmanı)
   ve `K/projeler/02-04-ydt-temel-s1/sahneler/05-hyperframes-kapak-b/` (`karakter.png` + krem çıkartma kenarı: CSS `drop-shadow`, dört yön).
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
sarı hap açık temada dolgu `vurguDolgu` (`#ffe066`), yazı `pilMetin` (`#1b2440`); tema çifti (açık + koyu; koyu kare de QA'ya girer).
Kapak kuralı: başlık 2 satır, ≤ 4 sözcük, kalın kontur; üçüncü satır, rakam, kalabalık yok.
Yasak (standart §1): "Tam ders" sözü, süre sözü ("dakika"), QR, "izle" düğmesi taklidi.

Bu sahneye özel:
- Durağan kare: anlatımdan bağımsız, ses yok, altyazı yok, çip yok. Kanal katmanı + künye tablodaki gibi.
- Başlık y 460–800: `ÜÇ İFADE,` / `TEK İŞARET` (mürekkep, hapsız; iki satır aynı boy, 900 px'e sığan en büyük, üst sınır 190; Ü, İ, Ş doğru).
  Başlık S2-C düzeltmesidir (jüri dil 3 + kaynak 1a); `TEK ZAMAN` ya da `ÜÇ SÖZCÜK` YAZMA.
- Görsel y 820–1380: solda el çizimi kart (x 60–600): `usually` · `always` · `every day` alt alta (Fredoka 72, mürekkep) → kalem oku →
  `Simple Present` sarı hap (Fredoka 80; karenin tek sarısı; hap kartın altında taşabilir ama x 960'ı geçmez).
- Sağda karakter görseli (x 620–960): `karakter.png` (genç erkek, gözlüklü, sola işaret eden "buldum" duruşu) karta işaret eder; çevresinde
  10 px krem `#f3efe6` çıkartma kenarı (dört yön `drop-shadow`; kapak-standardi.md). Koyu temada da aynı görsel.
- Sığmazsa önce köşedeki küçük takvim çıkar (taslak §5), sonra karakter ölçeği küçülür; yazı boyu 64'ün altına inmez.

## Doğrula (zorunlu, geçmeden bitirme)
1. `bash K/projeler/simple-present-temel-s2/sahneler/07-hyperframes-kapak-c/calistir.sh --tema acik` ve `--tema koyu` → rc 0; `file` çıktısı
   1080×1920 PNG (tek kare; zaman çizelgesi dışı, qa-yerel ölçmez). QA kareleri: açık tek kare (ilk = orta = son) + koyu tek kare.
2. Çakışma kapısı: `cd K && node araclar/cakisma-kapisi.mjs simple-present-temel-s2 --sahne 07-hyperframes-kapak-c --port 41333 --sunucu 41022`.
   Araç yalnız `zaman.json → sahneler[]` okur; durağan kare için `HATA sahne bulunamadı` (çıkış 2) beklenir. Komutu yine koş, çıktıyı aynen
   RAPOR'a yaz; aracı değiştirme. Çakışmayı karede gözle denetle.
3. Metin taraması: `grep -rniE 'tam ders|dakika' K/projeler/simple-present-temel-s2/sahneler/07-hyperframes-kapak-c/ --include=*.html --include=*.js --include=*.py` boş.
4. Kanal katmanı: QA karelerinin hepsinde görünür, konum ve boy tablodakiyle aynı (karede ölç; standart §7 madde 2).
Üretilen PNG'lere (`sahneler/07-hyperframes-kapak-c/k/`, `k/koyu/`, paket kökü `kapak-c.png`) Read ile BAK: taşma, kesik yazı, üst üste binme,
okunmaz kontrast, boş kare, 0–280 ve 1400–1920 boş mu, sağ 960–1080 bölgesinde içerik var mı. En çok 4 düzeltme turu; geçmezse dur ve raporla.

## Rapor
`sahneler/07-hyperframes-kapak-c/RAPOR.md`: öğe listesi, kapı sonuçları (son satırlar), bakılan kareler ve bulgu, agy koşu özeti yolu, açık
noktalar. Son mesajın en çok 10 satır: kapı çıkış kodları, kare yolları, agy koşu özeti, açık noktalar.
