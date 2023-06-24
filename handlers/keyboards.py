from telebot import types

from create_bot import bot
from Data import data
from base import check_user_language

def main_keyboard_set(message):
    bot.delete_message(message.chat.id, message.message_id)
    main_keyboard=types.ReplyKeyboardMarkup(resize_keyboard=True)
    dice_btn = types.KeyboardButton('/dice')
    anima_btn = types.KeyboardButton('/anima')
    picture_btn = types.KeyboardButton('/picture')
    link_btn = types.KeyboardButton('/link')
    sticker_btn = types.KeyboardButton('/sticker')
    settings_btn = types.KeyboardButton('/settings')
    main_keyboard.add(dice_btn,anima_btn,picture_btn,link_btn,
                      sticker_btn,settings_btn)
    bot.send_message(message.chat.id,data.TEXT_ASK,reply_markup=main_keyboard)

def anima_list(message):
    bot.delete_message(message.chat.id, message.message_id)
    bot.send_message(message.chat.id,data.TEXT_ANIMA)
    anima_keyboard=types.ReplyKeyboardMarkup(resize_keyboard=True)
    andice_btn=types.KeyboardButton('/andice')
    anslot_btn=types.KeyboardButton('/anslot')
    anbowling_btn=types.KeyboardButton('/anbowling')
    andart_btn=types.KeyboardButton('/andart')
    back_btn=types.KeyboardButton('/Main_Menu')
    anima_keyboard.add(andice_btn,anslot_btn,anbowling_btn,andart_btn,back_btn)
    bot.send_message(message.chat.id, data.TEXT_ASK,reply_markup=anima_keyboard)

def send_picture(message):
    bot.delete_message(message.chat.id, message.message_id)
    pictire_list_markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
    send_picture_btn=types.KeyboardButton('/creation')
    send_gif_btn=types.KeyboardButton('/generator')
    back_btn=types.KeyboardButton('/Main_Menu')
    pictire_list_markup.add(send_picture_btn,send_gif_btn,back_btn)
    bot.send_message(message.chat.id,
            data.TEXT_LINK,reply_markup=pictire_list_markup)

def send_link(message):
    bot.delete_message(message.chat.id, message.message_id)
    link_list_markup=types.InlineKeyboardMarkup()
    send_link_picture_btn=types.InlineKeyboardButton('сreation image',
            url=data.URL_PICTURE)
    send_link_gif_btn=types.InlineKeyboardButton('manul generator',
            url=data.URL_GIF)
    link_list_markup.add(send_link_picture_btn,send_link_gif_btn)
    bot.send_message(message.chat.id,data.TEXT_PICTURE_COMMENT,
            reply_markup=link_list_markup)
    
#___________DICES______________________

def dices(message):
    #bot.delete_message(message.chat.id, message.message_id)
    dice_keyboard=types.ReplyKeyboardMarkup(resize_keyboard=True)
    d4=types.KeyboardButton('/rd4')
    d6=types.KeyboardButton('/rd6')
    d8=types.KeyboardButton('/rd8')
    d10=types.KeyboardButton('/rd10')
    d12=types.KeyboardButton('/rd12')
    d20=types.KeyboardButton('/rd20')
    back_btn=types.KeyboardButton('/Main_Menu')
    dice_keyboard.add(d4,d6,d8,d10,d12,d20,back_btn)
    bot.send_message(message.chat.id,data.TEXT_DICE)
    bot.send_message(message.chat.id,data.TEXT_ASK,reply_markup=dice_keyboard)

def roll_dice_4(message):
    bot.delete_message(message.chat.id, message.message_id)
    bot.send_message(message.chat.id,data.TEXT_RD4_LIST)
    d4_keyboard=types.ReplyKeyboardMarkup(resize_keyboard=True)
    c1_d4=types.KeyboardButton('/1d4')
    c2_d4=types.KeyboardButton('/2d4')
    c3_d4=types.KeyboardButton('/3d4')
    c4_d4=types.KeyboardButton('/4d4')
    c5_d4=types.KeyboardButton('/5d4')
    c6_d4=types.KeyboardButton('/6d4')
    back_btn=types.KeyboardButton('/Main_Menu')
    dice_list=types.KeyboardButton('/dice')
    d4_keyboard.add(c1_d4,c2_d4,c3_d4,c4_d4,c5_d4,c6_d4,dice_list,back_btn)
    bot.send_message(message.chat.id, data.TEXT_ASK,reply_markup=d4_keyboard)

def roll_dice_6(message):
    bot.delete_message(message.chat.id, message.message_id)
    bot.send_message(message.chat.id,data.TEXT_RD6_LIST)
    d6_keyboard=types.ReplyKeyboardMarkup(resize_keyboard=True)
    c1_d6=types.KeyboardButton('/1d6')
    c2_d6=types.KeyboardButton('/2d6')
    c3_d6=types.KeyboardButton('/3d6')
    c4_d6=types.KeyboardButton('/4d6')
    c5_d6=types.KeyboardButton('/5d6')
    c6_d6=types.KeyboardButton('/6d6')
    back_btn=types.KeyboardButton('/Main_Menu')
    dice_list=types.KeyboardButton('/dice')
    d6_keyboard.add(c1_d6,c2_d6,c3_d6,c4_d6,c5_d6,c6_d6,dice_list,back_btn)
    bot.send_message(message.chat.id, data.TEXT_ASK,reply_markup=d6_keyboard)

def roll_dice_8(message):
    bot.delete_message(message.chat.id, message.message_id)
    bot.send_message(message.chat.id,data.TEXT_RD8_LIST)
    d8_keyboard=types.ReplyKeyboardMarkup(resize_keyboard=True)
    c1_d8=types.KeyboardButton('/1d8')
    c2_d8=types.KeyboardButton('/2d8')
    c3_d8=types.KeyboardButton('/3d8')
    c4_d8=types.KeyboardButton('/4d8')
    c5_d8=types.KeyboardButton('/5d8')
    c6_d8=types.KeyboardButton('/6d8')
    back_btn=types.KeyboardButton('/Main_Menu')
    dice_list=types.KeyboardButton('/dice')
    d8_keyboard.add(c1_d8,c2_d8,c3_d8,c4_d8,c5_d8,c6_d8,dice_list,back_btn)
    bot.send_message(message.chat.id, data.TEXT_ASK,reply_markup=d8_keyboard)

def roll_dice_10(message):
    bot.delete_message(message.chat.id, message.message_id)
    bot.send_message(message.chat.id,data.TEXT_RD10_LIST)
    d10_keyboard=types.ReplyKeyboardMarkup(resize_keyboard=True)
    c1_d10=types.KeyboardButton('/1d10')
    c2_d10=types.KeyboardButton('/2d10')
    c3_d10=types.KeyboardButton('/3d10')
    c4_d10=types.KeyboardButton('/4d10')
    c5_d10=types.KeyboardButton('/5d10')
    c6_d10=types.KeyboardButton('/6d10')
    back_btn=types.KeyboardButton('/Main_Menu')
    dice_list=types.KeyboardButton('/dice')
    d10_keyboard.add(c1_d10,c2_d10,c3_d10,c4_d10,c5_d10,c6_d10,dice_list,back_btn)
    bot.send_message(message.chat.id, data.TEXT_ASK,reply_markup=d10_keyboard)

def roll_dice_12(message):
    bot.delete_message(message.chat.id, message.message_id)
    bot.send_message(message.chat.id,data.TEXT_RD12_LIST)
    d12_keyboard=types.ReplyKeyboardMarkup(resize_keyboard=True)
    c1_d12=types.KeyboardButton('/1d12')
    c2_d12=types.KeyboardButton('/2d12')
    c3_d12=types.KeyboardButton('/3d12')
    c4_d12=types.KeyboardButton('/4d12')
    c5_d12=types.KeyboardButton('/5d12')
    c6_d12=types.KeyboardButton('/6d12')
    back_btn=types.KeyboardButton('/Main_Menu')
    dice_list=types.KeyboardButton('/dice')
    d12_keyboard.add(c1_d12,c2_d12,c3_d12,c4_d12,c5_d12,c6_d12,dice_list,back_btn)
    bot.send_message(message.chat.id, data.TEXT_ASK,reply_markup=d12_keyboard)

def roll_dice_20(message):
    bot.delete_message(message.chat.id, message.message_id)
    bot.send_message(message.chat.id,data.TEXT_RD20_LIST)
    d20_keyboard=types.ReplyKeyboardMarkup(resize_keyboard=True)
    c1_d20=types.KeyboardButton('/1d20')
    c2_d20=types.KeyboardButton('/2d20')
    c3_d20=types.KeyboardButton('/3d20')
    c4_d20=types.KeyboardButton('/4d20')
    c5_d20=types.KeyboardButton('/5d20')
    c6_d20=types.KeyboardButton('/6d20')
    back_btn=types.KeyboardButton('/Main_Menu')
    dice_list=types.KeyboardButton('/dice')
    d20_keyboard.add(c1_d20,c2_d20,c3_d20,c4_d20,c5_d20,c6_d20,dice_list,back_btn)
    bot.send_message(message.chat.id, data.TEXT_ASK,reply_markup=d20_keyboard)

#___________SETTINGS______________________
def settings(message):
    bot.delete_message(message.chat.id, message.message_id)
    settings_keayboard=types.ReplyKeyboardMarkup(resize_keyboard=True)
    admin_btn=types.KeyboardButton('/admin')
    language_btn=types.KeyboardButton('/language')
    update_btn=types.KeyboardButton('/update')
    about_btn=types.KeyboardButton('/about')
    back_btn=types.KeyboardButton('/Main_Menu')
    settings_keayboard.add(update_btn,language_btn,admin_btn,about_btn,back_btn)
    bot.send_message(message.chat.id, data.TEXT_SETTINGS,reply_markup=settings_keayboard)

def language_keyboard_set(message):
    bot.delete_message(message.chat.id, message.message_id)
    bot.send_message(message.chat.id,f"Now wikipedia language is {check_user_language(message)}")
    language_keayboard=types.ReplyKeyboardMarkup(resize_keyboard=True)
    Ru_language_btn=types.KeyboardButton('/RU')
    En_language_btn=types.KeyboardButton('/EN')
    settings_btn=types.KeyboardButton('/settings')
    back_btn=types.KeyboardButton('/Main_Menu')
    language_keayboard.add(Ru_language_btn,En_language_btn,settings_btn,back_btn)
    bot.send_message(message.chat.id,f"Do you want to chang it?",reply_markup=language_keayboard)

def register_keyboards(bot):
    bot.register_message_handler(main_keyboard_set, commands = ['Main_Menu'])
    bot.register_message_handler(anima_list, commands = ['anima'])
    bot.register_message_handler(send_picture, commands = ['picture'])
    bot.register_message_handler(send_link, commands = ['link'])
    bot.register_message_handler(dices, commands = ['dice'])
    bot.register_message_handler(roll_dice_4, commands = ['rd4'])
    bot.register_message_handler(roll_dice_6, commands = ['rd6'])
    bot.register_message_handler(roll_dice_8, commands = ['rd8'])
    bot.register_message_handler(roll_dice_10, commands = ['rd10'])
    bot.register_message_handler(roll_dice_12, commands = ['rd12'])
    bot.register_message_handler(roll_dice_20, commands = ['rd20'])
    bot.register_message_handler(settings, commands = ['settings'])
    bot.register_message_handler(language_keyboard_set, commands = ['language'])
    #bot.register_message_handler(, commands = [''])
