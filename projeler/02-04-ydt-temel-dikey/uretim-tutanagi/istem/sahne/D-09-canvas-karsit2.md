# İstem D-dikey — 02-04-ydt-temel-dikey sahne 09-canvas-karsit2 · 15.11.2026

MAKİNE: Linux x86_64 (srv21), kullanıcı sef. K=`/home/sef/01dev/_worktrees/kalem-0204` (git worktree, dal `sunucu/02-04-ydt-temel`).
Node `~/.nvm/versions/node/v24.22.2/bin`. Python `/usr/bin/python3 -I`. Skill `~/.claude/skills/motion-grafik-ders/`.
KURALLAR: Yalnız bu sahnenin dizinine yaz: `K/projeler/02-04-ydt-temel-dikey/sahneler/09-canvas-karsit2/`. Başka sahneye, `ortak/`a, BRIEF'e,
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
2. Paket: `K/projeler/02-04-ydt-temel-dikey/BRIEF-DIKEY.md` (§0, §1, §2 ve §3'teki 9. satır: Çip `Contrast 2 / 2`. Kare 0 = 08 son düzeni (ortak ölçüler §3 satır 8). 145,72'de 08 kartı + notu üst şeride küçülür (y 352–470: `is wearing … today → this day only` + tişört simgesi); bant, now ve `now` yerinde kalır. Kart y 490–760: `The train to İzmir / leaves at 7 pm today.` 72, sözcük zamanlı 145,84–148,80; kartın sağ iç köşesinde tren simgesi 146,00. 149,69 not `today`; 150,57 `odak` *7 pm* (dar öbek → `alti`); 151,05 not `+ 7 pm`; 151,85 zaman çizgisinde 7 pm çentiği + nokta (x 780, today bandının içinde); 152,25 `7 pm` etiketi; 153,45 now → 7 pm kalem yayı; 154,93 not oku + `timetable` (not satırı: `today + 7 pm → timetable`). 156,09 `odak` *leaves*. 157,21 çoklu `odak`: iki *today* (şerit + kart). Alt y 1290–1390: 159,05 `≠` (kalem, 3 darbe, x ≈ 570); 160,57 `RIGHT NOW` Caveat 64 now altında; 161,61 `TIMETABLE` 7 pm altında. Altyazı: cümle 10 dilimleri), `zaman.json` (bu sahne
   145,29–162,33 küresel sn), `ortak/anlatim/senaryo.json` + `sozcukler.json` + `baslar.json` + `altyazi.json` (cümle 10: olay
   söylendiği anda gelir), `K/projeler/present-continuous-dikey/BRIEF-DIKEY.md` §0 ve §2–§3 (Nadir'in dikey bulguları, HUD ölçüleri).
3. Yatay karşılık (içerik ve olay sırası; yerleşim DEĞİL): `/home/sef/01dev/_worktrees/kalem-0204/projeler/02-04-ydt-temel/sahneler/09-canvas-karsit2/` (kod + RAPOR.md).
4. Dikey örnek (aynı motor; dosya yapısı, calistir.sh kalıbı, 1080×1920 kurulum): `/home/sef/01dev/_worktrees/kalem-0204/projeler/present-continuous-dikey/sahneler/05-canvas-ornek3/`.

## Yaz
`sahneler/09-canvas-karsit2/` içinde örnekle aynı dosya yapısı. Kurallar: tek sütun, kenar 48, içerik bandı BRIEF-DIKEY §2; yazı tabanı ≥ 50
mantıksal px; satır ≤ 24 karakter; tek vurgu sarı (temaya göre), doğru şık yeşil, kırmızı yok, emoji yok; sabit px yerine oran ya da
BRIEF-DIKEY ölçüsü; altyazı + karaoke alt bantta; künye ve tema çifti (açık + koyu) `ortak/kunye.js` ile; 9 sn'den uzun boş çerçeve yok.
`calistir.sh`: `[ -d /opt/homebrew/bin ] && export PATH="/opt/homebrew/bin:$PATH"`, yük `Y=$(yuk1)`, yakalama `1080 1920`.

## Doğrula (zorunlu, geçmeden bitirme)
`cd K && bash araclar/qa-yerel.sh 02-04-ydt-temel-dikey 09-canvas-karsit2 <açık t1,t2,t3> <koyu t> --hazirla`
t değerleri KÜRESEL anlatım saniyesidir (145,29 + sahne içi saniye); olayların bittiği 3 an + koyu için 1 an. Çıkış kodu 0 olmalı.
qa-yerel ya da kapı dikey (1080×1920) paketi ölçemiyorsa dur ve hatayı aynen raporla; aracı değiştirme.
Üretilen PNG'lere (`sahneler/09-canvas-karsit2/k/`, `k/koyu/`) Read ile BAK: taşma, kesik yazı, üst üste binme, okunmaz kontrast, boş kare,
alt bantta altyazıyla çakışma. En çok 4 düzeltme turu; geçmezse dur ve raporla.

## Rapor
`sahneler/09-canvas-karsit2/RAPOR.md`: olay listesi, kapı sonucu (son satırlar), bakılan kareler ve bulgu, agy koşu özeti yolu, açık noktalar.
Son mesajın en çok 10 satır: kapı çıkış kodu, kare yolları, agy koşu özeti, açık noktalar.

## Kanca kuralı (şef, 15.11)
Kanca atlama bayrağı OLUŞTURMA (/tmp/conductor-*, ~/.conductor/*); bayrağı yalnız Nadir açar. Durdurma kancası sözleşme satırı isterse
`K/.claude/docs/sozlesme.md` dosyasına 1–2 satır EKLE (yalnız ekleme; bu, kapsam kuralının tek istisnasıdır).
