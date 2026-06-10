from pathlib import Path
from dotenv import load_dotenv
import os

# ==========================================================
# Project Root
# ==========================================================

BASE_DIR = Path(__file__).resolve().parents[2]

load_dotenv()


class Settings:
    """
    Centralized application settings.
    """

    APP_NAME = "AstroPulse"

    # ======================================================
    # Data Directories
    # ======================================================

    DATA_DIR = BASE_DIR / "data"

    RAW_DATA_DIR = DATA_DIR / "raw"
    SNAPSHOT_DIR = DATA_DIR / "snapshots"
    EXPORT_DIR = DATA_DIR / "exports"

    # ======================================================
    # Raw Data Domains
    # ======================================================

    RAW_LAUNCH_DIR = RAW_DATA_DIR / "launches"
    RAW_SATELLITE_DIR = RAW_DATA_DIR / "satellites"
    RAW_NEO_DIR = RAW_DATA_DIR / "neo"
    RAW_ISS_DIR = RAW_DATA_DIR / "iss"

    # ======================================================
    # Snapshot Domains
    # ======================================================

    SNAPSHOT_LAUNCH_DIR = SNAPSHOT_DIR / "launches"
    SNAPSHOT_SATELLITE_DIR = SNAPSHOT_DIR / "satellites"
    SNAPSHOT_NEO_DIR = SNAPSHOT_DIR / "neo"
    SNAPSHOT_ISS_DIR = SNAPSHOT_DIR / "iss"

    # ======================================================
    # Environment Variables
    # ======================================================

    NASA_API_KEY = os.getenv("NASA_API_KEY", "DEMO_KEY")

    DATABRICKS_HOST = os.getenv("DATABRICKS_HOST", "")
    DATABRICKS_TOKEN = os.getenv("DATABRICKS_TOKEN", "")

    POSTGRES_HOST = os.getenv("POSTGRES_HOST", "localhost")
    POSTGRES_PORT = os.getenv("POSTGRES_PORT", "5432")
    POSTGRES_DB = os.getenv("POSTGRES_DB", "astropulse")

    RABBITMQ_HOST = os.getenv("RABBITMQ_HOST", "localhost")
    RABBITMQ_PORT = os.getenv("RABBITMQ_PORT", "5672")


settings = Settings()