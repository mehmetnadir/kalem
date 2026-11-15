# İstem J3-OZET — 12 paketin (6 kol a + 6 kol b) 2. tur çıktı jürisi özeti ve son düzeltme planı · 16.11.2026

MAKİNE: Linux x86_64 (srv21), kullanıcı sef. K=`/home/sef/01dev/_worktrees/kalem-0204` (worktree), D=`/home/sef/01dev/dijital-anlatim`.
SABİT KURALLAR: SALT OKUMA; hiçbir üretim dosyasını ve hüküm dosyasını değiştirme. Yazacağın dosyalar: `K/uretim-hatti/raporlar/J3-OZET-1611.md` ve
`K/uretim-hatti/istemler/DUZ4-<kod>.md` (6 dosya; aşağıda). Silme yok, git commit yok, alt ajan yok, agy-filo yok, mp4 yok. Kanca atlama bayrağı
oluşturma. Arka plan işi beklerken `pgrep -f` kullanma.

## Girdi
- Hükümler (EN SON dosya sayılır; `juri-olcutleri.md` §1b): kol a `K/projeler/<paket>/uretim-tutanagi/juri/J2-hukum-*.md` (tarihli olanların en
  yenisi), kol b `K/projeler/<paket>b/uretim-tutanagi/juri/KBJ-hukum-*.md`. Paketler: `02-04-ydt-temel-s1`, `-s2`, `-s3`, `simple-present-temel-s1`,
  `-s2`, `-s3`. Önce 12 tarihli hüküm dosyasının varlığını denetle; eksik varsa ön planda `sleep 300` ile en çok 6 kez yeniden bak; hâlâ eksikse
  eldekilerle çalış ve eksikleri raporun başına yaz.
- İlk tur özeti: `K/uretim-hatti/raporlar/J2-OZET-1511.md` (A / B / C sınıfları). Düzeltme raporları: `…/uretim-tutanagi/DUZ2-RAPOR.md`.
- Ölçütler: `D/.claude/docs/juri-olcutleri.md`. Standartlar: `huni-v2-standart.md`, `huni-ab-sozlesme.md`, `kapak-standardi.md`.
- Kapı betiği: `D/araclar/huni-kapi.mjs` (jürilerin "kapı hatası" dediği satırlar betik hatasıdır).

## İş
1. Her hükümden kaldı maddelerini (hayır + kanıt yok) çıkar; tek tablo: madde × 12 paket.
2. İlk turla karşılaştır: kapanan madde, süren madde, YENİ çıkan madde (düzeltme bir şeyi bozdu mu?).
3. Her kaldı maddeyi sınıfla, standart satırıyla:
   - **A · gerçek hata**: düzeltme (dosya, sahne, ses gerekir mi).
   - **B · ölçüt hatası**: ölçüt belgesi için önerilen yeni metin. Kısa videoya uygulanmaması gereken ders maddeleri (DK-…, ST-…, EK-…) varsa
     "kısa için geçerli mi" kararını standarttan gerekçelendir.
   - **C · kanıt eksikliği**: kanıtı ÜRETİM oturumu üretebilir mi (kontak sayfası, 168 px kapak, kare çifti, `hyperframes check` çıktısı, motor zaman
     kapısı çıktısı) yoksa yalnız insan mı verebilir (dinleme: Nadir; adres gönderim kaydı: şef)? İnsan kanıtı isteyen maddeler ayrı liste.
   - **K · kapı hatası**: betik için düzeltme tarifi (dosya:satır, beklenen davranış).
4. Jüri tutarsızlığı: aynı maddeye aynı durumda farklı hüküm veren jüriler.
5. **DUZ4 istemleri (yaz).** Kısa çifti başına bir istem dosyası: `K/uretim-hatti/istemler/DUZ4-0204S1.md`, `-0204S2`, `-0204S3`, `-0202S1`, `-0202S2`,
   `-0202S3`. Kalıp olarak `K/uretim-hatti/istemler/DUZ2-0204S1.md` dosyasının başlık, MAKİNE ve SABİT KURALLAR bölümünü aynen al (Silinecekler dizin
   adını `2026-11-16-duz4-<kod>` yap), sonra o çifte ÖZEL iş listesini yaz: yalnız A sınıfı düzeltmeler ve üretim oturumunun üretebileceği C sınıfı
   kanıtlar; her iş için dosya, sahne, beklenen sonuç ve kanıtın tutanakta duracağı yol. Tek değişken kuralları (AB-3, AB-8, AB-9) ve "kareye kendin
   bak" satırı kalır. İş listesi boşsa o çift için dosya yazma, raporda "DUZ4 gerekmez" de.
6. Teslim durumu: 12 paketin her biri için "kapıdan geçer mi" (A = 0 ve üretilebilir C = 0 ise evet); geçmeyenlerde kalan iş sayısı.

Son mesajın en çok 12 satır: kapanan / süren / yeni madde sayıları, A / B / C / K sayıları, insan kanıtı isteyen maddeler, yazılan DUZ4 istemleri,
ölçüt belgesinde değişecek maddeler, kapıdan geçen paket sayısı, rapor yolu.
