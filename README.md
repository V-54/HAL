## HAL 5500

### Description

HAL 5500 is a Telegram bot that can perform various tasks such as searching for information on Wikipedia, rolling dice, sending images and stickers, and providing information about the creator of the bot.

## INSTALLATION

To install the necessary packages, run the following command:

```
pip install -r requirements.txt
```

Then, create a new bot in Telegram and obtain the API token. Add the token and your admin chat ID to the `config.py` file located in the `Data/` directory.
*(you need to create a config.py file)*

```
# you bot token from @BotFather
TOKEN = 'you bot token'

# that bot version using MySQL db for working
MySQL_db_name='HALmemory'
MySQL_db_user='root'
MySQL_db_password='you_password'

# you ID
admin_chat_id = 123456789
```

To start the bot, run the following command:

```
python3 main.py
```
**if you see a message in the console**
> HAL starting

So the bot listens for incoming messages and responds accordingly.

### Features

- **Search for text from posts in the Wikipedia database and respond with short excerpts from articles.**

- **Roll dice with different number of faces (4, 6, 8, 10, 12, and 20)** 
    **With the ability to roll several dice at once (from 1 to 6)** - /dice

- **Send animated stickers with mini games** - /anima

- **Send images and GIF animations** - /picture

- **Send links to Internet sources** - /link

- **Send stickers** - /stiker

- **Display information about the creator of the bot** - /about