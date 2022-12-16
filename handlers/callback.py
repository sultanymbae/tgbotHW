from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import bot, dp

async def quiz_2(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton("NEXT 1", callback_data="button_call_1")
    markup.add(button_call_1)

    question = "Что хочет Луффи из аниме ВанПис"
    answers = [
        'стать королем пиратов',
        'стать адмиралом',
        'убить акайну',
        'любви',
        'стать хокаге',
    ]

    await bot.send_poll(
        chat_id=message.from_user.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=0,
        explanation="Смотри ВанПис",
        open_period=5,
        reply_markup=markup
    )

@dp.callback_query_handler(text="button_call_1")
async def quiz_3(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton("NEXT 2", callback_data="button_call_2")
    markup.add(button_call_1)

    question = "Кто убил Учиху Итачи"
    answers = [
        "Мадара",
        "Наруто",
        "Хаширама",
        "Саске",
        "Гатс",
        "Зоро",
    ]

    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=3,
        explanation="Позер получается ",
        open_period=5,
        reply_markup=markup
    )

def register_handlers_client(dp: Dispatcher):
    dp.register_callback_query_handler(quiz_2, text="button_call_2")
    dp.register_callback_query_handler(quiz_3, text="button_call_3")