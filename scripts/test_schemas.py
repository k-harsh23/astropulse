
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from shared.schemas.launch import Launch

launch = Launch(
    launch_id="123",
    mission_name="Starlink Mission",
    rocket_name="Falcon 9",
)

print(launch)