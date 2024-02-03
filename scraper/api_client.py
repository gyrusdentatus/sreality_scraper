import requests
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class APIClient:
    def __init__(self):
        self.base_url = os.getenv('SREALITY_BASE_URL', 'https://www.sreality.cz/api/cs/v2/')
        self.timeout = int(os.getenv('REQUEST_TIMEOUT', 30))

    def fetch_properties(self, params):
        try:
            response = requests.get(f"{self.base_url}estates", params=params, timeout=self.timeout)
            response.raise_for_status()  # Raises stored HTTPError, if one occurred.
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Request failed: {e}")
            return None

