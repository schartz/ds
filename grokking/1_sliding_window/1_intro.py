# Given an array, find the average of all contiguous subarrays of size ‘K’ in it.
import time


def print_execution_time(func, *args, **kwargs):
	def wrapper(*args, **kwargs):
		ts = time.time()
		_ = func(*args, **kwargs)
		print(f'Execution time {time.time() - ts}')
		return _
	return wrapper


@print_execution_time
def contigous_sum(arr, k):
	l = len(arr)
	out = []
	for i in range(len(arr) - k + 1):
		sum = 0
		for j in range(i, i + k):
			sum += arr[j]
		out.append(sum/k)
	return out

@print_execution_time
def contigous_sum_sliding_window(arr, k):
	result = []
	sum = 0.0
	start = 0
	for end in range(len(arr)):
		sum += arr[end]

		if end >= k - 1:
			result.append(sum/k)
			sum -= arr[start]
			start += 1
	return result



print(contigous_sum([1, 3, 2, 6, -1, 4, 1, 8, 2], 5))
print(contigous_sum_sliding_window([1, 3, 2, 6, -1, 4, 1, 8, 2], 5))