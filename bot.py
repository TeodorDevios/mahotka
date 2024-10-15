from config import dp, bot
from commands import *

import asyncio
import logging

logging.basicConfig(level=logging.INFO)


for _ in all_routers:
    dp.include_router(_)


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())

