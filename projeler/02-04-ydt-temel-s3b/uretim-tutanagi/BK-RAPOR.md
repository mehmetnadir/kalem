# BK-0204S3 öz denetim — 02-04-ydt-temel-s3b (kol b, değişken `kanca`) · 15.11.2026

| Ölçüm | Değer |
|---|---|
| Kol a değeri → kol b değeri | `kopru` → `yanlis-cumle` |
| Yeni kanca | ses "Hata nerede?" (öğretmen, 2 sözcük, ilk söz 0,40) + ekran `The train to İzmir` / `is leave at 7 pm today.` |
| Süre | kol a 28,31 (ölçülmüş) → kol b ≈ 29,46 (tahmin, aralık 29,26–29,66) · fark +1,15 sn · **28 sn sınırı aşılır** (§e 1) |
| Yeniden seslendirilecek | 1 cümle ("Hata nerede?", 12 karakter); kol a cümle 1–5 önbellekten |
| Değer sahnesinin ilk cümlesi | değişmedi (cümle 1 "The train to Izmir leaves at seven p.m. today. I am going to the movie theater tonight.") |
| Yazılanlar | `senaryo-taslak.md`, `kol-b.json` (`/usr/bin/python3 -I` `json.load` OK), `kapak-taslak.md`, bu rapor · `K/.claude/docs/sozlesme.md` +1 satır (kanca isteği) |

## (a) Tek değişken — satır satır fark (kol a ↔ kol b)

| # | Öğe | Kol a | Kol b | Durum |
|---|---|---|---|---|
| 1 | Kanca türü | `kopru` | `yanlis-cumle` | **değişken** |
| 2 | Kanca sözü | yok; kanca sesi = cümle 1 başı "The train to Izmir leaves at seven" | "Hata nerede?" + aynı cümle 1 başı | **değişken** |
| 3 | İlk söz | 1,00 | 0,40 | kanca içi (§e 7) |
| 4 | Sahne 01 başlık | `TARİFE` / `≠ PLAN` | `HATA` / `NEREDE?` | kanca içi |
| 5 | Sahne 01 İngilizce etiket | `leaves` / `am going` | yok | kanca içi |
| 6 | Kart satır 1 `The train to İzmir` | sözle yazılır (1,00–1,92) | yanlış kartla gelir (0,40, `Hata` çapası) | kanca içi |
| 7 | Kart satır 2 | `leaves at 7` sözle (2,20–2,92) | `is leave at 7 pm today.` (≈ 0,85) → üstü çizilir (2,79) → solar (3,05–3,30) → `leaves at 7` sözle (3,35–4,07) | kanca içi |
| 8 | `?` işareti | yok | var (≈ 1,30–2,99) | kanca içi |
| 9 | Sahne 01 görsel | tren + saat + bilet tutan figür (340) | tren + saat + işaret eden figür (≈ 250), bilet yok | kanca içi |
| 10 | Sahne 01 geçiş | başlık konu adına uçar | başlık solar, konu adı açılır; tren ve satırlar kol a gibi | kanca içi |
| 11 | Kapak karesi (A) | t 1,97: başlık + satır 1 + etiketler | t ≈ 1,75: başlık + yanlış kart + `?` | kanca içi (sözleşme §4) |
| 12 | Sahne 01 altyazısı | cümle 1 | "Hata nerede?" → cümle 1 | kanca içi |
| 13 | Sahne 01 süresi | 3,00 | ≈ 4,15 | kancanın yan etkisi (§e 5) |
| 14 | Sahne 01 son hali (devir) | kart 71,472 878×254 · satır 568 / 666 · `leaves at 7` · tren köşede · künye | aynı | aynı |
| 15 | Sahne 02 sözü (cümle 1 sonu, 2, 3) | metin | aynı metin, aynı wav | aynı |
| 16 | Sahne 02 ekranı | kart 1, zaman çizgisi, kart 2, balon, `person → plan`, `train → timetable` | aynı (küresel +1,15; yerel aynı) | aynı |
| 17 | Sahne 08 sözü | "Bu, üç farktan yalnız biri. Bir arkadaşına gönder; o da karıştırıyor." | aynı | aynı |
| 18 | Sahne 08 ekranı | kart `Tarife → leaves,` / `plan → am going.` · `Arkadaşına gönder` · `Kaydet` | aynı | aynı |
| 19 | Sahne 03 sözü (öğrenci) | "Bu sadece başlangıç. Dersin tamamı YDS Publishing YouTube kanalında." | aynı | aynı |
| 20 | Sahne 03 ekranı | ana ders kapağı · `Bu sadece başlangıç.` · `@ydspublishing` hap · `YouTube` | aynı | aynı |
| 21 | Kanal katmanı, künye, rozet | 01 SPEC §3.5 | aynı | aynı |
| 22 | Ses kadrosu | öğretmen `…4fwc`, öğrenci `…9gjY` | aynı | aynı |
| 23 | Çağrı girişi + çekirdek | "Bu sadece başlangıç." + çekirdek | aynı | aynı |
| 24 | Kaydet kalıbı | "Bir arkadaşına gönder; o da karıştırıyor." | aynı | aynı |
| 25 | Toplam süre | 28,31 | ≈ 29,46 | **kancanın yan etkisi** (§e 1, 2) |
| 26 | Kapak B / C, hikâye A / B, açıklama A / B | grup türevi | yinelenmez | aynı |

Sonuç: değişen her öğe sahne 01'dedir ve sahne 01 kol a devir hâlinde biter. Kural sağlandı. Yan etki: süre +1,15 sn, ilk söz −0,60 sn.
Sahne 02, 08, 03 klasörü simge bağı olur (S1b'deki baş kırpımı burada gerekmez; emsal `sozlesme.md` simple-present-temel-s3b satırı).

## (b) Dilbilgisi

| Metin | Dil | Karar | Not |
|---|---|---|---|
| "Hata nerede?" (ses) | TR | jüri bakacak | doğru Türkçe soru; özne ekrandaki karttır (gösterme). Altyazıda aynı |
| `HATA` / `NEREDE?` (başlık) | TR | jüri bakacak | kanca sözünün kendisi; büyük harf, İ yok |
| `The train to İzmir is leave at 7 pm today.` gerçekten yanlış mı | EN | kesin | `is` yardımcı fiili yalın fiille kurulmaz (`is leave`); İngilizcede kabul gören bir okuması yok |
| Doğrusu `The train to İzmir leaves at 7 pm today.` | EN | kesin | ana ders cümle 5, jüriden geçti (D-0204); kol a değer cümlesi |
| Düzeltmenin iki yolu (`leaves` / `is leaving`) | EN | jüri bakacak | `is leaving` de dilbilgisi olarak doğrudur (kol a jürisi, `s3.kaynak-kural.md` madde 1). Video `leaves`'i seçer ve gerekçeyi verir ("Tren tarifeye uyar: geniş zaman", ana ders cümle 7). Video `is leaving` yanlıştır demez. Öğrencinin "Neden -ing yok?" sorusu bu ikinci yolu açıkça ele alır |
| Yeni kural | — | — | yok; kaydet kartı kol a ile aynı (`Tarife → leaves,` / `plan → am going.`) |
| Yedek yanlış cümle `The train to İzmir leave at 7 pm today.` | EN | kesin yanlış · jüri bakacak | özne-fiil uyumu; düzeltme tek sözcük (`leaves`). Konu bağı zayıf (uyum 02-04'ün konusu değil); yalnız jüri `is leave`'i reddederse |

## (c) Huni v2 §5 — altı ölçüt (kol b)

| Ölçüt | Kol b | Kanıt |
|---|---|---|
| Sınavda çıkar mı | evet | ana ders amaç 3 (tarifeli ↔ planlanmış gelecek); ana ders cümle 18 "Tarife mi, plan mı?" sınav sorusu kalıbı |
| Öğrenci en çok burada mı yanılır | evet | ana ders cümle 6 (öğrenci sorusu "Neden -ing yok?") kısanın içinde; `is leave` karışımı iki zamanı karıştırmanın biçimidir (yaygınlığı ölçülmedi, varsayım) |
| Kural tek cümleye sığar mı | evet | kaydet kartı `Tarife → leaves,` / `plan → am going.` |
| Türkçe köprüyle gösterilir mi | hayır | kısada Türkçe söz → İngilizce karşılık eşlemesi yok; Türkçe açıklama (`Tren tarifeye uyar`) var |
| Dersi izlemeden anlaşılır mı | evet | yanlış, doğrusu, soru ve cevap kısanın içinde |
| Sınav günü yeniden bakılır mı | evet | kaydet sahnesi ve kural kartı aynı |

5 / 6 evet (eşik 4).

## (d) Kol b neden farklı sonuç verebilir

Kol a doğru cümleyi ve cevabı ilk saniyelerde verir (`TARİFE ≠ PLAN`, `leaves` / `am going`); kol b izleyiciye bir görev verir ("Hata nerede?")
ve cevabı ≈ 2 sn bekletir. Varsayım: hata bulma merakı ilk saniyelerde kaydırmayı azaltır; bedeli, değer 1,15 sn geç gelir.

## (e) Açık noktalar

1. **Süre 28 sn'yi aşar (≈ 29,46).** Neden: kol a'da kanca sesi değer cümlesinin başıdır (cümle 1 sahne 01'de başlar). Kol a cümle 1
   başından sona 27,31 sn (28,31 − 1,00; söz + ara + kuyruk) değişmezse ilk sesten önce 28,00 − 27,31 = 0,69 sn kalır. Sesli her kanca 28'i aşar.
   Değer cümlesini kısaltmak da yetmez: "to Izmir" çıkarılıp kanca cümle 1'in ilk parçası yapılırsa ≈ 28,44 olur ve tek değişken bozulur.
   Seçenekler:
   - [1] Olduğu gibi kabul: 29,46 (30 sınırının altında); fark +1,15 sn değişkenin parçası sayılır. S2b emsali (`02-04-ydt-temel-s2b`, +0,81). **Önerim.**
   - [2] Ekran-yalnız kanca: ses yok, cümle 1 0,40'ta başlar, yanlış kart `leaves` sözünde düzelir; ≈ 27,71, yeni ses 0. Zayıf yanı: ses iki
     kolda aynı kalır, değişken yalnız ekrana iner, soru seste sorulmaz; ses ile ekran 1,2 sn ayrışır.
2. **Süre farkı karışık değişkendir.** Kol b +1,15 sn uzun. Ortalama izlenen yüzde kendiliğinden kol a lehine kayar. Kazanan kuralında
   (sözleşme §6) önce izleyip kalma okunmalı. S1b'de fark ters yöndedir (−3,96): iki grubun sonucu birlikte okunurken süre etkisi ayrılmalı.
3. **Süre tahmindir.** Kanca sözü d ölçülmedi (aralık 1,00–1,40 → toplam 29,26–29,66). Whisper kısa sözde (2 sözcük) yanılabilir; kulak denetimi gerekir.
4. **Kol a sınıfı.** Kol a kancası üç değerden hiçbirine tam uymaz (S1b BK-RAPOR §e 7 aynı tespiti yapar): ekranda Türkçe kavram →
   İngilizce biçim, seste İngilizce örnek. `kopru` en yakını. Kol a `soru` sayılsa da kol b değeri değişmez (S1b `soru` aldı). Sınıflama şefte.
5. **Sahne 01 süresi ≈ 4,15.** Huni v2 §3 "kanca 0–4 sn" 0,15 sn aşılır; kol a `zaman_uret.py` yorumu "giriş ≤ 3 sn" (K23) de aşılır.
   Yeni kanca bölümü 0,00–2,15'tir; 2,15–4,15 kol a sahne 01'in 1,00–3,00 parçasının karşılığıdır (aynı söz, ekran kol a devrine yakınsar).
   Kol b `zaman_uret.py`'de `GIRIS_SN` sabiti yerine "cümle 2 başı + 2,00" yazılır.
6. **Ekran sözden önce mi?** Başlık `HATA` / `NEREDE?` 0. karede görünür, söz 0,40'ta gelir (kapak karesi istisnası; kol a `TARİFE ≠ PLAN`,
   S1b `AYNI MI?` emsali). Kart satırları sesle gelir. Jüri bakacak.
7. **İlk söz iki kolda farklı (1,00 → 0,40).** `sozlesme.md` simple-present-temel-s1b satırı "ilk söz zamanı iki kolda aynı tutulur" der.
   Burada aynı tutulursa toplam ≈ 30,06 olur ve 30 sınırı da aşılır. İlk söz kanca bölgesindedir; 02-04 S1b emsali 0,50. Karar şefte.
8. **Kapak karesinde 4 yazı satırı** (başlık 2 + kart 2). Klişe 16 sınırı "≤ 3 satır". Jüri bakacak.
9. **Kapak benzerliği.** Kol b A kapağı grubun kapak B'sine (`NEDEN -ING` / `YOK?`, tren + `?` + kart + trene işaret eden figür) görsel
   olarak yakındır. Kapak değişkeni sınanırken not edilmeli.
10. **Cümle numarası kayar.** Kol b `senaryo.json`'da kanca cümle 1 olur; kol a cümle 1–5 kol b'de 2–6. Değişmeyen sahneler paketi
    `Path(__file__).resolve()` ile kol a yolundan okur, çıktıları aynıdır; kol b'de yeniden koşturulmaz. Doğrulanmadı: `birlestir.py`
    bağlı sahne klasöründe kol a `proje/` çıktısını olduğu gibi alıyor mu.
11. **Kol a sürüm satırı.** Sözleşme §4 kol a satırına `varyant` (`kol: "a"`, `deger: "kopru"`) ister. Kol a paketine dokunma yasağı nedeniyle
    yazılmadı; şef yazar. Kol b `surumler.json` (`s3b`, `s3b-kapak-a`) bu istemde yazılmadı (yazma kapsamı yalnız `uretim-tutanagi/`).
