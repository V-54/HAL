#import sqlite3 as sql
#import mysql.connector as sql
import pymysql
from Data import config 


try:
    #connection = pymysql.connect("Data/uesrs.db")
    connection = pymysql.connect(
    host="localhost",
    user=config.MySQL_db_user,
    password=config.MySQL_db_password,
    db="Data/users_db"
    )

    def create_users_table():
        with connection.cursor() as cursor:
            create_table_query = """CREATE TABLE IF NOT EXISTS users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            full_name TEXT,
            name TEXT DEFAULT '@none',
            telegram_id INT,
            language TEXT DEFAULT 'en'
            )"""
            cursor.execute(create_table_query)
            connection.commit()
            print("DB CREATED")

    def add_user(full_name,name,telegram_id,language):
        with connection.cursor() as cursor:
            query = f"INSERT INTO users (full_name, name, telegram_id, language) VALUE ('{full_name}', '{name}', {telegram_id}, '{language}')"            #cursor.execute(query, (full_name,name,telegram_id,language))
            cursor.execute(query)

        connection.commit()
except Exception as error:
    print("ERROR DB!")
    print(error)

#def add_user(full_name,name,telegram_id,language):
#    query = f"INSERT INTO users (full_name, name, telegram_id, language) VALUE ({full_name}, {name}, {telegram_id}, {language})"
#    cursor.execute(query, (full_name,name,telegram_id,language))
#    conn.commit()
#    conn.close()


#cursor.execute("""CREATE TABLE IF NOT EXISTS users(
#    id INTEGER PRIMARY KEY,
#    full_name TEXT,
#    name TEXT DEFAULT '@none',
#    telegram_id INTEGER,
#    language TEXT DEFAULT 'en'
#    )""")
