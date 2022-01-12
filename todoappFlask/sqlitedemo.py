import sqlite3

conn = sqlite3.connect('todoapp.db')

c = conn.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS items (
            name TEXT,
            status TEXT,
            createdtime DATE,
            actiontime DATE,
            repeatperdaycount INTEGER
            )""")
conn.commit()

insertQuery = """INSERT INTO items
    VALUES (?, ?, ?, ?, ?);"""
# c.execute(insertQuery, ('walk2', 'Not Started', '2026-01-02 10:20:05.123', '2026-01-01 10:20:05.123', 2))
conn.commit()
c.execute("select * from items")

sql = """UPDATE items
                SET status=?,
                    actiontime=?,
                    repeatperdaycount=?
                WHERE name=? """
print(c.fetchall())

conn.close()