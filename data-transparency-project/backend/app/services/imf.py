import httpx
from app.cache import get_cache, set_cache

BASE_URL = "https://www.imf.org/external/datamapper/api/v1/GDP/CHE"


# Example endpoint for GDP data by country
INDICATOR = "NGDPD"  # Nominal GDP in USD
COUNTRY = "CHE"      # Switzerland (ISO-3)

async def get_imf_data():
    cache_key = "imf_data"
    cached = get_cache(cache_key)
    if cached:
        return cached

    try:
        url = f"{BASE_URL}/{INDICATOR}/{COUNTRY}"
        async with httpx.AsyncClient() as client:
            response = await client.get(url)
            response.raise_for_status()
            data = response.json()

            if not data or COUNTRY not in data:
                raise ValueError("Data not found for Switzerland")

            series = data[COUNTRY]
            years = sorted(series.keys(), reverse=True)
            latest_year = years[0]
            gdp_value = series[latest_year]

            result = {
                "value": {
                    "country": "Switzerland",
                    "indicator": "Nominal GDP (USD)",
                    "year": latest_year,
                    "value": gdp_value
                },
                "source": {
                    "name": "IMF DataMapper API",
                    "url": "https://www.imf.org/external/datamapper/api/"
                }
            }

            set_cache(cache_key, result)
            return result

    except Exception as e:
        return {
            "value": f"Failed to fetch IMF data: {e}",
            "source": {
                "name": "IMF DataMapper API",
                "url": "https://www.imf.org/external/datamapper/api/"
            }
        }
