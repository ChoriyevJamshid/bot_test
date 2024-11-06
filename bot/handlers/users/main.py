from aiogram import types
from aiogram.fsm.context import FSMContext

from bot import utils
from bot.keyboards import inline

async def start_handler(message: types.Message, state: FSMContext):
    user = await utils.get_user(message.chat)
    print(f"{user = }")
    await message.answer("Hello world")


async def start2_handler(message: types.Message, state: FSMContext):
    await message.answer("Hello world 2")


async def users_handler(message: types.Message, state: FSMContext):

    text = "Barcha userlar ro'yhati"
    users = await utils.get_users()
    page_index = 0
    paginate_by = 5

    total_users = len(users)
    total = (page_index + 1) * paginate_by
    if total > len(users):
        total = len(users)
    users = users[page_index * paginate_by: total]


    markup = await inline.get_users_markup(users, page_index, total_users, paginate_by)
    await message.answer(text, reply_markup=markup)
















