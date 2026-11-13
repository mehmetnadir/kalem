# Sahne 10 · tuzak + soru anı 2 (HyperFrames, 639 kare, 167,60–188,50 sn; cümle 12–13)

Durum: P2 yazıldı, `ONIZLE_YALNIZ=1` hazırlığı koşuldu (açık tema son koşu). Render yok. Kapı ve `sahne-kare` koşulmadı (şef EK); `k/` boş.
Tema: acik.

## İçerik
- Cümle 12: `TRAP` etiketi + tam genişlik kart (`yaklas`: kart 0,93 → 1 ölçekle öne gelir). Cümle `We believe this situation / is temporary.` konuşmayla sözcük sözcük; `believe` sarı daire; `temporary` sarı belirteç; kartın sağ alt köşesinde kalemle `-ing`, ardından `?`.
- Cümle 13 (SORU ANI 2, yanılgı: Türkçe "şu anda" duygusuyla `-ing`): öğrenci başı (`ogrenci-bas.svg`, kadın, K22) + el çizimi balon; 9 sözcük, sözcük sözcük, Fredoka 600 48 px: "Hocam, şu anda inanıyoruz. We are believing. Olmaz mı?". `şu anda` sarı belirteç; sarı nokta balonu karttaki `-ing ?` notuna bağlar. Soru kartta kalır (video ortasında soru kartı yok). 0,75 sn duraklama ve cevap sahne 11'de.
Künye: sağ üst `Trap`, ajanda Trap etkin. Hareket 0,55–20,75 sn (ilk/son 12 kare durgun; `Y.kontrol` geçti).

## Olay ↔ sözcük (cümle 12 ve 13; küresel sn)
| Olay | Sözcük (i) | Sözcük t0 | Olay sn | Sapma |
|---|---|---|---|---|
| `TRAP` + kart çizilir + yaklaş | Tuzak. (12/0) | 168,15 | 168,15 / 168,25 | 0,00 / 0,10 |
| `We` yazılır | We (12/9) | 173,60 | 173,60 | 0,00 |
| `believe` + sarı daire | believe (12/10) | 173,84 | 173,84 / 173,96 | 0,00 / 0,12 |
| `situation` · `is` · `temporary.` | situation · is · temporary (12/12–14) | 174,52 · 175,12 · 175,84 | aynı | 0,00 |
| `temporary` sarı belirteç | geçici (12/17) | 177,29 | 177,29 | 0,00 |
| köşede `-ing` kalemle | -ing (12/23) | 181,45 | 181,45 | 0,00 |
| `?` konur | istersin. (12/25) | 182,09 | 182,09 | 0,00 |
| öğrenci başı + balon çizilir | Hocam, (13/0) | 183,36 | 183,16–183,26 | −0,20 / −0,10 (söz öncesi, ders kalıbı; 12. cümle 182,89'da biter) |
| balon sözcükleri | Hocam, … mı? (13/0–8) | 183,36–188,10 | aynı | 0,00 |
| `şu anda` sarı belirteç | şu (13/1) | 184,24 | 184,24 | 0,00 |
| sarı nokta + çizgi → `-ing ?` | believing. (13/6) | 186,25 | 186,25 | 0,00 |

## Kapı
Koşulmadı (EK). Yerinde kontroller: satır 1 sağ ucu 1230 px (kart sağ iç sınırı 1764) · `-ing` notu cümleden ≥ 60 px uzakta, karttan taşmıyor (assert) · balon 360–1041 px, y 640–850 · `node --check` JS tamam.

## Açık notlar
- `yaklas` çevre karartması (taslak "çevre karartma") yapılmadı: tema çiftinde güvenli karartma rengi yok; yerine ölçekle öne gelme. Gerek varsa şef karar versin.
- Taslak: `Sinyal var ama -ing yok` (170,63–173,35) sırasında kartta cümle henüz yok; sözcük sözcük gelme kuralı gereği 173,60'a kadar yalnız `TRAP` etiketi ve boş kart görünür (5,5 sn). Gerekirse söz sırasını karşılayan bir ara öğe eklenir (ör. soluk "Example 2 / 3" çipi); eklemedim, ekran metnini değiştirmemek için.

Dosyalar: `uret.py`, `olay.py`, `calistir.sh`, `yardim.py`, `proje/index.html`, `olaylar.json`.
Kare yolları: yok (EK).

## QA 13.11
- Kapı: HyperFrames, ölçülmez. Kareler `k/10-hyperframes-tuzak-{168.5,175,182,188}.png`, koyu `k/koyu/`.
- Göz: TRAP etiketi, believe halkası (this'in t harfine hafif değiyor), -ing el yazısı doğru. Düzeltme yok. Kalan sorun yok.
- QA 13.11 ek (halka kuralı): believe halkası el altçizgisine çevrildi, kare `k/10-hyperframes-tuzak-182.png` doğrulandı (this'e değmiyor).
- zaman eşitleme 13.11: yeniden kuruldu (cümle 12 sesi yenilenmiş; t_bas 167,52, kare 613). believe işareti "believe" sözcüğünde (173,12 sn): 173,4 karesinde "We believ…" yazılırken altçizgi başlıyor, erken değil (`k/10-hyperframes-tuzak-173.4.png`).
