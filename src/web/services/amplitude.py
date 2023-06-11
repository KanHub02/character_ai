from typing import ClassVar, Dict, List

import aiohttp
import json
from decouple import config


class AmplitudeRequestService:
    __API_KEY__: ClassVar[str] = config("AMPLITUDE_KEY")
    __HEADERS__: ClassVar[Dict[str, str]] = {
        "Content-type": "application/json",
        "Accept": "*/*",
    }

    @classmethod
    async def send_event(
        cls,
        device_id: str,
        event_type: str,
    ) -> None:
        data: Dict[str, List[Dict[str, str]]] = {
            "api_key": cls.__API_KEY__,
            "events": [{"device_id": device_id, "event_type": event_type}],
        }
        async with aiohttp.ClientSession() as session:
            await session.post(
                "https://api2.amplitude.com/2/httpapi",
                headers=cls.__HEADERS__,
                data=json.dumps(data),
            )
