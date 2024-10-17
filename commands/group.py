from config import bot, dp, start_text
from aiogram import types, Router
from aiogram.filters.command import Command

from filtres.base import IsNotRegister, IsRegister
from filtres.chat import ChatType

base_router = Router()



