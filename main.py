from aiogram import Bot, Dispatcher, executor, types
from dotenv import load_dotenv
from command_handler import CommandHandler
import os

load_dotenv()
bot = Bot(os.getenv('TOKEN'))
dp = Dispatcher(bot)

command_handler = CommandHandler(bot, dp)

@dp.message_handler(commands=['start'])
async def handle_start(message: types.Message):
    await command_handler.command_start(message)

@dp.message_handler(commands=['help'])
async def handle_help(message: types.Message):
    await command_handler.command_help(message)

@dp.message_handler()
async def handle_any(message: types.Message):
    await command_handler.command_any(message)

if __name__ == '__main__':
    executor.start_polling(dp,
                           skip_updates=True,
                           on_startup=command_handler.on_startup,
                           on_shutdown=command_handler.on_shutdown)
