# Sahne 14 · kapanış DİKEY (HyperFrames 1080×1920, 431 kare, 251,27–264,64 + 0,5 sn kuyruk; cümle 18; geçişsiz)

Durum: istem D-dikey (15.11.2026, srv21). Önizleme hazırlığı `ONIZLE_YALNIZ=1` ile koştu. Render yok, commit yok.
Tema: koyu

| Kapı | Sonuç |
|---|---|
| `qa-yerel.sh` çıkış kodu | 0 (tur 1 ve tur 2) |
| Çakışma kapısı | çakışma yok (55 örnek, 7610 kutu) |
| Kare bakışı (açık 3 + koyu 1 + ara 7) | taşma, kesik yazı, binme, okunmaz kontrast, boş kare, platform bandında öğe YOK |
| Düzeltme turu | 1 (ok çizimi: uç çizgiyle aynı anda beliriyordu → iki yol) |

## Olay listesi (cümle 18; yerel sn = küresel − 251,27)

| # | Olay | Küresel sn | Yerel sn (kare) | Cümle sözcüğü (i) | Ses olayı |
|---|---|---|---|---|---|
| 0 | HUD tam: logo 48,48 387×96 · ders 2 satır (Fredoka 56, taban 212/276) · rozet `YDT · BASIC` · çip `Next lesson` | — | kare 0'dan | — | — |
| 1 | altyazı dilim 0 (2 satır) | 251,77 | 0,50 (15) | Dil (0) − 0,05 | — |
| 2 | `MEANING` kinetik (x 96, taban 505, Fredoka 700 120) | 251,82 | 0,55 (16) | Dil (0) | `tik` |
| 3 | `FIRST` kinetik | 252,14 | 0,87 (26) | sınavında (1) | `tik` |
| 4 | sarı alt çizgi (taban + 34, kalınlık 11, 0,45 sn) | 252,62 | 1,35 (40) | boşluğu (2) | `cizgi` |
| 5 | numara halkaları 1 · 2 · 3 (r 46, ikincil, 0,12 sn ara); numara Fredoka 64 | 253,58 | 2,31 (69) | üç (4) | `cizgi` ×3 |
| 6 | soru 1 `general` · `or` · `now?` (Caveat 88, x 224, taban 690) | 254,78 / 255,18 / 255,66 | 3,51 / 3,91 / 4,39 | Genel (7) / mi (8) / şu (9) | `tik` ×2 |
| 7 | soru 2 `permanent` · `or` · `temporary?` (taban 840) | 256,54 / 257,02 / 257,42 | 5,27 / 5,75 / 6,15 | Kalıcı (12) / mı (13) / geçici (14) | `tik` ×2 |
| 8 | altyazı dilim 0 → dilim 1 (tek karede; üst üste binme yok) | 258,25 | 6,98 (209) | Tarife (16) − 0,05 | — |
| 9 | soru 3 `timetable` · `or` · `plan?` (taban 990) | 258,30 / 258,86 / 259,26 | 7,03 / 7,59 / 7,99 | Tarife (16) / mi (17) / plan (18) | `tik` ×2 |
| 10 | kart çerçevesi (x 48–1032, y 1100–1380, ikincil) | 260,30 | 9,03 (271) | Sonraki (20) | `cizgi` |
| 11 | `Next lesson` (Lexend 500 56, ikincil, taban 1196) | 260,70 | 9,43 (283) | derste (21) | — |
| 12 | `Stative` (Fredoka 700 96, taban 1316) | 261,18 | 9,91 (297) | -ing (22) | `tik` |
| 13 | `Verbs` | 262,06 | 10,79 (324) | fiilleri (24) | `tik` |
| 14 | sarı ok: çizgi 0,22 sn, uç +0,20 sn (x 770 → 968, y 1282) | 262,50 | 11,23 (337) | görüyoruz (25) | `cizgi` |
| 15 | altyazı dilim 1 söner (t1 + 0,35) | 264,57 | 13,30 (399) | — | — |
| 16 | durgun son düzen; kare 401'den sonrası kuyruk | — | 11,53 → 14,37 | Görüşürüz (26) olaysız | — |

`olaylar.json`: 16 ses olayı (6 `cizgi`, 10 `tik`), en büyük kare 337 < 419. `Y.kontrol`: hareket 0,55–11,53 sn; ilk ve son 12 kare durgun.
Sapma 0,00 sn: her olay sözcüğün t0'ında (`T(i, bas)` sözcük kayarsa durur).

## Kapı sonucu (son koşu)
```
== KAPI
14-hyperframes-kapanis | çakışma yok (55 örnek, 7610 kutu)
== KARE (açık)  256 · 260.1 · 263.6
== KARE (koyu)  263
kapı çıkış kodu: 0
```
Komut: `cd K && bash araclar/qa-yerel.sh 02-04-ydt-temel-dikey 14-hyperframes-kapanis 256.0,260.1,263.6 263.0 --hazirla`
(256,0 = başlık + alt çizgi + halkalar + soru 1 bitti · 260,1 = üç soru bitti, kart yok · 263,6 = son düzen; koyu 263,0 = son düzen).

## Bakılan kareler ve bulgu

| Kare | Bulgu |
|---|---|
| `k/14-hyperframes-kapanis-256.png` | HUD tam ve okunur; MEANING FIRST sağ uç ≈ 962; alt çizgi altta; halkalar 1–3, soru 1 tam; altyazı dilim 0 (2 satır) |
| `k/14-hyperframes-kapanis-260.1.png` | üç soru satırı; `temporary?` soru işareti sağ ucu ≈ 1022 (≤ 1032); `or` ikincil; altyazı dilim 1 |
| `k/14-hyperframes-kapanis-263.6.png` | son düzen: kart 1100–1380, `Stative Verbs` ↔ ok arası ≈ 80 px; kart altı ↔ altyazı ≈ 40 px; platform bandı boş |
| `k/koyu/14-hyperframes-kapanis-263.png` | koyu: rozet `#f2a93b` + koyu yazı, alt çizgi/ok vurgu, krem yazı; kontrast yeterli |
| `k/ara/` 251,4 · 253,75 · 258,28 · 262,62 (kontak `k/ara/kontak-ara.png`) | 251,4: HUD + boş bant (geçiş altı, ilk söz 251,82) · 253,75: halka çiziliyor, numara açılıyor · 258,28: tek altyazı dilimi · 262,62 (tur 1): ok ucu çizgiyle aynı anda beliriyordu → düzeltildi |
| `k/ara/` 262,58 · 262,66 · 262,74 (kontak `k/ara/kontak-ok.png`, tur 2) | ok önce çizgi, sonra uç; çakışma yok |

## Kod yolu
- Şef: `SPEC.md` yazdı; dikey sahne 01 `yardim.py`, `olay.py`, `calistir.sh` kopyalandı. `calistir.sh` Edit ile uyarlandı (başlık, `KARE=431`;
  `ONIZLE_YALNIZ`, `yuk1`, koşullu Homebrew PATH, `1080 1920` kontak sahne 01 kalıbından).
- agy (`agy-filo tek --rol kod`, gemini-3.8-flash-high, 184 sn, başarılı): `yardim.py` `kunye_svg(bolum)` tam dikey HUD (`ku-ders`, `ku-rz`,
  `ku-bolum`), `uret.py` yazıldı. Özet: `/home/sef/.claude/canavar/agy-filo/20261115-122311`.
- Şef okuması: SPEC'e uyuyor. Tek düzeltme Edit ile (QA sonrası): ok `el_ok` yolu iki yola bölündü (`kok` çizgi, `kok2` uç).

## Açık noktalar
1. **Ortak `el_ok` kusuru.** Chrome kesik çizgi desenini her alt yolda yeniden başlatır; `el_ok` (çizgi + uç tek yol) çizilirken uç baştan görünür.
   Bu sahnede yerel düzeltildi. `el_ok` kullanan öteki HF sahneleri (yatay 14 dahil) aynı 0,3 sn'lik geçici görüntüyü taşır; ortak düzeltme ayrı karar.
2. **Altyazı boyu 44.** İstem "yazı tabanı ≥ 50" der; BRIEF §2 ve `ortak/kunye.js` altyazıyı 44 yazar. 14 sahnenin tutarlılığı için BRIEF izlendi (sahne 01 ile aynı).
3. **Altyazı bandında karaoke yok.** Nadir 03.11 "karaoke şeridi yok"; sahne 01 ile aynı. Sözcükler söylendiği anda ekranda yazılır.
4. **`Next lesson` kart başlığı Lexend 500 56 `ikincil`.** BRIEF §3 satır 14 bunu ister; `present-continuous-dikey` §0 "ikincil yalnız ≥ 72" der. BRIEF izlendi.
5. **Kart yuvası 251,27–260,30 boş.** 1100–1380 arası 9 sn çizimsiz (çerçeve yok, boş çerçeve kuralı ihlal değil); kart sözü gelince çizilir.
6. "Görüşürüz." (263,42) olaysız (yatayla aynı; karşılığı olan görsel yok). Çip ve kart başlığı ikisi de `Next lesson` (BRIEF).
7. Birim testi yok (HF sahneleri test taşımıyor); doğrulama kapı + kare. `nesneler.json` / `zamanlar.json` yok (sahne 01 gibi; zaman `zaman.json` + `sozcukler.json`).
8. agy-filo "değişen" listesi `06-hyperframes-soru1`, `07-hyperframes-kural` dosyalarını da gösterdi: başka oturumların eşzamanlı işi; bu sahne o dosyalara dokunmadı.
9. Render kısmı (`calistir.sh` sonu, telefon kontağı) koşmadı: istem render yasaklar. `uret.py` tek başına koşulursa `index.html` tema dönüşümsüz yazılır; hazırlık `calistir.sh` ile.

Dosyalar: `SPEC.md`, `uret.py`, `yardim.py`, `olay.py`, `calistir.sh`, `proje/index.html`, `olaylar.json`, `k/`, `RAPOR.md`.
