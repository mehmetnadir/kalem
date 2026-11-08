# Brief — oynatıcı v1 (prototip 0.1, 08.11.2026)

Amaç: Nadir'in oynatıcı PRD'sini görerek onaylaması. Gerçek paket (present-perfect-temel) üstünde çalışan
YouTube sınıfı kontrol kromu; site sayfası taslağı (`ydspublishing.com/grammar/<video>`).
Kitle: öğrenci (web masaüstü, mobil yatay/dikey); Nadir ve öğretmen (editör önizlemesi, F2 inceleme).
Kip: uygulama (oynatıcı kromu) + vitrin parçası (sayfa başlığı, bölüm kartları).
Marka: YDS Publishing logosu renkleri — lacivert `#13204D`, sarı `#fece00` (`ortak/logo/yds-publishing-lacivert.svg`);
yazı tipi Lexend (paket `ortak/font/`, künye ile aynı). Beyaz zemin; koyu tema eş (belirteçlerle).
Bileşen kaynağı: §4 sıra 4 (elle). Gerekçe: kalem deposunda React/shadcn yok; oynatıcı sahne iframe'lerine
`postMessage` saatiyle bağlı özel bileşen; var olan `onizle.js` çekirdeği uyarlandı (hesaplamadan önce §0).
Hareket bütçesi: uygulama kipi 100–300 ms (kontrol gizlenmesi 200 ms, tutamaç 120 ms); sahne geçişi K37
(bölüm → kıvrım 0,6 sn, bölüm içi → fade 0,4 sn); `prefers-reduced-motion` → geçiş yok, kıvrım yerine fade.
İlham: galeri kaydı yok (oynatıcı için referans verilmedi); ölçü Nadir sözü "YouTube gibi profesyonel"
(K36) ve `arastirma/oynatici-ozellik-envanteri-0811.md` (30 özellik, 12 kaynak).
Başarı ölçütü:
1. present-perfect-temel sahneleri editördeki ses saatiyle aynı anda oynar (sapma ≤ 0,1 sn; 6 sahne, 3 motor).
2. Masaüstü 1440 ve telefon 390 ekran görüntülerinde emoji 0, dokunma alanı ≥ 44 px, odak halkası görünür.
3. Oynatma sırasında sunucu ucu 0 (statik paket), tam ekran ve klavye kısayolları çalışır.
Varsayımlar: `zaman.json.bolum` alanı henüz yok → bölüm = sahne `ad`, geçiş türü = önceki sahnenin `gecis`
alanı (BookFlip → kıvrım, fade → fade). Ses wav olduğu gibi (m4a kararı PRD açık soru 1).
