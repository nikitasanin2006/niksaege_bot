from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove
from create_bot import admins

def main_kb(user_telegram_id: int):
    kb_list = [
        [KeyboardButton(text="Контакты"), KeyboardButton(text="Настройки"), KeyboardButton(text="Сбросить настройки")]
    ]
    keyboard = ReplyKeyboardMarkup(keyboard=kb_list, resize_keyboard=True)
    return keyboard

def oobe_part_2():
    kb_list = [
        [KeyboardButton(text="8-9 класс"), KeyboardButton(text="10-11 класс")],
        [KeyboardButton(text="Студент")]
    ]
    keyboard = ReplyKeyboardMarkup(keyboard=kb_list, resize_keyboard=True, one_time_keyboard=True)
    return keyboard

def oobe_part_3():
    kb_list = [
        [KeyboardButton(text="Плохо, не думаю, что сдам"), KeyboardButton(text="Не знаю, сдам или нет")],
        [KeyboardButton(text="Уверен, что сдам, просто повторить")]
    ]
    keyboard = ReplyKeyboardMarkup(keyboard=kb_list, resize_keyboard=True, one_time_keyboard=True)
    return keyboard

def oobe_part_4():
    kb_list = [
        [KeyboardButton(text="Короткой (~2500 символов)"), KeyboardButton(text="Средней (~5000 символов)")],
        [KeyboardButton(text="Длинной (~10000 символов)")]
    ]
    keyboard = ReplyKeyboardMarkup(keyboard=kb_list, resize_keyboard=True, one_time_keyboard=True)
    return keyboard

def dialog():
    kb_list = [
        [KeyboardButton(text="Да"), KeyboardButton(text="Нет")]
    ]
    keyboard = ReplyKeyboardMarkup(keyboard=kb_list, resize_keyboard=True, one_time_keyboard=True)
    return keyboard

def delete_keyboard():
    keyboard = ReplyKeyboardRemove()
    return keyboard
