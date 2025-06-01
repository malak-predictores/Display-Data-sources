import httpx
from app.cache import get_cache, set_cache

BASE_URL = "https://opendata.swiss/api/3/action/package_search"

# All groups you listed
GROUPS = {
    "tech": "https://opendata.swiss/en/group/tech",
    "intr": "https://opendata.swiss/en/group/intr",
    "gove": "https://opendata.swiss/en/group/gove",
    "educ": "https://opendata.swiss/en/group/educ"
}

async def get_swiss_data():
    cache_key = "swiss_data"
    cached = get_cache(cache_key)
    if cached:
        return cached

    try:
        all_results = []

        async with httpx.AsyncClient() as client:
            for group, group_url in GROUPS.items():
                params = {
                    "fq": f"group:{group}",
                    "rows": 1,
                    "sort": "metadata_modified desc"
                }
                response = await client.get(BASE_URL, params=params)
                response.raise_for_status()
                data = response.json()

                if data.get("success") and data["result"]["results"]:
                    dataset = data["result"]["results"][0]
                    all_results.append({
                        "title": dataset.get("title"),
                        "notes": dataset.get("notes"),
                        "group": group,
                        "source": {
                            "name": f"opendata.swiss | {group}",
                            "url": group_url
                        }
                    })

        result = {
            "value": all_results,
            "source": {
                "name": "opendata.swiss (tech, intr, gove, educ)",
                "url": "https://opendata.swiss/en"
            }
        }

        set_cache(cache_key, result)
        return result

    except Exception as e:
        return {
            "value": f"Failed to fetch Swiss data: {e}",
            "source": {
                "name": "opendata.swiss",
                "url": "https://opendata.swiss/en"
            }
        }
