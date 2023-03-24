import sqlite3 
import datetime as dt
from shlak import lessons_emojies, schedule

PATH = "data/main.db"

def today(user_id):
    which_class = _get_user_class(user_id)
    
    with sqlite3.connect(PATH) as con:
        cur = sqlite3.Cursor(con)
        lessons = cur.execute(f'''SELECT number, lesson, cabinet FROM lessons WHERE class LIKE "{which_class}" 
                                  AND weekday = {dt.datetime.isoweekday(dt.datetime.now())}''').fetchall()
    if len(lessons):
        return _parse_lessons(lessons)

    return "Выходной😴"
        


def tomorrow(user_id):
    which_class = _get_user_class(user_id)
    
    with sqlite3.connect(PATH) as con:
        cur = sqlite3.Cursor(con)
        lessons = cur.execute(f'''SELECT number, lesson, cabinet FROM lessons WHERE class LIKE "{which_class}" 
                                  AND weekday = {dt.datetime.isoweekday(dt.datetime.now() + dt.timedelta(days=1))}''').fetchall()
    if len(lessons):
        return _parse_lessons(lessons)

    return "Выходной😴"

def change_class(which_class: str, user_id: int) -> bool:
    with sqlite3.connect(PATH) as con:
        cur = sqlite3.Cursor(con)
        if len(cur.execute(f'''SELECT DISTINCT class 
                               FROM lessons WHERE class LIKE "{which_class}"''').fetchall()) == 1:
            cur.execute(f'DELETE FROM users WHERE from_id = {user_id}')
            cur.execute(f'INSERT INTO users (from_id, class) VALUES ({user_id}, "{which_class}")')
            return True 
        
        return False
    

def _parse_lessons(lessons: list) -> str:
    answ: str = ""
    for lesson in lessons:
            l1 = f"🕘{lesson[0]} урок ({schedule[lesson[0]]})\n"
            l2 = f"{lessons_emojies[lesson[1]]}{lesson[1]}\n"
            l3 = f"кабинет №{lesson[2]}\n\n"
            answ += l1 + l2 + l3
            
    return answ

        
def _get_user_class(user_id: int) -> str:
    with sqlite3.connect(PATH) as con:
        cur = sqlite3.Cursor(con)
        return cur.execute(f"SELECT class FROM users WHERE from_id = {user_id}").fetchone()[0]
