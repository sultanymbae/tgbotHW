from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import bot, dp
from keyboards.client_kb import start_markup
from database.bot_db import sql_command_random
from parser.flashlight import ParserFlashlight


async def start_handler(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text=f"Салам хозяин {message.from_user.first_name}",
                           reply_markup=start_markup)


async def quiz_1(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton("NEXT", callback_data="button_call_1")
    markup.add(button_call_1)

    question = "Сколько лет Месси?"
    answers = [
        '44',
        '40',
        '35',
        '55',
        '69',
    ]

    await bot.send_poll(
        chat_id=message.from_user.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=2,
        explanation="Ок",
        open_period=5,
        reply_markup=markup
    )


async def get_random_user(message: types.Message):
    await sql_command_random(message)

async def get_flashlight(message: types.Message):
    flashlight = ParserFlashlight.parser()
    for i in flashlight:
        await message.answer(
            f"{i['link']}\n"
            f"{i['title']}\n"
            f"{i['price']} грн"
        )

def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(start_handler, commands=['start', 'help'])
    dp.register_message_handler(quiz_1, commands=['quiz'])
    dp.register_message_handler(get_random_user, commands=['get'])
    dp.register_message_handler(get_flashlight, commands=['flashlight'])