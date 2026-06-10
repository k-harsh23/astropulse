import json
from pathlib import Path
from datetime import datetime


def save_json(data: dict, directory: Path, prefix: str) -> Path:
    """
    Save JSON payload to disk with timestamp.
    """

    directory.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.utcnow().strftime("%Y%m%d_%H%M%S")

    file_path = directory / f"{prefix}_{timestamp}.json"

    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)

    return file_path