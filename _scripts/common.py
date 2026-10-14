from __future__ import annotations

import hashlib
import json
import re
from dataclasses import dataclass
from datetime import date, datetime, timezone
from email.utils import parsedate_to_datetime
from pathlib import Path
from typing import Any

import yaml


ROOT = Path(__file__).resolve().parents[1]


def slugify(value: str) -> str:
    text = value.strip().lower()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    text = re.sub(r"-+", "-", text).strip("-")
    return text or "untitled"


def normalize_text(value: str) -> str:
    text = re.sub(r"[^a-z0-9]+", " ", value.strip().lower())
    return re.sub(r"\s+", " ", text).strip()


def short_hash(value: str, length: int = 6) -> str:
    return hashlib.sha256(normalize_text(value).encode("utf-8")).hexdigest()[:length]


def release_id_for(product: str, release_date: str, identity: str) -> str:
    readable = slugify(identity)[:64].strip("-") or "release"
    return (
        f"{slugify(product)}-{release_date}-{readable}-"
        f"{short_hash(identity, length=8)}"
    )


def card_id_for(
    product: str,
    release_date: str,
    quote: str,
    source_release: str | None = None,
) -> str:
    identity = f"{source_release}\n{quote}" if source_release else quote
    return f"{slugify(product)}-{release_date}-{short_hash(identity)}"


def read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def read_yaml(path: Path) -> Any:
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def write_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def parse_date(value: str) -> date:
    try:
        return datetime.fromisoformat(value.replace("Z", "+00:00")).date()
    except ValueError:
        return parsedate_to_datetime(value).date()


def utc_timestamp() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def machine_hash(machine_fields: dict[str, Any], regions: dict[str, str]) -> str:
    fields = {key: value for key, value in machine_fields.items() if key != "machine_hash"}
    payload = {"fields": fields, "regions": regions}
    encoded = json.dumps(payload, sort_keys=True, ensure_ascii=False, separators=(",", ":"))
    return hashlib.sha256(encoded.encode("utf-8")).hexdigest()


@dataclass(frozen=True)
class PipelinePaths:
    run_id: str
    root: Path = ROOT

    def __post_init__(self) -> None:
        if not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9._-]*", self.run_id):
            raise ValueError("run-id must be a single alphanumeric path component")

    @property
    def run_dir(self) -> Path:
        return self.root / "_pipeline" / self.run_id

    @property
    def collected(self) -> Path:
        return self.run_dir / "01-collected" / "releases.json"

    @property
    def extracted(self) -> Path:
        return self.run_dir / "02-extracted" / "change_cards.json"

    @property
    def valid_cards(self) -> Path:
        return self.run_dir / "02-extracted" / "valid_change_cards.json"

    @property
    def theme_candidates(self) -> Path:
        return self.run_dir / "02-extracted" / "theme_candidates.json"

    @property
    def analyze_a(self) -> Path:
        return self.run_dir / "03a-analyzed-per" / "analysis.json"

    @property
    def analyze_b(self) -> Path:
        return self.run_dir / "03b-analyzed-cross" / "analysis.json"

    @property
    def silence(self) -> Path:
        return self.run_dir / "03c-silence" / "alerts.json"

    @property
    def validation_round2(self) -> Path:
        return self.run_dir / "04-validated" / "report.json"

    @property
    def dlq(self) -> Path:
        return self.root / "_pipeline" / "dlq" / f"{self.run_id}-failed.json"
