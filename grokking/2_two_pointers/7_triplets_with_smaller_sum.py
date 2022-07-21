# Given an array arr of unsorted numbers and a target sum, 
# count all triplets in it such that arr[i] + arr[j] + arr[k] < target 
# where i, j, and k are three different indices. 
# Write a function to return the count of such triplets.


def triplets_with_smaller_sum(nums, target):
	nums.sort()
	triplets = []
	count = 0

	for i in range(len(nums) - 2):
		left = i + 1
		right = len(nums) - 1
		sub_target = target - nums[i]

		while left < right:
			sum = nums[left] + nums[right]

			if sum < sub_target:
				triplets.append([nums[left], nums[right], nums[i]])
				count += right - left
				left += 1

			else:
				right -= 1
	return count


print(triplets_with_smaller_sum([-1, 0, 2, 3], target=3))
print(triplets_with_smaller_sum([-1, 4, 2, 1, 3], target=5))
