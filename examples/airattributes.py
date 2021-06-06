import asyncio
from datetime import date, timedelta

from flyline import FlylineClient

client = FlylineClient("")


async def main():
    tomorrow = (date.today() + timedelta(days=1)).isoformat()
    data = {
        "cabin_class": "economy",
        "departure": "DFW",
        "arrival": "LAX",
        "departure_date": tomorrow,
        "flight_no": "2812",
        "carrier": "AA",
    }
    res = await client.get_airattributes_by_flight_number(data)
    return res


if __name__ == "__main__":
    asyncio.run(main())
