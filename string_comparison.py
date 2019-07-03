"""
Сравнение строк

Написать функцию, которая принимает на вход две строки.
Если строки одинаковые, возвращает 1.
Если строки разные и первая длиннее, возвращает 2.
Если строки разные и вторая строка 'learn', возвращает 3.
"""


def comparison(first_string, second_string):
    if(first_string == second_string):
        print('строки одинаковые, возвращает 1')
        return 1
    elif(first_string != second_string and first_string > second_string):
        print('строки разные и первая длиннее, возвращает 2')
        return 2
    elif(first_string != second_string and second_string == 'learn'):
        print('строки разные и вторая строка "learn", возвращает 3')
        return 3


print(comparison('hello world', 'learn'))
