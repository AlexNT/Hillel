import string
import keyword

print('Введить рядок.\n')
my_str = input().strip()        # удаляємо пробіли на початку та кінці
flag = True

# перевіряємо чи строка не пуста
if my_str == '':
    flag = False
else:
# перевіряємо на знаки пунктуації крім '_'
# '_' міняємо на пробел ' '
    punt = string.punctuation.replace('_', ' ')
    for ch in punt:
        if my_str.find(ch) != -1:
            flag = False
# перевіряємо на зарезервовані слова
    for word in keyword.kwlist:
        if my_str == word:
            flag = False
# перевіряємо чи містить великі літери
    if my_str != my_str.lower():
        flag = False
# перевіряємо чи перший символ цифра
    if my_str[0].isnumeric():
        flag = False
# перевіряємо чи повне ім'я не містить тільки символи '_', більше одного
    if len(my_str) > 1:
        fl = True
        for ch in my_str:
            if ch != '_':
                fl = False
        if fl:
            flag = False

print(flag)



