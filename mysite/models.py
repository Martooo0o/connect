import sqlite3 as sql
from os import path

ROOT = path.dirname(path.relpath((__file__)))

def create_post(name, content):
    con = sql.connect(path.join(ROOT, 'database.db'))

    curr = con.cursor()
    curr.execute('insert into posts (name, content, likes) values (?, ?, ?)', (name, content, 0))
    con.commit()
    con.close()

def get_posts():
    con = sql.connect(path.join(ROOT, 'database.db'))
    curr = con.cursor()
    curr.execute('select * from posts')
    posts = curr.fetchall()
    return posts