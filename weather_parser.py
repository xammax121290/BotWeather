import requests
from bs4 import BeautifulSoup
from coordinates import City

def all_parse_weather(town):
    link = f"https://www.google.com/search?q=погода+в+{town}"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }
    response = requests.get(link, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    if soup.find("span", {"class": "wob_t", "id": "wob_tm"}):
        temperature = soup.select("#wob_tm")[0].getText()
        title = soup.select("#wob_dc")[0].getText()
        humidity = soup.select("#wob_hm")[0].getText()
        wind = soup.select("#wob_ws")[0].getText()

        weather_info = (
            f"Погода в городе {town}:\n"
            f"Состояние: {title}\n"
            f"Температура: {temperature}°C\n"
            f"Влажность: {humidity}\n"
            f"Ветер: {wind}"
        )
        return weather_info
    else:
        return f"Город {town} не найден. Проверьте правильность ввода"

def parse_weather(city_obj):
    try:
        city = city_obj.city
        link = f"https://www.google.com/search?q=погода+в+{city}"
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
        }
        response = requests.get(link, headers=headers)
        response.raise_for_status()  # Проверка на ошибки HTTP
        soup = BeautifulSoup(response.text, "html.parser")

        if soup.find("span", {"class": "wob_t", "id": "wob_tm"}):
            temperature = soup.select("#wob_tm")[0].getText()
            title = soup.select("#wob_dc")[0].getText()
            humidity = soup.select("#wob_hm")[0].getText()

            wind = soup.select("#wob_ws")[0].getText()

            weather_info = (
                f"Погода в городе {city}:\n"

                f"Состояние: {title}\n"
                f"Температура: {temperature}°C\n"
                f"Влажность: {humidity}\n"
                f"Ветер: {wind}"
            )
            return weather_info
        else:
            return f"Город {city} не найден. Проверьте правильность ввода"
    except Exception as e:
        return f"Произошла ошибка при получении данных: {e}"
