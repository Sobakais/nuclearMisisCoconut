import asyncio
import config as cfg
from aiogram import Bot, Dispatcher
from commands import cmds, pht


async def main():
    bot = Bot(token=cfg.API_TOKEN)
    dp = Dispatcher()


    dp.include_routers(cmds.router, pht.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
