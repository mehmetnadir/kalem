# Sahne 02 DİKEY — Kanca (Paper.js 1080x1920, 385 kare, t_bas 3,00)

Tema: koyu

## Sonuç
- ffprobe: h264 yuv420p 1080x1920 30 fps, 385 kare (zaman.json ile birebir), her iki tema.
- `olaylar.json`: 28 olay (cizgi 17, tik 8, parilti 3), son olay kare 368; son 12 karede olay yok. Darbe: 43.
- Konsol: `sayfa.html?canli=1&tema=acik` hata 0; editör t=1,5 slot 0 `hazir:true, goster:true, op:1`, t=8 slot 1
  `hazir:true, goster:true, op:1` (editörde 404 notu: sahne 01 RAPOR.md'ye bakın).
- Zamanlar küresel sn, yerel kare = round((t − 3,00) × 30): `gidiyorum` daire 12 · `-yor` 36 · `şimdiki zaman` 52 · takvim 65 ·
  `bu akşam → gelecek` 79 · İngilizce cümle 105 · `going` daire 131 · `-yor ⇄ -ing` 154 · kutu 164 · Form 239 ·
  Zaman ifadeleri 260 · 6 kullanım 309.

## Yerleşim
Cümle 1 Caveat 80 iki satır (taban 440/525, kare 0'dan hazır = sahne 01 sonuyla aynı; ilk 12 kare durgun) · notlar Caveat 64
(taban 625 / 705) + saat + takvim · faz 1 sahne y 750–1260 (figür 500 px, ev, hilal, zemin çizgisi) · 6,4 sn'de sahne
0,58'e toplanır (kare 86–106) · yer açılan alanda `-yor ⇄ -ing` Fredoka 110, İngilizce cümle Fredoka 64 (taban 1122, 890 px
tek satır), ajanda kutusu y 1155–1392 (saat + `6 dakikada:` | Form · Zaman ifadeleri · 6 kullanım, Fredoka 64) · altyazı
cümle 2 parçaları, 1400–1536.

## Kapı: gözle bakılan kareler
`k/0045.png`, `k/0165.png`, `k/0300.png`, `k/0372.png` (koyu), `k/acik-0-6-165-372.png` (açık: 0, 6, 165, 372),
`k/telefon-01.png` (koyu 14 kare, 1 sn aralık), `kontrol.png`. Çakışma 0 (ilk turda `going` dairesi zemin çizgisine
değiyordu), HUD okunur, altyazı var, platform bandı boş, kare 0 ve 6 aynı (durgun).

## Neden yeniden
`going` dairesi toplanmış sahnenin zemin çizgisine değiyordu → küçülme 0,6 → 0,58, İngilizce cümle taban 1115 → 1122.

## Sapmalar / açık sorular
- BRIEF-DIKEY sahne 02 satırları bandı aşıyor (cümle + 2 not + 480 px sahne + İngilizce cümle + ⇄ + 3 satır ajanda ≈ 1430 px,
  bant 1040). Çözüm: BRIEF §3 "yer açmak için küçülüp toplanır" kuralıyla sahne 6,4 sn'de 0,58'e toplanır; kalıcı
  sonuç: son karede figür ≈ 290 px (BRIEF ≥ 420). Faz 1'de (3,4–6,4 sn, `k/0045.png`) figür 500 px.
  Alternatif: ajandayı 2 satıra indirmek ya da `-yor ⇄ -ing` satırını atmak; karar şefte.
- Ajanda kutusu 3 satır Fredoka 64 BRIEF'teki y 1260–1392 (132 px) bandına sığmaz; kutu y 1155–1392 alındı.
- Son karede altyazı "Birinci örnek." (cümle 3'ün ilk parçası t=15,39'da başlar); son 12 kare sabit tutuldu.
- Uzun bekleme: yük > 24 iken yük bekçisi 5 dk bekler (koşu 284 sn sürdü).
- `kalem-paper.js` D1 kopyasından: `kunye.js` dikey v2'ye çevrildi, `altyaziCiz` eklendi, `kucul` (küçülme) eklendi.
- `ortak/kunye.js` hatası bulunmadı.
