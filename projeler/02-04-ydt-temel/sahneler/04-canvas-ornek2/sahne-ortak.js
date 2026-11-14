// Düz canvas sahnelerinin (04, 05) ortak iskeleti: zaman, olaylar, kalem öğeleri, cümle belirmesi.
// Her öğe {ciz(ctx, f)} taşır; zaman yalnız kare numarasından gelir (Math.random ve Date yok).
import { kunyeHazirla, zeminCiz, kunyeCiz, RENK, RT, renkCoz } from "/projeler/02-04-ydt-temel/ortak/kunye.js";
import { kalemCizgi, darbeCiz, svgYollari, elips, ok, kutu, altCizgi, kis, lerp, yavasla, geriTasma, hash,
  tohumSifirla, yaziDarbeleri, yaziCiz } from "/projeler/02-04-ydt-temel/ortak/kalem-canvas.js";
// Geliştirme günlüğü (12.11, pp g-11): POST /log yalnız yerel geliştirme sunucusunda; yayında istek yok.
const YEREL_SUNUCU = /^(localhost|127\.0\.0\.1|\[::1\]|10\.\d+\.\d+\.\d+|192\.168\.\d+\.\d+)$/
  .test(location.hostname);
const logGonder = (o) => (YEREL_SUNUCU ? fetch("/log", o).catch(() => {}) : Promise.resolve());

const gunluk = (o) => (new URLSearchParams(location.search).get("canli") === "1" ? Promise.resolve() : logGonder(o));
export { RENK, RT, renkCoz, elips, ok, kutu, altCizgi, kis, lerp, yavasla, geriTasma, hash };
const KOK = "/projeler/02-04-ydt-temel/ortak";
const OLC = document.createElement("canvas").getContext("2d");
const boyOku = (font) => parseFloat(font.match(/(\d+(?:\.\d+)?)px/)[1]);

// Yazı genişliği (px) ölçer.
export function olc(font, metin) { OLC.font = font; return OLC.measureText(metin).width; }

// Çoklu parça [[metin, renk], ...] toplam genişliği.
const toplamGen = (font, parca) => parca.reduce((t, [m]) => t + olc(font, m), 0);

export const FONT = { cumle: "700 64px Fredoka", not: "700 48px Caveat", etiket: "700 36px Lexend" };

export class Sahne {
  // a: {tbas, kare, icerik, bolum, cumle} — tbas küresel sn, kare/icerik zaman.json'dan.
  constructor(a) {
    Object.assign(this, { tbas: a.tbas, kareSay: a.kare, icerik: a.icerik, bolum: a.bolum, cumle: a.cumle,
      kayma: a.kayma || 0 });   // kayma: sözcük zamanlarını eski tbas çerçevesine çevirir (sn)
    this.ogeler = []; this.olaylar = new Map(); this.ilkBas = Infinity;
    this.cv = document.getElementById("cv"); this.ctx = this.cv.getContext("2d");
  }

  // Fontları, logoyu, gren karolarını ve cümlenin sözcük zamanlarını yükler.
  async kur() {
    tohumSifirla(1);
    this.K = await kunyeHazirla();
    const r = await fetch(`${KOK}/anlatim/sozcukler.json`);
    this.sozc = (await r.json()).filter((s) => s.cumle === this.cumle)
      .map((s) => ({ ...s, t0: s.t0 + this.kayma, t1: s.t1 + this.kayma }));
    // El yazısı verisi (tegaki, Caveat 700 Türkçe; ortak/tegaki/caveat-tr/KAYNAK.md)
    const [M, G] = await Promise.all([fetch(`/ortak/tegaki/caveat-tr/metrik.json`),
      fetch(`/ortak/tegaki/caveat-tr/glyphData-700.json`)]);
    this.EY = { M: await M.json(), G: await G.json() };
  }

  // Küresel saniyeyi yerel (kesirli) kareye çevirir.
  fr(t) { return (t - this.tbas) * 30; }

  // Yerel kareden küresel saniye.
  zm(f) { return this.tbas + f / 30; }

  // Sözcük dizisi: adı ad, t0'ı yakin'a en yakın girişten başlayıp adet sözcük döner.
  dizi(ad, yakin, adet) {
    let en = -1, fark = 1e9;
    this.sozc.forEach((s, i) => { if (s.sozcuk === ad && Math.abs(s.t0 - yakin) < fark) { fark = Math.abs(s.t0 - yakin); en = i; } });
    return this.sozc.slice(en, en + adet);
  }

  // Tek sözcüğün t0 değerini döner.
  t0(ad, yakin) { return this.dizi(ad, yakin, 1)[0].t0; }

  // Olay yazar: aynı karede en çok 3, aynı tür birleşir.
  olay(f, tur, guc) {
    f = Math.max(0, Math.min(this.kareSay - 1, Math.round(f)));
    for (let k = 0; k < 8; k++, f++) {
      const a = this.olaylar.get(f) || [], var_ = a.find((o) => o.tur === tur);
      if (var_) { var_.guc = Math.max(var_.guc, +guc.toFixed(2)); return; }
      if (a.length < 3) { a.push({ kare: f, tur, guc: +guc.toFixed(2) }); this.olaylar.set(f, a); return; }
    }
  }

  // Olay listesi (kareye göre sıralı).
  olayListe() { return [...this.olaylar.values()].flat().sort((a, b) => a.kare - b.kare || a.tur.localeCompare(b.tur)); }

  // Öğeyi (ya da öğe dizisini) sahneye ekler ve döner.
  koy(e) { if (Array.isArray(e)) e.forEach((x) => this.koy(x)); else this.ogeler.push(e); return e; }

  // İlk görünme karesini kaydeder (ilk 12 kare boş olmalı).
  bas(fb) { this.ilkBas = Math.min(this.ilkBas, fb); }

  // Tek kalem darbesi öğesi. tb küresel sn başlangıç, sure sn. ses: false ya da olay gücü.
  darbe(pts, o, tb, sure, ses) {
    const c = kalemCizgi(pts, o), fb = this.fr(tb), n = Math.max(1, sure * 30);
    this.bas(fb);
    if (ses !== false) this.olay(fb, "cizgi", ses || Math.min(0.7, 0.4 + c.L / 1500));
    const e = { c, fb, n, carpan: 1, ciz: (ctx, f) => { const t = yavasla((f - fb) / n); if (t > 0) darbeCiz(ctx, c, t, e.carpan); } };
    return e;
  }

  // Birden çok nokta dizisini sırayla darbeler olarak çizer; öğe dizisi döner.
  darbeler(liste, o, tb, sure, aralik, ses) {
    return liste.map((p, i) => this.darbe(p, { ...o }, tb + i * aralik, sure, i === 0 ? ses : false));
  }

  // El yazısı notu (Caveat, tegaki darbeleri): kalem gerçekten yazar. a: {metin, x, y (taban çizgisi),
  // boy (px, varsayılan FONT.not), renk, tb, sure (hedef sn; yoksa doğal), sozcukler ([{t0,t1}] sahne
  // çerçevesi: her sözcük kendi konuşma penceresinde yazılır — hız kuralı 05.11 karar 6), ses}.
  elYazisi(a) {
    const boy = a.boy || boyOku(FONT.not), M = this.EY.M;
    const Y = yaziDarbeleri(a.metin, this.EY.G, { upm: M.unitsPerEm, asc: M.ascender, boy, x: a.x,
      taban: a.y, renk: a.renk, sozcukler: a.sozcukler, hedefSure: a.sure, tohum: a.tohum });
    const mutlak = !!a.sozcukler, fb = mutlak ? this.fr(a.sozcukler[0].t0) : this.fr(a.tb);
    this.bas(fb);
    if (a.ses !== false) {
      const baslar = mutlak ? a.sozcukler.map((s) => this.fr(s.t0)) : [fb];
      baslar.forEach((f) => this.olay(f, "cizgi", a.ses || 0.35));
    }
    return { x: a.x, w: Y.gen, Y, sure: Y.sure, ciz: (ctx, f) => {
      const t = mutlak ? this.zm(f) : (f - fb) / 30; if (t <= (mutlak ? a.sozcukler[0].t0 : 0)) return;
      if (a.alfa == null || a.alfa >= 0.2) {
        window.__kalemKutu?.ekle("yazi", a.metin, a.x, a.y - boy * 0.9, Y.gen, boy * 1.1);
      }
      yaziCiz(ctx, Y, t, 1);
    } };
  }

  // Kalem çizimi grubu (SVG yollarından): figür/nesne. a: {svg, kutu, enCok, w, renk, tb, sure, olayEnCok, nefes}.
  cizim(a) {
    const yollar = svgYollari(a.svg, a.kutu, { enCok: a.enCok || 25, esik: a.esik == null ? 0.02 : a.esik });
    const g = { cocuk: [], donusum: null, dolgu: null, bitis: a.tb + a.sure, yollar };
    const n = yollar.length;
    gunluk({ method: "POST", body: `CIZIM ${a.ad || "?"} darbe=${n} esik=${a.esik == null ? 0.02 : a.esik}` });
    yollar.forEach((p, i) => {
      const dur = Math.min(a.sure * 0.6, 0.15 + p.L / 1800), bas = a.tb + (n > 1 ? i / (n - 1) : 0) * (a.sure - dur);
      g.cocuk.push(this.darbe(p, { w: a.w, renk: a.renk, alfa: a.alfa, uc0: 10, uc1: 22 }, bas, dur,
        i < (a.olayEnCok == null ? 6 : a.olayEnCok) ? undefined : false));
    });
    const fSon = this.icerik, fb = this.fr(a.tb + a.sure);
    const cx = a.kutu.x + a.kutu.w / 2, cy = a.kutu.y + a.kutu.h;
    if (a.nefes !== false) {
      g.donusum = (f) => {
        const ph = (Math.min(f, fSon) - fb) / 180, o = f < fb ? 1 : 1 + 0.006 * (1 - Math.cos(ph * Math.PI * 2));
        return { cx, cy, tx: 0, ty: 0, dondur: 0, olcek: o };
      };
    }
    g.ciz = (ctx, f) => {
      ctx.save();
      const d = g.donusum ? g.donusum(f) : null;
      if (f >= this.fr(a.tb) && (a.alfa == null || a.alfa >= 0.2)) {
        // Kanca: kutu çizimle aynı dönüşümden geçer (kalkan uçak, nefes ölçeği)
        let { x, y, w, h } = a.kutu;
        if (d) {
          const c = Math.cos(d.dondur || 0), s = Math.sin(d.dondur || 0), xs = [], ys = [];
          for (const [px, py] of [[x, y], [x + w, y], [x, y + h], [x + w, y + h]]) {
            const dx = (px - d.cx) * d.olcek, dy = (py - d.cy) * d.olcek;
            xs.push(d.cx + d.tx + dx * c - dy * s);
            ys.push(d.cy + d.ty + dx * s + dy * c);
          }
          x = Math.min(...xs); y = Math.min(...ys); w = Math.max(...xs) - x; h = Math.max(...ys) - y;
        }
        window.__kalemKutu?.ekle("cizim", a.ad || "cizim", x, y, w, h);
      }
      if (d) { ctx.translate(d.cx + d.tx, d.cy + d.ty); if (d.dondur) ctx.rotate(d.dondur); ctx.scale(d.olcek, d.olcek); ctx.translate(-d.cx, -d.cy); }
      if (g.dolgu) {
        const al = kis((f - g.dolgu.fb) / 8);
        if (al > 0) {
          ctx.globalAlpha = al; ctx.fillStyle = renkCoz(g.dolgu.renk);
          for (const pl of (Array.isArray(g.dolgu.nokta[0][0]) ? g.dolgu.nokta : [g.dolgu.nokta])) {
            ctx.beginPath(); pl.forEach((q, i) => (i ? ctx.lineTo(q[0], q[1]) : ctx.moveTo(q[0], q[1]))); ctx.closePath(); ctx.fill();
          }
        }
      }
      for (const c of g.cocuk) c.ciz(ctx, f);
      ctx.restore();
    };
    return g;
  }

  // Parçalı yazı (pop: ölçek 0,92→1 + alfa). a: {parca:[[metin,renk]], x, y, font, hiza, tb, sure, olcek0, ses}.
  metinPop(a) {
    const tw = toplamGen(a.font, a.parca), x0 = a.hiza === "orta" ? a.x - tw / 2 : a.x, boy = boyOku(a.font);
    const fb = this.fr(a.tb), n = (a.sure || 0.35) * 30, s0 = a.olcek0 == null ? 0.92 : a.olcek0;
    this.bas(fb);
    if (a.ses) this.olay(fb, a.turu || "tik", a.ses);
    return { x: x0, w: tw, y: a.y, fb, ciz: (ctx, f) => {
      const u = yavasla((f - fb) / n); if (u <= 0) return;
      const al = u * (a.alfa == null ? 1 : a.alfa);
      if (al >= 0.2) {
        window.__kalemKutu?.ekle("yazi", a.parca.map(([m]) => m).join(""), x0, a.y - boy * 0.9, tw, boy * 1.1);
      }
      ctx.save(); ctx.globalAlpha = al; ctx.font = a.font; ctx.textAlign = "left";
      ctx.textBaseline = "alphabetic";
      const cx = x0 + tw / 2, cy = a.y - boy * 0.35, s = lerp(s0, 1, u);
      ctx.translate(cx, cy); ctx.scale(s, s); ctx.translate(-cx, -cy);
      let xx = x0; for (const [m, r] of a.parca) { ctx.fillStyle = renkCoz(r); ctx.fillText(m, xx, a.y); xx += olc(a.font, m); }
      ctx.restore();
    } };
  }

  // El notu (Caveat): soldan sağa maske ile yazılır. a: {parca, x, y, font, tb, sure, ses}.
  not(a) {
    const font = a.font || FONT.not, tw = toplamGen(font, a.parca), boy = boyOku(font);
    const fb = this.fr(a.tb), n = (a.sure || 0.5) * 30;
    this.bas(fb);
    if (a.ses !== false) this.olay(fb, "tik", a.ses || 0.4);
    return { x: a.x, w: tw, ciz: (ctx, f) => {
      const u = kis((f - fb) / n); if (u <= 0) return;
      if (u >= 0.2) {
        window.__kalemKutu?.ekle("yazi", a.parca.map(([m]) => m).join(""), a.x, a.y - boy * 0.9, tw * u, boy * 1.1);
      }
      ctx.save(); ctx.beginPath(); ctx.rect(a.x - 8, a.y - boy * 1.1, (tw + 16) * u, boy * 1.6); ctx.clip();
      ctx.font = font; ctx.textAlign = "left"; ctx.textBaseline = "alphabetic";
      let xx = a.x; for (const [m, r] of a.parca) { ctx.fillStyle = renkCoz(r); ctx.fillText(m, xx, a.y); xx += olc(font, m); }
      ctx.restore();
    } };
  }

  // İngilizce cümle: sözcük sözcük belirir, konuşulan sözcüğün altında sarı alt çizgi kayar.
  // a: {sozcukler:[{sozcuk,t0,t1}], x, y, maxGen, satir, font, renk}
  cumleYaz(a) {
    const font = a.font || FONT.cumle, maks = a.maxGen || 980, boy = boyOku(font), satirH = a.satirH || 84;
    const ek = a.bosluk == null ? 10 : a.bosluk;  // sözcük aralığına ek px (halkalar komşu harfe değmesin)
    const kel = a.sozcukler.map((s) => ({ m: s.sozcuk, t0: s.t0, t1: s.t1 }));
    let satirlar = [[]], cur = "";
    for (const k of (a.satirSay ? [] : kel)) {
      const dene = cur ? `${cur} ${k.m}` : k.m;
      if (cur && olc(font, dene) + ek * satirlar[satirlar.length - 1].length > maks) { satirlar.push([]); cur = k.m; } else cur = dene;
      satirlar[satirlar.length - 1].push(k);
    }
    if (a.satirSay) { satirlar = []; let ix = 0; for (const n of a.satirSay) { satirlar.push(kel.slice(ix, ix + n)); ix += n; } }   // sabit satır sonları
    satirlar.forEach((sat, si) => {
      const yb = a.y + si * satirH;
      sat.forEach((k, i) => {
        const onek = sat.slice(0, i).map((q) => q.m).join(" ") + (i ? " " : "");
        k.x = a.x + olc(font, onek) + i * ek; k.w = olc(font, k.m); k.y = yb; k.satir = si;
      });
    });
    kel.forEach((k, i) => {
      k.alt = kalemCizgi(altCizgi(k.x - 4, k.x + k.w + 4, k.y + 15, 40 + i), { w: 8.5, renk: RT.vurguDolgu, alfa: 0.85, uc0: 8, uc1: 14, tohum: 700 + i });
    });
    this.bas(this.fr(kel[0].t0));
    this.olay(this.fr(kel[0].t0), "tik", 0.5);
    const e = { kel, font, boy, ciz: (ctx, f) => {
      const T = this.zm(f);
      let idx = -1; kel.forEach((k, i) => { if (T >= k.t0) idx = i; });
      if (idx >= 0) {
        const son = kel[kel.length - 1], sol = idx === kel.length - 1 ? 1 - kis((T - (son.t1 + 0.1)) / 0.45) : 1;
        const u = yavasla((T - kel[idx].t0) / 0.1);
        if (sol >= 0.2) {
          const ak = kel[idx];
          window.__kalemKutu?.ekle("isaret", "altCizgi", ak.x - 4, ak.y + 10, ak.w + 8, 14);
        }
        darbeCiz(ctx, kel[idx].alt, u, sol);
        if (idx > 0 && u < 1) {
          const p = kel[idx - 1]; ctx.save(); ctx.beginPath();
          ctx.rect(lerp(p.x - 8, p.x + p.w + 8, u), p.y - 80, 4000, 140); ctx.clip();
          darbeCiz(ctx, p.alt, 1, 1); ctx.restore();
        }
      }
      ctx.save(); ctx.font = font; ctx.textAlign = "left"; ctx.textBaseline = "alphabetic"; ctx.fillStyle = renkCoz(a.renk || RT.murekkep);
      for (const k of kel) {
        const u = kis((T - k.t0) / 0.12); if (u <= 0) continue;
        if (u >= 0.2) {
          window.__kalemKutu?.ekle("yazi", k.m, k.x, k.y - boy * 0.9, k.w, boy * 1.1);
        }
        ctx.save(); ctx.globalAlpha = yavasla(u); ctx.beginPath();
        ctx.rect(k.x - 6, k.y - boy * 1.1, (k.w + 12) * yavasla(u), boy * 1.6); ctx.clip();
        ctx.fillText(k.m, k.x, k.y); ctx.restore();
      }
      ctx.restore();
    } };
    return e;
  }

  // Sözcüğün çevresine sarı el elipsi çeker (belirteç). k: cumle öğesinden kel girdisi.
  halka(k, tb, sure = 0.35, tohum = 1, pay = 6) {
    const el = elips(k.x + k.w / 2, k.y - 22, k.w / 2 + pay, 52, -0.04 + 0.03 * hash(tohum, 3, 3), tohum);
    const d = this.darbe(el, { w: 6, renk: RT.vurgu, alfa: 0.85, uc0: 14, uc1: 30 }, tb, sure, 0.55);
    const eskiCiz = d.ciz;
    d.ciz = (ctx, f) => {
      const fb = this.fr(tb), n = Math.max(1, sure * 30);
      const t = yavasla((f - fb) / n);
      if (t >= 0.2) {
        window.__kalemKutu?.ekle("isaret", "halka:" + (k.m || ""), k.x - pay, k.y - 48, k.w + 2 * pay, 52);
      }
      eskiCiz(ctx, f);
    };
    return d;
  }

  // Daire içinde sayı (1,2,3): krem el dairesi + Fredoka sayı pop.
  daireSayi(sayi, cx, cy, tb) {
    const d = this.darbe(elips(cx, cy, 56, 54, 0.1, 5), { w: 4.6, uc0: 18, uc1: 34 }, tb, 0.55, 0.6);
    const m = this.metinPop({ parca: [[String(sayi), RT.murekkep]], x: cx, y: cy + 26, font: "700 78px Fredoka", hiza: "orta",
      tb: tb + 0.3, sure: 0.35, olcek0: 0.7, ses: 0.8, turu: "vurus" });
    return [d, m];
  }

  // Parıltı: 4 ışın büyür ve söner (süs, kalem değil). tb küresel sn.
  parilti(cx, cy, tb, boyut = 22) {
    const fb = this.fr(tb);
    this.bas(fb); this.olay(fb, "parilti", 0.5);
    return { ciz: (ctx, f) => {
      const u = (f - fb) / 16; if (u <= 0 || u >= 1) return;
      ctx.save(); ctx.strokeStyle = renkCoz(RT.vurgu); ctx.lineCap = "round"; ctx.lineWidth = 4; ctx.globalAlpha = (1 - u) * 0.95;
      for (let i = 0; i < 4; i++) {
        const a = i * Math.PI / 4 + 0.2, r0 = boyut * 0.35 * yavasla(u), r1 = boyut * (0.5 + 0.9 * yavasla(u)) * (i % 2 ? 0.7 : 1);
        ctx.beginPath(); ctx.moveTo(cx + Math.cos(a) * r0, cy + Math.sin(a) * r0);
        ctx.lineTo(cx + Math.cos(a) * r1, cy + Math.sin(a) * r1);
        ctx.moveTo(cx - Math.cos(a) * r0, cy - Math.sin(a) * r0); ctx.lineTo(cx - Math.cos(a) * r1, cy - Math.sin(a) * r1); ctx.stroke();
      }
      ctx.restore();
    } };
  }

  // Nabız: sarı halka büyüyüp söner; içerik sonuna kadar döner.
  nabiz(cx, cy, r, tb) {
    const fb = this.fr(tb), fSon = this.icerik;
    return { ciz: (ctx, f) => {
      if (f < fb) return;
      const ph = ((Math.min(f, fSon) - fb) % 40) / 40;
      ctx.save(); ctx.strokeStyle = renkCoz(RT.vurgu); ctx.lineWidth = 3; ctx.globalAlpha = (1 - ph) * 0.6;
      ctx.beginPath(); ctx.arc(cx, cy, r * (1 + 1.4 * yavasla(ph)), 0, Math.PI * 2); ctx.stroke(); ctx.restore();
    } };
  }

  // Formül kartı: el kutusu + satırlar. a: {x, y, w, h, tb, satirlar:[{parca, x, y, font, tb}]}.
  kart(a) {
    const o = [];
    const fb = this.fr(a.tb);
    const darbeler = this.darbeler(kutu(a.x, a.y, a.w, a.h, 90 + (a.tohum || 0)), { w: 3.6, renk: RT.ikincil, uc0: 10, uc1: 18 }, a.tb, a.kutuSure || 0.14,
      a.kutuAralik || 0.1, 0.55);
    darbeler.forEach((e, i) => {
      if (i === 0) {
        const eskiCiz = e.ciz;
        e.ciz = (ctx, f) => {
          if (f >= fb) {
            window.__kalemKutu?.ekle("kart", a.ad || "kart", a.x, a.y, a.w, a.h);
          }
          eskiCiz(ctx, f);
        };
      }
      o.push(e);
    });
    a.satirlar.forEach((s, i) => o.push(this.metinPop({ ...s, ses: i === 0 ? 0.5 : false })));
    return o;
  }

  // Bir kareyi çizer ve canvas'ı döndürür (sürücü kare(f)).
  async kare(f, hepsi) {
    if (typeof window !== "undefined" && window.__kalemKutu) {
      window.__kalemKutu.kare = [];
      window.__kalemKutu.ctx = this.ctx;
    }
    const ctx = this.ctx;
    zeminCiz(ctx, f, this.K);
    for (const e of this.ogeler) e.ciz(ctx, f);
    kunyeCiz(ctx, { bolum: this.bolum, etkin: 1, logo: this.K.logo });
    if (f === this.kareSay - 1) {
      await gunluk({ method: "POST", body: `ILKBAS ${Math.round(this.ilkBas)}` });
      await gunluk({ method: "POST", body: "OLAYLAR " + JSON.stringify(this.olayListe()) });
    }
    return this.cv;
  }
}
