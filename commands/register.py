from aiogram import types, F, Router
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext

from models.models import RegisterUserModel
from filtres.base import IsNotRegister
import database.database_bot as db
from config import bot, aviable_courses, aviable_spec

register_router = Router()


@register_router.message(StateFilter(None), F.text.lower() == "регистрация", IsNotRegister())
async def reg_begin(message: types.Message, state: FSMContext):
    kb = [[types.KeyboardButton(text=str(i + 1))] for i in range(4)]
    mrk = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True, one_time_keyboard=True)
    await bot.send_message(message.chat.id, 'Выбери курс из доступных', reply_markup=mrk)
    await state.set_state(RegisterUserModel.course)


@register_router.message(RegisterUserModel.course, F.text.in_(aviable_courses), IsNotRegister())
async def reg_course(message: types.Message, state: FSMContext):
    course = message.text
    await state.update_data(course=course)
    spec = db.get_spec(course)
    kb = [[types.KeyboardButton(text=s[2])] for s in spec]
    mrk = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True, one_time_keyboard=True)
    await bot.send_message(message.chat.id, 'Супер! А теперь выбери свою специальность', reply_markup=mrk)
    await state.set_state(RegisterUserModel.name)


@register_router.message(RegisterUserModel.course, IsNotRegister())
async def err_course(message: types.Message):
    await bot.send_message(message.chat.id, 'Я не знаю такого курса =)')


@register_router.message(RegisterUserModel.name, F.text.in_(aviable_spec), IsNotRegister())
async def reg_spec(message: types.Message, state: FSMContext):
    kb = [[types.KeyboardButton(text='Расписание на сегодня')], [types.KeyboardButton(text='Расписание на завтра')]]
    mrk = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True, one_time_keyboard=True)
    await bot.send_message(message.chat.id, 'Теперь ты можешь получать расписание', reply_markup=mrk)
    db.add_user(int(message.chat.id), db.get_un_id(message.text))
    await state.clear()


@register_router.message(RegisterUserModel.name, IsNotRegister())
async def err_spec(message: types.Message):
    await bot.send_message(message.chat.id, 'Я не знаю такой специальности =)')
