import requests
from typing import Dict

SWISS_GROUPS = ["tech", "intr", "gove", "educ"]
BASE_URL = "https://ckan.opendata.swiss/api/3/action/package_search"

def get_swiss_data() -> Dict:
    try:
        all_group_data = {}
        headers = {"Accept": "application/json"}

        for group in SWISS_GROUPS:
            params = {
                "fq": f"group:{group}",
                "rows": 1,
                "sort": "metadata_modified desc"
            }
            response = requests.get(BASE_URL, headers=headers, params=params, timeout=10)
            response.raise_for_status()

            data = response.json()
            all_group_data[group] = data.get("result", {}).get("results", [{}])[0]

        return {
            "value": all_group_data,
            "source": {
                "name": "opendata.swiss",
                "url": "https://opendata.swiss/en"
            }
        }
    except Exception as e:
        return {
            "value": f"Failed to fetch Swiss data: {str(e)}",
            "source": {
                "name": "opendata.swiss",
                "url": "https://opendata.swiss/en"
            }
        }
