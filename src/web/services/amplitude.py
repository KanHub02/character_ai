from typing import ClassVar, Dict, List

import aiohttp
import asyncio
import json
import datetime

from decouple import config

from web.models import Amplitude


class AmplitudeRequestService:
    __model__ = Amplitude
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
            async with session.post(
                "https://api2.amplitude.com/2/httpapi",
                headers=cls.__HEADERS__,
                data=json.dumps(data),
            ) as response:
                if response.status == 200:
                    try:
                        instance = cls.__model__.objects.create(
                            device_id=device_id, event_type=event_type
                        )
                        instance.save()
                    except:
                        pass
                else:
                    pass
