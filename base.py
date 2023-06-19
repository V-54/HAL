import pymysql
from Data import config 

user_language = 'en'
user_language = 'ru'

try:
    connection = pymysql.connect(
    host="localhost",
    user=config.MySQL_db_user,
    password=config.MySQL_db_password,
    database="HALmemory"
    )

    def add_user(full_name,name,telegram_id,language):
        with connection.cursor() as cursor:
            cursor.execute("SELECT COUNT(*) FROM users WHERE telegram_id = %s", (telegram_id,))
            result=cursor.fetchone()
            if result[0]==0:
                query = f"INSERT INTO users (name, full_name, telegram_id, language) VALUE ('{full_name}', '{name}', {telegram_id}, '{language}')"
                cursor.execute(query)
                connection.commit()
                print("User add in memory")
            else:
                print("I remember this user")

#    def check_user_language(message):
#        with connection.cursor() as cursor:
#            global user_language
#            telegram_id = message.chat.id
#            user_language = cursor.execute(f"SELECT language FROM users WHERE telegram_id = {telegram_id}")
#            print(user_language)
#            print(cursor.execute(f"SELECT language FROM users WHERE telegram_id = {telegram_id}"))

except Exception as error:
    print("ERROR DB!")
    print(error)