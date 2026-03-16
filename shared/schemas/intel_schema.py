from typing import Literal, Annotated
from typing_extensions import Self
from pydantic import BaseModel, model_validator, Field 
from datetime import datetime
from shared.models import target_bank 
from shared.utils import haversine_km


class IntelSchema(BaseModel):
    timestamp: datetime
    signal_id: str
    entity_id: str
    reported_lat: float
    reported_lon: float
    signal_type: Literal["SIGINT", "VISINT", "HUMINT"]
    priority_level: Annotated[int, Literal[1,2,3,4,5,99]] 
    distance: Annotated[float, Field(default=0, ge=0)]

    @model_validator(mode='after')
    def check_target_bank(self) -> Self:
        """validate if """
        for i in target_bank:
            if i["entity_id"] == self.entity_id:
                self.distance = haversine_km(i["lat"], i["lon"], self.reported_lat, self.reported_lon)
                return self
        self.priority_level = 99 
        return self 
    



    


