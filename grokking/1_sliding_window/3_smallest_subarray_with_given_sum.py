# Given an array of positive numbers and a positive number ‘S’, 
# find the length of the smallest contiguous subarray whose sum is greater than or equal to ‘S’. 
# Return 0, if no such subarray exists.
import time
import math


def print_execution_time(func, *args, **kwargs):
	def wrapper(*args, **kwargs):
		ts = time.time()
		_ = func(*args, **kwargs)
		print(f'Execution time {time.time() - ts}')
		return _
	return wrapper



def smallest_subarr(arr, s):
	pegs = [-1, -1]
	start = 0
	sum = 0
	smallest_length = math.inf
	
	for end in range(len(arr)):
		sum += arr[end]

		while sum >= s:
			if smallest_length > (end - start + 1):
				smallest_length = end - start + 1
				pegs = [start, end]
			
			sum -= arr[start]
			start += 1

	print(arr[pegs[0]: pegs[1] + 1])
	return smallest_length







print(smallest_subarr([2, 1, 5, 2, 3, 2], 7))
print(smallest_subarr([2, 1, 5, 2, 8], 7))
print(smallest_subarr([3, 4, 1, 1, 6], 8))