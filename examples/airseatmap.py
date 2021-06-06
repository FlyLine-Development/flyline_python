import asyncio
import os

from flyline import FlylineClient


async def main():
    key = os.getenv("FLYLINE_TOKEN")
    async with FlylineClient(key) as client:
        seat_map = await client.get_seat_map(carrier="QR", aircraft="77W")
        print(seat_map)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
