a = {'city': 'Москва', 'temperature': 25, 'wind': 'юго-западный'}

li = {
	'Маша': {'city': 'Волгоград', 'temperature': -17, 'wind': 'южный'},
	'Саша': {'city': 'Краснодар', 'temperature': 12, 'wind': 'северный'}, 
	'Клепа': {'city': 'Солнечногорск', 'temperature': 38, 'wind': 'западный'},
	'Изя': a
	}


print(li.keys())

name = input('Введите имя: ')

if name in li:
	print(li[name])
else:
	print('Ой!')
