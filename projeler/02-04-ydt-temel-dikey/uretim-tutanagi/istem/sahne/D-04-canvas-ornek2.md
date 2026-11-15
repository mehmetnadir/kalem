# İstem D-dikey — 02-04-ydt-temel-dikey sahne 04-canvas-ornek2 · 15.11.2026

MAKİNE: Linux x86_64 (srv21), kullanıcı sef. K=`/home/sef/01dev/_worktrees/kalem-0204` (git worktree, dal `sunucu/02-04-ydt-temel`).
Node `~/.nvm/versions/node/v24.22.2/bin`. Python `/usr/bin/python3 -I`. Skill `~/.claude/skills/motion-grafik-ders/`.
KURALLAR: Yalnız bu sahnenin dizinine yaz: `K/projeler/02-04-ydt-temel-dikey/sahneler/04-canvas-ornek2/`. Başka sahneye, `ortak/`a, BRIEF'e,
yatay pakete dokunma (eksik görürsen raporla). Silme yok (`~/Silinecekler/2026-11-15-0204/` altına taşı). mp4 render YOK:
`calistir.sh`'ı yalnız `ONIZLE_YALNIZ=1` ile koş. git commit yok. Claude alt ajanı açma.

## Kod yolu (kapı ve doktrin)
Kod yazma kapısı 15 satırdan uzun kod dosyasını sana kapatır; bayrak açmaya çalışma. Yol: tasarımı sahne dizininde `SPEC.md` olarak
yaz (yazılacak dosyanın mutlak yolu, örnek sahnenin mutlak yolu ve oradan alınacak kalıp, olay listesi olay · kare/küresel sn · cümle
sözcüğü, yerleşim, ekran metni, kurallar, kabul ölçütü; tam kod YAZMA). Sonra
`agy-filo tek --rol kod --cwd /home/sef/01dev/_worktrees/kalem-0204 --zaman 25m -p "<SPEC.md mutlak yolunu oku ve uygula. Yalnız <dosya
mutlak yolu> dosyasını yaz. Başka dosyaya dokunma. Silme yok. Test, render, git yok.>"`. Kodu agy yazar; sen baştan sona okur, spec'e
uyuyor mu bakarsın, küçük düzeltmeyi Edit ile yaparsın, büyük düzeltmeyi agy'ye geri verirsin (en çok 2 tur). Tam kodu kendin yazıp
agy'ye birebir kopyalatmak YASAK (kapıyı vekille dolanmaktır). Kısa dosyalar (`calistir.sh`, `sayfa.html`) Edit ile yazılabilir.

## Okuma
1. Skill `SKILL.md`, `references/kalem-hatti.md`, `stil-anayasasi.md`, `hareket-sozlugu.md`, `kliseler.md`, `soru-ani.md` (soru sahnesiyse).
2. Paket: `K/projeler/02-04-ydt-temel-dikey/BRIEF-DIKEY.md` (§0, §1, §2 ve §3'teki 4. satır: Çip `Example 2 / 3`. 44,40 daire içinde 2 (sol üst köşe, 96 px). `live` Fredoka 140 pop 47,20 (y 380–520) + sarı altı 47,55. Kart A çerçevesi 47,70, y 540–770: `I live in İstanbul / with my family.` 72, sözcük zamanlı 48,09–49,61. Ev (`tabler/home.svg`) y 790–1210, 420 px, 50,82 (`Ailemle`). Zaman çizgisi A y 1230–1390: eksen 52,90, now 53,15 + `now`, uzun bant 53,30 (`hep`), `PERMANENT` Caveat 72 bandın üstünde 54,58. 55,54 `odak` *live*. 56,64'te çift kart kuralı: şerit `live → PERMANENT` + ev simgesi. Kart B y 490–830: `My parents are out of / town, so I am living / with my uncle.` 72 (3 satır), sözcük zamanlı 56,99–59,95. Bavul (yatay `sahne.js` çizimi) y 845–1265, 62,28. Zaman çizgisi B y 1270–1390: eksen 65,00, now 65,25, kısa bant 65,60–66,12 (uç çizgileri 66,00 / 66,12), `TEMPORARY` 66,84. 67,88 `odak` *am living*. Türkçe çeviri yok (yatayda yok). Altyazı: cümle 4 dilimleri), `zaman.json` (bu sahne
   43,85–68,84 küresel sn), `ortak/anlatim/senaryo.json` + `sozcukler.json` + `baslar.json` + `altyazi.json` (cümle 4: olay
   söylendiği anda gelir), `K/projeler/present-continuous-dikey/BRIEF-DIKEY.md` §0 ve §2–§3 (Nadir'in dikey bulguları, HUD ölçüleri).
3. Yatay karşılık (içerik ve olay sırası; yerleşim DEĞİL): `/home/sef/01dev/_worktrees/kalem-0204/projeler/02-04-ydt-temel/sahneler/04-canvas-ornek2/` (kod + RAPOR.md).
4. Dikey örnek (aynı motor; dosya yapısı, calistir.sh kalıbı, 1080×1920 kurulum): `/home/sef/01dev/_worktrees/kalem-0204/projeler/present-continuous-dikey/sahneler/04-canvas-ornek2/`.

## Yaz
`sahneler/04-canvas-ornek2/` içinde örnekle aynı dosya yapısı. Kurallar: tek sütun, kenar 48, içerik bandı BRIEF-DIKEY §2; yazı tabanı ≥ 50
mantıksal px; satır ≤ 24 karakter; tek vurgu sarı (temaya göre), doğru şık yeşil, kırmızı yok, emoji yok; sabit px yerine oran ya da
BRIEF-DIKEY ölçüsü; altyazı + karaoke alt bantta; künye ve tema çifti (açık + koyu) `ortak/kunye.js` ile; 9 sn'den uzun boş çerçeve yok.
`calistir.sh`: `[ -d /opt/homebrew/bin ] && export PATH="/opt/homebrew/bin:$PATH"`, yük `Y=$(yuk1)`, yakalama `1080 1920`.

## Doğrula (zorunlu, geçmeden bitirme)
`cd K && bash araclar/qa-yerel.sh 02-04-ydt-temel-dikey 04-canvas-ornek2 <açık t1,t2,t3> <koyu t> --hazirla`
t değerleri KÜRESEL anlatım saniyesidir (43,85 + sahne içi saniye); olayların bittiği 3 an + koyu için 1 an. Çıkış kodu 0 olmalı.
qa-yerel ya da kapı dikey (1080×1920) paketi ölçemiyorsa dur ve hatayı aynen raporla; aracı değiştirme.
Üretilen PNG'lere (`sahneler/04-canvas-ornek2/k/`, `k/koyu/`) Read ile BAK: taşma, kesik yazı, üst üste binme, okunmaz kontrast, boş kare,
alt bantta altyazıyla çakışma. En çok 4 düzeltme turu; geçmezse dur ve raporla.

## Rapor
`sahneler/04-canvas-ornek2/RAPOR.md`: olay listesi, kapı sonucu (son satırlar), bakılan kareler ve bulgu, agy koşu özeti yolu, açık noktalar.
Son mesajın en çok 10 satır: kapı çıkış kodu, kare yolları, agy koşu özeti, açık noktalar.
