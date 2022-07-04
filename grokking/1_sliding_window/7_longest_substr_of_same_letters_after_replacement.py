# Given a string with lowercase letters only, if you are allowed to replace no more than ‘k’ letters with any letter, 
# find the length of the longest substring having the same letters after replacement.

import time
import math


def print_execution_time(func, *args, **kwargs):
    def wrapper(*args, **kwargs):
        ts = time.time()
        _ = func(*args, **kwargs)
        print(f'Execution time {time.time() - ts}')
        return _
    return wrapper

def longest_substr_of_same_letters_after_replacement(str, k):
    start = 0
    R = 0
    max_len = 0
    frequency = {}
    subtr = ""

    for end in range(len(str)):
        right_char = str[end]

        if right_char not in frequency:
            frequency[right_char] = 1
        else:
            frequency[right_char] += 1

        R = max(R, frequency[right_char])

        if(end - start + 1 - R) > k:
            left_char = str[start]
            frequency[left_char] -= 1
            start += 1
        if max_len < end - start + 1:
            max_len = end - start + 1
            subtr = str[start: end + 1]
    print(subtr)
    return max_len



print(longest_substr_of_same_letters_after_replacement("aabccbb", 2))
print(longest_substr_of_same_letters_after_replacement("abbcb", 1))
print(longest_substr_of_same_letters_after_replacement("abccde", 1))
print(longest_substr_of_same_letters_after_replacement("01100011011", 2))