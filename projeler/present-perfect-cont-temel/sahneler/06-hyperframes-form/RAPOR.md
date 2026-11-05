# Sahne 06 — Soru + Form (PPC temel, YATAY, HyperFrames) — RAPOR

Tema: acik + koyu · 05.11.2026 · 681 kare, t_bas 61,51

## Yapılan
- Şablon: present-continuous/06 (uret.py iskeleti, olay.py, calistir.sh); yardim.py = ppc 01 ile aynı (künye "PRESENT PERFECT CONTINUOUS"); zamanlar.json yeni (BRIEF §4 zamanları).
- Akış: öğrenci başı + balon (0,40 sn'den, ilk 12 kare boş), 8 sözcük zamanlı, "been" sarı belirteç · sağ: have/has been waiting/playing/raining (62,95–64,05) · 65,97 künye Question → Form; üç "been" tek büyük "been"e (Fredoka 160 sarı) uçar, satır gövdeleri solar, balon+baş küçülür (alfa 0,45) · "past → now" oku + "have" etiketi · 68,61 been kutusu + "-ing" + in progress bandı · 72,12 "-dir … -yor" ⇄ "have been … -ing" (Fredoka 96, çift yönlü ok) · 74,53 "I have been working for two hours." sözcük sözcük · 77,42 Caveat "saat-tir çalış-ıyor-um" + sarı alt çizgiler + iki kalem bağı · 79,14 kart "have / has been + V-ing" (tik) · 82,30 "Next lesson →".
- Dosyalar: uret.py, olay.py, yardim.py, zamanlar.json, nesneler.json, calistir.sh (KARE 681, alarm 1500, font kopyası cp ile), olaylar.json, kontrol.png, k/.

## Sayılar
- 1920×1080 yuv420p 681 kare (iki tema). olaylar.json 40 olay, ilk 12, son 633 (< 681). Nefes animasyonu 21,46 sn'de biter; son 30 kare durgun (gren hariç).

## Kapılar
- Editör kapısı (başsız, ortak-tarayici + cdpilot context): t=52 → slot {"no":4,"hazir":true,"goster":true,"op":1} (sahne 05); t=72 ve t=80 → {"no":5,"hazir":true,"goster":true,"op":1} (sahne 06). Konsol: yalnız t=52 sayfasında 2 × "405 Method Not Allowed" (canvas sahnesinin /log POST çağrısı: önizleme sunucusu /log kabul etmez, görüntüyü etkilemez; t=72/80 sayfalarında konsol temiz).
- Kare: k/30.png, k/75.png, k/110.png, k/120.png (balon), k/330.png, k/540.png, kontrol.png; ayrıca 6'lı döküm (kare 150/260/330/420/520/640) incelendi. Çakışma yok, künye tam; son karede kart + Next lesson + ajanda yerinde.

## Neden yeniden
- Tur 1: "have" etiketi satırlar uçarken üst üste biniyordu → have_etiket 66,0 → 66,85 (zamanlar.json), yeniden koşuldu (iki tema).

## Açık sorular
- Kalem bağları (bg1/bg2) çapraz geçiyor (-tir ↔ for two hours, -yor ↔ have been); okunur ama dağınık.
- 405 konsol uyarısı: 05 sahnesinin /log çağrısı (bu sahne değil).
