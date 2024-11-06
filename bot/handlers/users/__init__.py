from aiogram import Router, F


def prepare_router() -> Router:

    router = Router()
    router.message.filter(F.chat.type == "private")

    return router
