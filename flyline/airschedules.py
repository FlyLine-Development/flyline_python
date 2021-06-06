from typing import List, Optional

from .schemas import Schedule


class AirScheduleAPI:
    async def get_schedules_by_flight_no(self, airline: str, date: str, flight_number: str) -> Optional[Schedule]:
        url = f"{self.BASE_URL}/schedule-flight/"
        data = {
            "airline": airline,
            "date": date,
            "flight_number": flight_number,
        }
        async with self.session.post(url, json=data) as response:
            res = await response.json()
            return Schedule.from_json(res)

    async def get_schedules_by_route(
        self, airline: str, origin: str, destination: str, date: str
    ) -> Optional[List[Schedule]]:
        url = f"{self.BASE_URL}/schedule-flight/"
        data = {
            "airline": airline,
            "origin": origin,
            "destination": destination,
            "date": date,
        }
        async with self.session.post(url, json=data) as response:
            res = await response.json()
            return Schedule.from_json(res)
