import pandas as pd
import sqlite3

con = sqlite3.connect("main.db")
cur = con.cursor()

for lesson in pd.read_excel("example.xlsx").values:
    for i in range(1, 6):
        cur.execute(f'''INSERT INTO lessons (number, class, lesson, room, weekday) 
                        VALUES ({lesson[0]}, "{lesson[1]}", "{lesson[2]}", "{lesson[3]}", {i})''')

con.commit()