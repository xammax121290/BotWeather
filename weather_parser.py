import requests
from bs4 import BeautifulSoup


def all_parse_weather(town):
  link = f"https://www.google.com/search?q=погода+в+{town}"
  headers = {
      'User-Agent':
      'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
  }
  response = requests.get(link, headers=headers)
  soup = BeautifulSoup(response.text, "html.parser")

  if soup.find("span", {"class": "wob_t", "id": "wob_tm"}):
    temperature = soup.select("#wob_tm")[0].getText()
    temperature= round((int(temperature)-32)*5/9)
    #title = soup.select("#wob_dc")[0].getText()
    humidity = soup.select("#wob_hm")[0].getText()
    wind = soup.select("#wob_ws")[0].getText()
    wind = round(int(wind[0:-4])/2.237)

    weather_info = (
        f"Погода в городе {town}:\n"
        #f"Состояние: {title}\n"
        f"Температура: {temperature}°C\n"
        f"Влажность: {humidity}\n"
        f"Ветер: {wind}м/с\n")
    return weather_info
  else:
    return f"Город {town} не найден. Проверьте правильность ввода"
