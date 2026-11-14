# İstem A — 02-04-ydt-temel senaryo taslağı (sunucuda üretilen ilk ders, 14.11.2026)

MAKİNE: Linux x86_64 (srv21), kullanıcı sef. Çalışma kökü (git worktree, dal `sunucu/02-04-ydt-temel`):
`/home/sef/01dev/_worktrees/kalem-0204` (aşağıda K). Kaynak deposu `/home/sef/01dev/dijital-anlatim` (aşağıda D).
Python `/usr/bin/python3 -I` (3.10). Node `~/.nvm/versions/node/v24.22.2/bin/node`.
Skill dosyaları `~/.claude/skills/motion-grafik-ders/` (SKILL.md + references/).

KURALLAR: Yalnız isteneni yaz. Silme yok (gerekirse `~/Silinecekler/2026-11-14-0204/` altına taşı). Render yok, mp4 yok.
git commit / push yok (şef yapar). Ses üretimi yok (ElevenLabs çağrısı yok). Kaynakta olmayan kural ekleme.
Alt ajan açma; işi kendin yap. Yazdığın dosyalar yalnız `K/projeler/02-04-ydt-temel/uretim-tutanagi/` altında.

## Görev

Ders: `02-04-ydt-temel` · kod `ING-YDT-GR-02-04-T` · GR-02-04 · Tenses (02) · "Simple Present vs Present Continuous" · YDT · temel ·
yatay 16:9 · sesler öğretmen Atakan + öğrenci Gökçe Deniz (eleven_v4) · süre iddiası YOK.
Bu dersin senaryo taslağını yaz. Taslak sonra 3 bağımsız jüriye gidecek (kaynak, kural, dil).

## Okuma sırası (hepsini oku, atlama)

1. Skill: `SKILL.md`, `references/stil-anayasasi.md`, `ses-tasarimi.md`, `hareket-sozlugu.md`, `tempo-ve-pedagoji.md`,
   `soru-ani.md`, `kliseler.md`, `uretim-yolu.md`.
2. Proje defteri: `D/.claude/docs/grammar-defter.md` (son 120 satır; Nadir notları, D-0204, D-0205 kararları).
3. Biçim örneği (aynı hattın bir önceki dersi, jüriden geçti): `K/projeler/02-03-ydt-temel/uretim-tutanagi/senaryo-taslak.md`
   ve `juri.md`. Tablonun sütunlarını, bölüm adlarını ve ses metni yazımını bu örnekten al.
4. Katalog: `D/varlik/grammar/katalog.json` ve `D/varlik/grammar/konu-adlari.json` içinde 02-01 … 02-06 ydt satırları.
   Komşu dersler: 02-01 Present Continuous, 02-02 Simple Present, 02-03 ayrım alıştırması, 02-05 (başlığını katalogdan oku).
   02-04 komşularının konusunu yinelemez; 02-05'in konusunu (katalogdaki başlık) bu derse taşıma, en çok bir cümleyle işaret et.
5. Kaynak 1 — pptx: `D/varlik/grammar/kaynak-pptx/YEDEK/Tenses/unit-1_sunum-3 uygun.pptx`. Metni python `zipfile` ile çıkar
   (`ppt/presentation.xml` + `ppt/_rels/presentation.xml.rels` slayt sırası; her `ppt/slides/slideN.xml` içindeki `a:t` metinleri).
   python-pptx kurma. Hangi slaytlar 02-04'ün konusudur, gerekçesiyle seç.
6. Kaynak 2 — eski ders dökümü (Doğan Hoca, Vimeo 863572960, "02 - tenses - 04"): `D/varlik/grammar/transkript-whisper/863572960.md`.

## Çıktı 1 — `uretim-tutanagi/istem/A-girdi.md`

Künye tablosu · seçilen pptx slaytları (slayt no + çıkarılan metnin tamamı) · seçilmeyen slaytlar ve neden ·
dökümden alınan kapsam maddeleri (zaman damgalı, en çok 25 madde) · komşu ders sınırı (02-03 ve 02-05 ile örtüşmeyen kapsam).

## Çıktı 2 — `uretim-tutanagi/senaryo-taslak.md`

02-03 örneğiyle aynı yapı: başlık, künye, kaynak eşleme tablosu (kaynak → taslak satırı), sonra 8 bölümlü senaryo tablosu
(kanca → 3 örnek → kural kartı → karşıt çift → tuzak → ara özet → mini soru → kapanış; skill'deki süre payları hedef, süre iddiası yok),
her satırda konuşan (öğretmen/öğrenci), ses metni (söylenen; tr/en parçaları belli), ekran metni, görsel fikir (hareket sözlüğü
olay adlarıyla), tahmini sn. Öğrenci sesi: 2 soru + 1 yanlış cevap (soru-ani.md). Konuşmada "YDT" kısaltması yok, "dil sınavı" de.
İngilizce örnekler YDT düzeyinde, doğal ve kaynakla uyumlu. Sonda "Açık noktalar" (jüriye soru) listesi.

## Bitince

Son mesajın en çok 20 satır: yazdığın 2 dosyanın yolu, seçilen slaytlar, toplam tahmini süre, açık noktalar.
