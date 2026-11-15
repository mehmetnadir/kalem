# İstem D-S1 — simple-present-temel-s1 sahne 02-paperjs-deger (huni v2) · 15.11.2026

<!-- P0202-S1-C (15.11) yazdı. Şablon: K/projeler/02-04-ydt-temel-s1/uretim-tutanagi/istem/sahne-v2/D-02-paperjs-ornek.md. Paket yeni: sahne kodu yok. -->

MAKİNE: Linux x86_64 (srv21), kullanıcı sef. K=`/home/sef/01dev/_worktrees/kalem-0204` (git worktree, dal `sunucu/02-04-ydt-temel`),
D=`/home/sef/01dev/dijital-anlatim`. Node `~/.nvm/versions/node/v24.22.2/bin`. Python `/usr/bin/python3 -I`. Skill `~/.claude/skills/motion-grafik-ders/`.
KURALLAR: Yalnız bu sahnenin dizinine yaz: `K/projeler/simple-present-temel-s1/sahneler/02-paperjs-deger/` (klasör yeni; sen açarsın). Başka sahneye, `ortak/`a,
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
3. Paket: `K/projeler/simple-present-temel-s1/BRIEF-S1.md` ("Yerleşim", "Kanal katmanı" tablosu, "Sahneler" satırı: `| 2 Değer | 02-paperjs-deger | Paper.js | 3,00–14,63 | 361 | öğretmen |`; "Sahne içeriği" 3,40–14,63 satırları), `zaman.json`
   (`sahneler[]`, `hikaye`, `duragan[]`), `ortak/anlatim/senaryo.json` + `sozcukler.json` + `baslar.json` + `altyazi.json` (cümle 1'in sonu ve cümle 2: `goes` 3,40 · `mu?` 3,80 · `My` 4,67 · `goes` 5,23 · `bus.` 6,19–6,83 · `He,` 7,08 · `she,` 7,64 · `it` 8,12 · `s` 9,25 · `I,` 10,62 · `you,` 11,42 · `we,` 12,14 · `they` 12,86 · `gelmez.` 13,59–14,63),
   `uretim-tutanagi/S1-C-RAPOR.md`, `uretim-tutanagi/senaryo-taslak.md` §2 sahne 2 (jüri D1 ve K2 satırları), `uretim-tutanagi/S1-duzeltme.md`.
4. Kod tabanı (paket yeni): yapı ve v2 düzeni emsal `K/projeler/02-04-ydt-temel-s1/sahneler/02-paperjs-ornek/` (`sahne-02.js`, `kalem-paper.js`, `sayfa.html`, `calistir.sh`, `SPEC.md`); bu dersin eski kısa değer sahnesi `~/Silinecekler/2026-11-15-huni-v2/simple-present-temel-s1-eski/sahneler/02-paperjs-ornek/` (aynı örnek cümle, `go-es` formülü) içerik kaynağıdır; otobüs `K/projeler/simple-present-temel/sahneler/04-canvas-ornek2/`, kırmızı `s` çizgisi `.../06-hyperframes-form/`. Emsal sahnenin `RAPOR.md`'si "huni v2" diyorsa v2 hâlidir: onu taban al. Demiyorsa v1'dir: dosya yapısını al, v2 yerleşimini ve kanal katmanını bu istemle kur.

## Kanal katmanı ve künye (bütün sahnelerde AYNI; değer değiştirme)
| Öğe | Değer |
|---|---|
| Logo | `ortak/logo/` (açık `yds-publishing-lacivert.svg`, koyu `yds-publishing-seffaf.svg`); yükseklik 48, genişlik 193,5; resim x 53,2 (görünür sol kenar x 60), y 291–339 |
| Yazı | `@ydspublishing`, Lexend 700 42 px, renk `murekkep`, x 263, taban y 330 |
| Davranış | 0. kareden son kareye; opaklık 1; giriş/çıkış animasyonu yok; uçuş/geçiş dokunmaz; kimlik `kanal`; `__kalemKutu` türü `kunye`, ad `kunye:kanal` |
| Künye | y 360–450: konu `Simple Present` (Fredoka 700, x 60, taban 420; boy ≤ 34, rozetle x 960'a sığan en büyük, alt sınır 28) + rozet `YDT · BASIC` (hap y 386–434, Lexend 700 26, dolgu `vurguDolgu`, yazı `pilMetin`, konu sonu + 20) |
| Bantlar | üst 0–280 boş (çip YOK) · içerik 460–1380, x 60–960 · altyazı 1400–1550 (en çok 2 satır) · alt 1570–1920 boş |

Değerleri BRIEF-S1 "Kanal katmanı" tablosundan birebir al; elle başka değer yazma.

Canvas: `ortak/kunye.js` bu pakette HAZIR ve v2'dir (`KANAL` + `kanalCiz`, `KUNYE` bantları, konu `Simple Present`, rozet `YDT · BASIC`; emsal `02-04-ydt-temel-s1/ortak/kunye.js` kopyası). Yalnız oku, içe aktar; dokunma. Eksik görürsen raporla.

## Yaz
Tek sütun; yazı tabanı ≥ 64 mantıksal px (künye, kanal ve altyazı hariç); satır ≤ 24 karakter; tek vurgu sarı (temaya göre), doğru
yeşil, kırmızı yalnız sahne 02'deki `s` yuvası çizgisi (ana ders `K/projeler/simple-present-temel/BRIEF.md` satır 159), emoji yok; sarı hap açık
temada dolgu `vurguDolgu` (`#ffe066`), yazı `pilMetin` (`#1b2440`); tema çifti zorunlu: açık + koyu (koyu tema QA karesi ayrı bakılır).
Yasak (standart §1): kural 4'teki eski kapanış sözü, süre sözü, QR, "izle" düğmesi taklidi, YouTube logosu taklidi.

Bu sahneye özel:
- Kare 0 = sahne 01 uçuş sonu: künye konu `Simple Present`, Caveat `Kardeşim gider:` (taban 560, x 60), kart `go` (x 60–440, y 620–820), küçük figür + otobüs (x 700–960, y 460–600). 3,40 kart `goes` (x 580–960, aynı satır); 3,80 iki kart arasında kalem `?` (x 450–570).
- 4,67–6,83 EN kart `My brother goes` / `to school by bus.` (Fredoka 700 ≥ 64, karaoke). `Kardeşim gider:` aynı yerde soluk Caveat'e döner (ikincil renk; seslendirilmez; sahne sonuna dek kalır; jüri K2: köprü çifti değer ekranında birlikte görünür, EN büyük, TR soluk). Söylenmeyen yeni TR satır EKLEME (`Kardeşim okula otobüsle gider.` yok). Figür ve küçük otobüs solar; otobüs EN kartın yanında kalemle 4,67–6,19.
- 5,23: kanca kartı `goes` cümledeki *goes*'a uçar, sarı alt çizgi alır; kart `go` soluk, sağ kenarda bekler (kaybolmaz).
- 7,08–8,28: `My brother` altında Caveat `= he` + kalem oku · çipler `he` 7,08 · `she` 7,64 · `it` 8,12. 9,25: `goes` → `go-es`, `es` sarı daire (sarı belirteç en çok 2: alt çizgi + daire).
- 10,62–13,02: ikinci satır çipler `I` · `you` · `we` · `they` (sözcük çapası). 13,59 (`gelmez.`): soluk `go` kartı ikinci satırın yanına döner; `s` yuvası üstünden kırmızı kalem çizgisi (ana ders BRIEF satır 159).
- Son durum (13,59–14,63) iki satır: `he · she · it → goes` / `I · you · we · they → go`; hiçbir öğe sahne bitmeden kaybolmaz. Bütün içerik x 60–960, y 460–1380; kartlar 900 px'e sığmazsa yazı boyu değil iç pay küçülür (yazı ≥ 64).
- Altyazı + karaoke 1400–1550; çip yok. Sahne `sahne-02.js` bekçisi `KUNYE.icerikSon` (1380) ile çalışır.

## Doğrula (zorunlu, geçmeden bitirme)
1. `cd K && bash araclar/qa-yerel.sh simple-present-temel-s1 02-paperjs-deger 3.05,8.80,14.55 8.80 --hazirla` → çıkış 0. t değerleri KÜRESEL anlatım
   saniyesidir (yerel değil; yerel kare = round((t − t_bas) × 30)): ilk kare 3,05, orta 8,80, son kare 14,55; koyu tema 8.80.
   qa-yerel ya da kapı dikey paketi ölçemiyorsa dur ve hatayı aynen raporla; aracı değiştirme.
2. Çakışma kapısı: `cd K && node araclar/cakisma-kapisi.mjs simple-present-temel-s1 --sahne 02-paperjs-deger --port 41333 --sunucu 41022` → çıkış 0, 0 uyarı.
3. Metin taraması: `grep -rniE 'tam[ ]ders|dak[i]ka' K/projeler/simple-present-temel-s1/sahneler/02-paperjs-deger/ --include=*.html --include=*.js --include=*.py` boş.
4. Kanal katmanı: QA karelerinin hepsinde görünür, konum ve boy tablodakiyle aynı (karede ölç; standart §7 madde 2).
Üretilen PNG'lere (`sahneler/02-paperjs-deger/k/`, `k/koyu/`) Read ile BAK: taşma, kesik yazı, üst üste binme, okunmaz kontrast, boş kare,
0–280 ve 1570–1920 boş mu, sağ 960–1080 bölgesinde içerik var mı. En çok 4 düzeltme turu; geçmezse dur ve raporla.

## Rapor
`sahneler/02-paperjs-deger/RAPOR.md`: olay listesi, kapı sonuçları (son satırlar), bakılan kareler ve bulgu, agy koşu özeti yolu, açık noktalar.
Son mesajın en çok 10 satır: kapı çıkış kodları, kare yolları, agy koşu özeti, açık noktalar.
