import requests
import time
import logging
from dataclasses import dataclass

logger = logging.getLogger(__name__)

class ExtractError(Exception):
    "Raised when extraction fails after all retries are used up"

@dataclass
class ExtractConfig:
    url: str
    max_retries: int = 3
    backoff: int = 2

def extract_orders(config: ExtractConfig):
    for attempt in range(1, config.max_retries + 1):
        try:
            response = requests.get(config.url, timeout=5)
            if response.status_code == 200:
                return response.json()
            logger.error(f"Got status code {response.status_code}")
        except requests.exceptions.RequestException as e:
            logger.error(f"Request failed: {e}")
        time.sleep(config.backoff)

    raise ExtractError(f"Failed to extract orders after {config.max_retries} retries")