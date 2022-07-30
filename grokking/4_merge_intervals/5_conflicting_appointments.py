def conflict(intervals):
	intervals.sort(key = lambda x: x[0])

	for i in range(1, len(intervals)):
		first = intervals[i - 1]
		second = intervals[i]

		if first[1] > second[0]:
			return False
	return True


print(conflict([[1,4], [2,5], [7,9]]))
print(conflict([[[6,7], [2,4], [8,12]]]))
print(conflict([[4,5], [2,3], [3,6]]))