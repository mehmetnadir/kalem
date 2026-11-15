"""simple-present-temel-s3 sahne 07 kapak C (kural + karşıt çift) olaylar.json: ses yok (durağan kare, anlatımdan bağımsız) -> boş liste."""
import json
from pathlib import Path

AD = Path(__file__).resolve().parent
(AD / "olaylar.json").write_text(json.dumps([], ensure_ascii=False))
print("olay 0")
