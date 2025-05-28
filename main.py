import logging
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.fsm.storage.memory import MemoryStorage
from dotenv import load_dotenv
import os

# .env fayldan TOKEN ni yuklash
load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

# Loglarni sozlash
logging.basicConfig(level=logging.INFO)

# Bot va dispatcher
bot = Bot(token=BOT_TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher(storage=MemoryStorage())

# /start komandasi
@dp.message(CommandStart())
async def start_handler(message: Message):
    await message.answer("Assalomu alaykum! 🍗 Oltin Juja botga xush kelibsiz!")

# Botni ishga tushurish
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
