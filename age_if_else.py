"""
Возраст

Попросить пользователя ввести возраст.
По возрасту определить, чем он должен заниматься:
учиться в детском саду, школе, ВУЗе или работать.
Вывести занятие на экран.
"""

age = int(input('Please, indicate your age: '))


if age <= 6:
    print('You go to kindergarten')
elif age > 6 and age <= 16:
    print('You go to school')
elif age > 16 and age <= 22:
    print('You study at University')
else:
    print('You work')
