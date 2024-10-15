from aiogram.filters.state import State, StatesGroup


class RegisterUserModel(StatesGroup):
    course = State()
    name = State()


class RegisterSpecModel(StatesGroup):
    course = State()
    name = State()


class RegisterSubjModel(StatesGroup):
    name_sp = State()
    text_sbj = State()
