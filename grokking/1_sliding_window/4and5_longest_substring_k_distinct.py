# Given a string, find the length of the longest substring in it with no more than K distinct characters.




# this pattern can be used in a problem similar to following
'''
Given an array of characters where each character represents a fruit tree, 
you are given two baskets and your goal is to put maximum number of fruits in each basket. 
The only restriction is that each basket can have only one type of fruit.

You can start with any tree, but once you have started you can’t skip a tree. 
You will pick one fruit from each tree until you cannot, i.e., you will stop when you have to pick from a third fruit type.
'''


# pattern is also called "Longest Substring with at most k distinct characters"


import time
import math


def print_execution_time(func, *args, **kwargs):
    def wrapper(*args, **kwargs):
        ts = time.time()
        _ = func(*args, **kwargs)
        print(f'Execution time {time.time() - ts}')
        return _
    return wrapper

@print_execution_time
def longest_substring_k_distinct(str, k):
    frequency = {}
    start = 0
    substr = ""
    longest_str = ""
    max_len = 0

    for end in range(len(str)):
        substr += str[end]

        if str[end] in frequency:
            frequency[str[end]] += 1
        else:
            frequency[str[end]] = 1

        while len(frequency) > k:
            left_char = substr[start]

            frequency[left_char] -= 1
            if frequency[left_char] == 0:
                del frequency[left_char]
            start += 1
        if max_len < end - start + 1:
            max_len = end - start + 1
            longest_str = str[start:end + 1]
    print(longest_str)
    return max_len





print(longest_substring_k_distinct("araaci", 2))
print(longest_substring_k_distinct("araaci", 1))
print(longest_substring_k_distinct("cbbebi", 3))

# inputs from fruit basket problem
print(longest_substring_k_distinct("abcac", 2))
print(longest_substring_k_distinct("abcbbc", 2))
