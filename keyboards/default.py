from telebot.types import KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove


def main_buttons():
    markup = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    btn1 = KeyboardButton("📚 maktab darsliklari")
    btn2 = KeyboardButton("📚 badiiy adabiyotlar")
    btn3 = KeyboardButton("🌐 IT course")
    btn4 = KeyboardButton("📚 IELTS course")
    markup.add(btn1, btn2, btn3, btn4)
    return markup