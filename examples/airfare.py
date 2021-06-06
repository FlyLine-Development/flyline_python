import asyncio
import datetime
import os

from flyline import FlylineClient


async def main():
    key = os.getenv("FLYLINE_TOKEN")
    async with FlylineClient(key) as client:
        tomorrow = datetime.date.today() + datetime.timedelta(days=1)
        data = {
            "cabin_class": "economy",
            "slices": [{"departure": {"code": "DFW", "date": tomorrow.isoformat()}, "arrival": {"code": "LAX"}}],
            "permitted_carriers": ["UA"],
            "passengers": [{"age": 27}],
        }
        seat_map = await client.get_airfares(data=data)
        print(seat_map)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
