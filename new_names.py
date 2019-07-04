import requests
from apikeys import mos_api
"""
Напишите функцию,

которая получает данные при помощи requests и читает содержимое в формате json.
Для получения данных используйте ссылку:
http://api.data.mos.ru/v1/datasets/2009/rows
"""


def get_names(url):
    result = requests.get(url)
    if result.status_code == 200:
        return result.json()
    else:
        return "status code: {}".format(result.status_code)


url = 'http://api.data.mos.ru/v1/datasets/2009/rows?api_key={}'.format(mos_api)

if __name__ == '__main__':
    print(get_names(url))
