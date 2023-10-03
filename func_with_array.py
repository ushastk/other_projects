from random import *  # порядковый номер считается с нуля

def create_and_sort_array(n):
    max_size = 10000
    min_size = 1
    general_array = []
    items = list(range(min_size, max_size))
    shuffle(items)
    array_size = items[:n]
    for i in range(n):
        array = [randint(min_size, max_size) for _ in range(array_size[i])]
        if i % 2 == 0:
            array.sort()
        else:
            array.sort(reverse=True)
        general_array.append(array)
    return general_array
print(create_and_sort_array(7))