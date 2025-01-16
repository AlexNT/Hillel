my_list = [12, 3, 4, 10] #=> [10, 12, 3, 4]
#my_list = [1] #=> [1]
#my_list = [] #=> []
#my_list = [12, 3, 4, 10, 8] #=> [8, 12, 3, 4, 10]

if not my_list:
    print([])
else:
    my_list.insert(0, my_list.pop(-1))
    print(my_list)