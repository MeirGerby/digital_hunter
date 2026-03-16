from pydantic import BaseModel 
from datetime import datetime


class IntelSchema(BaseModel):
    timestamp: datetime
    signal_id: str
    entity_id: str
    reported_lat: float
    reported_lon: float
    signal_type: str
    priority_level: int 

