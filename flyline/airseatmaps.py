from typing import List

from .schemas import SeatMap


class AirSeatMapAPI:
    async def get_seat_map(self, carrier: str, aircraft: str) -> List[SeatMap]:
        async with self.session.get(f"{self.BASE_URL}/seat-maps/") as response:
            res = await response.json()
            return SeatMap.from_json(res)
