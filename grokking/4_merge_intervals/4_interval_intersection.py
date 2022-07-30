def interval_intersection(firstList, secondList):
	a, b = 0, 0
	result = []
	while a < len(firstList) and b < len(secondList):
        first_item, second_item = firstList[a], secondList[b]
        
		start = max(first_item[0], second_item[0])
		end = min(first_item[1], second_item[1])

		if start <= end:
			result.append([start, end])


		if first_item[1] < second_item[1]:
			a += 1
		else:
			b += 1
	return result



print(interval_intersection(firstList=[[1, 3], [5, 6], [7, 9]], secondList=[[2, 3], [5, 7]]))
print(interval_intersection(firstList=[[1, 3], [5, 7], [9, 12]], secondList=[[5, 10]]))


