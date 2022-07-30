# Given a list of intervals, merge all the overlapping intervals to produce a list 
# that has only mutually exclusive intervals.

class interval:
	def __init__(self, start, end):
		self.start = start
		self.end = end

	def print_interval(self):
		print("[" + str(self.start) + ", " + str(self.end) + "]", end='')

	def __repr__(self):
		return "[" + str(self.start) + ", " + str(self.end) + "]"


def merge(intervals):
	merged = []

	print(f'given: {intervals}')

	intervals.sort(key=lambda x: x.start)
	print(f'sorted: {intervals}')
	
	for current_interval in intervals:
		if len(merged) == 0:
			merged.append(current_interval)
		first = merged[-1]

		if first.end >= current_interval.start:
			merged[-1] = interval(min(first.start, current_interval.start), max(first.end, current_interval.end))
		else:
			merged.append(current_interval)
	return merged



def main():
	
	print(merge([interval(7, 9), interval(2, 5), interval(1, 4)]))
	print()
	
	print(merge([interval(6, 7), interval(2, 4), interval(5, 9)]))
	print()

	print(merge([interval(1, 4), interval(2, 6), interval(3, 5)]))
		

main()
