from pydantic import BaseModel 
from datetime import datetime
from typing import Literal 

class DamageSchema(BaseModel):

    timestamp: datetime 
    attack_id: str 
    entity_id: str 
    result: Literal["destroyed", "damaged", "no_damage"] 
