from aiogram.filters import BaseFilter
from aiogram.types import Message
from typing import Union


class ChatType(BaseFilter):
    def __init__(self, chat_type: Union[str, list]):
        self.chat_type = chat_type

    async def __call__(self, message: Message):
        if isinstance(self.chat_type, str):
            return self.chat_type == message.chat.type
        else:
            return message.chat.type in self.chat_type
