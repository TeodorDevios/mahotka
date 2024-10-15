from aiogram import types, Router, F
from aiogram.utils.keyboard import InlineKeyboardBuilder
from datetime import datetime

from config import bot, days, url
import database.database_bot as db

schedule_router = Router()


@schedule_router.message(F.text.lower() == 'расписание на сегодня')
async def schedule_today(message: types.Message):
    now = datetime.now()
    b = InlineKeyboardBuilder()
    day_n = datetime.isoweekday(now)
    ind_n = 0
    ind_l = 0
    match day_n:
        case 7:
            ind_l = 1
            ind_n = 1
        case 1: ind_l = 7
        case _:
            ind_l = day_n - 1
            ind_n = day_n + 1
    b.row(types.InlineKeyboardButton(text='⬅️', callback_data=f'left:{ind_l}'),
          types.InlineKeyboardButton(text='➡️', callback_data=f'right:{ind_n}'))
    b.row(types.InlineKeyboardButton(text='Google-Таблица с расписанием', url=url))
    schedule = db.get_schedule(message.chat.id, day_n)
    if schedule[0]:
        await bot.send_message(message.chat.id, f'Вот твое расписание на {days[schedule[0][0][2]]}:\n'
                                            f'{schedule[1]}', reply_markup=b.as_markup())
    await bot.send_message(message.chat.id, f'Расписания на {days[str(day_n)]} нет. Отдыхаем',
                           reply_markup=b.as_markup())



