catalog_item = {
	"type": "phone",
	"vendor": "Apple",
	"model": "iPhone 7 black",
	"price": 37.5
}

print('Словарь: {}'.format(catalog_item))

catalog_item["audio_jack"] = False

print('Словарь(добавили раздел): {}'.format(catalog_item))

catalog_item['price'] = 70

print('Словарь(обновили цену): {}'.format(catalog_item))
print('Вывод данных по ключу: price - {}'.format(catalog_item['price']))

item_name = '{} {}'.format(catalog_item['vendor'], catalog_item['model'])

print('Составное название по ключАм: {}'.format(item_name))

print('Метод get() - catalog_item.get("type"): {}'.format(catalog_item.get('type')))

print('Если ключа нет в списке(catalog_item.get("discount", "Скидок нет и не будет!")) : {}'.
	format(catalog_item.get("discount", "Скидок нет и не будет!")))

print('Есть ли ключ в словаре("model" in catalog_item)?: {}'.format("model" in catalog_item))
print('Есть ли ключ в словаре("discount" not in catalog_item)?: {}'.format("discount" not in catalog_item))


print('Вывод каждого ключа в словаре: ')
for key in catalog_item:
    print(key)


print('Вывод ключ значение из словаря: ')
for key, value in catalog_item.items():
    print('{}: {}'.format(key, value))

del catalog_item["price"]
print('Удаление элементов из словаря(del catalog_item.get("price")): {}'.format(catalog_item))

try:
    print('Пытаемся удалить значение ключа "discount".')
    del catalog_item['discount']
except KeyError:
    print('Поймали KeyError, работаем дальше.')
    pass

print('Закончили зарядку!')


