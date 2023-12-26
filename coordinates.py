from urllib.request import urlopen
from dataclasses import dataclass
import json

@dataclass()
class City:
    city: str


def get_city():
    data=_get_ip_data()
    city = data.get('city')
    return city

def _get_ip_data():
    try:
        url = 'http://ipinfo.io/json'
        response = urlopen(url)
        data = json.load(response)
        return data
    except json.JSONDecodeError:
        print('Ошибка при декодировании JSON')
        return {}
    except Exception as e:
        print(f'Произошла ошибка: {e}')
        return {}
