from telebot import types
import pyautogui
from loguru import logger

from create_bot import bot
from Data import data, config


logger.add('Log/admin.log', format = '{time} {message}')


def log_admin_success(message):
    logger.info(f'@{message.from_user.username} - admin access')
    bot.send_message(message.chat.id,data.TEXT_ADMIN_SUCCESS)

def log_admin_denied(message):
    logger.info(f'@{message.from_user.username} - access denied!')
    bot.send_message(message.chat.id,data.TEXT_ADMIN_DENIED +' Access denied')


def admin_chek(message):
    if message.chat.id == config.admin_chat_id:
        log_admin_success(message)
        admin_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        screen_btn=types.KeyboardButton('/screen')
        back_btn = types.KeyboardButton('/Main_Menu')
        admin_keyboard.add(screen_btn, back_btn)
        bot.send_message(message.chat.id,data.TEXT_ASK,reply_markup=admin_keyboard)
    else:
        log_admin_denied(message)

def send_screenshot(message):
    if message.chat.id == config.admin_chat_id:
        logger.info(f'@{message.from_user.username} - creen send')
        screenshot = pyautogui.screenshot()
        screenshot.save('Data/image/screenshot.png')
        with open('Data/image/screenshot.png', 'rb') as photo:
            bot.send_photo(message.chat.id, photo)
    else:
        log_admin_denied(message)

# данные для доступа к панели администратора лежат в файле 
# Data/config.py
# нужно изменить данные на свои, 
# чтобы бот выдал вам доступ к функционалу администратора

def register_handlesrs_admin(bot):
    bot.register_message_handler(send_screenshot, commands = ['screen'])
    bot.register_message_handler(admin_chek, commands = ['admin'])
    #bot.register_message_handler(, commands = [''])
