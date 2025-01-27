ans = num = int(input('Введіть ціле число:\n'))
while ans > 9:                     # повторюємо поки не буде меньше чи дорівнювати 9
    my_list = list(str(ans))       # передворюємо в список
    ans = 1
    for n in my_list:              # перемножуємо числа
        ans *= int(n)
print(f'{num} -> {ans}')