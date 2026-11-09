# Oynatıcı teslim kapısı v4 — K40 çözünürlük kontağı (09.11.2026)

Karar K40 (Nadir): tam ekran = tam pencere; yerel tam ekran peşinde koşulmaz; oynatıcı her çözünürlükte
görünümü doldurur. Ölçüm: `araclar/oynatici-kare.mjs --tamekran 1 --sahte 1` (iPhone yolu) ve `--olc` geometri.
Paket present-perfect-temel (yatay + dikey çifti), açık tema, t = 25 sn, başsız Chrome 9333 (Mac yükü 32–46).

| Görünüm | Sayfa kipi | Tam pencere kipi | Sonuç |
|---|---|---|---|
| iPhone dikey 390×844 (dokunma) | oynatıcı kenardan kenara, altında gezin + başlık | ko 390×844, sahne 390×693 ortada, siyah bant 75 px | GEÇTİ (düzeltme sonrası) |
| iPhone yatay 844×390 (dokunma) | **tiyatro**: başlık gizli, oynatıcı 693×390 ortada, tam ekran düğmesi görünür | ko 844×390, sahne 693×390 | GEÇTİ (düzeltme sonrası) |
| Android dikey 360×800 (dokunma) | iPhone ile aynı düzen | ko 360×800, sahne 360×640 | GEÇTİ (düzeltme sonrası) |
| Tablet yatay 1024×768 | oynatıcı + sağda bölümler | ko 1024×768, sahne 1024×576 | GEÇTİ |
| Tablet dikey 768×1024 | dikey paket 440 px ortada, altında bölümler | ko 768×1024, sahne 576×1024 | GEÇTİ (düzeltme sonrası) |
| Masaüstü 1440×900 | iki sütun | ko 1440×900, sahne 1440×810 | GEÇTİ |

## Bulunan ve düzeltilen (0.4.3)

1. **Dikey görünümlerde tam pencere hiç görünmüyordu.** Ev sayfası oynatıcıyı grid'de `justify-self:center` ile
   hizalıyor; konumlu (`position:fixed; inset:0`) kutu `width:auto` ile içeriğe büzülür, `container-type:inline-size`
   içerik ölçüsünü 0 yapar → kutu 0 px (`--olc` ölçümü: rect 195,0,0,844). Çözüm: sahte kipte `width/height:100%`,
   `justify-self/align-self:stretch`, hepsi `!important`.
2. **Telefon yatayda oynatıcı ekrandan taşıyordu**, kontrol çubuğu ve tam ekran düğmesi görünmüyordu (sayfa 64 px
   başlık + 16:9 oynatıcı 450 px > 390 px). Çözüm: `index.html` tiyatro kuralı `(orientation:landscape) and
   (max-height:520px)`: başlık gizli, oynatıcı `min(100%, 100dvh·ar)` ortada, sayfa altta kaydırılır.
3. Başsız Chrome'da gerçek Fullscreen API 800×600 pencereye düşer; telefon ölçümü için `--sahte 1` eklendi
   (Fullscreen API kapatılır, iPhone yolu zorlanır).

## Kapı maddeleri

| # | Madde | Sonuç | Kanıt |
|---|---|---|---|
| 1 | Ekran görüntüsü masaüstü + telefon | GEÇTİ | `scratchpad/oynatici-kare/k40-*.png`, `k40b-*.png` (12 + 5) |
| 2 | Emoji taraması | GEÇTİ | SVG simgeler; CSS/JS/HTML değişikliklerinde emoji yok |
| 3 | Yapay görünüm | GEÇTİ | değişiklik yerleşim; renk/yazı tipi değişmedi |
| 4 | Hareket / JS kapalı | GEÇTİ | kurallar CSS; `prefers-reduced-motion` korunur |
| 5 | Erişilebilirlik | GEÇTİ | kontrol çubuğu her görünümde görünür, düğme ≥ 44 px dokunmada |
| 6 | Metin | GEÇTİ | sözlükten (0.4.1) |
| 7 | Algılanan hız | — | temiz yük ölçümü bekçide (yük < 10) |
| 8 | Uygulama kipi | GEÇTİ | iki yön, 6 görünüm |

Gerçek cihaz 09.11 15:14: Huawei MatePad Pro (Huawei Browser, Chromium 114; adb + CDP 9241) — sahneler gerçek ekranda
doğru (`adb screencap`; CDP ekran görüntüsü GPU canvas'ı siyah basar, kanıt sayılmaz), m4a oynuyor, soğuk yük 3,68 MB /
hazır 1,0 sn, ikinci yük 0,02 MB (ETag 304), 0.4.5 sahne tamponu yüklü, hata 0.

Chrome 104 canlı 15:44 (aynı tablet, Dijital Denge parolası Nadir): soğuk 4,79 MB / hazır 1,1 sn, ikinci yük 0,02 MB,
gerçek dokunmayla oynadı, 22 ve 52 sn'de sahneler gerçek ekranda eksiksiz, hata 0 — GEÇTİ.

Açık: iPhone yenileme; temiz yük ve dönüş ölçümü bekçileri (yük
3 sa < 12'ye düşmedi).
