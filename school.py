"""
Оценки

Создать список с оценками учеников разных классов школы вида
[{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
Посчитать и вывести средний балл по всей школе.
Посчитать и вывести средний балл по каждому классу.
"""


scores = [
	{'school_class': '5a', 'scores': [3, 3, 3, 5, 2]},
	{'school_class': '4a', 'scores': [3, 4, 4, 4, 1]},
	{'school_class': '3a', 'scores': [2, 2, 4, 5, 3]},
	{'school_class': '2a', 'scores': [5, 5, 4, 5, 3]},
	{'school_class': '1a', 'scores': [3, 4, 4, 5, 2]}
	]


amount = 0
count = 0


for i in scores:

	for d in i['scores']:
		amount += d
		count += 1
	print('Class: {}, Average score: {}'.format(i['school_class'], amount/count))


print('School average score: {}'.format(amount/count))
