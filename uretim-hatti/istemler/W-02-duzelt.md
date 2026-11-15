# İstem W-02-duzelt — 02-04-ydt-temel-dikey sahne 02-paperjs-kanca: ders adı uçuşu içeriğin üstünden geçiyor · 15.11.2026

MAKİNE: Linux x86_64 (srv21), kullanıcı sef. K=`/home/sef/01dev/_worktrees/kalem-0204`. Node `~/.nvm/versions/node/v24.22.2/bin`.
KURALLAR: Yazma yalnız `K/projeler/02-04-ydt-temel-dikey/sahneler/02-paperjs-kanca/` altında. `ortak/kunye.js` ve diğer sahnelere
DOKUNMA (13 sahne şu an render ediliyor). Silme yok (`~/Silinecekler/2026-11-15-0204/`). mp4 render YOK. git commit yok. Alt ajan yok.
Bayrak dosyası oluşturma; durma kancası sözleşme isterse `K/.claude/docs/sozlesme.md` dosyasına 1 satır ekle.
Kod yolu: küçük değişiklik Edit ile; 15+ satır yeni kod gerekiyorsa SPEC.md + `agy-filo tek --rol kod --cwd K --zaman 25m -p "…"`
ÖN PLANDA koş. agy işini `until ! pgrep -f …` döngüsüyle BEKLEME (kendi komut satırını eşler, sonsuz bekler).

## Sorun (şef kareye baktı; kapı 18 uyarı)
Paket kapısı (`node araclar/cakisma-kapisi.mjs 02-04-ydt-temel-dikey --sahne 02-paperjs-kanca --port 41333 --sunucu 41022`) bu sahnede
16,25–16,50 sn (küresel) aralığında 17 uyarı veriyor: ders adı ("SIMPLE PRESENT vs / PRESENT CONTINUOUS") sahne ortasından künye
yerine UÇARKEN "I live in İstanbul.", "I am living with my uncle." ve "İstanbul'da yaşı-yor-um." yazılarının üstünden geçiyor
(kareler `k/02-paperjs-kanca-16.25.png`, `-16.5.png`). Ayrıca 6,75 sn'de 1 uyarı: "Amcamla × yaşı-" 194×38 px (satır geçişi).
Yatay derste uçuş boş alandan geçiyordu; 1080×1920 yerleşimde yol içerikle kesişiyor.

## İstenen
1. Ders adı içeriğin üstünden geçmesin. Tercih sırası: (a) ders adı künye yerinde belirsin (opaklık 0→1 + en çok 16 px yukarı kayma,
   aynı zamanlama, ses anına bağlı an değişmez); (b) uçuş kalacaksa yol ve başlangıç noktası hiçbir yazı/çizim kutusuyla kesişmesin.
   Künyedeki son konum, boyut, renk ve 2 satır kırılımı diğer sahnelerle birebir aynı kalır (sahne 03'ün künyesiyle karşılaştır).
2. 6,75 sn uyarısına bak: gerçek üst üste binme ise (iki yazı aynı anda okunur durumda kesişiyor) düzelt; geçiş anıysa kısalt ya da
   sırala (önce çıkan tamamen çıksın).
3. Doğrula: kapı bu sahnede `çakışma yok` ve 0 uyarı; `bash araclar/qa-yerel.sh 02-04-ydt-temel-dikey 02-paperjs-kanca
   6.75,16.0,16.25,16.5,17.0,20.1 16.5 --kapisiz` karelerine Read ile BAK (taşma, kesişme, künye yeri). En çok 3 düzeltme turu.
4. `RAPOR.md` sonuna 4 satır: ne değişti, kapı çıktısı, bakılan kareler.

Son mesajın en çok 8 satır.
