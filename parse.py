from bs4 import BeautifulSoup
from reque import get_html


url = 'https://yandex.ru/search/?lr=10738&msid=1491633162.22888.601&text=python'
html = get_html(url)

if html:
    bs = BeautifulSoup(html, 'html.parser')
    # print(bs.prettify())
    data = []


    for item in bs.find_all('li', class_='serp-item'):
        block_title = item.find('a', class_='organic__url')
        href = item.find('a', class_='path__item')
        data.append({
                'title': block_title.text,
                'link': href.get('href')
            })

    print(data)
else:
    print('Что-то пошло не так.')