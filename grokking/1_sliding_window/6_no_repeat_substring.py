# Given a string, find the length of the longest substring which has no repeating characters.


import time
import math


def print_execution_time(func, *args, **kwargs):
    def wrapper(*args, **kwargs):
        ts = time.time()
        _ = func(*args, **kwargs)
        print(f'Execution time {time.time() - ts}')
        return _
    return wrapper


def no_repeat_substring(str):
	index_frequency = {}
	start = 0

	max_len = 0
	longest_substr = ""

	for end in range(len(str)):
		if str[end] in index_frequency:
			start = max(start, index_frequency[str[end]] + 1)

		index_frequency[str[end]] = end
		if max_len < end - start + 1:
			max_len = end - start + 1
			longest_substr = str[start: end + 1]
	print(longest_substr)
	return max_len

		

print(no_repeat_substring("aabccbb"))
print(no_repeat_substring("abbbb"))
print(no_repeat_substring("abccde"))