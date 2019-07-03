"""
Задание

Пройдите в цикле по списку ["Вася", "Маша", "Петя", "Валера", "Саша", "Даша"]
пока не встретите имя "Валера". Когда найдете напишите "Валера нашелся".
Подсказка: используйте метод list.pop()

Перепишите предыдущий пример в виде функции find_person(name),
которая ищет имя в списке.

Написать функцию ask_user() чтобы с помощью input()
спрашивать пользователя “Как дела?”,

пока он не ответит “Хорошо”
При помощи функции get_answer() отвечать на вопросы пользователя в ask_user(),
пока он не скажет “Пока!”
"""


# names = ["Вася", "Маша", "Петя", "Валера", "Саша", "Даша"]
# name = ''
# while name != 'Валера':
# 	name = names.pop()
# 	print(name)


# def find_person(name):
# 	names = ["Вася", "Маша", "Петя", "Валера", "Саша", "Даша"]
# 	i = ''

# 	while i != name:
# 		i = names.pop()

# 	print('We found a name: {}'.format(i))

# find_person('Валера')


def get_answer(user_input):
	while user_input != 'Пока!':
		print('Сам ты {}'.format(user_input))
		user_input = input().capitalize()

def ask_user():
	user_input = ''

	while user_input != 'Хорошо':
		print('Как дела?')
		user_input = input().capitalize()
		if '?' in user_input:
			get_answer(user_input)


ask_user()
