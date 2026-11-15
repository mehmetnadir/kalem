# İstem D-V2-S3 — 02-04-ydt-temel-s3 sahne 03-hyperframes-cta (çağrı, yeniden) · huni v2 · 15.11.2026

MAKİNE: Linux x86_64 (srv21), kullanıcı sef. K=`/home/sef/01dev/_worktrees/kalem-0204` (git worktree, dal `sunucu/02-04-ydt-temel`).
Node `~/.nvm/versions/node/v24.22.2/bin`. Python `/usr/bin/python3 -I`. Skill `~/.claude/skills/motion-grafik-ders/`.
KURALLAR: Yalnız bu sahnenin dizinine yaz: `K/projeler/02-04-ydt-temel-s3/sahneler/03-hyperframes-cta/`. Tek istisna: ana kapak kopyası
`K/projeler/02-04-ydt-temel-s3/ortak/kapak/ana-kapak.png` ve `ana-kapak-koyu.png` (aşağıda; dizin yoksa aç). Başka sahneye, `ortak/`un
geri kalanına, `BRIEF-S3.md`'ye, `zaman.json`'a, ana derse (`02-04-ydt-temel`, yalnız okunur) ve S1 paketine dokunma (eksik görürsen
raporla). Silme yok. v1 sahne kodunun yedeği hazır: `~/Silinecekler/2026-11-15-huni-v2/02-04-ydt-temel-s3/sahneler-v1/03-hyperframes-cta/`
(V2-S3-C aldı); yerinde düzenle, v1'e oradan bak. mp4 render YOK: `calistir.sh`'ı yalnız `ONIZLE_YALNIZ=1` ile koş. git commit yok.
Claude alt ajanı açma. Kanca atlama bayrağı oluşturma (`/tmp/conductor-*`, `~/.conductor/*`); sözleşme kancası isterse
`K/.claude/docs/sozlesme.md` dosyasına 1–2 satır ekle.

## İlk adım: ana kapak (yoksa DUR)
1. `ls -la K/projeler/02-04-ydt-temel/kapak.png K/projeler/02-04-ydt-temel/kapak-koyu.png` (1920×1080, `kapak-standardi.md`).
2. İkisi de varsa `cp -a` ile `K/projeler/02-04-ydt-temel-s3/ortak/kapak/ana-kapak.png` ve `ana-kapak-koyu.png` olarak kopyala;
   `cmp` ile doğrula. Kaynak dosyalardan biri yoksa başka hiçbir şey yapma: `sahneler/03-hyperframes-cta/RAPOR.md`'ye ve son mesaja
   "ana kapak bekliyor" yaz, DUR. (15.11 18:35 ölçümü: iki dosya da var, 1920×1080.)

## Kod yolu (kapı ve doktrin)
Kod yazma kapısı 15 satırdan uzun kod dosyasını sana kapatır; bayrak açmaya çalışma. Yol: tasarımı sahne dizininde `SPEC.md` olarak
yaz (yazılacak dosyanın mutlak yolu, örnek sahnenin mutlak yolu ve oradan alınacak kalıp, olay listesi olay · kare/küresel sn · cümle
sözcüğü, yerleşim, ekran metni, kurallar, kabul ölçütü; tam kod YAZMA). Sonra
`agy-filo tek --rol kod --cwd /home/sef/01dev/_worktrees/kalem-0204 --zaman 25m -p "<SPEC.md mutlak yolunu oku ve uygula. Yalnız <dosya
mutlak yolu> dosyasını yaz. Başka dosyaya dokunma. Silme yok. Test, render, git yok.>"`. Kodu agy yazar; sen baştan sona okur, spec'e
uyuyor mu bakarsın, küçük düzeltmeyi Edit ile yaparsın, büyük düzeltmeyi agy'ye geri verirsin (en çok 2 tur). Tam kodu kendin yazıp
agy'ye birebir kopyalatmak YASAK. Kısa dosyalar (`calistir.sh`, `sayfa.html`) ve var olan dosyada küçük değişiklik Edit ile yapılır.

## Okuma
1. BAĞLAYICI: `/home/sef/01dev/dijital-anlatim/.claude/docs/huni-v2-standart.md` (§1 kural 2, 3, 4, 5, 7; §2; §3 çağrı sahnesi; §4; §7).
   Kapak dosyaları: `/home/sef/01dev/dijital-anlatim/.claude/docs/kapak-standardi.md`.
2. Skill `SKILL.md`, `references/kalem-hatti.md`, `stil-anayasasi.md`, `hareket-sozlugu.md`, `kliseler.md`.
3. Paket `K/projeler/02-04-ydt-temel-s3/`: `BRIEF-S3.md` ("Yerleşim" tablosu; "Sahneler" 4. satırı `| 4 Çağrı | 03-hyperframes-cta |
   HyperFrames | 21.33–28.31 | 239 | öğrenci |`; "Sahne içeriği" 21,33–28,31 satırları), `zaman.json` (bu sahne 21,33–28,31 küresel sn,
   239 kare = 209 içerik + 30 kuyruk; `sahneler[]` son sıra), `ortak/anlatim/senaryo.json` + `sozcukler.json` + `baslar.json` +
   `altyazi.json` + `METIN.md` (cümle 5, ÖĞRENCİ sesi, 21,88–27,31: `Bu` 21,88 · `sadece` 22,12 · `başlangıç.` 22,68 · `Dersin` 23,79 ·
   `tamamı` 24,35 · `YDS` 25,07 · `Publishing` 25,55 · `YouTube` 26,19 · `kanalında.` 26,59). Olay söylendiği anda gelir.
4. Başlangıç noktası: var olan v1 sahne kodu (`calistir.sh`, `uret.py`, `yardim.py`, `olay.py` kalıbı). v1 içeriği (`üç farktan biri`,
   ders bandı, saat, eski çağrı satırı, tren/bilet döngüsü) TAMAMEN kalkar.
5. v1 istemi (yalnız tarih için; içerik GEÇERSİZ): `uretim-tutanagi/istem/sahne/D-03-hyperframes-cta.md`.

## v2 yerleşim ve kanal katmanı (bütün sahnelerde AYNI piksel)
Künye ortak dosyadan GELMEZ: `ortak/kunye.js` ve sahnelerin `yardim.py` künyesi v1 HUD'dur (logo 48–144, ders adı 212, çip) ve v2 kanal
katmanını taşımaz. Aşağıdaki değerleri aynen kullan; ölçü icat etme. Değerler S1 ve S2 kısalarıyla aynı (`K/projeler/02-04-ydt-temel-s1/BRIEF-S1.md` "Kanal katmanı"). v1 HUD öğelerini (üst logo, 2 satır ders adı, çip) kaldır.

| Öğe | Değer |
|---|---|
| Üst boş | y 0–280 yalnız zemin |
| Kanal katmanı (kimlik `kanal`) | logo: tema logosu (açık `ortak/logo/yds-publishing-lacivert.svg`, koyu `yds-publishing-seffaf.svg`; sahnenin `assets/logo.svg` + `hf_tema.py` kalıbı), yükseklik 48, genişlik 193,5 (48 × 1920 / 476,3), resim x 53,2 (SVG iç boşluğu 68/1920 düşülür; görünür sol kenar x 60), y 291–339 · yazı `@ydspublishing` Lexend 700 42 px, renk `murekkep`, x 263, taban y 330 · ilk kareden son kareye opaklık 1; giriş, çıkış, uçuş, solma YOK · `__kalemKutu` türü `kunye`, ad `kunye:kanal` |
| Künye | y 360–450 tek satır: `Simple Present vs Present Continuous` Fredoka 700, x 60, taban y 420, boy ≤ 34 (rozetle x 960'a sığan en büyük, alt sınır 28) · rozet hapı `YDT · BASIC` Lexend 700 26 px, y 386–434, konu sonu + 20, dolgu `vurguDolgu`, yazı `pilMetin` · çip YOK |
| İçerik | y 460–1380, x 60–960; içerik yazısı ≥ 64 px (kanal ve künye standart §2 ölçüsünde) |
| Altyazı + karaoke `#altyazi` | y 1400–1550, x 60–960 (orta x 510), en çok 2 satır, Lexend 500 44 px (uzun parçada 40 → 36) |
| Alt boş | y 1570–1920 yalnız zemin; sağ şerit x 960–1080'e içerik girmez |

Ortak: tek vurgu sarı (açık temada hap dolgusu `#ffe066`, yazı `#1b2440`), doğru şık yeşil, kırmızı yok, emoji yok; satır ≤ 24 karakter;
9 sn'den uzun boş çerçeve yok; ekranda `İzmir` noktalı ve `7 pm`; tema çifti açık + koyu. Eski çağrı kalıbı ("tam ders"), süre sözü, QR,
"izle" düğmesi taklidi yok.


## Bu sahneye özel (çağrı, 21,33–28,31; öğrenci sesi)
- Kare 0'dan: kanal katmanı + künye tam.
- Ana dersin kapağı 16:9 kart: 900×506, x 60–960, y 620–1126 (standart ≈ 920×518; x 60–960 sınırına göre 900), görsel temaya göre
  (`ortak/kapak/ana-kapak.png` açık, `ana-kapak-koyu.png` koyu), köşe yuvarlak 24, ince `murekkep` çerçeve. Sahne başında yumuşak girer
  (≤ 0,4 sn, alfa + hafif ölçek). Kapak üstüne oynat düğmesi, ilerleme çubuğu, süre etiketi YOK ("izle" düğmesi taklidi yok).
- Giriş sözü `Bu sadece başlangıç.` Fredoka 700, kartın üstünde (y 470–600; 900 px'e sığan en büyük boy, üst sınır 96), sözcük zamanlı
  (`Bu` 21,88 · `sadece` 22,12 · `başlangıç.` 22,68).
- `@ydspublishing · YouTube` kartın altında (y 1160–1260): `@ydspublishing` sarı hapta (dolgu `vurguDolgu`, yazı `pilMetin`), `· YouTube`
  `murekkep`; Lexend 700 64. Tek satıra sığmazsa iki satır (`@ydspublishing` / `YouTube`, y 1150–1370). Hap `YDS` (25,07) çapasında
  kalemle çizilir; `YouTube` (26,19) çapasında gelir. YouTube logosu taklidi yok; yalnız yazı.
- 27,31–28,31 durgun kuyruk: kart ve satırlar yerinde, son kare = tam düzen.
- Altyazı `altyazi.json`'dan küresel t ile (cümle 5: 21,88–23,64 ve 23,79–27,39), 1400–1550 bandında, x 60–960. Ekranda marka
  `YDS Publishing` yazar (seste "YeDeSe Publishing").

## Doğrula (zorunlu, geçmeden bitirme)
1. QA kareleri: `cd K && bash araclar/qa-yerel.sh 02-04-ydt-temel-s3 03-hyperframes-cta 21.33,24.82,28.28 27.0 --hazirla` — açık: ilk
   kare 21,33, orta 24,82, son kare 28,28; koyu 27,00. Çıkış kodu 0. qa-yerel t değerleri KÜRESEL anlatım saniyesidir (`zaman.json` t_bas
   21,33 + sahne içi saniye), sahne içi saniye DEĞİLDİR.
2. Çakışma kapısı: `cd K && node araclar/cakisma-kapisi.mjs 02-04-ydt-temel-s3 --sahne 03-hyperframes-cta --port 41333 --sunucu 41022`
   → 0 uyarı. Port doluysa (başka sahne oturumu) 1 dk bekle, yeniden koş.
3. Kanal katmanı (standart §7.2): üç açık karede ve koyu karede logo + `@ydspublishing` görünür, konum aynı (x 60, y 291–339).
4. Ana kapak (standart §7.5): orta ve son karede kapak kartı görünür; koyu karede koyu kapak.
5. Metin taraması: `grep -rniE "tam ders|dakika" K/projeler/02-04-ydt-temel-s3/sahneler/03-hyperframes-cta/proje` → sonuç yok.
6. Kareleri (`k/`, `k/koyu/`) Read ile AÇ: taşma, kesik yazı, üst üste binme, kontrast, boş kare; 0–280 ve 1570–1920 boş mu; içerik
   x 960'ı aşıyor mu; altyazı 1400–1550 içinde mi. En çok 4 düzeltme turu; geçmezse dur, raporla.
qa-yerel ya da kapı paketi ölçemiyorsa dur ve hatayı aynen raporla; aracı değiştirme.

## Rapor
`sahneler/03-hyperframes-cta/RAPOR.md`: ana kapak kopyası (kaynak, `cmp`), olay listesi (olay · küresel sn · sözcük), kanal katmanı konum
ölçümü, qa ve çakışma kapısı sonucu (son satırlar), bakılan kareler ve bulgu, agy koşu özeti yolu, açık noktalar. Son mesajın en çok
10 satır.
