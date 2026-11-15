# Üretim hattı — istem şablonları ve yardımcı betikler

Kaynak: srv21 `/home/sef/is/uretim-0204/` çalışma dizininin kalıcı kopyası (15.11.2026). Sunucu dizini bunun türevidir.
Bağlayıcı standartlar: `~/01dev/dijital-anlatim/.claude/docs/` (huni-v2, kapak, youtube-surumu, huni-ab, juri-olcutleri).

| Dosya | Aşama | Ne zaman |
|---|---|---|
| `istemler/A-senaryo.md`, `S?-A.md`, `SN-A.md`, `P0202-S?-A.md` | A senaryo taslağı | ders ya da kısa başlarken |
| `istemler/B-juri-*.md`, `B2-juri-*.md` | B ders jürisi (kaynak, kural, dil; tur 2) | senaryo taslağı bitince |
| `istemler/S?-B-kural.md`, `S?-B-dil.md`, `S1-B.md` | B kısa jürisi (v2) | kısa taslağı ve çıktısı için |
| `istemler/S?-C.md`, `V2-S?-C.md`, `C-paket.md`, `P0202-C-*.md` | C paket üretimi (zaman.json, kapak, hikâye, açıklama) | jüri GEÇTİ sonrası |
| `istemler/D-*.md`, `D/D-NN-*.md`, `D-sahne-sablon.md` | D sahne yazımı (ders) | paket hazır olunca |
| `istemler/KAPAK-*.md`, `S1-KAPAK-A.md` | kapak üretimi | kapak-standardi.md |
| `istemler/hk/`, `bk/`, `hk-uret.py`, `bk-uret.py` | huni kolu (konu adayı, A/B kol b) | A/B planı |
| `istemler/DUZ-1.md`, `A2-duzelt.md`, `W-02-duzelt.md`, `duzelt-istem.py` | düzeltme turları | jüri DÜZELT sonrası |
| `istemler/RUNBOOK.md` | uçtan uca koşu defteri | hat kurarken |
| `betikler/kos.sh`, `kos-devam.sh` | sunucuda başsız iş başlatma | her iş |
| `betikler/sonra.sh`, `sonra2.sh`, `zincir*.sh`, `sahne-kuyruk*.sh` | zincir, kuyruk | biten yerine yenisi |
| `betikler/oku.py`, `bekle.sh` | sonuç oku, durum bekle | iş sonrası |
| `betikler/kontak.py`, `render-*.sh`, `olc*.sh` | kontak sayfası, ölçüm | görsel denetim |
| `betikler/kapasite*.sh`, `takili-bekci.sh` | kapasite, takılı bekleyici | izleme |

## Kullanım
- `kos.sh <ad> <model> <istem-dosyası>` — ayrık oturumda başsız Claude işi; çıktı `~/is/uretim-0204/<ad>.json`, `.err`, `.durum`, `.bitti`.
- `sonra.sh <beklenen-ad> <iş-adı>…` — beklenen iş `bitti 0` olunca her iş için `kos.sh` başlatır.
- `oku.py <ad> [karakter]` — iş sonucunu okur.
- `bekle.sh <durum-dosyası>…` — biri `bitti` olunca çıkar (en çok 90 dk).

## Sabit kurallar
1. Silme yok; eski koşu dosyası `eski/<zaman>/` altına taşınır.
2. `pgrep -f` ile bekleme yok (başsız oturum kendini eşler); durum dosyası ya da `bekle.sh` kullan.
3. mp4 yalnız Nadir'in açık sözüyle.
4. Kanca atlama bayrağı yok.
5. Jüri çıktıyı görür, içerik değişince yeniden koşar, modeli üreticiden farklıdır.
