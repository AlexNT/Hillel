def bubble_sort(arr):
    fl_exit = True
    while fl_exit:
        fl_exit = False
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                fl_exit = True
    return arr

# Перевірка
assert bubble_sort([64, 34, 25, 12, 22, 11, 90]) == [11, 12, 22, 25, 34, 64, 90]
assert bubble_sort([5, 2, 9, 1, 5, 6]) == [1, 2, 5, 5, 6, 9]
assert bubble_sort([3, 8, 1, 7, 2, 9, 6]) == [1, 2, 3, 6, 7, 8, 9]