from aiogram import types, Router, F
from aiogram.enums import ParseMode
from aiogram.utils.keyboard import InlineKeyboardBuilder
from datetime import datetime
import calendar

from config import bot, days, url, mood_d
import database.database_bot as db

schedule_router = Router()


@schedule_router.message(F.text.lower() == 'расписание на сегодня')
async def schedule_today(message: types.Message):
    now = datetime.now().weekday()
    n = datetime.now().date()
    b = InlineKeyboardBuilder()
    day_n = datetime.isoweekday(n)
    ind_r = 0
    ind_l = 0
    mood = mood_d(str(n))
    match day_n:
        case 7:
            ind_l = 6
            ind_r = 1
        case 1: ind_l = 7
        case _:
            ind_l = day_n - 1
            ind_r = day_n + 1
    b.row(types.InlineKeyboardButton(text='⬅️', callback_data=f'left:{ind_l}:{str(n)}'),
          types.InlineKeyboardButton(text='➡️', callback_data=f'right:{ind_r}:{str(n)}'))
    b.row(types.InlineKeyboardButton(text='Google-Таблица с расписанием', url=url))
    schedule = db.get_schedule(message.chat.id, day_n)
    if schedule[0]:
        await bot.send_message(message.chat.id, f'<i><u>Расписание на <b>{days[schedule[0][0][2]]} [{mood}]:</b></u>\n{schedule[1]}</i>',
                               reply_markup=b.as_markup(), parse_mode=ParseMode.HTML)
    else:
        await bot.send_message(message.chat.id, f'<i>Пар на <b>{days[str(day_n)]}</b> необнаружено. Можно поспать💤</i>',
                               reply_markup=b.as_markup(), parse_mode=ParseMode.HTML)


@schedule_router.callback_query(F.data.startswith('right:'))
async def right(call: types.CallbackQuery):
    data = call.data.split(':')
    ind = int(data[1])
    ind_r = 0
    ind_l = 0
    now_data = datetime.isocalendar(datetime.strptime(data[2], "%Y-%m-%d"))
    mx_d = calendar.monthrange(now_data.year, int(data[2].split('-')[1]))[1]
    mounth = int(data[2].split('-')[1])
    day = int(data[2].split('-')[2])
    day_n = 0
    if mx_d == day:
        if mounth == 12:
           day_n = 1
           mounth = 1
        else:
            mounth = int(data[2].split('-')[1]) + 1
            day_n = 1
    elif mx_d > day:
        day_n = int(data[2].split('-')[2]) + 1

    mood = mood_d(str(f'{data[2].split('-')[0]}-{mounth}-{day_n}'))
    now_data = str(f'{data[2].split('-')[0]}-{mounth}-{day_n}')
    match ind:
        case 7:
            ind_l = 6
            ind_r = 1
        case 1:
            ind_l = 7
            ind_r = ind + 1
        case _:
            ind_l = ind - 1
            ind_r = ind + 1
    b = InlineKeyboardBuilder()
    b.row(types.InlineKeyboardButton(text='⬅️', callback_data=f'left:{ind_l}:{now_data}'),
          types.InlineKeyboardButton(text='➡️', callback_data=f'right:{ind_r}:{now_data}'))
    b.row(types.InlineKeyboardButton(text='Google-Таблица с расписанием', url=url))
    schedule = db.get_schedule(call.from_user.id, ind)
    if schedule[0]:
        await call.message.edit_text(text=f'<i><u>Расписание на <b>{days[schedule[0][0][2]]} [{mood}]:</b></u>\n{schedule[1]}</i>',
                                     reply_markup=b.as_markup(), parse_mode=ParseMode.HTML)
    else:
        await call.message.edit_text(text=f'<i>Пар на <b>{days[str(ind)]}</b> необнаружено. Можно поспать 💤</i>',
                                     reply_markup=b.as_markup(), parse_mode=ParseMode.HTML)


@schedule_router.callback_query(F.data.startswith('left:'))
async def left(call: types.CallbackQuery):
    data = call.data.split(':')
    ind = int(call.data.split(':')[1])
    ind_r = 0
    ind_l = 0
    mounth = int(data[2].split('-')[1])
    day = int(data[2].split('-')[2])
    day_n = 0
    now_data = datetime.isocalendar(datetime.strptime(data[2], "%Y-%m-%d"))
    mx_d = calendar.monthrange(now_data.year, int(data[2].split('-')[1]))[1]
    if day == 1:
        mounth = int(data[2].split('-')[1]) - 1
        day_n = 31
    elif mx_d > day:
        day_n = int(data[2].split('-')[2]) - 1
    mood = mood_d(str(f'{data[2].split('-')[0]}-{mounth}-{day_n}'))
    now_data = str(f'{data[2].split('-')[0]}-{mounth}-{day_n}')
    match ind:
        case 7:
            ind_l = 6
            ind_r = 1
        case 1:
            ind_l = 7
            ind_r = ind + 1
        case _:
            ind_l = ind - 1
            ind_r = ind + 1
    b = InlineKeyboardBuilder()
    b.row(types.InlineKeyboardButton(text='⬅️', callback_data=f'left:{ind_l}:{now_data}'),
          types.InlineKeyboardButton(text='➡️', callback_data=f'right:{ind_r}:{now_data}'))
    b.row(types.InlineKeyboardButton(text='Google-Таблица с расписанием', url=url))
    schedule = db.get_schedule(call.from_user.id, ind)
    if schedule[0]:
        await call.message.edit_text(text=f'<i><u>Расписание на <b>{days[schedule[0][0][2]]} [{mood}]:</b></u>\n{schedule[1]}</i>',
                                     reply_markup=b.as_markup(), parse_mode=ParseMode.HTML)
    else:
        await call.message.edit_text(text=f'<i>Пар на <b>{days[str(ind)]}</b> необнаружено. Можно поспать 💤</i>',
                                     reply_markup=b.as_markup(), parse_mode=ParseMode.HTML)
