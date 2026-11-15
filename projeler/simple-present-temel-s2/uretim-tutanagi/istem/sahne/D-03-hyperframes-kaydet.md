# İstem D-V2 — simple-present-temel-s2 sahne 03-hyperframes-kaydet (huni v2) · 15.11.2026

<!-- S2-C (15.11) yazdı. Şablon: K/projeler/02-04-ydt-temel-s1/uretim-tutanagi/istem/sahne-v2/D-08-hyperframes-kaydet.md. -->

MAKİNE: Linux x86_64 (srv21), kullanıcı sef. K=`/home/sef/01dev/_worktrees/kalem-0204` (git worktree, dal `sunucu/02-04-ydt-temel`),
D=`/home/sef/01dev/dijital-anlatim`. Node `~/.nvm/versions/node/v24.22.2/bin`. Python `/usr/bin/python3 -I`. Skill `~/.claude/skills/motion-grafik-ders/`.
KURALLAR: Yalnız bu sahnenin dizinine yaz: `K/projeler/simple-present-temel-s2/sahneler/03-hyperframes-kaydet/` (klasör yeni; sen açarsın).
Başka sahneye, `ortak/`a, `BRIEF-S2.md`'ye, `zaman.json`'a, ana derse (`simple-present-temel`) ve emsale (`02-04-ydt-temel-s1`) dokunma (ikisi
yalnız okunur); eksik görürsen raporla. Silme yok (`~/Silinecekler/2026-11-15-0204/simple-present-temel-s2/` altına taşı). mp4 render YOK:
`calistir.sh`'ı yalnız `ONIZLE_YALNIZ=1` ile koş. git commit yok. Claude alt ajanı açma.
Kanca atlama bayrağı OLUŞTURMA (`/tmp/conductor-*`, `~/.conductor/*`). Durdurma kancası sözleşme satırı isterse `K/.claude/docs/sozlesme.md`
dosyasına 1–2 satır EKLE (tek istisna).

## Kod yolu (kapı ve doktrin)
Kod yazma kapısı 15 satırdan uzun kod dosyasını sana kapatır; bayrak açmaya çalışma. Emsalden kopyalanan dosyalar (`calistir.sh`, `olay.py`,
`yardim.py`) `cp -p` + küçük Edit ile kurulur (paket adı, klasör adı, çıktı adı, künye konu adı). Yeni içerik taşıyan kod (`uret.py`): tasarımı
sahne dizininde `SPEC.md` olarak yaz (yazılacak dosyanın mutlak yolu, var olan kodun mutlak yolu ve oradan alınacak kalıp, olay listesi olay ·
kare/küresel sn · cümle sözcüğü, yerleşim, ekran metni, kurallar, kabul ölçütü; tam kod YAZMA). Sonra
`agy-filo tek --rol kod --cwd /home/sef/01dev/_worktrees/kalem-0204 --zaman 25m -p "<SPEC.md mutlak yolunu oku ve uygula. Yalnız <dosya
mutlak yolu> dosyasını yaz. Başka dosyaya dokunma. Silme yok. Test, render, git yok.>"`. Kodu agy yazar; sen baştan sona okur, spec'e
uyuyor mu bakarsın, küçük düzeltmeyi Edit ile yaparsın, büyük düzeltmeyi agy'ye geri verirsin (en çok 2 tur). Tam kodu kendin yazıp
agy'ye birebir kopyalatmak YASAK.

## Okuma
1. `D/.claude/docs/huni-v2-standart.md` (tamamı; BAĞLAYICI: §1 kural 6, §2 yerleşim, §3 "3 Kaydet", §4 kaydet kalıbı, §7 kapı).
2. Skill `SKILL.md`, `references/kalem-hatti.md`, `stil-anayasasi.md`, `hareket-sozlugu.md`, `kliseler.md`.
3. Paket: `K/projeler/simple-present-temel-s2/BRIEF-S2.md` ("Yerleşim", "Kanal katmanı" tablosu, "Sahneler" satırı:
   `| 3 Kaydet | 03-hyperframes-kaydet | HyperFrames | 11,87–19,07 | 228 | öğretmen |`; "Sahne içeriği" 11,87–19,07 satırları), `zaman.json`
   (sahne no 3, kare 228 = içerik 216 + geçiş 12; dokunma), `ortak/anlatim/senaryo.json` + `sozcukler.json` + `baslar.json` + `altyazi.json`
   (cümle 3: `Usually,` 12,42 · `always,` 13,70 · `every` 14,50 · `day:` 14,74 · `Simple` 15,54 · `Present.` 15,86–16,50 · `Bu` 16,75 ·
   `kuralı` 16,91 · `kaybetme.` 17,31 · `Kaydet.` 18,47–19,15), `uretim-tutanagi/S2-C-RAPOR.md`, `uretim-tutanagi/senaryo-taslak.md` §2 sahne 3.
4. Kod tabanı (yalnız okunur): emsalde kaydet sahnesi 15.11 19:10 ölçümünde YOK (`02-04-ydt-temel-s1/sahneler/08-hyperframes-kaydet/`);
   sen başladığında kurulmuşsa önce ona bak (aynı rol). Yapı örneği aynı motordan, v2: `K/projeler/02-04-ydt-temel-s1/sahneler/03-hyperframes-cta/`
   (`calistir.sh`, `olay.py`, `yardim.py`, `uret.py`, `zamanlar.json`, `nesneler.json`, `olaylar.json`). Emsal tarif:
   `K/projeler/02-04-ydt-temel-s1/uretim-tutanagi/istem/sahne-v2/D-08-hyperframes-kaydet.md`.
5. Sözleşme `K/.claude/docs/sozlesme.md` huni v2 satırları ("HF huni v2 kanal katmanı `Y.html` ile", `kunye_svg()`, `#logoimg`, `.tema-acik #id`).

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

Bu sahneye özel (sn KÜRESEL):
- 11,87'de başlar (ilk 12 kare = 11,87–12,27 geçiş payı), 19,07'de biter. Altyazı 11,87–11,95 cümle 2'nin son sözcüğünü (`gibi.`) taşıyabilir.
- Kural özeti kartı: tek cümle üç satır `Usually, always,` / `every day:` / `Simple Present.` (Fredoka 700 72; kâğıt kart + kalem kenarı),
  x 60–960, y ≈ 560–900. Kart girişi 12,42'de tek hareket (ölçek 0,96 → 1 + saydamlık, ≤ 0,45 sn). Yazı sözcük zamanlı: `Usually,` 12,42 ·
  `always,` 13,70 · `every day:` 14,50 · `Simple Present.` 15,54. `Simple Present` sarı hapta (sahnenin tek sarısı; 15,54).
- 15,86'dan 19,07'ye kart sabit (hareketsiz; 3,21 sn ≥ standart "2 sn sabit").
- `Kaydet.` çapası 18,47: yer imi simgesi (SVG yol; Tabler `bookmark` biçimi: dikdörtgen gövde + alt V çentik; yerel `ortak/cizim/tabler/` içinde
  YOK, yolu sahne içinde yaz; emoji değil) kalem darbesiyle ≤ 0,3 sn çizilir, mürekkep; yanında `Kaydet` (Fredoka 700 72, mürekkep, hapsız —
  sarı yalnız `Simple Present`'te); ikisi kartın altında ortalı, y ≈ 960–1060.
- Sahne 02 öğeleri sahne sınırında solar (geçiş birleştirmede); bu sahnede yalnız kart + `Kaydet`.
- Altyazı + karaoke 1400–1550 (cümle 3). Çip yok.

## Doğrula (zorunlu, geçmeden bitirme)
1. `cd K && bash araclar/qa-yerel.sh simple-present-temel-s2 03-hyperframes-kaydet 11.95,15.45,19.00 19.00 --hazirla` → çıkış 0. t değerleri
   KÜRESEL anlatım saniyesidir (yerel değil): ilk kare 11,95, orta 15,45, son kare 19,00; koyu tema 19.00. qa-yerel ya da kapı dikey paketi
   ölçemiyorsa dur ve hatayı aynen raporla; aracı değiştirme.
2. Çakışma kapısı: `cd K && node araclar/cakisma-kapisi.mjs simple-present-temel-s2 --sahne 03-hyperframes-kaydet --port 41333 --sunucu 41022`
   → çıkış 0, 0 uyarı.
3. Metin taraması: `grep -rniE 'tam ders|dakika' K/projeler/simple-present-temel-s2/sahneler/03-hyperframes-kaydet/ --include=*.html --include=*.js --include=*.py` boş.
4. Kanal katmanı: QA karelerinin hepsinde görünür, konum ve boy tablodakiyle aynı (karede ölç; standart §7 madde 2).
Üretilen PNG'lere (`sahneler/03-hyperframes-kaydet/k/`, `k/koyu/`) Read ile BAK: taşma, kesik yazı, üst üste binme, okunmaz kontrast, boş kare,
0–280 ve 1570–1920 boş mu, sağ 960–1080 bölgesinde içerik var mı. En çok 4 düzeltme turu; geçmezse dur ve raporla.

## Rapor
`sahneler/03-hyperframes-kaydet/RAPOR.md`: olay listesi, kapı sonuçları (son satırlar), bakılan kareler ve bulgu, agy koşu özeti yolu, açık
noktalar. Son mesajın en çok 10 satır: kapı çıkış kodları, kare yolları, agy koşu özeti, açık noktalar.
