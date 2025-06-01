import requests
from typing import Dict

EUROPA_API_URL = "https://data.europa.eu/data/datasets?res_format=JSON"

def get_europa_data() -> Dict:
    try:
        headers = {"Accept": "application/json"}
        response = requests.get(EUROPA_API_URL, headers=headers, timeout=10)
        response.raise_for_status()

        data = response.json()
        return {
            "value": data if data else "No data available",
            "source": {
                "name": "The official portal for European data",
                "url": "https://data.europa.eu"
            }
        }
    except Exception as e:
        return {
            "value": f"Failed to fetch data: {str(e)}",
            "source": {
                "name": "The official portal for European data",
                "url": "https://data.europa.eu"
            }
        }
