# 02-04-ydt-temel-s1 · hikâye karesi taslağı (1080×1920)

Durum: TASLAK (istem S1-A, 15.11.2026). Görsel üretim ve render YOK.
Biçim: durağan PNG birincil (`hikaye.png`). En çok 15 sn MP4 isteğe bağlı (§4).
Kaynak: huni-plan §2 (veri: `senaryo.json` → `meta.kapak.satir1`, `satir2`, `meta.canAlici`), §5 (platform), §7 (dil).

## 1. Platform

| Platform | Hikâye | Bağlantı | Kaynak |
|---|---|---|---|
| Instagram | API ile (`media_type=STORIES`) ya da elle | API ile yok. Elle paylaşımda bağlantı çıkartması eklenebilir (doğrulanmadı, uygulama özelliği) | huni-plan §5 [2] |
| TikTok | yalnız mobil uygulama, elle | açıklamada tıklanmaz | huni-plan §5 [4] |
| YouTube | yok (özellik kapandı) | — | huni-plan §5 |

## 2. Dil kararı (huni-plan §7)

**Seçim:** metin öğretmene ve YDT öğrencisine birlikte seslenir. Veli dili bu pakette kullanılmaz.

| Gerekçe | Kanıt |
|---|---|
| YDT kitlesi 17–18 yaş, 15 yaş yasağının dışında; sosyal ağı doğrudan kullanır | huni-plan §7 "Kitle Etkisi" |
| §7 veli/öğretmen önerisinin kaynağı 9. sınıf (14 yaş) Maarif kitlesidir | huni-plan §7 + karar sorusu 3 ("14 yaşındaki 9. sınıf kitlesi") |
| Kare sen/siz hitabı taşımaz; öğrenci okur, öğretmen sınıfa iletir. Öğretmen satırı tek ve kısa | §3 alt satır |
| §7 kararı Kovan sicilinde yok (D-… kaydı bulunmadı); seçim geri alınır, yalnız metin değişir | `kovan-defteri/kararlar.jsonl` taraması |

Veli satırı gerekirse (Maarif 9–10 paketleri): `Çocuğunuzun İngilizce temelini güçlendirin` (huni-plan §7 örneği).

## 3. Kare içeriği

| Bant (y px) | Öğe | Metin | Biçim |
|---|---|---|---|
| 0–288 HUD | rozet + ders adı | `YDT · BASIC` · `Simple Present vs Present Continuous` | rozet 36 px, ders adı 56 px, 2 satır (dikey v2) |
| 300–420 | üst satır | `Türkçede tek sözcük` | Lexend 64, mürekkep |
| 440–700 | can alıcı | `YAŞI-YOR-UM` | Fredoka, `YOR` sarı kutuda (`ek_ayir` görünümü), 952 px'e sığan en büyük boy |
| 720–1180 | can alıcı kartları | kart 1 `I live` · `PERMANENT` · ev ikonu + uzun bant <br> kart 2 `I am living` · `TEMPORARY` · bavul ikonu + kısa bant | Fredoka 72 kart; etiket Caveat 64; Shorts sahne 02 görseliyle aynı |
| 1190–1300 | alt satır | `İngilizcede iki zaman` | Lexend 64, mürekkep |
| 1344–1536 | "tam ders" çağrısı | `Tam ders: profildeki bağlantı` (2 satır: `Tam ders:` / `profildeki bağlantı`) · `@ydspublishing` | `Tam ders:` Caveat 72; `@ydspublishing` sarı hap; logo sol alt y ≈ 1478 |
| 1536–1920 | boş | — | platform arayüzü; Instagram'da elle bağlantı çıkartması bu bandın üst kısmına (öneri) |

- Satır uzunluğu en çok 24 karakter (kalıp §3): en uzun satır `İngilizcede iki zaman` = 21.
- Öğretmen satırı (Instagram açıklamasında, karede değil): `Öğretmenseniz sınıfınızla paylaşın.` Gerekçe: karede 3 metin satırı + çağrı yeter.
- Süre karede yazmaz: kare durağan ve kalıcıdır, süre açıklamada ölçülmüş değerle yazılır (`aciklama-taslak.md`).

## 4. İsteğe bağlı MP4 (en çok 15 sn)

| sn | Hareket |
|---|---|
| 0,0–1,5 | `Türkçede tek sözcük` + `YAŞI-YOR-UM` kalemle; `YOR` sarı kutu kayar |
| 1,5–6,0 | kart 1 ve kart 2 kalemle; bantlar çizilir |
| 6,0–8,0 | `İngilizcede iki zaman` + çağrı satırı |
| 8,0–12,0 | durgun (okuma süresi) |

Ses yok (hikâye çoğunlukla sessiz izlenir; kalıp §1 kural 3). Önerim: önce yalnız PNG; MP4 Nadir isterse.

## 5. UTM (yalnız bağlantı çıkartması için, elle Instagram paylaşımı)

`https://ydspublishing.com/grammar/02-04-ydt-temel?utm_source=instagram&utm_medium=story&utm_campaign=ing-ydt-gr-02-04-t&utm_content=s1`

Adres kaynağı ve durum: `aciklama-taslak.md` §1.

## 6. Sürüm B — soru kartı (istem S1-VAR, 15.11.2026)

Çıktı `hikaye-b.png` (paket kökü), sahne `sahneler/07-hyperframes-hikaye-b/` (durağan kare, zaman çizelgesi dışı).
Fikir: A kuralı gösterir; B soruyu sorar, iki seçenek verir, cevabı vermez. Cevap tam derste.
Dil kararı §2 ile aynı (öğretmen + YDT öğrencisi; sen/siz hitabı yok).

| Bant (y px) | Öğe | Metin | Biçim |
|---|---|---|---|
| 0–288 HUD | logo, ders adı, rozet, çip | A ile aynı; çip `Quiz` (`kunye.js` `cipler`'de 07 satırı yok; sahne sabiti) | dikey v2 |
| 352–570 | Türkçe cümle | `Şimdilik amcamla` / `yaşıyorum.` | Fredoka 700 88, 2 satır, mürekkep |
| 596–680 | soru | `Hangisi doğru?` | sarı hap (dolgu `vurguDolgu`, yazı `pilMetin`), Fredoka 700 64 — **tek vurgu** |
| 716–976 | seçenek kartı A | daire içinde `A` · `I live` / `with my uncle.` | çerçeve mürekkep 4 px, Fredoka 700 72 |
| 1008–1268 | seçenek kartı B | daire içinde `B` · `I am living` / `with my uncle.` | kart A ile birebir aynı biçim |
| 1344–1536 | çağrı | `Cevap tam derste:` / `profildeki bağlantı` · `@ydspublishing` hapı | Caveat 72 · hap sağa hizalı (A ile aynı) |
| 1536–1920 | boş | — | platform arayüzü |

- Cevap yok: tik, çarpı, renk farkı, altçizgi yok. İki kart aynı çerçeve, aynı boy, aynı renk.
- İpucu cümlenin kendisinde: `Şimdilik` → geçici durum → doğru cevap B (`I am living`). Karede ve açıklamada yazılmaz.
- Kaynak: örnek ana derste var — `02-04-ydt-temel/ortak/anlatim/senaryo.json`: "My parents are out of town, so I am living with
  my uncle. … amcamla yaşıyorum. Bu yalnız şimdilik. Geçici durum: şimdiki zaman." "Cevap tam derste" iddiası buna dayanır.
- Satır uzunluğu en çok 24: en uzun `Şimdilik amcamla` = 16, `Cevap tam derste:` = 17, `with my uncle.` = 14.
- Instagram'da elle paylaşımda "test" çıkartması eklenebilir (uygulama özelliği, doğrulanmadı); kare çıkartmasız da çalışır.
- UTM (bağlantı çıkartması, elle): set değeri — `aciklama-b.md` `…&utm_medium=story&…&utm_content=s1-b`; `aciklama-a.md` `s1-a`.
  Bu belgenin §5 satırı `utm_content=s1` olarak kaldı (var olan metin değişmedi).

| | A (`hikaye-a.png`) | B (`hikaye-b.png`) |
|---|---|---|
| Kip | kural kartı | soru kartı |
| Üst | `Türkçede tek sözcük` + `YAŞI-YOR-UM` | `Şimdilik amcamla` / `yaşıyorum.` |
| Orta | iki kart: `I live` PERMANENT · `I am living` TEMPORARY (zaman bantlı) | iki seçenek: A `I live …` · B `I am living …` (bantsız, etiketsiz) |
| Çağrı | `Tam ders:` / `profildeki bağlantı` | `Cevap tam derste:` / `profildeki bağlantı` |
| Tek vurgu | `YOR` kutusu | `Hangisi doğru?` hapı |
