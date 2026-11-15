# S1 jüri düzeltmeleri — 02-04-ydt-temel-s1 · 15.11.2026 (istem S1-C)

Girdi: `juri/s1.dil.md` (DÜZELT, 3 madde), `juri/s1.kaynak-kural.md` (DÜZELT, 4 madde). 7 maddenin 7'si işlendi.
İki jürinin "Amcamla" maddesi (dil 1, kaynak 2) aynı sorundur; tek düzeltme ikisini kapatır.

| # | Madde | Yapılan | Kanıt |
|---|---|---|---|
| 1 | dil 1 + kaynak 2 — cümle 1 ses–ekran sınırı: "Amcamla" 2,52'de duyulur, ekrana 3,00'te gelir | İki jürinin ortak ilk seçeneği: sahne 01 iki satır taşır; `Amcamla yaşı-yor-um.` `Amcamla` çapasında gelir. Sahne 01 → 02 sınırı 3,00'te kalır (K23 giriş ≤ 3 sn). `ek_ayir` `Türkçede` çapasına (3,96) bağlandı. Süre tablosu güncellendi | `senaryo-taslak.md` §2 satır 01–02, §4 · ölçülen `ortak/anlatim/sozcukler.json`: `Amcamla` 2,52–3,00 · `yaşıyorum.` 3,08 · `Türkçede` 3,96 · `BRIEF-S1.md` "Sahne içeriği" |
| 2 | dil 2 — ders adındaki "ve" için kanıt yetersiz | Not düzeltildi: "Kural 7 `ve,` uygular; sentezde kulak + Whisper kapısı zorunlu". Ekran `vs` sesteki `ve` çapasına (24,77) bağlandı | `senaryo-taslak.md` §3 · kuru koşu `ses_metni`: `Tam ders: Simple Present ve, Present Continuous.` · `ortak/anlatim/sentez.wav.rapor.json` parça 8: duyulan `Tam Ders, Simple Present ve Present Continuous`, benzerlik 1,00 |
| 3 | dil 3 — "üç farkın hepsi" göndermesi Shorts içinde açık değil | Jürinin önerdiği ilk yol: cümle 3 başına `Bu, üç farktan yalnız biri.` (+5 sözcük). Açıklamanın 3 bölümüne "üç farktan biri" yazıldı | `ortak/anlatim/senaryo.json` cümle 3 · `aciklama-taslak.md` §3–§5 · `../aciklama.md` §1–§3. Etki: ölçülen toplam 30,56 sn (jüri tahmini ≈ 28) → `S1-C-RAPOR.md` açık nokta 1 |
| 4 | kaynak 1 — hap rengi yanlış (`#d9900f` üstüne `#f7f3ea`, ≈ 2,4:1) | Hap = dolgu `#ffe066` (`RENK.vurguDolgu`), yazı `#1b2440` (`RENK.pilMetin`); üç yerde yazıldı. "Kalem sözleşmesi 14.11" atfı senaryodan silindi; S1-A raporuna geçersiz notu eklendi | `kapak-taslak.md` satır 12 · `senaryo-taslak.md` sahne 03 satırı · `S1-A-RAPOR.md` karar 7 ek satırı · kaynak `present-continuous-ileri-s1/ortak/kunye.js` satır 9–10 (`vurguDolgu: "#ffe066"`, `pilMetin: "#1b2440"`), 139–140 |
| 5 | kaynak 3 — `utm_campaign` küçük harf sapması tabloda yok, K35 gerekçesi uymuyor | §2 gerekçesi düzeltildi (analitik büyük/küçük harfi ayırır; K35 yalnız biçim emsali). §6 tablosuna 4. satır eklendi. huni-plan §6 güncellenmedi (yazma kapsamı dışı; Nadir kararı) | `aciklama-taslak.md` §2, §6 · `../aciklama.md` §4 |
| 6 | kaynak 4 — "yeni metin yok" iddiası yanlış | S1-A raporu karar 1'e düzeltme satırı: "kavramlar ve örnekler ana dersten; bağlayıcı TR cümleler yeni" ve 5 yeni cümle listesi | `S1-A-RAPOR.md` karar 1 ek satırı |
| 7 | kaynak 4 (koşul) — "ses sentezinden önce dil jürisi yeni 4 TR cümleyi okusun"; *live* ayrı `en` parçada kalsın | *live* ayrı `en` parçada korundu. Dil okuması: S1-B dil jürisi `senaryo-taslak.md`'nin tamamını denetledi (4 cümle dahil), madde açmadı ("Ses metni" geçen kontrolü); 5. cümle dil jürisinin kendi önerisidir. Ayrı bir dil jürisi koşusu açılmadı | `juri/s1.dil.md` "Geçen kontroller" · `senaryo.json` cümle 2 parça 2 `["en", "I live in Istanbul."]` · Whisper kapısı 9/9 (`S1-C-RAPOR.md` §2). Yorum şefte: `S1-C-RAPOR.md` açık nokta 3 |

## Uygulanmayan / Nadir kararı

| Madde | Neden |
|---|---|
| huni-plan §6 `utm_campaign` şemasını küçük harfe çekmek | `dijital-anlatim` belgesi; yazma kapsamı dışı, Nadir kararı (kaynak 3) |
| Dikey kalıp §5 `@ydspublishing · 6 dk` ve örnek paketin "kanalda izle" / "6 dakika" metni | iki jüri de "bu paketin dışında" dedi (S1-A açık nokta 5); sahne 03 istemi örneği kopyalamayı yasaklar |
| Instagram/TikTok dili (öğretmen + YDT öğrencisi) | S1-A "Nadir'e soru"; dil jürisi "dilde sorun yok" dedi; karar Nadir'de |
