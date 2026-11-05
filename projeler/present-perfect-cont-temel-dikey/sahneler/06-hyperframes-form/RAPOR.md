# Sahne 06 DİKEY — Soru + Form (PPC temel, HyperFrames) — RAPOR

Tema: acik + koyu · 05.11.2026 · 1080×1920 · 681 kare, t_bas 61,51

## Yapılan
- Şablon: simple-past-temel-dikey/06 (dikey HUD v2, grup düzeni, altyazı div + GSAP set); yardim.py ders adı "PRESENT PERFECT CONTINUOUS" Fredoka 56 (851 px, 984'e sığar, küçültme gerekmedi). Balon yazısı Caveat 68, 2 satır.
- Akış: balon + baş (160 px) üstte · orta: 3 satır Fredoka 100 (have/has been …) → 65,97'de balon 0,72 ölçeğiyle küçülür, "been"ler büyük Fredoka 150'ye toplanır · past → now oku · been kutusu + -ing + in progress · "-dir … -yor ⇄ have been … -ing" Fredoka 96 · 74,20 üst blok 0,6 ölçeğe toplanır, altta cümle (2 satır Fredoka 72, sözcük zamanlı) + Caveat 72 "saat-tir çalış-ıyor-um" + alt çizgiler + bağ · kart "have / has been + V-ing" Fredoka 72 (tik). Altyazı cümle 6–7 (altyazi.json, ≤ 2 satır).
- Son durum: içerik 352–1372 dolu (alt bant boş kalmıyor).

## Sayılar
- 1080×1920 yuv420p 681 kare (iki tema). olaylar.json 37 olay, ilk 12, son 615. Nefes animasyonu 21,46 sn'de biter.

## Kapılar
- Editör kapısı (başsız, ortak-tarayici + cdpilot context): t=52 → slot {"no":4,"hazir":true,"goster":true,"op":1} (sahne 05); t=72 ve t=80 → {"no":5,"hazir":true,"goster":true,"op":1} (sahne 06). Konsol: yalnız t=52 sayfasında 2 × "405 Method Not Allowed" (canvas sahnesinin /log POST çağrısı: önizleme sunucusu /log kabul etmez, görüntüyü etkilemez; t=72/80 sayfalarında konsol temiz).
- Kare: k/90.png, k/210.png, k/330.png, k/510.png, k/630.png, kontrol.png, k/telefon-01..04.png Read ile açıldı (telefon-03 ve -04): HUD okunuyor, kart tam genişlik, altyazı bandı dolu, platform boş, çakışma yok.

## Neden yeniden
- Tur 1: üst blok toplanırken (ölçek 0,65, y −100) "been -ing" balonun alt satırına biniyordu → ölçek 0,6, y −40 (blok balonun 15 px altında başlar); iki tema yeniden koşuldu.

## Sapma / açık sorular
- Toplanan üst blokta Caveat etiketler ≈ 38–42 px, çift yönlü ok çok küçük (⇅ nokta gibi); telefon kuralına (≥ 48) 0,6 ölçek yüzünden uymaz. İyi örnek (simple-past 06) 0,62 ölçek kullanıyor, aynı sapma. Çözüm için blok iki satıra bölünüp ölçek 0,75'e çıkarılabilir (sığma ≈ 60 px aşar).
- Bölüm 06 kod kartı yüksekliği 124 px; BRIEF-DIKEY §4 "formül satırları girince alt bant boş kalmasın" karşılandı (kart y 1252–1376).
