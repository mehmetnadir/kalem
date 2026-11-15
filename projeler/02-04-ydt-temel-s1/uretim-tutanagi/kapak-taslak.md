# 02-04-ydt-temel-s1 · kapak taslağı (1080×1920 PNG)

Durum: TASLAK (istem S1-A, 15.11.2026). Görsel üretim ve render YOK.
Kural: `dijital-anlatim/.claude/docs/dikey-senaryo-kalibi.md` §4 ve "Uygulandı (04.11)" bant tablosu.
Kapak = Shorts'un ilk karesi (kalıp §5). Çıktı adı: `kapak.png` (paket kökü; `surumler.json` → `kapak`).

## 1. Öğeler

| Öğe | Değer | Kural (§4) |
|---|---|---|
| Başlık satır 1 | `YAŞIYORUM` · mürekkep `#1b2440` · `YOR` altında sarı el altçizgisi (`alti`) | büyük, 2 satır, en çok 4 sözcük, kalın kontur |
| Başlık satır 2 | `= İKİ ZAMAN` · sarı hap: dolgu `#ffe066` (`RENK.vurguDolgu`), yazı `#1b2440` (`RENK.pilMetin`); kaynak `present-continuous-ileri-s1/ortak/kunye.js` satır 9–10, 139–140 (S1-C düzeltme 4) | 3 sözcük toplam; üçüncü satır yok |
| Can alıcı kısa kod | `yaşıyorum = live / am living` → başlık + sahne etiketleriyle okunur: ev yanında `I live`, bavul yanında `I am living` (Caveat, en az 72 px) | `canAlici[4]`'ün kısa kodu |
| Görsel | tek sahne: solda ev (kalıcı), sağda elinde bavul tutan öğretmen figürü (geçici); ifade: hafif gülümseme, baş eve dönük | figür + nesne, ifade okunur, kalabalık yok |
| Zemin | açık: kâğıt `#f7f3ea`, mürekkep `#1b2440` | K19 |
| Rozet | `YDT · BASIC` (tek rozet; şablon dili İngilizce; present-continuous-ileri-s1 `YDT · ADVANCED` ile koşut) | ders + seviye |
| Logo | `dijital-anlatim/varlik/logo/yds-publishing.svg`, alt sol (y ≈ 1478) | gerçek marka SVG'si |
| Yasak | üçüncü satır, küçük yazı, emoji, kalabalık sahne | §4 |

## 2. Yerleşim (dikey v2 bantları, y px)

```
0 ─────── 288   HUD: rozet YDT · BASIC
288 ───── 768   başlık: YAŞIYORUM / = İKİ ZAMAN   (y 346–768)
864 ──── 1344   sahne: ev (sol) · bavullu figür (sağ) · etiketler I live / I am living
1344 ─── 1536   boş (Shorts'ta altyazı bandı) · logo sol alt y ≈ 1478
1536 ─── 1920   platform arayüzü: BOŞ
```

- Başlık boyu: iki satır aynı boy. Boy = 952 px genişliğe (1080 − 2 × 64 kenar) sığan en büyük değer, üst sınır 190 px
  (present-continuous-ileri-s1 kapak boyu). Motor ölçer; elle boy yazılmaz.
- Etiket ve başlık yazısı dikey tabanın üstünde: en az 64 px (`motion-grafik-ders` kapısı dikey 50; dikey v2 64).

## 3. `senaryo.json` alanları (huni-plan §2 veri kaynağı)

```json
"giris": {
  "logo": "varlik/logo/yds-publishing.svg",
  "satir1": "YAŞIYORUM",
  "satir2": "= İKİ ZAMAN",
  "rozetler": ["YDT · BASIC"],
  "sahne": [
    {"ad": "house", "x": 30, "y": 58, "olcek": 0.6},
    {"figur": "ogretmen", "x": 68, "y": 58, "olcek": 0.8},
    {"ad": "suitcase", "x": 80, "y": 66, "olcek": 0.35}
  ]
},
"meta": {
  "kapak": {
    "satir1": "YAŞIYORUM",
    "satir2": "= İKİ ZAMAN",
    "canAlici": "Türkçe yaşıyorum iki zamana karşılık gelir: I live (kalıcı), I am living (geçici)"
  }
}
```

İkon adları (`house`, `suitcase`) öneridir; ikon kataloğunda yoksa Open Doodles / Tabler taranır (ana ders §6 kuralı).
x, y, olcek değerleri başlangıç önerisidir; sahne kodu yazılırken kontak sayfasında düzeltilir.

## 4. Karar notu

- İlk kare = kapak: başlık 0. karede tam görünür. Kalem hareketi yalnız `YOR` altçizgisinde (0,3–0,8 sn).
  Gerekçe: TikTok ve Instagram'da kapak seçilmezse akışta ilk kare görünür; YouTube Shorts kapağı yalnız Studio'da seçilir (huni-plan §5).
- Seçenek B (kullanılmadı): `YAŞIYORUM` / `LIVE? AM LIVING?`. Satır 2 16 karakter; 952 px'e sığması için boy ≈ 110 px'e düşer (kaba hesap: 0,55 em/karakter, ölçülmedi). Başlık küçülür.

## 5. Sürüm B — soru / merak (istem S1-VAR, 15.11.2026)

Çıktı `kapak-b.png` (paket kökü), sahne `sahneler/05-hyperframes-kapak-b/` (durağan kare, zaman çizelgesi dışı).
Fikir: A cevabı başlıkta verir (`= İKİ ZAMAN`); B soruyu sorar, cevabı vermez. İzleyici cevabı videoda bulur.

| Öğe | Değer | Kural (§4) |
|---|---|---|
| Başlık satır 1 | `YAŞIYORUM` · mürekkep · `YOR` sarı kutuda (dolgu `vurguDolgu`, yazı `pilMetin`) — **tek vurgu** | 2 satır, kalın kontur (zemin rengi 12 px, A ile aynı) |
| Başlık satır 2 | `NASIL DENİR?` · mürekkep, hap yok | toplam 3 sözcük; üçüncü satır yok |
| Can alıcı kısa kod | iki düşünce balonu: `I live?` · `I am living?` (Caveat, en az 72 px). Soru işareti seçenektir; cevap yok | `canAlici[4]` soru biçiminde |
| Görsel | solda öğretmen figürü (aynı kadro: ShirtPantsWB / Smile / Short), sağda alt alta iki balon; balon 1'de ev, balon 2'de bavul ikonu; balon ile baş arasında düşünce noktaları | figür + nesne, tek sahne |
| HUD | logo sol üst 96 px, rozet `YDT · BASIC` (48, 216) — A kapak karesiyle aynı; ders adı ve çip yok | BRIEF-DIKEY §0 (logo HUD'da) |

```
0 ─────── 288   HUD: logo · rozet YDT · BASIC
346 ───── 720   başlık: YAŞI[YOR]UM / NASIL DENİR?
840 ──── 1344   sahne: figür (sol) · balon 1 "I live?" + ev · balon 2 "I am living?" + bavul · zemin çizgisi 1344
1344 ─── 1920   boş
```

## 6. Sürüm C — karşıt çift (istem S1-VAR, 15.11.2026)

Çıktı `kapak-c.png`, sahne `sahneler/06-hyperframes-kapak-c/`.
Fikir: A Türkçe başlık + İngilizce etiket taşır; C bunu ters çevirir: İngilizce çift başlıkta, Türkçe anlam etikette.

| Öğe | Değer | Kural (§4) |
|---|---|---|
| Başlık satır 1 | `I LIVE` · mürekkep | 2 satır, kalın kontur |
| Başlık satır 2 | `I AM LIVING` · `AM LIVING` sarı kutuda — **tek vurgu** (fiil öbeği; yalnız `-ING` vurgulanırsa "I living" yanlışı pekişir) | |
| Hizalama | iki satır aynı sol x: iki `I` alt alta, çift göz hizasında okunur; blok yatay ortalı | |
| Can alıcı kısa kod | Türkçe etiketler: ev üstünde `kalıcı`, bavul üstünde `geçici` (Caveat, en az 72 px) | `canAlici[4]`: I live (kalıcı), I am living (geçici) |
| Görsel | solda ev, ortada öğretmen figürü (eli boş), sağda yerde bavul; zemin çizgisi | figür + nesne, tek sahne |
| HUD | A ile aynı (logo + rozet) | |

```
0 ─────── 288   HUD: logo · rozet YDT · BASIC
346 ───── 720   başlık: I LIVE / I [AM LIVING]   (sol hizalı blok)
840 ──── 1344   sahne: ev + "kalıcı" · figür · bavul + "geçici" · zemin çizgisi 1344
1344 ─── 1920   boş
```

**SAPMA (Nadir kararı):** C başlığı 5 sözcük (`I live` 2 + `I am living` 3); §4 "en çok 4 sözcük" der. İstem C'yi bu çiftle
tanımlar; video ve kartlar `I am living` yazar. 4 sözcüklü seçenek `I LIVE` / `I'M LIVING`: kısaltma derste geçmeyen yeni biçim
getirir, bu yüzden seçilmedi. Satır 2 11 karakter, 952 px'e büyük boyla sığar (§4'ün amacı: büyük yazı).

## 7. A / B / C farkı

| | A (`kapak-a.png`) | B (`kapak-b.png`) | C (`kapak-c.png`) |
|---|---|---|---|
| Başlık dili | Türkçe, yargı | Türkçe, soru | İngilizce, çift |
| Başlık | `YAŞIYORUM` / `= İKİ ZAMAN` | `YAŞIYORUM` / `NASIL DENİR?` | `I LIVE` / `I AM LIVING` |
| Tek vurgu | satır 2 sarı hap (+ `YOR` altçizgisi) | `YOR` sarı kutu | `AM LIVING` sarı kutu |
| Kısa kod | EN etiket `I live` / `I am living` | EN soru balonu `I live?` / `I am living?` | TR etiket `kalıcı` / `geçici` |
| Sahne | ev (sol) · bavullu figür (sağ) | figür (sol) · iki balon (sağ) | ev · figür · bavul |
| Cevap karede | var | yok | var |
