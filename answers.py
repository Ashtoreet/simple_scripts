def get_answer(question, answers):
	if question in answers:
		return answers[question]
	else:
		return 'Ой!'


answers = {
		"привет": "И тебе привет!", 
		"как дела": "Лучше всех", 
		"пока": "Увидимся"
		}

print('Напишите:')
print('"привет", "как дела" или "пока".')
question = input('Введите слово: ').lower()

print(get_answer(question, answers))
