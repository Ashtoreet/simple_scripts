"""
Возьмите словарь с ответами из функции get_answer
Запишите его содержимое в формате csv в формате: "ключ"; "значение". 
Каждая пара ключ-значение должна располагаться на отдельной строке
"""


import csv


with open('users.csv', 'r', encoding='utf-8') as f:
    fields = ['first_name', 'last_name', 'balance']
    reader = csv.DictReader(f, fields, delimiter=';')

    for row in reader:
        print(row)
