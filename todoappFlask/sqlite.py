import sqlite3
from datetime import datetime

DB_PATH = 'todoapp.db'   # Update this path accordingly
NOTSTARTED = 'Not Started'
INPROGRESS = 'In Progress'
COMPLETED = 'Completed'

insertQuery = """INSERT INTO items
    VALUES (?, ?, ?, ?, ?);"""

updatequery = """UPDATE items
                SET status=?,
                    actiontime=?,
                    repeatperdaycount=?
                WHERE name=?;"""

deletequery = """DELETE from items
WHERE name=?"""


def add_to_list(item:str, actiontime:str, repeatcount:int):
    try:
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        createdtime = datetime.now()
        actiondatetime = datetime.strptime(actiontime, "%Y-%m-%d %H:%M:%S")
        print(createdtime)
        c.execute(insertQuery, (item, NOTSTARTED, datetime.now(), actiondatetime, repeatcount))
        conn.commit()
        return {"item": item, "status": NOTSTARTED, "repeatcount": repeatcount}
    except Exception as e:
        print('Error: ', e)
        return None

def get_all_items():
    try:
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute('select * from items')
        rows = c.fetchall()
        return { "count": len(rows), "items": rows }
    except Exception as e:
        print('Error: ', e)
        return None

def get_items(item):
    try:
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute('select * from items where item=?', (item))
        rows = c.fetchall()
        return { "count": len(rows), "items": rows }
    except Exception as e:
        print('Error: ', e)
        return None

def update(item, status, actiontime, repeatcount):
    try:
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        _actiondatetime = datetime.strptime(actiontime, "%Y-%m-%d %H:%M:%S")
        c.execute(updatequery, (status, _actiondatetime, repeatcount, item))
        conn.commit()
        return {"item": item, "status": status, "actiontime": actiontime, "repeatcount": repeatcount}
    except Exception as e:
        print('Error: ', e)
        return None

def delete(item):
    try:
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute(deletequery, (item,))
        conn.commit()
        return {"item": item}
    except Exception as e:
        print('Error: ', e)
        return None