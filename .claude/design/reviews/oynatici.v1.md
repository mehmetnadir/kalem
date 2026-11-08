# Teslim kapısı — oynatıcı v1 (prototip 0.1, 08.11.2026)

Ekran görüntüleri: `araclar/oynatici-kare.mjs` (ortak başsız Chrome 9333, `Target.activateTarget` +
`Emulation.setFocusEmulationEnabled`); dosyalar oturum scratchpad `oynatici-kare/*.png` (masaüstü 1440×900 açık /
afiş / koyu+menü / dikey paket; telefon 390×844 yatay paket tam sayfa / dikey paket).

| # | Madde | Sonuç | Kanıt |
|---|---|---|---|
| 1 | Görüntüye bakıldı (1440 + 390) | GEÇTİ | 10 PNG şef tarafından okundu; 2 kusur bulundu ve düzeltildi: telefonda orta kontroller altyazıyla çakışıyordu (kapsayıcı sorgusu ≤480: orta 44 px + yukarı 14 px, altyazı 56 px); dikey pakette alt sıra taşıyordu (tema düğmesi ve bölüm adı gizlendi, düğme 40 px); telefon dikeyde kontrol çubuğu sayfa dibine düşüyordu (`main.dikey .oynatici{position:static}` `.ko`'nun `relative` konumunu eziyordu → kaldırıldı) |
| 2 | Emoji taraması | GEÇTİ | `emoji-tara.sh`: temiz (4 dosya) |
| 3 | Yapay görünüm | GEÇTİ | `impeccable detect`: ilk koşu 2 bulgu (`<img>` src'siz → statik logo yolu; renkli gölge → nötr siyah gölge), ikinci koşu 0. §2 listesi görüntüde: serif/krem/mor gradyan/cam/grain yok; marka rengi lacivert + sarı |
| 4 | Hareket | GEÇTİ | `prefers-reduced-motion` → geçiş süreleri 0, kıvrım yerine fade (`gecisTur`). JS kapalıyken: sayfa iskeleti (başlık, bölüm listesi boş) görünür; oynatıcı JS ister (doğası gereği) |
| 5 | Erişilebilirlik | GEÇTİ (masaüstü denetimi) | Düğmeler ≥44 px (dar oynatıcıda 40 px; dokunma alanı 44 px kuralı iPhone gerçek cihazda ölçülecek), odak halkası sarı 2 px, `role=slider` + `aria-valuetext`, canlı bölge (bölüm değişimi, oynat/duraklat), menü `role=menu`. Kontrast: beyaz metin koyu kaplama üstünde; sarı ilerleme çubuğu |
| 6 | Metin | GEÇTİ | Türkçe arayüz: Oynat, Duraklat, Bölümler, Altyazı, Oynatma hızı, Tam ekran, Tekrar dene; emoji yok |
| 7 | Algılanan hız | KISMEN | Lexend `font-display:swap` (kayma olası, preload yok); ilk kare ≤2 sn ölçülmedi; ses 9,1 MB wav (PRD açık soru 1) |
| 8 | Uygulama kipi | GEÇTİ | Yoğun ama okunur kontrol çubuğu; vitrin parçasında (sayfa) kart dili: yuvarlak köşe 12 px, bütün kart tıklanır, kırıntı var |

Açık (Nadir kararı): kontrol çubuğu sahne üstünde (YouTube) → sahne künyesinin alt satırı (logo, ajanda) kontroller
görünürken örtülür; alternatif çubuğu sahnenin altına almak. Afiş görseli (kapak) yok → ilk kare + karartma.
