import requests

from shared.config.constants import (
    UPCOMING_LAUNCHES_ENDPOINT,
)
from shared.config.settings import settings
from shared.utils.file_utils import save_json


class LaunchProducer:

    def fetch_launches(self) -> dict:

        response = requests.get(
            UPCOMING_LAUNCHES_ENDPOINT,
            timeout=30
        )

        response.raise_for_status()

        return response.json()

    def save_launches(self, data: dict):

        file_path = save_json(
            data=data,
            directory=settings.RAW_DATA_DIR,
            prefix="launches"
        )

        print(f"Saved file: {file_path}")

    def run(self):

        print("Fetching launch data...")

        payload = self.fetch_launches()

        print(
            f"Records fetched: "
            f"{len(payload.get('results', []))}"
        )

        self.save_launches(payload)


if __name__ == "__main__":

    producer = LaunchProducer()

    producer.run()