Şef kararı (14.11): istemdeki "alt ajan açma" kuralını bu iş için kaldırıyorum. Kapının önerdiği yol doğru yoldur:

BAĞLAYICI STANDART: üretimden önce `D/.claude/docs/` altından oku — `huni-v2-standart.md` (kısa), `kapak-standardi.md` (kapak, hikâye), `youtube-surumu-standart.md` (YouTube sürümü), `huni-ab-sozlesme.md` (A/B kolu). Bu istemdeki eski (v1) söz bunlarla çelişirse standart geçer. mp4 yalnız Nadir'in açık sözüyle. D=`/home/sef/01dev/dijital-anlatim`.
tasarımı sen yaz, kodu agy yazsın, sen incele ve doğrula. Bayrak açmaya çalışma, kapıyı parça parça yazarak dolanma.

1. Spec: sahne dizininde `SPEC.md` yaz (belge; kapıya takılmaz). İçerik: yazılacak dosyanın mutlak yolu; örnek sahnenin
   mutlak yolu ve oradan alınacak kalıp (dosya yapısı, ortak API, calistir.sh beklentisi); olay listesi (olay · kare/zaman ·
   cümle sözcüğü); yerleşim ve ekran metni; kurallar (tek vurgu sarı, doğru şık yeşil, kırmızı yok, emoji yok, yazı tabanı
   yatay 30 mantıksal px, sabit px yok, künye ve açık/koyu tema `ortak/kunye.js` ile, sessiz catch yok); kabul ölçütü
   (qa-yerel.sh çıkış 0). Tam kod yazma; olay, yerleşim ve işlev adları yeterli.
2. agy ile yazdır (komut ön planda, en çok 25 dk):
   `agy-filo tek --rol kod --cwd /home/sef/01dev/_worktrees/kalem-0204 --zaman 25m -p "<SPEC.md mutlak yolunu oku ve uygula.
   Yalnız <dosya mutlak yolu> dosyasını yaz. Başka dosyaya dokunma. Silme yok. Test, render, git yok.>"`
   Dönen özet tablosunda `eksik`, `SAHİPSİZ` ya da `bos-kosu` varsa spec'i netleştir ve bir kez daha koş.
3. agy'nin yazdığı dosyayı baştan sona oku: spec'e uyuyor mu, örnekteki kalıp mı, olay zamanları sözcük zamanına bağlı mı,
   sabit px / kırmızı / emoji / sessiz catch var mı, ortak dosyalara yazmış mı (`git status --short` ile bak; yalnız bu sahnenin
   dizini değişmiş olmalı). Küçük düzeltmeyi Edit ile yap. Büyük düzeltme gerekirse agy'ye yeniden ver (en çok 2 tur).
4. İstemdeki "Doğrula" adımını eksiksiz koş (`bash araclar/qa-yerel.sh 02-04-ydt-temel <sahne> … --hazirla`, çıkış 0),
   PNG'lere Read ile bak, en çok 4 düzeltme turu. Sonra `RAPOR.md`yi yaz ya da güncelle (agy koşusunun özet yolu dahil).

Son mesajın en çok 10 satır: kapı çıkış kodu, kare yolları, agy koşu özeti, açık noktalar.
