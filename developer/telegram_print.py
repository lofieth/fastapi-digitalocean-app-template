import asyncio

from telegram import Bot


def telegram_print(text):
    if not text:
        return

    asyncio.run(send_message(text))


# Create a Telegram Bot:
# Open Telegram and search for the "BotFather" bot.
# Start a chat with BotFather and use the /newbot command to create a new bot.

# Get Chat ID:
# Send the /my_id to telegram bot @get_id_bot.
# To get group chat ID, first add the bot to the group, then send /my_id in the group.


async def send_message(text):
    token = ""
    chat_id = ""

    bot = Bot(token)
    await bot.send_message(chat_id, text)

    # time.sleep(1)
