// Önizleme + görev haritası sunucusu (Node, bağımlılıksız).
// Paket kökünü statik sunar (Range destekli), /api/<proje>/... JSON ucunu verir ve
// /p/<proje>/{harita,onizle}.html editörünü ortak/editor/ içinden sunar.
// Kullanım: node ortak/onizle-sunucu.mjs [--port 3012] [--kok <dizin>]
import http from 'node:http';
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const ENUM = {
  gorevTur: ['uret', 'duzelt', 'turev', 'karar'],
  gorevDurum: ['acik', 'uretimde', 'inceleme', 'onay', 'kapali'],
  atanan: ['sef', 'ajan', 'Nadir'],
  grup: ['motor', 'oynatici', 'senaryo', 'tasarim-karar', 'platform'],
  oncelik: ['dusuk', 'orta', 'yuksek'],
  surumTur: ['ana-yatay', 'dikey', 'shorts', 'alternatif'],
  surumDurum: ['planli', 'uretimde', 'inceleme', 'onay', 'kapali'],
  yazar: ['Nadir', 'sef', 'ajan'],
  yorumDurum: ['acik', 'cozuldu'],
};
const MIME = {
  '.html': 'text/html; charset=utf-8', '.js': 'text/javascript; charset=utf-8',
  '.mjs': 'text/javascript; charset=utf-8', '.css': 'text/css; charset=utf-8',
  '.json': 'application/json; charset=utf-8', '.png': 'image/png', '.jpg': 'image/jpeg',
  '.svg': 'image/svg+xml', '.wav': 'audio/wav', '.mp3': 'audio/mpeg', '.mp4': 'video/mp4',
  '.ttf': 'font/ttf', '.woff2': 'font/woff2', '.md': 'text/markdown; charset=utf-8',
  '.txt': 'text/plain; charset=utf-8',
};
const MAX_GOVDE = 1024 * 1024;
const EDITOR_DIZINI = path.join(path.dirname(fileURLToPath(import.meta.url)), 'editor');
const EDITOR_DOSYA = new Set(['harita.html', 'harita.js', 'harita.css', 'harita-model.js',
  'onizle.html', 'onizle.js', 'onizle.css', 'yol.js']);

class HataApi extends Error {
  constructor(kod, mesaj) { super(mesaj); this.kod = kod; }
}

function gecerli(deger, liste, ad) {
  if (!liste.includes(deger)) {
    throw new HataApi(400, `geçersiz ${ad}: "${deger}" (izinli: ${liste.join(', ')})`);
  }
  return deger;
}
function metin(deger, ad, zorunlu = false) {
  if (deger === undefined || deger === null || deger === '') {
    if (zorunlu) throw new HataApi(400, `${ad} zorunlu`);
    return undefined;
  }
  if (typeof deger !== 'string') throw new HataApi(400, `${ad} metin olmalı`);
  return deger.trim();
}
function sayi(deger, ad) {
  if (deger === undefined || deger === null || deger === '') return undefined;
  const n = Number(deger);
  if (!Number.isFinite(n) || n < 0) throw new HataApi(400, `${ad} geçerli bir sayı değil`);
  return n;
}
function sonrakiKimlik(liste, onek) {
  let en = 0;
  for (const o of liste) {
    const m = String(o.kimlik || '').match(new RegExp(`^${onek}-(\\d+)$`));
    if (m) en = Math.max(en, Number(m[1]));
  }
  return `${onek}-${en + 1}`;
}
function kisaAd(ad) {
  const t = { ç: 'c', ğ: 'g', ı: 'i', ö: 'o', ş: 's', ü: 'u', Ç: 'c', Ğ: 'g', İ: 'i',
    Ö: 'o', Ş: 's', Ü: 'u' };
  return ad.replace(/[çğıöşüÇĞİÖŞÜ]/g, (c) => t[c]).toLowerCase()
    .replace(/[^a-z0-9]+/g, '-').replace(/^-+|-+$/g, '').slice(0, 40) || 'surum';
}

export function sunucuKur({ kok }) {
  const KOK = path.resolve(kok);
  const kuyruk = new Map(); // proje -> zincir (tek süreç kilidi)

  function kilitle(proje, is) {
    const onceki = kuyruk.get(proje) || Promise.resolve();
    const sonraki = onceki.then(is, is);
    kuyruk.set(proje, sonraki.catch(() => {}));
    return sonraki;
  }
  function projeDizini(proje) {
    if (!/^[a-z0-9][a-z0-9-]*$/.test(proje)) throw new HataApi(400, 'geçersiz proje adı');
    const d = path.join(KOK, 'projeler', proje);
    if (!fs.existsSync(d) || !fs.statSync(d).isDirectory()) throw new HataApi(404,
      `proje yok: ${proje}`);
    return d;
  }
  function oku(dizin, ad, varsayilan) {
    try { return JSON.parse(fs.readFileSync(path.join(dizin, ad), 'utf8')); }
    catch (e) { if (e.code === 'ENOENT') return varsayilan; throw new HataApi(500,
      `${ad} okunamadı: ${e.message}`); }
  }
  function yaz(dizin, ad, veri) {
    const hedef = path.join(dizin, ad);
    const gecici = `${hedef}.${process.pid}.${Date.now()}.tmp`;
    fs.writeFileSync(gecici, JSON.stringify(veri, null, 2) + '\n');
    fs.renameSync(gecici, hedef);
  }
  function gunluk(dizin, islem, kimlik, veri) {
    const satir = JSON.stringify({ t: new Date().toISOString(), islem, kimlik, veri });
    fs.appendFileSync(path.join(dizin, 'gorev-gunlugu.jsonl'), satir + '\n');
  }

  const GOREV_ALAN = ['surum', 'tur', 'baslik', 'aciklama', 'grup', 'durum', 'atanan', 'oncelik',
    'bagimli'];

  function gorevAlanlari(g, kismi) {
    const s = {};
    if ('surum' in g) s.surum = metin(g.surum, 'surum');
    if ('tur' in g) s.tur = gecerli(g.tur, ENUM.gorevTur, 'tur');
    if ('baslik' in g) s.baslik = metin(g.baslik, 'baslik', true);
    if ('aciklama' in g) s.aciklama = metin(g.aciklama, 'aciklama') || '';
    if ('grup' in g) s.grup = gecerli(g.grup, ENUM.grup, 'grup');
    if ('durum' in g) s.durum = gecerli(g.durum, ENUM.gorevDurum, 'durum');
    if ('atanan' in g) s.atanan = gecerli(g.atanan, ENUM.atanan, 'atanan');
    if ('oncelik' in g) s.oncelik = gecerli(g.oncelik, ENUM.oncelik, 'oncelik');
    if ('bagimli' in g) {
      if (!Array.isArray(g.bagimli) || g.bagimli.some((x) => typeof x !== 'string')) {
        throw new HataApi(400, 'bagimli kimlik listesi olmalı');
      }
      s.bagimli = g.bagimli;
    }
    if (kismi) {
      const bilinmeyen = Object.keys(g).filter((k) => !GOREV_ALAN.includes(k));
      if (bilinmeyen.length) throw new HataApi(400,
        `değiştirilemez alan: ${bilinmeyen.join(', ')}`);
    }
    return s;
  }

  // Katalog deposu (projesiz videolar): kayıt "video: <kimlik>" taşır, kimlik katalogda olmalı.
  function katalogVideo(deger) {
    const kimlik = metin(deger, 'video', true);
    const kat = oku(path.join(KOK, 'projeler'), 'katalog.json', { uniteler: [] });
    const var_ = kat.uniteler.some((u) => u.konular.some((k) =>
      k.videolar.some((v) => v.kimlik === kimlik)));
    if (!var_) throw new HataApi(400, `bilinmeyen video: ${kimlik}`);
    return kimlik;
  }

  function gorevEkle(dizin, proje, g) {
    const liste = oku(dizin, 'gorevler.json', []);
    const sv = oku(dizin, 'surumler.json', { video: { kimlik: proje }, surumler: [],
      revizyonlar: [] });
    const a = gorevAlanlari(g, false);
    metin(g.baslik, 'baslik', true);
    if (a.surum && !sv.surumler.some((x) => x.kimlik === a.surum)) {
      throw new HataApi(400, `bilinmeyen sürüm: ${a.surum}`);
    }
    const tur = a.tur || 'uret';
    const kayit = {
      kimlik: sonrakiKimlik(liste, 'g'),
      video: proje === 'katalog' ? katalogVideo(g.video) : (sv.video?.kimlik || proje),
      surum: a.surum || null, tur, baslik: a.baslik, aciklama: a.aciklama || '',
      grup: a.grup || 'senaryo', durum: a.durum || 'acik',
      atanan: a.atanan || (tur === 'karar' ? 'Nadir' : 'sef'), oncelik: a.oncelik || 'orta',
      olusturan: gecerli(g.olusturan || 'Nadir', ENUM.yazar, 'olusturan'),
      tarih: new Date().toISOString(), bagimli: a.bagimli || [],
    };
    for (const b of kayit.bagimli) {
      if (!liste.some((x) => x.kimlik === b)) throw new HataApi(400,
        `bilinmeyen bağımlı görev: ${b}`);
    }
    liste.push(kayit);
    yaz(dizin, 'gorevler.json', liste);
    gunluk(dizin, 'gorev-ekle', kayit.kimlik, kayit);
    return kayit;
  }

  async function api(yontem, parcalar, govde) {
    const [proje, kaynak, kimlik] = parcalar;
    if (!proje || !kaynak) throw new HataApi(404, 'uç yok');
    const dizin = projeDizini(proje);
    const dosya = { gorevler: 'gorevler.json', surumler: 'surumler.json',
      yorumlar: 'yorumlar.json' };

    if (yontem === 'GET' && dosya[kaynak] && !kimlik) {
      const bos = kaynak === 'surumler' ? { video: { kimlik: proje }, surumler: [],
        revizyonlar: [] } : [];
      return oku(dizin, dosya[kaynak], bos);
    }
    if (yontem === 'GET' && kaynak === 'konum') return oku(dizin, 'harita-konum.json', {});

    return kilitle(proje, () => {
      if (yontem === 'POST' && kaynak === 'gorev' && !kimlik) return gorevEkle(dizin, proje, govde);

      if (yontem === 'PATCH' && kaynak === 'gorev' && kimlik) {
        const liste = oku(dizin, 'gorevler.json', []);
        const g = liste.find((x) => x.kimlik === kimlik);
        if (!g) throw new HataApi(404, `görev yok: ${kimlik}`);
        const a = gorevAlanlari(govde, true);
        if (!Object.keys(a).length) throw new HataApi(400, 'değişecek alan yok');
        Object.assign(g, a, { guncelleme: new Date().toISOString() });
        yaz(dizin, 'gorevler.json', liste);
        gunluk(dizin, 'gorev-guncelle', kimlik, a);
        return g;
      }

      if (yontem === 'POST' && kaynak === 'yorum' && !kimlik) {
        const liste = oku(dizin, 'yorumlar.json', []);
        const sv = oku(dizin, 'surumler.json', { surumler: [] });
        const gorevler = oku(dizin, 'gorevler.json', []);
        const gorev = metin(govde.gorev, 'gorev');
        if (gorev && !gorevler.some((x) => x.kimlik === gorev)) {
          throw new HataApi(400, `bilinmeyen görev: ${gorev}`);
        }
        const surum = metin(govde.surum, 'surum') || (gorev && gorevler.find((x) =>
          x.kimlik === gorev)?.surum);
        if (surum && !sv.surumler.some((x) => x.kimlik === surum)) {
          throw new HataApi(400, `bilinmeyen sürüm: ${surum}`);
        }
        const video = proje === 'katalog' ? katalogVideo(govde.video) : undefined;
        const kayit = {
          kimlik: sonrakiKimlik(liste, 'y'), ...(video ? { video } : {}), gorev: gorev || null,
          surum: surum || null,
          t: sayi(govde.t, 't') ?? null, sahne: metin(govde.sahne, 'sahne') || null,
          nesne: metin(govde.nesne, 'nesne') || null, metin: metin(govde.metin, 'metin', true),
          yazar: gecerli(govde.yazar || 'Nadir', ENUM.yazar, 'yazar'),
            tarih: new Date().toISOString(),
          durum: 'acik',
        };
        if (!kayit.gorev && !kayit.surum && !kayit.video) {
          throw new HataApi(400, 'gorev, surum ya da video zorunlu');
        }
        liste.push(kayit);
        yaz(dizin, 'yorumlar.json', liste);
        gunluk(dizin, 'yorum-ekle', kayit.kimlik, kayit);
        return kayit;
      }

      if (yontem === 'PATCH' && kaynak === 'yorum' && kimlik) {
        const liste = oku(dizin, 'yorumlar.json', []);
        const y = liste.find((x) => x.kimlik === kimlik);
        if (!y) throw new HataApi(404, `yorum yok: ${kimlik}`);
        const bilinmeyen = Object.keys(govde).filter((k) => k !== 'durum');
        if (bilinmeyen.length || !('durum' in govde)) throw new HataApi(400,
          'yalnız durum değişir');
        y.durum = gecerli(govde.durum, ENUM.yorumDurum, 'durum');
        yaz(dizin, 'yorumlar.json', liste);
        gunluk(dizin, 'yorum-guncelle', kimlik, { durum: y.durum });
        return y;
      }

      if (yontem === 'POST' && kaynak === 'surum' && !kimlik) {
        const sv = oku(dizin, 'surumler.json', { video: { kimlik: proje }, surumler: [],
          revizyonlar: [] });
        const tur = gecerli(govde.tur, ENUM.surumTur, 'tur');
        const ad = metin(govde.ad, 'ad', true);
        const kaynakSurum = metin(govde.kaynak, 'kaynak');
        if (kaynakSurum && !sv.surumler.some((x) => x.kimlik === kaynakSurum)) {
          throw new HataApi(400, `bilinmeyen kaynak sürüm: ${kaynakSurum}`);
        }
        const govde0 = kisaAd(ad).startsWith(tur) ? kisaAd(ad) : `${tur}-${kisaAd(ad)}`;
        let kid = govde0;
        for (let i = 2; sv.surumler.some((x) => x.kimlik === kid); i++) kid = `${govde0}-${i}`;
        const not = metin(govde.senaryo_notu, 'senaryo_notu') || '';
        const yeni = {
          kimlik: kid, video: sv.video?.kimlik || proje, tur, ad, senaryo: null, kapak: null,
          seviye: metin(govde.seviye, 'seviye') || null, kaynak: kaynakSurum || null,
          durum: 'planli', onizleme: null, senaryo_notu: not, tarih: new Date().toISOString(),
        };
        sv.surumler.push(yeni);
        yaz(dizin, 'surumler.json', sv);
        gunluk(dizin, 'surum-ekle', kid, yeni);
        const gorev = gorevEkle(dizin, proje, {
          surum: kid, tur: 'turev', baslik: `Türev: ${ad}`, grup: 'senaryo', atanan: 'sef',
          aciklama: not || `${tur} türevi için senaryo yazılacak.`,
          bagimli: [], olusturan: govde.olusturan || 'Nadir',
        });
        return { surum: yeni, gorev };
      }

      if (yontem === 'POST' && kaynak === 'konum' && !kimlik) {
        const konum = oku(dizin, 'harita-konum.json', {});
        for (const [k, v] of Object.entries(govde)) {
          if (!v || !Number.isFinite(v.x) || !Number.isFinite(v.y)) throw new HataApi(400,
            `konum geçersiz: ${k}`);
          konum[k] = { x: Math.round(v.x), y: Math.round(v.y) };
        }
        yaz(dizin, 'harita-konum.json', konum);
        return konum;
      }
      throw new HataApi(404, 'uç yok');
    });
  }

  function govdeOku(istek) {
    return new Promise((coz, red) => {
      const parca = []; let boy = 0;
      istek.on('data', (c) => {
        boy += c.length;
        if (boy > MAX_GOVDE) { red(new HataApi(413, 'gövde çok büyük')); istek.destroy();
          return; }
        parca.push(c);
      });
      istek.on('end', () => {
        const s = Buffer.concat(parca).toString('utf8');
        if (!s.trim()) return coz({});
        try {
          const v = JSON.parse(s);
          if (!v || typeof v !== 'object' || Array.isArray(v)) throw new Error('nesne bekleniyor');
          coz(v);
        } catch (e) { red(new HataApi(400, `JSON okunamadı: ${e.message}`)); }
      });
      istek.on('error', red);
    });
  }
  function json(yanit, kod, veri) {
    const s = JSON.stringify(veri);
    yanit.writeHead(kod, { 'Content-Type': MIME['.json'], 'Content-Length': Buffer.byteLength(s),
      'Cache-Control': 'no-store' });
    yanit.end(s);
  }

  function statik(istek, yanit, yol) {
    let dosya;
    try { dosya = path.join(KOK, decodeURIComponent(yol)); } catch { return json(yanit, 400,
      { hata: 'adres bozuk' }); }
    if (dosya !== KOK && !dosya.startsWith(KOK + path.sep)) return json(yanit, 403,
      { hata: 'yasak' });
    let st;
    try { st = fs.statSync(dosya); } catch { return json(yanit, 404, { hata: 'bulunamadı' }); }
    if (st.isDirectory()) {
      const idx = path.join(dosya, 'index.html');
      if (!fs.existsSync(idx)) return json(yanit, 404, { hata: 'bulunamadı' });
      dosya = idx; st = fs.statSync(idx);
    }
    const tur = MIME[path.extname(dosya).toLowerCase()] || 'application/octet-stream';
    const baslik = { 'Content-Type': tur, 'Accept-Ranges': 'bytes', 'Cache-Control': 'no-cache' };
    const r = istek.headers.range && /^bytes=(\d*)-(\d*)$/.exec(istek.headers.range);
    if (r) {
      let bas = r[1] === '' ? st.size - Number(r[2]) : Number(r[1]);
      let son = r[1] === '' || r[2] === '' ? st.size - 1 : Math.min(Number(r[2]), st.size - 1);
      if (!(bas >= 0 && bas <= son && bas < st.size)) {
        yanit.writeHead(416, { 'Content-Range': `bytes */${st.size}` }); return yanit.end();
      }
      yanit.writeHead(206, { ...baslik, 'Content-Range': `bytes ${bas}-${son}/${st.size}`,
        'Content-Length': son - bas + 1 });
      if (istek.method === 'HEAD') return yanit.end();
      return fs.createReadStream(dosya, { start: bas, end: son }).pipe(yanit);
    }
    yanit.writeHead(200, { ...baslik, 'Content-Length': st.size });
    if (istek.method === 'HEAD') return yanit.end();
    fs.createReadStream(dosya).pipe(yanit);
  }

  // /p/<proje>/<editör dosyası>: bütün projeler için ortak/editor/ içeriğini sunar.
  function editorSun(istek, yanit, parcalar) {
    const [proje, dosya, ...artik] = parcalar;
    if (artik.length || !EDITOR_DOSYA.has(dosya)) return json(yanit, 404, { hata: 'bulunamadı' });
    projeDizini(proje);
    const yol = path.join(EDITOR_DIZINI, dosya);
    const tur = MIME[path.extname(dosya)] || 'application/octet-stream';
    const boy = fs.statSync(yol).size;
    yanit.writeHead(200, { 'Content-Type': tur, 'Content-Length': boy, 'Cache-Control': 'no-cache' });
    if (istek.method === 'HEAD') return yanit.end();
    fs.createReadStream(yol).pipe(yanit);
  }

  return http.createServer(async (istek, yanit) => {
    const url = new URL(istek.url, 'http://x');
    try {
      if (url.pathname.startsWith('/api/')) {
        const parcalar = url.pathname.slice(5).split('/').filter(Boolean).map(decodeURIComponent);
        const govde = ['POST', 'PATCH', 'PUT'].includes(istek.method) ? await govdeOku(istek) : {};
        return json(yanit, istek.method === 'POST' ? 201 : 200, await api(istek.method, parcalar,
          govde));
      }
      // Sahnelerin canlı kip günlüğü (POST /log): sessizce yutulur; konsolda 405 görünmesin (05.11).
      if (url.pathname === '/log') { istek.resume(); yanit.writeHead(204); return yanit.end(); }
      if (!['GET', 'HEAD'].includes(istek.method)) return json(yanit, 405, { hata: 'yöntem yok' });
      if (url.pathname.startsWith('/p/')) {
        const parcalar = url.pathname.slice(3).split('/').map(decodeURIComponent);
        return editorSun(istek, yanit, parcalar);
      }
      // eski adres: /projeler/<proje>/(harita|onizle).html -> /p/<proje>/..., sorgu korunur
      const eski = /^\/projeler\/([^/]+)\/(harita|onizle)\.html$/.exec(url.pathname);
      if (eski) {
        yanit.writeHead(302, { Location: `/p/${eski[1]}/${eski[2]}.html${url.search}`,
          'Cache-Control': 'no-store' });
        return yanit.end();
      }
      statik(istek, yanit, url.pathname);
    } catch (e) {
      if (e instanceof HataApi) return json(yanit, e.kod, { hata: e.message });
      console.error(e);
      json(yanit, 500, { hata: 'sunucu hatası' });
    }
  });
}

export function baslat({ kok, port, adres = '127.0.0.1' }) {
  if (port === 3000) return Promise.reject(new Error('port 3000 yasak'));
  const s = sunucuKur({ kok });
  return new Promise((coz, red) => {
    s.once('error', (e) => red(e.code === 'EADDRINUSE' ? new Error(`port dolu: ${port}`) : e));
    s.listen(port, adres, () => coz(s));
  });
}

if (process.argv[1] && fileURLToPath(import.meta.url) === path.resolve(process.argv[1])) {
  const arg = (ad, v) => { const i = process.argv.indexOf(ad); return i > 0 ? process.argv[i + 1]
    : v; };
  const port = Number(arg('--port', 3012));
  const kok = arg('--kok', path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..'));
  baslat({ kok, port }).then(() =>
    console.log(`önizleme sunucusu: http://127.0.0.1:${port}/ (kök ${kok})`))
    .catch((e) => { console.error(`HATA: ${e.message}`); process.exit(1); });
}
