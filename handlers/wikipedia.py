import wikipedia, re

from create_bot import bot
from Data import data

wikipedia.set_lang("ru")
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

def unknown_messages(message):
    bot.send_chat_action(message.chat.id, 'typing')
    bot.send_message(message.chat.id, getwiki(message.text))

def register_handlesrs_wiki(bot):
    bot.register_message_handler(unknown_messages,func=lambda call: True)
    #bot.register_message_handler(, commands = [''])
