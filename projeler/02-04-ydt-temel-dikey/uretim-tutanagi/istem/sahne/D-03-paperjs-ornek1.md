# İstem D-dikey — 02-04-ydt-temel-dikey sahne 03-paperjs-ornek1 · 15.11.2026

MAKİNE: Linux x86_64 (srv21), kullanıcı sef. K=`/home/sef/01dev/_worktrees/kalem-0204` (git worktree, dal `sunucu/02-04-ydt-temel`).
Node `~/.nvm/versions/node/v24.22.2/bin`. Python `/usr/bin/python3 -I`. Skill `~/.claude/skills/motion-grafik-ders/`.
KURALLAR: Yalnız bu sahnenin dizinine yaz: `K/projeler/02-04-ydt-temel-dikey/sahneler/03-paperjs-ornek1/`. Başka sahneye, `ortak/`a, BRIEF'e,
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
2. Paket: `K/projeler/02-04-ydt-temel-dikey/BRIEF-DIKEY.md` (§0, §1, §2 ve §3'teki 3. satır: Çip `Example 1 / 3`. Kart A çerçevesi 20,77 (`Birinci`), y 380–720: `She wears her coat / in the winter.` Fredoka 72 sözcük zamanlı 24,22–25,78, karaoke altı; TR `Kışın montunu giyer.` Caveat 64 el yazısı 26,79 (kart içinde, y ≈ 680). Mont çizimi (yatay `MONT`) y 750–1190, 440 px, 25,02 (`coat`). 28,55 `odak` *in the winter*. `GENERAL` Caveat 80 el yazısı 30,31, y 1230–1320; altı 31,35. 32,41'de çift kart kuralı: kart A + mont üst şeride (`wears → GENERAL` + mont simgesi). Kart B y 490–830: `She is wearing her / pink T-shirt today.` sözcük zamanı yatay `EN2` (32,41–34,13); TR `Bugün pembe tişörtünü giyiyor.` Caveat 64 (35,37, 665 px). Tişört (yatay `TISORT`) y 860–1260, 400–420 px, 33,63. 38,17 `odak` *today*. `RIGHT NOW` Caveat 80 39,05, y 1280–1370; altı 41,45. 42,81 *is* altı, 43,05 *-ing* altı. Altyazı: cümle 3 dilimleri), `zaman.json` (bu sahne
   20,22–43,85 küresel sn), `ortak/anlatim/senaryo.json` + `sozcukler.json` + `baslar.json` + `altyazi.json` (cümle 3: olay
   söylendiği anda gelir), `K/projeler/present-continuous-dikey/BRIEF-DIKEY.md` §0 ve §2–§3 (Nadir'in dikey bulguları, HUD ölçüleri).
3. Yatay karşılık (içerik ve olay sırası; yerleşim DEĞİL): `/home/sef/01dev/_worktrees/kalem-0204/projeler/02-04-ydt-temel/sahneler/03-paperjs-ornek1/` (kod + RAPOR.md).
4. Dikey örnek (aynı motor; dosya yapısı, calistir.sh kalıbı, 1080×1920 kurulum): `/home/sef/01dev/_worktrees/kalem-0204/projeler/present-continuous-dikey/sahneler/03-paperjs-ornek1/`.

## Yaz
`sahneler/03-paperjs-ornek1/` içinde örnekle aynı dosya yapısı. Kurallar: tek sütun, kenar 48, içerik bandı BRIEF-DIKEY §2; yazı tabanı ≥ 50
mantıksal px; satır ≤ 24 karakter; tek vurgu sarı (temaya göre), doğru şık yeşil, kırmızı yok, emoji yok; sabit px yerine oran ya da
BRIEF-DIKEY ölçüsü; altyazı + karaoke alt bantta; künye ve tema çifti (açık + koyu) `ortak/kunye.js` ile; 9 sn'den uzun boş çerçeve yok.
`calistir.sh`: `[ -d /opt/homebrew/bin ] && export PATH="/opt/homebrew/bin:$PATH"`, yük `Y=$(yuk1)`, yakalama `1080 1920`.

## Doğrula (zorunlu, geçmeden bitirme)
`cd K && bash araclar/qa-yerel.sh 02-04-ydt-temel-dikey 03-paperjs-ornek1 <açık t1,t2,t3> <koyu t> --hazirla`
t değerleri KÜRESEL anlatım saniyesidir (20,22 + sahne içi saniye); olayların bittiği 3 an + koyu için 1 an. Çıkış kodu 0 olmalı.
qa-yerel ya da kapı dikey (1080×1920) paketi ölçemiyorsa dur ve hatayı aynen raporla; aracı değiştirme.
Üretilen PNG'lere (`sahneler/03-paperjs-ornek1/k/`, `k/koyu/`) Read ile BAK: taşma, kesik yazı, üst üste binme, okunmaz kontrast, boş kare,
alt bantta altyazıyla çakışma. En çok 4 düzeltme turu; geçmezse dur ve raporla.

## Rapor
`sahneler/03-paperjs-ornek1/RAPOR.md`: olay listesi, kapı sonucu (son satırlar), bakılan kareler ve bulgu, agy koşu özeti yolu, açık noktalar.
Son mesajın en çok 10 satır: kapı çıkış kodu, kare yolları, agy koşu özeti, açık noktalar.

## Kanca kuralı (şef, 15.11)
Kanca atlama bayrağı OLUŞTURMA (/tmp/conductor-*, ~/.conductor/*); bayrağı yalnız Nadir açar. Durdurma kancası sözleşme satırı isterse
`K/.claude/docs/sozlesme.md` dosyasına 1–2 satır EKLE (yalnız ekleme; bu, kapsam kuralının tek istisnasıdır).
