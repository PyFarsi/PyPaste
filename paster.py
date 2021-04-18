import sqlite3
import base64
import uuid
from random import choice

chars = 'abcdefghijklmnopqrstuvwxyz'
db_path = 'db\Pastes.db'
db_conn = sqlite3.connect(db_path, check_same_thread=False)

def key_is_not_exists(key):
    cur = db_conn.cursor()
    cur.execute('SELECT * FROM pastes WHERE key=?', (key,))
    if not cur.fetchall():
        return True
    else:
        return False

def gen_key():
    while True:
        key = ''
        for i in range(10):
            key += choice(chars)
        if key_is_not_exists(key):
            break
    return key

def sqlitify(content):
    key = gen_key()
    cur = db_conn.cursor()
    cur.execute('INSERT INTO pastes(key, contents) VALUES(?, ?)', (key, base64.b64encode(content.encode()).decode()))
    db_conn.commit()
    del cur
    print(key)
    return key

def paste(content):
    key = sqlitify(
        content=content
    )
    return key

def get_content(key):
    cur = db_conn.cursor()
    cur.execute('SELECT * FROM pastes WHERE key=?', (key,))
    f = cur.fetchall()
    if not f:
        return 'DOCUMENT(PASTE)_NOT_FOUND'
    else:
        content = f[0][1]
        content_dec = base64.b64decode(content.encode()).decode()
        return content_dec