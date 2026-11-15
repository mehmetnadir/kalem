# Sahne 01 · kanca (huni v2; HyperFrames DİKEY 1080×1920, 102 kare, 0,00–3,00 sn + 12 kare geçiş payı)

| Ölçüm | Değer |
|---|---|
| Durum | yazıldı (istem D-V2, 15.11.2026, srv21). Önizleme hazırlığı `ONIZLE_YALNIZ=1`. mp4 yok, commit yok |
| Tema | açık (koyu kareyle de denetlendi; `proje/` son hâli açık) |
| qa-yerel | çıkış 0 · `01-hyperframes-kanca \| çakışma yok (13 örnek, 6133 kutu)` |
| Çakışma kapısı (ayrı koşu) | çıkış 0 · 0 uyarı |
| Metin taraması (`tam ders\|dakika`) | boş (grep çıkış 1) |
| Kanal katmanı | 6 karede aynı (piksel kenarı): açık logo x 60–241, y 297–332 · yazı x 263–598, y 295–341; koyu ±1 px (kenar süzgeci) |
| Kapak A | `kapak-a.png` = `kapak.png` (md5 `61ef66f4cc5c7d87…`), `k/koyu/kapak-a-koyu.png` (`bb671f16a98e7fe4…`); 1080×1920; t 0,90; altyazısız; izin 644 |

Kod yolu: emsal `02-04-ydt-temel-s1/sahneler/01-hyperframes-kapak/` → `cp -p` `calistir.sh`, `olay.py`, `yardim.py` + küçük Edit
(`yardim.py` KONU `Simple Present`; `olay.py` olay listesi; `calistir.sh` başlık ve kapak saniyesi). Şef `SPEC.md` yazdı → agy `uret.py`
yazdı → şef okudu, 2 Edit yaptı, koşturdu, kapıya soktu. Veri (kod değil): `zamanlar.json`, `nesneler.json` (`[]`), `cizim/ogrenci.json`
(katalogdan çıkarıldı), `cizim/KAYNAK.md`.

Şef Edit'leri (`uret.py`): (1) tik 2. ve 3. noktasında x kayması `TIK_KAY[i][1]` → `TIK_KAY[i][0]` (denetim doğru öğeyi ölçüyordu, çizim
yanlış öğeyi kullanıyordu); (2) yasak söz `assert` satırı kaldırıldı: satırın kendisi kapı 3 grep'ine takılıyordu (SPEC §8.7 güncellendi).

## İçerik
İlk kare = kapak A: kanal katmanı (logo + `@ydspublishing`), künye `Simple Present` (Fredoka 34) + `YDT · BASIC` (x 309,7–513,2), başlık
`USUALLY` / `= ALIŞKANLIK` (B = 137, iki satır aynı boy; satır 2 sarı hapta x 63–957, y 624–794). Görsel bandı: solda takvim yaprağı
(Tabler `calendar` biçimi: yaprak x 60–440, y 918–1310, 2 halka, başlık çizgisi; 5 el çizimi gün kutusu 100×100, 3 + 2 dizilim), sağda
öğrenci figürü (`kadro.ogrenci` saç/yüz/gözlük + `PointingFingerWB` gövdesi, aynalı, kit y 1200'de kırpık; x 465–954, y 949–1376; parmak
ucu ≈ (483, 1131) takvime bakar). Karakter görseli (`karakter.png`) bu sahnede yok (kapak C'de).

## Olay listesi (küresel sn = yerel sn)
| Olay | Kare / sn | Cümle sözcüğü | `olaylar.json` |
|---|---|---|---|
| kapak tam görünür (kanal, künye son yerinde, başlık, takvim 5 boş kutu, figür) | 0 / 0,00 | söz öncesi | — |
| tik 1–4 kalemle (`sine.inOut`, 0,11 sn) | 9 · 13 · 17 · 21 / 0,30 · 0,43 · 0,56 · 0,69 (son 0,80'de biter) | söz öncesi | `cizgi` 0,5 × 4 |
| KAPAK KARESİ (4 tik bitmiş, ses yok) | 27 / 0,90 | — | — |
| altyazı dilimi açılır (tek satır, orta x 510, taban 1484) | 28,5 / 0,95 | Usually t0 − 0,05 | `tik` 0,4 (kare 28) |
| karaoke altçizgisi (vurgu, 0,15 sn çizim) | 30 · 54 · 78 · 88 / 1,00 · 1,80 · 2,60 · 2,92 | Usually · görünce · hangi · zaman? | — |
| takvim + figür solar (`power2.in`) | 72–90 / 2,40–3,00 | — | — |
| uçuş: `#baslik` küçülür (ölçek 0,20, `power3.out` 0,45 sn), künye satırının sağ boş bölümüne gider (merkez 738,6 / 405; `power3.inOut` 0,60 sn) | 72–90 / 2,40–3,00 | — | `parilti` 0,5 (kare 72) |
| başlık solar (`power2.in`), 3,00'te opaklık 0 | 81–90 / 2,70–3,00 | — | — |
| durgun: kanal + künye + altyazı; içerik bandı boş (sahne 02 kare 0 ile aynı) | 90–101 / 3,00–3,40 | `zaman?` 3,48'e dek → sahne 02 | — |

`olaylar.json`: 6 olay, hepsi kare < 90. Kanal ve künyeye tween yok (`#kunye`, `#kanal`, `#ku-konu`, `#rz0` script'te geçmez).
`uret.py` 6 denetim maddesini assert eder (başlık, takvim, figür, dikey sıra, uçuş örneklemesi rozet/konu/kanal × başlık kutusu, zaman).

## Kapı çıktısı (son koşu)
```
== HAZIRLA → olay 6 · önizleme hazır
== KAPI
01-hyperframes-kanca | çakışma yok (13 örnek, 6133 kutu)
== KARE (açık) 0 · 1.5 · 2.95   == KARE (koyu) 1.5
kapı çıkış kodu: 0
== ÇAKIŞMA KAPISI (ayrı): 01-hyperframes-kanca | çakışma yok (13 örnek, 6133 kutu) · KAPI_RC=0
== METİN TARAMASI: GREP_RC=1 (eşleşme yok)
```
Komutlar: `bash araclar/qa-yerel.sh simple-present-temel-s2 01-hyperframes-kanca 0.00,1.50,2.95 1.50 --hazirla` ·
`node araclar/cakisma-kapisi.mjs simple-present-temel-s2 --sahne 01-hyperframes-kanca --port 41333 --sunucu 41022`.

## Bakılan kareler ve bulgu
| Kare | Bulgu |
|---|---|
| `k/01-hyperframes-kanca-0.png` | kapak tam; 5 kutu boş (tikler henüz yok); taşma, kesik yazı, üst üste binme yok |
| `k/01-hyperframes-kanca-1.5.png`, `k/koyu/01-hyperframes-kanca-1.5.png` | 4 tik + 1 boş kutu; altyazı tek satır x ≈ 176–842, `Usually` altında karaoke çizgisi; iki temada okunur |
| `k/01-hyperframes-kanca-2.95.png` | başlık künye satırının sağında (x ≈ 650–828, y ≈ 372–437), rozetle arası ≈ 135 px; takvim + figür ≈ %23 opaklıkta solarken; `zaman?` karaokesi başlıyor |
| `k/ara/` 2,45 · 2,55 · 2,65 · 2,75 · 2,85 · 3,0 (kontak `k/ara/kontak-ucus.png`) | başlık önce yerinde küçülür, sonra sağ üste çıkar; hiçbir karede rozet, konu ya da kanalla kesişmez; 3,00'te içerik bandı boş |
| `k/ka-acik/at-0.9s.png`, `k/ka-koyu/at-0.9s.png` | altyazı yok; kanal, künye, başlık, 4 tik, figür tam |

Piksel ölçümü (kenar süzgeci, eşik 40) 6 karede: 0–280 boş, 1570–1920 boş, x 962–1078 (y 280–1570) boş. Kapak A'da 1385–1920 boş.

## Kapak A (S1-KAPAK-A yöntemi)
`ONIZLE_YALNIZ=1 bash calistir.sh --tema <t>` → `cp -a proje/. proje-ka/` → `proje-ka/index.html` ilk `</style>` önüne
`#altyazi{display:none}` → `hyperframes snapshot . --at 0.90 --no-end --keep -o <S>/k/ka-<t>` (koyu önce, açık sonra; `proje/` açık kalır).
Açık → paket kökü `kapak-a.png`, `cp -p` → `kapak.png`; koyu → `k/koyu/kapak-a-koyu.png`. Snapshot dosyası 600 izinle çıkar → emsal gibi 644.

## agy koşu özeti
| Şerit | Dosya | Süre | Özet |
|---|---|---|---|
| tek | `uret.py` (SPEC) | 346 sn, tek tur | `~/.claude/canavar/agy-filo/20261115-192744` |
Rol `kod` (gemini-3.8-flash-high). "değişen" listesinde başka paketlerin dosyaları göründü (`02-04-ydt-temel-s2/08`, `sozlesme.md`): aynı worktree'deki
paralel oturumlar; ajan yalnız `uret.py` yazdı.

## Açık noktalar
1. Figür gövdesi kadronun `Sitting` gövdesi değil: işaret pozu için aynı kitin `PointingFingerWB` gövdesi (sözleşme satırı 66 emsali);
   yatay aynalı, kit y 1200'de kırpık → gövde alt kenarı y 1376'da düz biter (kitin bel üstü görünümü).
2. Tikler mürekkep renginde (sarı değil): sarı hap ve rozet tek vurguyu taşır; açık zeminde ince sarı çizgi zayıf okunur.
3. Karaoke altçizgisi vurgu rengi (emsal 03 kalıbı). Skill klişe #10 "sarı dolgu" der; kanal bütünlüğü için emsal izlendi.
4. 2,95 karesinde solma sürer (`power2.in`): takvim + figür ≈ %23, başlık ≈ %42; 3,00'te ikisi de 0.
5. Altyazı sahne sonuna (3,40) dek açık; `zaman?` sesi 3,48'de biter, sahne 02 altyazıyı devralır.
6. HF kutu adları `kunye:kanal:image0` / `kunye:kanal:text0` (emsal açık nokta 1 ile aynı).
7. Kovan kaydı ve sözleşme satırı yazılmadı (yazma kapsamı sahne dizini; durdurma kancası satır istemedi).
