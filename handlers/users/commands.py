from telebot.types import Message
from data.loader import bot

from keyboards.default import main_buttons

@bot.message_handler(commands=["start"])
def start(message: Message):
    chat_id = message.chat.id
    text = (f"Assalomu alaykum FN30 gruhining Kutubxona botiga xush kelibsiz\n"
            f"Registratsiyadan o'ting!\n")
    bot.send_message(chat_id, text)
    bot.send_message(chat_id, "Ismingizni kiriting:")