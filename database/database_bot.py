import psycopg2 as ps

conn = ps.connect(user="postgres", password="artd2006st", host="127.0.0.1",
                                  port="5432",
                                  database="mah")

peer = {
    '1': '8:00 - 9:35',
    '2': '9:45 - 11:20',
    '3': '11:30 - 13:05',
    '4': '13:25 - 15:00',
    '5': '15:10 - 16:45',
    '6': '16:55 - 18:30'
}


def add_speciality(course: int, name: str) -> None:
    curs = conn.cursor()
    curs.execute('''INSERT INTO speciality(course, name_sp) VALUES (%s, %s)''', (course, name))
    conn.commit()


def get_spec(course: str) -> list:
    curs = conn.cursor()
    curs.execute('''SELECT * FROM speciality WHERE course=%s''', (course,))
    res = curs.fetchall()
    return res


def get_all_spec() -> list:
    curs = conn.cursor()
    curs.execute('''SELECT * FROM speciality''')
    res = curs.fetchall()
    return res


def add_user(user_id: int, un_id: int):
    curs = conn.cursor()
    curs.execute('''INSERT INTO users(user_id, un_id) VALUES (%s, %s)''', (user_id, un_id))
    conn.commit()


def get_un_id(name: str) -> int:
    curs = conn.cursor()
    curs.execute('''SELECT * FROM speciality WHERE name_sp=%s''', (name,))
    res = curs.fetchall()[0][1]
    return res


def get_users_id() -> list:
    curs = conn.cursor()
    curs.execute('''SELECT * FROM users''')
    res = curs.fetchall()
    us_id = []
    for i in range(len(res)):
        us_id.append(res[i][0])
    return us_id


def add_sub(un_id: int, subj_list: list):
    curs = conn.cursor()
    for i in range(len(subj_list)):
        curs.execute('''INSERT INTO subjects(un_id, day_num, time_pr, name_sbj) VALUES (%s, %s, %s, %s)''',
                     (un_id, subj_list[i][0], subj_list[i][1], subj_list[i][2]))
    conn.commit()


# Доработать обязательно
def edit_sub():
    pass


def get_sub():
    pass


def get_schedule(user_id: int, day_n: int):
    curs = conn.cursor()
    curs.execute('''SELECT un_id FROM users WHERE user_id=%s''', (user_id,))
    un_id = curs.fetchall()[0]
    curs.execute('''SELECT * FROM subjects WHERE un_id=%s AND day_num=%s''', (un_id, str(day_n)))
    r = curs.fetchall()
    text = ''
    for i in range(len(r)):
        text += f'{peer[r[i][3]]}у - {r[i][4]}\n'
    return [r, text]


def get_shed_week():
    pass
