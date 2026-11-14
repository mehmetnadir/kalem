# Tur 1 düzeltme tutanağı — 02-04-ydt-temel · 14.11.2026

Yazan: taslağın yazarı (Claude oturumu, srv21, istem A2). Düzeltilen dosya: `../senaryo-taslak.md` (tur 2).
Jüri dosyaları değişmedi. Önceki taslak kopyası yalnız oturum içi karşılaştırma için tutuldu (repoda yok).

| Jüri | Karar | Madde | Uygulandı | Uygulanmadı / kısmen |
|---|---|---|---|---|
| kaynak | DÜZELT | 2 | 2 | 0 |
| kural | GEÇTİ | 0 | — | — |
| dil | DÜZELT | 4 + 1 ek öneri | 5 | 0 |
| dil · okunuş riski | — | 6 | 2 | 2 metin değişmedi · 1 kısmen · 1 değişiklik gerekmedi |

## 1. Kaynak jürisi

| # | Madde | Durum | Değişen taslak satırı (önce → sonra) |
|---|---|---|---|
| K1 | §1 künye kapsam aralığı çelişiyor | uygulandı | Künye "Kaynak döküm": "00:00–04:30 bu dersin kapsamı" → "00:00–03:14 kullanıldı; 03:14–04:30 slayt 3 S4, *smell*, 02-05'e bırakıldı". Kaynak notu: "tabloyu 00:17–04:30 arasında satır satır işler" → "tablonun 3 satırını 00:17–03:14 arasında işler; 4. satır (03:14–04:30) 02-05'te". Aynı çelişki §5'te de vardı: "eski video 00:17–04:30, 4,5 dk … kalan 14,5 dakikası" → "00:17–03:14, yaklaşık 3 dk … kalan 16 dakikası (03:14–19:15) durum ↔ eylem satırı ve -ing almayan fiiller". |
| K2 | §4 satır 7 "planı kişi yapar" türetilmiş diye işaretli değil | uygulandı (jürinin 1. yolu) | §3 yeni satır: "Türetilmiş 3 · planı yapan kişidir, ekran *person → plan* (döküm 03:08 "plan yapmış"; yeni kural yok) → Satır 7". "Döküm 02:46–03:14" satırı: "Satır 5" → "Satır 5, satır 7 (türetilmiş 3)". Kaynak notu: "türetilmiş 2 cümle" → "türetilmiş 3 öğe (2 cümle, 1 çıkarım)". Ekran metni değişmedi: istem kuralı 2 (çıkarım kalırsa türetilmiş işareti). |

Not (K1): `istem/A-girdi.md` satır 111 hâlâ 04:30'u "02-04 kapsamının sonu" sayar. Bu istem yalnız taslağı ve bu dosyayı yazmaya izin verir; A-girdi düzeltmesi girdiyi yazan oturumun işidir.

## 2. Dil jürisi

| # | Madde | Durum | Değişen taslak satırı (önce → sonra) |
|---|---|---|---|
| D1 | satır 9: *today* konuşma anını göstermez | uygulandı | Ses: "Burada today konuşma anını gösterir. Bugünkü kıyafet: şimdiki zaman." → "Burada /təˈdeɪ/ bugünü gösterir. Bugünkü kıyafet: konuşma anında olan durum, şimdiki zaman." Ekran: `today → right now` → `today → this day only`. Görsel (anlatımla çelişmesin): `zaman_cizgisi` "now noktası nabız atar" → "today kısa gün bandı; now noktası bandın içinde nabız atar". Olay adı yeni değil. |
| D2 | satır 11: "İngilizcede ing yok" genel kural gibi ve yanlış | uygulandı | "Ama İngilizcede ing yok." → "Ama bu cümlede /ɪŋ/ eki yok." |
| D3 | satır 7: "Bu cümlelerde" belirsiz zamir | uygulandı | "Bu cümlelerde özne genelde cansızdır." → "Tarife cümlelerinde özne genelde cansızdır: tren, uçak, ders." *uçak*, *ders* kaynakta yok (döküm yalnız *train*) → §3 Türetilmiş 3 satırında işaretli. |
| D4 | satır 2 ↔ 8: "kullanım farkı" / "karşıtlık" iki ad | uygulandı | Satır 8: "Bu derste üç karşıtlık gördük." → "Bu derste üç fark gördük." Bölüm adı "Karşıt çift" kaldı (jüri izni). |
| Ek | satır 15: "Boşlukta hangisi?" doğal değil | uygulandı | "Boşlukta hangisi?" → "Boşluğa hangi şık gelir?" |

Çelişki denetimi (D-0205): kaynak ile dil jürisi çatışmadı. D1'de iki jüri de "bugüne ait" der; kaynak etiketi ("konuşma esnasında olan durum") seste korundu, yeni kategori etiketi yok. D3'te kaynak sözü ("özne genelde cansız") korundu; yalnız örnek özneler eklendi ve türetilmiş diye işaretlendi. Karşı kural eklenmedi.

## 3. Okunuş riskleri (dil jürisi tablosu)

| # | Yer · risk | Durum | Değişen taslak satırı / neden |
|---|---|---|---|
| O1 | satır 3 "Fiil aynı: wear." · "ver" okunuşu | uygulandı (IPA) | "wear." → "/wɛr/." |
| O2 | satır 9, 10 *today* tr parçada · "tudey/todi" | uygulandı (IPA) | tr parçalarda 4 kez "today" → "/təˈdeɪ/" ("Today iki cümlede de var." → "/təˈdeɪ/ iki cümlede de var."). EN parçalar değişmedi. |
| O3 | satır 3, 17 yalın *wearing*, *living* | uygulanmadı (metin) | 02-03 kanıtı: `kulak-rapor.md` cümle 18 "/æm/ writing" Whisper'da "I'm writing" duyuldu; kalıp aynı (`/ɪz/` + yalın V-ing). §6 risklere dinleme notu eklendi. |
| O4 | satır 11, 13 "yor eki", "ing" · harf harf | kısmen | "ing": tr parçada `/ɪŋ/` yazıldı (satır 6 "Neden ing yok?" → "Neden /ɪŋ/ yok?", satır 11, satır 18 "ing almayan" → "/ɪŋ/ almayan"). Neden: `ses_metni.py` Kural 4 yalnız tireli "-ing"i çevirir; taslaktaki tiresiz "ing" çevrilmezdi. 02-03 `ses-duzeltme.md`: tiresiz "ing" "İngi / INEG" duyuldu. §6'daki eski not ("ses_metni.py /ɪŋ/ yapar") yanlıştı, düzeltildi. "yor": metin değişmedi (Türkçe hece; tire "tire" okunur); §6 dinleme notu. |
| O5 | satır 15 `[sus 0,5 sn]` · EN kök bölünür | uygulanmadı (metin) | Boşluk soru kökünün parçası; sus kalır. Ton dinleme işi; §6 risklere eklendi. |
| O6 | satır 5, 10 *p.m.* | değişiklik gerekmedi | Jüri: "pi em" doğru (açık nokta 6). |

## 4. Kural jürisi (GEÇTİ) — korunan yapı

İskelet 8 bölüm, 18 satır, sıra aynı. Soru anları satır 6 (10 sözcük) ve satır 12 (10 sözcük), bölüm 2 ve 5. Öğrenci sonrası 0,75 sn, cevap ≤ 2 sn. Şıklar ekranda, ses okumaz. Görsel sütundaki tek değişiklik var olan `zaman_cizgisi` olayıdır (D1). Ses metninde süre iddiası ve kısaltma yok.

## 5. Açık noktalar

1–8: kapandı (taslak §7, her satırda "Kapandı: <jüri> — <karar>"). 9 yeni: tr parçada içerik sözcüğü IPA'sı (`/wɛr/`, `/təˈdeɪ/`) mı, ayrı `en` parça mı. IPA seçtim; tek sözcüklük `en` parça 13.11 KULAK ölçümünde zayıf duyuldu (`ses_metni.py` Kural 6). Kulak denemesi ses üretiminde.

## 6. Süre

| bölüm | tur 1 (sn) | tur 2 (sn) | neden |
|---|---|---|---|
| 2 Örnekler (3) | 84 | 85 | satır 7 +3 sözcük (D3) |
| 4 Karşıt çift | 30 | 31 | satır 9 +3 sözcük (D1) |
| 5 Tuzak | 37 | 38 | satır 11 +2 sözcük (D2) |
| 7 Mini soru | 30 | 31 | satır 15 +2 sözcük (ek öneri) |
| **Toplam** | **241 (4:01)** | **246 (4:06)** | 501 → 511 sözcük; EN %22; öğrenci 27 |

Hesap §5 ölçüsüyle (130 sözcük/dk, IPA = 1 sözcük). Sayaç önce tur 1 tablosunu satır satır birebir üretti, sonra tur 2'yi saydı.
