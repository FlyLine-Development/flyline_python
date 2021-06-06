import asyncio

from aiohttp import ClientSession


class FlylineBaseClient:
    BASE_URL = "https://api.flyline.io/api"

    def __init__(self, key: str):
        self._key = key
        headers = {"Authorization": f"FToken {self._key}"}
        self._loop = asyncio.get_event_loop()
        self.session = ClientSession(headers=headers, loop=self._loop)

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.session.close()
