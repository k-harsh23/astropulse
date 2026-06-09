from pathlib import Path
from dotenv import load_dotenv
import os

BASE_DIR = Path(__file__).resolve().parents[2]

load_dotenv()

class Settings:
    APP_NAME = "AstroPulse"

    RAW_DATA_DIR = BASE_DIR / "data" / "raw"
    SNAPSHOT_DIR = BASE_DIR / "data" / "snapshots"
    EXPORT_DIR = BASE_DIR / "data" / "exports"

    NASA_API_KEY = os.getenv("NASA_API_KEY", "DEMO_KEY")

settings = Settings()