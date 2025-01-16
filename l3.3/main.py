#my_list = [1, 2, 3, 4, 5, 6] #=> [[1, 2, 3], [4, 5, 6]]
#my_list = [1, 2, 3] #=> [[1, 2], [3]]
#my_list = [1, 2, 3, 4, 5] #=> [[1, 2, 3], [4, 5]]
#my_list = [1] #=> [[1], []]
my_list = [] #=> [[], []]

l = len(my_list)
mid = int(l / 2)
new_list = []
if (l % 2) == 0:
    # Кількість елементів списку парна
    new_list.append(my_list[0:mid])
    new_list.append(my_list[mid:l])
else:
    # Кількість елементів списку не парна
    new_list.append(my_list[0:mid + 1])
    new_list.append(my_list[mid + 1:l])

print(new_list)