from telebot.types import Message
from data.loader import bot


@bot.message_handler(commands=["start"])
def start(message: Message):
    chat_id = message.chat.id
    text = (f"Assalomu alaykum FN30 gruhining Kutubxona botiga xush kelibsiz\n"
            f"Kitoblar toplamlari:")
    bot.send_message(chat_id, text)