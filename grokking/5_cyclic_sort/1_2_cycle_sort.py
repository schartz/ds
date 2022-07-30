def cycle_sort(nums):
	i = 0
	while i < len(nums):
		j = nums[i] - 1
		num = nums[i]

		if nums[i] != nums[j]:
			nums[i], nums[j] = nums[j], nums[i]
		else:
			i += 1
	return nums


print(cycle_sort([3, 1, 5, 4, 2]))
