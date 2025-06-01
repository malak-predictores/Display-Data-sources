import httpx
from app.cache import get_cache, set_cache

BASE_URL = "https://data.europa.eu/api/hub/search"

async def get_europa_data():
    cache_key = "europa_data"
    cached = get_cache(cache_key)
    if cached:
        return cached

    params = {
        "q": "gdp",       # Example keyword
        "limit": 1,       # Limit for brevity
        "lang": "en"
    }

    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(BASE_URL, params=params)
            response.raise_for_status()
            data = response.json()

            # Example data structure simplification
            result = {
                "value": data.get("results", [])[0] if data.get("results") else "No results found",
                "source": {
                    "name": "The official portal for European data",
                    "url": "https://data.europa.eu"
                }
            }

            set_cache(cache_key, result)
            return result

    except Exception as e:
        return {
            "value": f"Failed to fetch data: {e}",
            "source": {
                "name": "The official portal for European data",
                "url": "https://data.europa.eu"
            }
        }
