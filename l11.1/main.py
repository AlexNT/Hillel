def prime_generator(end):
    if end < 2:                                 # Якщо end менше 2, немає простих чисел для повернення
        return
    lst = [x for x in range(2, end + 1) if all(x % y != 0 for y in range(2, int(x**0.5) + 1))]  # використовую оптимизований алгоритм "решето Эратосфена" для обрахування простого числа
                                                                                                # замість перевірки всіх чисел до x-1, ми перевіряємо лише до квадратного кореня з x (int(x**0.5) + 1)
    for num in lst:
        yield num                           # Повертаємо прості числа через yield

from inspect import isgenerator

gen = prime_generator(1)
assert isgenerator(gen) == True, 'Test0'
assert list(prime_generator(10)) == [2, 3, 5, 7], 'Test1'
assert list(prime_generator(15)) == [2, 3, 5, 7, 11, 13], 'Test2'
assert list(prime_generator(29)) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29], 'Test3'
print('Ok')