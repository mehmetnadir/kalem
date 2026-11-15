# DUZ3-0201I — `present-continuous-ileri` dersin kendi içerik düzeltmeleri (jüri c sınıfı) · 16.11.2026

> Girdi: `uretim-hatti/raporlar/YV-DUZ-1511.md` §4 (bu dersin 2 satırı) ve §3 (kapak dokunulmaz),
> `uretim-tutanagi/juri/YVJ-hukum.md` "Ana ders gözlemi" (3 satır). Makine srv21 (Linux x86_64).
> Render yok, mp4 yok, alt ajan yok. Silinen dosya yok: eski ses `~/Silinecekler/2026-11-16-duz3-0201I/` altında
> (`~/Silinecekler/LISTE.md` satırı yazıldı). Dikey paketin raporu: `../present-continuous-ileri-dikey/uretim-tutanagi/DUZ3-RAPOR.md`.
> Önceki oturum bellek arızasıyla kesildi: senaryoda c3 ve c7 metni yazılmış, c3'ün 3 parçası ve c7'nin 2 parçası sunucu
> önbelleğine sentezlenmişti. Bu oturum metni denetledi, c7 son parçasını değiştirdi, eksik sentezi tamamladı, gerisini yaptı.

## 1. Cümle tablosu

| # | Cümle | Önce | Sonra | Gerekçe |
|---|---|---|---|---|
| 1 | c3 parça 3 | `While, tam anı gösterir.` | `Burada while, aynı anda süren iki işi bağlar.` | "Tam an" belirsiz terimdir; while eşzamanlı iki süreci bağlar ("-ken"). YV-DUZ önerisi "While, aynı anda süren iki işi bağlar." genel kural gibi okunur; while uzun eylemle kısa olayı da bağlar (*While I was cooking, the phone rang*). "Burada" sözcüğü iddiayı bu cümleye sınırlar. |
| 2 | c7 parça 1 | `Olmaz. Know, believe, own, belong durum fiilidir, -ing almaz.` | `Olmaz. Know, believe, own, belong durum fiilidir, durum anlamında -ing almaz.` | Mutlak kural. Durum fiili eylem anlamında -ing alır (*I am thinking about it*, *I am having lunch*). YV-DUZ önerisi aynen. |
| 3 | c7 parça 5 | `Always artı -ing şikâyettir.` | `Always artı -ing çoğu zaman şikâyet bildirir.` | Mutlak. Olumlu kullanım da var (*She is always helping people*). YV-DUZ önerisi aynen. |
| 4 | c7 parça 5 | `Kod: olay -ing alır, durum almaz.` | `Kod: olay -ing alabilir, durum genellikle almaz.` | Jüri hükmü (YVJ, cümle 7) bu cümleyi de mutlak buldu; YV-DUZ §4 tablosu yalnız ilk iki ifadeyi aldı. "Olay -ing alır" alışkanlıkta yanlıştır (*I play tennis every day*); "durum almaz" eylem anlamını dışarıda bırakmaz. Önceki oturum "durum çoğu zaman almaz" yazmıştı; aynı parçada "çoğu zaman" iki kez geçiyordu, "genellikle" seçildi (anlam aynı). |

Değişen dosyalar (1–4 ortak): `ortak/anlatim/senaryo.json` (parça + `metin`), `ortak/anlatim/METIN.md`, `ortak/anlatim/altyazi.json`,
`sureler.json`, `sozcukler.json`, `ortak/anlatim/sozcuk_uret.py` (cümle başları), sahne 03 (`sahne-03.js`) ve sahne 06 (`uret.py` → `proje/index.html`),
`surumler.json` (`canAlici[3]`, sürüm adı, revizyon), `BRIEF.md`.

| Alan | Önce | Sonra |
|---|---|---|
| `meta.canAlici[3]` (senaryo + `surumler.json`) | `always + -ing = şikâyet; sınav bunu tuzak yapar` | `always + -ing çoğu zaman şikâyet bildirir; sınav bunu tuzak yapar` |
| `youtube.json`, `youtube-aciklama.md` | aynı iddia yok (grep 0) | metin değişmedi; zamanlar §6 |

### Kendi taramam (dersin öteki cümleleri)

| Cümle | Hüküm | Gerekçe |
|---|---|---|
| c1 `Dil sınavındaki -ing tuzağına düşme.` | doğru | Ana pakette doğru. **Dikeyde ekran ve altyazı eski metinde kalmıştı** (`YDT'nin …`, 13.11 düzeltmesi taşınmamış) → dikey raporu §2. |
| c2 formül cümleleri | doğru | `Subject + am/is/are + verb-ing` tam formüldür. |
| c4 `Geçici bir durum. This week bunu söyler.` | doğru, dokunulmadı | "This week" geçici süreyi işaret eder; kural iddiası kurmaz. Geçiciliği asıl Present Continuous taşır; cümle bunu dışlamaz. |
| c5 `Planlı gelecek. Bilet alınmış, saat belli.` | doğru, dokunulmadı | Örnek durumun yorumu (ayarlanmış plan); genel kural cümlesi değil. |
| c7 `Türkçede biliyorum deriz, ama İngilizcede -ing yok.` | doğru | Tek örneğe (`I know the answer`) bağlı karşıtlık; birebir denklik kurmaz. |
| c7 `Sınavda ikisi de çıkar.` | doğru | Dil bilgisi iddiası değil. |
| `meta.canAlici[0]`, `[4]`, `meta.kapak` | doğru | "Her fiile -ing eklenmez", "her zaman -ing değil": mutlak değil. |
| Rozet `YDT · ADVANCED` | düzeltildi | HV-24 (İngilizce seviye adı). §4. |

## 2. Ses ve süre

Yöntem (öteki cümlelerin sesi değişmez):
1. `el.py` önbellek anahtarı ağsız benzetildi (`~/is/duz3-0201I/anahtar.py`). Sunucu önbelleğinde bu dersin özgün sesi yoktu
   (ses Mac'te üretilmiş). Önceki oturum c3'ün 3 parçasını ve c7'nin 2 parçasını `HIZ_EN=0.9` ile önbelleğe yazmıştı.
2. Hız denetimi: özgün c3 EN parçası 5,12 sn, önbellekteki 0,9 sürümü 5,04 sn; özgün c7 `I know the answer.` 1,52 sn = 0,9 sürümü 1,52 sn.
   Özgün ses 0,9 ile üretilmiş; `ses-sunucu.sh` varsayılanı (0,9) korundu.
3. `el.py` yalnız c3 ve c7'yi taşıyan geçici senaryoyla koştu: `timeout 1500 bash araclar/ses-sunucu.sh --kok ~/is/duz3-0201I/kok present-continuous-ileri`.
   rc 0; 8 / 8 parça kapıdan geçti; 3 parça kapı önbelleğinden (c3); 293 karakter (≈ 1,44 TL). c7 parça 5 değiştiği için parça 1–2 de
   yeniden istendi (bağlam metni anahtara girer).
4. c1, c2, c4, c5, c6 eski `anlatim.wav`'dan örnek-eşit kesildi (`[başlangıç_N, başlangıç_N+1)`, 48 kHz; `~/is/duz3-0201I/kes.py`);
   c3 ve c7 = yeni `cumle-1.wav`, `cumle-2.wav`. `kur.py` → `anlatim.wav`; `araclar/ses-paketle.py --yaz --paket present-continuous-ileri` → `anlatim.m4a`.
5. Kayma 3 kare katına yuvarlandı: c3 +0,96 sn → c4–c7 başları +1,00 sn (sahne kare sınırları tam sayı kalır).
6. Kanıt: 0–15,80 sn PCM sha256 eski = yeni (`6f99eb6367df4ee2`); eski 30,13–60,40 = yeni 31,13–61,40 (`c89111ccc47c7b8e`);
   30,55–31,13 sn sessiz (en büyük örnek 0). Üreteçler önce eski dosyaları birebir yeniden üretti (`sozcuk_uret.py`, `altyazi_uret.py`: `cmp` eşit).

| Ölçü | Önce | Sonra |
|---|---|---|
| c3 süresi / sözcük | 13,78 sn / 35 | 14,74 sn / 39 |
| c7 süresi / sözcük | 23,56 sn / 40 | 25,72 sn / 46 |
| Cümle başları c4 · c5 · c6 · c7 | 30,13 · 42,62 · 54,63 · 60,40 | 31,13 · 43,62 · 55,63 · 61,40 |
| Konuşma sonu | 83,96 | 87,12 |
| Ders süresi (`zaman.json` son `t_son`, `anlatim.wav`, `anlatim.m4a`) | 84,96 sn | 88,16 sn |
| `anlatim.wav` sha256 | `5d1c5359e598` | `56d4c991e45c` |
| `anlatim.m4a` sha256 | — (sunucuda yoktu) | `8bc542bcf7f9` |
| `altyazi.json` | 21 parça, son t1 83,96 | 21 parça, son t1 87,20 (≤ 88,16) |

Whisper (faster-whisper large-v3-turbo int8, eşik 0,85; rapor `~/is/duz3-0201I/kok/…/sentez.wav.rapor.json`):

| Cümle | Dil | Metin | Duyulan | Benzerlik |
|---|---|---|---|---|
| c3 | tr | Birinci kök. | Birinci Kök | 1,00 |
| c3 | en | Please be quiet! The baby is sleeping in the next room while I am talking on the phone. | (aynı, "quiet.") | 1,00 |
| c3 | tr | Bebek uyuyor, … Burada while, aynı anda süren iki işi bağlar. | … İki işte şu anda sürüyor. Burada while. Aynı anda süren iki işi bağlar. | 0,99 |
| c7 | tr | Olmaz. Know, believe, own, belong durum fiilidir, durum anlamında -ing almaz. | … Durum anlamında. Ing almaz. | 1,00 |
| c7 | en | I know the answer. | I know the answer. | 1,00 |
| c7 | tr | Türkçede biliyorum deriz, ama İngilizcede -ing yok. | … İngilizce'de in yok. | 0,99 |
| c7 | en | He is always losing his keys. | He's always losing his keys. | **0,96** (en düşük) |
| c7 | tr | Always artı -ing çoğu zaman şikâyet bildirir. … Kod: olay -ing alabilir, durum genellikle almaz. | (aynı; "ing", "şikayet") | 1,00 |

## 3. Zaman zinciri

| Dosya | Değişiklik |
|---|---|
| `zaman.json` (iki paket) | 03: kare 442 → 472, t_son 30,58 (içerik 460) · 04: 30,58–43,07 · 05: 43,07–55,08 · 06: 55,08–88,16, kare 956 → 1022 (içerik 992) |
| `sozcuk_uret.py` | `BASLAR` c4–c7 +1,00 |
| `sozcukler.json` | 169 → 179 sözcük (c3 ve c7 yeni, c4–c6 +1,00) |
| `altyazi.json` | `altyazi_uret.py` ile yeniden |
| `METIN.md` | c3, c7 satırları yeni; c4–c6 +1,00; c1 tablo, parça ve sözcük satırı 13.11 metnine getirildi (eskiden `YDT'nin(1.00) …` kalmıştı; ses ve `sozcukler.json` zaten yeniydi); c2 dokunulmadı |
| Sahne 03 `calistir.sh` | `N=472`, denetim anları |
| Sahne 06 `zamanlar.json`, `calistir.sh` | t_bas 55,08, kare 1022; denetim anları |

## 4. Sahneler

| Sahne | Ne değişti | Neden |
|---|---|---|
| 01 giriş | `uret.py`, `yardim.py`: rozet `YDT · İLERİ` → `proje/index.html` | HV-24 |
| 02–05 künye | `ortak/kunye.js` `seviye: "YDT İLERİ"` (çalışma anında çizilir) | HV-24 |
| 03 örnek 1 | c3 sözcük zamanları (sabit sn değerleri yeni sese; daire, kutu, figürler, zaman çizgisi, bantlar); `NOW` → `aynı anda` (28,58); bantların sağ ucunu birleştiren ayraç (29,54 "iki işi"); formül kartı 28,62'ye | c3 yeni metin + süre |
| 04 örnek 2 | `kayma: -1.0` (sahne eski çerçevede, TBAS 29,58; yerel kareler aynı) | c3 +1,00 sn |
| 05 örnek 3 | `kayma: -1.0` (TBAS 42,07) | c3 +1,00 sn |
| 06 soru + form | c7 sözcük dizinleri kaydırıldı (`~/is/duz3-0201I/dizin-kaydir.py`, 37 dizin; eski metinle sözcük sözcük eşleşme denetimi); balon toplanma `S(T(7, 1)) - 0,35`; `always` 76,12 sabiti → `T(7, 28)`; R4 `always + V-ing: çoğu zaman şikâyet` (Caveat 52, 624 px; figür x ≥ 1640'tan önce biter); Kod `olay + -ing ✓` / `durum + -ing ✗ genellikle`; künye rozeti | c7 yeni metin + HV-24 |
| 90 kapak | `yardim.py` kullanılmayan `ROZET = "YDT · BASIC"` → `YDT · İLERİ` (kapak `uret.py` kendi `YDT · İLERİ` sabitini kullanır; kapak çıktısı değişmez) | HV-24 |

HF kaynak üretimi: `uret.py` → `olay.py` → `tema_hf acik` (`~/is/duz3-0201I/hf-uret.sh`; render yok). Taban farkı (kaynak değişmeden
yeniden üretim): yalnız tema betiği önündeki satır sonu ve dikey 01'de bir `hisirti` olayının sırası.

Kareler (kendim baktım; `node araclar/sahne-kare.mjs present-continuous-ileri <sahne> <t,…> <dizin> --tema acik --port 41333 --sunucu 41022`,
dizin `sahneler/<sahne>/k/duz3/`, git dışı):

| Sahne | Anlar (sn) | Gözlem |
|---|---|---|
| 01 | 1,2 · 2,9 | hap `YDT · İLERİ` + `GRAMMAR`; künye `· YDT İLERİ` |
| 02 | 9,0 · 15,0 | künye `PRESENT CONTINUOUS · YDT İLERİ`; süre etiketi `1.5 min` (88 sn → değişmez) |
| 03 | 19,5 · 22,2 · 26,6 · 28,7 · 29,7 · 30,5 | `aynı anda` okun ucunda, TR satırına binmez; ayraç x 935–968, bantlara ve zaman çizgisine değmez; kart sırası doğru |
| 04 | 33,4 · 38,0 · 42,9 | 33,4'te `is leaking` çiziliyor (ses 33,30); yerleşim eskisiyle aynı |
| 05 | 46,2 · 52,5 · 54,9 | 52,5'te `yarın` dairesi (ses 52,12) |
| 06 | 59,0 · 63,5 · 68,7 · 72,6 · 77,0 · 80,9 · 83,0 · 85,3 · 87,0 · 88,1 | R4 figüre değmez; `genellikle` formül kartının altında, `Next lesson`dan uzak; ✓ ve ✗ okunur |

## 5. Kapak

Kapak değişmedi. YV-DUZ §3 bu ders için "kusur görselde (beyaz üçgen), görsel bu işte değişmez" der; §4 kapak sütunu "—".
Kapak yazısı `KNOWING? OLMAZ!` yeni cümlelerle çelişmez (c6–c7: *I am knowing* biliyorum anlamında kabul edilmez).

## 6. Yayın verisi zamanı (`youtube.json`, `youtube-aciklama.md`; iki pakette aynı)

| Öğe | Önce | Sonra |
|---|---|---|
| Bölüm 1 Formül | 0,00 (00:00) | 0,00 (00:00) |
| Bölüm 2 is sleeping | 15,25 (00:15) | 15,25 (00:15) |
| Bölüm 3 this week | 29,58 (00:30) | 30,58 (00:31) |
| Bölüm 4 tomorrow morning | 42,07 (00:42) | 43,07 (00:43) |
| Bölüm 5 Tuzak | 54,08 (00:54) | 55,08 (00:55) |
| En kısa bölüm | 12,01 sn | 12,01 sn (son bölüm 33,08 sn) |
| Bildirim | 30,13 sn (%35,5) | 31,13 sn (%35,3); c4 başı, önceki cümle 30,54'te biter; son 20 sn sınırı 68,16 |

Damga bloğu `bolumler` ile aynı (yuvarlama `int(t + 0,5)`, betikle aynı).

## 7. Kapılar

```
$ /usr/bin/python3 uretim-hatti/betikler/yv-tutarlilik.py --kilitli simple-present-temel,simple-present-temel-dikey,02-04-ydt-temel-dikey
present-continuous-ileri / -dikey: süre 88.16 sn, bölüm 5; sinir, damga, kanal-etiketi, emoji, baslik, liste, dikey → TAMAM
[SORUN] zaman: 6 — hepsi simple-present-ileri ve -dikey (bölüm 3–5 sahne başı değil; başka oturumun DUZ3-0202I işi)
→ çıkış 1 (bu derste sorun 0; kilitli pakette 0)

$ node araclar/cakisma-kapisi.mjs present-continuous-ileri --port 41333 --sunucu 41022 --json ~/is/duz3-0201I/kapi-ana.json
02, 03, 04, 05: çakışma yok
01: cg:path0 × cg:text0 (-ing halkası × cümle, 2,00–3,00) hata; t1 × t2 uyarı
06: bw6/bw7 × xk1/xk2 (yanlış cümle × kırmızı çarpı) 4 hata; kn2 × kst (know-ing × üstü çizgi) hata; hf1 × los (his × losing dairesi) hata;
    br:text0 × br:text1, al2 × al3 (aynı sözcüğün renk dilimleri) uyarı
→ çıkış 1 (7 hata, 4 uyarı)
```

Hata çiftlerinin hepsi kasıtlı çizim (halka, çarpı, üstü çizgi, daire) ile bu işte dokunulmayan öğe arasındadır. Yeni öğelerde
(`aynı anda`, ayraç, `al5`/`al6`, `k1t`, `k2g`, `n3`/`n4`) hata 0. Sahne 03'ün yeni hâli çakışmasız.

## 8. Kısa video (`present-continuous-ileri-s1`; yalnız rapor, dokunulmadı)

| Dosya | Aynı sınıf ifade |
|---|---|
| `ortak/anlatim/senaryo.json` (ses), `altyazi.json`, `uretim-tutanagi/art.json` | `Bilmek durumdur, -ing almaz.` (mutlak kalıp; *know* için pratikte doğru, ana dersin yeni biçimi "durum anlamında -ing almaz") |
| `sahneler/02-paperjs-ornek/sahne-02.js` (ekran) | `-ing almaz.` |
| `BRIEF-S1.md` | can alıcı `know -ing almaz` |
| `senaryo.json` `meta.canAlici`, `surumler.json` | `always + -ing = şikâyet; sınav bunu tuzak yapar` (ana derste düzeltilen ifade) |
| `ortak/kunye.js`, `sahneler/01-…/yardim.py`, `sahneler/03-…/yardim.py`, `senaryo.json` | rozet `YDT · ADVANCED` (HV-24) |

Ana paketin `uretim-tutanagi/huni-konu.{json,md}` dosyası da `kural_ozeti` alanında eski mutlak cümleleri taşır
("Know, believe, own, belong durum fiilidir; -ing almaz.", "Always ile -ing birlikte gelirse şikâyettir."); tutanaktır, dokunulmadı.

## 9. Düzeltemediklerim / açık kalanlar

| Madde | Sebep |
|---|---|
| EK-11 kulak dinlemesi (c3, c7 yeni ses) | Nadir'in işi; Whisper süzgeçtir |
| mp4'ler bayat | render yasak; sahne `calistir.sh` dosyaları güncel kare sayısında (03 `N=472`, 06 `KARE=1022`) |
| Çakışma kapısı çıkış 1 | kasıtlı çizim çiftleri (§7); bu işin kapsamı dışında, yeni öğe kaynaklı değil |
| Tutarlılık kapısı çıkış 1 | `simple-present-ileri` (başka ders) |
| Kapak beyaz üçgen (`karakter.png`) | görsel kusur; istem "yeni görsel üretme" der |
| `huni-konu.{json,md}` eski kural özeti | tutanak; s1/s2 kısaları üretilirken jüri notuyla birlikte düzeltilmeli |
| Yazım boyutu kapısı | `write-size-gate` 15 satır ve üstü 4 düzenlemeyi durdurdu (03 ana, 06 dikey ×3); atlama bayrağı açılmadı, düzenlemeler ≤ 14 satırlık parçalara bölündü |
| Dikey çakışma kapısı | çıkış 1; ayrıntı ve sahne 03 ölçüm yanlış pozitifi dikey raporu §4 |
| `.claude/docs/sozlesme.md`, Kovan | istem yazmayı iki paketle sınırladı |

---
Son Güncelleme: 16.11.2026 (DUZ3-0201I oturumu).
