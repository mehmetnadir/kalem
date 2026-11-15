# RAPOR — simple-present-temel-s2 · sahne 06-hyperframes-kapak-b (huni v2, durağan kapak B) · 15.11.2026

İstem: `../../uretim-tutanagi/istem/sahne/D-06-hyperframes-kapak-b.md`. Tasarım: `SPEC.md` (şef). Kod: `uret.py` (agy, rol `kod`).

| Kapı | Sonuç |
|---|---|
| `calistir.sh --tema acik` | rc 0 · `png,1080,1920` · `P/kapak-b.png` |
| `calistir.sh --tema koyu` | rc 0 · `png,1080,1920` · `k/koyu/kapak-b-koyu.png` |
| uret.py stdout | `index.html yazıldı 27035` · `S=116 BS=1.70 Q=24 uc=472,1040 sac_sag=449.6` (SPEC §6 assert'leri geçti) |
| Çakışma kapısı | rc 2 · `HATA sahne bulunamadı: 06-hyperframes-kapak-b` (beklenen: araç yalnız `sahneler[]` okur; durağan kare gözle + piksel ölçümüyle denetlendi) |
| Metin taraması (`tam ders\|dakika`, html/js/py) | boş (grep rc 1) |
| Kanal katmanı (piksel) | iki temada logo x 60–239 · y 298–330, `@ydspublishing` x 265–596 · y 296–339; kanal + künye bandı (y 280–450) `kapak-a.png` ile piksel farkı 0 |
| Boş bantlar (piksel) | iki temada y 0–280, y 1380–1920 ve x 960–1080 boş |

## Öğe listesi (`nesneler.json`, x,y w×h)

kanal 60,291 542×48 · kunye 60,386 453×48 · baslik 60,495 893×270 · bas 60,836 398×542 · balon 520,833 436×156 · kuyruk 470,894 56×148 ·
balon-yazi 605,876 264×72 · soru 734,1014 218×362.

- Başlık: `ALWAYS VARSA` / `HANGİ ZAMAN?` Fredoka 700 116, mürekkep, hapsız, sol hizalı x 60 (künye ile aynı sol kenar; seri pilotu 02-04-s2 kapak B kalıbı), zemin renkli 12 px kontur.
- Öğrenci başı: `ortak/cizim/peeps-kit/ogrenci-bas.svg` (3 yol, `kadro.ogrenci`), ölçek 1,70, kalem çizgisi 4 px; yüz sağa, balona bakar.
- Balon: ana ders sahne 06 `konusma_balonu()` el çizimi yolu; kuyruk sol alttan aşağı-sola, uç (472, 1040) yüz hizasında, saçtan 22 px uzakta. Yazı `always?` Fredoka 700 72.
- Soru işareti: Tabler `question-mark` (yerel `cizim/`, kaynak `cizim/KAYNAK.md`), 26 px çizgi, vurgu (açıkta `#d9900f`, koyuda `#f2a93b`); karenin tek sarısı (künye rozeti kanal katmanının parçası).
- Yok: karakter PNG, cevap, altyazı, çip, rakam, emoji, QR, "izle" düğmesi.

## Bakılan kareler ve bulgu

| Kare | Bulgu |
|---|---|
| `P/kapak-b.png` (açık; tek kare = ilk = orta = son) | taşma yok, kesik yazı yok, üst üste binme yok; `HANGİ` İ noktalı; kontrast iyi |
| `k/koyu/kapak-b-koyu.png` (koyu) | aynı yerleşim; çizgiler krem, `?` turuncu-sarı, logo şeffaf sürüm |
| kırpım x 380–980 · y 800–1100 (açık) | kuyruk saça ve gözlüğe değmiyor; yazı balonun ortasında; `?` balonun 25 px altında |

Düzeltme turu: 0 (ilk koşu kabul ölçütünü geçti).

## Kurulum (şef)

- `cp -p` emsal `02-04-ydt-temel-s1/sahneler/05-hyperframes-kapak-b/`: `calistir.sh`, `olay.py`, `yardim.py`, `zamanlar.json`; `cizim/question-mark.svg` ← `02-04-ydt-temel-s2/…/05-hyperframes-kapak-b/cizim/`.
- Edit: `yardim.py` docstring + `KONU = "Simple Present"`, `KONU_PARCA = ("Simple", "Present")`; `olay.py` docstring; `calistir.sh` başlık yorumu, paket adı
  yorumu ve `uret.py && olay.py` zinciri iki satıra bölündü (sözleşme: `set -e` zincirde uret.py hatasını yutar, eski index.html yakalanır).

## agy koşusu

`agy-filo tek --rol kod` · gemini-3.8-flash-high · 270 sn · başarılı · özet `/home/sef/.claude/canavar/agy-filo/20261115-194924`.
Şef kodu baştan sona okudu: SPEC'e uyuyor, düzeltme gerekmedi (0 tur).

## Açık noktalar

1. Görsel bandında alt orta boşluk (x ≈ 458–734, y ≈ 1042–1376) bilinçli: `?` balonun altında, baş solda; `?` boyu (218×362) seri pilotu (210×348) ile aynı ölçekte.
2. agy özetinin "değişen" listesinde paralel oturumların dosyaları var (`simple-present-temel-s1/…/07-hyperframes-kapak-c/`, `.claude/docs/sozlesme.md`);
   agy yalnız `uret.py` yazdığını bildirdi, bu dizinde zaman damgaları bunu doğruluyor. Bu oturum o dosyalara yazmadı.
3. Kovan kaydı yazılmadı (istem yazma kapsamı yalnız sahne dizini).
