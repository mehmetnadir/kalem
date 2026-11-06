// Sahne 02 — Kadro karakteri üretim sürümü (492 kare = 16 sn, t_bas 3,00; anlatımdan bağımsız).
// 3 satır: kız 10–11 × 8 duygu · erkek 14–15 × 8 duygu · öğretmen × 4 duygu + 2 oturur figür.
// Her satır ≈ 139 kare (figür 62 kare, figürler arası 11 kare); son ≈ 2,8 sn tam sayfa durur.
// Yerel kare = round((t − 3,00) × 30).
import { sahneKur,
  RT } from "/projeler/deneme-karakter/sahneler/02-paperjs-kanca/kalem-paper.js";
import { karakter } from "/projeler/deneme-karakter/sahneler/02-paperjs-kanca/karakter.js";

export const KARE = 492, T_BAS = 3.0;

const DUYGULAR = ["notr", "dikkat", "dusunme", "saskin", "kararsiz", "yanlis", "dogru", "sevinc"];
const BASLIK = ["nötr", "dikkat", "düşünme", "şaşkın", "kararsız", "yanlış", "doğru", "sevinç"];
const KOLON0 = 190, ADIM = 222, H = 56;          // sütun aralığı 222 px; baş yüksekliği h = 56 px
const SATIR0 = 6, SATIR_ADIM = 140, FIGUR_SURE = 62, FIGUR_ARA = 11;
// y: ayak tabanı (px) · bas: başlık taban çizgisi
const SATIRLAR = [
  { y: 402, bas: 200, ad: "kız 10–11 yaş", kimlik: "ogrenci_kiz", yas: 10, duygu: DUYGULAR },
  { y: 664, bas: 452, ad: "erkek 14–15 yaş", kimlik: "ogrenci_erkek", yas: 14, duygu: DUYGULAR },
  { y: 941, bas: 712, ad: "öğretmen", kimlik: "ogretmen", yas: 30, duygu: DUYGULAR.slice(0, 4) }];
const OTURUR = [{ kol: 5.4, kimlik: "ogrenci_kiz", yas: 12, duygu: "dusunme" },
  { kol: 6.9, kimlik: "ogrenci_erkek", yas: 13, duygu: "dogru" }];

export async function kur(P) {
  const S = await sahneKur(P, { KARE, tBas: T_BAS, bolum: "Model", etkin: 0 });
  const { elYazisi, genislik, not } = S;
  const kx = (i) => KOLON0 + i * ADIM;

  // sütun başlıkları: el yazısı, Caveat boy 40, hücre ortasında
  BASLIK.forEach((b, i) => {
    const w = genislik(b, "700 40px Caveat");
    elYazisi(b, { x: kx(i) - w / 2, y: 150, boyut: 40, bas: 2 + i * 3, sure: 22 });
  });
  not("sütun başlıkları", 2);

  SATIRLAR.forEach((s, r) => {
    const b0 = SATIR0 + r * SATIR_ADIM;
    elYazisi(s.ad, { x: 50, y: s.bas, boyut: 36, bas: b0, sure: 22 });
    s.duygu.forEach((d, i) => {
      karakter(S, { x: kx(i), y: s.y, yas: s.yas, duygu: d, h: H, poz: "ayakta",
        kimlik: s.kimlik, bas: b0 + i * FIGUR_ARA, sure: FIGUR_SURE });
    });
    if (s.kimlik === "ogretmen") {                 // oturur figürler: satır 3'ün sağ yarısı
      elYazisi("oturur 12–13 yaş", { x: kx(OTURUR[0].kol) - 100, y: s.bas, boyut: 36,
        bas: b0 + 4 * FIGUR_ARA, sure: 22 });
      OTURUR.forEach((q, j) => {
        karakter(S, { x: kx(q.kol), y: s.y, yas: q.yas, duygu: q.duygu, h: H, poz: "oturur",
          kimlik: q.kimlik, bas: b0 + (4 + j) * FIGUR_ARA, sure: FIGUR_SURE + 6 });
      });
    }
    not("satır " + (r + 1) + " başı", b0);
  });
  return S;
}
