# Given a string and a pattern, find out if the string contains any permutation of the pattern.

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
def has_permutation(str, pattern):
    start = 0
    occurance_count = 0
    flag = False

    for end in range(len(str)):
        right_char = str[end]

        if right_char in pattern:
            flag = True
            occurance_count += 1
        else:
            flag = False
            occurance_count =0
            

        if occurance_count == len(pattern):
            return True

    return False



def has_permutation_correct(str, pattern):
    frequency = {}
    start = 0
    matched = 0
    for c in pattern:
        if c not in frequency:
            frequency[c] = 0
        frequency[c] += 1

    for end in range(len(str)):
        right_char = str[end]
        if right_char in frequency:
            frequency[right_char] -= 1

            if frequency[right_char] == 0:
                matched += 1
        while(end - start + 1) > len(pattern):
            left_char = str[start]

            if left_char in frequency:
                if frequency[left_char] == 0:
                    matched -= 1
                frequency[left_char] += 1
            start += 1
        if matched == len(frequency):
            return True
    return False

print(has_permutation("oidbcaf", "abc"))
print(has_permutation("odicf", "dc"))
print(has_permutation("bcdxabcdy", "bcdyabcdx"))
print(has_permutation("aaacb", "abc"))

print("======================================")

print(has_permutation_correct("oidbaaf", "abc"))
print(has_permutation_correct("odicf", "dc"))
print(has_permutation_correct("bcdxabcdy", "bcdyabcdx"))
print(has_permutation_correct("aaacb", "abc"))