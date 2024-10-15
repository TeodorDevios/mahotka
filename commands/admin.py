from aiogram import types, Router, F
from aiogram.filters.command import Command
from filtres.admin import IsAdmin
from filtres.chat import ChatType
from config import bot

admin_router = Router()


@admin_router.message(IsAdmin(1330646571), ChatType(['private']), Command('r'))
async def add_schedule(message: types.Message):
    kb = [[types.KeyboardButton(text='Новое направление')], [types.KeyboardButton(text='Создать')],
          [types.KeyboardButton(text='Редактировать')],
          [types.KeyboardButton(text='Закрыть')]]
    mark = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True, one_time_keyboard=True)
    await bot.send_message(message.chat.id, 'Выбери действие', reply_markup=mark)


