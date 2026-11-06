// Sahne 02 — Zaman hattı (metro hattı), deneme 7. 600 kare = 20 sn, t_bas 3,00; anlatımsız.
// Zamanlar yerel sn → kare: k(s) = round(s × 30). Kalem modeli ve kamera yok; sayfa sonunda durur.
import { sahneKur, RT } from "/projeler/deneme-metro/sahneler/02-paperjs-kanca/kalem-paper.js";
import { zamanHatti, aralik, baslangic, tren }
  from "/projeler/deneme-metro/sahneler/02-paperjs-kanca/zamanhatti.js";

export const KARE = 600, T_BAS = 3.0;
const k = (s) => Math.round(s * 30);

export async function kur(P) {
  const S = await sahneKur(P, { KARE, tBas: T_BAS, bolum: "Hook", etkin: 0, kayma: 0 });
  const { elYazisi, oge, not } = S;
  const kis = S.kis;
  const sil1 = { bas: k(11.0), sure: 14 };                  // cümle 1'in işaretleri solar
  const solar = (sil) => (f) => 1 - kis((f - sil.bas) / sil.sure);

  // cümle 1 (üstte, el yazısı Caveat 56); 11. sn'de solar
  elYazisi("I have lived here since 2015.", { x: 160, y: 240, boyut: 56, renk: RT.murekkep,
    bas: k(0.2), sure: 66, oge: oge({ alfa: solar(sil1) }) });
  not("cümle 1", k(0.2));

  // hat: 4 durak; 2015 · 2020 geçmiş, now şimdi, ? gelecek (kesik)
  const hat = zamanHatti(S, { x: 160, y: 600, w: 1600, t0: 2013, t1: 2031, bas: k(1.0), sure: 70,
    duraklar: [
      { ad: "2015", t: 2015, tur: "gecmis" },
      { ad: "2020", t: 2020, tur: "gecmis" },
      { ad: "now", t: 2025, tur: "simdi" },
      { ad: "?", t: 2029, tur: "gelecek" },
    ] });

  baslangic(hat, "2015", { etiket: "since 2015", bas: k(3.4), sil: sil1 });
  aralik(hat, "2015", "now", { etiket: "for 10 years", bas: k(5.0), sil: sil1 });
  tren(hat, "2015", "now", { bas: k(7.0), sure: 54 });

  // cümle 2: aynı hat; durak 2022 sonradan çıkar, hat yeniden çizilmez
  elYazisi("She has worked there for 3 years.", { x: 160, y: 240, boyut: 56, renk: RT.murekkep,
    bas: k(11.6), sure: 66 });
  not("cümle 2", k(11.6));
  const d22 = hat.durakEkle({ ad: "2022", t: 2022, tur: "gecmis", bas: k(13.6) });
  aralik(hat, d22, "now", { etiket: "for 3 years", bas: k(14.4) });
  tren(hat, d22, "now", { bas: k(16.2), sure: 40 });
  return S;
}
