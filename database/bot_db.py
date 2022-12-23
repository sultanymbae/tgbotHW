import random
import sqlite3


def sql_create():
    global db, cursor
    db = sqlite3.connect("bot.sqlite3")
    cursor = db.cursor()

    if db:
        print("База данных подключена")

    db.execute("CREATE TABLE IF NOT EXISTS sultan"
               "(id INTEGER PRIMARY KEY, username TEXT, "
               "name TEXT, course TEXT, "
               "age INTEGER, group INTEGER)")
    db.commit()


async def sql_command_insert(state):
    async with state.proxy() as data:
        cursor.execute("INSERT INTO sultan VALUES "
                       "(?, ?, ?, ?, ?, ?)", tuple(data.values()))
        db.commit()


async def sql_command_random(message):
    result = cursor.execute("SELECT * FROM sultan").fetchall()
    random_user = random.choice(result)
    await message.answer(
        random_user[6],
        caption=f"{random_user[1]} {random_user[2]} {random_user[3]}"
                f"\n{random_user[4]} {random_user[5]} {random_user[0]}"
    )


async def sql_command_all():
    return cursor.execute("SELECT * FROM sultan").fetchall()


async def sql_command_delete():
    cursor.execute("DELETE FROM sultan WHERE id = ?", (user_id))
    db.commit()
