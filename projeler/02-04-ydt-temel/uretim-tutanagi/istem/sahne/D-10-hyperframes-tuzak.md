# İstem D — 02-04-ydt-temel sahne 10-hyperframes-tuzak (P2) · 14.11.2026

MAKİNE: Linux x86_64 (srv21), kullanıcı sef. K=`/home/sef/01dev/_worktrees/kalem-0204` (git worktree, dal `sunucu/02-04-ydt-temel`).
Node `~/.nvm/versions/node/v24.22.2/bin`. Python `/usr/bin/python3 -I`. Skill `~/.claude/skills/motion-grafik-ders/`.
KURALLAR: Yalnız bu sahnenin dizinine yaz: `K/projeler/02-04-ydt-temel/sahneler/10-hyperframes-tuzak/`. Başka sahneye, `ortak/`a, BRIEF'e,
senaryoya, sese dokunma (ortakta eksik görürsen raporla). Silme yok (`~/Silinecekler/2026-11-14-0204/` altına taşı).
mp4 render YOK: `calistir.sh`'ı yalnız `ONIZLE_YALNIZ=1` ile koş (kare/video çekme yok). git commit yok. Alt ajan açma.

## Okuma
1. Skill `SKILL.md`, `references/kalem-hatti.md`, `stil-anayasasi.md`, `hareket-sozlugu.md`, `kliseler.md`, `soru-ani.md` (soru sahnesiyse).
2. Paket: `K/projeler/02-04-ydt-temel/BRIEF.md` (§3 sahne planındaki 10. satır: tablodaki No 10 satırını aynen uygula), `zaman.json` (bu sahnenin t_bas/t_son,
   kare sayısı), `ortak/anlatim/senaryo.json` + `sozcukler.json` + `baslar.json` (cümle 11, 12 (öğrenci) sözcük zamanları: olay söylendiği anda gelir),
   `uretim-tutanagi/senaryo-taslak.md` (görsel fikir sütunu).
3. Örnek (aynı motor, aynı hattın önceki dersi; dosya yapısını ve calistir.sh kalıbını buradan al, içeriği değil):
   `K/projeler/02-03-ydt-temel/sahneler/10-hyperframes-tuzak/`.

## Yaz
`sahneler/10-hyperframes-tuzak/` içinde örnekle aynı dosya yapısı (HyperFrames: `uret.py`/`olay.py`/`yardim.py` + `calistir.sh`; Paper.js/canvas:
`sayfa.html` + sahne js + `calistir.sh`). Kurallar: tek vurgu sarı (temaya göre `RENK`), doğru şık yeşil, kırmızı yok, emoji yok;
yazı tabanı yatay 30 mantıksal px; sabit px yok (oran); ekran metni senaryodaki ekran metni sütunu; künye ve tema çifti (açık + koyu)
`ortak/kunye.js` ile. `calistir.sh` kalıbı: `[ -d /opt/homebrew/bin ] && export PATH="/opt/homebrew/bin:$PATH"`, yük `Y=$(yuk1)` (ortak/tema.sh).

## Doğrula (zorunlu, geçmeden bitirme)
`cd K && bash araclar/qa-yerel.sh 02-04-ydt-temel 10-hyperframes-tuzak <açık t1,t2,t3> <koyu t> --hazirla`
(t değerleri sahne içi saniye; olayların bittiği 3 an + koyu için 1 an). Çıkış kodu 0 olmalı (çakışma yok, ölçüm hatası yok).
Üretilen PNG'lere (`sahneler/10-hyperframes-tuzak/k/` ve `k/koyu/`) Read aracıyla BAK: taşma, kesilen yazı, üst üste binme, okunmaz kontrast,
boş kare varsa düzelt ve yeniden koş. En çok 4 düzeltme turu; geçmezse dur ve raporla.

## Rapor
`sahneler/10-hyperframes-tuzak/RAPOR.md`: olay listesi (olay · kare/zaman · cümle sözcüğü), kapı sonucu (son çıktı satırları), bakılan kareler ve
bulgu, açık noktalar. Son mesajın en çok 10 satır: kapı çıkış kodu, kare yolları, açık noktalar.
