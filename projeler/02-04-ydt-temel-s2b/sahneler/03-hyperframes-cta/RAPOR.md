# Sahne 03 çağrı · huni v2 (02-04-ydt-temel-s2, HyperFrames DİKEY 1080×1920, 230 kare, t_bas 22,75; cümle 4, öğrenci) · 15.11.2026

| Ölçüm | Sonuç |
|---|---|
| Ana kapak | `ortak/kapak/ana-kapak.png` + `ana-kapak-koyu.png` = `02-04-ydt-temel/kapak.png` + `kapak-koyu.png` (`cp -a`, 1920×1080) |
| Hazırlık | `ONIZLE_YALNIZ=1 calistir.sh --tema acik` (qa-yerel `--hazirla`); render yok |
| Çakışma kapısı | `03-hyperframes-cta \| çakışma yok (28 örnek, 2920 kutu)` · `kapı çıkış kodu: 0` |
| Metin taraması | `grep -rniE "tam ders\|dakika" … --exclude-dir=k` → boş (rc 1) |
| Kanal katmanı | 22,75 · 26,5 · 29,35 karelerinde aynı konumda (logo x 53,15 y 291–339, `@ydspublishing` x 263 taban 330) |
| Son kare | ana kapak kartı görünür (açık: sarı kapak; koyu 28,5: koyu kapak) |
| Yedek | v1 sahne: `~/Silinecekler/2026-11-15-huni-v2/02-04-ydt-temel-s2/sahneler/03-hyperframes-cta/` · v1 kareleri `…/03-hyperframes-cta-v1-kareler/` (taşındı) |

## Olay listesi (sahne içi sn = küresel − 22,75; çapa `sozcukler.json` cümle 4)

| Olay | Çapa | Küresel | Sahne içi | Kare | Hareket | Ses |
|---|---|---|---|---|---|---|
| kare 0 | — | 22,75 | 0,00 | 0 | kanal katmanı + künye; içerik boş | — |
| `Bitmedi,` | T(0) | 23,30 | 0,55 | 16 | kinetik (0,22 sn, `back.out(1.6)`) | tik 0,4 |
| `gel.` | T(1) | 24,26 | 1,51 | 45 | kinetik | tik 0,45 |
| kapak kartı | T(2) `Dersin` | 24,89 | 2,14 | 64 | opaklık + ölçek 0,96 → 1, 0,4 sn `power3.out` | vurus 0,7 |
| `@ydspublishing` hap | T(4) `YDS` | 26,17 | 3,42 | 103 | opaklık + ölçek 0,9 → 1, 0,3 sn | tik 0,6 |
| `· YouTube` | T(6) | 27,29 | 4,54 | 136 | kinetik | tik 0,4 |
| kuyruk | E(7) `kanalında.` | 28,49 | 5,74 → 7,67 | 172 → 230 | durgun | — |

İlk olay karesi 16 (SPEC 17): `round(0,55 × 30)` yarımı aşağı yuvarladı; olay sınırı (≥ 12) içinde.
Altyazı: yalnız cümle 4 (2 parça: 23,30–24,74 · 24,89–28,41); cümle 3'ün kuyruğu bu sahneye girmez.

## Yerleşim (px)

| Öğe | Değer |
|---|---|
| Kanal katmanı `#kanal` (`#kunye` içinde, tween yok) | logo `#logoimg` 193,49×48 x 53,15 y 291 · `#kanal-ad` Lexend 700 42 x 263 taban 330 |
| Künye | `Simple Present vs Present Continuous` Fredoka 700 34 (rozetle son x 868,2) · rozet `YDT · BASIC` x 664,6 w 203,6 y 386–434 |
| Giriş sözü | `Bitmedi,` + `gel.` Fredoka 700 96, x 60 / 432,3, taban 572 |
| Kapak kartı | 900×506, x 60–960, y 627–1133, rx 24 kırpma, mürekkep çerçeve 3; iki `<image>`, görünürlük tema CSS'i |
| Hap satırı | hap x 60–616,4 y 1170–1250 rx 40, `@ydspublishing` Lexend 700 64 · `· YouTube` Lexend 700 64 x 630,4 (sağ uç ≈ 956) |
| Altyazı | 1400–1550 bandı, `Y.altyazi_svg` (ortak kalıp, merkez 540, genişlik 984) |

## Bakılan kareler ve bulgu

| Kare | Bulgu |
|---|---|
| `k/03-hyperframes-cta-22.75.png` (açık) | yalnız kanal katmanı + künye; içerik ve altyazı boş |
| `k/03-hyperframes-cta-26.5.png` (açık) | giriş sözü, kapak kartı, hap; `· YouTube` henüz yok (27,29); altyazı 2 satır |
| `k/03-hyperframes-cta-29.35.png` (açık) | kuyruk: kart + giriş sözü + hap satırı yerinde; altyazı kapandı (28,76) |
| `k/koyu/03-hyperframes-cta-28.5.png` (koyu) | koyu kapak görseli, şeffaf logo, hap `#f2a93b`; okunur |

Taşma, kesik yazı, üst üste binme yok. İçerik x 960 sağına geçmez. 0–280 ve 1570–1920 boş.
Düzeltme turu 1: ilk koşuda açık tema koyu çıktı (zemin koyu, lacivert logo okunmuyordu). Neden: uret.py CSS'indeki
`#root.tema-acik #kapak-…` seçicisi `ortak/hf_tema.py`'nin "zaten çevrildi" bekçisini (`"#root.tema-acik" not in html`) tetikledi;
tema değişkenleri eklenmedi. Seçici `.tema-acik #kapak-…` oldu; ikinci koşuda dört kare doğru.

## agy koşu özeti

| Koşu | Model | Süre | Sonuç | Özet |
|---|---|---|---|---|
| `s2cta-yardim` (yardim.py, SPEC §2) | gemini-3.8-flash-high | 214 sn | başarılı | `/home/sef/.claude/canavar/agy-filo/20261115-184934` |
| `s2cta-uret` (uret.py, SPEC §3–§6) | gemini-3.8-flash-high | 211 sn | başarılı | `/home/sef/.claude/canavar/agy-filo/20261115-184937` |

Şef düzeltmesi: uret.py tema seçicisi (2 satır + 1 yorum satırı). `calistir.sh` şefte (KARE 230, ana kapak kopyası + yoksa
"ana kapak bekliyor" çıkışı, boyut denetimi `GEN=1080; YUK=1920`). agy özetindeki "değişen" listesi ortak worktree'deki
başka oturumların dosyalarını da sayar (S1, `-dikey`); bu iki koşunun yazdığı dosya yalnız `yardim.py` ve `uret.py`.

## Açık noktalar

1. Ana kapak görselinde rozet `YDT · TEMEL`, künyede `YDT · BASIC`: aynı karede iki dil (V2-C-RAPOR madde 3). Karar şef/Nadir.
2. Altyazı ortak kalıpla x ≈ 116–965 (en geniş satır): sağ uç 960'ı ≈ 5 px geçer (platform sağ bölgesi). Bütün sahneler
   `ortak/kunye.js` ile aynı genişliği (984) kullanır; değişiklik paket düzeyinde.
3. Ana kapak görseli kendi sarısını taşır (açık temada sarı zemin); "tek sarı vurgu" bu sahnede hap + kapak görseli. Kapak, standart gereği görünür (§1 kural 7).
4. Kanal katmanı kutu adı çakışma kapısında `kunye:kanal:image0` / `kunye:kanal:text0` (tür `kunye`); BRIEF `kunye:kanal` der.
5. Ses kapısı (huni v2 §7 madde 4) bu sahnenin işi değil; V2-C-RAPOR: çağrı parçası öğrenci sesi, Whisper 1,00.
