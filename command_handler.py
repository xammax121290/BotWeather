from aiogram import types
from weather_parser import all_parse_weather

class CommandHandler:
    def __init__(self, bot, dp):
        self.bot = bot
        self.dp = dp
        self.help_command = '''
<b>/help</b> - <em>список команд</em>

<em>Чтобы узнать погоду </em>
<em>напиши город ниже</em>
'''

    async def on_startup(self, _):
        print('Бот успешно запущен')

    async def on_shutdown(self, _):
        print('Бот остановлен')

    async def command_start(self, message: types.Message):
        await message.answer(text=f'Привет, <b>{message.from_user.username}</b>!👋',
                             parse_mode="HTML")
        await message.answer(text=f'Вот, что я могу: {self.help_command}',
                             parse_mode="HTML")

    async def command_help(self, message: types.Message):
        await message.answer(text=f'Вот, что я могу: {self.help_command}',
                             parse_mode="HTML")

    async def command_any(self, message: types.Message):
        town = (message.text).capitalize()
        weather_info = all_parse_weather(town)
        await message.answer(text=weather_info)