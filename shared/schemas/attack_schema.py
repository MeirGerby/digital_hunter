from pydantic import BaseModel 
from datetime import datetime
from typing import Literal 

class AttackSchema(BaseModel):
    timestamp: datetime
    attack_id: str 
    entity_id: str 
    weapon_type: Literal[
        "AGM-114 Hellfire",
        "GBU-39 SDB",
        "Delilah Missile",
        "SPICE-250",
        "Popeye AGM",
        "Griffin LGM",
    ]
    
