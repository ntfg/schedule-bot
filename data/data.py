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
            self.cur.execute(sql_script)
    
    def update_data(self, xl_files: List[str]):
        for weekday, file_name in enumerate(xl_files, start=1):
            pass