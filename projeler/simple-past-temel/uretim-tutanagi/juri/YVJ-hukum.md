# YVJ-0210T — `simple-past-temel` YouTube yayın verisi ÇIKTI jürisi · 15.11.2026

**Jüri modeli: Claude Sonnet 5.5 (`claude-sonnet-5-5`).** Üretici model: Claude Opus 5.5 (`claude-opus-5-5`; kaynak `YV-RAPOR.md`, dosyalar henüz commit değil). Model farklı. Jüri hiçbir üretim dosyasını değiştirmedi.

## Özet

| Sonuç | Sayı |
|---|---|
| geçti (evet) | 12 (YV-1 … YV-9 + sayı, cümle sınırı, ilk 30 sn / son 20 sn) |
| kaldı (hayır) | 1 (YT §3 zaman ≈ %30) |
| kanıt yok | 0 |

Ölçülen girdiler: `youtube.json`, `youtube-aciklama.md` (ana + dikey), `zaman.json` (ana + dikey), `ortak/anlatim/METIN.md`, `altyazi.json`, `kapak.png` (iki biçim, görüldü), `D/varlik/grammar/katalog.json`, `konu-adlari.json`. Pakette `senaryo.json` ve `baslar.json` yok; `METIN.md` cümle başları ve anlatım sözü kaynak alındı.

## Madde tablosu (§2f)

| Kimlik | Hüküm | Kanıt | Not |
|---|---|---|---|
| YV-1 | evet | başlık "Simple Past \| YDT İngilizce" = 27 karakter; kalıp `<Konu> \| <kitle> İngilizce` | konu `surumler.json` `video.konu` |
| YV-2 | evet | `wc -c` = 640 bayt (ana ve dikey); sıra: değer cümlesi (s1) · kaydet (s2) · damgalar (s4–8) · sıradaki ders (s10) · bağlantı (s11) · etiket (s13) | bağlantı canlılığı ölçüt dışı (bkz. not 3) |
| YV-3 | evet | ilk damga 00:00; 5 bölüm; en kısa bölüm 14,55 sn (`zaman.json`: 0–14,8–29,35–47,82–64,78–93,81); damgalar en yakın saniye: 00:15 · 00:29 · 00:48 · 01:05, `youtube.json` `t` ile tutarlı | |
| YV-4 | evet | her ad `METIN.md` cümlesiyle eşleşti: b1 = c1–2 ("Türkçede biten işe -di ekleriz"; Simple Past duyurusu), b2 = c3 (watch + -ed), b3 = c4 ("Go değil, went"), b4 = c5 (didn't, "Did you play football?"), b5 = c6 (öğrenci "Neden?") + c7 (iki yol, yesterday · ago · last year, özet) | iç ad ("Örnek 1") yok; en uzun ad 38 karakter |
| YV-5 | evet | düz toplam 130; YouTube sayımı (virgül + 8 boşluklu etikete tırnak) 158 ≤ 500; konu "Simple Past", zaman adı "Past Simple" + "geçmiş zaman", kitle "YDT" var; yineleme yok | |
| YV-6 | evet | metin taraması: emoji 0; "dakika", "dk", "Tam ders", "BASIC" yok. İddialar: açıklama s1 ("watched gibi -ed alan fiiller, went gibi düzensiz fiiller, didn't ve did ile olumsuz ve soru") doğru; g1 ("watched" ama "went"; üç örnek) doğru; sabit yorum iddiasız; mutlak kural ve yanlış denklik yok | "köprü" sözü: bölüm 1 adı -di ile Simple Past arasında köprü kurar, -di = -ed demez; geçer. Ana ders bulguları ayrı: not 1 |
| YV-7 | evet | katalog: ünite `02` "Tenses"; GR-02-10 sıra 10; videolar `02-09-ydt-temel` (Present Perfect Continuous) ve `02-11-ydt-temel` (Past Continuous); `kitleler.ydt` = YDT, `seviyeler.temel` = Temel → "Tenses · YDT Temel" | sonraki öğe `durum: planli` (not 2) |
| YV-8 | evet | `altyazi.json` son satır `t1` = 92,81 < ders sonu 93,81; srt pakette yok (panel türetir) | |
| YV-9 | evet | `kapak.png` var: ana 1920×1080, dikey 1080×1920; ikisi açık tema (sarı zemin, görüldü); g1 `gorsel` = `kapak.png`; gönderi metninde emoji 0 | kapakta "-di → -ed · go → went" iki ayrı yolu gösterir; yanlış denklik yok |

## `youtube-surumu-standart.md` §3 bildirim kuralları

| Kural | Hüküm | Kanıt |
|---|---|---|
| Sayı | evet | ders 93,81 sn < 240 → 1 bildirim; `youtube.json` 1 satır |
| Zaman ≈ %30 | **hayır (kaldı)** | `t` = 47,82 → %51,0 (47,82 / 93,81). %30 hedefi 28,14 sn. Standart "≈ %30" der; %51 bunun dışında. Üretici gerekçesi "ilk 30 sn yasağı" bu okumaya dayanır: ders zamanı. Standart ölçü zamanını tanımlamaz. `youtube.json` `t` ders zamanıdır, YouTube zamanı giriş (3 sn) kadar kayar → cümle başı 29,35 YouTube zamanında 32,35 sn olur ve ilk 30 sn dışına düşer; bu an %31,3'tür |
| Cümle sınırı | evet | 47,82 = `METIN.md` cümle 5 başı ("Üçüncü örnek."); önceki söz 47,27'de biter |
| İlk 30 sn / son 20 sn | evet | 47,82 ≥ 30; bildirim 47,82–50,82, son 20 sn başlangıcı 73,81 → dışında (YouTube zamanında 50,82–53,82; çıkış sonuna kadar 20 sn ek, yine dışında) |

## Kaldı maddesi ve düzeltme önerisi

**YT §3 zaman ≈ %30.** Öneri (tek cümle): standart §3'e "ilk 30 sn YouTube zamanıyla ölçülür (giriş klibi dahil)" yazılsın ve `youtube.json` `bildirimler[0].t` 47,82 yerine **29,35** olsun (cümle 4 başı "İkinci örnek.", %31,3; YouTube zamanında 32,35 sn); ya da standart değişmeyecekse 47,82 için standarda "ders < 2 dk ise cümle sınırı ve ilk 30 sn %30 hedefinden önce gelir" istisnası yazılsın. Karar şefte: standart yorumu jürinin işi değil.
Uyarı: 29,35 ve 47,82 ikisi de sahne geçişiyle çakışır (`gecis_kare` 12 = 0,4 sn); üreticinin açık nokta 3'ü iki seçenekte de geçerlidir; Nadir önizlemede bakar.

## Notlar (kaldı sayılmaz)

1. **Ana ders dilbilgisi (kural §1c; bu pakette değişmedi, yayın metnine girmedi).** (a) `METIN.md` cümle 7 "Olumsuzda ve soruda did gelir, fiil yalın kalır." mutlak biçimde yazılı: `be` fiilinde (I wasn't, Were you…?) yanlış. Cümle 5'te kapsam örneğe bağlı ("We didn't play"); cümle 7 genelliyor. Öneri: "Düzenli ve düzensiz fiillerde olumsuzda ve soruda did gelir, fiil yalın kalır." (b) `METIN.md` cümle 2 "İngilizce de -ed ekler." her fiil için okunabilir; cümle 4 hemen düzeltir ("Burada -ed yok, çünkü go düzensiz"). Geçer, ama kanca cümlesi tek başına yanlış denklik çağrıştırır. (c) `surumler.json` `canAlici` "Türkçedeki -di = İngilizcedeki -ed" yanlış denklik; yayın verisine girmedi (grep: `youtube*` dosyalarında yok). Öneri: "Türkçedeki -di işlevi, İngilizcede Simple Past'tır; düzenli fiilde -ed, düzensizde ikinci hâl."
2. **Sıradaki ders sözü.** Açıklamada "Sıradaki ders: Past Continuous"; `02-11-ydt-temel` katalogda `planli`. Yayın sırası kataloğa uyarsa sorun yok; 02-11 yayından önce yüklenirse söz boşa gider. Yükleme sırası kuralına bağla.
3. **Ölçülmeyenler.** Bağlantı (`https://ydspublishing.com/grammar/02-10-ydt-temel?utm_…`) canlı mı: ağ kapalı, ölçülmedi; biçim iki emsal paketle (`02-04-ydt-temel`, `02-02-ydt-temel`) aynı (`utm_content=ana-yatay`, `dikey-tam`). Dikey sürüm YouTube süresi ≈ 100,8 sn (3 + 93,81 + 4 kısa çıkış) ≤ 180 → standart §2 gereği Shorts sayılır; Shorts'ta bölüm damgaları ve bitiş ekranı çalışmaz. Dikey `youtube.json` ana ile bayt bayt aynıdır (`cmp`); dikey damgaların işe yarayıp yaramadığı yayın sözleşmesinde yazılı değil. Şef kararı.
