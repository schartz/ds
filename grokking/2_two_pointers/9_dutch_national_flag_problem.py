# Given an array containing 0s, 1s and 2s, sort the array in-place. 
# You should treat numbers of the array as objects, hence, 
# we can’t count 0s, 1s, and 2s to recreate the array.

import time
from random import *
from typing import List

def print_execution_time(func, *args, **kwargs):
	def wrapper(*args, **kwargs):
		ts = time.time()
		_ = func(*args, **kwargs)
		print(f'Execution time {time.time() - ts}')
		return _
	return wrapper

def swap(a, b):
	c = b
	b = a
	a = c
	return a, b

def dutch_national_flag(nums):
	left, right = 0, len(nums) - 1
	index = 0

	while(index <= right and left < right):
		if nums[index] == 0:
			nums[left], nums[index] = swap(nums[left], nums[index])
			left += 1
			index += 1
		elif nums[index] == 2:
			nums[right], nums[index] = swap(nums[right], nums[index])
			right -= 1
			# index += 1
		else:
			index += 1
	return nums


print(dutch_national_flag([1, 0, 2, 1, 0]))
