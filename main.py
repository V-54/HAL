from create_bot import bot
from handlers import client, dice, admin, keyboards
import base

def main():
    print('Hal starting')
#    base.create_user_db()
    dice.register_handlesrs_dice(bot)
    admin.register_handlesrs_admin(bot)
    client.register_handlesrs_client(bot)
    keyboards.register_keyboards(bot)
    base.register_handlesrs_wiki(bot)

    bot.polling(none_stop=True, interval=0)

if __name__ == "__main__":
    main()
