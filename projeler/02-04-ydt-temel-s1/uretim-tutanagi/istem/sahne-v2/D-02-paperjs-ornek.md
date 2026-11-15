# İstem D-V2 — 02-04-ydt-temel-s1 sahne 02-paperjs-ornek (huni v2) · 15.11.2026

<!-- V2-S1-C (15.11) yazdı. Taban: ../sahne/D-s1-sablon.md. Eski istem: ../sahne/D-02-paperjs-ornek.md. -->

MAKİNE: Linux x86_64 (srv21), kullanıcı sef. K=`/home/sef/01dev/_worktrees/kalem-0204` (git worktree, dal `sunucu/02-04-ydt-temel`),
D=`/home/sef/01dev/dijital-anlatim`. Node `~/.nvm/versions/node/v24.22.2/bin`. Python `/usr/bin/python3 -I`. Skill `~/.claude/skills/motion-grafik-ders/`.
KURALLAR: Yalnız bu sahnenin dizinine yaz: `K/projeler/02-04-ydt-temel-s1/sahneler/02-paperjs-ornek/`. İzinli istisna: `ortak/kunye.js` (paket içinde onu içe aktaran tek sahne budur; s2/s3 kendi kopyalarını kullanır). Önce `~/Silinecekler/2026-11-15-huni-v2/02-04-ydt-temel-s1/ortak/kunye.js` olarak kopyala. Başka sahneye, `ortak/`a (yukarıdaki istisna dışında),
`BRIEF-S1.md`'ye, `zaman.json`'a, ana derse (`02-04-ydt-temel`, yalnız okunur) dokunma; eksik görürsen raporla. Silme yok
(`~/Silinecekler/2026-11-15-huni-v2/02-04-ydt-temel-s1/` altına taşı). mp4 render YOK: `calistir.sh`'ı yalnız `ONIZLE_YALNIZ=1` ile koş. git commit yok. Claude alt ajanı açma.
Kanca atlama bayrağı OLUŞTURMA (`/tmp/conductor-*`, `~/.conductor/*`). Durdurma kancası sözleşme satırı isterse `K/.claude/docs/sozlesme.md`
dosyasına 1–2 satır EKLE (tek istisna).

## Kod yolu (kapı ve doktrin)
Kod yazma kapısı 15 satırdan uzun kod dosyasını sana kapatır; bayrak açmaya çalışma. Yol: tasarımı sahne dizininde `SPEC.md` olarak
yaz (yazılacak dosyanın mutlak yolu, var olan kodun mutlak yolu ve oradan alınacak kalıp, olay listesi olay · kare/küresel sn · cümle
sözcüğü, yerleşim, ekran metni, kurallar, kabul ölçütü; tam kod YAZMA). Sonra
`agy-filo tek --rol kod --cwd /home/sef/01dev/_worktrees/kalem-0204 --zaman 25m -p "<SPEC.md mutlak yolunu oku ve uygula. Yalnız <dosya
mutlak yolu> dosyasını yaz. Başka dosyaya dokunma. Silme yok. Test, render, git yok.>"`. Kodu agy yazar; sen baştan sona okur, spec'e
uyuyor mu bakarsın, küçük düzeltmeyi Edit ile yaparsın, büyük düzeltmeyi agy'ye geri verirsin (en çok 2 tur). Tam kodu kendin yazıp
agy'ye birebir kopyalatmak YASAK. Kısa dosyalar (`calistir.sh`, `sayfa.html`) Edit ile yazılabilir. Değiştirmeden önce eski dosyayı
`~/Silinecekler/2026-11-15-huni-v2/02-04-ydt-temel-s1/sahneler/02-paperjs-ornek/` altına kopyala.

## Okuma
1. `D/.claude/docs/huni-v2-standart.md` (tamamı; BAĞLAYICI: §1 kurallar, §2 yerleşim, §3 yapı, §6 türevler, §7 kapı).
2. Skill `SKILL.md`, `references/kalem-hatti.md`, `stil-anayasasi.md`, `hareket-sozlugu.md`, `kliseler.md`.
3. Paket: `K/projeler/02-04-ydt-temel-s1/BRIEF-S1.md` ("Yerleşim", "Kanal katmanı" tablosu, "Sahneler" satırı: `| 2 Değer | 02-paperjs-ornek | Paper.js | 3,00–19,99 | 522 | öğretmen |`; "Sahne içeriği" 3,08–19,99 satırı (akış v1 ile aynı: eski BRIEF satırları `~/Silinecekler/2026-11-15-huni-v2/02-04-ydt-temel-s1/BRIEF-S1.md`)), `zaman.json`
   (`sahneler[]`, `hikaye`, `duragan[]`), `ortak/anlatim/senaryo.json` + `sozcukler.json` + `baslar.json` + `altyazi.json` (cümle 1'in sonu ve cümle 2: `yaşıyorum.` 3,08 · `Türkçede` 3,96 · `İngilizcede` 6,91 · `I` 9,08 · `Hep` 11,17 · `I` 14,70 · `Şimdilik:` 17,03 · `şimdiki` 19,03),
   `uretim-tutanagi/V2-C-RAPOR.md`.
4. Var olan sahne (v1; kod tabanı): `K/projeler/02-04-ydt-temel-s1/sahneler/02-paperjs-ornek/` (`sahne-02.js`, `kalem-paper.js`, `sayfa.html`, `SPEC.md`, `RAPOR.md`). İçerik aynı kalır; değişen yerleşim + kanal katmanı.

## Kanal katmanı ve künye (bütün sahnelerde AYNI; değer değiştirme)
| Öğe | Değer |
|---|---|
| Logo | `ortak/logo/` (açık `yds-publishing-lacivert.svg`, koyu `yds-publishing-seffaf.svg`); yükseklik 48, genişlik 193,5; resim x 53,2 (görünür sol kenar x 60), y 291–339 |
| Yazı | `@ydspublishing`, Lexend 700 42 px, renk `murekkep`, x 263, taban y 330 |
| Davranış | 0. kareden son kareye; opaklık 1; giriş/çıkış animasyonu yok; uçuş/geçiş dokunmaz; kimlik `kanal`; `__kalemKutu` türü `kunye`, ad `kunye:kanal` |
| Künye | y 360–450: konu `Simple Present vs Present Continuous` (Fredoka 700, x 60, taban 420; boy ≤ 34, rozetle x 960'a sığan en büyük, alt sınır 28) + rozet `YDT · BASIC` (hap y 386–434, Lexend 700 26, dolgu `vurguDolgu`, yazı `pilMetin`, konu sonu + 20) |
| Bantlar | üst 0–280 boş (çip YOK) · içerik 460–1380, x 60–960 · altyazı 1400–1550 (en çok 2 satır) · alt 1570–1920 boş |

Künye ortak dosyadan gelmez (paketin tek künye modülü yok): değerleri BRIEF-S1 "Kanal katmanı" tablosundan birebir al, elle başka değer yazma.
Canvas: `ortak/kunye.js`'i v2'ye çevir (15+ satır kod → SPEC + agy): `KANAL` sabiti + `kanalCiz(ctx, K)` (logo + yazı, tablo değerleri, `__kalemKutu` `kunye:kanal`), `KUNYE` bantları (içerik 460–1380, kenar 60, sağ sınır 960, altyazı 1400–1550), künye satırı (konu + rozet tek satır, y 360–450), çip çizimi kapalı. `kunyeCiz` her karede `kanalCiz`'i de çağırır. `sahne-02.js` bekçisi (`KUNYE.icerikSon`) yeni değerle çalışır. Dosya başına tek satır not: "huni v2 (15.11): kanal katmanı + v2 bantları".

## Yaz
Tek sütun; yazı tabanı ≥ 64 mantıksal px (künye, kanal ve altyazı hariç); satır ≤ 24 karakter; tek vurgu sarı (temaya göre), doğru
yeşil, kırmızı yok, emoji yok; sarı hap açık temada dolgu `vurguDolgu` (`#ffe066`), yazı `pilMetin` (`#1b2440`); tema çifti (açık + koyu);
ekranda "İstanbul" noktalı. Yasak (standart §1): "Tam ders" sözü, süre sözü ("dakika"), QR, "izle" düğmesi taklidi.

Bu sahneye özel:
- İçerik ve olay sırası v1 ile aynı (`ek_ayir`, iki *yor* kutusu, kart 1 `I live in İstanbul.` + `Hep orada.` + `PERMANENT` + uzun bant,
  kart 2 `I am living` / `with my uncle.` + `Şimdilik.` + `TEMPORARY` + kısa bant; ev ve bavul ikonları).
- Yerleşim v2: bütün içerik x 60–960, y 460–1380 (eski 48–1032, 352–1392). Kartlar 900 px'e sığar; sığmazsa yazı boyu değil, kart iç payı küçülür
  (yazı ≥ 64).
- Kare 0'daki iki TR satırı v2 sabitinde: `Y_L1` 560, `Y_L2` 680 (v1 470/590 + 90); sahne 01 uçuş sonu aynı değeri kullanır
  (`D-01-hyperframes-kapak.md`). Öteki y değerleri (`YC1`, `YC2` …) aynı mantıkla içerik bandına (460–1380) taşınır.
- Altyazı + karaoke 1400–1550; çip yok.

## Doğrula (zorunlu, geçmeden bitirme)
1. `cd K && bash araclar/qa-yerel.sh 02-04-ydt-temel-s1 02-paperjs-ornek 3.05,11.50,19.90 11.50 --hazirla` → çıkış 0. t değerleri KÜRESEL anlatım saniyesidir (yerel değil): ilk kare 3,05, orta 11,50, son kare 19,90; koyu tema 11.50. qa-yerel ya da kapı dikey paketi ölçemiyorsa dur ve hatayı aynen raporla; aracı değiştirme.
2. Çakışma kapısı: `cd K && node araclar/cakisma-kapisi.mjs 02-04-ydt-temel-s1 --sahne 02-paperjs-ornek --port 41333 --sunucu 41022` → çıkış 0, 0 uyarı.
3. Metin taraması: `grep -rniE 'tam ders|dakika' K/projeler/02-04-ydt-temel-s1/sahneler/02-paperjs-ornek/ --include=*.html --include=*.js --include=*.py` boş.
4. Kanal katmanı: QA karelerinin hepsinde görünür, konum ve boy tablodakiyle aynı (karede ölç; standart §7 madde 2).
Üretilen PNG'lere (`sahneler/02-paperjs-ornek/k/`, `k/koyu/`) Read ile BAK: taşma, kesik yazı, üst üste binme, okunmaz kontrast, boş kare,
0–280 ve 1570–1920 boş mu, sağ 960–1080 bölgesinde içerik var mı. En çok 4 düzeltme turu; geçmezse dur ve raporla.

## Rapor
`sahneler/02-paperjs-ornek/RAPOR.md` (eski RAPOR.md varsa önce Silinecekler'e kopyala): olay listesi, kapı sonuçları (son satırlar), bakılan kareler
ve bulgu, agy koşu özeti yolu, açık noktalar. Son mesajın en çok 10 satır: kapı çıkış kodları, kare yolları, agy koşu özeti, açık noktalar.
