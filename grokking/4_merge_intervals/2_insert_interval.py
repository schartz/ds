def insert(intervals, new_interval):
    merged = []
    index = 0
    for interval in intervals:
        if new_interval[0] > interval[0]:
            index += 1
        else:
            break

    intervals.insert(index, new_interval)
    # print(intervals)

    for interval in intervals:
        if len(merged) == 0:
            merged.append(interval)
        else:
            first = merged[-1]

            if first[1] >= interval[0]:
                merged[-1] = [min(first[0], interval[0]), max(first[1], interval[1])]
            else:
                merged.append(interval)
    return merged


print("Intervals after inserting the new interval: " + str(insert([[1, 3], [5, 7], [8, 12]], [4, 6])))
print("Intervals after inserting the new interval: " + str(insert([[1, 3], [5, 7], [8, 12]], [4, 10])))
print("Intervals after inserting the new interval: " + str(insert([[2, 3], [5, 7]], [1, 4])))

