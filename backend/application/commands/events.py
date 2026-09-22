from dataclasses import dataclass
from datetime import datetime
from typing import Any


@dataclass(frozen=True)
class IngestEventCommand:
    source: str
    event_type: str
    timestamp: datetime
    raw_event: dict[str, Any]
    src_ip: str | None = None
    src_port: int | None = None
    dest_ip: str | None = None
    dest_port: int | None = None
    protocol: str | None = None
    severity: int | None = None
    signature: str | None = None