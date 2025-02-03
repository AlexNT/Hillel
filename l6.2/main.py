sec = int(input('Введіть число від 0 до 8640000:\n'))
day, sec = divmod(sec, 24 * 60 * 60)       # рахуємо кількість днів
hour, sec = divmod(sec, 60 * 60)           # рахуємо кількість годин
mint, sec = divmod(sec, 60)                # рахуємо кількість годин
# вираховуємо відмінок
words = ['день', 'дні', 'днів']
if all((day % 10 == 1, day % 100 != 11)):
    n_day = words[0]
elif all((2 <= day % 10 <= 4, any((day % 100 < 10, day % 100 >= 20)))):
    n_day = words[1]
else:
    n_day = words[2]

print('{day} {n_day}, {hour:02}:{min:02}:{sec:02}'.format(day = day, hour = hour, min = mint, sec = sec, n_day = n_day))