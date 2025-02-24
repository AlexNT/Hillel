from typing import List, Tuple

def mountain_scape(tops):
    points = set()  # Для хранения уникальных точек, покрытых треугольниками

    for x, y in tops:
        # Вычисляем основание треугольника
        base_start = x - y + 1
        base_end = x + y

        # Перебираем основание и высоту, чтобы покрыть все точки в треугольнике
        for i in range(base_start, base_end + 1):
            for j in range(1, y + 1):
                if abs(i - x) < j:
                    points.add((i, j))

    # Площадь — это количество уникальных точек
    return len(points)


if __name__ == '__main__':
    print("Example:")
    print(mountain_scape([(1, 1), (4, 2), (7, 3)]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert mountain_scape([(1, 1), (4, 2), (7, 3)]) == 13
    assert mountain_scape([(0, 2), (5, 3), (7, 5)]) == 29
    assert mountain_scape([(1, 3), (5, 3), (5, 5), (8, 4)]) == 37
    print("Coding complete? Click 'Check' to earn cool rewards!")