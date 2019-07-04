from flask import Flask, abort, request
from req import get_weather
from datetime import datetime
from news_list import all_news
from apikeys import weather
import new_names


city_id = 524901
apikey = weather


app = Flask(__name__)

@app.route("/")
def index():
    url = 'http://api.openweathermap.org/data/2.5/weather?id={}&APPID={}&units=metric'.format(city_id, apikey)
    weather = get_weather(url)
    cur_date = datetime.now().strftime('%d %b %y')

    result = '<p><b>Температура</b>: {}\n</p>'.format(weather['main']['temp'])
    result += '<p>Город: {}\n</p>'.format(weather['name'])
    result += '<p>Ветер: {}м/с</p>'.format(weather['wind']['speed'])
    result += '<p><b>Дата:</b> {}</p>'.format(cur_date)
    return result


@app.route('/news')
def all_the_news():
    colors = ['green', 'red', 'blue', 'magenta']
    try:
        limit = int(request.args.get('limit'))
    except:
        limit = 0

    color = request.args.get('color', 'black') if request.args.get('color') in colors else 'black'
    return '<h1 style="color: {}">News: <small>{}</small></h1>'.format(color, limit)



@app.route('/news/<int:news_id>')
def news_by_id(news_id):

    news_to_show = [news for news in all_news if news['id'] == news_id]
    if len(news_to_show) == 1:

        di = datetime.strptime(news_to_show[0]['date'], '%Y-%m-%d').strftime('%d %b %y')
        result = '<h1>%(title)s</h1><p><i>{}</i></p><p>%(text)s</p>'.format(di)
        result = result % news_to_show[0]

        return result
    else:
        return abort(404)


@app.route('/names')
def names_to_table():
    year = int(request.args.get('year'))


    url = new_names_2.url
    names = new_names_2.get_names(url)
    table = [name['Cells'] for name in names]

    rows = ''
    for item in table:
        if item['Year'] == year:
            rows += '<tr><td>{}</td><td>{}</td><td>{}</td><td>{}</td></tr>'.format(item['Name'], item['NumberOfPersons'], item['Month'], item['Year'])

    header = '<tr><th>Имя</th><th>Кол-во детей</th><th>Месяц</th><th>Год</th></tr>'
    result = '<table>{}{}</table>'.format(header, rows)

    return result


if __name__ == '__main__':
	app.run(port=5010, debug=True)
