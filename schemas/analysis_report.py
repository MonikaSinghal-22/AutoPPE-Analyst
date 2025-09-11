from pydantic import BaseModel, Field
from typing import Dict, List


class RiskFlag(BaseModel):
    worker_id: str = Field(
        ..., description="Worker flagged for repeated non-compliance"
    )
    issue: str = Field(
        ..., description="Nature of the risk (e.g., Helmet non-compliance)"
    )
    count: int = Field(
        ..., description="Number of occurrences"
    )
    severity: str = Field(
        ..., description="Aggregated severity level"
    )


class AnalysisReport(BaseModel):
    compliance_rate: float = Field(
        ..., description="Overall compliance percentage across all entries"
    )
    non_compliance_counts: Dict[str, int] = Field(
        ..., description="Number of non-compliant events by PPE item"
    )
    high_risk_workers: List[RiskFlag] = Field(
        ..., description="Workers repeatedly non-compliant"
    )
    time_trends: Dict[str, float] = Field(
        ..., description="Compliance trend over time, keyed by date or period"
    )
    notes: str = Field(
        ..., description="Additional context or observations"
    )
