from pydantic import BaseModel


class ISSPosition(BaseModel):
    timestamp: int
    latitude: float
    longitude: float