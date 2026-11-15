// Salt okur: KontrolSurum.paket doluluk özeti + verilen öğelerin sürüm satırları (15.11 doğrulama).
// Koşu: cd /var/www/videokayit && node --env-file=.env --import tsx <bu dosya> <kimlik>…
import { prisma } from "@/lib/db";

async function ana(): Promise<void> {
  const kimlikler = process.argv.slice(2);
  const toplam = await prisma.kontrolSurum.count();
  const dolu = await prisma.kontrolSurum.count({ where: { paket: { not: null } } });
  console.log(`surum ${toplam} · paket dolu ${dolu}`);
  for (const kimlik of kimlikler) {
    const oge = await prisma.kontrolOge.findUnique({
      where: { kimlik },
      select: { paket: true, surumler: { select: { ad: true, tur: true, durum: true, paket: true } } },
    });
    if (!oge) {
      console.log(`${kimlik}: yok`);
      continue;
    }
    console.log(`${kimlik} (oge.paket ${oge.paket ?? "-"})`);
    for (const s of oge.surumler) console.log(`  ${s.tur} · ${s.ad} · ${s.durum ?? "-"} · ${s.paket ?? "-"}`);
  }
  await prisma.$disconnect();
}

ana().catch((e: unknown) => {
  console.error(e instanceof Error ? e.message : e);
  process.exit(1);
});
