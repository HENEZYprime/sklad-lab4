import os
import sqlite3
base_dir = os.path.dirname(os.path.abspath(__file__))
init_path = os.path.join(base_dir, 'db', 'init.sql')

with open(init_path, 'r', encoding='utf-8') as f:
    sql = f.read()

conn = sqlite3.connect(os.path.join(base_dir, 'db', 'sklad.db'))
conn.executescript(sql)
conn.commit()
conn.close()
print("База успешно создана!")