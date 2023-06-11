from typing import ClassVar, Dict, List, Any

import aiohttp

from decouple import config


class GptRequestService:
    __API_KEY__: ClassVar[str] = config("OPENAI_API_KEY")
    __HEADERS__: ClassVar[Dict[str, str]] = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {__API_KEY__}",
    }

    def __init__(self, character: str) -> None:
        self.role = character

    async def send_message(self, message: str) -> str:
        data: Dict[str, Any] = {
            "model": "gpt-3.5-turbo",
            "messages": [
                {
                    "role": "system",
                    "content": f"Pretend to be this character - {self.role}",
                },
                {"role": "user", "content": message},
            ],
        }
        async with aiohttp.ClientSession() as session:
            async with session.post(
                "https://api.openai.com/v1/chat/completions",
                headers=self.__HEADERS__,
                json=data,
            ) as response:
                response_data = await response.json()
                return response_data

    async def create_character(self, instance) -> None:
        data: Dict[str, Any] = {
            "model": "gpt-3.5-turbo",
            "messages": [
                {
                    "role": "system",
                    "content": f"Pretend to be this character - {self.role}",
                },
                {
                    "role": "user",
                    "content": "напиш о себе",
                },
            ],
        }
        async with aiohttp.ClientSession() as session:
            async with session.post(
                "https://api.openai.com/v1/chat/completions",
                headers=self.__HEADERS__,
                json=data,
            ) as response:
                response_content = await response.json()
                message = response_content.get("choices")[0]["message"].get("content")
                instance.greeting_message = message
                await self.generate_type(instance)

    async def generate_type(self, instance) -> None:
        data: Dict[str, Any] = {
            "model": "gpt-3.5-turbo",
            "messages": [
                {
                    "role": "user",
                    "content": f"напиши о {instance.title} в двух словах",
                },
            ],
        }
        async with aiohttp.ClientSession() as session:
            async with session.post(
                "https://api.openai.com/v1/chat/completions",
                headers=self.__HEADERS__,
                json=data,
            ) as response:
                response_content = await response.json()
                short_description = response_content.get("choices")[0]["message"].get(
                    "content"
                )
                instance.short_description = short_description
