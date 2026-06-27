#!/usr/bin/env python3
"""Stub for screenshot time recognition. Replace with OCR/AI agent later."""
from __future__ import annotations
import json
from datetime import datetime
from pathlib import Path

DATA = Path(__file__).resolve().parents[1] / "data" / "records"
DATA.mkdir(parents=True, exist_ok=True)
record = {
    "created_at": datetime.utcnow().isoformat() + "Z",
    "source": "manual_stub",
    "recognized_time": None,
    "confidence": 0.0,
    "needs_review": True,
}
with (DATA / "worklog.jsonl").open("a", encoding="utf-8") as f:
    f.write(json.dumps(record, ensure_ascii=False) + "\n")
print("Saved stub worklog record")
