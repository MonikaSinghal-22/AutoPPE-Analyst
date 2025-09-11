from typing import List
from pydantic import BaseModel, Field
from datetime import datetime


class LogEntry(BaseModel):
    timestamp: datetime = Field(
        ..., description="Time of the event in ISO 8601 format"
    )
    worker_id: str = Field(
        ..., description="Unique worker identifier"
    )
    ppe_item: str = Field(
        ..., description="PPE item involved (Helmet, Gloves, Goggles, etc.)"
    )
    status: str = Field(
        ..., description="Compliance status (Compliant / Non-Compliant)"
    )
    severity: str = Field(
        ..., description="Risk severity (Low / Medium / High)"
    )
    location: str = Field(
        ..., description="Location where the event occurred"
    )


class PreparedLog(BaseModel):
    source_file: str = Field(
        ..., description="Name or path of the processed file"
    )
    total_entries: int = Field(
        ..., description="Number of entries extracted"
    )
    cleaned_entries: List[LogEntry] = Field(
        ..., description="List of cleaned and validated log entries"
    )
    cleaning_notes: str = Field(
        ..., description="Description of what was cleaned/standardized"
    )
