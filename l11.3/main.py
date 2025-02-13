def is_even(number):
    x = int(str(number)[-1])                # видиляємо останю цифру в числі
    return x in range(0, 8, 2)              # якщо остання цифра є в списку парних цифр вертаємо True

assert is_even(2494563894038**2) == True, 'Test1'
assert is_even(1056897**2) == False, 'Test2'
assert is_even(24945638940387**3) == False, 'Test3'