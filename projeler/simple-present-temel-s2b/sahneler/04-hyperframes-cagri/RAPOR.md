# Sahne 04 Çağrı — huni v2 (simple-present-temel-s2, HyperFrames DİKEY 1080×1920, 230 kare, t_bas 19,07; cümle 4 öğrenci)

| Kapı | Sonuç |
|---|---|
| `qa-yerel.sh … 19.15,23.00,25.68 25.68 --hazirla` | çıkış 0 · `04-hyperframes-cagri \| çakışma yok (28 örnek, 4193 kutu)` · `kapı çıkış kodu: 0` |
| `cakisma-kapisi.mjs --sahne 04-hyperframes-cagri --port 41333 --sunucu 41022` | çıkış 0 · `04-hyperframes-cagri \| çakışma yok (28 örnek, 4193 kutu)` · 0 uyarı |
| `grep -rniE 'tam ders\|dakika'` (html/js/py) | boş (grep çıkış 1) |
| Kanal katmanı (piksel ölçümü, 4 QA karesi) | 4 karede aynı: logo mürekkebi x 60–239, y 298–330 (resim kutusu 53,2–246,7 × 291–339) · `@ydspublishing` x 264–595, y 296–339 (taban 330) |
| Boş bölgeler (piksel ölçümü, 4 QA karesi) | 0–280 boş · 1570–1920 boş · sağ 963–1080 (y 280–1570) içerik yok |
| Ana kapak (standart §7 madde 5) | son karede görünür: açık `ana-kapak.png`, koyu `ana-kapak-koyu.png` |

Durum: yazıldı, önizleme hazır (`ONIZLE_YALNIZ=1`, son hazırlık AÇIK tema). Render yok. Commit yok.

## Dosyalar
- Emsal `02-04-ydt-temel-s1/sahneler/03-hyperframes-cta/` → `cp -p`: `calistir.sh`, `olay.py`, `yardim.py`, `uret.py`.
- `olay.py`: değişiklik yok.
- `yardim.py` (Edit 1 satır): `KONU = "Simple Present"` (künye BRIEF-S2; `kunye_svg()` emsalle aynı).
- `calistir.sh` (Edit): başlık, `KARE=230`, kapak yorum satırı, `uret.py` ve `olay.py` ayrı satır (`a && b` zincirinde `set -e` `uret.py` hatasını yutar; sözleşme 15.11), denetim kareleri (render içindir, koşulmadı).
- `uret.py` (Edit): başlık, `T_BAS`/`KARE` yorumları, sözcük çapaları (`Gerisi` → `Bitmedi,`, `bizde` → `gel`; kimlikler `#bitmedi`, `#gel`), ana kapak iki `<image>` (`#kapakA` açık, `#kapakK` koyu) + CSS `#kapakA{display:none}` · `.tema-acik #kapakA{display:inline}` · `.tema-acik #kapakK{display:none}`; emsaldeki MutationObserver betiği çıktı; `"#root.tema-acik" not in html` assert'i.
- `proje/assets/`: emsalden kopyalanmadı (emsal kapağı 02-04 dersinindir). `calistir.sh` logoyu `ortak/logo/`, ana kapağı `ortak/kapak/` (S2) dizininden kopyalar; yazı tiplerini `uret.py` kopyalar.
- Üretilen: `proje/index.html`, `zamanlar.json`, `olaylar.json` (4 ses olayı), `k/*.png`.
- Ana kapak dosyaları: `ortak/kapak/ana-kapak.png`, `ana-kapak-koyu.png` var (S2-C, 18:40–18:41).

## Yerleşim
| Öğe | Yazı · boy | Konum |
|---|---|---|
| Kanal | logo + `@ydspublishing` Lexend 700 42 | BRIEF-S2 tablosu; `#kunye > #kanal`, opaklık 1, animasyon yok |
| Künye | `Simple Present` Fredoka 700 34 + rozet `YDT · BASIC` Lexend 700 26 | taban 420; hap 386–434, x 309,7–513,2 |
| `Bitmedi, gel.` | Fredoka 700 96 (genişlik 527) | x 60, taban 560 (≈ 489–581); `gel.` x 432,3 |
| Ana kapak kartı | 16:9, 900×506 | x 60–960, y 620–1126, köşe 24, mürekkep kenar 4 px |
| `@ydspublishing` hapı + `· YouTube` | Lexend 700 56 | hap x 60–567,9, y 1160–1240 (tek vurgu; açık dolgu `vurguDolgu`, yazı `pilMetin`); `· YouTube` x 585,9–870,9, taban 1220 |
| Altyazı + karaoke | Lexend 500 44 | 1400–1550, orta x 510, en çok 2 satır; okunan sözcük altında vurgu çizgisi |

## Olay listesi (yerel sn = küresel − 19,07; zaman `sozcukler.json` cümle 4 çapasından, `T(i, bas)` assert'li)
| Olay | Kare · yerel (küresel) | Cümle 4 sözcüğü |
|---|---|---|
| ana kapak kartı girer (ölçek 0,94 → 1 0,50 sn + saydamlık 0,25 sn) | 0 · 0,00 (19,07) → 0,50 (19,57) | sahne başı |
| `Bitmedi,` kinetik (0,22 sn, `back.out(1.6)`) | 16 · 0,55 (19,62) | Bitmedi, |
| `gel.` kinetik | 45 · 1,51 (20,58) | gel. |
| `@ydspublishing` hapı girer (ölçek 0,9 → 1, 0,30 sn) | 103 · 3,42 (22,49) | YDS |
| `· YouTube` girer (x −12 → 0, 0,30 sn) | 136 · 4,54 (23,61) | YouTube |
| durgun kuyruk | 172 · 5,74 (24,81) → 230 | kanalında. sonu |

Ses olayları (`olaylar.json`): kare 12 vurus 0,6 · 16 tik 0,4 · 103 tik 0,6 · 136 tik 0,4.
Altyazı: yalnız cümle 4 (2 parça: `Bitmedi, gel.` 0,50–2,09 · `Dersin tamamı …` 2,09–6,09 yerel); karaoke çizgisi her sözcüğün t0'ında 0,15 sn'de çizilir, sonraki sözcükte söner.

## Bakılan kareler
| Kare | Bulgu |
|---|---|
| `k/04-hyperframes-cagri-19.15.png` | kanal + künye tam; kart girişte (yarı saydam, küçük ölçek). Altyazı yok. Taşma yok. |
| `k/04-hyperframes-cagri-20.2.png` (ek) | `Bitmedi,` tam, `gel.` henüz yok; kart tam; altyazı 1 satır, `Bitmedi` altında karaoke çizgisi (x 372–545). |
| `k/04-hyperframes-cagri-22.7.png` (ek) | hap girişte; altyazı 2 satır, `YDS` altında karaoke çizgisi (x 406–502). |
| `k/04-hyperframes-cagri-23.png` | `Bitmedi, gel.`, kart, hap; `· YouTube` henüz yok (23,61); altyazı 2 satır x ≈ 80–937. Karaoke çizgisi bu anda yok: 23,00 = kare 117,9, `Publishing` t0 22,97 sınırına düşer (önceki çizgi söner, yeni çizgi 0 uzunlukta). 22,70 ve 20,20 ek kareleri çizgiyi doğruladı. |
| `k/04-hyperframes-cagri-25.68.png` | son kare: bütün öğeler tam; altyazı kapalı (kuyruk). Üst üste binme yok. Ana kapak görünür. |
| `k/koyu/04-hyperframes-cagri-25.68.png` | koyu zemin, koyu kapak (`ana-kapak-koyu.png`) seçildi; şeffaf logo; hap ve rozet koyu vurgu dolgusu; kontrast okunur. |
| `k/koyu/04-hyperframes-cagri-22.7.png` (ek) | koyu temada karaoke çizgisi aynı yerde (x 406–502). |

Taşma, kesik yazı, okunmaz kontrast, boş kare yok. 0–280 ve 1570–1920 boş; sağ 960–1080 bölgesinde içerik yok. Düzeltme turu: 0.

## agy koşu özeti
- agy koşusu yok. Değişiklik küçük Edit sınırında kaldı (metin, sözcük çapası, kapak yolu, künye adı); yeni düzen ve yeni olay mantığı yok, bu yüzden `SPEC.md` yazılmadı.

## Açık noktalar
1. Ana kapak görselinde rozet `YDT · TEMEL`, künyede `YDT · BASIC`: aynı karede iki seviye adı (emsal S1 ve 02-04-s2 raporlarındaki açık nokta). Karar şefte.
2. Ana kapak görseli açık temada kendi sarı zeminini taşır; karede sarı = hap + kapak görseli (standart §1 kural 7 gereği görünür).
3. Kuyruk: BRIEF cümle bitişi 24,73; `kanalında.` t1 24,81 (ElevenLabs hizalaması, ≤ 0,08 sn). Durgun kuyruk 24,81'de başlar; altyazı 25,16'da (24,81 + 0,35) söner, hareket yok.
4. Sahne başında (kare 0–7) kart henüz saydam; geçiş (`gecis_kare` 12) bu aralığı örter. mp4 birleştirmede bakılmalı.
5. Kanal katmanı kutu adı çakışma kapısında `kunye:kanal:image0` / `kunye:kanal:text0` (tür `kunye`); BRIEF `kunye:kanal` der (emsalle aynı).
6. Ses kapısı (standart §7 madde 4) bu sahnenin işi değil; S2-C-RAPOR: cümle 4 öğrenci sesi, önbellekten.

Tema: acik (koyu kareler canlı tema geçişiyle çekildi).
