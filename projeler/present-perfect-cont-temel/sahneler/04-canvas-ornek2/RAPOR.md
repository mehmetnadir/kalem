# Sahne 04 YATAY — Örnek 2 (PPC temel, düz canvas)

Tema: acik ve koyu ikisi de koşuldu.

- Kare: 462 (ffprobe 462/462, 1920x1080 yuv420p 30 fps, iki tema). t_bas 32,28. Olay: 34 (en büyük kare 439).
- Dosyalar: sahne.js, sahne-ortak.js (ana PC 04 kopyası, PPC yolları), sayfa.html, calistir.sh.
- İçerik: BRIEF §4 sahne 04: 2 dairesi, cümle, kardeş (sitting-2) + gitar (coco/guitar) + 3 nota, güneş (coco/sun) → now zaman oku, TR çeviri, since + for = süre uzunluğu, has daire, formül kartı has been + V-ing / play-ing.
- Sapma: Caveat `başlangıç noktası` 42,47'de (konuşulduğu an) çıkar; BRIEF satırı 40,62–42,22 aralığını verir ama sözcük 42,47'de söylenir.
- Editör kapısı (başsız, ortak-tarayici): `?surum=<ana-yatay|dikey-tam>&tema=acik&t=22` → slot no 2 `hazir:true, goster:true, op:1`; `t=38` → slot no 3 `hazir:true, goster:true, op:1`. Editör konsolundaki 404 (3 adet) başka ajanların henüz yazılmamış sahnelerinden; kendi sahne sayfam `?canli=1` konsol hatası 0. Sahne sayfası konsolunda `/log` POST 405'i vardı (CIZIM tanı satırı); `canli` kipinde kapatıldı (görüntü değişmez, videolar öncesi koşudan).
- Bakılan kareler: k/0097 k/0277 k/0412 k/0449 (acik ve koyu), kontrol.png.
- Neden yeniden: (1) güneş yalnız daire çıkıyordu (tabler/sun kısa ışın yolları) → coco/sun; (2) play-ing satırı kart kenarına taşıyordu → x 200.
- Açık soru: BRIEF §4'te `guitar` adı yalnız coco/guitar.svg ile var (tabler'de yalnız guitar-pick).
