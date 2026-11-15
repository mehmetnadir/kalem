# İstem D-V2 — 02-04-ydt-temel-s1 sahne 03-hyperframes-cta (huni v2) · 15.11.2026

<!-- V2-S1-C (15.11) yazdı. Taban: ../sahne/D-s1-sablon.md. Eski istem: ../sahne/D-03-hyperframes-cta.md. -->

MAKİNE: Linux x86_64 (srv21), kullanıcı sef. K=`/home/sef/01dev/_worktrees/kalem-0204` (git worktree, dal `sunucu/02-04-ydt-temel`),
D=`/home/sef/01dev/dijital-anlatim`. Node `~/.nvm/versions/node/v24.22.2/bin`. Python `/usr/bin/python3 -I`. Skill `~/.claude/skills/motion-grafik-ders/`.
KURALLAR: Yalnız bu sahnenin dizinine yaz: `K/projeler/02-04-ydt-temel-s1/sahneler/03-hyperframes-cta/`. İzinli istisna: `ortak/kapak/ana-kapak.png`, `ortak/kapak/ana-kapak-koyu.png` (ana ders kapağının kopyası, aşağıda). Başka sahneye, `ortak/`a (yukarıdaki istisna dışında),
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
`~/Silinecekler/2026-11-15-huni-v2/02-04-ydt-temel-s1/sahneler/03-hyperframes-cta/` altına kopyala.

## Okuma
1. `D/.claude/docs/huni-v2-standart.md` (tamamı; BAĞLAYICI: §1 kurallar, §2 yerleşim, §3 yapı, §6 türevler, §7 kapı).
2. Skill `SKILL.md`, `references/kalem-hatti.md`, `stil-anayasasi.md`, `hareket-sozlugu.md`, `kliseler.md`.
3. Paket: `K/projeler/02-04-ydt-temel-s1/BRIEF-S1.md` ("Yerleşim", "Kanal katmanı" tablosu, "Sahneler" satırı: `| 4 Çağrı | 03-hyperframes-cta | HyperFrames | 25,49–31,75 | 218 | öğrenci |`; "Sahne içeriği" 25,49–31,75 satırları), `zaman.json`
   (`sahneler[]`, `hikaye`, `duragan[]`), `ortak/anlatim/senaryo.json` + `sozcukler.json` + `baslar.json` + `altyazi.json` (cümle 4 (öğrenci sesi): `Gerisi` 26,04 · `bizde.` 26,52 · `Dersin` 27,23 · `YDS` 28,51 · `Publishing` 29,19 · `YouTube` 29,63 · `kanalında.` 30,03–30,83),
   `uretim-tutanagi/V2-C-RAPOR.md`, `D/.claude/docs/kapak-standardi.md` (ana kapak dosyası).
4. Var olan sahne (v1; kod tabanı): `K/projeler/02-04-ydt-temel-s1/sahneler/03-hyperframes-cta/` (v1: `üç farktan biri`, `Tam ders:`, ders bandı, saat, süre — HEPSİ kalkar). Kod tabanı v1 `uret.py` / `yardim.py`; içerik baştan (SPEC + agy).

## Kanal katmanı ve künye (bütün sahnelerde AYNI; değer değiştirme)
| Öğe | Değer |
|---|---|
| Logo | `ortak/logo/` (açık `yds-publishing-lacivert.svg`, koyu `yds-publishing-seffaf.svg`); yükseklik 48, genişlik 193,5; resim x 53,2 (görünür sol kenar x 60), y 291–339 |
| Yazı | `@ydspublishing`, Lexend 700 42 px, renk `murekkep`, x 263, taban y 330 |
| Davranış | 0. kareden son kareye; opaklık 1; giriş/çıkış animasyonu yok; uçuş/geçiş dokunmaz; kimlik `kanal`; `__kalemKutu` türü `kunye`, ad `kunye:kanal` |
| Künye | y 360–450: konu `Simple Present vs Present Continuous` (Fredoka 700, x 60, taban 420; boy ≤ 34, rozetle x 960'a sığan en büyük, alt sınır 28) + rozet `YDT · BASIC` (hap y 386–434, Lexend 700 26, dolgu `vurguDolgu`, yazı `pilMetin`, konu sonu + 20) |
| Bantlar | üst 0–280 boş (çip YOK) · içerik 460–1380, x 60–960 · altyazı 1400–1550 (en çok 2 satır) · alt 1570–1920 boş |

Künye ortak dosyadan gelmez (paketin tek künye modülü yok): değerleri BRIEF-S1 "Kanal katmanı" tablosundan birebir al, elle başka değer yazma.
HyperFrames: sahnenin `yardim.py` `kunye_svg()` işlevini v2'ye çevir: `<g id="kanal">` (logo `<image>` + `@ydspublishing` `<text>`) eklenir; eski ders adı 2 satır + rozet + çip yerine künye satırı (y 360–450). `KUNYE`/`HUD` sabitlerindeki eski bantlar (hudSon 320, icerikBas 352, icerikSon 1392, altyaziSon 1536, kenar 48) v2 değerlerine geçer. `hf_tema.py` logo `href` değişimi `#logoimg` kimliğini arar: kanal logosunun kimliği `logoimg` olsun (tema geçişi bozulmaz).

## Yaz
Tek sütun; yazı tabanı ≥ 64 mantıksal px (künye, kanal ve altyazı hariç); satır ≤ 24 karakter; tek vurgu sarı (temaya göre), doğru
yeşil, kırmızı yok, emoji yok; sarı hap açık temada dolgu `vurguDolgu` (`#ffe066`), yazı `pilMetin` (`#1b2440`); tema çifti (açık + koyu);
ekranda "İstanbul" noktalı. Yasak (standart §1): "Tam ders" sözü, süre sözü ("dakika"), QR, "izle" düğmesi taklidi.

Bu sahneye özel:
- ÖNCE kapak: `K/projeler/02-04-ydt-temel/kapak.png` ve `kapak-koyu.png` var mı bak. İkisi de varsa `cp -p` ile
  `K/projeler/02-04-ydt-temel-s1/ortak/kapak/ana-kapak.png` ve `ana-kapak-koyu.png`. Biri yoksa DUR: başka dosya yazma, `sahneler/03-hyperframes-cta/RAPOR.md`'ye ve
  son mesaja "ana kapak bekliyor" yaz (15.11 18:30 ölçümü: ikisi de YOK).
- Kart: ana kapak 16:9, 900×506, x 60–960, y 620–1126 (standart ≈ 920×518; x 960 sınırı için 900); köşe yarıçapı 24, `murekkep` kenar 4 px;
  tema uyumlu (açık → `ana-kapak.png`, koyu → `ana-kapak-koyu.png`; `hf_tema.py` logo geçişi gibi `href` değişimi). Giriş 25,49–26,04 tek hareket
  (ölçek 0,94 → 1 + saydamlık), sonra sabit.
- `Gerisi bizde.` Fredoka 700 (≈ 96 px, 900 px'e sığan), y ≈ 470–590, `Gerisi` çapasında (26,04), sözcük zamanlı.
- `@ydspublishing · YouTube` Lexend 700 ≈ 56, y ≈ 1160–1240, `YDS` çapasında (28,51); `@ydspublishing` sarı hapta (tek vurgu).
- Yasak: "Tam ders", süre, saat simgesi, oynat/izle düğmesi taklidi, YouTube logosu taklidi, QR.
- Altyazı + karaoke 1400–1550 (cümle 4). Kuyruk 30,83–31,75 durgun. Çip yok.

## Doğrula (zorunlu, geçmeden bitirme)
1. `cd K && bash araclar/qa-yerel.sh 02-04-ydt-temel-s1 03-hyperframes-cta 25.55,28.60,31.70 31.70 --hazirla` → çıkış 0. t değerleri KÜRESEL anlatım saniyesidir (yerel değil): ilk kare 25,55, orta 28,60, son kare 31,70; koyu tema 31.70. qa-yerel ya da kapı dikey paketi ölçemiyorsa dur ve hatayı aynen raporla; aracı değiştirme.
2. Çakışma kapısı: `cd K && node araclar/cakisma-kapisi.mjs 02-04-ydt-temel-s1 --sahne 03-hyperframes-cta --port 41333 --sunucu 41022` → çıkış 0, 0 uyarı.
3. Metin taraması: `grep -rniE 'tam ders|dakika' K/projeler/02-04-ydt-temel-s1/sahneler/03-hyperframes-cta/ --include=*.html --include=*.js --include=*.py` boş.
4. Kanal katmanı: QA karelerinin hepsinde görünür, konum ve boy tablodakiyle aynı (karede ölç; standart §7 madde 2).
Üretilen PNG'lere (`sahneler/03-hyperframes-cta/k/`, `k/koyu/`) Read ile BAK: taşma, kesik yazı, üst üste binme, okunmaz kontrast, boş kare,
0–280 ve 1570–1920 boş mu, sağ 960–1080 bölgesinde içerik var mı. En çok 4 düzeltme turu; geçmezse dur ve raporla.

## Rapor
`sahneler/03-hyperframes-cta/RAPOR.md` (eski RAPOR.md varsa önce Silinecekler'e kopyala): olay listesi, kapı sonuçları (son satırlar), bakılan kareler
ve bulgu, agy koşu özeti yolu, açık noktalar. Son mesajın en çok 10 satır: kapı çıkış kodları, kare yolları, agy koşu özeti, açık noktalar.
