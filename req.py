import requests
from apikeys import *

def get_weather(url):
    result = requests.get(url)
    if result.status_code == 200:
        return result.json()
    else:
        print("status code: {}".format(result.status_code))


if __name__ == "__main__":
    url = "http://api.openweathermap.org/data/2.5/weather?id=524901&APPID={}&units=metric".format(weather)
    data = get_weather(url)
    print(data)
