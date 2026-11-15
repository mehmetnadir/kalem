# simple-past-ileri · huni v2 konu seçimi (6 aday, ilk 3 üretilecek)

Durum: TASLAK (istem HK-0210I, 15.11.2026). Senaryo, ses, sahne kodu ve render YOK.
Bağlayıcı standart: `dijital-anlatim/.claude/docs/huni-v2-standart.md` §5 (altı ölçüt, biçim tablosu), §9 (pilot).
Ana ders: `../ortak/anlatim/METIN.md` (7 cümle; cümle numaraları bu dosyadan), `../surumler.json` (`amaclar`, `canAlici`), `../BRIEF.md`.
Ana dersin kapak metni: `USED TO mu` / `WOULD mu?` / `durum: yalnız used to` (`KAPAK-RAPOR.md`). Hiçbir aday bu metni aynen yinelemez.
Emsal: 02-02 temel S1 köprü · S2 sinyal sözcük · S3 yanlış–doğru (`../../simple-present-temel-s2/uretim-tutanagi/senaryo-taslak.md`).

Ölçüt kısaltması yok; sütun başlıkları: Sınav = sınavda çıkar mı · Yanılır = öğrenci en çok burada mı yanılır · Tek = kural tek cümleye
sığar mı · Köprü = Türkçe köprüyle gösterilir mi · İzlemeden = dersi izlemeden anlaşılır mı · Bakılır = sınav günü yeniden bakılır mı.

## 1. Adaylar (değer sırası)

| Sıra | Biçim | Taşıdığı bilgi | Kural özeti kartı | Kanca (ilk 1 sn) | Örnek EN · TR | Ana ders kaynağı |
|---|---|---|---|---|---|---|
| 1 (s1) | yanlış–doğru | `ago` belirli zaman bildirir; Present Perfect'i engeller, fiil Simple Past olur. | Ago varsa Present Perfect değil, Simple Past. | Yanlış cümle (ekranda kırmızı): `The manager has resigned two weeks ago.` Doğru mu? | `The manager resigned two weeks ago.` · `Müdür iki hafta önce istifa etti.` | cümle 5 (örnek), 6 (öğrenci tam bu yanlışı soruyor), 7 (`A definite time word blocks the present perfect.`), 1 (`Ago varsa Perfect yok.`) |
| 2 (s2) | köprü cümle | Türkçe `-erdi` iki karşılık alır: durum fiilinde (yaşardık) yalnız `used to`, tekrarlanan eylemde (giderdik) `used to` ya da `would`. | Yaşardık used to olur; giderdik would da olur. | `Yaşardık: would live olur mu?` | `We used to live in a village, and we would walk to school every morning.` · `Köyde yaşardık, her sabah okula yürüyerek giderdik.` | cümle 4 (bütün parçalar: `would walk doğru, would live yanlış`) |
| 3 (s3) | sinyal sözcük | `yet` (henüz) Present Perfect ister; Türkçe `bulamadı` geçmiş ekli olsa da İngilizcesi `has not found … yet` olur. | Yet görürsen Simple Past değil, Present Perfect. | `Yet görünce hangi zaman?` | `The board has not found a replacement yet.` · `Yönetim kurulu henüz yerine birini bulamadı.` | cümle 5 (`Has not found: yet var, zaman belirsiz, Present Perfect.`), 7 (`Present Perfect for, since, yet ister.`) |
| 4 (s4) | mini test | Durum fiili (`live`) `would` almaz; belirli geçmiş (`when we were kids`) Present Perfect'i de engeller; cevap `used to live`. | Live gibi durum fiilinde would değil, used to. | Boşluklu cümle ekranda: `When we were kids, we ___ in a village.` Boşluğa ne gelir? Şıklar: a) would live b) used to live c) have lived | `When we were kids, we used to live in a village.` · `Çocukken köyde yaşardık.` | cümle 4 (`would live yanlış`), 7 (belirli zaman); `When we were kids` ana derste yok: soru kökü için bağlam |
| 5 (s5) | kural kartı | `last year`, `in 1911`, `ago` gibi belirli zaman sözcükleri Simple Past ister. | Last year, in 1911 gibi belirli zaman: Simple Past. | `In 1911: has won mı, won mı?` | `Marie Curie won her second Nobel Prize in 1911.` · `Marie Curie ikinci Nobel Ödülü'nü 1911'de kazandı.` | cümle 3 (`In 1911 belirli zaman, yani Simple Past.`), 7 (`Ago, last year, in 1911: belirli zaman.`) |
| 6 (s6) | tuzak | Simple Past fiilin ikinci hâlidir (`began`); üçüncü hâl (`begun`) yardımcı fiil (has/had) olmadan yüklem olmaz. İşaret: has/had yok → ikinci hâl. | Simple Past ikinci hâldir: began; begun yardımcısız olmaz. | `Began mı, begun mu?` | `… three years before the war began.` · `… savaş başlamadan üç yıl önce.` | cümle 3 (`Tuzak: begin, began, begun. Burada begun yanlış.`) |

| Sıra | Sınav | Yanılır | Tek | Köprü | İzlemeden | Bakılır | Evet | Sınavdaki değeri (kanıt) |
|---|---|---|---|---|---|---|---|---|
| 1 | evet | evet | evet | evet | evet | evet | 6 | YDT dilbilgisi boşluk doldurma: `two weeks ago` / `last year` + şıklarda `has resigned` · `resigned`; ders bu tuzağı "asıl tuzak" diye anlatır (cümle 5–7), `canAlici[0]`. |
| 2 | evet | evet | evet | evet | evet | evet | 6 | YDT geçmiş alışkanlık sorusu (`used to` / `would` şıkları); `amaclar[1]`, `canAlici[2]`; ders kök 2 (cümle 4). |
| 3 | evet | evet | evet | evet | evet | evet | 6 | YDT zaman seçimi: `yet` / `since` cümlesinde Present Perfect şıkkı; ders kök 3 ikinci yarısı (cümle 5), `canAlici[4]`. |
| 4 | evet | evet | evet | evet | evet | evet | 6 | YDT soru tipinin kendisi (boşluk + 3 şık); iki çeldirici dersin iki kuralından gelir (cümle 4 ve 7). |
| 5 | evet | hayır | evet | hayır | evet | evet | 4 | YDT tarihli cümlede zaman seçimi; `canAlici[1]`; ders kök 1 (cümle 3) ve kod kartı (cümle 7). |
| 6 | hayır | evet | evet | hayır | evet | evet | 4 | Dolaylı: YDT şıkları dilbilgiseldir, çıplak `begun` şık olmaz; değer şıklardaki `began` · `had begun` · `has begun` ayrımını tanımakta; `amaclar[2]`, `canAlici[3]`, cümle 3. |

Sıra yalnız "evet" sayısından gelmez. Ölçüt: sınavda görülme sıklığı + öğrencinin yanılma payı + öteki adaylardan farklı bilgi.
Aday 4 altı "evet" alır, ama aday 2 ile aynı kuralı sınar; bu yüzden 4. sırada.

## 2. Kısa açıklamalar

1. **s1 · yanlış–doğru (ago).** Dersin çekirdeği. Öğrenci sorusu (cümle 6) bu yanlışın kendisidir; kısa onu kancaya taşır.
   Türkçe köprü: `iki hafta önce` = `ago`; Türkçe `istifa etti` iki İngilizce biçime çevrilebilir, `önce` sözcüğü Simple Past'i seçer.
   Eski kısa (`simple-past-ileri-s1`, "AGO = PAST") aynı konuyu taşır: bkz. §3.
2. **s2 · köprü cümle (-erdi).** Ana kapağın sorusunu kısaca cevaplar; çağrı sahnesindeki kapak (`USED TO mu WOULD mu?`) kısayla
   aynı konudadır, huni bağı güçlüdür. Türkçe `-erdi` hiç ayrım yapmaz; öğrenci her `-erdi`ye `would` yazar. Kart metni kapak satırını
   yinelemez (`durum: yalnız used to` yok).
3. **s3 · sinyal sözcük (yet).** s1'in karşı yüzü: aynı Türkçe geçmiş eki (`bulamadı`) bu kez Present Perfect olur, çünkü `yet` var.
   Kart yalnız `yet` taşır; `for` ve `since` bilerek dışarıda (jüri notu).
4. **s4 · mini test.** s2 kuralını sınav biçiminde yineler; `have lived` çeldiricisi s1 ailesinden (belirli geçmiş). 3 sn sayaç, cevap b.
5. **s5 · kural kartı.** s1'i tek sözcükten sınıfa genişletir (`last year`, `in 1911`). Ders kanıtı yalnız `ago` hatasını gösterir;
   bu yüzden "Yanılır" hayır.
6. **s6 · tuzak (began/begun).** Ders bu noktayı kendisi "Tuzak" diye adlandırır. YDT şıkları dilbilgisel olduğu için sınav değeri dolaylı.

## 3. Eski kısa

`simple-past-ileri-s1` (BRIEF-S1, METIN): konu `ago → Simple Past`, örnek `The manager resigned two weeks ago.`, biçim sinyal sözcük
(kural + örnek). Ölçütleri 6/6 geçer → **listede, 1. sırada**. v2'de biçim yanlış–doğru olur (sinyal sözcük biçimi s3'te).
Eski kısanın v2'ye aykırı yerleri: `Tam ders` sözü, `6 dakika` süre sözü, 3 sahneli yapı, kaydet sahnesi yok (standart §1 kural 4–6).
Örnek cümle ve Türkçesi s1'in doğru biçimi olarak kalabilir.

## 4. Elenen adaylar

| Aday | Kaynak | Evet | Neden girmedi |
|---|---|---|---|
| `did` + yalın fiil (`Did not resign.`) | cümle 7 | 3 | Sınav hayır (YDT şıkları dilbilgisel), köprü hayır, sınav günü bakılmaz; 02-02 S3 ile aynı kural (yardımcı fiil + yalın fiil). |
| Simple Past tanımı (`A finished action at a definite time in the past.`) | cümle 2 | 4 | Ölçütü geçer, ama s1 ve s5 ile aynı bilgi; yedek aday. |

## 5. Jüri bakacak

- s2: `would live` koşul anlamında doğrudur (`we would live in a village if …`); kısa "geçmiş alışkanlık" çerçevesinde kalmalı.
  Türkçe `okula yürüyerek giderdik` doğallığı (ana derste Türkçe çeviri yok).
- s3: Amerikan İngilizcesinde konuşmada `yet` + Simple Past geçer (`Did you find one yet?`); ders ve YDT İngiliz kullanımına göre.
  `for` kartta yok: Simple Past ile de gelir (`He worked there for ten years.`). `since` yan cümlesi Simple Past alır
  (`since the manager resigned`); kartta yok.
- s4: `When we were kids` bağlamı ana derste yok.
- s5: `in 1911` bitmiş yıl; bitmemiş zaman (`this year`) kapsam dışı.

## 6. Kardeş ders taraması (sözleşme: kardeş derslerin kısa konuları taranır)

Kardeş derslerin `huni-konu.json` dosyaları da 15.11 taslağıdır; yayında kısa yok, bu yüzden aday elenmedi. Örtüşme şefin kararına kalır:

| Bu ders | Kardeş ders adayı | Örtüşme |
|---|---|---|
| s1 (ago → Present Perfect değil) | simple-past-temel s3 `Yesterday, ago, last year görürsen: Simple Past.` · present-perfect-ileri s1 `Ago'lu cümlecik Simple Past, yet'li cümlecik Present Perfect.` | aynı kural; s1 eski kısanın (05.11) konusu, öncelik bu derste |
| s3 (yet → Present Perfect) | present-perfect-ileri s1 | aynı cümle tipi (ago + yet); present-perfect-ileri s1 seçilirse s3 yerine s4 öne çıkar |
| s5 (last year, in 1911) | simple-past-temel s3 | aynı sinyal listesi; s5 zaten yayma sırasında |

s2 (`used to` / `would`), s4 ve s6 kardeş derslerde yok.

---
Son Güncelleme: 15.11.2026 — ilk sürüm (istem HK-0210I).
