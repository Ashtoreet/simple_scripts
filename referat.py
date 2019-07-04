"""
кол-во слов в файле
"""

summa = 0


with open('referat.txt', 'r', encoding='utf-8') as f:
    content = f.read()
    content = content.replace('\n', ' ').split(' ')
    for word in content:
        if word != '':
            summa += 1


print('Кол-во слов: {}'.format(summa))
