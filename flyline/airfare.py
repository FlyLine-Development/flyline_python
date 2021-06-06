from .schemas import AirFare


class AirFareAPI:
    async def get_airfares(self, data) -> AirFare:
        url = f"{self.BASE_URL}/flights/shop/"
        async with self.session.post(url, json=data) as response:
            res = await response.json()
            return AirFare.from_json(res)
