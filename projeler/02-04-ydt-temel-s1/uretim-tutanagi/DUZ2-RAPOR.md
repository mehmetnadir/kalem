# DUZ2-0204S1 raporu — 02-04-ydt-temel-s1 (kol a) · J2 özeti A sınıfı düzeltmeleri · 15.11.2026

Yazan: üretici oturumu (fa49db46), model Claude Opus 5.5 (`claude-opus-5-5`). İstem DUZ2-0204S1. Girdi: `uretim-hatti/raporlar/J2-OZET-1511.md`
§3A, §4.1, §4.2 satır T1; `juri/J2-hukum.md`. Ses sentezi, mp4, commit, alt ajan, imagen YOK. Silinen dosya yok; taşınanlar
`~/Silinecekler/2026-11-15-duz2-0204S1/` (`LISTE.md`). Kol b raporu: `../../02-04-ydt-temel-s1b/uretim-tutanagi/DUZ2-RAPOR.md`.

| Ölçüm | Değer |
|---|---|
| Düzeltilen kusur | A1 (TD-1 rozet) · A3 (EK-5b kural kapsamı) · C1 parçası (HV-22: sahne 02 `yor` çip 1 × `-um.`) |
| Uygulanmayan toplu düzeltme | TD-2 (SP paketi), TD-3 (grep 0), TD-4 (grep 0) — bu pakette iş yok |
| Yeniden sentez | 0 cümle (A3 kartı seste yok; ses ve zaman dosyaları değişmedi) |
| Süre | 31,75 sn (`anlatim.m4a` ffprobe 31,750000; ≤ 35 ✓, hedef 22–26 ✗ — D-0279 istisnası) |
| Whisper en düşük | 0,96 (cümle 2 `I am living with my uncle.` → "I'm living…"); eşik 0,90 ✓ |
| Çakışma kapısı | video sahneleri çıkış **0** (4 sahne, 0 uyarı) · durağan türevler çıkış **0** (4 sahne, geçici kök) |
| Kareler | 4 sahne + kapak A/B/C + hikâye A/B, açık + koyu, yeniden çekildi; hepsine Read ile bakıldı |

## 1. Düzeltmeler

| # | Kusur | Dosya | Önce → sonra | Kanıt |
|---|---|---|---|---|
| 1 | A1 / TD-1 (KS-2 → HV-24) | `ortak/anlatim/senaryo.json` `giris.rozetler`, `ortak/kunye.js` `rozet`, `BRIEF-S1.md` §künye, 7 × `sahneler/*/yardim.py` (`ROZET` / `ROZETLER`), 7 × `SPEC.md` | `YDT · BASIC` → `YDT · TEMEL` | `grep -rln BASIC --include=*.py/*.js/*.json/*.md` (RAPOR.md, `uretim-tutanagi/` ve `/k/` dışı) → 0 dosya; bütün karelerde hap `YDT · TEMEL`; çağrı karesinde künye ve ana kapak kartı aynı metin (HV-24 "aynı karede iki rozet metni yok" ✓) |
| 2 | A3 (EK-5b) kaydet kartı | `sahneler/08-hyperframes-kaydet/uret.py` (`#kural0` yeni) | 2 satır `Kalıcıysa geniş zaman,` / `geçiciyse şimdiki zaman.` → 3 satır `Live, work fiillerinde:` / `kalıcıysa geniş zaman,` / `geçiciyse şimdiki zaman.` (Fredoka 700, boy 73, taban 717 / 813 / 909; kart iç kenarına ≥ 39 px) | `k/08-hyperframes-kaydet-25.4.png`, `k/koyu/08-hyperframes-kaydet-25.4.png` |
| 3 | A3 hikâye A | `sahneler/04-hyperframes-hikaye/uret.py` | özet 2 → 3 satır (taban 924 / 1008 / 1092); `Kaydet` 1048–1136 → 1416–1504 (hikâye B ile aynı yer; 1150–1380 boş kalır) | `hikaye-a.png` (= `hikaye.png`, md5 `7f52fd9c5eba`), `sahneler/04-…/k/koyu/hikaye-a-koyu.png`; uret.py assert'leri geçti (kesişim 0, boşluk ≥ 16, satır ≤ 24) |
| 4 | A3 hikâye B | `sahneler/07-hyperframes-hikaye-b/uret.py` | özet 2 → 3 satır (taban 959 / 1039 / 1119, alt kenar 1136 ≤ 1140); Türkçe cümle, şık kartı, etiketler 28 px yukarı (tr 517/601, kart 714/794, etiket 880) | `hikaye-b.png` (md5 `4ff7a7a62c59`), `sahneler/07-…/k/koyu/hikaye-b-koyu.png`; assert'ler geçti |
| 5 | A3 belge | `BRIEF-S1.md` §kural özeti ve zaman çizelgesi; `SPEC.md` (04, 07, 08) | kart metni ve konumlar yeni değerlere | `grep -c Kalıcıysa` SPEC 04/07/08 → 0 |
| 6 | C1 / HV-22 (J2 §4-4, KBJ HV-22) | `sahneler/02-paperjs-ornek/kalem-paper.js` (`yazi` isteğe bağlı `sonKay`, varsayılan 36), `sahne-02.js` (`SON_KAY = 24`, 4 TR parçası) | sönen satır 2 `-um.` 36 px yukarı kayıyor, çip 1 kutusuna 72×12 px biniyordu (8,37–8,43 sn) → kayma 24 px, kesişim yok | dar pencere ölçümü (8,30–8,47 sn, 6 kare): önce 3 karede `yor çip 1 × -um.` 72×11–12 px uyarı → sonra 0; kapı tam koşu 0 uyarı (§3) |

A3 metin kararı (J2-OZET önerisi "live, work, stay gibi eylemlerde: …" denetlendi):

| Öneri parçası | Karar | Gerekçe |
|---|---|---|
| `stay` | çıkarıldı | `stay` doğası gereği geçicidir; geniş zamanda kalıcı durum değil alışkanlık bildirir (`I stay at home on Sundays`). "kalıcıysa geniş zaman" `stay` için yanlış olur. |
| `gibi` | çıkarıldı | ekran satırı ≤ 24 karakter (SPEC §5.7, uret.py assert): `live, work gibi fiillerde:` = 27. `Live, work fiillerinde:` = 23. Kapsam daralır ama doğru kalır. |
| `eylemlerde` → `fiillerinde` | değişti | sınav dilindeki terim "fiil" (MEB); ses ve kartın öteki terimleri okul terimleri (geniş zaman, şimdiki zaman). |
| Büyük harf `Live` | değişti | cümle başı. |

Bağımsız doğruluk: `live`, `work` fiillerinde kalıcı durum → Simple Present (`I live in Istanbul`, `I work in a bank`), geçici durum →
Present Continuous (`I am living with my uncle`, `I'm working in a café this summer`). Genelleme durum fiillerine taşmaz (`I have a cold
this week` kartın kapsamı dışında). Ses aynı terimleri taşır: cümle 2 "kalıcı durum, geniş zaman" / "geçici durum, şimdiki zaman" ↔
kart "kalıcıysa geniş zaman" / "geçiciyse şimdiki zaman". Kapak A/B/C kural cümlesi taşımaz. Açıklama satırları örneğe bağlıdır
(`I live in İstanbul. → kalıcı durum, geniş zaman`); değişiklik gerekmedi.

## 2. Süre, ilk söz, Whisper (ses değişmedi; değerler yeniden okundu)

| Ölçü | Değer | Sınır | Durum |
|---|---|---|---|
| Toplam süre | 31,75 sn | ≤ 35 (hedef 22–26) | sınır içinde; hedef aşılır (D-0279) |
| İlk söz | 1,00 sn | ≤ 1 | ✓ |
| Kanca cümlesi bitişi (sözcük t1) | 6,44 sn (`sureler.json` 1,00 + 5,36 = 6,36) | kanca ≤ 4 sn | **aşar** (ekran kancası 3,0 sn; ses kancası üç kısa cümle, J2 HV-12 "evet" saydı) |

| Cümle | Parça | Whisper |
|---|---|---|
| 1 | İstanbul'da yaşıyorum. Amcamla yaşıyorum. Türkçede ikisi de yaşıyorum. | 1,00 |
| 2 | İngilizcede ikisi ayrılır. · I live in Istanbul. · Hep orada: … · I am living with my uncle. · Şimdilik: … | 1,00 · 1,00 · 1,00 · **0,96** · 1,00 |
| 3 | Bu, üç farktan yalnız biri. · Sınavdan önce lazım olacak. Kaydet. | 1,00 · 1,00 |
| 4 (öğrenci) | Gerisi bizde. · Dersin tamamı YDS Publishing YouTube kanalında. | 1,00 · 1,00 ("YEDESE Publishing", HV-17) |

## 3. Kareler ve kapı

Eski kareler (rozet BASIC) `~/Silinecekler/2026-11-15-duz2-0204S1/eski-kare/02-04-ydt-temel-s1/` altına taşındı. Yöntem: video sahneleri
`ONIZLE_YALNIZ=1 bash calistir.sh --tema koyu|acik` + `node araclar/sahne-kare.mjs … --port 41333 --sunucu 41022`; kapak A `proje-ka`
(`#altyazi{display:none}`) + `hyperframes snapshot --at 1.97`; durağan türevler `bash calistir.sh --tema koyu`, sonra `--tema acik`.

| Sahne / türev | Açık | Koyu | Göz denetimi |
|---|---|---|---|
| 01 kanca | `k/01-…-0.2 · 1.97 · 2.45 · 2.95.png` | `k/koyu/…-1.97 · 2.45.png` | rozet `YDT · TEMEL`, taşma yok |
| Kapak A | `kapak-a.png` = `kapak.png` (md5 `4329647639d4`), `k/ka-acik/at-1.97s.png` | `k/koyu/kapak-a-koyu.png` | altyazısız, kanal katmanı var |
| 02 değer | `k/02-…-3.05 · 8.4 · 9.86 · 11.5 · 13.86 · 15 · 17.86 · 19.9.png` | `k/koyu/…-11.5 · 15.png` | 8,4 sn: çip 1 ile sönen satırlar ayrık; 11,5 sn çip 2 kart 2 yuvasında bekler (tasarım; kapı 0) |
| 08 kaydet | `k/08-…-20.05 · 21.2 · 22.75 · 23.4 · 25.4.png` | `k/koyu/…-25.4.png` | 3 satır kart, yer imi, `Kaydet` |
| 03 çağrı | `k/03-…-25.55 · 28.6 · 31.7.png` | `k/koyu/…-31.7.png` | ana kapak kartı + künye aynı rozet |
| Kapak B / C | `kapak-b.png` (`cb0daa28ab77`), `kapak-c.png` (`ac37e83abb69`) | `sahneler/05|06-…/k/koyu/kapak-b|c-koyu.png` | yalnız rozet değişti |
| Hikâye A / B | `hikaye-a.png`, `hikaye-b.png` | `k/koyu/hikaye-a|b-koyu.png` | 3 satır özet; 1150–1380 boş |

Kontak sayfaları: `kontak/DUZ2-duragan.png`, `kontak/DUZ2-video-1.png`, `kontak/DUZ2-video-2.png`, `kontak/DUZ2-koyu.png`.
Her karede: 0–280 ve 1570–1920 boş, kanal katmanı y 291–339, okunmayan yazı yok, emoji yok.

HV-13 (kart 2 sn sabit, kart dikdörtgeni x 61–959, y 601–979): 22,75 ↔ 25,4 sn ve 23,4 ↔ 25,4 sn → 10 piksel, en büyük fark 1/255
(işleme gürültüsü; eşik 1 ile 0 px). Kol b aynı karelerde 0 px.

Çakışma kapısı (`kapi-cikti-DUZ2.txt`, JSON `cakisma-DUZ2.json`, `cakisma-DUZ2-duragan.json`):

```
$ node araclar/cakisma-kapisi.mjs 02-04-ydt-temel-s1 --port 41333 --sunucu 41022 --json …/cakisma-DUZ2.json
01-hyperframes-kapak | çakışma yok (13 örnek, 3528 kutu)
02-paperjs-ornek | çakışma yok (69 örnek, 3180 kutu)
08-hyperframes-kaydet | çakışma yok (23 örnek, 2800 kutu)
03-hyperframes-cta | çakışma yok (26 örnek, 3880 kutu)
çıkış kodu: 0
$ KALEM_KOK=~/Silinecekler/2026-11-15-duz2-0204S1/kapi-kok SAHNE_KARE_BETIK=$PWD/araclar/sahne-kare.mjs \
  node araclar/cakisma-kapisi.mjs 02-04-ydt-temel-s1 --port 41333 --sunucu 41022 --json …/cakisma-DUZ2-duragan.json
04-hyperframes-hikaye | çakışma yok (3 örnek, 564 kutu) · 05-hyperframes-kapak-b | çakışma yok (3 örnek, 468 kutu)
06-hyperframes-kapak-c | çakışma yok (3 örnek, 1044 kutu) · 07-hyperframes-hikaye-b | çakışma yok (3 örnek, 336 kutu)
çıkış kodu: 0
```

Geçici kök: gerçek `zaman.json` kopyası, `sahneler[]` = 4 durağan sahne (HyperFrames, t 0–0,5), `sahneler` simge bağı (DUZ-1 yöntemi).
Kapı `K/_is/cakisma/ham_png` geçici deposuna yazar (git dışı, araç davranışı).

## 4. Diff sınıflaması (kol a ↔ kol b)

Tam tablo kol b raporunda (§4) ve `../../02-04-ydt-temel-s1b/uretim-tutanagi/diff-siniflama-DUZ2.txt`. Beklenmeyen satır: 0.

## 5. Düzeltilmeyen maddeler

| Madde | Sınıf | Sebep |
|---|---|---|
| KS-4 → HV-20b (kapak B "YAŞIYORUM NASIL DENİR?" ↔ başlık B) | B4 | ölçüt kararı (şef); §4.2 T1 satırında yok. Birebir yineleme değil. |
| KS-3, KS-1/2 düzen | B3 | ölçüt hatası (KS-1…3 ana ders kapağı içindir; kısa için HV-20a) |
| HV-19 | B2 | ölçüt hatası (yayın bağları büyük harf); s2 bu paketin dışı |
| KS-6 168 px dosyası | C3 | kanıt maddesi, istem kapsamı dışı (A sınıfı değil) |
| EK-5c "Hep orada" (KBJ, kol b) | — | gerçek hata saymadım: kural cümlesi değil, `I live in Istanbul` örneğinin durumunu anlatır ("Şimdilik" karşıtı). J2-OZET T1 EK-5c = G. Değiştirmek iki kolda değer sesini değiştirir (AB-3). Şef kararı. |
| Kanca cümlesi 6,44 sn (> 4) | — | ses değişmedi; istem kanca sesini değiştirmiyor |
| `meta.amaclar` "planlanmış gelecek" genellemesi | ana ders A3 | şef kararı bekliyor (J2-OZET §3A ana ders satırı); kısa ekranında ve seste yok |
| `sahneler/*/RAPOR.md` içindeki eski `YDT · BASIC` anlatımı | — | geçmiş üretim kaydı; çıktı dosyası değil. Bu rapor günceli yazar. |
| Süre hedefi 22–26 sn | — | ses yeniden yazılmadı (D-0279) |

## 6. Değiştirilen dosyalar

Git'te izlenen: `BRIEF-S1.md`, `ortak/anlatim/senaryo.json`, `ortak/kunye.js`, `surumler.json` (`revizyonlar` r1),
`sahneler/01-hyperframes-kapak/{yardim.py,SPEC.md,proje/index.html,proje-ka/index.html}`, `sahneler/02-paperjs-ornek/{kalem-paper.js,sahne-02.js,SPEC.md}`,
`sahneler/03-hyperframes-cta/{yardim.py,SPEC.md,proje/index.html}`, `sahneler/04-hyperframes-hikaye/{uret.py,yardim.py,SPEC.md,nesneler.json,proje/index.html}`,
`sahneler/05-hyperframes-kapak-b/{yardim.py,SPEC.md,RAPOR.md (Tema satırı),nesneler.json,proje/index.html}`, `sahneler/06-hyperframes-kapak-c/` (aynı 5),
`sahneler/07-hyperframes-hikaye-b/{uret.py,yardim.py,SPEC.md,nesneler.json,proje/index.html}`, `sahneler/08-hyperframes-kaydet/{uret.py,yardim.py,SPEC.md,proje/index.html}`,
yeni: `uretim-tutanagi/{DUZ2-RAPOR.md,kapi-cikti-DUZ2.txt,cakisma-DUZ2.json,cakisma-DUZ2-duragan.json,kontak/DUZ2-*.png}`.
Git dışı: kök PNG'ler (kapak, hikâye), `sahneler/*/k/` kareleri.
