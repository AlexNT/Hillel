import string
my_list = list(input('Введіть дві літери через дефіз:\n'))
fl = False
for ch in string.ascii_letters: # проходимо по набору літер
    if my_list[0] == ch:        # шукаємо першу літеру
        fl = True
    if fl:                      # знайшли першу літеру
        print(ch, end = '')
        if my_list[2] == ch:    # виводимо до другої літери та закінчуємо цікл
            break