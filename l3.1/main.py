from contextlib import nullcontext

print('Додаток "Калькулятор". Введіть почерзі перше число, дію, та друге число.\n')
print('Введіть перше число: ')
x = float(input())
print('Введіть дію (+,-,*,/): ')
diya = input()
print('Введіть друге число: ')
y = float(input())
err = False
ans = 0
if (diya != '+') and (diya != '-') and (diya != '*') and (diya != '/'):
    err = True
    print('Помилка: не введена дія.')
elif (diya == '/') and(y == 0):
    err = True
    print('Помилка: на 0 ділити заборонено.')
elif diya == '+':
    ans = x + y
elif diya == '-':
    ans = x - y
elif diya == '*':
    ans = x * y
elif diya == '/':
    ans = x / y
if not err:
    print('Відповідь: ' + str(x) + ' ' + diya + ' ' + str(y) + ' ' + '=' + ' ' + str(ans))
