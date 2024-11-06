from aiogram.types import Chat, User

from common.models import TelegramProfile


async def get_user(chat: Chat | User):
    if TelegramProfile.objects.filter(chat_id=chat.id).exists():
        return TelegramProfile.objects.filter(chat_id=chat.id).first()

    return TelegramProfile.objects.create(
        chat_id=chat.id,
        first_name=chat.first_name,
        last_name=chat.last_name,
        username=chat.username
    )


async def get_users():
    return TelegramProfile.objects.all()


async def get_telegram_user(user_id: int):
    return TelegramProfile.objects.filter(id=user_id).first()












