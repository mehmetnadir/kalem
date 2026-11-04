// Görev haritası modeli (DOM yok): ağaç, sayım, dağılım, açık-küme, arama, URL.
// Kimlik: ünite "02" · konu "02-01" · video "02-01-ydt-temel" · sürüm "<video>/<sürüm>".

export const VIDEO_DURUM = ['planli', 'hazirlik', 'uretimde', 'inceleme', 'onay', 'yayinda'];
export const DERINLIK = ['unite', 'konu', 'video', 'hepsi'];

export const konuKimlik = (kod) => String(kod).replace(/^GR-/, '');

// Metin eşleştirme için: küçük harf, Türkçe harf katlama, boşluk daraltma.
export function normalle(s) {
  const t = { ç: 'c', ğ: 'g', ı: 'i', ö: 'o', ş: 's', ü: 'u', â: 'a', î: 'i', û: 'u' };
  return String(s ?? '').replace(/İ/g, 'i').toLowerCase().replace(/[çğıöşüâîû]/g, (c) =>
    t[c])
    .replace(/\s+/g, ' ').trim();
}

export function agacKur(katalog) {
  const unite = new Map(); const konu = new Map(); const video = new Map();
  const uniteler = katalog.uniteler.map((u) => {
    const un = { tur: 'unite', id: u.kod, kod: u.kod, ad: u.ad, ham: u, ata: null, konular: [] };
    unite.set(un.id, un);
    for (const q of u.konular) {
      const kn = { tur: 'konu', id: konuKimlik(q.kod), kod: q.kod, ad: q.ad, ham: q, ata: un,
        lms: q.lms || [], pptx: q.pptx || [], videolar: [] };
      konu.set(kn.id, kn); un.konular.push(kn);
      for (const v of q.videolar) {
        const vd = { tur: 'video', id: v.kimlik, kimlik: v.kimlik, kod: v.kod, kitle: v.kitle,
          seviye: v.seviye,
          durum: v.durum, proje: v.proje || null, eskiKod: v.eskiKod || null, not: v.not || null,
            ata: kn };
        video.set(vd.id, vd); kn.videolar.push(vd);
      }
    }
    return un;
  });
  return { uniteler, unite, konu, video, katalog };
}

export function sayimlar(agac) {
  let konu = 0; let kaynak = 0;
  for (const u of agac.uniteler) { konu += u.konular.length;
    for (const k of u.konular) kaynak += k.lms.length; }
  return { unite: agac.uniteler.length, konu, kaynak, video: agac.video.size };
}

// Projeli videoya sürümleri bağlar (v.surumler). Veri: { [proje]: { sv, gorevler } }.
export function projeBagla(agac, projeler) {
  for (const v of agac.video.values()) {
    const p = v.proje && projeler[v.proje];
    v.surumler = p && p.sv ? p.sv.surumler || [] : [];
  }
}

// Videonun görevleri: projeliyse proje görevleri, değilse katalog deposunda video === kimlik.
export function videoGorevleri(v, projeler, depo) {
  if (v.proje && projeler[v.proje]) return projeler[v.proje].gorevler || [];
  return (depo || []).filter((g) => g.video === v.kimlik);
}

export function durumDagilimi(videolar) {
  const d = Object.fromEntries(VIDEO_DURUM.map((x) => [x, 0]));
  for (const v of videolar) d[v.durum] = (d[v.durum] || 0) + 1;
  return d;
}
export function uniteVideolari(u) { return u.konular.flatMap((k) => k.videolar); }

export function konuOzet(k) {
  const sure = k.lms.reduce((a, l) => a + (l.sure || 0), 0);
  const izlenme = k.lms.reduce((a, l) => a + (l.izlenme || 0), 0);
  const tamamlama = k.lms.reduce((a, l) => a + (l.tamamlama || 0), 0);
  const ort = k.lms.length ? Math.round(k.lms.reduce((a, l) => a + (l.ortYuzde || 0),
    0) / k.lms.length) : 0;
  return { sure, sureDk: Math.round(sure / 60), izlenme, tamamlama, ortYuzde: ort };
}
export function uniteOzet(u) {
  const vs = uniteVideolari(u); let sure = 0; let toplam = 0; let adet = 0;
  for (const k of u.konular) for (const l of k.lms) { sure += l.sure || 0; toplam += l.ortYuzde
    || 0; adet++; }
  return { konu: u.konular.length, video: vs.length, sureDk: Math.round(sure / 60),
    ortYuzde: adet ? Math.round(toplam / adet) : 0, dagilim: durumDagilimi(vs) };
}

// ---- açık-küme: Set<kimlik> ----
export const degistir = (acik, id) => { const s = new Set(acik); if (!s.delete(id)) s.add(id);
  return s; };
export const ac = (acik, id) => new Set([...acik, id]);
export const kapat = (acik, id) => { const s = new Set(acik); s.delete(id); return s; };
export const hepsiniKapat = () => new Set();

function surumKimlikleri(v) { return (v.surumler || []).map((s) => `${v.id}/${s.kimlik}`); }
export function hepsiniAc(agac) {
  const s = new Set();
  for (const u of agac.uniteler) { s.add(u.id); for (const k of u.konular) { s.add(k.id);
    for (const v of k.videolar) { s.add(v.id); for (const x of surumKimlikleri(v)) s.add(x); } } }
  return s;
}
// unite: yalnız ünite açık · konu: + konu · video: + video · hepsi: + sürüm.
export function derinlik(agac, d) {
  const s = new Set(); const i = DERINLIK.indexOf(d);
  if (i < 0) throw new Error(`geçersiz derinlik: ${d}`);
  for (const u of agac.uniteler) {
    if (i >= 0) s.add(u.id);
    for (const k of u.konular) {
      if (i >= 1) s.add(k.id);
      for (const v of k.videolar) {
        if (i >= 2) s.add(v.id);
        if (i >= 3) for (const x of surumKimlikleri(v)) s.add(x);
      }
    }
  }
  return s;
}
// Bir düğümün atalarını (kendisi dahil) döndürür. Sürüm kimliği "<video>/<sürüm>".
export function yol(agac, id) {
  const sira = [];
  let dugum = agac.video.get(id) || agac.konu.get(id) || agac.unite.get(id);
  if (!dugum && id.includes('/')) {
    dugum = agac.video.get(id.split('/')[0]);
    if (dugum) sira.push(id);
  }
  for (; dugum; dugum = dugum.ata) sira.push(dugum.id);
  return sira.reverse().length ? sira : [];
}
const bilinir = (agac, id) => agac.video.has(id) || agac.konu.has(id) || agac.unite.has(id)
  || (id.includes('/') && agac.video.has(id.split('/')[0]));

// ---- URL ?ac=02,02-01,02-01-ydt-temel ----
export function urlUret(acik) { return [...acik].sort().join(','); }
export function urlCoz(agac, metin) {
  const s = new Set();
  for (const id of String(metin || '').split(',').map((x) => x.trim()).filter(Boolean)) {
    if (!bilinir(agac, id)) continue;
    for (const a of yol(agac, id)) s.add(a);
    if (id.includes('/')) s.add(id);
  }
  return s;
}
export function sonKimlik(agac, metin) {
  const l = String(metin || '').split(',').map((x) => x.trim()).filter((x) => x && bilinir(agac,
    x));
  return l.length ? l[l.length - 1] : null;
}

// ---- arama ----
// eslesen: doğrudan · canli: eşleşen + ata + torun · ac: açılacak yol.
export function arama(agac, sorgu) {
  const q = normalle(sorgu);
  const sonuc = { eslesen: new Set(), canli: new Set(), ac: new Set(), aktif: q !== '' };
  if (!q) return sonuc;
  const var_ = (...m) => m.some((x) => normalle(x).includes(q));
  const torunlar = (d) => {
    sonuc.canli.add(d.id);
    for (const c of d.konular || d.videolar || []) torunlar(c);
  };
  const atalar = (d) => { for (let a = d.ata; a; a = a.ata) { sonuc.canli.add(a.id);
    sonuc.ac.add(a.id); } };
  for (const u of agac.uniteler) {
    if (var_(u.kod, u.ad)) { sonuc.eslesen.add(u.id); torunlar(u); }
    for (const k of u.konular) {
      if (var_(k.kod, k.id, k.ad, ...k.lms.map((l) => l.ad))) {
        sonuc.eslesen.add(k.id); torunlar(k); atalar(k); sonuc.ac.add(k.id);
      }
      for (const v of k.videolar) {
        if (var_(v.kimlik, v.kod, v.eskiKod || '')) {
          sonuc.eslesen.add(v.id); sonuc.canli.add(v.id); atalar(v);
        }
      }
    }
  }
  return sonuc;
}

// ---- filtre (kitle, video durumu) ----
export const videoGecer = (v, f) => (!f.kitle || v.kitle === f.kitle) && (!f.vdurum
  || v.durum === f.vdurum);
export function filtreAktif(f) { return Boolean(f.kitle || f.vdurum); }

// ---- kırıntı ve sec çözümü ----
const agacYap = (k) => (k && k.uniteler && !k.unite ? agacKur(k) : k);
const yolListe = (yol) => (Array.isArray(yol) ? yol : String(yol || '').split(','))
  .map((x) => String(x).trim()).filter(Boolean);

// Proje adına bağlı videonun yolu: ["02", "02-01", "02-01-ydt-temel"] (yoksa []).
export function projeYolu(katalog, proje) {
  const agac = agacYap(katalog);
  for (const v of agac.video.values()) if (v.proje === proje) return yol(agac, v.id);
  return [];
}

// Kırıntı: Harita ▸ ünite ▸ konu ▸ video. Her öğe ac/sec taşır.
export function kirinti(katalog, yolMetni) {
  const agac = agacYap(katalog);
  const kitle = (agac.katalog.kitleler || {}); const sev = (agac.katalog.seviyeler || {});
  const ogeler = [{ ad: 'Harita', ac: '', sec: '' }]; const acik = [];
  for (const id of yolListe(yolMetni)) {
    const d = agac.unite.get(id) || agac.konu.get(id) || agac.video.get(id);
    if (!d) continue;
    acik.push(id);
    const ad = d.tur === 'unite' ? `${d.kod} ${d.ad}`
      : d.tur === 'konu' ? `${d.id} ${d.ad.replace(/^\d+\s*-\s*/, '')}`
        : `${kitle[d.kitle] || d.kitle} ${sev[d.seviye] ? sev[d.seviye].toLowerCase() : d.seviye}`;
    ogeler.push({ ad, ac: acik.join(','), sec: id });
  }
  return ogeler;
}
export const kirintiAdresi = (o) => {
  const q = [o.ac ? `ac=${encodeURIComponent(o.ac)}` : '', o.sec
    ? `sec=${encodeURIComponent(o.sec)}` : '']
    .filter(Boolean).join('&');
  return `harita.html${q ? `?${q}` : ''}`;
};

// ?sec=<kimlik>: ünite, konu ya da video; açılacak yol ile birlikte. Bilinmeyen -> null.
export function secCoz(agac, sec) {
  const id = String(sec || '').trim();
  const d = agac.video.get(id) || agac.konu.get(id) || agac.unite.get(id);
  if (!d) return null;
  const ata = yol(agac, id);
  return { tur: d.tur, id, ac: new Set(d.tur === 'unite' ? ata : ata.slice(0, -1)),
    panel: d.tur === 'video' };
}
