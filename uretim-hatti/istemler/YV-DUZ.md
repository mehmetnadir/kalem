# İstem YV-DUZ — 12 dersin YouTube yayın verisi: jüri bulgularının düzeltmesi + dersler arası tutarlılık · 15.11.2026

MAKİNE: Linux x86_64 (srv21), kullanıcı sef. K=`/home/sef/01dev/_worktrees/kalem-0204` (worktree), D=`/home/sef/01dev/dijital-anlatim`.
SABİT KURALLAR: silme yok (`rm` yok; eski dosya `/home/sef/Silinecekler/2026-11-15-yv-duz/` altına taşınır). mp4 render yok. Ses sentezi yok. git commit
yok (şef atar). Alt ajan yok, agy-filo yok. `.env`, `*.key` okuma. Kanca atlama bayrağı oluşturma. Arka plan işi beklerken `pgrep -f` kullanma; komutu
ön planda `timeout` ile koştur. Türkçe karakter tam. Yeni görsel üretme (imagen yok).
YAZMA ALANI: yalnız ders paketlerinin (ve onların `-dikey` paketlerinin) `youtube.json`, `youtube-aciklama.md` dosyaları, kapak üretici girdisi ve
kapak PNG'leri (yalnız madde 3), `uretim-tutanagi/` altı. Senaryo, ses, zaman, sahne dosyalarına dokunma. Şu paketlere HİÇ dokunma (başka oturumlar
şu an değiştiriyor): `simple-present-temel`, `simple-present-temel-dikey`, `02-04-ydt-temel-dikey` ve bütün `-s1 … -s3b` kısaları.
`simple-present-temel` için bulduğun düzeltmeleri yalnız rapora yaz.

## Girdi
- 12 hüküm: `K/projeler/<ders>/uretim-tutanagi/juri/YVJ-hukum.md`. Dersler: `02-04-ydt-temel`, `simple-present-temel`, `present-continuous`,
  `present-continuous-ileri`, `simple-present-ileri`, `02-03-ydt-temel` (ya da üretim adı; hüküm dosyası olan paketi bul:
  `ls K/projeler/*/uretim-tutanagi/juri/YVJ-hukum.md`), `present-perfect-temel`, `present-perfect-ileri`, `present-perfect-cont-temel`,
  `present-perfect-cont-ileri`, `simple-past-temel`, `simple-past-ileri`.
- Ölçütler: `D/.claude/docs/juri-olcutleri.md` §2f (YV-1…9) ve §1 (yapı kuralları: "kaynağa uygun" ≠ "doğru"; dersler arası tutarlılık).
- Sözleşme: `D/.claude/docs/youtube-yayin-verisi-sozlesme.md` §2 (`youtube.json` alanları; zaman DERS zamanıdır), `youtube-surumu-standart.md` §3.
- Kapak: `D/.claude/docs/kapak-standardi.md`.

## İş
1. **Hüküm dökümü.** 12 hükümden "hayır" ve düzeltme önerisi taşıyan "uyarı/not" maddelerini tek tabloda topla (ders × madde × bulgu × öneri).
   Her bulguyu sınıfla: (a) yayın verisi metni (başlık, açıklama, bölüm adı, etiket, sabit yorum, gönderi) · (b) kapak görselindeki yazı ·
   (c) dersin kendisi (ses/sahne; bu işte düzeltilmez) · (d) ölçüt ya da kanıt (mp4 yok, `yer.json` dersin dışında, srt paneldedir).
2. **(a) metin düzeltmeleri.** Uygula. Her öneriyi dil bilgisi açısından kendin de denetle: mutlak ve yanlış kural, yanlış Türkçe–İngilizce
   denkliği, dersin kendi örneğiyle çelişen cümle kalmaz (ör. "have -ing almaz", "ago varsa Present Perfect olmaz", "'u / 'ı" ek tutarlılığı).
   Sınırlar: başlık ≤ 100 karakter (hedef ≤ 60), açıklama ≤ 5.000 bayt, etiketler toplam ≤ 500 karakter, bölüm ≥ 10 sn ve en az 3 bölüm, ilk bölüm 0.
3. **(b) kapak yazısı.** Jürinin yanlış bulduğu kapak yazısını (ör. `present-continuous` "GİDİYORUM = AM GOING" / "-yor → -ing";
   `simple-present-ileri` ya da ilgili derste "YARIN ama WILL YOK") önce dersin kendisiyle karşılaştır:
   - Ders doğru, kapak yanlışsa: kapağı paketin kendi kapak üreticisiyle düzelt (yatay + dikey, açık + koyu); yeni yazı 2–5 sözcük, doğru ve dersin
     iddiasıyla aynı. Kareye KENDİN bak (taşma, okunurluk). Karakter ve nesne görseli değişmez.
   - Aynı yanlış dersin sesinde ya da sahnesinde de varsa: kapağa dokunma; (c) olarak raporla (cümle, sahne, önerilen doğru cümle).
4. **Dersler arası tutarlılık (betikle ölç, elle sayma).** 12 dersin `youtube.json` dosyalarını okuyan küçük bir Python betiği yaz
   (`K/uretim-hatti/betikler/yv-tutarlilik.py`; yalnız standart kitaplık; salt okuma; çıkış kodu sorun varsa 1) ve koş:
   - Başlıklar birbirinden farklıdır (temel ve ileri aynı başlığı taşımaz). Kural: temel `<Konu> | YDT İngilizce`; ileri `<Konu>: <ayırt edici
     içerik, 2–4 sözcük> | YDT İngilizce İleri` (ör. "Simple Past: used to ve would | YDT İngilizce İleri" — içerik dersin gerçekten anlattığı şey).
   - Liste adı ve sırası çakışmaz; aynı listede sıra yinelenmez.
   - Etiket yazımı tutarlı (aynı kavram aynı yazımla); kanal etiketi her derste var.
   - Sabit yorum ve gönderi metinleri birebir kopya değil (aynı cümle 2'den çok derste geçmez).
   - Dikey paketin `youtube.json` dosyası yatayla aynı başlık/açıklama/etiketi taşır (fark yalnız biçim alanları).
   - Zaman alanları dersin `zaman.json` süresini aşmaz.
   Bulduğu her sorunu düzelt, betiği yeniden koş (çıkış 0).
5. **Rapor.** `K/uretim-hatti/raporlar/YV-DUZ-1511.md`: madde 1 tablosu (sınıfıyla), uygulanan düzeltmeler (ders, alan, önce → sonra), kapak
   düzeltmeleri (kare yolları), (c) sınıfı açık işler (ders, cümle, öneri, ses yeniden gerekir mi), (d) sınıfı ölçüt notları, tutarlılık betiğinin
   son çıktısı, `simple-present-temel` için bekleyen düzeltmeler.

Son mesajın en çok 12 satır: sınıf sayıları (a/b/c/d), düzeltilen ders sayısı, yeni başlık listesi (12 satır yerine: değişenler), düzeltilen kapaklar,
(c) açık işler (ders + tek cümle), betik çıkış kodu, rapor yolu.
