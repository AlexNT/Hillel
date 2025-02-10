import string

def first_word(text):
    string.ascii_letters += "'"                 # добавляю апостроф к списку символів
    _str = ''
    fl_first = False
    for ch in text:                             # проходимо посимвольно по рядку та перевіряємо чи входить символ в в рядок ascii_letters
        if string.ascii_letters.find(ch) > -1:
            fl_first = True                     # якщо знайшли перше входженя символу
            _str += ch
        elif fl_first:
            return _str
    return _str



assert first_word("Hello world") == "Hello", 'Test1'
assert first_word("greetings, friends") == "greetings", 'Test2'
assert first_word("don't touch it") == "don't", 'Test3'
assert first_word(".., and so on ...") == "and", 'Test4'
assert first_word("hi") == "hi", 'Test5'
assert first_word("Hello.World") == "Hello", 'Test6'
print('OK')