from pydantic import BaseModel
from typing import Optional


class Launch(BaseModel):
    launch_id: str
    mission_name: str
    rocket_name: Optional[str] = None
    agency: Optional[str] = None
    launch_status: Optional[str] = None
    launch_date: Optional[str] = None