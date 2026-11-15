# Sahne 13 — Mini soru DİKEY (02-04 YDT temel, HyperFrames 1080×1920, 940 kare)

Tema: koyu

| Alan | Değer |
|---|---|
| Durum | yazıldı · önizleme hazır (`ONIZLE_YALNIZ=1`) · kapı GEÇTİ (çıkış 0) · render YOK |
| Zaman | t_bas 220,33 · t_son 251,27 · 940 kare · hareket yerel 0,55–30,05 sn (izin 0,40–30,93) |
| Cümleler | 15 soru (öğretmen) · 16 yanlış cevap A (öğrenci) · 17 cevap (öğretmen) |
| Dosyalar | `SPEC.md` (şef) · `uret.py` (agy + şef düzeltmesi) · `yardim.py` (dikey s01 kopyası) · `olay.py` (s01 kopyası, açıklama satırı) · `calistir.sh` (s07 kopyası, başlık + `KARE=940`) · `proje/index.html` · `olaylar.json` (29 olay, 11 çizgi) · `k/` |
| Yerleşim | HUD 0–320 (logo, ders 2 satır, rozet, çip `Mini question`) · kart 380–712 · şıklar 730–1162 · baş + balon 1198–1384 · altyazı 1400–1536 · platform boş |

## Olay listesi (kare = yerel; sözcük = cümle.sıra)

| Olay | Kare | Küresel sn | Cümle sözcüğü |
|---|---|---|---|
| kart çerçevesi (lejant boşluklu) + `MINI QUESTION` | 16 | 220,88 | 15.0 Mini |
| kök sözcük sözcük + 0,3 sn karaoke altı (11 sözcük) | 48 → 159 | 221,93 → 225,64 | 15.2 My → 15.12 us. |
| boşluk çizgisi (soluk, susma anında) | 131 | 224,71 | 15.10 he t1 + 0,06 |
| boşluk vurgu çizgisi (soluk çizgi söner) | 212 | 227,40 | 15.13 Boşluğa + 0,15 |
| sayaç halkası + 5 (kart sağ üst), 5 şık 0,18 sn arayla | 270 → 275 | 229,33 | 15.17 Beş |
| öğrenci başı → balon → balon sözcükleri | 307 / 310 / 313 | 230,58 / 230,68 / 230,76 | 16.0 Bence |
| A soluk sarı çerçeve | 332 | 231,40 | 16.1 A |
| balon söner (baş kalır) | 441 | 235,03 | 17.0 Ankara'da |
| odak *lives in* → *Ankara* (iki satır) | 444 / 454 | 235,13 / 235,48 | 17.0 |
| odak *this month*; ilk odak `ikincil`e döner | 547 | 238,55 | 17.6 bu |
| A pili `this month → temporary`; A çerçevesi söner; A soluk | 633 | 241,43 | 17.13 geçici |
| doğru B: `vurguDolgu` + yazı `pilMetin` | 693 | 243,43 | 17.17 B |
| B tiki (`pilMetin`) | 699 | 243,63 | 17.17 + 0,2 |
| boşluğa *is living*; *this month* odağı `ikincil`e döner | 739 | 244,95 | 17.20 is |
| C imleci; boşluk vurgusu `ikincil`e döner | 772 | 246,07 | 17.22 C |
| E imleci | 799 | 246,95 | 17.25 E |
| C pili `he ↔ live`; C soluk | 820 | 247,67 | 17.27 özneyle |
| E pili `he ↔ are`; E soluk | 835 | 248,15 | 17.28 uyumsuz. |
| D imleci (C, E imleci söner) | 863 | 249,11 | 17.29 D |
| D pili `to live: no tense`; D soluk | 885 | 249,83 | 17.31 tek |
| durgun; son 12 kare fade altında | 902 → 939 | 250,38 → 251,27 | — |

Sarı belirteç sayımı (karaoke ≤ 0,45 sn hariç) hiçbir anda 3'ü geçmez: 235,13 ve 238,55'te 3, 243,43'te 3, 246,95'te 3, son kare 2.

## Kapı sonucu

Komut: `bash araclar/qa-yerel.sh 02-04-ydt-temel-dikey 13-hyperframes-mini-soru 234.5,245.9,251.0 251.0 --hazirla`

```
== HAZIRLA
tema: acik
index.html yazıldı; komut 105 olay 29 hareket (0.55, 30.05)
olay 29 cizgi 11
önizleme hazır
== KAPI
13-hyperframes-mini-soru | çakışma yok (125 örnek, 35555 kutu)
kapı çıkış kodu: 0
```

Ek kareler: aynı betik `227.2,240.5 240.5 --kapisiz` (çıkış 0).

## Bakılan kareler ve bulgu

| Kare | Ne görünür | Bulgu |
|---|---|---|
| `k/13-hyperframes-mini-soru-227.2.png` | HUD, kart, kök 3 satır, soluk boşluk çizgisi, altyazı `with us.` | sorun yok; şıklar henüz yok, bant alt yarısı boş (açık nokta 1) |
| `k/13-hyperframes-mini-soru-234.5.png` | 5 şık, A çerçevesi, baş + 2 satır balon | sorun yok; balon kuyruğu başa değmez |
| `k/13-hyperframes-mini-soru-240.5.png` | iki odak (ilki `ikincil`), A çerçevesi, boşluk vurgusu | 3 sarı; sorun yok |
| `k/13-hyperframes-mini-soru-245.9.png` | B dolgu + tik, boşlukta *is living*, A pili, A soluk | sorun yok; *g* kuyruğu çizgiye değmez |
| `k/13-hyperframes-mini-soru-251.png` | son hâl: 4 pil, B yanık, D imleci | sorun yok |
| `k/koyu/…-240.5.png`, `k/koyu/…-251.png` | koyu tema | kontrast iyi; turuncu dolgu üstünde koyu yazı + tik |

Taşma, kesik yazı, üst üste binme, okunmaz kontrast, boş kare, platform bandında öğe yok.

Düzeltme turları (2/4):
1. agy çıktısı sonrası (şef, Edit): `230,68` ve `235,48` sabitleri türetilmiş zamana döndü; `MINI QUESTION` vurgu → `murekkep`
   (sözleşme: açık temada vurgu yazısı ≈ 2,3:1); boşluk çizgisi taban + 0,48 × boy (sözleşme kalıcı altçizgi kuralı).
2. Kare incelemesi sonrası (şef, Edit): A pilinde *temporary* y kuyruğu sağ alt köşe eğrisine ≈ 8 px yaklaşıyordu; ok ile *he* /
   *month* arası dardı → parça arası 14 → 18, ok 56 → 52, sağ iç pay 24 → 34 (A pili sağ ucu 1031 ≤ 1032). Kök tabanları +8 px
   (etiket ile satır 1 arası açıldı). SPEC.md aynı değerlere çekildi.

## agy koşu özeti

`agy-filo tek --rol kod` · gemini-3.8-flash-high · başarılı · 282 sn · özet `/home/sef/.claude/canavar/agy-filo/20261115-122642`.
agy yalnız `uret.py`'yi yazdı (mtime ile denetlendi). Özetin "değişen" listesindeki öbür dosyalar paralel oturumlarındır (06, 07, sözleşme).

## Açık noktalar

1. **Bant 220,33–229,33 arası alt yarısı boş (≈ 9 sn).** BRIEF kartı y 380–700'e sabitliyor, şıklar `Beş` sözcüğünde (229,33) geliyor.
   Kart dolu, boş çerçeve yok; ama "alt yarı boş" bulgusuna benzer. Öneri (şef kararı): kart bant ortasında başlar, 229,33'te yukarı toplanır (sahne 10 kalıbı).
2. **Balon satır 2 `Yaşamak kalıcı bir durum.` 25 karakter.** BRIEF bölümü aynen uygulandı (24 karakter kuralını nokta aşıyor).
   3 satır 1190–1390 bandına Caveat 64'te sığmaz.
3. **Altyazı dilimi cümle ortasından bölünüyor.** Ortak `altyazi_dilimleri` açgözlü 2 satır doldurur: `durum. Doğru cevap …` (241,83) ve
   `başına cümle kuramaz.` (250,03). Kural BRIEF §2.4 / `kunye.js` ile aynı; cümle sınırına göre bölme ortak düzeltme ister.
4. **Karaoke yorumu.** İstemdeki "altyazı + karaoke alt bantta": altyazı alt bantta; karaoke kökteki okunan sözcüğün 0,3 sn sarı altı
   (03.11 `karaoke:"kart"` kuralı). Altyazı bandında sözcük vurgusu yok (ortak kalıp çizmiyor).
5. **Doğru şık rengi.** İstem şablonu "doğru şık yeşil" der; BRIEF §3 satır 13 ve 13.11 QA "ham yeşil yok" der. BRIEF uygulandı.
   Tik `pilMetin` için sahnede `<style id="pm13">` kuralı var: hf_tema `[stroke="#1b1a17"]`'yi zemine boyar, kural olmasa açık temada tik açık renk olurdu.
6. **`ikincil`e dönüş ikiz yolla.** GSAP ile stroke rengi değiştirmek satır içi renk yazar, temayı ezer; bu yüzden her sarı yolun `ikincil` ikizi var.
7. **Pillerde ✗ yok.** BRIEF dikey pil metinleri çarpısız; elenme satırın soluklaşmasıyla görünür (yatayda ✗ vardı).
8. **calistir.sh yakalama.** HyperFrames sahnesi `yakala.py` kullanmaz; çözünürlük `data-width/height` (1080×1920) ile gelir. Render yapılmadı
   (`video.mp4`, `kontrol.png` yok). `__pycache__/` derlemeden kaldı, silinmedi. Birim testi yok (HF sahneleri test taşımıyor); doğrulama kapı + kare.
