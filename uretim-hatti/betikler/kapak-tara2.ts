// Salt okur: paketi yazılı her yatay/dikey/kısa sürüm satırı için ders sayfasının kapak çözümünü (kapakCoz) iki temada koşar.
// Koşu: cd /var/www/videokayit && node --env-file=.env --import tsx <bu dosya> [öğe kimliği…]
import { prisma } from "@/lib/db";
import { aynaKokYolu } from "@/lib/kontrol/ayna-okuma";
import { kapakCoz } from "@/lib/kontrol/kapak-coz";

async function ana(): Promise<void> {
  const ayrinti = new Set(process.argv.slice(2));
  const kok = aynaKokYolu();
  const satirlar = await prisma.kontrolSurum.findMany({
    where: { paket: { not: null } },
    select: { tur: true, paket: true, oge: { select: { kimlik: true } } },
    orderBy: [{ oge: { kimlik: "asc" } }, { tur: "asc" }],
  });
  const say = { acik: 0, koyu: 0, tasarlanmis: 0 };
  const yok: string[] = [];
  for (const s of satirlar) {
    const paket = s.paket as string;
    const kisa = s.tur === "kisa";
    const acik = await kapakCoz(kok, paket, "acik", { kisa });
    const koyu = kisa ? acik : await kapakCoz(kok, paket, "koyu", { kisa });
    if (acik) say.acik += 1;
    if (koyu) say.koyu += 1;
    if (acik && /\/kapak\.png/.test(acik)) say.tasarlanmis += 1;
    if (!acik || !koyu) yok.push(`${s.oge.kimlik} · ${s.tur} · ${paket} · açık ${acik ? "var" : "YOK"} · koyu ${koyu ? "var" : "YOK"}`);
    if (ayrinti.has(s.oge.kimlik)) console.log(`${s.oge.kimlik} · ${s.tur} · açık ${acik ?? "-"} · koyu ${koyu ?? "-"}`);
  }
  console.log(`satır ${satirlar.length} · açık kapak ${say.acik} · koyu kapak ${say.koyu} · tasarlanmış (açık) ${say.tasarlanmis} · eksik ${yok.length}`);
  for (const y of yok) console.log(`  ${y}`);
  await prisma.$disconnect();
}

ana().catch((e: unknown) => {
  console.error(e instanceof Error ? e.message : e);
  process.exit(1);
});
