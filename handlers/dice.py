import time
import random

import threading

from create_bot import bot
from Data import data

# чтобы пользователь не мог постоянно вызывать функцию, которая уже исполняется
# был добавлен механизм блокировки ответа на сообщение 
# пока команда не завершится
lock = threading.Lock()

def roll_dice(message):
    bot.delete_message(message.chat.id, message.message_id)
    bot.send_message(message.chat.id,'Wait please...')
    number = int(message.text[1])
    if len(message.text) ==5:
        dice_facet=int(message.text[3]+message.text[4])
    else:
        dice_facet=int(message.text[3])
    i=0
    try:
        while i < number:
            bot.send_chat_action(message.chat.id, 'typing')
            lock.locked()
            i+=1
            roll_dice=str(random.randint(1,dice_facet))
            bot.send_message(message.chat.id,
                    str(i)+f'{data.TEXT_RD}{dice_facet} =  {roll_dice}')
        lock.release()
    except:
        #чтобы не было ошибок при спаме
         # бот ждет, пока прошлая команда завершится
        time.sleep(5)

def register_handlesrs_dice(bot):
    bot.register_message_handler(roll_dice, commands = ['1d4','2d4','3d4','4d4','5d4','6d4',
                                                        '1d6','2d6','3d6','4d6','5d6','6d6',
                                                        '1d8','2d8','3d8','4d8','5d8','6d8',
                                                        '1d10','2d10','3d10','4d10','5d10','6d10',
                                                        '1d12','2d12','3d12','4d12','5d12','6d12',
                                                        '1d20','2d20','3d20','4d20','5d20','6d20'])
    #bot.register_message_handler(, commands = [''])
