Jüri modeli: Claude Sonnet 5.5 (`claude-sonnet-5-5`). Üretici: Claude Opus 5.5 → FARKLI model (§1e sağlandı).

# YVJ-0202I — simple-present-ileri YouTube yayın verisi ÇIKTI jürisi · 15.11.2026

## Özet

| Sonuç | Sayı |
|---|---|
| Geçti (evet) | 8 (YV-1 … YV-8) |
| Kaldı (hayır) | 1 (YV-9) |
| Kanıt yok | 0 |
| §3 bildirim kuralları | 4 / 4 evet (veri düzeyi) |

Jüri hiçbir üretim dosyasını değiştirmedi. Sayılar salt okuma ile ölçüldü (`/usr/bin/python3 -I`, `diff`, `file`).
Bakılan dosyalar: `youtube.json`, `youtube-aciklama.md`, `zaman.json`, `ortak/anlatim/{METIN.md,senaryo.json,altyazi.json}`,
`kapak.png` (görüntü olarak), dikey paket eşleri, `varlik/grammar/katalog.json`, `02-03-ydt-ileri/surumler.json`.

## §2f madde tablosu

| Kimlik | Hüküm | Kanıt | Not |
|---|---|---|---|
| YV-1 | evet | Başlık "Simple Present \| YDT İngilizce" = 30 karakter (≤ 100). Kalıp `<Konu> \| <kitle> İngilizce`; konu `senaryo.json` "Simple Present", kitle "YDT" | Not: `simple-present-temel/youtube.json` aynı başlığı taşıyor. YV-1 yinelemeyi yasaklamaz; ama aynı kanalda iki videonun başlığı özdeş. Öneri aşağıda (N-1) |
| YV-2 | evet | `wc -c` = 675 bayt (≤ 5.000). Sıra: değer cümlesi → "Sınav günü bakmak için kaydet." → "Bölümler:" + 5 damga → "Sıradaki ders" → "Ders sayfası" (utm) → hashtag satırı | Değer cümlesi senaryodaki 3 kökle uyuşuyor (cümle 3, 4, 5). Dil ve yazım temiz |
| YV-3 | evet | İlk damga 00:00. 5 bölüm. Bölüm süreleri (sn): 17,65 · 14,80 · 15,84 · 13,12 · 29,02; en kısa 13,12 ≥ 10. Her `t` bir `zaman.json` sahne başı (0 · 17,65 · 32,45 · 48,29 · 61,41). Damgalar `round`: 00:18 · 00:32 · 00:48 · 01:01, açıklamayla birebir | Yuvarlanmış damgalarla en kısa aralık 13 sn (00:48 → 01:01), kural tutuyor. 00:32, 00:48 ve 01:01 sahne başından 0,29–0,45 sn önce düşer (önceki sözcüğün sonu); 00:18 sahne başından 0,35 sn sonra düşer ve sessizliğe denk gelir. Kabul edilir |
| YV-4 | evet | Senaryodan denetlendi: (1) "Hangi zaman? Önce kural: s ve does" = cümle 1–2: tarife kancası, he/she/it takes s, does + yalın fiil. (2) "Although cümlesinde zaman: it gives" = cümle 3, "Bağlaç var… gives". (3) "Durum fiilleri: owns ve costs" = cümle 4, "Owns ve costs durum fiilidir". (4) "Tarifeli gelecek: takes off tomorrow" = cümle 5. (5) "Will mi, Simple Present mi? Özet" = cümle 6–7: öğrenci sorusu, will ile ayrım, know/own/cost, "Kod:" özeti | İç ad ("Giriş", "Kanca", "Örnek 1") kalmadı. En uzun ad 36 karakter. Bölüm 5 yeni örnek de taşıyor (know, "I am knowing"); "Özet" adı bunu karşılıyor |
| YV-5 | evet | 12 etiket, ham 145 karakter (virgül dahil), YouTube sayımı 161 (tırnaklı çok sözcüklü etiketler dahil); ≤ 500. Konu (Simple Present), zaman adları (Present Simple, geniş zaman), kitle (YDT), "İngilizce", "gramer" var; yineleme yok | "ileri" tek başına zayıf arama sözcüğü ama zararsız |
| YV-6 | evet | Metin denetimi (başlık, açıklama, sabit yorum, gönderi g1): "Tarifeli bir saat için Simple Present kullanırız: The flight takes off at nine." doğru ve will'i dışlamıyor. "durum fiilleri", "bağlaçlı uzun cümle", "tarifeli gelecek" ders içeriğiyle uyuşuyor. Mutlak sözcük yok ("her zaman", "asla", "always", "never" taraması boş). Yazım hatası yok | Etiket "geniş zaman": arama sözcüğü, denklik iddiası değil; kabul. Kapak görseli bu madde kapsamında değil, YV-9'da hüküm aldı |
| YV-7 | evet | Katalog: ünite 02 "Tenses" sıra 2; konu GR-02-02 sıra 2; `seviyeler.ileri` = "İleri", `kitleler.ydt` = "YDT" → "Tenses · YDT İleri", sıra 2 doğru. Önceki `02-01-ydt-ileri`, sonraki `02-03-ydt-ileri` katalogda var. "Sıradaki ders" metni `02-03-ydt-ileri/surumler.json` `konu` ile birebir | N-2: katalog `02-02-ydt-ileri` öğesinin `proje` alanı `02-02-ydt-ileri` paketini gösteriyor (16 sahne, 419,12 sn, `youtube.json` YOK); veri `simple-present-ileri` paketinde. YV-7'nin konusu değil ama panel yanlış paketi okursa uç boş döner |
| YV-8 | evet | `altyazi.json` 22 satır; son `t1` = 89,51 ≤ ders süresi 90,43 (`zaman.json` son `t_son`). Dikey `altyazi.json` ana ile `diff` boş | `altyazi.srt` pakette yok (panel türetir), beklenen |
| YV-9 | hayır | B yönü tamam: `gorsel` = `kapak.png`, dosya pakette var, 1920×1080 açık tema (`file`); gönderi, sabit yorum ve açıklamada emoji yok. D yönü kaldı: kapağı açtım, büyük yazı **"YARIN ama WILL YOK"**. Bu gönderi görseli olarak yayına çıkacak. Mutlak ve yanlış denklik: "yarın" gelince will olmaz. "Our flight will take off at eleven tomorrow morning" dilbilgisi olarak doğru; derste cümle 7 de will'in tahmin ve ani karar için olduğunu söylüyor (üretici raporu §5 aynı uyarıyı yazmış). Ders içi cümle 6–7 "Hayır." kapsam sorunu ayrıca var (EK-5c sınıfı) | Düzeltme önerisi N-3 |

## §3 bildirim kuralları (`youtube-surumu-standart.md` §3)

| Kural | Hüküm | Kanıt |
|---|---|---|
| Sayı: ders < 4 dk ise 1 | evet | Ders 90,43 sn → 1; `youtube.json` `bildirimler` 1 satır |
| Zaman: ders payı ≈ %30, cümle sınırında | evet | `t` = 33,00 → %36,5. %30 hedefi 27,13 sn ilk 30 sn yasağına düşüyor; 33,00 ilk uygun cümle başı. `METIN.md`: cümle 4 başlar 33,00 (cümle 3 biter 32,45). Söz ortasına denk gelmiyor |
| İlk 30 sn | evet | 33,00 > 30 |
| Son 20 sn | evet | Son 20 sn sınırı 70,43; kart 33,00–36,00 |

Kapsam dışı (mp4 yok, kare yok): bildirim yeri ve çakışma (`ortak/youtube/bildirim/yer.json` bu çıkışta yok), sessizlik, sahne 4 örnek kartıyla (34,13'te açılır) çakışma. Bunlar YT-3 mp4 sonrası jürisinde ölçülür.

## Notlar

- N-1: Başlık özdeşliği. `simple-present-temel` ve bu ders aynı başlığı taşıyor. Öneri (kalıp korunur): "Simple Present: tarife ve durum fiilleri | YDT İngilizce" (56 karakter; kalıba uyuyor, YV-1 geçer).
- N-2: Katalog `02-02-ydt-ileri` → `proje: 02-02-ydt-ileri` (youtube.json yok). Panelin hangi paketi okuyacağı şef kararı; bu hüküm veriyi `simple-present-ileri` paketinde değerlendirdi.
- N-3 (YV-9 düzeltmesi): gönderi görselini yenile, büyük yazıyı mutlak olmayan hale getir. Önerilen yeni kapak metni: "YARIN ama TARİFE VAR" (alt satır "The flight takes off at nine." kalır) ya da `surumler.json` dikey kapak alanındaki "TARİFE = SIMPLE". Kapak yenilenince kapak jürisi yeniden koşar ve gönderi `gorsel` adı aynı kalır (`kapak.png`). Dikey paketin kapağı da aynı sloganı taşıyor (üretici raporu: 190 px "WILL YOK"); aynı düzeltme dikeye de uygulanır.
- N-4: Dikey sürüm Shorts sayılır: giriş 3 + ders 90,43 + kısa çıkış 4 ≈ 97,4 sn ≤ 180 (standart §2). Shorts'ta bölüm damgaları işlemez; açıklamadaki "Bölümler:" bloğu yine zararsız. Üretici raporundaki 113,43 sn 20 sn çıkışla hesaplanmış; standartta bu durumda kısa çıkış kullanılır.
- Dikey paket: `youtube.json` ana ile özdeş (`diff` boş); `zaman.json` yalnız genişlik ve yükseklik alanlarında farklı, sahne sınırları aynı; `youtube-aciklama.md` tek satır farkı `utm_content=dikey-tam` (doğru).
- Üretici raporundaki sayılar bağımsız ölçümle tutuyor (675 bayt, 30 karakter, 90,43 sn, 89,51 sn). Tek fark: etiket ham sayımı (rapor 134, jüri 145; ayırıcı virgüller dahil). Sonuç aynı.
