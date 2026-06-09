from pydantic import BaseModel
from typing import Optional


class NearEarthObject(BaseModel):
    asteroid_id: str
    asteroid_name: str
    hazardous: bool = False
    velocity_kph: Optional[float] = None
    miss_distance_km: Optional[float] = None