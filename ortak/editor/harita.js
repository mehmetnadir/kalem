// Görev haritası: ünite > konu > video (kitle x seviye) > sürüm > görev. Açılır/kapanır.
// Veri: /projeler/katalog.json (plan) + /api/<proje>/{surumler,gorevler,yorumlar} + /api/katalog/*.
import * as M from './harita-model.js';

const Y = globalThis.KalemYol;
const PROJE = new URLSearchParams(location.search).get('proje') || Y.projeAdi()
  || 'present-continuous';
const KAT = 'katalog';
const ETIKET = {
  durum: { acik: 'Açık', planli: 'Planlı', hazirlik: 'Hazırlık', uretimde: 'Üretimde',
    inceleme: 'İnceleme',
    onay: 'Onay', yayinda: 'Yayında', kapali: 'Kapalı' },
  grup: { motor: 'Motor', oynatici: 'Oynatıcı', senaryo: 'Senaryo',
    'tasarim-karar': 'Tasarım-karar',
    platform: 'Platform' },
  tur: { uret: 'Üret', duzelt: 'Düzelt', turev: 'Türev', karar: 'Karar' },
  surumTur: { 'ana-yatay': 'Ana yatay', dikey: 'Dikey', shorts: 'Shorts',
    alternatif: 'Alternatif' },
  oncelik: { dusuk: 'Düşük', orta: 'Orta', yuksek: 'Yüksek' },
};
const GOREV_DURUM = ['acik', 'uretimde', 'inceleme', 'onay', 'kapali'];
const ATANAN = ['sef', 'ajan', 'Nadir'];
const DERINLIK_AD = { unite: 'Üniteler', konu: 'Konular', video: 'Videolar', hepsi: 'Hepsi' };
const ANAHTAR = 'harita-acik';

const S = { agac: null, katalogMetin: '', projeler: {}, depo: { gorevler: [], yorumlar: [] },
  konum: {},
  konumlar: {}, acik: new Set(), secili: null, sur: { x: 40, y: 40, k: 1 }, imza: '',
  sus: { grup: '', durum: '', atanan: '', kitle: '', vdurum: '' },
  ara: { aktif: false, canli: new Set(), eslesen: new Set(), ac: new Set() } };

const $ = (id) => document.getElementById(id);
const e = (tag, ozellik = {}, ...cocuk) => {
  const n = document.createElement(tag);
  for (const [k, v] of Object.entries(ozellik)) {
    if (k === 'class') n.className = v; else if (k.startsWith('on')) n.addEventListener(k.slice(2),
      v);
    else if (v !== null && v !== undefined && v !== false) n.setAttribute(k, v === true ? '' : v);
  }
  for (const c of cocuk.flat(3)) {
    if (c !== null && c !== undefined && c !== false) n.append(c.nodeType ? c
      : document.createTextNode(c));
  }
  return n;
};
const tarihKisa = (iso) => { const d = new Date(iso); return isNaN(d) ? '' :
  `${String(d.getDate()).padStart(2, '0')}.${String(d.getMonth() + 1).padStart(2, '0')}`; };
const sure = (t) =>
  `${String(Math.floor(t / 60)).padStart(2, '0')}:${(t % 60).toFixed(1).padStart(4, '0')}`;
const mmss = (sn) => `${Math.floor(sn / 60)}:${String(sn % 60).padStart(2, '0')}`;
const sayi = (n) => new Intl.NumberFormat('tr-TR').format(n);
const kitleAd = (k) => (S.agac.katalog.kitleler || {})[k] || k;
const sevAd = (k) => (S.agac.katalog.seviyeler || {})[k] || k;

function uyar(mesaj) {
  const u = $('uyari'); u.textContent = mesaj; u.hidden = false;
  clearTimeout(uyar.z); uyar.z = setTimeout(() => { u.hidden = true; }, 4500);
}
async function cagri(proje, yontem, yol, govde) {
  const r = await fetch(`/api/${proje}${yol}`, { method: yontem,
    headers: govde ? { 'Content-Type': 'application/json' } : {}, body: govde
      ? JSON.stringify(govde) : undefined });
  const v = await r.json().catch(() => ({}));
  if (!r.ok) { uyar(v.hata || `istek başarısız (${r.status})`); throw new Error(v.hata
    || r.status); }
  return v;
}
const getJson = (adres) => fetch(adres).then((r) =>
  { if (!r.ok) throw new Error(`${adres}: ${r.status}`);
  return r.json(); });

// ---- veri ----
const proje = (p) => (p === KAT ? { sv: null, gorevler: S.depo.gorevler, yorumlar: S.depo.yorumlar }
  : S.projeler[p]);
const gorevleri = (v) => M.videoGorevleri(v, S.projeler, S.depo.gorevler);
const depoProje = (v) => (v.proje && S.projeler[v.proje] ? v.proje : KAT);

async function yukle(zorla) {
  const katMetin = await fetch('/projeler/katalog.json').then((r) => r.text());
  const katalog = JSON.parse(katMetin);
  const adlar = [...new Set(katalog.uniteler.flatMap((u) => u.konular.flatMap((k) =>
    k.videolar.map((v) => v.proje).filter(Boolean))))];
  const projeler = {};
  await Promise.all(adlar.map(async (p) => {
    try {                                 // proje dizini henüz yoksa (üretimde) harita kırılmaz, kart katalogdan çizilir
      const [sv, gorevler, yorumlar] = await Promise.all(['surumler', 'gorevler', 'yorumlar']
        .map((k) => getJson(`/api/${p}/${k}`)));
      projeler[p] = { sv, gorevler, yorumlar };
    } catch (e) { console.warn('proje yüklenemedi:', p, String(e)); }
  }));
  const [dg, dy, konum] = await Promise.all([getJson(`/api/${KAT}/gorevler`),
    getJson(`/api/${KAT}/yorumlar`),
    getJson(`/api/${PROJE}/konum`).catch(() => ({}))]);
  const imza = JSON.stringify([katMetin.length, projeler, dg, dy]);
  if (!zorla && imza === S.imza) return;
  const ilk = !S.agac;
  if (katMetin !== S.katalogMetin) { S.agac = M.agacKur(katalog); S.katalogMetin = katMetin; }
  Object.assign(S, { projeler, depo: { gorevler: dg, yorumlar: dy }, konum, imza });
  M.projeBagla(S.agac, projeler);
  if (ilk) ilkDurum();
  ciz();
  if (ilk) ilkGorunum();
  if (S.secili) panel();
}

// ---- açık-küme: URL + localStorage ----
function depodanOku() { try { return localStorage.getItem(ANAHTAR) || ''; } catch { return ''; } }
function kaydet() {
  const m = M.urlUret(S.acik);
  try { localStorage.setItem(ANAHTAR, m); } catch { /* depolama kapalı: yalnız oturum */ }
  const u = new URL(location.href);
  if (m) u.searchParams.set('ac', m); else u.searchParams.delete('ac');
  history.replaceState(null, '', u);
}
let ilkHedef = null;
function ilkDurum() {
  const q = new URLSearchParams(location.search);
  const acMetin = q.has('ac') ? q.get('ac') : depodanOku();
  S.acik = M.urlCoz(S.agac, acMetin);
  if (q.has('ac')) ilkHedef = M.sonKimlik(S.agac, acMetin);
  const sc = M.secCoz(S.agac, q.get('sec'));
  if (sc) {
    for (const a of sc.ac) S.acik.add(a);
    ilkHedef = sc.id;
    if (sc.panel) S.secili = `v:${sc.id}`;
  }
}
function acikAyarla(yeni) { S.acik = yeni; kaydet(); ciz(); }

// ---- filtre / arama ----
const videoSonuk = (v) => (S.ara.aktif && !S.ara.canli.has(v.id)) || !M.videoGecer(v, S.sus);
const sonuk = (g) => (S.sus.grup && g.grup !== S.sus.grup) || (S.sus.durum
  && g.durum !== S.sus.durum)
  || (S.sus.atanan && g.atanan !== S.sus.atanan);
const dugumSonuk = (d, videolar) => (S.ara.aktif && !S.ara.canli.has(d.id))
  || (M.filtreAktif(S.sus) && videolar.every((v) => !M.videoGecer(v, S.sus)));

// ---- çizim ----
const chev = () => e('span', { class: 'chev' });
const cubuk = (dagilim) => e('div', { class: 'cubuk' }, M.VIDEO_DURUM.filter((d) =>
  dagilim[d]).map((d) =>
  e('i', { class: `d-${d}`, style: `flex:${dagilim[d]}`,
    title: `${ETIKET.durum[d]}: ${dagilim[d]}` })));

function gorevSatiri(p, g) {
  const id = `g:${p}/${g.kimlik}`;
  return e('div',
    { class: `gk d-${g.durum}${sonuk(g) ? ' sonuk' : ''}${S.secili === id ? ' secili' : ''}`,
    'data-act': 'sec', 'data-sec': id, title: g.baslik },
  e('b', {}, g.baslik), e('span', {}, ETIKET.durum[g.durum] || g.durum), e('span', {}, g.atanan));
}
function surumKutusu(v, s, gs) {
  const sid = `${v.id}/${s.kimlik}`; const acik = S.acik.has(sid);
    const pid = `s:${v.proje}/${s.kimlik}`;
  return e('div', { class: `sk d-${s.durum}${acik ? ' acik' : ''}`, 'data-id': sid },
    e('div', { class: 'sk-ust' },
      e('span', { class: 'tg', 'data-act': 'ac', 'data-ac': sid }, chev()),
      e('span', { class: `sk-ad${S.secili === pid ? ' secili' : ''}`, 'data-act': 'sec',
        'data-sec': pid },
        s.ad),
      e('span', { class: 'etiket' }, ETIKET.surumTur[s.tur] || s.tur),
      e('span', { class: 'say' }, `${gs.length} görev`)),
    acik ? gs.map((g) => gorevSatiri(v.proje, g)) : null);
}
function videoAlt(v) {
  const gs = gorevleri(v); const p = depoProje(v);
  const sv = v.surumler || [];
  if (!sv.length && !gs.length) return e('div', { class: 'bosnot' },
    'Sürüm ve görev yok.');
  const bagli = new Set(sv.map((s) => s.kimlik));
  const yetim = gs.filter((g) => !g.surum || !bagli.has(g.surum));
  return e('div', { class: 'vk-alt' },
    sv.map((s) => surumKutusu(v, s, gs.filter((g) => g.surum === s.kimlik))),
    yetim.length ? [e('div', { class: 'grupbasi' }, 'Sürüme bağlı olmayan görevler'),
      yetim.map((g) => gorevSatiri(p, g))] : null);
}
const sayimMetni = (v, gs) => [(v.surumler || []).length ? ` · ${v.surumler.length} sürüm` : '',
  gs.length ? ` · ${gs.length} görev` : ''].join('');
function videoKart(v) {
  const acik = S.acik.has(v.id); const id = `v:${v.id}`;
  const gs = gorevleri(v);
  return e('div',
    { class: `vk d-${v.durum}${acik ? ' acik' : ''}${acik && v.surumler.length ? ' genis' : ''}`
    + `${videoSonuk(v) ? ' sonuk' : ''}`
    + `${S.secili === id ? ' secili' : ''}`, 'data-id': v.id, 'data-act': 'sec', 'data-sec': id },
  e('div', { class: 'vk-ust' },
    e('span', { class: 'tg', 'data-act': 'ac', 'data-ac': v.id }, chev()),
    e('span', { class: 'vk-kod', title: v.kod }, v.kod),
    e('span', { class: 'etiket durum' }, ETIKET.durum[v.durum] || v.durum)),
  e('div', { class: 'vk-meta' }, `${kitleAd(v.kitle)} · ${sevAd(v.seviye)}`
    + sayimMetni(v, gs)),
  acik ? videoAlt(v) : null);
}
const cipSecili = (v) => (S.secili === `v:${v.id}` ? ' secili' : '');
function konuKart(k) {
  const acik = S.acik.has(k.id); const o = M.konuOzet(k);
  return e('div', { class: `konu${acik ? ' acik' : ''}${dugumSonuk(k, k.videolar) ? ' sonuk' : ''}`,
    'data-id': k.id },
  e('div', { class: 'k-baslik', 'data-act': 'ac', 'data-ac': k.id }, chev(), e('span',
    { class: 'k-kod' }, k.kod),
    e('span', { class: 'k-ad' }, k.ad)),
  k.lms.map((l) => e('div', { class: `k-lms${l.eski ? ' eski' : ''}` }, l.ad, ' ', e('span', {},
    mmss(l.sure)))),
  e('div', { class: 'k-meta' }, e('span', {}, `${o.sureDk} dk`),
    e('span', {}, `${sayi(o.izlenme)} izlenme · ${sayi(o.tamamlama)} tamamlama`),
    e('span', {}, `ort. %${o.ortYuzde}`), k.pptx.length ? e('span', {}, `${k.pptx.length} pptx`)
      : null),
  e('div', { class: 'cipler' }, k.videolar.map((v) => e('button', { type: 'button',
    class: `cip d-${v.durum}${videoSonuk(v) ? ' sonuk' : ''}${cipSecili(v)}`,
    'data-act': 'sec', 'data-sec': `v:${v.id}`,
    title: `${v.kod} · ${ETIKET.durum[v.durum]}` }, `${kitleAd(v.kitle)} ${sevAd(v.seviye)[0]}`))),
  acik ? e('div', { class: 'videolar' }, k.videolar.map(videoKart)) : null);
}
function uniteKart(u) {
  const acik = S.acik.has(u.id); const o = M.uniteOzet(u);
  return e('div',
    { class: `unite${acik ? ' acik' : ''}${dugumSonuk(u, M.uniteVideolari(u)) ? ' sonuk' : ''}`,
    'data-id': u.id },
  e('div', { class: 'u-baslik' }, chev(), e('span', { class: 'u-kod' }, u.kod), e('span',
    { class: 'u-ad' }, u.ad)),
  e('div', { class: 'u-ozet' },
    e('div', { class: 'sayilar' }, e('span', {}, e('b', {}, o.konu), ' konu'), e('span', {}, e('b',
      {}, o.video), ' video'),
      e('span', {}, e('b', {}, sayi(o.sureDk)), ' dk kaynak'), e('span', {}, 'tamamlama ', e('b',
        {}, `%${o.ortYuzde}`))),
    cubuk(o.dagilim)),
  acik ? e('div', { class: 'konular' }, u.konular.map(konuKart) ) : null);
}

function ciz() {
  const d = $('dugumler'); const parca = document.createDocumentFragment();
  for (const u of S.agac.uniteler) parca.append(uniteKart(u));
  d.replaceChildren(parca);
  yerlestir();
  derinlikDugmeleri();
}
// Izgara görünüm genişliğini izler; konumu kayıtlı KAPALI üniteler ızgaradan çıkar.
function izgaraGenisligi() {
  $('dugumler').style.width = `${Math.max(640, $('gorunum').clientWidth)}px`;
}
function yerlestir() {
  izgaraGenisligi();
  for (const n of $('dugumler').children) {
    const kay = S.konum[`u:${n.dataset.id}`];
    const sabit = Boolean(kay) && !n.classList.contains('acik');
    n.classList.toggle('sabit', sabit);
    n.style.left = sabit ? `${kay.x}px` : ''; n.style.top = sabit ? `${kay.y}px` : '';
  }
}
function secimGoster() {
  for (const n of document.querySelectorAll('[data-sec]')) {
    n.classList.toggle('secili', n.dataset.sec === S.secili);
  }
}

// ---- görünüm: kaydır, yakınlaştır, sığdır ----
function uygula() {
  $('dunya').style.transform = `translate(${S.sur.x}px,${S.sur.y}px) scale(${S.sur.k})`;
  const g = $('gorunum'); const b = 24 * S.sur.k;
  g.style.backgroundSize = `${b}px ${b}px`;
    g.style.backgroundPosition = `${S.sur.x}px ${S.sur.y}px`;
}
function sigdir() {
  const ks = [...$('dugumler').children]; if (!ks.length) return;
  const x0 = Math.min(...ks.map((n) => n.offsetLeft)), y0 = Math.min(...ks.map((n) => n.offsetTop));
  const x1 = Math.max(...ks.map((n) => n.offsetLeft + n.offsetWidth));
  const y1 = Math.max(...ks.map((n) => n.offsetTop + n.offsetHeight));
  const gv = $('gorunum').getBoundingClientRect(); const sagBos = $('panel').hidden ? 0 : 400;
  const k = Math.min(1, (gv.width - sagBos - 80) / (x1 - x0), (gv.height - 80) / (y1 - y0));
  S.sur = { k, x: 40 - x0 * k + Math.max(0, (gv.width - sagBos - 80 - (x1 - x0) * k) / 2),
    y: 40 - y0 * k };
  uygula();
}
function gorunumeGetir(el) {
  const g = $('gorunum').getBoundingClientRect(); const r = el.getBoundingClientRect();
  S.sur.x += g.left + 60 - r.left; S.sur.y += g.top + 80 - r.top; uygula();
}
function hedefeGit(id) {
  const el = document.querySelector(`[data-id="${CSS.escape(id)}"]`);
  if (el) gorunumeGetir(el);
}
function ilkGorunum() {
  if (ilkHedef) { hedefeGit(ilkHedef); ilkHedef = null; } else sigdir();
}
const ETKIN = '[data-act], .u-baslik, button, a, input, textarea, select';
function kaydirmaKur() {
  const g = $('gorunum'); let bas = null;
  g.addEventListener('pointerdown', (ev) => {
    if (ev.button !== 0 || ev.target.closest(ETKIN)) return;
    bas = { x: ev.clientX, y: ev.clientY, ox: S.sur.x, oy: S.sur.y, hareket: false };
    g.setPointerCapture(ev.pointerId); g.classList.add('tut');
  });
  g.addEventListener('pointermove', (ev) => {
    if (!bas) return;
    const dx = ev.clientX - bas.x, dy = ev.clientY - bas.y;
    if (Math.abs(dx) + Math.abs(dy) > 3) bas.hareket = true;
    S.sur.x = bas.ox + dx; S.sur.y = bas.oy + dy; uygula();
  });
  const bitir = () => { if (bas && !bas.hareket && S.secili) { S.secili = null;
    $('panel').hidden = true;
    secimGoster(); }
  bas = null; g.classList.remove('tut'); };
  g.addEventListener('pointerup', bitir); g.addEventListener('pointercancel', bitir);
  g.addEventListener('wheel', (ev) => {
    ev.preventDefault();
    const r = g.getBoundingClientRect(); const mx = ev.clientX - r.left, my = ev.clientY - r.top;
    const yk = Math.min(2.5, Math.max(0.1, S.sur.k * Math.exp(-ev.deltaY * 0.0015)));
    S.sur.x = mx - (mx - S.sur.x) * (yk / S.sur.k); S.sur.y = my - (my - S.sur.y) * (yk / S.sur.k);
      S.sur.k = yk;
    uygula();
  }, { passive: false });
}

// ---- etkileşim: tek dinleyici (delegasyon) ----
function ustSurukle(ev) {
  const el = ev.target.closest('.unite'); if (ev.button !== 0 || !el) return;
  const id = el.dataset.id; ev.stopPropagation(); el.setPointerCapture(ev.pointerId);
  const acik = el.classList.contains('acik');
  const bas = { x: ev.clientX, y: ev.clientY, hareket: false,
    p: { x: el.offsetLeft, y: el.offsetTop } };
  const tasi = (m) => {
    const dx = (m.clientX - bas.x) / S.sur.k, dy = (m.clientY - bas.y) / S.sur.k;
    if (acik || (!bas.hareket && Math.abs(dx) + Math.abs(dy) < 4 / S.sur.k)) return;
    if (!bas.hareket) el.classList.add('sabit');
    bas.hareket = true;
    S.konumlar[id] = { x: Math.round(bas.p.x + dx), y: Math.round(bas.p.y + dy) };
    el.style.left = `${S.konumlar[id].x}px`; el.style.top = `${S.konumlar[id].y}px`;
  };
  const son = () => {
    el.removeEventListener('pointermove', tasi); el.removeEventListener('pointerup', son);
    if (bas.hareket) {
      S.konum[`u:${id}`] = S.konumlar[id];
      cagri(PROJE, 'POST', '/konum', { [`u:${id}`]: S.konumlar[id] }).catch(() => {});
    } else acikAyarla(M.degistir(S.acik, id));
  };
  el.addEventListener('pointermove', tasi); el.addEventListener('pointerup', son);
}
function dinleyiciKur() {
  const d = $('dugumler');
  d.addEventListener('pointerdown', (ev) =>
    { if (ev.target.closest('.u-baslik')) ustSurukle(ev); });
  d.addEventListener('click', (ev) => {
    const h = ev.target.closest('[data-act]'); if (!h) return;
    if (h.dataset.act === 'ac') acikAyarla(M.degistir(S.acik, h.dataset.ac));
    else sec(h.dataset.sec);
  });
}
function sec(id) { S.secili = id; secimGoster(); panel(); }

// ---- sağ panel ----
function editorAdresi(surum, t, vYol) {
  if (!surum || !surum.onizleme) return null;
  const y = vYol ? `&yol=${encodeURIComponent(vYol)}` : '';
  return `${Y.yeniAdres(surum.onizleme)}?surum=${encodeURIComponent(surum.kimlik)}&t=${t || 0}${y}`;
}
const videoYolu = (v) => M.yol(S.agac, v.id).join(',');
const projeVideosu = (p) => [...S.agac.video.values()].find((v) => v.proje === p);
const surumYolu = (p) => { const v = projeVideosu(p); return v ? videoYolu(v) : ''; };
function secenek(liste, deger, etiket) {
  return liste.map((o) => e('option', { value: o, selected: o === deger }, (etiket && etiket[o])
    || o));
}
function yorumKutusu(p, y) {
  const sv = proje(p).sv; const surum = sv && sv.surumler.find((s) => s.kimlik === y.surum);
  const ad = editorAdresi(surum, y.t || 0, surumYolu(p));
  return e('div', { class: `yorum${y.durum === 'cozuldu' ? ' cozuldu' : ''}` },
    e('div', { class: 'ust' }, e('b', {}, y.yazar), y.t != null ? e('span', {}, sure(y.t)) : null,
      y.sahne ? e('span', {}, `sahne ${y.sahne}`) : null, e('span', {}, tarihKisa(y.tarih)),
        e('span', { class: 'bos' }),
      ad ? e('a', { href: ad }, 'Editörde aç') : null,
      e('button', { onclick: async () => { await cagri(p, 'PATCH', `/yorum/${y.kimlik}`,
        { durum: y.durum === 'cozuldu' ? 'acik' : 'cozuldu' }); await yukle(true); } },
      y.durum === 'cozuldu' ? 'Yeniden aç' : 'Çözüldü')),
    e('div', {}, y.metin));
}
function yorumEkleme(p, ek) {
  const alan = e('textarea', { placeholder: 'Yorum yaz' });
  const t = e('input', { type: 'number', step: '0.1', min: '0', placeholder: 'sn (isteğe bağlı)',
    style: 'width:130px' });
  const gonder = e('button', { class: 'btn ana', onclick: async () => {
    if (!alan.value.trim()) return uyar('Yorum boş olamaz');
    await cagri(p, 'POST', '/yorum', { ...ek, metin: alan.value, t: t.value === '' ? undefined
      : Number(t.value) });
    await yukle(true);
  } }, 'Yorum ekle');
  return [e('h3', {}, 'Yorum ekle'), alan, e('div', { class: 'satir' }, t, gonder)];
}
const gorevLinkleri = (p, gs) => e('div', { class: 'liste' }, gs.map((g) => e('a', {
  onclick: () => sec(`g:${p}/${g.kimlik}`) }, `${ETIKET.durum[g.durum]} · ${g.baslik}`)));
const kapatDugmesi = () => e('button', { class: 'btn kapat', title: 'Kapat', onclick: () => {
  S.secili = null; $('panel').hidden = true; secimGoster(); } }, 'x');

function panel() {
  const p = $('panel'); const id = S.secili;
  if (!id) { p.hidden = true; return; }
  const tur = id[0]; const kalan = id.slice(2);
  p.hidden = false; p.replaceChildren(kapatDugmesi());
  const ekle = (...c) => p.append(...c.flat(4).filter((x) => x != null && x !== false));
  if (tur === 'v') {
    const v = S.agac.video.get(kalan); if (!v) { p.hidden = true; return; }
    return panelVideo(v, ekle);
  }
  const ay = kalan.indexOf('/'); const pr = kalan.slice(0, ay); const kim = kalan.slice(ay + 1);
  if (!veri) { p.hidden = true; return; }
  if (tur === 'g') panelGorev(pr, veri, kim, ekle); else panelSurum(pr, veri, kim, ekle);
}
function panelGorev(pr, veri, kim, ekle) {
  const g = veri.gorevler.find((x) => x.kimlik === kim); if (!g) { $('panel').hidden = true;
    return; }
  const surum = veri.sv && veri.sv.surumler.find((s) => s.kimlik === g.surum);
  const yor = veri.yorumlar.filter((y) => y.gorev === g.kimlik);
  const ilkT = (yor.find((y) => y.t != null) || {}).t;
  const ed = editorAdresi(surum, ilkT, surumYolu(pr));
  const degistir = (alan) => async (ev) => { await cagri(pr, 'PATCH', `/gorev/${g.kimlik}`,
    { [alan]: ev.target.value }); await yukle(true); };
  ekle(e('h2', {}, g.baslik),
    e('div', { class: 'meta' }, e('span', { class: 'etiket' }, g.kimlik), e('span',
      { class: 'etiket' }, ETIKET.grup[g.grup]),
      e('span', { class: 'etiket' }, ETIKET.tur[g.tur]), e('span', {},
        `öncelik ${ETIKET.oncelik[g.oncelik] || g.oncelik}`),
      pr === KAT ? e('span', { class: 'etiket' }, g.video) : null, e('span', {},
        tarihKisa(g.tarih))),
    e('p', {}, g.aciklama || 'Açıklama yok.'),
    e('div', { class: 'satir' },
      e('label', {}, 'Durum', e('select', { onchange: degistir('durum') }, secenek(GOREV_DURUM,
        g.durum, ETIKET.durum))),
      e('label', {}, 'Atanan', e('select', { onchange: degistir('atanan') }, secenek(ATANAN,
        g.atanan)))),
    pr === KAT ? null : e('div', { class: 'satir' }, ed ? e('a', { class: 'btn ana', href: ed },
      'Editörde aç')
      : e('span', { class: 'btn pasif' }, 'Editörde aç (önizleme yok)')),
    (g.bagimli || []).length ? [e('h3', {}, 'Bağımlılıklar'), e('div', { class: 'liste' },
      g.bagimli.map((b) => { const bg = veri.gorevler.find((x) => x.kimlik === b);
        return e('a', { onclick: () => sec(`g:${pr}/${b}`) },
          `${b} · ${bg ? bg.baslik : ''}`); }))] : null,
    e('h3', {}, `Yorumlar (${yor.length})`), yor.map((y) => yorumKutusu(pr, y)),
    yorumEkleme(pr, pr === KAT ? { gorev: g.kimlik, video: g.video } : { gorev: g.kimlik,
      surum: g.surum || undefined }));
}
function panelSurum(pr, veri, kim, ekle) {
  const s = veri.sv.surumler.find((x) => x.kimlik === kim); if (!s) { $('panel').hidden = true;
    return; }
  const gs = veri.gorevler.filter((g) => g.surum === s.kimlik);
  const yor = veri.yorumlar.filter((y) => y.surum === s.kimlik);
  const ed = editorAdresi(s, 0, surumYolu(pr));
  ekle(e('h2', {}, s.ad),
    e('div', { class: 'meta' }, e('span', { class: 'etiket' }, ETIKET.surumTur[s.tur]),
      e('span', { class: 'etiket durum d-' + s.durum }, ETIKET.durum[s.durum]),
      s.kaynak ? e('span', {}, `kaynak: ${s.kaynak}`) : null, s.seviye ? e('span', {},
        `seviye ${s.seviye}`) : null),
    s.senaryo_notu ? e('p', {}, s.senaryo_notu) : null,
    s.kapak_canalici ? e('p', {}, `Kapak: can alıcı #${s.kapak_canalici}'den — ${
      (veri.sv.video.canAlici || [])[s.kapak_canalici - 1] || ''}`) : null,
    e('div', { class: 'satir' }, ed ? e('a', { class: 'btn ana', href: ed }, 'Editörde aç')
      : e('span', { class: 'btn pasif' }, 'Editörde aç (önizleme yok)')),
    e('h3', {}, `Görevler (${gs.length})`), gorevLinkleri(pr, gs),
    e('h3', {}, `Yorumlar (${yor.length})`), yor.map((y) => yorumKutusu(pr, y)), yorumEkleme(pr,
      { surum: s.kimlik }));
}
function kopya(m) { navigator.clipboard.writeText(m).then(() => uyar('Kopyalandı'), () =>
  uyar('Kopyalanamadı')); }
function listeBolumu(baslik, dizi, numarali) {
  const madde = (m, no) => e('div', { class: 'yorum' }, e('div', { class: 'ust' },
    no ? e('b', {}, `#${no}`) : null, e('span', { class: 'bos' }),
    e('button', { onclick: () => kopya(m) }, 'Kopyala')), e('div', {}, m));
  return [e('h3', {}, `${baslik} (${(dizi || []).length})`),
    (dizi || []).length ? [dizi.map((m, i) => madde(m, numarali ? i + 1 : 0)),
      e('div', { class: 'satir' }, e('button', { class: 'btn', onclick: () => kopya(dizi.map((m,
        i) =>
        numarali ? `${i + 1}. ${m}` : `- ${m}`).join('\n')) }, 'Tümünü kopyala'))] : e('p', {},
          'Yok.')];
}
function panelVideo(v, ekle) {
  const k = v.ata; const pr = depoProje(v);
  const gs = gorevleri(v); const sv = v.surumler || [];
  const yor = v.proje ? [] : S.depo.yorumlar.filter((y) => y.video === v.kimlik && !y.gorev);
  const pv = v.proje && S.projeler[v.proje] ? S.projeler[v.proje].sv.video : null;
  ekle(e('h2', {}, pv ? `${pv.ders}: ${pv.konu}`
    : `${k.ad} · ${kitleAd(v.kitle)} ${sevAd(v.seviye)}`),
    e('div', { class: 'meta' }, e('span', { class: 'etiket' }, v.kod),
      v.eskiKod ? e('span', { class: 'etiket' }, `eski ${v.eskiKod}`) : null,
      e('span', { class: 'etiket' }, kitleAd(v.kitle)), e('span', { class: 'etiket' },
        sevAd(v.seviye)),
      e('span', { class: `etiket durum d-${v.durum}` }, ETIKET.durum[v.durum] || v.durum),
      e('span', {}, v.id)),
    v.not ? e('p', {}, v.not) : null,
    e('div', { class: 'satir' }, e('button', { class: 'btn ana', onclick: () => gorevFormu(v) },
      'Görev aç'),
      v.proje ? e('button', { class: 'btn', onclick: () => turevFormu(v.proje) }, 'Yeni türev')
        : null),
    e('h3', {}, `Kaynak LMS videoları (${k.lms.length})`),
    k.lms.length ? k.lms.map((l) => e('a', { class: `lms${l.eski ? ' eski' : ''}`, target: '_blank',
      rel: 'noopener',
      href: `https://vimeo.com/${l.vimeo}` }, l.ad, e('small', {},
        `${mmss(l.sure)} · ${sayi(l.izlenme)} izlenme · `
      + `${sayi(l.tamamlama)} tamamlama · ort. %${l.ortYuzde}${l.eski ? ' · eski' : ''}`)))
        : e('p', {}, 'Yok.'),
    e('h3', {}, `Sunumlar (${k.pptx.length})`),
    k.pptx.length ? e('div', { class: 'liste' }, k.pptx.map((a) => e('a', {}, a))) : e('p', {},
      'Yok.'),
    pv ? [...listeBolumu('Amaçlar', pv.amaclar, false).flat(3),
      ...listeBolumu('Can alıcı bilgiler', pv.canAlici, true).flat(3),
      ...listeBolumu('Kazanım (MEB)', pv.kazanim, false).flat(3)] : null,
    sv.length ? [e('h3', {}, `Sürümler (${sv.length})`), e('div', { class: 'liste' },
      sv.map((s) => e('a', {
      onclick: () => sec(`s:${v.proje}/${s.kimlik}`) }, `${ETIKET.durum[s.durum]} · ${s.ad}`)))]
        : null,
    e('h3', {}, `Görevler (${gs.length})`), gs.length ? gorevLinkleri(pr, gs) : e('p', {}, 'Yok.'),
    v.proje ? [e('h3', {}, 'Durum özeti'), ...GOREV_DURUM.map((d) =>
      e('p', {}, `${ETIKET.durum[d]}: ${gs.filter((g) => g.durum === d).length}`))] : null,
    v.proje ? null : [e('h3', {}, `Yorumlar (${yor.length})`), yor.map((y) => yorumKutusu(KAT, y)),
      yorumEkleme(KAT, { video: v.kimlik })]);
}

// ---- formlar ----
function formAc(baslik, alanlar, gonder) {
  const f = $('form'); f.replaceChildren(e('h2', {}, baslik));
  const girdi = {};
  for (const a of alanlar) {
    const g = a.tip === 'select' ? e('select', {}, a.secenek.map(([v, t]) => e('option',
      { value: v }, t)))
      : a.tip === 'metin' ? e('textarea', { rows: 3 }) : e('input', { type: 'text' });
    girdi[a.ad] = g; f.append(e('label', {}, a.etiket, g));
  }
  const kapat = () => { $('modal').hidden = true; };
  f.append(e('div', { class: 'alt' }, e('button', { type: 'button', class: 'btn', onclick: kapat },
    'Vazgeç'),
    e('button', { type: 'submit', class: 'btn ana' }, 'Kaydet')));
  f.onsubmit = async (ev) => {
    ev.preventDefault();
    const v = Object.fromEntries(Object.entries(girdi).map(([k, g]) => [k, g.value]));
    try { await gonder(v); kapat();
      await yukle(true); } catch { /* uyarı çağrıda gösterildi */ }
  };
  $('modal').hidden = false; Object.values(girdi)[0].focus();
}
const secList = (obj) => Object.entries(obj);
const surumSec = (p, bos) => [...(bos ? [['', bos]] : []),
  ...(proje(p).sv ? proje(p).sv.surumler : []).map((s) => [s.kimlik, s.ad])];
function gorevFormu(v) {
  const p = v ? depoProje(v) : PROJE;
  if (!proje(p)) return uyar(`proje verisi yok: ${p}`);
  formAc(v ? `Yeni görev: ${v.kod}` : 'Yeni görev', [
    { ad: 'baslik', etiket: 'Başlık', tip: 'girdi' },
    { ad: 'grup', etiket: 'Grup', tip: 'select', secenek: secList(ETIKET.grup) },
    { ad: 'tur', etiket: 'Tür', tip: 'select', secenek: secList(ETIKET.tur) },
    ...(p === KAT ? [] : [{ ad: 'surum', etiket: 'Sürüm', tip: 'select', secenek: surumSec(p,
      'Sürümsüz') }]),
    { ad: 'atanan', etiket: 'Atanan', tip: 'select', secenek: ATANAN.map((a) => [a, a]) },
    { ad: 'aciklama', etiket: 'Açıklama', tip: 'metin' },
  ], (f) => cagri(p, 'POST', '/gorev', { ...f, surum: f.surum || undefined, video: p === KAT
    ? v.kimlik : undefined }));
}
function turevFormu(p) {
  if (!proje(p) || !proje(p).sv) return uyar(`proje verisi yok: ${p}`);
  formAc('Yeni türev', [
    { ad: 'tur', etiket: 'Tür', tip: 'select', secenek: secList(ETIKET.surumTur) },
    { ad: 'ad', etiket: 'Ad', tip: 'girdi' },
    { ad: 'kaynak', etiket: 'Kaynak sürüm', tip: 'select', secenek: surumSec(p, 'Kaynak yok') },
    { ad: 'seviye', etiket: 'Seviye (isteğe bağlı)', tip: 'girdi' },
    { ad: 'senaryo_notu', etiket: 'Senaryo notu', tip: 'metin' },
  ], (v) => cagri(p, 'POST', '/surum', { ...v, kaynak: v.kaynak || undefined, seviye: v.seviye
    || undefined }));
}

// ---- araç çubuğu ----
function derinlikDugmeleri() {
  const hedef = $('derinlik'); if (!hedef.children.length) {
    hedef.append(...M.DERINLIK.map((d) => e('button', { class: 'btn', 'data-d': d, onclick: () =>
      acikAyarla(M.derinlik(S.agac, d)) }, DERINLIK_AD[d])));
  }
  const m = M.urlUret(S.acik);
  for (const b of hedef.children) b.classList.toggle('aktif', m === M.urlUret(M.derinlik(S.agac,
    b.dataset.d)));
}
function aramaYap() {
  const q = $('ara').value; S.ara = M.arama(S.agac, q);
  if (S.ara.aktif) S.acik = new Set([...S.acik, ...S.ara.ac]);
  kaydet(); ciz();
  const ilk = [...S.ara.eslesen][0];
  if (S.ara.aktif && ilk) hedefeGit(ilk);
}
function baglamaKur() {
  $('yg').onclick = () => gorevFormu(null);
  $('yt').onclick = () => turevFormu(PROJE);
  $('modal').addEventListener('pointerdown', (ev) =>
    { if (ev.target === $('modal')) $('modal').hidden = true; });
  document.addEventListener('keydown', (ev) =>
    { if (ev.key === 'Escape') $('modal').hidden = true; });
  $('sigdir').onclick = sigdir;
  addEventListener('resize', izgaraGenisligi);
  $('hepsi-ac').onclick = () => acikAyarla(M.hepsiniAc(S.agac));
  $('hepsi-kapa').onclick = () => acikAyarla(M.hepsiniKapat());
  let z = 0; $('ara').addEventListener('input', () => { clearTimeout(z); z = setTimeout(aramaYap,
    150); });
  const doldur = (id, bos, harita, alan) => {
    const s = $(id); s.replaceChildren(e('option', { value: '' }, bos),
      ...Object.entries(harita).map(([v, t]) => e('option', { value: v }, t)));
    s.onchange = () => { S.sus[alan] = s.value; ciz(); };
  };
  doldur('s-kitle', 'Hepsi', { ydt: 'YDT', maarif: 'Maarif 9–10' }, 'kitle');
  doldur('s-vdurum', 'Hepsi', Object.fromEntries(M.VIDEO_DURUM.map((d) => [d, ETIKET.durum[d]])),
    'vdurum');
  doldur('s-grup', 'Hepsi', ETIKET.grup, 'grup');
  doldur('s-durum', 'Hepsi', Object.fromEntries(GOREV_DURUM.map((d) => [d, ETIKET.durum[d]])),
    'durum');
  doldur('s-atanan', 'Hepsi', Object.fromEntries(ATANAN.map((a) => [a, a])), 'atanan');
  $('lejant').append(...M.VIDEO_DURUM.map((d) => e('span', { class: `d-${d}` }, e('i', {}),
    ETIKET.durum[d])));
}

baglamaKur(); kaydirmaKur(); dinleyiciKur(); uygula();
yukle(true).then(() => {
  const s = $('altbaslik'); const n = M.sayimlar(S.agac);
  s.textContent = `${n.unite} ünite · ${n.konu} konu · ${n.kaynak} kaynak video`
    + ` · ${n.video} planlı video`;
}).catch((x) => uyar(`veri yüklenemedi: ${x.message}`));
setInterval(() => { if (!$('modal').hidden
  || document.activeElement?.tagName === 'TEXTAREA') return;
  yukle(false).catch(() => {}); }, 6000);
window.__harita = { S, M, sec, sigdir };
