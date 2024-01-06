
#from aiogram import Bot, Dispatcher, types
#from aiogram import executor
#from weather_parser import all_parse_weather
#from dotenv import load_dotenv
#import os
#
#load_dotenv()
#bot=Bot(os.getenv('TOKEN'))
#dp=Dispatcher(bot)
#
#HELP_COMMAND = '''
#<b>/help</b> - <em>список команд</em>
#
#<em>Чтобы узнать погоду </em>
#<em>напиши город ниже</em>
#'''
#
#
#async def on_startup(_):
#  print('Бот успешно запущен')
#
#
#async def on_shutdown(_):
#  print('Бот остановлен')
#
#
#@dp.message_handler(commands=['start'])
#async def command_start(message: types.message):
#  await message.answer(text=f'Привет, <b>{message.from_user.username}</b>!👋',
#                       parse_mode="HTML")
#  await message.answer(text=f'Вот, что я могу: {HELP_COMMAND}',
#                       parse_mode="HTML")
#
#
#@dp.message_handler(commands=['help'])
#async def command_help(message: types.message):
#  await message.answer(text=f'Вот, что я могу: {HELP_COMMAND}',
#                       parse_mode="HTML")
#
#
#@dp.message_handler()
#async def command_any(message: types.Message):
#  town = (message.text).capitalize()
#  weather_info = all_parse_weather(town)
#  await message.answer(text=weather_info)
#
#if __name__ == '__main__':
#  executor.start_polling(dp,
#                         skip_updates=True,
#                         on_startup=on_startup,
#                         on_shutdown=on_shutdown)
#
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
