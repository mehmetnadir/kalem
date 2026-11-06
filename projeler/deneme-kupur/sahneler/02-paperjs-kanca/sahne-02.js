// Sahne 02 — Kâğıt küpür kadro (492 kare, t_bas 3,00; anlatımdan bağımsız, ≈ 16 sn).
// Satır 1: 12 üye ayakta · satır 2: tek üye × 8 duygu · satır 3: aynı üye 4 yaş bandı + öğretmen.
// Son 64 kare (≈ 2 sn) tam sayfa durur. Yerel kare = round((t − 3,00) × 30).
import { sahneKur,
  RT } from "/projeler/deneme-kupur/sahneler/02-paperjs-kanca/kalem-paper.js";
import { kupur, kadro } from "/projeler/deneme-kupur/sahneler/02-paperjs-kanca/kupur.js";

export const KARE = 492, T_BAS = 3.0;

const DUYGULAR = ["notr", "dikkat", "dusunme", "saskin", "kararsiz", "yanlis", "dogru", "sevinc"];
const BASLIK = ["nötr", "dikkat", "düşünme", "şaşkın", "kararsız", "yanlış", "doğru", "sevinç"];
const YAS = [{ yas: 11, ad: "10–11 yaş" }, { yas: 13, ad: "12–13 yaş" },
  { yas: 15, ad: "14–15 yaş" }, { yas: 17, ad: "16–18 yaş" }];
const TOHUM = 7;

export async function kur(P) {
  const S = await sahneKur(P, { KARE, tBas: T_BAS, bolum: "Hook", etkin: 0 });
  const { elYazisi, genislik, not } = S;
  const K = kadro(12, TOHUM), UYE = K[4];
  const OGRT = { ...K[1], ogretmen: true, sac: 5, aks: 0, etek: false, ten: 1, ust: 4, alt: 1,
    sacRenk: 0 };
  const etiket = (m, x, y, bas, boyut = 30, orta = true) => {
    const w = genislik(m, `700 ${boyut}px Caveat`);
    return elYazisi(m, { x: orta ? x - w / 2 : x, y, boyut, bas, sure: 18 });
  };

  // satır 1: 12 üye, nötr, h = 42 px
  etiket("12 kişilik kadro", 50, 295, 2, 36, false);
  K.forEach((kim, i) => kupur(S, { x: 360 + i * (1480 / 11), y: 395, h: 42, kimlik: kim,
    yas: kim.yas, duygu: "notr", bas: 8 + i * 9, sure: 40 }));
  not("satır 1 başı", 8);

  // satır 2: tek üye × 8 duygu, h = 38 px
  etiket("tek üye, 8 duygu", 50, 540, 160, 36, false);
  DUYGULAR.forEach((d, i) => {
    const x = 360 + i * (1480 / 7), b = 164 + i * 11;
    kupur(S, { x, y: 640, h: 38, kimlik: UYE, yas: 13, duygu: d, bas: b, sure: 36 });
    etiket(BASLIK[i], x, 678, b + 32);
  });
  not("satır 2 başı", 164);

  // satır 3: aynı üye 4 yaş bandı + öğretmen, h = 35 px
  etiket("4 yaş, öğretmen", 50, 860, 288, 36, false);
  YAS.concat([{ ad: "öğretmen" }]).forEach((a, i) => {
    const x = 420 + i * 350, b = 292 + i * 20;
    kupur(S, { x, y: 960, h: 35, kimlik: a.yas ? UYE : OGRT, yas: a.yas, duygu: "notr", bas: b,
      sure: 44 });
    etiket(a.ad, x, 996, b + 40);
  });
  not("satır 3 başı", 292);
  return S;
}
