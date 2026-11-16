# İstem DJ-@KOD@ — `@PA@` (ve `@PA@-dikey`) ana ders ÇIKTI jürisi · 16.11.2026

MAKİNE: Linux x86_64 (srv21), kullanıcı sef. K=`/home/sef/01dev/_worktrees/kalem-0204` (worktree), D=`/home/sef/01dev/dijital-anlatim`.
SABİT KURALLAR: SALT OKUMA; hiçbir üretim dosyasını değiştirme. Silme yok, git commit yok, alt ajan yok, agy-filo yok, mp4 yok, ses sentezi yok.
`.env` okuma. Kanca atlama bayrağı oluşturma. Arka plan işi beklerken `pgrep -f` kullanma.
YAZMA ALANI: yalnız `K/projeler/@PA@/uretim-tutanagi/juri/DJ-hukum-<GGAA-SSDD>.md` (ad şimdiki zamandan: `date +%d%m-%H%M`; dizini aç). Var olan
hüküm dosyalarına DOKUNMA (`juri-olcutleri.md` §1b: önceki hüküm kalır, en son hüküm sayılır).

## Jüri kuralları (`juri-olcutleri.md` §1)
- TASLAĞA değil ÇIKTIYA bakarsın: karelere (`sahneler/*/k/*.png`; Read ile aç), sesin metnine (senaryo cümleleri + Whisper kaydı varsa o),
  altyazıya, kapaklara, `youtube.json` ve `youtube-aciklama.md` dosyalarına.
- "Kaynağa uygun" ≠ "doğru": her kural cümlesini, her Türkçe–İngilizce denkliğini ve her örnek cümleyi dil bilgisi açısından KENDİN denetle
  (mutlak kural, dersin kendi örneğiyle çelişen cümle, yanlış denklik). Şüphelendiğin cümleye karşı örnek yaz.
- Her madde: kimlik | hüküm (evet / hayır / kanıt yok / uygulanmaz) | kanıt (dosya:satır ya da kare adı) | not. Kaçamak hüküm yok.
- Kendi model adını ve üretici modeli (raporda yazıyorsa) hüküm dosyasının başına yaz.

## İş
1. Oku: `D/.claude/docs/juri-olcutleri.md` (tamamı), `kapak-standardi.md`, `youtube-yayin-verisi-sozlesme.md` §2, `youtube-surumu-standart.md` §3.
2. Paket: `K/projeler/@PA@/` ve `K/projeler/@PA@-dikey/` (varsa). Düzeltme raporu varsa oku: `uretim-tutanagi/DUZ3-RAPOR.md` (ya da `DUZ2-RAPOR.md`);
   raporun "düzeltildi" dediği her cümleyi çıktıda ara (ses metni, kart, altyazı, kapak); eski cümle bir yerde kaldıysa "hayır".
3. §2b (ders) BÜTÜN maddelerine, §2c (kapak) maddelerine (yatay + dikey kapak, açık + koyu) ve §2f (yayın verisi YV-1…9) maddelerine hüküm ver.
   Dersin BÜTÜN cümlelerini tek tek oku (yalnız düzeltilenleri değil); tablo: cümle no | metin | doğru mu | karşı örnek ya da not.
4. Rozet: künyede `YDT · TEMEL` / `YDT · İLERİ` mi (`BASIC` yasak; HV-24 derse de uygulanır).
5. Yatay ile dikey tutarlı mı: aynı cümleler, aynı ses (sha256), aynı başlık/açıklama/etiket; dikey karelerde taşma ve güvenli alan.
6. Tutarlılık kapısı çıktısını ekle: `python3 K/uretim-hatti/betikler/yv-tutarlilik.py --kilitli
   simple-present-temel,simple-present-temel-dikey,02-04-ydt-temel-dikey` (çıkış kodu ve bu derse düşen satırlar).
7. Hüküm dosyası: özet (geçti / kaldı / kanıt yok sayıları), cümle tablosu, madde tablosu, kaldı maddeleri için düzeltme önerisi (tek cümle).
8. Kalıcılık tablosu (hükmün sonunda, ZORUNLU): önceki hükmü (aynı paketteki bir önceki `DJ-hukum-*.md`) oku; her `hayır` kimliği için bir satır:
   `| kimlik | önceki hükümde? | arada düzeltme turu var mı | sınıf a–e |`. "Arada düzeltme turu" = önceki hükümden sonra değişen `DUZ*-RAPOR.md` ya da
   paket dosyası (mtime). Sınıf: a render gerektirir · b düzeltilebilir · c ölçüt belirsiz ya da çelişkili · d kaynak/veri sorunu · e ölçüm aracı eksik.
   Araya düzeltme turu girmediyse hükmün BAŞINA "aynı durum yeniden yargılandı" satırı yaz; hayır sayısının artışını gerileme sayma.
9. EK-5b / EK-5c `hayır` satırı karşı örnek + önerilen kapsam sözcüğü taşımak zorundadır (örn. "çoğu zaman", "durum anlamında"); ikisi de yoksa
   satır eksik sayılır. Düzeltici öneriyi uygular ya da karşı gerekçe yazar.

Son mesajın en çok 10 satır: geçti / kaldı / kanıt yok sayıları, yanlış bulduğun cümleler (no + tek cümle), kaldı maddeleri (kimlik + tek cümle),
jüri modeli.
