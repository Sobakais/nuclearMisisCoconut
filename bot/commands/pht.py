from aiogram import Router, F
from commands.photo_handlers import photo


router = Router()
router.message.filter(F.photo)
router.include_routers(photo.router)
