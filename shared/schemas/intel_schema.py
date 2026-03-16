from typing import Literal, Annotated
from pydantic import BaseModel, Field  
from datetime import datetime


class IntelSchema(BaseModel):
    timestamp: datetime
    signal_id: str
    entity_id: str
    reported_lat: float
    reported_lon: float
    signal_type: Literal["SIGINT", "VISINT", "HUMINT"]
    priority_level: Annotated[int, Literal[1,2,3,4,5,99]]

