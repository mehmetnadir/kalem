# İstem J2-OZET — 6 kısanın çıktı jürisi hükümlerini tek tabloda topla ve sınıfla · 15.11.2026

MAKİNE: Linux x86_64 (srv21), kullanıcı sef. K=`/home/sef/01dev/_worktrees/kalem-0204` (worktree), D=`/home/sef/01dev/dijital-anlatim`.
SABİT KURALLAR: SALT OKUMA; hiçbir üretim dosyasını ve hüküm dosyasını değiştirme. Tek yazacağın dosya:
`K/uretim-hatti/raporlar/J2-OZET-1511.md` (dizini aç). Silme yok, git commit yok, alt ajan yok, agy-filo yok, mp4 yok. Kanca atlama bayrağı
oluşturma. Arka plan işi beklerken `pgrep -f` kullanma.

## Girdi
Hükümler: `K/projeler/<paket>/uretim-tutanagi/juri/J2-hukum.md`; paketler: `02-04-ydt-temel-s1`, `-s2`, `-s3`, `simple-present-temel-s1`, `-s2`, `-s3`.
Ölçütler: `D/.claude/docs/juri-olcutleri.md`. Standartlar: `D/.claude/docs/huni-v2-standart.md`, `kapak-standardi.md`.

## İş
1. Her hüküm dosyasından "hayır" ve "kanıt yok" maddelerini çıkar (kimlik, jürinin notu, kanıtı).
2. Tek tablo: madde kimliği × paket (hücre: kaldı / kanıt yok / geçti).
3. Her kaldı maddeyi SINIFLA ve gerekçesini standarttan satırla göster:
   - **A · gerçek hata** (çıktı standarda aykırı): düzeltme = hangi dosya, hangi sahne, ses yeniden gerekir mi (evet ise hangi cümle), kare yeniden
     gerekir mi. Aynı hata ana derste de varsa ayrı satır.
   - **B · ölçüt hatası** (madde yanlış yazılmış ya da kısa video için geçersiz; ör. Whisper'ın "YEDESE" duyması beklenen davranış, ana ders kapağı
     maddesinin kısa kapağına uygulanması): `juri-olcutleri.md` için önerilen yeni madde metni.
   - **C · kanıt eksikliği** (araç ya da kayıt yok; ör. çakışma kapısı çıktısı tutanakta yok, dinleme kaydı yok): kanıtı kimin, hangi komutla üreteceği.
4. Düzeltme planı: paket başına iş listesi (yalnız A sınıfı), işleri "yalnız metin/md" · "sahne yeniden" · "ses yeniden" diye ayır; tahmini oturum sayısı.
   Birden çok pakette yinelenen aynı düzeltmeyi (ör. rozet metni, utm harfi, kapak karakteri) tek "toplu düzeltme" satırında topla.
5. Jürinin kendisine dair gözlem: 6 jüri aynı maddeye farklı hüküm verdiyse (tutarsızlık) listele.

Son mesajın en çok 12 satır: A / B / C sayıları, toplu düzeltmeler listesi, ses yeniden gerektiren düzeltmeler, ölçüt belgesinde değişmesi gereken
maddeler, rapor yolu.
