a = [1, 6, 8, 5, 2]

print('Список: {}'.format(a))
print('Cрез списка: {}'.format(a[2:4]))

a.append(99)

print('Добавили элемент: {}'.format(a))

b = [3, 4, 7]

print('Сложение списков: {} и {} = {}'.format(a, b, (a + b)))

for i in b:
	print('Элемент списка b: {}'.format(i))

# важно именно так написать "list(reversed(a))" а то вернет обьект
print('Реверс списка а: {}'.format(list(reversed(a))))

print('Сортировка списка: {}'.format(sorted(a)))
