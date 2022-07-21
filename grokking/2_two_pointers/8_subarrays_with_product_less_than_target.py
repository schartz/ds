# Given an array with positive numbers and a target number, 
# find all of its contiguous subarrays whose product is less than the target number.

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


@print_execution_time
def subarrays_with_product_less_than_target(nums, target):
	print(len(nums))
	subarrs = []
	iter_count = 0
	for i in range(len(nums)):
		iter_count += 1
		idx = i
		product = 1
		while idx < len(nums):
			iter_count +=1

			product = product * nums[idx]

			if product < target:
				subarrs.append(nums[i:idx + 1])
				idx += 1
			else:
				break
	print(iter_count)
	print(subarrs)
	return len(subarrs)



@print_execution_time
def subarrays_with_product_less_than_target2(nums: List[int], k: int) -> int:
    N = len(nums)
    product_so_far = 1
    left = 0
    subarrs = 0
    total = 0

    for i in range(N):
        # calculate product so far and add to subarrs
        product_so_far = product_so_far * nums[i]
        subarrs += 1

        # while loop to increase left and decrease subarrs
        while product_so_far >= k and left <= i:
            product_so_far /= nums[left]
            left += 1
            subarrs -= 1
            

        # if product < k
        #   add total to subarrays

        if product_so_far < k:
            total += subarrs
    return total

@print_execution_time
def subarrays_with_product_less_than_target3(nums: List[int], k: int) -> int:
	right, left = 0, 0
	product_so_far = 1
	result = 0

	while right < len(nums):
		product_so_far = product_so_far * nums[right]

		while product_so_far >= k:
			product_so_far = product_so_far / nums[left]
			left += 1
		result += right - left + 1
		right += 1
	return result


# print(subarrays_with_product_less_than_target([2, 5, 3, 10], target=30))
# print(subarrays_with_product_less_than_target([8, 2, 6, 5], target=50 ))
t = [x + randint(1, 10) for x in range(4000)]
print(subarrays_with_product_less_than_target3(t, 958850))
print()
print()
print(subarrays_with_product_less_than_target2(t, 958850))

