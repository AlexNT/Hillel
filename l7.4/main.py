def common_elements():
    set1 = set(range(3, 303, 3))   # список з числами кратними 3 len 100, перетворюємо відразу у множину
    set2 = set(range(5, 505, 5))   # список p кратними числами 5 len 100, перетворюємо відразу у множину
    print(set1 & set2)
    return set1 & set2             # перетин множин
assert common_elements() == {0, 75, 45, 15, 90, 60, 30}