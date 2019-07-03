"""
Задание

Переписать функцию ask_user(), добавив обработку exception-ов
Добавить перехват ctrl+C и прощание
"""


def get_answer(user_input):
	while user_input != 'Пока!':
		print('Сам ты {}'.format(user_input))
		user_input = input('надо писать Пока!: ').capitalize()


def ask_user():
	user_input = ''

	try:
		while user_input != 'Хорошо':
			print('Как дела?')
			user_input = input('надо писать хорошо: ').capitalize()

			if '?' in user_input:
				get_answer(user_input)
	except KeyboardInterrupt:
		print('Ctrl + C')
	finally:
		print('The program is finished, thanks for using :)')


ask_user()
