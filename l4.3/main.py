import random
# генерація спіска с кількістю елементів від 3 до 10
my_list: list[int] = [random.randint(1,100) for i in range(random.randint(3, 10))]
print(my_list)
new_list = [my_list[0], my_list[2], my_list[-2]]    # новий список із 3-х елементів
print(new_list)