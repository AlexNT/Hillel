my_list = [0, 1, 7, 2, 4, 8] #=> (0 + 7 + 4) * 8 = 88
#my_list = [1, 3, 5] #=> 30
#my_list = [6] #=> 36
#my_list = [] #=> 0

y = 0
for i, el in enumerate(my_list):
    if i % 2 == 0:            # шукаємо парний індекс
        y += el               # сумуємо елементи списку
if my_list:
    y *= my_list[-1]          # множимо на останній елемент
print(y)
