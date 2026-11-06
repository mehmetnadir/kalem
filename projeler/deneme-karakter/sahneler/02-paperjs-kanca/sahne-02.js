// Sahne 02 — Kadro karakteri model sayfası (432 kare, t_bas 3,00; anlatımdan bağımsız).
// 4 satır × 8 duygu: satır başına ≈ 2,7 sn kalemle çizim; son 2,5 sn tam sayfa durur.
// Yerel kare = round((t − 3,00) × 30).
import { sahneKur,
  RT } from "/projeler/deneme-karakter/sahneler/02-paperjs-kanca/kalem-paper.js";
import { karakter } from "/projeler/deneme-karakter/sahneler/02-paperjs-kanca/karakter.js";

export const KARE = 432, T_BAS = 3.0;

const DUYGULAR = ["notr", "dikkat", "dusunme", "saskin", "kararsiz", "yanlis", "dogru", "sevinc"];
const BASLIK = ["nötr", "dikkat", "düşünme", "şaşkın", "kararsız", "yanlış", "doğru", "sevinç"];
const KOLON0 = 385, ADIM = 190, H = 28;          // hücre ≈ 190×205 px; baş yüksekliği h = 28 px
const SATIRLAR = [                                // zemin y (ayak tabanı), başlık, kimlik, yaş
  { y: 300, ad: "kız 10–11 yaş", kimlik: "ogrenci_kiz", yas: 10 },
  { y: 505, ad: "kız 14–15 yaş", kimlik: "ogrenci_kiz", yas: 14 },
  { y: 720, ad: "kız 16–18 yaş", kimlik: "ogrenci_kiz", yas: 17 },
  { y: 945, ad: "erkek / öğretmen", kimlik: "ogrenci_erkek", yas: 14, ogretmen: 4 }];
const SATIR0 = 24, SATIR_ADIM = 80, FIGUR_SURE = 66, FIGUR_ARA = 2;

export async function kur(P) {
  const S = await sahneKur(P, { KARE, tBas: T_BAS, bolum: "Model", etkin: 0 });
  const { ciz, elYazisi, genislik, not } = S;
  const kx = (i) => KOLON0 + i * ADIM;

  // sütun başlıkları: el yazısı, Caveat boy 44, hücre ortasında
  BASLIK.forEach((b, i) => {
    const w = genislik(b, "700 44px Caveat");
    elYazisi(b, { x: kx(i) - w / 2, y: 138, boyut: 44, bas: 2 + i * 3, sure: 22 });
  });
  not("sütun başlıkları", 2);

  SATIRLAR.forEach((s, r) => {
    const b0 = SATIR0 + r * SATIR_ADIM;
    elYazisi(s.ad, { x: 50, y: s.y - 70, boyut: 36, bas: b0, sure: 22 });
    DUYGULAR.forEach((d, i) => {
      const ogr = s.ogretmen != null && i >= s.ogretmen;
      karakter(S, { x: kx(i), y: s.y, yas: s.yas, duygu: d, h: H, poz: "ayakta",
        kimlik: ogr ? "ogretmen" : s.kimlik, bas: b0 + i * FIGUR_ARA, sure: FIGUR_SURE });
    });
    if (s.ogretmen != null) {                      // erkek | öğretmen ayracı
      const x = (kx(s.ogretmen - 1) + kx(s.ogretmen)) / 2;
      ciz([[x, s.y - 210], [x, s.y]], { w: 2.4, renk: RT.ikincil, alfa: 0.7, bas: b0,
        sure: 24, duz: true, ses: false });
    }
    not("satır " + (r + 1) + " başı", b0);
  });
  return S;
}
