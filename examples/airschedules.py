import asyncio
import os

from flyline import FlylineClient


async def main():
    key = os.getenv("FLYLINE_TOKEN")
    async with FlylineClient(key) as client:
        schedule = await client.get_schedules_by_flight_number(airline="AA", date="2021-06-03", flight_number="110ff0")
        print(schedule)
        schedules = await client.get_schedules_by_route(
            origin="DFW", destination="LAX", airline="AA", date="2021-06-01"
        )
        print(schedules)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
