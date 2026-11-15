# YVJ-0206T — `present-perfect-temel` YouTube yayın verisi · ÇIKTI jürisi · 15.11.2026

juri_model: Claude Sonnet 5.5 (`claude-sonnet-5-5`) · uretici_model: Claude Opus 5.5 (`claude-opus-5-5`, YV-RAPOR.md satır 3) → FARKLI (`juri-olcutleri.md` §1e sağlandı).
Bakılan çıktı: `youtube.json`, `youtube-aciklama.md` (ana + dikey; dikey `youtube.json` bayt bayt aynı, açıklama yalnız utm_content ayrışır), `zaman.json`, `ortak/anlatim/METIN.md`, `altyazi.json`, `surumler.json`, `kapak.png` (Read), katalog, `konu-adlari.json`.
Üretim dosyasına dokunulmadı. Sayılar bu jüri tarafından yeniden ölçüldü.

## Özet

| Geçti | Kaldı | Kanıt yok |
|---|---|---|
| 9 / 9 madde (YV-8 ve YV-3 bildirim yeri kısmen kanıt yok, aşağıda) | 0 | 2 alt kalem (srt eşitliği; bildirim yer.json) |

Kaldı yok. Aşağıdaki 3 not düzeltme önerisidir; hiçbiri kapıyı kapatmaz.

## Madde tablosu (§2f)

| Kimlik | Hüküm | Kanıt | Not |
|---|---|---|---|
| YV-1 | evet | başlık 31 karakter (≤100); kalıp `<Konu> \| <kitle> İngilizce`; konu = `surumler.json` "Present Perfect", kitle YDT | NFC doğru; ileri dersin başlığıyla çakışmıyor ("…since, for ve ago tuzağı") |
| YV-2 | evet | 684 bayt (≤5.000); sıra: değer cümlesi → kaydet → Bölümler → Sıradaki ders → bağlantı → hashtag; damga satırları `youtube.json` ile birebir (5/5 eşleşti) | utm_campaign `ING-YDT-GR-02-06-T` = `meta.kod`; emsal 02-04 ve ileri dersle aynı biçim (büyük harf, `ana-yatay` / `dikey-tam`). Bağlantı canlılığı ölçülmedi: kanıt yok, bu maddeyi kapatmaz |
| YV-3 | evet | ilk damga 0:00; 5 bölüm; süreler 18,73 · 15,43 · 16,96 · 16,07 · 27,67 sn (en kısa ≥10); her `t` `zaman.json` sahne başı (5/5) | Giriş (3,0 sn) Kanca ile birleşmiş: doğru |
| YV-4 | evet | senaryo (METIN.md) karşılaştırıldı: B1 cümle 1–2 "geçmişte oldu, sonucu şimdi"; B2 cümle 3 "I have broken", "have + üçüncü hâl"; B3 cümle 4 "has played … for five years", for = süre; B4 cümle 5 "never flown", "hayatın bugüne kadarki kısmı"; B5 cümle 6–7 öğrenci sorusu + "for/since, never/ever, just/already" özeti | İç ad yok. B3 adındaki "since" sahnede yalnız karşıtlık olarak geçer ("başlangıç olsaydı since derdik"); ad bu karşıtlığı söyler, yanlış değil. B4 "Deneyim" sözcüğü sahne 5'te geçmez, kavram geçer; kabul |
| YV-5 | evet | 15 etiket; düz 158, virgüllü 172 karakter; boşluklu 10 etiketin tırnak payıyla ≈192 (≤500); yineleme 0; konu, "Present Perfect Tense", YDT, İngilizce, gramer var | — |
| YV-6 | evet | Başlık, açıklama, sabit yorum (110 karakter, tek cümle), gönderi metni tek tek okundu. Mutlak kural yok ("sinyal sözcük" yumuşak söz), yanlış denklik yok, emoji 0, yazım doğru (hâl, hâlâ, İngilizcede, Present Perfect'i) | Gönderi sorusu ("hangi zamanla söylersin?") tek zaman ima eder; "I lost my key" de doğrudur. Metin ötekini yanlış saymıyor → geçer. Not 1 ve 2'ye bak |
| YV-7 | evet | katalog ünite 02 "Tenses"; GR-02-06 `sira` 6; önceki GR-02-05 → `02-05-ydt-temel`, sonraki GR-02-07 → `02-07-ydt-temel`; "Sıradaki ders: Present Perfect: Since & For" = `konu-adlari.json` GR-02-07 (güven yüksek) | Sonraki öğe katalogda `planli` (paket yok): yükleme sırası kapanana kadar bağ boş kalır |
| YV-8 | evet (json) · srt eşitliği kanıt yok | `altyazi.json` 23 satır, son `t1` 93,94 ≤ ders 94,86 (`zaman.json` t_son ve `anlatim.wav` ffprobe 94,86 aynı); dikey paketteki dosya aynı | srt'yi panel türetir; `youtube-saf.test.ts` bu worktree'de koşmadı. Madde metni json yarısını ister → geçer |
| YV-9 | evet | `kapak.png` pakette var: ana 1920×1080, dikey 1080×1920; kapak standardı satır 11 ve 13 "açık"; görsel okundu; gönderi metninde emoji 0 | Not 3'e bak |

## youtube-surumu-standart.md §3 bildirim

| Kural | Hüküm | Kanıt |
|---|---|---|
| Sayı | evet | ders 94,86 sn < 4 dk → 1 bildirim; `bildirimler` 1 kayıt |
| Zaman (≈%30 ve ilk bilgiden sonra) | evet | 34,71 sn = %36,6; ilk bilgi (have + üçüncü hâl) 34,16'da bitti; "≈%30" (28,5 sn) ile "ilk 30 sn yok" çakışır, üretici ilk cümle başını seçti. Standart iki kuralı birlikte karşılamanın yolunu yazmıyor (Not 2) |
| Cümle sınırı | evet | 34,71 = METIN.md cümle 4 başı ("İkinci örnek."); `baslar.json` pakette yok, METIN.md ve `sureler.json` kullanıldı |
| İlk 30 sn / son 20 sn | evet | 34,71 ≥ 30; kart biter 37,71 ≤ 74,86 |
| Ses yok, `sure` 3,0, `giris`/`cikis` true | evet | `youtube.json` |
| Yer (`yer.json`, dikeyde ayrı ölçüm) | kanıt yok | `ortak/youtube/bildirim/yer.json` dosyasını bu jüri bulamadı (yol `D/ortak/youtube/bildirim/` yok; arama kapısı yeniden aramaya izin vermedi). Dikey yer ölçümü `youtube.json`'da görünmez; araç türetir. Görsel jüri (G) bakar. Kart 36,00–39,12'de ekrandaki İngilizce örnekle aynı anda: G doğrulamalı |

## Düzeltme önerileri (kaldı değil)

1. Not 1 (dikey Shorts): dikey sürüm 3 + 94,86 + 4 = ≈102 sn ≤ 180 → standart D-0351 gereği Shorts sayılır; bölüm damgası ve bitiş ekranı çalışmaz, `youtube.json` iki pakette aynı ve dikey için "cikis": true. Öneri: şef dikey paketin damga bloğu için karar versin; yayın verisini değiştirmek gerekmez.
2. Not 2 (standart): §3'e tek cümle ekle — "≈%30 ilk 30 sn'ye düşüyorsa, ilk 30 sn sonrasındaki ilk cümle başı seçilir."
3. Not 3 (kapak metni): gönderi görseli "KAYBETTİM = HAVE LOST" yazıyor. Türkçe "-dı" ile "have lost" arasında birebir denklik kurar (kaybettim = I lost de olur). Dersin kendisi "geçmişte oldu, sonucu şimdi" diyerek şartı veriyor; ama görsel şartı taşımıyor. YV-6 kapsamı yazılı metinlerdir; kapak metni kapak jürisinin (KS) maddesi. Öneri: kapak jürisi bu denkliği bakar; gerekirse "KAYBETTİM, KAPIDA KALDIM = HAVE LOST".

Dersin kendi cümlesi (dil jürisi için not, kural 1c): cümle 7 "For ve since süre" — since süre değil başlangıç noktasıdır (cümle 4 doğru söylüyor); "just ve already yeni biten iş" — already "çoktan" anlamı taşır. Açıklama bu cümleleri yinelemiyor; senaryo jürisine iletilir.
