lst_mine = [[7], [5, 8], [9, 8, 2], [1, 3, 5, 6], [6, 2, 4, 4, 5], [9, 5, 3, 5, 5, 7], [7, 4, 6, 4, 7, 6, 8]]

res_mining = []         # результат майнінгу

def mining(lst, row = 0, level = 0, suma = 0):
    suma += lst_mine[level][row]
    if level == (len(lst_mine) - 1):                     # перевіряємо чи це не останій рівень
        res_mining.append(suma)                          # рекурсивний вихід
        return
    if row < (len(lst_mine[level + 1]) - 1):              # перевіряємо чи можна на слідуючому рівні уйти вправо та вниз
        mining(lst_mine, row + 1, level + 1, suma)        # уходимо вправо та вніз
    mining(lst_mine, row, level + 1, suma)                # уходимо вніз
    return

mining(lst_mine)        # рекурсивно проходимо список списків

print('Результат всіх варіантів сум добитих золотих злитків:\n', res_mining, ' len-> ', len(res_mining))

print('Максимальна кількість добитих злитків:', max(res_mining))
