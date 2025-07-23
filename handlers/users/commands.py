from telebot.types import Message, ReplyKeyboardRemove
from database.dbase import Database
from keyboards import default
from data.loader import bot, REGISTER

from keyboards.default import main_buttons

db = Database()

@bot.message_handler(commands=['start'])
def start(message: Message):
    chat_id = message.chat.id
    login = message.from_user.full_name
    from_user_id = message.from_user.id

    if not db.get_user(from_user_id):
        db.insert_telegram_id(from_user_id)
    else:
        if None in db.get_user(from_user_id):
            text = (f"Assalomu alaykum {login} FN30 gruhining Kutubxona botiga xush kelibsiz\n"
                    f"Registratsiyadan o'ting!\nLogin kiriting:")
            msg = bot.send_message(chat_id, text)
            bot.register_next_step_handler(msg, get_name)
        else:
            bot.send_message(chat_id, "Tugmalardan birini tanlang", reply_markup=default.main_buttons())

def get_name(message: Message):
    chat_id = message.chat.id
    from_user_id = message.from_user.id

    login = message.text
    REGISTER[from_user_id] = {
        "login": login
    }

    msg = bot.send_message(chat_id, "Parol kiriting:")
    bot.register_next_step_handler(msg, get_password)

def get_password(message: Message):
    chat_id = message.chat.id
    from_user_id = message.from_user.id
    password = message.text
    login = REGISTER[from_user_id]['login']
    db.update_user(from_user_id, login, password)
    bot.send_message(chat_id, "Tabriklaymiz siz ro'yxatdan o'tdiz!!!",
                     reply_markup=ReplyKeyboardRemove())
    bot.send_message(chat_id, "Tugmalardan birini tanlang!", reply_markup=main_buttons())