# 02-04-ydt-temel-s1b · kol b senaryo taslağı (A/B deneme kolu, değişken `kanca`)

Durum: TASLAK (istem BK-0204S1, 15.11.2026). Ses sentezi, sahne kodu, render YOK.
Bağlayıcı: `D/.claude/docs/huni-ab-sozlesme.md` (v1, §2–§4) · `D/.claude/docs/huni-v2-standart.md` (§1–§7).
Kol a: `../../02-04-ydt-temel-s1/` (ölçülmüş süre 31,75 sn, `anlatim.m4a` ffprobe; `zaman.json`).

## 1. Künye

| Alan | Değer |
|---|---|
| Paket | `02-04-ydt-temel-s1b` · sürüm kimliği `s1b` · `utm_content` = `s1b-<açıklama seti>` (sözleşme §4) |
| Varyant | `{"grup": "s1", "kol": "b", "degisken": "kanca", "deger": "soru"}` |
| Kol a değeri | `kopru`: cümle 1 Türkçe söz ("İstanbul'da yaşıyorum. Amcamla yaşıyorum. Türkçede ikisi de yaşıyorum.") + kapakta İngilizce karşılık (`I live` / `I am living`). Standart §5 "Köprü cümle: bir Türkçe söz → iki İngilizce karşılık" |
| Kol b değeri | `soru`: tek soru cümlesi. İngilizce karşılık kancada YOK; cevabı değer sahnesi verir |
| Neden `soru` | Değer sahnesinin ilk sözü "İngilizcede ikisi ayrılır." soruya doğrudan cevaptır; değer sahnesinin cümlesi değişmez. `yanlis-cumle` için konuya bağlı "gerçekten yanlış" cümle değer sahnesinin ilk cümlesini ve ekranını değiştirirdi (BK-RAPOR §e) |
| Ses kadrosu | kol a ile aynı: öğretmen `gsJ9nrlXYbPztJxC4fwc` (kanca, değer, kaydet) · öğrenci `oPC5I9GKjMReiaM29gjY` (çağrı) |
| Kanal katmanı, künye, rozet | kol a ile aynı (`../../02-04-ydt-temel-s1/BRIEF-S1.md` "Kanal katmanı" tablosu, künye satırı) |

## 2. Senaryo

**TR** / **EN** = ses parçasının dili. Kalın = kol b'de değişen. Zamanlar küresel sn; kol b zamanı tahmindir (§4).

| Sahne | Konuşan | Ses metni | Ekran metni | Görsel fikir |
|---|---|---|---|---|
| **1 Kanca · `01-hyperframes-kapak` · 0,00–2,40** | **öğretmen** | **TR "Bu iki yaşıyorum aynı mı?"** · **ilk söz 0,50** · **YENİ CÜMLE — jüri bakacak** | **0,00: başlık `YAŞIYORUM` / `AYNI MI?` (sarı hap) · rozet `YDT · BASIC`** · **0,50 (`Bu`): `İstanbul'da yaşı-yor-um.`** · **≈ 0,72 (`iki`): `Amcamla yaşı-yor-um.`** · **altyazı `Bu iki yaşıyorum aynı mı?`** · **İngilizce yazı YOK** (`I live` / `I am living` etiketleri kalkar) | **Kol a kapak sahnesi (ev, elinde bavul tutan öğretmen figürü) küçük boyla kalır; iki Türkçe satır `Bu` ve `iki` çapasında gelir; `yaşıyorum` çapasında iki satırda `yor` sarı kutuya geçer (ek_ayir); `aynı mı?` sırasında başlık solar, konu adı açılır, satırlar sahne 02 konumuna kayar. Ayrıntı §3** |
| 2 Değer · `02-paperjs-ornek` · 2,40–16,03 | öğretmen | kol a ile aynı: **TR** "İngilizcede ikisi ayrılır." · **EN** "I live in Istanbul." · **TR** "Hep orada: kalıcı durum, geniş zaman." · **EN** "I am living with my uncle." · **TR** "Şimdilik: geçici durum, şimdiki zaman." | kol a ile aynı: Kart 1 `I live in İstanbul.` · soluk TR `Hep orada.` · `PERMANENT` · Kart 2 `I am living` / `with my uncle.` · soluk TR `Şimdilik.` · `TEMPORARY` | kol a ile aynı: "ayrılır" çapasında TR satırlar solar, iki `yor` kutusu kartlara kayar; kart 1 + ev, kart 2 + bavul; `odak` *live* / *am living*; uzun bant / kısa bant zaman çizgisi. **Baş kırpımı: kol a sahne 02'nin 3,00–6,36 parçası (cümle 1 kuyruğu: karaoke `yaşı-yor-um.`, ek_ayir, `Türkçede` çapası) kol b'de YOK. Bu parça kancanın sözüdür; kancayla değişir. Kol b sahne 02 = kol a sahne 02 yerel kare 101'den (küresel 6,36) sona** |
| 3 Kaydet · `08-hyperframes-kaydet` · 16,03–21,53 | öğretmen | kol a ile aynı: **TR** "Bu, üç farktan yalnız biri." · **TR** "Sınavdan önce lazım olacak. Kaydet." | kol a ile aynı: `üç farktan biri` · kart `Kalıcıysa geniş zaman,` / `geçiciyse şimdiki zaman.` · yer imi simgesi + `Kaydet` sarı hap | kol a ile aynı: kart `Bu,` çapasında girer (0,45 sn), sahne sonuna kadar sabit; `Kaydet.` çapasında yer imi kalemle çizilir, hap gelir |
| 4 Çağrı · `03-hyperframes-cta` · 21,53–27,79 | öğrenci | kol a ile aynı: **TR** "Gerisi bizde." · **TR** "Dersin tamamı YDS Publishing YouTube kanalında." | kol a ile aynı: ana dersin kapağı 16:9 kart (900×506) · `Gerisi bizde.` · `@ydspublishing · YouTube` | kol a ile aynı: kart sahne başında oturur, `Gerisi` kinetik, hap ve `YouTube` sözcük çapasında; son söz + 1,0 sn durgun kuyruk |

## 3. Kanca ayrıntısı (sahne 01, kol b)

Zaman sözcük çapasından okunur (kol b `ortak/anlatim/sozcukler.json`, sentez sonrası); aşağıdaki sn tahmindir.

| # | Olay | sn | Çapa |
|---|---|---|---|
| 1 | Kapak tabanı: kanal katmanı · rozet `YDT · BASIC` x 60 · başlık `YAŞIYORUM` (kol a ölçüsü, B ≈ 152) / `AYNI MI?` sarı hap (dolgu `#ffe066`, yazı `#1b2440`) · ev (sol) + elinde bavul tutan öğretmen figürü, figür yüksekliği ≈ 280 (kol a 400; satır 2 ile çakışmasın) · yer çizgisi 1372. Cümle satırı ve İngilizce etiket yok | 0,00 | söz öncesi |
| 2 | `YOR` altına sarı el altçizgisi (kol a ile aynı darbe) | 0,30–0,80 | söz öncesi |
| 3 | Altyazı dilimi açılır | 0,45 | `Bu` − 0,05 |
| 4 | Satır 1 `İstanbul'da yaşı-yor-um.` kırpmayla (Caveat 700 80, x 84, taban 920 = kol a R1_K) | 0,50–0,80 | `Bu` |
| 5 | Satır 2 `Amcamla yaşı-yor-um.` kırpmayla (taban 1040 = kol a R2_K) | ≈ 0,72–1,02 | `iki` |
| 6 | ek_ayir: iki satırda `yor` sarı kutuda (kol a sahne 02 olay 3–4 görünümü, aynı kutu ölçüsü) | ≈ 1,04–1,40 | `yaşıyorum` |
| 7 | KAPAK KARESİ: kol b A kapağı (`kapak-taslak.md`) | ≈ 1,75 | `aynı` öncesi |
| 8 | Başlık 2 satır solar (uçuş yok: `AYNI MI?` konu adının bir parçası değil) · konu adı açılır (`kunye_ac`) · rozet x 60 → rz_x · ev ve figür solar · iki satır `yor` kutularıyla DY = −360 kayar (920 → 560, 1040 → 680) | ≈ 1,80–2,35 | `aynı mı?` |
| 9 | Son hâl = kol a sahne 02 yerel kare 101 hâli: kanal + künye + iki satır (x 84, taban 560 / 680) + `yor` kutuları (x ≈ 551–636 / 482–567). Son 12 kare geçiş altında | 2,35–2,40 | → sahne 02 |

- İkinci satırın sözcükleri seslendirilmez; iki satır sorunun gösterdiği nesnedir ("bu iki"). Satırlar gösteren sözcüğün çapasında gelir, önce gelmez.
- Başlık 0. karede görünür (kapak karesi kuralı). Kol a'da da `YAŞIYORUM` 0. karede, söz 1,64'te gelir. Jüri bakacak (BK-RAPOR §e madde 4).
- Kapak karesinde 4 yazı satırı var (başlık 2 + cümle 2). Kol a uçuş anında da 4 satır taşır. Klişe 16 "≤ 3 satır": jüri bakacak.

## 4. Süre

Hız ölçüsü (kol a öğretmen, `sureler.json`): "Amcamla yaşıyorum." 7 hece 1,20 sn (5,8 hece/sn) · "İngilizcede ikisi ayrılır." 11 hece 1,92 sn
(5,7 hece/sn). "Bu iki yaşıyorum aynı mı?" 10 hece → 1,75 sn + soru tonu payı 0,15 = **≈ 1,90 sn** (tahmin).

| Parça | Kol a (ölçülmüş) | Kol b (tahmin) | Fark (sn) |
|---|---|---|---|
| İlk söz | 1,00 | 0,50 | −0,50 |
| Kanca sözü | 1,00–6,36 (5,36; 8 sözcük) | 0,50–2,40 (1,90; 5 sözcük) | −3,46 |
| Kanca sonu → cümle 2 | 0,55 | 0,55 | 0 |
| Cümle 2 başı | 6,91 | 2,95 | −3,96 |
| Sahne 01 | 0,00–3,00 (3,00; 102 kare) | 0,00–2,40 (2,40; 84 kare) | −0,60 |
| Sahne 02 | 3,00–19,99 (16,99; 522 kare) | 2,40–16,03 (13,63; 421 kare) | −3,36 |
| Sahne 08 | 19,99–25,49 (5,50; 177 kare) | 16,03–21,53 (5,50; 177 kare) | 0 |
| Sahne 03 | 25,49–31,75 (6,26; 218 kare) | 21,53–27,79 (6,26; 218 kare) | 0 |
| **Toplam** | **31,75** | **≈ 27,79** | **−3,96** |

- Sahne sınırı = sonraki cümle başı − 0,55 (kol a kuralı): 01 → 02 = 2,95 − 0,55 = 2,40. Kare = içerik + 12 geçiş karesi (kol a ile aynı).
- 28 sn sınırı: toplam = 25,89 + d (d = kanca sözü süresi; ilk söz 0,50; 24,84 = kol a 31,75 − 6,91). d ≤ 2,11 sn olmalı; pay 0,21 sn.
- Sentezde d > 2,11 çıkarsa sırayla: (1) ilk söz 0,40'a çekilir (d ≤ 2,21); (2) yedek kanca "Bu ikisi aynı mı?" (≈ 1,40 sn, toplam ≈ 27,29;
  jüri bakacak). Sahne 02–03'e dokunulmaz.
- Kanca sözü kol a'dan 3,96 sn kısadır. Kol b'nin bütün sonraki olayları 3,96 sn erken gelir; içerik ve aralıklar aynıdır.

## 5. Ses

- Yeniden seslendirilecek: 1 cümle (cümle 1, öğretmen, tek TR parça, 25 karakter): "Bu iki yaşıyorum aynı mı?"
- Önbellekten: cümle 2, 3, 4 (kol a `cumle-2.wav`, `cumle-3.wav`, `cumle-4.wav`; parça önbelleği, aynı ses kimliği).
- `anlatim.m4a`, `sozcukler.json`, `altyazi.json` kol b için yeniden kurulur (sentez değil; BRIEF-S1 "Ses yeniden kurulumu" zinciri).
- Okunuş: "yaşıyorum" TR parçada, IPA gerekmez. Soru tonu "mı?" ile; kulak + Whisper kapısı (el.py eşiği 0,85). Rakam ve kısaltma yok.

## 6. Paket notu (sözleşme §4)

- Kol b taşır: sahne 01 (yeni), kendi `zaman.json`, kendi `ortak/anlatim/` (cümle 1 yeni, 2–4 önbellek), `kapak-a.png` (`s1b-kapak-a`).
- Simge bağı: `08-hyperframes-kaydet`, `03-hyperframes-cta`, `ortak/` içindeki anlatım dışı klasörler.
- `02-paperjs-ornek` düz simge bağı OLAMAZ: baş kırpımı (kol a yerel kare 0–100 yok) için başlangıç karesi ayarı ya da kol b kopyası gerekir.
  Söz ve ekran cümle 2'den sona kol a ile birebir aynıdır. Karar şefte (BK-RAPOR §e madde 1).
- Hikâye kareleri, kapak B / C, açıklama setleri gruba aittir; kol b'de yinelenmez.
