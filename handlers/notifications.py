import aioschedule
from aiogram import types, Dispatcher
from config import bot
import asyncio


async def get_chat_id(message: types.Message):
    global chat_id
    chat_id = message.from_user.id
    await message.answer("OkOk")


async def wake_up():
    await bot.send_message(chat_id=chat_id, text="Ержан вставай")


async def scheduler():
    aioschedule.every().sunday.at("07:00").do(wake_up)

    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(3)


def register_handlers_notification(dp: Dispatcher):
    dp.register_message_handler(get_chat_id,
                                lambda word: 'че там' in word.text)