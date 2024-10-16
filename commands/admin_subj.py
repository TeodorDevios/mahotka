from aiogram import types, Router, F
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext

from filtres.admin import IsAdmin
from filtres.chat import ChatType
from models.models import RegisterSubjModel
from config import bot
import database.database_bot as db

subj_router = Router()


@subj_router.message(F.text.lower() == 'создать', StateFilter(None), IsAdmin(1330646571), ChatType(['private']))
async def name_subj(message: types.Message, state: FSMContext):
    await bot.send_message(message.chat.id, 'Напиши название группы')
    await state.set_state(RegisterSubjModel.name_sp)


@subj_router.message(RegisterSubjModel.name_sp, IsAdmin(1330646571), ChatType(['private']))
async def save_name(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    await bot.send_message(message.chat.id, 'Теперь расписание. Формат: день_период_предмет_мод')
    await state.set_state(RegisterSubjModel.text_sbj)


@subj_router.message(RegisterSubjModel.text_sbj)
async def save_subj(message: types.Message, state: FSMContext):
    data = await state.get_data()
    subjects = [s.split('_') for s in message.text.split('\n')]
    db.add_sub(db.get_un_id(data['name']), subjects)
    await bot.send_message(message.chat.id, 'Расписание успешно добавлено')
    await state.clear()
