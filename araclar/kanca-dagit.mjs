#!/usr/bin/env node
// araclar/kanca-dagit.mjs
// Çakışma kapısı kancasını paket motor kopyalarına dağıtır.
// Kullanım: node araclar/kanca-dagit.mjs <paket...> [--kuru] [--geri]
//
// Dosyalar:
//   - projeler/<paket>/ortak/kalem-canvas.js
//   - projeler/<paket>/ortak/kunye.js
//   - projeler/<paket>/sahneler/*/kalem-paper.js
//   - projeler/<paket>/sahneler/*/sahne-ortak.js
//
// Kurallar:
//   - Çapa bulunamazsa dosyayı DEĞİŞTİRMEZ, "ÇAPA YOK <dosya> <çapa>" yazar, çıkış kodu 1.
//   - Kanca zaten varsa "VAR <dosya>" yazar ve dokunmaz.
//   - --kuru yalnız simüle eder, diske yazmaz.
//   - --geri ise _is/cakisma/dagit/<paket>/yedek/ altındaki yedeklerden geri yazar.

import fs from "node:fs";
import path from "node:path";

const KOK = path.resolve(path.dirname(new URL(import.meta.url).pathname), "..");

// --- Kanca Metinleri ---

const KANCA_KALEM_CANVAS_TANIM = `// Kanca (yalnız kayıt): pencerede yoksa oluştur
if (typeof window !== "undefined" && !window.__kalemKutu) {
  window.__kalemKutu = {
    kare: [],
    ekle(tur, ad, x, y, w, h) {
      if (w > 0 && h > 0) {
        this.kare.push({
          tur,
          ad: String(ad || ""),
          x: Math.round(x),
          y: Math.round(y),
          w: Math.round(w),
          h: Math.round(h),
        });
      }
    },
  };
}

`;

const KANCA_KUNYE_TANIM = `
// Kanca (yalnız kayıt): pencerede yoksa oluştur
if (typeof window !== "undefined" && !window.__kalemKutu) {
  window.__kalemKutu = {
    kare: [],
    ekle(tur, ad, x, y, w, h) {
      if (w > 0 && h > 0) {
        this.kare.push({
          tur,
          ad: String(ad || ""),
          x: Math.round(x),
          y: Math.round(y),
          w: Math.round(w),
          h: Math.round(h),
        });
      }
    },
  };
}
`;

const KANCA_KUNYE_CIZ_EK = `

  // Kanca: künye bölgelerini 'kunye' türü olarak ekle (alfa >= 0.2 ise)
  if (typeof window !== "undefined" && window.__kalemKutu && alfa >= 0.2) {
    window.__kalemKutu.ekle("kunye", "kunye:sol-ust", k.kenar, k.ustTaban - k.dersYazi, dw + 14 + sw, k.dersYazi + 6);
    if (bolum && bw > 0) {
      window.__kalemKutu.ekle("kunye", "kunye:sag-ust", W - k.kenar - bw, k.ustTaban - k.bolumYazi, bw, k.bolumYazi + 6);
    }
    if (logo && logoW > 0) {
      window.__kalemKutu.ekle("kunye", "kunye:logo", k.kenar, H - 44 - logoH, logoW, logoH);
    }
    const ajandaGen = (W - k.kenar) - x;
    if (ajandaGen > 0) {
      window.__kalemKutu.ekle("kunye", "kunye:ajanda", x, k.altTaban - k.ajandaYazi - 4, ajandaGen, k.ajandaYazi + 8);
    }
  }
`;

const KANCA_PAPER_TOPLA = `  // ---------- Kanca (paperTopla) ----------
  if (typeof window !== "undefined") {
    if (!window.__kalemKutu) {
      window.__kalemKutu = {
        kare: [],
        ekle(tur, ad, x, y, w, h) {
          if (w > 0 && h > 0) {
            this.kare.push({
              tur,
              ad: String(ad || ""),
              x: Math.round(x),
              y: Math.round(y),
              w: Math.round(w),
              h: Math.round(h),
            });
          }
        },
      };
    }
    window.__kalemKutu.paperTopla = function () {
      if (!P || !P.project) return;
      const kunyeler = (this.kare || []).filter((k) => k.tur === "kunye");
      this.kare = kunyeler;
      function topla(item) {
        if (!item || item.visible === false) return;
        if (item.opacity != null && item.opacity < 0.2) return;
        if (item.data && item.data.kalemTur) {
          let b = item.bounds;
          if (item.clipped && item.children && item.children.length > 0) {
            const mask = item.children.find((c) => c.clipMask);
            const icerikler = item.children.filter((c) => !c.clipMask && c.visible !== false);
            if (mask && icerikler.length > 0) {
              let ix0 = Infinity, iy0 = Infinity, ix1 = -Infinity, iy1 = -Infinity;
              for (const c of icerikler) {
                const cb = c.bounds;
                if (cb.width > 0 && cb.height > 0) {
                  ix0 = Math.min(ix0, cb.x);
                  iy0 = Math.min(iy0, cb.y);
                  ix1 = Math.max(ix1, cb.x + cb.width);
                  iy1 = Math.max(iy1, cb.y + cb.height);
                }
              }
              if (ix0 < ix1 && iy0 < iy1) {
                const mb = mask.bounds;
                const x0 = Math.max(ix0, mb.x);
                const y0 = Math.max(iy0, mb.y);
                const x1 = Math.min(ix1, mb.x + mb.width);
                const y1 = Math.min(iy1, mb.y + mb.height);
                const w = x1 - x0;
                const h = y1 - y0;
                if (w > 0 && h > 0) {
                  b = { x: x0, y: y0, width: w, height: h };
                } else {
                  return;
                }
              }
            }
          }
          if (b && b.width > 0 && b.height > 0) {
            window.__kalemKutu.ekle(item.data.kalemTur, item.data.kalemAd || "", b.x, b.y, b.width, b.height);
            return;
          }
        }
        if (item.children && item.children.length > 0) {
          for (const child of item.children) topla(child);
        }
      }
      for (const layer of P.project.layers) topla(layer);
    };
  }

`;

// --- Dosya Dönüştürücüleri ---

export function kancaKalemCanvas(icerik, dosyaYol) {
  if (icerik.includes("__kalemKutu")) {
    return { durum: "VAR", icerik };
  }
  const CAPA = "// ---------- küçük yardımcılar ----------";
  if (!icerik.includes(CAPA)) {
    return { durum: "CAPA_YOK", capa: CAPA, dosyaYol };
  }
  const yeniIcerik = icerik.replace(CAPA, KANCA_KALEM_CANVAS_TANIM + CAPA);
  return { durum: "DEGISTI", icerik: yeniIcerik };
}

export function kancaKunye(icerik, dosyaYol) {
  if (icerik.includes("__kalemKutu")) {
    return { durum: "VAR", icerik };
  }

  const CAPA1 = "export const RENK = { ...TEMALAR.koyu };";
  if (!icerik.includes(CAPA1)) {
    return { durum: "CAPA_YOK", capa: CAPA1, dosyaYol };
  }

  // kunyeCiz içi çapa
  const CAPA2 =
`  const dw = ctx.measureText(k.ders).width;
  ctx.fillStyle = R.ikincil; ctx.font = \`500 \${k.seviyeYazi}px Lexend\`; ctx.fillText(\`· \${k.seviye}\`, k.kenar + dw + 14, k.ustTaban);
  ctx.textAlign = "right"; ctx.fillStyle = R.vurgu; ctx.font = \`700 \${k.bolumYazi}px Lexend\`;
  ctx.fillText(bolum || "", W - k.kenar, k.ustTaban);
  if (logo) { const h = k.logoYuk, w = h * 1920 / 476.3; ctx.drawImage(logo, k.kenar, H - 44 - h, w, h); }`;

  if (!icerik.includes(CAPA2)) {
    return { durum: "CAPA_YOK", capa: "kunyeCiz ders/bolum/logo", dosyaYol };
  }

  const YENI_KUNYE_CIZ_BAS =
`  const dw = ctx.measureText(k.ders).width;
  ctx.fillStyle = R.ikincil; ctx.font = \`500 \${k.seviyeYazi}px Lexend\`; ctx.fillText(\`· \${k.seviye}\`, k.kenar + dw + 14, k.ustTaban);
  const sw = ctx.measureText(\`· \${k.seviye}\`).width;
  ctx.textAlign = "right"; ctx.fillStyle = R.vurgu; ctx.font = \`700 \${k.bolumYazi}px Lexend\`;
  ctx.fillText(bolum || "", W - k.kenar, k.ustTaban);
  const bw = bolum ? ctx.measureText(bolum).width : 0;
  let logoW = 0, logoH = 0;
  if (logo) { logoH = k.logoYuk; logoW = logoH * 1920 / 476.3; ctx.drawImage(logo, k.kenar, H - 44 - logoH, logoW, logoH); }`;

  // Restore sonrası ekleme çapası
  const CAPA3 = `  ctx.restore();`;
  const idx2 = icerik.indexOf(CAPA2);
  const idxRestore = icerik.indexOf(CAPA3, idx2);
  if (idxRestore === -1) {
    return { durum: "CAPA_YOK", capa: "kunyeCiz ctx.restore()", dosyaYol };
  }

  let metin = icerik.replace(CAPA1, CAPA1 + KANCA_KUNYE_TANIM);
  metin = metin.replace(CAPA2, YENI_KUNYE_CIZ_BAS);

  // Restore sonrasına KANCA_KUNYE_CIZ_EK ekle
  // Sadece kunyeCiz içindeki ilk restore'a eklemek için:
  const idxRestoreSonrasi = metin.indexOf(CAPA3, metin.indexOf(YENI_KUNYE_CIZ_BAS));
  if (idxRestoreSonrasi === -1) {
    return { durum: "CAPA_YOK", capa: "kunyeCiz ctx.restore() sonra", dosyaYol };
  }
  metin = metin.slice(0, idxRestoreSonrasi + CAPA3.length) + KANCA_KUNYE_CIZ_EK + metin.slice(idxRestoreSonrasi + CAPA3.length);

  return { durum: "DEGISTI", icerik: metin };
}

export function kancaKalemPaper(icerik, dosyaYol) {
  if (icerik.includes("paperTopla") || (icerik.includes("__kalemKutu") && icerik.includes("kalemTur"))) {
    return { durum: "VAR", icerik };
  }

  let metin = icerik;

  // 1. ciz
  const CAPA_CIZ = "const c = kalemGeo(pts, o); c.bas = o.bas || 0; c.sure = Math.max(2, o.sure || 20); c.og = o.oge || kok; c.yolP = null; c.tam = false;";
  if (!metin.includes(CAPA_CIZ)) {
    return { durum: "CAPA_YOK", capa: "ciz kalemGeo", dosyaYol };
  }
  metin = metin.replace(CAPA_CIZ, CAPA_CIZ + "\n    c.tur = o.tur || \"cizim\"; c.ad = o.ad || \"cizgi\";");

  // 2. daire
  const CAPA_DAIRE = "return ciz(pts, { w: 7.5, renk: RT.vurgu, alfa: 0.85, amp: 0.4, uc0: 14, uc1: 40, ...o });";
  if (!metin.includes(CAPA_DAIRE)) {
    return { durum: "CAPA_YOK", capa: "daire ciz", dosyaYol };
  }
  metin = metin.replace(CAPA_DAIRE, "return ciz(pts, { w: 7.5, renk: RT.vurgu, alfa: 0.85, amp: 0.4, uc0: 14, uc1: 40, tur: \"isaret\", ad: o.ad || \"daire\", ...o });");

  // 3. ok
  const CAPA_OK1 = "const g = ciz(pts, { w, renk, alfa, bas: o.bas, sure, uc0: 10, uc1: 14, amp: 0.7, oge: o.oge });";
  if (!metin.includes(CAPA_OK1)) {
    return { durum: "CAPA_YOK", capa: "ok govde ciz", dosyaYol };
  }
  metin = metin.replace(CAPA_OK1, "const g = ciz(pts, { w, renk, alfa, bas: o.bas, sure, uc0: 10, uc1: 14, amp: 0.7, oge: o.oge, tur: \"isaret\", ad: o.ad || \"ok\" });");

  const CAPA_OK2 = "return ciz([rot(0.5), tip, rot(-0.5)], { w: w * 0.9, renk, alfa, bas: o.bas + sure - 2, sure: 8, uc0: 6, uc1: 6, amp: 0.4, duz: true, oge: o.oge, ses }); };";
  if (!metin.includes(CAPA_OK2)) {
    return { durum: "CAPA_YOK", capa: "ok uc ciz", dosyaYol };
  }
  metin = metin.replace(CAPA_OK2, "return ciz([rot(0.5), tip, rot(-0.5)], { w: w * 0.9, renk, alfa, bas: o.bas + sure - 2, sure: 8, uc0: 6, uc1: 6, amp: 0.4, duz: true, oge: o.oge, ses, tur: \"isaret\", ad: (o.ad || \"ok\") + \":uc\" }); };");

  // 4. kutu
  const CAPA_KUTU = "bas: cur, sure: sr, uc0: 10, uc1: 12, oge: o.oge, ses: i === 0 ? true : false }); cur += sr; });";
  if (!metin.includes(CAPA_KUTU)) {
    return { durum: "CAPA_YOK", capa: "kutu ciz", dosyaYol };
  }
  metin = metin.replace(CAPA_KUTU, "bas: cur, sure: sr, uc0: 10, uc1: 12, oge: o.oge, ses: i === 0 ? true : false, tur: \"kart\", ad: o.ad || \"kutu\" }); cur += sr; });");

  // 5. tik
  const CAPA_TIK = "return ciz([[cx - 14, cy + 1], [cx - 4, cy + 12], [cx + 17, cy - 15]], { w: 7, renk: RT.vurgu, alfa: 0.9, bas: o.bas, sure: 9, uc0: 5, uc1: 8, amp: 0.3, ses: \"tik\", oge: o.oge });";
  if (!metin.includes(CAPA_TIK)) {
    return { durum: "CAPA_YOK", capa: "tik ciz", dosyaYol };
  }
  metin = metin.replace(CAPA_TIK, "return ciz([[cx - 14, cy + 1], [cx - 4, cy + 12], [cx + 17, cy - 15]], { w: 7, renk: RT.vurgu, alfa: 0.9, bas: o.bas, sure: 9, uc0: 5, uc1: 8, amp: 0.3, ses: \"tik\", oge: o.oge, tur: \"isaret\", ad: o.ad || \"tik\" });");

  // 6. yazi
  const CAPA_YAZI = "if (o.oge) o.oge.g.addChild(g);";
  if (!metin.includes(CAPA_YAZI)) {
    return { durum: "CAPA_YOK", capa: "yazi o.oge.g.addChild", dosyaYol };
  }
  metin = metin.replace(CAPA_YAZI, "g.data = { kalemTur: \"yazi\", kalemAd: str };\n    if (o.oge) { o.oge.g.addChild(g); o.oge.g.data = { kalemTur: \"yazi\", kalemAd: str }; }");

  // 7. paperTopla kancası
  const CAPA_KARE_BOLUM = "  // ---------- kare ----------";
  if (!metin.includes(CAPA_KARE_BOLUM)) {
    return { durum: "CAPA_YOK", capa: "// ---------- kare ----------", dosyaYol };
  }
  metin = metin.replace(CAPA_KARE_BOLUM, KANCA_PAPER_TOPLA + CAPA_KARE_BOLUM);

  // 8. kare(f) başı
  const CAPA_KARE_FONK = "  async function kare(f) {";
  if (!metin.includes(CAPA_KARE_FONK)) {
    return { durum: "CAPA_YOK", capa: "async function kare(f)", dosyaYol };
  }
  metin = metin.replace(CAPA_KARE_FONK, CAPA_KARE_FONK + "\n    if (typeof window !== \"undefined\" && window.__kalemKutu) {\n      window.__kalemKutu.kare = [];\n    }");

  // 9. c.yolP = cokgen(c, t); c.og.g.addChild(c.yolP); c.tam = t >= 1;
  const CAPA_YOLP = "c.yolP = cokgen(c, t); c.og.g.addChild(c.yolP); c.tam = t >= 1;";
  if (!metin.includes(CAPA_YOLP)) {
    return { durum: "CAPA_YOK", capa: "cokgen c.yolP", dosyaYol };
  }
  metin = metin.replace(CAPA_YOLP, "c.yolP = cokgen(c, t);\n      c.yolP.data = { kalemTur: c.tur, kalemAd: c.ad };\n      c.og.g.addChild(c.yolP); c.tam = t >= 1;");

  return { durum: "DEGISTI", icerik: metin };
}

export function kancaSahneOrtak(icerik, dosyaYol) {
  if (icerik.includes("__kalemKutu")) {
    return { durum: "VAR", icerik };
  }

  let metin = icerik;

  // 1. cumle
  const CAPA_CUMLE = `    return { x: a.x, w: Y.gen, Y, sure: Y.sure, ciz: (ctx, f) => {
      const t = mutlak ? this.zm(f) : (f - fb) / 30; if (t <= (mutlak ? a.sozcukler[0].t0 : 0)) return;
      yaziCiz(ctx, Y, t, 1);
    } };`;
  if (!metin.includes(CAPA_CUMLE)) {
    return { durum: "CAPA_YOK", capa: "cumle yaziCiz", dosyaYol };
  }
  const YENI_CUMLE = `    return { x: a.x, w: Y.gen, Y, sure: Y.sure, ciz: (ctx, f) => {
      const t = mutlak ? this.zm(f) : (f - fb) / 30; if (t <= (mutlak ? a.sozcukler[0].t0 : 0)) return;
      if (a.alfa == null || a.alfa >= 0.2) {
        window.__kalemKutu?.ekle("yazi", a.metin, a.x, a.y - boy * 0.9, Y.gen, boy * 1.1);
      }
      yaziCiz(ctx, Y, t, 1);
    } };`;
  metin = metin.replace(CAPA_CUMLE, YENI_CUMLE);

  // 2. gorsel
  const CAPA_GORSEL = `    g.ciz = (ctx, f) => {
      ctx.save();`;
  if (!metin.includes(CAPA_GORSEL)) {
    return { durum: "CAPA_YOK", capa: "gorsel g.ciz", dosyaYol };
  }
  const YENI_GORSEL = `    g.ciz = (ctx, f) => {
      if (f >= this.fr(a.tb) && (a.alfa == null || a.alfa >= 0.2)) {
        window.__kalemKutu?.ekle("cizim", a.ad || "cizim", a.kutu.x, a.kutu.y, a.kutu.w, a.kutu.h);
      }
      ctx.save();`;
  metin = metin.replace(CAPA_GORSEL, YENI_GORSEL);

  // 3. metinPop
  const CAPA_METIN_POP = `    return { x: x0, w: tw, y: a.y, fb, ciz: (ctx, f) => {
      const u = yavasla((f - fb) / n); if (u <= 0) return;
      ctx.save(); ctx.globalAlpha = u * (a.alfa == null ? 1 : a.alfa); ctx.font = a.font; ctx.textAlign = "left";`;
  if (!metin.includes(CAPA_METIN_POP)) {
    return { durum: "CAPA_YOK", capa: "metinPop ciz", dosyaYol };
  }
  const YENI_METIN_POP = `    return { x: x0, w: tw, y: a.y, fb, ciz: (ctx, f) => {
      const u = yavasla((f - fb) / n); if (u <= 0) return;
      const al = u * (a.alfa == null ? 1 : a.alfa);
      if (al >= 0.2) {
        window.__kalemKutu?.ekle("yazi", a.parca.map(([m]) => m).join(""), x0, a.y - boy * 0.9, tw, boy * 1.1);
      }
      ctx.save(); ctx.globalAlpha = al; ctx.font = a.font; ctx.textAlign = "left";`;
  metin = metin.replace(CAPA_METIN_POP, YENI_METIN_POP);

  // 4. metinDaktilo
  const CAPA_DAKTILO = `    return { x: a.x, w: tw, ciz: (ctx, f) => {
      const u = kis((f - fb) / n); if (u <= 0) return;
      ctx.save(); ctx.beginPath(); ctx.rect(a.x - 8, a.y - boy * 1.1, (tw + 16) * u, boy * 1.6); ctx.clip();`;
  if (!metin.includes(CAPA_DAKTILO)) {
    return { durum: "CAPA_YOK", capa: "metinDaktilo ciz", dosyaYol };
  }
  const YENI_DAKTILO = `    return { x: a.x, w: tw, ciz: (ctx, f) => {
      const u = kis((f - fb) / n); if (u <= 0) return;
      if (u >= 0.2) {
        window.__kalemKutu?.ekle("yazi", a.parca.map(([m]) => m).join(""), a.x, a.y - boy * 0.9, tw * u, boy * 1.1);
      }
      ctx.save(); ctx.beginPath(); ctx.rect(a.x - 8, a.y - boy * 1.1, (tw + 16) * u, boy * 1.6); ctx.clip();`;
  metin = metin.replace(CAPA_DAKTILO, YENI_DAKTILO);

  // 5. altCizgiPop (varsa uygula)
  const CAPA_ALT1 = `        const u = yavasla((T - kel[idx].t0) / 0.1);
        darbeCiz(ctx, kel[idx].alt, u, sol);`;
  if (metin.includes(CAPA_ALT1)) {
    const YENI_ALT1 = `        const u = yavasla((T - kel[idx].t0) / 0.1);
        if (sol >= 0.2) {
          const ak = kel[idx];
          window.__kalemKutu?.ekle("isaret", "altCizgi", ak.x - 4, ak.y + 10, ak.w + 8, 14);
        }
        darbeCiz(ctx, kel[idx].alt, u, sol);`;
    metin = metin.replace(CAPA_ALT1, YENI_ALT1);
  }

  const CAPA_ALT2 = `      for (const k of kel) {
        const u = kis((T - k.t0) / 0.12); if (u <= 0) continue;
        ctx.save(); ctx.globalAlpha = yavasla(u); ctx.beginPath();`;
  if (metin.includes(CAPA_ALT2)) {
    const YENI_ALT2 = `      for (const k of kel) {
        const u = kis((T - k.t0) / 0.12); if (u <= 0) continue;
        if (u >= 0.2) {
          window.__kalemKutu?.ekle("yazi", k.m, k.x, k.y - boy * 0.9, k.w, boy * 1.1);
        }
        ctx.save(); ctx.globalAlpha = yavasla(u); ctx.beginPath();`;
    metin = metin.replace(CAPA_ALT2, YENI_ALT2);
  }

  // 6. halka
  const CAPA_HALKA = `  halka(k, tb, sure = 0.35, tohum = 1, pay = 6) {
    const el = elips(k.x + k.w / 2, k.y - 22, k.w / 2 + pay, 52, -0.04 + 0.03 * hash(tohum, 3, 3), tohum);
    return this.darbe(el, { w: 6, renk: RT.vurgu, alfa: 0.85, uc0: 14, uc1: 30 }, tb, sure, 0.55);
  }`;
  if (!metin.includes(CAPA_HALKA)) {
    return { durum: "CAPA_YOK", capa: "halka", dosyaYol };
  }
  const YENI_HALKA = `  halka(k, tb, sure = 0.35, tohum = 1, pay = 6) {
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
  }`;
  metin = metin.replace(CAPA_HALKA, YENI_HALKA);

  // 7. kart
  const CAPA_KART = `  kart(a) {
    const o = [];
    this.darbeler(kutu(a.x, a.y, a.w, a.h, 90 + (a.tohum || 0)), { w: 3.6, renk: RT.ikincil, uc0: 10, uc1: 18 }, a.tb, a.kutuSure || 0.14,
      a.kutuAralik || 0.1, 0.55).forEach((e) => o.push(e));
    a.satirlar.forEach((s, i) => o.push(this.metinPop({ ...s, ses: i === 0 ? 0.5 : false })));
    return o;
  }`;
  if (!metin.includes(CAPA_KART)) {
    return { durum: "CAPA_YOK", capa: "kart", dosyaYol };
  }
  const YENI_KART = `  kart(a) {
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
  }`;
  metin = metin.replace(CAPA_KART, YENI_KART);

  // 8. kare(f, hepsi)
  const CAPA_KARE = `  async kare(f, hepsi) {
    const ctx = this.ctx;`;
  if (!metin.includes(CAPA_KARE)) {
    return { durum: "CAPA_YOK", capa: "async kare(f, hepsi)", dosyaYol };
  }
  const YENI_KARE = `  async kare(f, hepsi) {
    if (typeof window !== "undefined" && window.__kalemKutu) {
      window.__kalemKutu.kare = [];
    }
    const ctx = this.ctx;`;
  metin = metin.replace(CAPA_KARE, YENI_KARE);

  return { durum: "DEGISTI", icerik: metin };
}

// --- Ana İşleyici ---

export function dosyayiKancala(dosyaYol, icerik) {
  const ad = path.basename(dosyaYol);
  if (ad === "kalem-canvas.js") {
    return kancaKalemCanvas(icerik, dosyaYol);
  } else if (ad === "kunye.js") {
    return kancaKunye(icerik, dosyaYol);
  } else if (ad === "kalem-paper.js") {
    return kancaKalemPaper(icerik, dosyaYol);
  } else if (ad === "sahne-ortak.js") {
    return kancaSahneOrtak(icerik, dosyaYol);
  }
  return { durum: "BILINMEYEN_DOSYA", icerik };
}

export function paketDosyalariniBul(paketAdi) {
  const paketDizin = path.isAbsolute(paketAdi)
    ? paketAdi
    : (paketAdi.startsWith("projeler/") ? path.join(KOK, paketAdi) : path.join(KOK, "projeler", paketAdi));

  if (!fs.existsSync(paketDizin)) {
    return [];
  }

  const dosyalar = [];

  const canvasYol = path.join(paketDizin, "ortak", "kalem-canvas.js");
  if (fs.existsSync(canvasYol)) dosyalar.push(canvasYol);

  const kunyeYol = path.join(paketDizin, "ortak", "kunye.js");
  if (fs.existsSync(kunyeYol)) dosyalar.push(kunyeYol);

  const sahnelerDizin = path.join(paketDizin, "sahneler");
  if (fs.existsSync(sahnelerDizin)) {
    const altDizinler = fs.readdirSync(sahnelerDizin).sort();
    for (const alt of altDizinler) {
      const altTam = path.join(sahnelerDizin, alt);
      if (fs.statSync(altTam).isDirectory()) {
        const paperYol = path.join(altTam, "kalem-paper.js");
        if (fs.existsSync(paperYol)) dosyalar.push(paperYol);

        const ortakYol = path.join(altTam, "sahne-ortak.js");
        if (fs.existsSync(ortakYol)) dosyalar.push(ortakYol);
      }
    }
  }

  return dosyalar;
}

export function paketYedekle(paketAdi, dosyalar) {
  const pAd = path.basename(paketAdi);
  const yedekDizin = path.join(KOK, "_is", "cakisma", "dagit", pAd, "yedek");
  fs.mkdirSync(yedekDizin, { recursive: true });

  const paketKok = path.isAbsolute(paketAdi)
    ? paketAdi
    : (paketAdi.startsWith("projeler/") ? path.join(KOK, paketAdi) : path.join(KOK, "projeler", paketAdi));

  for (const d of dosyalar) {
    const rel = path.relative(paketKok, d);
    const hedef = path.join(yedekDizin, rel);
    fs.mkdirSync(path.dirname(hedef), { recursive: true });
    fs.copyFileSync(d, hedef);
  }
}

export function paketGeriYukle(paketAdi) {
  const pAd = path.basename(paketAdi);
  const yedekDizin = path.join(KOK, "_is", "cakisma", "dagit", pAd, "yedek");
  if (!fs.existsSync(yedekDizin)) {
    console.error(`Yedek bulunamadı: ${yedekDizin}`);
    return false;
  }

  const paketKok = path.isAbsolute(paketAdi)
    ? paketAdi
    : (paketAdi.startsWith("projeler/") ? path.join(KOK, paketAdi) : path.join(KOK, "projeler", paketAdi));

  function geriKopyala(dizin, relDizin = "") {
    const entries = fs.readdirSync(dizin, { withFileTypes: true });
    for (const e of entries) {
      const kaynak = path.join(dizin, e.name);
      const rel = path.join(relDizin, e.name);
      if (e.isDirectory()) {
        geriKopyala(kaynak, rel);
      } else {
        const hedef = path.join(paketKok, rel);
        fs.mkdirSync(path.dirname(hedef), { recursive: true });
        fs.copyFileSync(kaynak, hedef);
        console.log(`GERİ YAZILDI ${path.relative(KOK, hedef)}`);
      }
    }
  }

  geriKopyala(yedekDizin);
  return true;
}

// --- Komut Satırı Koşucusu ---

export async function ana() {
  const argv = process.argv.slice(2);
  const secenekler = { kuru: false, geri: false };
  const paketler = [];

  for (const arg of argv) {
    if (arg === "--kuru") {
      secenekler.kuru = true;
    } else if (arg === "--geri") {
      secenekler.geri = true;
    } else if (!arg.startsWith("--")) {
      paketler.push(arg);
    }
  }

  if (paketler.length === 0) {
    console.error("Kullanım: node araclar/kanca-dagit.mjs <paket...> [--kuru] [--geri]");
    process.exit(2);
  }

  let tumuBasarili = true;

  for (const paket of paketler) {
    const pAd = path.basename(paket);
    if (secenekler.geri) {
      const ok = paketGeriYukle(pAd);
      if (!ok) tumuBasarili = false;
      continue;
    }

    const dosyalar = paketDosyalariniBul(paket);
    if (dosyalar.length === 0) {
      console.warn(`UYARI: ${pAd} için motor dosyası bulunamadı.`);
      continue;
    }

    let paketCapaYok = false;
    let paketDegisen = false;
    let paketVar = true;
    const islemListesi = [];

    for (const dosya of dosyalar) {
      const relYol = path.relative(KOK, dosya);
      const icerik = fs.readFileSync(dosya, "utf8");
      const sonuc = dosyayiKancala(dosya, icerik);

      if (sonuc.durum === "VAR") {
        console.log(`VAR ${relYol}`);
      } else if (sonuc.durum === "DEGISTI") {
        paketVar = false;
        paketDegisen = true;
        islemListesi.push({ dosya, relYol, yeniIcerik: sonuc.icerik });
        if (secenekler.kuru) {
          console.log(`EKLENECEK ${relYol}`);
        } else {
          console.log(`EKLENDİ ${relYol}`);
        }
      } else if (sonuc.durum === "CAPA_YOK") {
        paketVar = false;
        paketCapaYok = true;
        tumuBasarili = false;
        console.log(`ÇAPA YOK ${relYol} ${sonuc.capa}`);
      }
    }

    // Gerçek koşu ve çapa yok hatası yoksa diske yaz
    if (!secenekler.kuru && !paketCapaYok && paketDegisen) {
      paketYedekle(pAd, dosyalar);
      for (const item of islemListesi) {
        fs.writeFileSync(item.dosya, item.yeniIcerik, "utf8");
      }
    }
  }

  if (!tumuBasarili) {
    process.exitCode = 1;
  }
}

// Doğrudan CLI ile çağrıldığında çalıştır
if (process.argv[1] && path.resolve(process.argv[1]) === path.resolve(new URL(import.meta.url).pathname)) {
  ana().catch((err) => {
    console.error("HATA:", err);
    process.exit(1);
  });
}
