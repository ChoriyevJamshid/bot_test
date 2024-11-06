from aiogram import Router, F
from aiogram.filters import CommandStart, Command

from bot.handlers.users.main import *
from bot.handlers.users.callback_handlers import *


def prepare_router() -> Router:

    router = Router()
    router.message.filter(F.chat.type == "private")

    # message handlers
    router.message.register(start_handler, CommandStart())
    router.message.register(users_handler, Command('users'))

    # callback handlers
    router.callback_query.register(detail_user_callback, F.data.startswith("users"))
    router.callback_query.register(paginate_users_callback, F.data.startswith("paginate"))

    return router
