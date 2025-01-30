def correct_sentence(text):
    text = text.rstrip('.')
    my_list = text.split('.')       # розбиваємо на підречення
    if len(my_list) > 1:            # обробка у випадку декілька речень
        text = ''
        for s in my_list:
            text += s + '.'
        text = text.title()
    else:                           # якщо речення одне
        text = text.capitalize()
        text += '.'                 # точку в кінець чи є точка в кінці
    return text


assert correct_sentence("greetings, friends") == "Greetings, friends.", 'Test1'
assert correct_sentence("hello") == "Hello.", 'Test2'
assert correct_sentence("Greetings. Friends") == "Greetings. Friends.", 'Test3'
assert correct_sentence("Greetings, friends.") == "Greetings, friends.", 'Test4'
assert correct_sentence("greetings, friends.") == "Greetings, friends.", 'Test5'
print('ОК')