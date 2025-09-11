from pydantic import BaseModel, Field
from typing import List


class ReportSummary(BaseModel):
    title: str = Field(
        ...,
        description="Title of the report"
    )
    executive_summary: str = Field(
        ...,
        description="Concise summary for stakeholders"
    )
    key_findings: List[str] = Field(
        ...,
        description="Bullet points of main findings"
    )
    recommendations: List[str] = Field(
        ...,
        description="Actionable suggestions based on analysis"
    )
    visualizations: List[str] = Field(
        default_factory=list,
        description=(
            "Optional list of paths/URLs to generated charts or figures"
        )
    )
    approval_status: str = Field(
        default="Pending",
        description="Final approval status by human supervisor"
    )
