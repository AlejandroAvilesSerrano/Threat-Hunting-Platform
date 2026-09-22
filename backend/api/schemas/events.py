from datetime import datetime
from typing import Any

from pydantic import BaseModel, Field

""" Event Input Example
{
  "event_type": "alert",
  "timestamp": "2026-09-22T10:30:00Z",
  "src_ip": "192.168.1.20",
  "src_port": 51512,
  "dest_ip": "8.8.8.8",
  "dest_port": 53,
  "protocol": "UDP",
  "severity": 2,
  "signature": "ET DNS Suspicious Query",
  "raw_event": {
    "event_type": "alert",
    "alert": {
      "signature": "ET DNS Suspicious Query"
    }
  }
}
"""

class EventCreate(BaseModel):
    source: str = Field(..., examples=["suricata", "zeek", "sysmon"])
    event_type: str = Field(..., examples=["alert", "dns", "connection"])
    timestamp: datetime

    src_ip: str | None = None
    src_port: int | None = None
    dest_ip: str | None = None
    dest_port: int | None = None
    protocol: str | None = None

    severity: int | None = None
    signature: str | None = None

    raw_event: dict[str, Any]

class EventResponse(EventCreate):
    id: str