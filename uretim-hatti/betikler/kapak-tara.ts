// Salt okur: paketi yazılı her sürüm satırı için ders sayfasının kapak çözümünü (önizleme deposu → ayna yedeği) koşar.
// Koşu: cd /var/www/videokayit && node --env-file=.env --import tsx <bu dosya>
import { prisma } from "@/lib/db";
import { aynaKokYolu, kapakYedegi } from "@/lib/kontrol/ayna-okuma";
import { onizlemeAdresleri } from "@/lib/kontrol/onizleme-sunucu";

async function ana(): Promise<void> {
  const kok = aynaKokYolu();
  const satirlar = await prisma.kontrolSurum.findMany({
    where: { paket: { not: null } },
    select: { ad: true, tur: true, paket: true, oge: { select: { kimlik: true } } },
    orderBy: [{ oge: { kimlik: "asc" } }, { tur: "asc" }],
  });
  let var_ = 0;
  const yok: string[] = [];
  const kaynak = { onizleme: 0, ayna: 0 };
  for (const s of satirlar) {
    const paket = s.paket as string;
    const depo = (await onizlemeAdresleri(paket, "acik")).kapak;
    const adres = depo ?? (await kapakYedegi(kok, paket, "acik"));
    if (adres) {
      var_ += 1;
      kaynak[depo ? "onizleme" : "ayna"] += 1;
    } else {
      yok.push(`${s.oge.kimlik} · ${s.tur} · ${paket}`);
    }
  }
  console.log(`satır ${satirlar.length} · kapak var ${var_} (önizleme ${kaynak.onizleme}, ayna ${kaynak.ayna}) · yok ${yok.length}`);
  for (const y of yok) console.log(`  YOK ${y}`);
  await prisma.$disconnect();
}

ana().catch((e: unknown) => {
  console.error(e instanceof Error ? e.message : e);
  process.exit(1);
});
