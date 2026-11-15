# İstem D-dikey — 02-04-ydt-temel-dikey sahne 11-canvas-tuzak-cevap · 15.11.2026

MAKİNE: Linux x86_64 (srv21), kullanıcı sef. K=`/home/sef/01dev/_worktrees/kalem-0204` (git worktree, dal `sunucu/02-04-ydt-temel`).
Node `~/.nvm/versions/node/v24.22.2/bin`. Python `/usr/bin/python3 -I`. Skill `~/.claude/skills/motion-grafik-ders/`.
KURALLAR: Yalnız bu sahnenin dizinine yaz: `K/projeler/02-04-ydt-temel-dikey/sahneler/11-canvas-tuzak-cevap/`. Başka sahneye, `ortak/`a, BRIEF'e,
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
2. Paket: `K/projeler/02-04-ydt-temel-dikey/BRIEF-DIKEY.md` (§0, §1, §2 ve §3'teki 11. satır: Çip `Trap · answer`. Tek satırlık karşıt çift (§2.5 istisna). 184,20 öğrenci başı alt sağda (x 870–1030, y 1220–1380). Kart 1 çerçevesi 184,54, y 380–500. 185,90 `≠` sarı kalem + 186,22–186,82 `meaning` el yazısı, orta satırda y 720–850 (çarpı yok; iki cümle de doğru). Kart 1: `I am living in İstanbul.` 72 sözcük zamanlı 187,11–188,95; not `→ for now (temporary)` Caveat 64 y 520–590 (189,12; `(temporary)` 191,55–192,30); zaman çizgisi 1 y 600–700: eksen 189,68, now 190,00, kısa bant 190,24. Kart 2 çerçevesi 192,48 (`Ailenle`; 185,42'de çizilmez), y 880–1000; zaman çizgisi 2 y 1100–1200: eksen 192,48, now 192,90 (now x iki çizgide aynı), uzun bant 193,36–194,21; not `→ always (permanent)` y 1020–1090 (193,12; `(permanent)` 193,95). Kart 2 cümlesi `I live in İstanbul.` 194,89–196,65. 197,70 / 197,78 çoklu `odak` *am living* + *live*; 201,30 *meaning* altı ve fiil altları `ikincil`e döner (en çok 3 sarı); 202,30–203,30 öğrenci 1 sn baş sallar; 202,74 `(permanent)` altı; 203,46 `(temporary)` altı. Altyazı: cümle 13 dilimleri), `zaman.json` (bu sahne
   183,79–205,30 küresel sn), `ortak/anlatim/senaryo.json` + `sozcukler.json` + `baslar.json` + `altyazi.json` (cümle 13: olay
   söylendiği anda gelir), `K/projeler/present-continuous-dikey/BRIEF-DIKEY.md` §0 ve §2–§3 (Nadir'in dikey bulguları, HUD ölçüleri).
3. Yatay karşılık (içerik ve olay sırası; yerleşim DEĞİL): `/home/sef/01dev/_worktrees/kalem-0204/projeler/02-04-ydt-temel/sahneler/11-canvas-tuzak-cevap/` (kod + RAPOR.md).
4. Dikey örnek (aynı motor; dosya yapısı, calistir.sh kalıbı, 1080×1920 kurulum): `/home/sef/01dev/_worktrees/kalem-0204/projeler/present-continuous-dikey/sahneler/04-canvas-ornek2/`.

## Yaz
`sahneler/11-canvas-tuzak-cevap/` içinde örnekle aynı dosya yapısı. Kurallar: tek sütun, kenar 48, içerik bandı BRIEF-DIKEY §2; yazı tabanı ≥ 50
mantıksal px; satır ≤ 24 karakter; tek vurgu sarı (temaya göre), doğru şık yeşil, kırmızı yok, emoji yok; sabit px yerine oran ya da
BRIEF-DIKEY ölçüsü; altyazı + karaoke alt bantta; künye ve tema çifti (açık + koyu) `ortak/kunye.js` ile; 9 sn'den uzun boş çerçeve yok.
`calistir.sh`: `[ -d /opt/homebrew/bin ] && export PATH="/opt/homebrew/bin:$PATH"`, yük `Y=$(yuk1)`, yakalama `1080 1920`.

## Doğrula (zorunlu, geçmeden bitirme)
`cd K && bash araclar/qa-yerel.sh 02-04-ydt-temel-dikey 11-canvas-tuzak-cevap <açık t1,t2,t3> <koyu t> --hazirla`
t değerleri KÜRESEL anlatım saniyesidir (183,79 + sahne içi saniye); olayların bittiği 3 an + koyu için 1 an. Çıkış kodu 0 olmalı.
qa-yerel ya da kapı dikey (1080×1920) paketi ölçemiyorsa dur ve hatayı aynen raporla; aracı değiştirme.
Üretilen PNG'lere (`sahneler/11-canvas-tuzak-cevap/k/`, `k/koyu/`) Read ile BAK: taşma, kesik yazı, üst üste binme, okunmaz kontrast, boş kare,
alt bantta altyazıyla çakışma. En çok 4 düzeltme turu; geçmezse dur ve raporla.

## Rapor
`sahneler/11-canvas-tuzak-cevap/RAPOR.md`: olay listesi, kapı sonucu (son satırlar), bakılan kareler ve bulgu, agy koşu özeti yolu, açık noktalar.
Son mesajın en çok 10 satır: kapı çıkış kodu, kare yolları, agy koşu özeti, açık noktalar.

## Kanca kuralı (şef, 15.11)
Kanca atlama bayrağı OLUŞTURMA (/tmp/conductor-*, ~/.conductor/*); bayrağı yalnız Nadir açar. Durdurma kancası sözleşme satırı isterse
`K/.claude/docs/sozlesme.md` dosyasına 1–2 satır EKLE (yalnız ekleme; bu, kapsam kuralının tek istisnasıdır).
