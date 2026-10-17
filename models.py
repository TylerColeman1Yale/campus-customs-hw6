from typing import Literal
from pydantic import BaseModel, Field


class VendorDecision(BaseModel):
    vendor: str
    sku: str
    unit_price: float | None = None
    lead_time_days: int | None = None
    min_order: int | None = None
    decision: Literal['recommend', 'do_not_recommend']
    reason: str = Field(description='Exactly one concise sentence explaining the decision.')
