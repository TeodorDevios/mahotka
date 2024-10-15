from config import bot, dp, start_text
from aiogram import types, Dispatcher, Router
from aiogram.filters.command import Command

from filtres.base import IsNotRegister, IsRegister
from filtres.chat import ChatType

base_router = Router()


@base_router.message(Command('start'), IsNotRegister(), ChatType(['private']))
async def start_message(message: types.Message):
    kb = [
        [types.KeyboardButton(text='Регистрация')]
    ]
    key = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True, input_field_placeholder='Выбери нужное',
                                    one_time_keyboard=True)
    await bot.send_message(message.chat.id, start_text, reply_markup=key)


@base_router.message(Command('start'), IsRegister(), ChatType(['private']))
async def start_reg(message: types.Message):
    kb = [[types.KeyboardButton(text='Расписание на сегодня')], [types.KeyboardButton(text='Расписание на завтра')]]
    mrk = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True, one_time_keyboard=True)
    await bot.send_message(message.chat.id, 'Ты уже зарегестирован =)', reply_markup=mrk)
