def calc(user_text):
	text = user_text.strip(' ')
	if '=' in text:

		c = text[:-1]
		''.join(c.split())
		try:
			print(eval(c))
		except ZeroDivisionError:
			print('Делить на ноль - нехорошо!')
		except SyntaxError:
			print('А выражение до "=" написать?')
		except NameError:
			print('Уравнения я не понимаю :(')
		finally:
			print('Все будет хорошо! ^_^')


user_text = input('Enter an arithmetic expression that ends with an equal: ')
# calc("2/0= ")
calc(user_text)
