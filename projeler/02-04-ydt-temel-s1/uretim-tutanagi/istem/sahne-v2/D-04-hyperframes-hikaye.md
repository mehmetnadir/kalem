# İstem D-V2 — 02-04-ydt-temel-s1 sahne 04-hyperframes-hikaye (huni v2) · 15.11.2026

<!-- V2-S1-C (15.11) yazdı. Taban: ../sahne/D-s1-sablon.md. Eski istem: ../sahne/D-04-hyperframes-hikaye.md. -->

MAKİNE: Linux x86_64 (srv21), kullanıcı sef. K=`/home/sef/01dev/_worktrees/kalem-0204` (git worktree, dal `sunucu/02-04-ydt-temel`),
D=`/home/sef/01dev/dijital-anlatim`. Node `~/.nvm/versions/node/v24.22.2/bin`. Python `/usr/bin/python3 -I`. Skill `~/.claude/skills/motion-grafik-ders/`.
KURALLAR: Yalnız bu sahnenin dizinine yaz: `K/projeler/02-04-ydt-temel-s1/sahneler/04-hyperframes-hikaye/`. Çıktı: paket kökü `hikaye-a.png` + `hikaye.png` (aynı dosya, `cp -p`) ve `k/koyu/hikaye-a-koyu.png`. Eski PNG yedeği `~/Silinecekler/2026-11-15-huni-v2/02-04-ydt-temel-s1/` altında (V2-C aldı). Başka sahneye, `ortak/`a (yukarıdaki istisna dışında),
`BRIEF-S1.md`'ye, `zaman.json`'a, ana derse (`02-04-ydt-temel`, yalnız okunur) dokunma; eksik görürsen raporla. Silme yok
(`~/Silinecekler/2026-11-15-huni-v2/02-04-ydt-temel-s1/` altına taşı). mp4 render YOK (tek kare PNG serbest: `calistir.sh --tema acik|koyu`). git commit yok. Claude alt ajanı açma.
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
`~/Silinecekler/2026-11-15-huni-v2/02-04-ydt-temel-s1/sahneler/04-hyperframes-hikaye/` altına kopyala.

## Okuma
1. `D/.claude/docs/huni-v2-standart.md` (tamamı; BAĞLAYICI: §1 kurallar, §2 yerleşim, §3 yapı, §6 türevler, §7 kapı).
2. Skill `SKILL.md`, `references/kalem-hatti.md`, `stil-anayasasi.md`, `hareket-sozlugu.md`, `kliseler.md`.
3. Paket: `K/projeler/02-04-ydt-temel-s1/BRIEF-S1.md` ("Yerleşim", "Kanal katmanı" tablosu, "Sahneler" satırı: `| — | 04-hyperframes-hikaye · … | HyperFrames | zaman çizelgesi dışı | 1 | — |`; "Hikâye kareleri" bölümü), `zaman.json`
   (`sahneler[]`, `hikaye`, `duragan[]`), `ortak/anlatim/senaryo.json` + `sozcukler.json` + `baslar.json` + `altyazi.json` (anlatım yok; kural özeti metni BRIEF-S1 girişinde),
   `uretim-tutanagi/V2-C-RAPOR.md`, `uretim-tutanagi/hikaye-taslak.md`.
4. Var olan sahne (v1; kod tabanı): `K/projeler/02-04-ydt-temel-s1/sahneler/04-hyperframes-hikaye/` (v1 kural kartı; `Tam ders:` / `profildeki bağlantı` satırı ve `Full lesson` çipi kalkar).

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
- Durağan kare: anlatımdan bağımsız, ses yok, altyazı yok, çip yok. Kanal katmanı + künye tablodaki gibi.
- Düzen A (kural kartı; B'den farklı): içerik y 460–1140: `YAŞI-YOR-UM` (Fredoka; `YOR` sarı kutu) · iki kart yan yana `I live` + `PERMANENT`
  + ev ikonu / `I am living` + `TEMPORARY` + bavul ikonu · kural özeti `Kalıcıysa geniş zaman,` / `geçiciyse şimdiki zaman.` (Fredoka 700 ≥ 64) ·
  yer imi simgesi (SVG yol, emoji değil) + `Kaydet` sarı hap. Sığmazsa v1'deki `Türkçede tek sözcük` / `İngilizcede iki zaman` satırları çıkar.
- y 1150–1380 boş zemin (bağ çıkartması elle konur; kutu ya da çerçeve çizme). 1400–1920 boş.

## Doğrula (zorunlu, geçmeden bitirme)
1. `bash K/projeler/02-04-ydt-temel-s1/sahneler/04-hyperframes-hikaye/calistir.sh --tema acik` ve `--tema koyu` → rc 0; `file` çıktısı 1080×1920 PNG (tek kare; zaman çizelgesi dışı, qa-yerel ölçmez). QA kareleri: açık tek kare (ilk = orta = son) + koyu tek kare.
2. Çakışma kapısı: `cd K && node araclar/cakisma-kapisi.mjs 02-04-ydt-temel-s1 --sahne 04-hyperframes-hikaye --port 41333 --sunucu 41022`. Araç yalnız `zaman.json → sahneler[]` okur; durağan kare için `HATA sahne bulunamadı` (çıkış 2) beklenir (S1-VAR-RAPOR §5). Komutu yine koş, çıktıyı aynen RAPOR'a yaz; aracı değiştirme. Çakışmayı karede gözle denetle.
3. Metin taraması: `grep -rniE 'tam ders|dakika' K/projeler/02-04-ydt-temel-s1/sahneler/04-hyperframes-hikaye/ --include=*.html --include=*.js --include=*.py` boş.
4. Kanal katmanı: QA karelerinin hepsinde görünür, konum ve boy tablodakiyle aynı (karede ölç; standart §7 madde 2).
Üretilen PNG'lere (`sahneler/04-hyperframes-hikaye/k/`, `k/koyu/`) Read ile BAK: taşma, kesik yazı, üst üste binme, okunmaz kontrast, boş kare,
0–280 ve 1570–1920 boş mu, sağ 960–1080 bölgesinde içerik var mı. En çok 4 düzeltme turu; geçmezse dur ve raporla.

## Rapor
`sahneler/04-hyperframes-hikaye/RAPOR.md` (eski RAPOR.md varsa önce Silinecekler'e kopyala): olay listesi, kapı sonuçları (son satırlar), bakılan kareler
ve bulgu, agy koşu özeti yolu, açık noktalar. Son mesajın en çok 10 satır: kapı çıkış kodları, kare yolları, agy koşu özeti, açık noktalar.
