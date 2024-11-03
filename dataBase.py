import sqlite3
conn=sqlite3.connect("dataBase.db")
cursor =conn.cursor()

qurey="CREATE TABLE IF NOT EXISTS commands( id INTEGER PRIMARY KEY AUTOINCREMENT, command TEXT NOT NULL,action_type TEXT NOT NULL,action_value TEXT NOT NULL)"
cursor.execute(qurey)
query="INSERT INTO commands (command, action_type, action_value) VALUES('open google', 'url', 'https://www.google.com'),('open github', 'url', 'https://www.github.com'),('open vs code', 'file', 'C:\\Users\\satap\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code'),('open mywork folder', 'file', 'E:\\myWorks'),('open you tube', 'url', 'https://www.youtube.com/')"
cursor.execute(query)
conn.commit()
conn.close()