from telebot import types
from loguru import logger

from create_bot import bot
from Data import data
import base

logger.add('Log/users.log', format = '{time}  {level}  {message}',level = 'DEBUG')

def start_message(message):
    bot.delete_message(message.chat.id, message.message_id)
    bot.send_message(message.chat.id,'🤖')
    starting_keyboard=types.ReplyKeyboardMarkup(resize_keyboard=True)
    #reg_button = types.KeyboardButton(text="Отправить номер телефона", 
    #request_contact=True)
    btn0=types.KeyboardButton('/Main_Menu')
    starting_keyboard.add(btn0)
    bot.send_message(message.chat.id,data.TEXT_START,
            reply_markup=starting_keyboard,parse_mode='html')
# сбор метрики пользователя (кто запустил бота) 
    logger.info(f'id {message.from_user.id} = {message.from_user.full_name} - @{message.from_user.username}')
   # base.add_user(message.from_user.full_name,message.from_user.username,message.message.chat.id,'ru')

def help(message):
    bot.delete_message(message.chat.id, message.message_id)
    bot.send_message(message.chat.id,data.TEXT_HELP,parse_mode='html')

def delete_message(message):
    bot.delete_message(message.chat.id, message.chat.id)
    if message.text == data.TEXT_ASK:
        bot.delete_message(message.chat.id, message.chat.id)
        print("delete")
    else:
        print("no delete")

def andice(message):
    bot.delete_message(message.chat.id, message.message_id)
    bot.send_dice(message.chat.id,data.TEXT_ANDICE)

def anslot(message):
    bot.delete_message(message.chat.id, message.message_id)
    bot.send_dice(message.chat.id,data.TEXT_ANSLOT)

def anbowling(message):
    bot.delete_message(message.chat.id, message.message_id)
    bot.send_dice(message.chat.id,data.TEXT_ANBOWLING)

def andart(message):
    bot.delete_message(message.chat.id, message.message_id)
    bot.send_dice(message.chat.id,data.TEXT_ANDART)

def picture_1(message):
    bot.delete_message(message.chat.id, message.message_id)
    bot.send_message(message.chat.id,data.TEXT_PICTURE_COMMENT)
    bot.send_photo(message.chat.id,open('Data/image/'+data.PICTURE_1,'rb'))

def gif_1(message):
    bot.delete_message(message.chat.id, message.message_id)
    bot.send_message(message.chat.id,data.TEXT_GIF_COMMENT)
    bot.send_animation(message.chat.id,open('Data/image/'+data.GIF_1,'rb'))

def send_sticker(message):
    bot.delete_message(message.chat.id, message.message_id)
    bot.send_sticker(message.chat.id,data.STICKER_ID)

def print_about(message):
    bot.delete_message(message.chat.id, message.message_id)
    bot.send_message(message.chat.id,'🐍')
    bot.send_message(message.chat.id,data.TEXT_CREATOR)

def update_message(message):
    bot.send_message(message.chat.id,f'hi {message.from_user.username}')
    bot.send_message(message.chat.id,data.TEXT_UPDATE,parse_mode = 'html')

def language(message):
    bot.send_message(message.chat.id,"eng")

def register_handlesrs_client(bot):
    bot.register_message_handler(start_message, commands = ['start'])
    bot.register_message_handler(help, commands = ['help'])
    bot.register_message_handler(andice, commands = ['andice'])
    bot.register_message_handler(anslot, commands = ['anslot'])
    bot.register_message_handler(anbowling, commands = ['anbowling'])
    bot.register_message_handler(andart, commands = ['andart'])
    bot.register_message_handler(picture_1, commands = ['creation'])
    bot.register_message_handler(gif_1, commands = ['generator'])
    bot.register_message_handler(send_sticker, commands = ['sticker'])
    bot.register_message_handler(print_about, commands = ['creator'])
    bot.register_message_handler(update_message, commands = ['update'])
    bot.register_message_handler(delete_message, commands = ['delete'])

    #bot.register_message_handler(, commands = [''])
