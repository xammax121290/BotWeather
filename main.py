
from aiogram import Bot, Dispatcher, types, executor
from config import BOT_TOKEN
import requests
from bs4 import BeautifulSoup

bot=Bot(BOT_TOKEN)
dp=Dispatcher(bot)

#HELP_COMMAND = '''
#<b>/help</b> - <em>список команд</em>
#<b>/start</b> - <em>начать работу с ботом</em>
#'''


async def on_startup(_):
    print('Бот успешно запущен')

async def on_shutdown(_):
  print('Бот остановлен')


@dp.message_handler(commands=['start'])
async def command_start(message: types.Message):
    await message.answer(text='привет')

@dp.message_handler(commands=['weather'])
async def command_weather(message: types.Message):
    await message.answer(text='Чтобы узнать погоду, укажи город')


@dp.message_handler()
async def command_any(message: types.Message):
    city = (message.text).capitalize()



    link = f"https://www.google.com/search?q=погода+в+{city}"

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }
    response = requests.get(link, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        temperature = soup.select("#wob_tm")[0].getText()
        title = soup.select("#wob_dc")[0].getText()
        humidity = soup.select("#wob_hm")[0].getText()
        time = soup.select("#wob_dts")[0].getText()
        wind = soup.select("#wob_ws")[0].getText()

        weather_info = (
            f"Погода в городе {city}:\n"
            #f"Время: {time}\n"
            #f"Состояние: {title}\n"
            f"Температура: {temperature}C\n"
            #f"Влажность: {humidity}\n"
            #f"Ветер: {wind}"
        )
        await message.answer(text=weather_info)
    else:
        await message.answer(text=f"Не удалось получить данные о погоде в городе {city}")



if __name__=='__main__':
    executor.start_polling(dp, skip_updates=True,
                           on_startup=on_startup,
                           on_shutdown=on_shutdown)