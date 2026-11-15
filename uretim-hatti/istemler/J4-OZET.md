# İstem J4-OZET — 12 paketin (6 kol a + 6 kol b) 3. tur çıktı jürisi özeti ve kapanış planı · 16.11.2026

MAKİNE: Linux x86_64 (srv21), kullanıcı sef. K=`/home/sef/01dev/_worktrees/kalem-0204` (worktree), D=`/home/sef/01dev/dijital-anlatim`.
SABİT KURALLAR: SALT OKUMA; hiçbir üretim dosyasını ve hüküm dosyasını değiştirme. Yazacağın dosyalar: `K/uretim-hatti/raporlar/J4-OZET-1611.md` ve
`K/uretim-hatti/istemler/DUZ5-<kod>.md` (6 dosya; aşağıda). Silme yok, git commit yok, alt ajan yok, agy-filo yok, mp4 yok. Kanca atlama bayrağı
oluşturma. Arka plan işi beklerken `pgrep -f` kullanma.

## Girdi
- Hükümler (EN SON dosya sayılır; `juri-olcutleri.md` §1b): kol a `K/projeler/<paket>/uretim-tutanagi/juri/J2-hukum-*.md` (tarihli olanların en
  yenisi), kol b `K/projeler/<paket>b/uretim-tutanagi/juri/KBJ-hukum-*.md`. Paketler: `02-04-ydt-temel-s1`, `-s2`, `-s3`, `simple-present-temel-s1`,
  `-s2`, `-s3`. Önce 12 tarihli hüküm dosyasının varlığını denetle; eksik varsa ön planda `sleep 300` ile en çok 6 kez yeniden bak; hâlâ eksikse
  eldekilerle çalış ve eksikleri raporun başına yaz.
- Önceki tur özeti: `K/uretim-hatti/raporlar/J3-OZET-1611.md` (A / B / C / K sınıfları ve §7 ana derse geri besleme). Düzeltme raporları:
  `…/uretim-tutanagi/DUZ4-RAPOR.md`. Ölçüt belgesi 16.11'de yamalandı (B1–B15; §2b "Kısa" sütunu; EK-4 ve EK-11 Ş maddesi) ve kapı
  16.11'de düzeltildi (K1, K3–K5; yeni KS-6f, KR-1): jüriler yeni metne göre hüküm verdi.
- Ölçütler: `D/.claude/docs/juri-olcutleri.md`. Standartlar: `huni-v2-standart.md`, `huni-ab-sozlesme.md`, `kapak-standardi.md`.
- Kapı betiği: `D/araclar/huni-kapi.mjs` (jürilerin "kapı hatası" dediği satırlar betik hatasıdır).

## Bu tura özel kurallar
- Hükümler: EN SON tarihli dosya; yalnız `DUZ4-RAPOR.md` dosyasından YENİ olan hüküm bu turun hükmüdür. Eski kalan paketi raporun başına yaz.
- Sayım tablosu başlık satırını ("| Bölüm | evet | hayır | kanıt yok |") hüküm satırı sayma. "şef bekliyor" / "Nadir bekliyor" (Ş) satırları
  kaldı değildir; ayrı listede topla (dinleme listesi ve adres gönderimi).
- **Ana ders kapağı (HV-7).** Kısaların çağrı sahnesi ana dersin kapağını gösterir. Ana dersler bu gece ayrı turda düzeliyor (DUZ3B / KNT); kapak
  ya da kapak metni değişebilir. Her çift için: çağrı sahnesindeki kapak görseli ana paketin bugünkü `kapak.png` dosyasıyla aynı mı (sha256 ya da
  kare karşılaştırması)? Farklıysa DUZ5 işine "ana ders kapağını ana paketin SON hâlinden kopyala, çağrı sahnesi karelerini yeniden çek" yaz
  ve "bu iş ana ders kilitlendikten sonra koşar" notunu düş. Aynı kural kısanın ana derse verdiği terim ve cümle göndermeleri için de geçerlidir.
- Jüri tutarsızlığı bu turda da varsa (aynı duruma farklı hüküm) hangi ölçüt cümlesinin yoruma açık kaldığını yaz; yeni ölçüt metni öner.
- Kapanış ölçütü: bir paket A = 0 ve üretilebilir C = 0 ise "teslim kapısından geçer"; Ş maddeleri (EK-4, EK-11) teslimi bloklamaz.
- DUZ5 istemine şu sabit satırlar girer: `surumler.json` revizyon notu ≤ 500 karakter ve `no` = `r<sayı>`; rapor ilk satırı `uretici_model`;
  KARELER EN SON çekilir (KR-1); 168 px kapak dosyaları (KS-6f) kapak değiştiyse yeniden üretilir.

## İş
1. Her hükümden kaldı maddelerini (hayır + kanıt yok) çıkar; tek tablo: madde × 12 paket.
2. Önceki turla (J3-OZET) karşılaştır: kapanan madde, süren madde, YENİ çıkan madde (düzeltme bir şeyi bozdu mu?).
3. Her kaldı maddeyi sınıfla, standart satırıyla:
   - **A · gerçek hata**: düzeltme (dosya, sahne, ses gerekir mi).
   - **B · ölçüt hatası**: ölçüt belgesi için önerilen yeni metin. Kısa videoya uygulanmaması gereken ders maddeleri (DK-…, ST-…, EK-…) varsa
     "kısa için geçerli mi" kararını standarttan gerekçelendir.
   - **C · kanıt eksikliği**: kanıtı ÜRETİM oturumu üretebilir mi (kontak sayfası, 168 px kapak, kare çifti, `hyperframes check` çıktısı, motor zaman
     kapısı çıktısı) yoksa yalnız insan mı verebilir (dinleme: Nadir; adres gönderim kaydı: şef)? İnsan kanıtı isteyen maddeler ayrı liste.
   - **K · kapı hatası**: betik için düzeltme tarifi (dosya:satır, beklenen davranış).
4. Jüri tutarsızlığı: aynı maddeye aynı durumda farklı hüküm veren jüriler.
5. **DUZ5 istemleri (yaz).** Kısa çifti başına bir istem dosyası: `K/uretim-hatti/istemler/DUZ5-0204S1.md`, `-0204S2`, `-0204S3`, `-0202S1`, `-0202S2`,
   `-0202S3`. Kalıp olarak `K/uretim-hatti/istemler/DUZ4-0204S1.md` dosyasının başlık, MAKİNE ve SABİT KURALLAR bölümünü aynen al (Silinecekler dizin
   adını `2026-11-16-duz5-<kod>` yap), sonra o çifte ÖZEL iş listesini yaz: yalnız A sınıfı düzeltmeler ve üretim oturumunun üretebileceği C sınıfı
   kanıtlar; her iş için dosya, sahne, beklenen sonuç ve kanıtın tutanakta duracağı yol. Tek değişken kuralları (AB-3, AB-8, AB-9) ve "kareye kendin
   bak" satırı kalır. İş listesi boşsa o çift için dosya yazma, raporda "DUZ5 gerekmez" de.
6. Teslim durumu: 12 paketin her biri için "kapıdan geçer mi" (A = 0 ve üretilebilir C = 0 ise evet); geçmeyenlerde kalan iş sayısı.

Son mesajın en çok 12 satır: kapanan / süren / yeni madde sayıları, A / B / C / K sayıları, insan kanıtı isteyen maddeler, yazılan DUZ5 istemleri,
ölçüt belgesinde değişecek maddeler, kapıdan geçen paket sayısı, rapor yolu.
