from aiogram.utils.keyboard import (
    InlineKeyboardBuilder,
    InlineKeyboardMarkup,
    InlineKeyboardButton
)
from django.db.models import QuerySet


async def get_users_markup(users: QuerySet, page_index: int, total_users: int, paginate_by: int = 5):

    builder = InlineKeyboardBuilder()
    for user in users:
        builder.add(
            InlineKeyboardButton(
                text=f"{user.username if user.username else user.first_name}",
                callback_data=f"users_{user.id}"
            )
        )

    total_page = total_users // paginate_by if total_users % paginate_by == 0 else total_users // paginate_by + 1
    pagination_builder = InlineKeyboardBuilder()
    if total_page > 1:
        if page_index > 0:
            pagination_builder.add(InlineKeyboardButton(text="⬅️", callback_data=f"paginate_{page_index - 1}"))

        pagination_builder.add(InlineKeyboardButton(text=f"{page_index + 1}", callback_data=f"paginate_{page_index}"))

        if page_index < total_page - 1:
            pagination_builder.add(InlineKeyboardButton(text="➡️", callback_data=f"paginate_{page_index + 1}"))

    builder.adjust(*(1,))
    pagination_builder.adjust(*(3,))
    builder.attach(pagination_builder)
    return builder.as_markup()
