# İstem DUZ-1 — huni v2 bağımsız inceleme bulgularının düzeltmesi (3 paket, metin + 1 hikâye karesi) · 15.11.2026

MAKİNE: Linux x86_64 (srv21), kullanıcı sef. K=`/home/sef/01dev/_worktrees/kalem-0204` (worktree), D=`/home/sef/01dev/dijital-anlatim`.
Python `/usr/bin/python3 -I`.
KURALLAR: Yalnız isteneni yaz. Silme yok (`rm` yok; gerekirse `~/Silinecekler/2026-11-15-huni-v2/` altına taşı). Ses sentezi yok, ElevenLabs
çağrısı yok, mp4 render yok, git commit yok, alt ajan yok, agy-filo yok, ayna yüklemesi yok. Aşağıda adı geçmeyen dosyaya dokunma.
Kanca atlama bayrağı oluşturma (`/tmp/conductor-*`, `~/.conductor/*`); sözleşme kancası isterse `K/.claude/docs/sozlesme.md` dosyasına 1 satır ekle.
Arka plan işi beklerken `pgrep -f` kullanma; komutu ön planda `timeout` ile koştur.

Bağımsız inceleme 6 kısa pakette 5 kusur buldu. Her birini aşağıdaki gibi düzelt; her düzeltmeden sonra kanıt komutunu koştur.

## 1. `projeler/02-04-ydt-temel-s1` — hikâye B doğru cümleyi "yanlış" diye çiziyor
- Yer: `sahneler/07-hyperframes-hikaye-b/proje/index.html` (`yanlis-yazi` = "I live with my uncle.", `yanlis-cizgi` üstü çizgi) ve üreticisi
  (`uret.py` varsa önce orada düzelt, sonra `calistir.sh` ile yeniden üret; `SPEC.md` ilgili satırını da güncelle).
- Sorun: "I live with my uncle." dilbilgisi olarak doğru bir cümle; üstü çizili kart "bu cümle hatalı" okunur. Yanlış olan cümle değil,
  "şimdilik" (geçici) bağlamına uymaması.
- Düzeltme: üstü çizgiyi kaldır. İki şık yan yana kalsın; doğru şıkta onay işareti, öteki şık soluk ve altında küçük etiket: `kalıcıysa`
  (doğru şıkkın altında `şimdilik → geçici`). Kartın geri kalanı, kanal katmanı, künye ve "Kaydet" değişmez. Emsal çözüm: aynı dersin S2
  hikâye B karesi (`projeler/02-04-ydt-temel-s2/sahneler/07-hyperframes-hikaye-b/`) ve jüri notu `…-s2/uretim-tutanagi/juri/s2.dil.md`.
- Kareyi yeniden çek (sahnenin `calistir.sh` yolu; açık + koyu), paket kökündeki `hikaye-b.png` dosyasını güncelle. Çakışma kapısı:
  `node araclar/cakisma-kapisi.mjs 02-04-ydt-temel-s1 --sahne 07-hyperframes-hikaye-b --port 41333 --sunucu 41022` → çıkış 0.
- Kanıt: yeni `hikaye-b.png` dosyasına Read ile bak; üstü çizgi yok, iki etiket okunuyor, taşma yok.

## 2. `projeler/02-04-ydt-temel-s1` — açıklama metni
- `aciklama-a.md` ve `aciklama.md`: "konusu püf noktası" → "konusunun püf noktası".
- `aciklama-a.md`, `aciklama-b.md`, `aciklama.md`: `utm_campaign=ing-ydt-gr-02-04-t` → `utm_campaign=ING-YDT-GR-02-04-T` (öteki 5 paket büyük harf).
- `aciklama.md`: `utm_content=s1` → `utm_content=s1-a` (`aciklama.md` = A setinin kopyası; öteki paketlerle aynı kural).
- Kanıt: `grep -c "utm_campaign=ING-YDT-GR-02-04-T"` üç dosyada > 0; `grep -c "utm_campaign=ing-"` üç dosyada 0; `grep -c "konusu püf"` 0.

## 3. `projeler/simple-present-temel-s1` — yanlış denklik "Türkçedeki geniş zaman eki = İngilizcedeki s"
- Yerler: `aciklama-a.md`, `aciklama-b.md`, `aciklama.md`, `surumler.json` (açıklama alanı), `ortak/anlatim/senaryo.json` (meta / not alanları;
  SES ve EKRAN cümlelerine DOKUNMA — bu cümle seste yok, olsaydı ses yeniden gerekirdi; varsa dur ve raporla).
- Sorun: Türkçe geniş zaman eki bütün kişilerde var (giderim, gidersin, gider); İngilizce -s yalnız he/she/it. Cümle "I goes" hatasına götürür.
- Düzeltme metni: `Gider = goes; ama yalnız he, she, it ile. I, you, we, they ile go.` (bağlama göre aynı anlamda kısalt; "eki = s" denkliği kalmasın).
- JSON dosyalarını yazdıktan sonra ayrıştır (`json.load`). Kanıt: `grep -c "eki = İngilizcedeki"` bütün paket metin dosyalarında 0.

## 4. `projeler/simple-present-temel-s2` — `always` için istisnasız kural (yalnız açıklama)
- `aciklama-a.md`, `aciklama-b.md`, `aciklama.md`: "Usually, always, every day = Simple Present" türü kesin eşitlikleri "çoğunlukla" ile yumuşat
  (ör. başlık: `Usually, always, every day görürsen: çoğunlukla Simple Present`). Video, ses, ekran, kapak DEĞİŞMEZ.
- Kanıt: değişen satırların eski ve yeni hâlini raporda yan yana yaz.

## 5. Rapor
`projeler/02-04-ydt-temel-s1/uretim-tutanagi/DUZ-1-RAPOR.md`: madde başına değişen dosyalar, kanıt komutu ve çıktısı, hikâye B'nin önce/sonra
tarifi, dokunmadığın ama gördüğün benzer kusur (varsa). Değiştirdiğin dosyaların tam listesini sona yaz (şef aynaya yükleyip commit atacak).

Son mesajın en çok 10 satır.
