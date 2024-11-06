from aiogram import types
from aiogram.fsm.context import FSMContext

from bot import utils
from bot.keyboards import inline


async def detail_user_callback(callback: types.CallbackQuery, state: FSMContext):
    user_id = int(callback.data.split('_')[-1])

    print(f"{user_id = }")
    telegram_user = await utils.get_telegram_user(user_id)

    text = (f"Chat ID: {telegram_user.chat_id}"
            f"\nUsername: {telegram_user.username}"
            f"\nFirst Name: {telegram_user.first_name}"
            f"\nLast Name: {telegram_user.last_name}"
            f"\nJoin Date: {telegram_user.created_at.date()}")

    await callback.message.answer(text)
    return await callback.answer()



async def paginate_users_callback(callback: types.CallbackQuery, state: FSMContext):

    page_index = int(callback.data.split('_')[-1])
    print(page_index)
    paginate_by = 5
    users = await utils.get_users()

    total_users = len(users)
    total = (page_index + 1) * paginate_by
    if total > len(users):
        total = len(users)
    users = users[page_index * paginate_by: total]

    text = "Barcha userlar ro'yhati"
    markup = await inline.get_users_markup(users, page_index, total_users, paginate_by)
    await callback.message.edit_text(text, reply_markup=markup)



