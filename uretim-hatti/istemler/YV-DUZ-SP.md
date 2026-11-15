# İstem YV-DUZ-SP — `simple-present-temel` (ve `-dikey`): bekleyen yayın verisi düzeltmeleri · 16.11.2026

MAKİNE: Linux x86_64 (srv21), kullanıcı sef. K=`/home/sef/01dev/_worktrees/kalem-0204` (worktree), D=`/home/sef/01dev/dijital-anlatim`.
SABİT KURALLAR: silme yok (`rm` yok). mp4 render yok. Ses sentezi yok. git commit yok (şef atar). Alt ajan yok, agy-filo yok. `.env` okuma. Kanca
atlama bayrağı oluşturma. Arka plan işi beklerken `pgrep -f` kullanma. Türkçe karakter tam.
YAZMA ALANI: yalnız `K/projeler/simple-present-temel` ve `K/projeler/simple-present-temel-dikey` içinde `youtube.json`, `youtube-aciklama.md`,
`surumler.json` (yalnız `canAlici` ve düzeltme notu), `uretim-tutanagi/`. Senaryo, ses, zaman, sahne, kapak dosyalarına dokunma.

## Girdi
- `K/uretim-hatti/raporlar/YV-DUZ-1511.md` §7 (bu ders için bekleyen 5 madde) ve §5 (ölçüt notları).
- Ana ders düzeltme raporu: `K/projeler/simple-present-temel/uretim-tutanagi/DUZ2-RAPOR.md` (cümle 7 değişti; ders 93,47 → 96,47 sn).
- Sözleşme: `D/.claude/docs/youtube-yayin-verisi-sozlesme.md` §2. Kurallar: `K/uretim-hatti/README.md` "YouTube yayın verisi kuralları".

## İş
1. §7 madde 1 ve 2'yi uygula (açıklamada "Bölümler:" satırı; satır 1 düzeltmesi). Dikey paket yatayla aynı metni taşır.
2. §7 madde 3: `canAlici` ve açıklama/başlık/etiket/sabit yorum/gönderi metinlerinde "geniş zaman eki = s" denkliği ve "always, usually, every day"
   için mutlak kod ifadesi kalmasın. Dersin YENİ cümle 7'siyle aynı iddiayı taşı (senaryodan oku). Dersin sesinde kalan mutlak ifade varsa (ör.
   "Kod: always, usually, every day") dokunma; cümleyi ve önerilen doğru cümleyi raporla.
3. Zaman: `youtube.json` `bolumler[].t` ve `bildirimler[].t` değerlerini yeni `zaman.json` ile karşılaştır (ders zamanı; bölüm sahne başında, ≥ 10 sn,
   ilk bölüm 0; bildirim cümle başında, ilk 30 sn ve son 20 sn dışında). Kayan değeri düzelt; açıklamadaki damga bloğu `bolumler` ile aynı olsun.
4. Kapı: `python3 K/uretim-hatti/betikler/yv-tutarlilik.py --kilitli 02-04-ydt-temel-dikey` çıkış 0 olmalı (bu derse düşen satır kalmaz).
5. Kanıt: `K/projeler/simple-present-temel/uretim-tutanagi/YV-DUZ-SP-RAPOR.md`: madde başına önce → sonra, kapı çıktısı, dersin sesinde kalan açık iş.

Son mesajın en çok 8 satır: uygulanan maddeler, değişen zaman değerleri, kapı çıkış kodu, dersin sesinde kalan açık iş, rapor yolu.
