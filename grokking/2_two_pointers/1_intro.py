# Given an array of sorted numbers and a target sum, find a pair in the array whose sum is equal to the given target.

import time


def print_execution_time(func, *args, **kwargs):
	def wrapper(*args, **kwargs):
		ts = time.time()
		_ = func(*args, **kwargs)
		print(f'Execution time {time.time() - ts}')
		return _
	return wrapper


def sum_of_pair(arr, target):
	start = 0
	end = len(arr) - 1
	pegs = []
	peg_vals = []

	while end > start:
		if arr[start] + arr[end] == target:
			pegs = [start, end]
			peg_vals = [arr[start], arr[end]]
			print(pegs)
			return peg_vals
		if arr[start] + arr[end] < target:
			start += 1
		if arr[start] + arr[end] > target:
			end -= 1

	


print(sum_of_pair([1, 2, 3, 4, 6], 6))


print()
print()


print(sum_of_pair([2, 5, 9, 11], 11))