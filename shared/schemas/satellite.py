from pydantic import BaseModel
from typing import Optional


class Satellite(BaseModel):
    satellite_id: str
    satellite_name: str
    operator: Optional[str] = None
    orbit_type: Optional[str] = None
    country: Optional[str] = None