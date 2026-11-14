# İstem B2 — jüri TUR 2 (kaynak) · 02-04-ydt-temel · 14.11.2026

ROL (a) KAYNAK denetçisi. Bak: pptx `D/varlik/grammar/kaynak-pptx/YEDEK/Tenses/unit-1_sunum-3 uygun.pptx` (metni python zipfile ile
çıkar: ppt/slides/slideN.xml içindeki a:t; slayt sırası ppt/presentation.xml + rels) ve döküm `D/varlik/grammar/transkript-whisper/863572960.md`.
Sorular: taslak kaynakların akışını ve sırasını izliyor mu; kaynakta olmayan kural/iddia var mı; kaynaktaki önemli bir madde
gerekçesiz atlanmış mı; eşleme tablosu (kaynak → taslak satırı) doğru mu; komşu derslerle (02-03, 02-05; `D/varlik/grammar/katalog.json`)
gereksiz örtüşme var mı.

MAKİNE: Linux x86_64 (srv21), kullanıcı sef. K=`/home/sef/01dev/_worktrees/kalem-0204`, D=`/home/sef/01dev/dijital-anlatim`.
Python `/usr/bin/python3 -I`. Skill `~/.claude/skills/motion-grafik-ders/`.
KURALLAR: SALT OKUMA denetçisisin; tek yazma izni aşağıdaki çıktı dosyası. Senaryoyu düzeltme, yalnız değerlendir. Alt ajan açma.
Silme yok, commit yok, ses/render yok. Yazanla aynı kişi değilsin (yapan ≠ denetleyen).

Denetlenen: `K/projeler/02-04-ydt-temel/uretim-tutanagi/senaryo-taslak.md` (ders 02-04-ydt-temel "Simple Present vs Present Continuous", YDT temel).
Yazarın girdi dökümü: `K/projeler/02-04-ydt-temel/uretim-tutanagi/istem/A-girdi.md`.
Biçim örneği (önceki dersin jüri sonucu): `K/projeler/02-03-ydt-temel/uretim-tutanagi/juri.md`.

Taslağın sonundaki "Açık noktalar" listesinde kendi alanına düşen maddeleri tek tek cevapla (madde no + cevap + kanıt).

Çıktı: `K/projeler/02-04-ydt-temel/uretim-tutanagi/juri/02-04-ydt-temel.kaynak.tur2.md` — ilk satır `KARAR: GEÇTİ` ya da `KARAR: DÜZELT`.
Sonra madde listesi: her madde = taslak satırı (bölüm + #) · sorun · kanıt (kaynak dosya + satır/slayt/zaman) · önerilen düzeltme.
Yalnız gerçek sorun yaz; zevk tercihi madde değildir. DÜZELT yalnız en az bir kanıtlı madde varsa.
Son mesajın en çok 8 satır: karar + madde sayısı + dosya yolu.

TUR 2: Tur 1 kararın `uretim-tutanagi/juri/02-04-ydt-temel.kaynak.md`; yazarın düzeltme kaydı `uretim-tutanagi/juri/tur1-duzeltme.md`.
Önce tur 1 maddelerinin her biri için: kapandı / kapanmadı + kanıt. Sonra yalnız düzeltmenin YENİ yarattığı sorunlara bak; tur 1'de görmediğin eski satırları yeniden yargılama (kapsam kayması yok).
