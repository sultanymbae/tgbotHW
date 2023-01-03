from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

start_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True,
    row_width=3
)

start_button = KeyboardButton("/start")
quiz_button = KeyboardButton("/quiz")
flash_button = KeyboardButton("/flashlight")
start_markup.add(start_button, quiz_button, flash_button)

cancel_button = KeyboardButton('Отменить регистрацию')
cancel_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True
).add(cancel_button)

backend_button = KeyboardButton('Backend')
frontend_button = KeyboardButton('Frontend')
ux_ui_button = KeyboardButton('UX/UI')
android_button = KeyboardButton('Android')
ios_button = KeyboardButton('IOS')
courses_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True,
    row_width=3,
).add(backend_button, frontend_button, ux_ui_button, android_button, ios_button)

submit_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True
).add(KeyboardButton('Да'), KeyboardButton('Нет'))