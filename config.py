from aiogram import Bot, Dispatcher

import database.database_bot as db

bot = Bot(token='7186326652:AAEJEfLGVt0RPpdk4AtjI1Qwr3og3BlQpNI')
dp = Dispatcher()

start_text = '''
Привет!
Здесь ты сможешь посмотреть свое расписание на каждый день
Главное - убедись, что твои группа и направление поддерживаются 
'''

aviable_courses = ['1', '2', '3', '4']
aviable_spec = [s[2] for s in db.get_all_spec()]
peer = {
    '1': '8:00 - 9:35',
    '2': '9:45 - 11:20',
    '3': '11:30 - 13:05',
    '4': '13:25 - 15:00',
    '5': '15:10 - 16:45',
    '6': '16:55 - 18:30'
}
days = {
    '1': 'Понедельник',
    '2': 'Вторник',
    '3': 'Среда',
    '4': 'Четверг',
    '5': 'Пятница',
    '6': 'Суббота',
    '7': 'Воскресенье'
}

url = 'https://docs.google.com/spreadsheets/d/1nJ7-eGB-gYJNgm5CTqodenKnUSQlhMeFs2gVLuyxEsM/edit?gid=64208083#gid=64208083'
