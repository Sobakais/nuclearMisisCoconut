from aiogram import Router, F
from commands.com_handlers import start, help


router = Router()
router.message.filter(F.text.startswith("/"))
router.include_routers(start.router, help.router)
