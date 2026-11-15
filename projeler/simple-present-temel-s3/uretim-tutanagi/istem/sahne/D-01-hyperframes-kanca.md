# İstem D — simple-present-temel-s3 sahne 01-hyperframes-kanca (huni v2) · 15.11.2026

<!-- P0202-S3-C (15.11) yazdı. Şablon: emsal `K/projeler/02-04-ydt-temel-s1/uretim-tutanagi/istem/sahne-v2/D-01-hyperframes-kapak.md`. -->

MAKİNE: Linux x86_64 (srv21), kullanıcı sef. K=`/home/sef/01dev/_worktrees/kalem-0204` (git worktree, dal `sunucu/02-04-ydt-temel`),
D=`/home/sef/01dev/dijital-anlatim`. Node `~/.nvm/versions/node/v24.22.2/bin`. Python `/usr/bin/python3 -I`. Skill `~/.claude/skills/motion-grafik-ders/`.
KURALLAR: Yalnız bu sahnenin dizinine yaz: `K/projeler/simple-present-temel-s3/sahneler/01-hyperframes-kanca/` (klasör yeni; sen açarsın). Ek çıktı (kapak A, tek kare PNG): paket kökü `kapak-a.png` + `kapak.png` (aynı dosya) ve `sahneler/01-hyperframes-kanca/k/koyu/kapak-a-koyu.png`. Başka sahneye, `ortak/`a,
`BRIEF-S3.md`'ye, `zaman.json`'a, ana derse (`simple-present-temel`) ve emsal pakete (`02-04-ydt-temel-s1`) dokunma (ikisi yalnız okunur);
eksik görürsen raporla. Silme yok (`~/Silinecekler/2026-11-15-0204/simple-present-temel-s3/` altına taşı). mp4 render YOK: `calistir.sh`'ı yalnız `ONIZLE_YALNIZ=1` ile koş. Kapak A için `hyperframes snapshot` tek kare serbest. git commit yok. Claude alt ajanı açma.
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
üzerine yazman gerekirse önce `~/Silinecekler/2026-11-15-0204/simple-present-temel-s3/sahneler/01-hyperframes-kanca/` altına kopyala.

## Okuma
1. `D/.claude/docs/huni-v2-standart.md` (tamamı; BAĞLAYICI: §1 kurallar, §2 yerleşim, §3 yapı, §6 türevler, §7 kapı).
2. Skill `SKILL.md`, `references/kalem-hatti.md`, `stil-anayasasi.md`, `hareket-sozlugu.md`, `kliseler.md`.
3. Paket: `K/projeler/simple-present-temel-s3/BRIEF-S3.md` ("Yerleşim", "Kanal katmanı" tablosu, "Sahneler" satırı: `| 1 Kanca | 01-hyperframes-kanca | HyperFrames | 0,00–3,89 | 129 | öğretmen |`; "Sahne içeriği" 0,00–3,89 satırları; "Kapak" bölümü), `zaman.json`
   (`sahneler[]`, `hikaye`, `duragan[]`), `ortak/anlatim/senaryo.json` + `sozcukler.json` + `baslar.json` + `altyazi.json` (cümle 1: `He` 1,00 · `doesn't` 1,32 · `goes.` 1,72 · `Hata` 2,69 · `nerede?` 3,09–3,89; olay söylendiği anda gelir, zaman sözcük çapasından),
   `uretim-tutanagi/S3-C-RAPOR.md`, `uretim-tutanagi/S3-duzeltme.md`, `uretim-tutanagi/kapak-taslak.md` §1–§3, `D/.claude/docs/kapak-standardi.md` (çıkartma kenarı).
4. Kod tabanı (emsal v2, yalnız okunur): `K/projeler/02-04-ydt-temel-s1/sahneler/01-hyperframes-kapak/` (`SPEC.md`, `uret.py`, `yardim.py`, `olay.py`, `calistir.sh`, `zamanlar.json`, `nesneler.json`, `olaylar.json`, `proje-ka/` kapak A yöntemi, `RAPOR.md`). `calistir.sh`, `olay.py`, `yardim.py` kopyalanır (paket, klasör, çıktı adı ve konu metni Edit ile); `uret.py` içerik farklı → SPEC + agy. İçerik baştan kurulur: ev, bavul ve doodle figür YOK; kart + karakter görseli var.

## Kanal katmanı ve künye (bütün sahnelerde AYNI; değer değiştirme)
| Öğe | Değer |
|---|---|
| Logo | `ortak/logo/` (açık `yds-publishing-lacivert.svg`, koyu `yds-publishing-seffaf.svg`); yükseklik 48, genişlik 193,5; resim x 53,2 (görünür sol kenar x 60), y 291–339 |
| Yazı | `@ydspublishing`, Lexend 700 42 px, renk `murekkep`, x 263, taban y 330 |
| Davranış | 0. kareden son kareye; opaklık 1; giriş/çıkış animasyonu yok; uçuş/geçiş dokunmaz; kimlik `kanal`; `__kalemKutu` türü `kunye`, ad `kunye:kanal` |
| Künye | y 360–450: konu `Simple Present` (Fredoka 700, x 60, taban 420; boy ≤ 34, rozetle x 960'a sığan en büyük, alt sınır 28) + rozet `YDT · BASIC` (hap y 386–434, Lexend 700 26, dolgu `vurguDolgu`, yazı `pilMetin`, konu sonu + 20) |
| Bantlar | üst 0–280 boş (çip YOK) · içerik 460–1380, x 60–960 · altyazı 1400–1550 (en çok 2 satır) · alt 1570–1920 boş |

Künye ortak dosyadan gelmez (paketin tek künye modülü yok): değerleri BRIEF-S3 "Kanal katmanı" tablosundan birebir al, elle başka değer yazma.
HyperFrames: kanal katmanını ve künye satırını emsal sahnenin v2 `yardim.py`'sinden kur (`kunye_svg()`: `<g id="kanal">` = logo `<image>` + `@ydspublishing` `<text>`; künye satırı y 360–450; v2 bant sabitleri). Kopyada yalnız konu metni (`Simple Present`), paket
adı ve yollar değişir. `hf_tema.py` logo `href` değişimi `#logoimg` kimliğini arar: kanal logosunun kimliği `logoimg` kalır.

## Yaz
Tek sütun; yazı tabanı ≥ 64 mantıksal px (künye, kanal ve altyazı hariç; ikincil satır ve etiket ≥ 50); satır ≤ 24 karakter; tek vurgu
sarı (temaya göre); kırmızı (`#d6453a`) YALNIZ yanlış işaretinde: `?`; emoji yok (`✗`, `✓`, `?` ve simgeler SVG kalem çizimidir); sarı hap açık temada dolgu `vurguDolgu`
(`#ffe066`), yazı `pilMetin` (`#1b2440`); tema çifti (açık + koyu). Yasak (standart §1): "Tam ders" sözü, süre sözü ("dakika"), QR,
"izle" düğmesi taklidi.

Bu sahneye özel:
- 0. kare = kapak (ilk kare kapaktır; kanal katmanı + künye dahil): başlık `BU CÜMLE` / `YANLIŞ` (`YANLIŞ` sarı hapta). Fredoka 700, iki satır
  aynı boy, 900 px'e sığan en büyük değer (üst sınır 190; motor ölçer, elle boy yazma), zemin renginde 10 px kontur (`paint-order: stroke fill`), y ≈ 470–800.
- Kart `He doesn't goes.` (Fredoka 80; kâğıt kart + kalem kenarı), sol, x 60'tan, y ≈ 840–1000; kart genişliği yazıya göre (taslaktaki x 640
  Fredoka 80'e dar: ≈ 700 px gerekir, ölç). Yazı küçülmez (alt sınır 72). Ekran metni ses öncesi görünür: kapak istisnası (kalıp §5).
- Karakter: `ortak/kapak/karakter.png` (896×1200 RGBA, ana ders kopyası; ana kapaktaki karakterle aynı) kartın sağında kalan alanda (x kart sonu + 20 … 960), y ≈ 880–1380,
  sola karta işaret eder; arkasında sarı daire (`#fece00`); 10 px krem `#f3efe6` çıkartma kenarı (CSS `drop-shadow`, dört yön; kapak-standardi.md).
  Karakter kartla çakışmaz: gerekirse karakter küçülür, kart değil.
- 0,30–0,80: `YANLIŞ` hap çerçevesi kalemle çizilir.
- 1,00–2,44: kart karaoke sözcük zamanlı (`He` 1,00 · `doesn't` 1,32 · `goes.` 1,72). EN parça kartta, TR parça altyazıda karaoke.
- 2,69–3,15: `Hata` çapasında kartın sağ üstüne kırmızı kalem `?` (SVG yol, ≤ 0,45 sn).
- 3,39–3,89: çıkış: başlık söner, karakter sağa kayarak çıkar, kart içerik bandının üstüne kayar: x 60, y 480–640, Fredoka 80. Bu konum ve boy
  sahne 02 kare 0 ile AYNI (D-02-paperjs-deger.md aynı sabiti yazar). Kanal katmanı ve künye yerinde kalır.
- Altyazı + karaoke 1400–1550 (`Hata nerede?`). Çip yok.
- Kapak A (QA geçtikten sonra): t 0,90 karesi (başlık tam, hap çizili; karaoke ve `?` henüz yok), altyazı katmanı gizli. Yöntem S1-KAPAK-A
  (emsal `proje-ka/`): `proje` kopyasında yalnız CSS `#altyazi{display:none}`, `hyperframes snapshot --at 0.9`, açık ve koyu ayrı.
  Açık → paket kökü `kapak-a.png`, `cp -p kapak-a.png kapak.png`; koyu → `k/koyu/kapak-a-koyu.png`. Karede kanal katmanı ve künye var, altyazı yok.

## Doğrula (zorunlu, geçmeden bitirme)
1. `cd K && bash araclar/qa-yerel.sh simple-present-temel-s3 01-hyperframes-kanca 0.00,1.95,3.80 1.95 --hazirla` → çıkış 0. t değerleri KÜRESEL anlatım saniyesidir (yerel değil;
   yerel kare = round((t − 0,00) × 30)): ilk kare 0,00, orta 1,95, son kare 3,80; koyu tema 1.95. qa-yerel ya da kapı dikey paketi ölçemiyorsa dur ve hatayı aynen
   raporla; aracı değiştirme.
2. Çakışma kapısı: `cd K && node araclar/cakisma-kapisi.mjs simple-present-temel-s3 --sahne 01-hyperframes-kanca --port 41333 --sunucu 41022` → çıkış 0, 0 uyarı.
3. Metin taraması: `grep -rniE 'tam ders|dakika' K/projeler/simple-present-temel-s3/sahneler/01-hyperframes-kanca/ --include=*.html --include=*.js --include=*.py` boş.
4. Kanal katmanı: QA karelerinin hepsinde görünür, konum ve boy tablodakiyle aynı (karede ölç; standart §7 madde 2).
Üretilen PNG'lere (`sahneler/01-hyperframes-kanca/k/`, `k/koyu/`) Read ile BAK: taşma, kesik yazı, üst üste binme, okunmaz kontrast, boş kare,
0–280 ve 1570–1920 boş mu, sağ 960–1080 bölgesinde içerik var mı. En çok 4 düzeltme turu; geçmezse dur ve raporla.

## Rapor
`sahneler/01-hyperframes-kanca/RAPOR.md`: olay listesi, kapı sonuçları (son satırlar), bakılan kareler ve bulgu, agy koşu özeti yolu, açık noktalar.
Son mesajın en çok 10 satır: kapı çıkış kodları, kare yolları, agy koşu özeti, açık noktalar.
