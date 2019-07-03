"""
Метод для бота который сравнивает строки.
"""
def count_word(user_text):
    print(user_text)
    if '"' in user_text:
        words = user_text.split('"')[1]
        print(words)
        if words:
            c_word = words.split(' ')
            print(c_word)
            print(len(c_word))
            # update.message.reply_text(len(c_word))
        else:
            print('Тут пустая строка!')
            # update.message.reply_text('Тут пустая строка!')

    else:
        print('не было кавычек!')
        # update.message.reply_text('не было кавычек!')


count_word('/wordcount "1 2"')