# İstem D-dikey — 02-04-ydt-temel-dikey sahne 02-paperjs-kanca · 15.11.2026

MAKİNE: Linux x86_64 (srv21), kullanıcı sef. K=`/home/sef/01dev/_worktrees/kalem-0204` (git worktree, dal `sunucu/02-04-ydt-temel`).
Node `~/.nvm/versions/node/v24.22.2/bin`. Python `/usr/bin/python3 -I`. Skill `~/.claude/skills/motion-grafik-ders/`.
KURALLAR: Yalnız bu sahnenin dizinine yaz: `K/projeler/02-04-ydt-temel-dikey/sahneler/02-paperjs-kanca/`. Başka sahneye, `ortak/`a, BRIEF'e,
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
2. Paket: `K/projeler/02-04-ydt-temel-dikey/BRIEF-DIKEY.md` (§0, §1, §2 ve §3'teki 2. satır: Kare 0 = 01 son düzeni. 3,08 `yaşı-yor-um.` 4. satır (taban y 1140) + 2. *yor* sarı kutu. 4,84 / 5,24 sarı kalem `=`: iki *yor* kutusunu sağdan bağlayan iki kısa çizgi. 6,50'de dört satır üst şeride toplanır (y 352–560, Fredoka 64: `İstanbul'da yaşı-yor-um.` / `Amcamla yaşı-yor-um.`, *yor* kutuları kalır). Kanca çifti (tek satırlık, §2.5 istisna): kart A y 600–740 `I live in İstanbul.` Fredoka 72 sözcük zamanlı (6,91), karaoke altı; 8,60 `bag` oku üst şeritteki 1. *yor* → *live*; etiket `SIMPLE` (9,08) `PRESENT` (9,40) Fredoka 64 kart altında y 770–840. Kart B y 880–1020 `I am living with my uncle.` (10,69, 812 px tek satır); 12,86 `bag` 2. *yor* → *am living*; `PRESENT` (13,50) `CONTINUOUS` (13,94) y 1050–1120. 15,82 `vs` iki etiket arasında. 15,98 (`zamanın`) üç parça HUD'a uçar: `SIMPLE PRESENT vs` ders satır 1, `PRESENT CONTINUOUS` satır 2; iniş bitince rozet açılır (≈ 16,7). 17,26 sağ kenarda iki uçlu sarı fark oku (kart A ↔ kart B). 19,26 `MEANING` Fredoka 140 y 1180–1340 + 19,58'de biten sarı belirteç (yazının alt yarısı). Altyazı: cümle 1 sonu, cümle 2 dilimleri), `zaman.json` (bu sahne
   3,00–20,22 küresel sn), `ortak/anlatim/senaryo.json` + `sozcukler.json` + `baslar.json` + `altyazi.json` (cümle 1 (sonu), 2: olay
   söylendiği anda gelir), `K/projeler/present-continuous-dikey/BRIEF-DIKEY.md` §0 ve §2–§3 (Nadir'in dikey bulguları, HUD ölçüleri).
3. Yatay karşılık (içerik ve olay sırası; yerleşim DEĞİL): `/home/sef/01dev/_worktrees/kalem-0204/projeler/02-04-ydt-temel/sahneler/02-paperjs-kanca/` (kod + RAPOR.md).
4. Dikey örnek (aynı motor; dosya yapısı, calistir.sh kalıbı, 1080×1920 kurulum): `/home/sef/01dev/_worktrees/kalem-0204/projeler/present-continuous-dikey/sahneler/02-paperjs-kanca/`.

## Yaz
`sahneler/02-paperjs-kanca/` içinde örnekle aynı dosya yapısı. Kurallar: tek sütun, kenar 48, içerik bandı BRIEF-DIKEY §2; yazı tabanı ≥ 50
mantıksal px; satır ≤ 24 karakter; tek vurgu sarı (temaya göre), doğru şık yeşil, kırmızı yok, emoji yok; sabit px yerine oran ya da
BRIEF-DIKEY ölçüsü; altyazı + karaoke alt bantta; künye ve tema çifti (açık + koyu) `ortak/kunye.js` ile; 9 sn'den uzun boş çerçeve yok.
`calistir.sh`: `[ -d /opt/homebrew/bin ] && export PATH="/opt/homebrew/bin:$PATH"`, yük `Y=$(yuk1)`, yakalama `1080 1920`.

## Doğrula (zorunlu, geçmeden bitirme)
`cd K && bash araclar/qa-yerel.sh 02-04-ydt-temel-dikey 02-paperjs-kanca <açık t1,t2,t3> <koyu t> --hazirla`
t değerleri KÜRESEL anlatım saniyesidir (3,00 + sahne içi saniye); olayların bittiği 3 an + koyu için 1 an. Çıkış kodu 0 olmalı.
qa-yerel ya da kapı dikey (1080×1920) paketi ölçemiyorsa dur ve hatayı aynen raporla; aracı değiştirme.
Üretilen PNG'lere (`sahneler/02-paperjs-kanca/k/`, `k/koyu/`) Read ile BAK: taşma, kesik yazı, üst üste binme, okunmaz kontrast, boş kare,
alt bantta altyazıyla çakışma. En çok 4 düzeltme turu; geçmezse dur ve raporla.

## Rapor
`sahneler/02-paperjs-kanca/RAPOR.md`: olay listesi, kapı sonucu (son satırlar), bakılan kareler ve bulgu, agy koşu özeti yolu, açık noktalar.
Son mesajın en çok 10 satır: kapı çıkış kodu, kare yolları, agy koşu özeti, açık noktalar.
