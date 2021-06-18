import asyncio
import datetime
import os

from flyline import FlylineClient


async def main():
    key = os.getenv("FLYLINE_TOKEN")
    async with FlylineClient(key) as client:
        tomorrow = datetime.date.today() + datetime.timedelta(days=1)
        # Attributes by Flight no
        data = {
            "cabin_class": "economy",
            "departure": "DFW",
            "arrival": "LAX",
            "departure_date": tomorrow.isoformat(),
            "flight_no": "2812",
            "carrier": "AA",
        }
        res = await client.get_airattributes_by_flight_number(data=data)
        print(res)

        # Attributes by Route
        data = {
            "cabin_class": "economy",
            "slices": [{"departure": {"code": "DFW", "date": tomorrow.isoformat()}, "arrival": {"code": "LAX"}}],
        }
        res = await client.get_airattributes_by_route(data=data)
        print(res)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
