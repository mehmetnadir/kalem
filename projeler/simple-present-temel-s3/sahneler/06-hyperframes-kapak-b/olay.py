"""simple-present-temel-s3 sahne 06 kapak B (soru) olaylar.json: ses yok (durağan kare, anlatımdan bağımsız) -> boş liste."""
import json
from pathlib import Path

AD = Path(__file__).resolve().parent
(AD / "olaylar.json").write_text(json.dumps([], ensure_ascii=False))
print("olay 0")
