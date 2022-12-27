from aiogram.utils import executor
from handlers import client, callback, extra, admin, fsm_mentors, notifications
from config import dp
import logging
from database.bot_db import sql_create
import asyncio

client.register_handlers_client(dp)
callback.register_handlers_client(dp)
admin.register_handlers_admin(dp)
fsm_mentors.register_handlers_fsm_mentor(dp)
notifications.register_handlers_notification(dp)

extra.register_handler_extra(dp)


async def on_startup(_):
    asyncio.create_task(notifications.scheduler())
    sql_create()

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)