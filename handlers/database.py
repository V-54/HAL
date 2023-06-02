import sqlite3 as sq

def create_user_db():
    with sq.connect("User_sttings.db") as con:
        con.execute("""CREATE TABLE username
                       (name TEXT NOT NULL);""")
        con.close()

def user_settings():
    con

    con.commit()
    con.close()
