def add_one(some_list):
    # спочатку список перетворюємо в число та додаемо 1
    # далі пертворюємо в строку, яку вже перетворюємо в список цисел
    return list(int(s) for s in iter(str(int(''.join(str(i) for i in some_list)) + 1)))

assert add_one([1, 2, 3, 4]) == [1, 2, 3, 5], 'Test1'
assert add_one([9, 9, 9]) == [1, 0, 0, 0], 'Test2'
assert add_one([0]) == [1], 'Test3'
assert add_one([9]) == [1, 0], 'Test4'
print("ОК")