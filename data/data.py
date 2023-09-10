import sqlite3
from typing import List

class Data:
    def __init__(self):
        self.con = sqlite3.connect("data/main.db")
        self.cur = self.con.cursor()
        
        """
        Проверка на наличие таблицы lessons
        Если её нет, произойдет ошибка SQL и в модуле except она создастся
        """
        try: 
            self.cur.execute("SELECT * FROM lessons")
        except:
            sql_script = open("data/script.sql", "r").read()
            self.cur.executescript(sql_script)
            
    def user_exists(self, user_id: int) -> bool:
        return self.cur.execute(f'SELECT * FROM users WHERE user_id = {user_id}').fetchone()

    def class_exists(self, user_class: str) -> bool:
        return self.cur.execute(f'SELECT * FROM lessons WHERE class LIKE "{user_class}"').fetchone()
    
    def update_class(self, user_id: int, user_class: str) -> None:
        self.cur.execute(f'DELETE FROM users WHERE user_id = {user_id}')
        self.cur.execute(f'INSERT INTO users (user_id, class) VALUES ({user_id}, "{user_class}")')
        self.con.commit()
        
    def get_schedule(self, user_id: int, weekday: int) -> List[tuple]: 
        return self.cur.execute(f'''SELECT * FROM lessons 
                                    WHERE class = (SELECT class FROM users WHERE user_id = {user_id}) AND weekday = {weekday}
                                    ORDER BY number''').fetchall()
        
        