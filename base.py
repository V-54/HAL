import pymysql
import wikipedia, re

from create_bot import bot
from Data import config, data

user_language = 'en'
#user_language = 'ru'

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

    def check_user_language(message):
        global user_language
        telegram_id = message.chat.id
        with connection.cursor() as cursor:
            cursor.execute(f"SELECT language FROM users WHERE telegram_id = {telegram_id}")
            result = cursor.fetchone()
            if result:
                user_language = result[0]
                wikipedia.set_lang(user_language)
                return user_language
            else:
                user_language = 'en' # default language
                wikipedia.set_lang(user_language)
                return user_language

    def change_user_language(message, laguage):
        global user_language
        user_language = laguage
        telegram_id = message.chat.id
        with connection.cursor() as cursor:
            cursor.execute(f"UPDATE users SET language = '{laguage}' WHERE telegram_id = {telegram_id}")
            wikipedia.set_lang(user_language)
            connection.commit()

    def getwiki(s):
        try:
            ny = wikipedia.page(s)
            wikitext=ny.content[:1000]
            wikimas=wikitext.split('.')
            wikimas = wikimas[:-1]
            wikitext2 = ''
            for x in wikimas:
                if not('==' in x):
                    if(len((x.strip()))>3):
                       wikitext2=wikitext2+x+'.'
                else:
                    break
            wikitext2=re.sub('\([^()]*\)', '', wikitext2)
            wikitext2=re.sub('\([^()]*\)', '', wikitext2)
            wikitext2=re.sub('\{[^\{\}]*\}', '', wikitext2)
            return wikitext2
        except Exception as e:
            return data.TEXT_UNKNOWN

    def register_handlesrs_wiki(bot):
        bot.register_message_handler(unknown_messages,func=lambda call: True)
        #bot.register_message_handler(, commands = [''])       

except Exception as error:
    print("ERROR DB!")
    print(error)

def unknown_messages(message):
    check_user_language(message)
    bot.send_chat_action(message.chat.id, 'typing')
    bot.send_message(message.chat.id, getwiki(message.text))