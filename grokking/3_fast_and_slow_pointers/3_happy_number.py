
def process(n):
	s = str(n)
	l = [int(x) for x in s]
	s = 0
	for i in l:
		s += i*i
	return s


def happy_number(n):
	sums = []
	num = n
	while True:
		p = process(num)
		if p == 1:
			return True
		elif p in sums:
			return False
		else:
			sums.append(p)
			num = p
		print(sums)


print(happy_number(23))
print(happy_number(12))