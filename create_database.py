import sqlite3

conn = sqlite3.connect('database.db')

c = conn.cursor()


DROP TABLE IF EXISTS users;
CREATE TABLE users (
           id integer unique primary key autoincrement,
           name text,
           dept text,
           role text
);

c.executescript(sql)

conn.commit()

conn.close()