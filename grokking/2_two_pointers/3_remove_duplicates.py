# Given an array of sorted numbers, remove all duplicates from it. You should not use any extra space; 
# after removing the duplicates in-place return the new length of the array.

import time


def print_execution_time(func, *args, **kwargs):
    def wrapper(*args, **kwargs):
        ts = time.time()
        _ = func(*args, **kwargs)
        print(f'Execution time {time.time() - ts}')
        return _
    return wrapper


def remove_duplicates(arr):
    arr_length = len(arr)

    if arr_length <= 1:
        return 1

    first = 0
    second = 1
    while second < len(arr):
        if arr[first] == arr[second]:
            arr_length -= 1
        second += 1
        first += 1

    return arr_length


print(remove_duplicates([2, 3, 3, 3, 6, 9, 9]))
print(remove_duplicates([2, 2, 2, 11]))