from typing import Literal
from pydantic import BaseModel, Field  
from datetime import datetime


class IntelSchema(BaseModel):
    timestamp: datetime
    signal_id: str
    entity_id: str
    reported_lat: float
    reported_lon: float
    signal_type: Literal["SIGINT", "VISINT", "HUMINT"]
    priority_level: int = Field(..., ge=1, le=5)

