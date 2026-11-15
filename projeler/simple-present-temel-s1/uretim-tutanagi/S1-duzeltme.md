# S1 düzeltme kaydı — simple-present-temel-s1 (02-02-ydt-temel-s1) · jüri S1-B uygulaması · 15.11.2026

İstem P0202-S1-C adım 1. Jüri: `juri/s1.dil.md` (KARAR: DÜZELT, 4 madde → D1–D4) · `juri/s1.kaynak-kural.md` (KARAR: DÜZELT, 2 madde → K1–K2).

| Madde | Yapılan | Kanıt |
|---|---|---|
| D1 · orta — zamir listeleri TR parçada (`/aɪ/` → "A" riski, `it` Türkçe) | Değer cümlesi 5 parçaya bölündü: EN `My brother goes to school by bus.` · EN `He, she, it` · TR `ile fiile s gelir.` · EN `I, you, we, they` · TR `ile gelmez.` `senaryo-taslak.md` §2 (satır 39–40), §3, §4 notu ("ölçülmüş risk: TR `/aɪ/` → 'A'"), §5 süre tablosu; `S1-A-RAPOR.md` açık nokta 3 | `ortak/anlatim/senaryo.json` cümle 2 · `sentez.wav.rapor.json`: duyulan `He, she, it.` 1,00 · `İle fiile s gelir.` 1,00 · `I, you, we, they.` 1,00 · `ile gelmez.` 1,00 · değer cümlesi 9,96 sn (taslak tahmini 10,88) |
| D2 · düşük — değer kartında soluk TR yok; öneri `Kardeşim okula` / `otobüsle gider.` | **UYGULANMADI (öneri satırı).** K2 ile çelişir: K2 "söylenmeyen yeni TR satır (`Kardeşim okula otobüsle gider.`) ekleme" der. Ortak sorun (değer ekranında TR soluk yok) K2 yoluyla kapandı | `juri/s1.dil.md` madde 2 ↔ `juri/s1.kaynak-kural.md` madde 2 son cümle · karar şefte (`S1-C-RAPOR.md` açık nokta 1) |
| D3 · düşük — "konusunda köprü" iç terim | Satır 60 ve 108: `Simple Present (ING-YDT-GR-02-02-T): Türkçedeki geniş zaman eki = İngilizcedeki s. Gider = goes.`; §6 gerekçe satırı güncellendi | `aciklama-taslak.md` §3, §4, §6 · `../aciklama-a.md` §1 · `../aciklama-b.md` §1 · `grep "konusunda köprü"` → 0 |
| D4 · düşük — set B YouTube başlığı kapak B sorusunu yineler | Başlık `My brother goes: s nereden geliyor? \| YDT İngilizce #Shorts`; satır 116 kapak notu ve §5 "Eşleşen kapak" satırı güncellendi | `aciklama-taslak.md` §4–§5 · `../aciklama-b.md` §1 |
| K1 · düşük–orta — "hangi özne -s alır?" -s'i özneye bağlar | Kapak B `FİİLE -S` / `HANGİ ÖZNEYLE?` (4 sözcük; boy küçük kalırsa `-S HANGİ` / `ÖZNEYLE?`); Reels B ve TikTok B satırı `Fiile s hangi özneyle gelir?`. D4 ile birlikte YouTube B başlığı kapaktan ayrı kaldı | `kapak-taslak.md` §1, §4, §6 · `aciklama-taslak.md` §1 girişi, §4, §5 · `S1-A-RAPOR.md` satır 6, 57 · `grep "HANGİ ÖZNE /\|-S ALIR\|s alır?"` → 0 |
| K2 · düşük — değer sahnesinde örneğin Türkçesi yok | `Kardeşim gider:` satırı sahne 02'de soluk Caveat (ikincil renk) olarak sürer; sahne 01'in son konumundan başlar (taban y 560); ses değişmedi | `senaryo-taslak.md` §2 sahne 2 ekran sütunu · `../BRIEF-S1.md` "Sahne içeriği" 4,67 satırı · `istem/sahne/D-02-paperjs-deger.md` |

## İstem kaynaklı değişiklikler (jüri dışı)

| Değişiklik | Gerekçe | Dosya |
|---|---|---|
| Rozet `YDT · TEMEL` → `YDT · BASIC` | istem "Rozet emsaldeki gibi" (emsal `02-04-ydt-temel-s1` BRIEF); standart §2 örneği `YDT · TEMEL` | `senaryo-taslak.md` §1 · `kapak-taslak.md` (8 yer) · `hikaye-taslak.md` §3 · `../ortak/anlatim/senaryo.json` · `../ortak/kunye.js` |
| Klasör adları v2 temiz numara (01 kanca · 02 değer · 03 kaydet · 04 çağrı · 05 hikâye A · 06 kapak B · 07 kapak C · 08 hikâye B) | istem "Huni v2" bölümü | `senaryo-taslak.md` klasör eşlemesi · `kapak-taslak.md` §1, §6 · `hikaye-taslak.md` girişi |

## Jüri açık noktalarından sonraki duruma etki edenler

- Dil açık nokta 3 (`go` / `goes` TR parçada okunuş): Whisper `Kardeşim gider. Go mu, goes mu?` 1,00 duydu. Kulak kararı zorunlu (Nadir). B planı
  (TR `Kardeşim gider:` + EN `Go or goes?`) uygulanmadı; yeniden sentez yok.
- Kaynak açık nokta 5 (karakter erkek ↔ `kadro.ogrenci` kadın): S1 maddesi değil; karar Nadir/şef. Kapak B ve çağrı kartı ana dersin görselini kullanır.
