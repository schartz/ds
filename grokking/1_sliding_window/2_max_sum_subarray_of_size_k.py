# Given an array of positive numbers and a positive number ‘k’, find the maximum sum of any contiguous subarray of size ‘k’.
import time


def print_execution_time(func, *args, **kwargs):
	def wrapper(*args, **kwargs):
		ts = time.time()
		_ = func(*args, **kwargs)
		print(f'Execution time {time.time() - ts}')
		return _
	return wrapper



@print_execution_time
def max_subarr(arr, k):
	max_sum = 0
	for i in range(len(arr) - k + 1):
		sum = 0
		for j in range(i, k+i):
			sum += arr[j]
		if sum > max_sum:
			max_sum = sum
	return max_sum



@print_execution_time
def max_subarr2(arr, k):
	max_sum = 0
	temp_sum = 0
	start = 0

	max_start = start
	max_end = -1

	for end in range(len(arr)):
		temp_sum += arr[end]

		if end >= k - 1:
			if temp_sum > max_sum:
				max_sum = temp_sum
				max_start = start
				max_end = end

			temp_sum -= arr[start]
			start += 1
	print('-->', arr[max_start:max_end + 1])
	return max_sum




print(max_subarr([2, 1, 5, 1, 3, 2], 3 ))
print()
print(max_subarr2([2, 1, 5, 1, 3, 2], 3 ))
print()
print(max_subarr2([2, 3, 4, 1, 5], 2 ))