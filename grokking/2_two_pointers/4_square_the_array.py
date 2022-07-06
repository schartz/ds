# Given a sorted array, create a new array containing squares of all the number of the input array in the sorted order.

import time


def print_execution_time(func, *args, **kwargs):
    def wrapper(*args, **kwargs):
        ts = time.time()
        _ = func(*args, **kwargs)
        print(f'Execution time {time.time() - ts}')
        return _
    return wrapper



def square_the_array(arr):
	second = 0
	first  = 0
	squares = []

	for i in range(len(arr)):
		if arr[i] >= 0:
			second = i
			first  = i - 1
			break

	if first < 0:
		first = 0

	print(second, first)

	flag = True

	while flag:
		s_square = -1
		f_square = -1
		if second < len(arr):
			s_square = arr[second]*arr[second]
			# print('s_square --> ', s_square)
			second += 1

		if first > -1:
			f_square = arr[first]*arr[first]
			print('f_square --> ', f_square)
			first -= 1


		if s_square > -1 and f_square < 0:
			squares.append(s_square)
		elif f_square > -1 and s_square < 0:
			squares.append(f_square)
		else:
			squares.append(min(s_square, f_square))
			squares.append(max(s_square, f_square))
		print(first, second)
		if second == len(arr) and first == -1:
			flag = False
	return squares


def square_the_array2(arr):
	second = len(arr) - 1
	first  = 0
	squares = []
	t = 'y'

	while second >= first:
		f_square = arr[first]*arr[first]
		s_square = arr[second]*arr[second]

		print(f'{f_square} --- {s_square}')

		if f_square >= s_square:
			squares.append(f_square)
			first += 1
		if s_square > f_square:
			squares.append(s_square)
			second -= 1
		print(first, second)

	return list(reversed(squares))



print(square_the_array2([-2, -1, 0, 2, 3]))
print(square_the_array2([-3, -1, 0, 1, 2]))