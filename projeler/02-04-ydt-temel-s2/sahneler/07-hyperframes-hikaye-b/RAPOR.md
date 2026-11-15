# Sahne 07 — Hikâye karesi B, soru kartı (02-04-ydt-temel-s2, HyperFrames, 1080×1920, tek kare)

Tema: acik

| Alan | Değer |
|---|---|
| Durum | uret.py yazıldı (agy) · önizleme hazır · açık + koyu PNG yakalandı · mp4 YOK · zaman çizelgesi dışı (`zaman.json` → `duragan`) |
| Teslim | `P/hikaye-b.png` (1080×1920, md5 `a9f106d1…`) · `D/k/koyu/hikaye-b-koyu.png` (1080×1920, md5 `2823ee8e…`) |
| Dosyalar | `SPEC.md` (şef) · `uret.py` (agy, 525 satır) · `calistir.sh`, `olay.py`, `zamanlar.json`, `yardim.py` (S1 sahne 07 kopyası) · `proje/index.html` · `nesneler.json` · `olaylar.json` (`[]`) |
| Kaynak | `BRIEF-S2.md` Hikâye tablosu B · `uretim-tutanagi/hikaye-taslak.md` §4 · `S2-duzeltme.md` madde 1 · BRIEF-DIKEY §0, §2–§3 |

## Ekran (y = blok, px)

```
HUD 0–288      logo · SIMPLE PRESENT vs / PRESENT CONTINUOUS · YDT · BASIC · çip "Full lesson" (kunye.js)
376–472        Hangisi doğru?                        Fredoka 96, mürekkep, hapsız
512–788        kök kartı: Look! She ____ her / pink T-shirt today.   Fredoka 72 · boşluk = kalem çizgisi · sağ üstte tişört
828–988        şık A: (A) wears                      kart, Fredoka 72
1028–1188      şık B: (B) is wearing                 kart, Fredoka 72 (A ile birebir aynı biçim)
1228–1295      Genel mi, şu an mı?                   Caveat 64
1364–1520      Cevap ve neden: / tam derste           Caveat 72 · @ydspublishing hapı (sağ)
1536–1920      boş (platform)
```
İçerik bandı doluluğu 0,884 (≥ 0,85). Sarı vurgu yok; doğru şık işaretsiz; `Look!` vurgusuz.

## Olay listesi

| Olay | Kare | Küresel sn | Yerel sn | Cümle sözcüğü |
|---|---|---|---|---|
| tek kare (bütün öğeler kare 0'dan görünür) | 0 (yakalama 15) | — (anlatımda yeri yok) | 0,0 (yakalama 0,5) | — (ses yok) |

## Kapı sonucu (son satırlar)

qa-yerel / çakışma kapısı koşulmadı: sahne `sahneler[]` dışında (istem D-S2; S1-VAR ölçümü: durağan sahnede `HATA sahne bulunamadı`).
Yerine `uret.py` içindeki 11 kural assert'i (§7: sınırlar, ≥ 64 px, ≤ 24 karakter, blok kesişimi 0, dikey boşluk ≥ 16, kart içi pay,
bant doluluğu, cevap yok, yasaklar) her koşuda geçer.

```
$ ONIZLE_YALNIZ=1 bash calistir.sh        → tema: acik · index.html yazıldı 8695 · olay 0 · önizleme hazır (çıkış 0)
$ bash calistir.sh --tema acik            → snapshot frame 1/1 at 0.5s · png,1080,1920 · P/hikaye-b.png (çıkış 0)
$ bash calistir.sh --tema koyu            → snapshot frame 1/1 at 0.5s · png,1080,1920 · D/k/koyu/hikaye-b-koyu.png (çıkış 0)
ffprobe: hikaye-b.png 1080,1920 · hikaye-b-koyu.png 1080,1920
```
Son durum: `proje/index.html` açık temada (önizleme varsayılanı).

## Bakılan kareler ve bulgu

| Kare | Bulgu |
|---|---|
| `P/hikaye-b.png` (açık) | Taşma yok · kesik yazı yok · üst üste binme yok · kontrast iyi (lacivert/krem; hap `#ffe066` + `#1b2440`) · boşluk çizgisi `She` ile `her` arasında okunur · tişört kart köşesinde, yazıya değmiyor · 1536 altı boş · altyazı yok |
| `D/k/koyu/hikaye-b-koyu.png` (koyu) | Aynı yerleşim; mürekkep krem, hap `#f2a93b` + koyu yazı; sorun yok |

Düzeltme turu: 0 (ilk koşu kabul).

## agy koşu özeti

`/home/sef/.claude/canavar/agy-filo/20261115-124829` — rol `kod`, gemini-3.8-flash-high, 294 sn, başarılı; yalnız `uret.py` yazdı.
Özetteki "değişen" listesi paralel oturumların dosyalarını da içerir (sahne 01, 02, 03, 05; S3 paketi); mtime ile ayrıldı.

## Açık noktalar

1. **Logo yeri:** BRIEF-S2 Hikâye B satırı "logo sol alt" der; BRIEF-DIKEY §0 (Nadir 04.11) "logo HUD sol üst, alt bantta logo yok" der.
   S1 hikâye B örneği gibi HUD'da tek logo kullanıldı. Şef ya da Nadir kararı.
2. **Çip metni:** `KUNYE.cipler["07-hyperframes-hikaye-b"]` = `Full lesson` kullanıldı (istem). S1 hikâye B çipi `Quiz` idi; soru kartı için
   `Quiz` daha uygun olabilir. Değişiklik `ortak/kunye.js`'te (kapsam dışı); uret.py çipi oradan okur, yeniden koşu yeter.
3. **Tişört rengi:** "pembe tişört" çizimi mürekkep çizgi; pembe dolgu palet dışı olduğu için konmadı.
4. **Instagram test çıkartması** (taslak §4 notu): elle konursa 1040–1300 bandı ipucu satırını (1228–1295) örter; o durumda ipucu çıkar.
5. Cevap anahtarı (B · `Look!` konuşma anı) karede yok; yalnız `hikaye-taslak.md` §4 ve açıklama notunda.
