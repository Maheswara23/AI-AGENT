from engine.db_utils import get_connection
import csv

with get_connection() as con:
    cur = con.cursor()

#query = "CREATE TABLE IF NOT EXISTS sys_command(id integer PRIMARY KEY, name VARCHAR(100), path VARCHAR(100));"
#cur.execute(query)

#query = "INSERT INTO sys_command VALUES (null, 'vs code', 'C:\\Users\\mukka\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe');"
#cur.execute(query)
#con.commit()

#query = "CREATE TABLE IF NOT EXISTS web_command(id integer PRIMARY KEY, name VARCHAR(100), path VARCHAR(100));"
#cur.execute(query)

#query = "INSERT INTO web_command VALUES (null, 'github', 'https://github.com/')"
#cur.execute(query)
#con.commit()

#cur.execute('''CREATE TABLE IF NOT EXISTS contacts (id integer primary key, name VARCHAR(200), mobile_no VARCHAR(255), email VARCHAR(255) NULL)''')
#con.commit()


cur.execute("UPDATE contacts SET name='topper' WHERE id=88")
con.commit()