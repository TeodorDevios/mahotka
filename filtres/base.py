from aiogram.filters import BaseFilter
from aiogram.types import Message
import database.database_bot as db


class IsNotRegister(BaseFilter):
    async def __call__(self, message: Message):
        return not(message.chat.id in db.get_users_id())


class IsRegister(BaseFilter):
    async def __call__(self, message: Message):
        return message.chat.id in db.get_users_id()
