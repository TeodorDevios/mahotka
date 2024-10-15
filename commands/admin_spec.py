from aiogram import types, Router, F
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext

from filtres.admin import IsAdmin
from filtres.chat import ChatType
from models.models import RegisterSpecModel
from config import bot
import database.database_bot as db

spec_router = Router()


@spec_router.message(StateFilter(None), F.text.lower() == 'новое направление', IsAdmin(1330646571), ChatType(['private']))
async def spec_reg(message: types.Message, state: FSMContext):
    await bot.send_message(message.chat.id, 'Напиши курс')
    await state.set_state(RegisterSpecModel.course)


@spec_router.message(RegisterSpecModel.course, IsAdmin(1330646571), ChatType(['private']))
async def spec_course(message: types.Message, state: FSMContext):
    await state.update_data(course=message.text)
    await bot.send_message(message.chat.id, 'Напиши название специальности')
    await state.set_state(RegisterSpecModel.name)


@spec_router.message(RegisterSpecModel.name, IsAdmin(1330646571), ChatType(['private']))
async def spec_name(message: types.Message, state: FSMContext):
    data = await state.get_data()
    db.add_speciality(data['course'], message.text)
    await bot.send_message(message.chat.id, 'Предмет добавлен')
    await state.clear()
