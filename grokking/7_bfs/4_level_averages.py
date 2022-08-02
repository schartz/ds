class TreeNode:
	def __init__(self, value):
		self.val = value
		self.left = None
		self.right = None
	def __repr__(self):
		return str(self.val)


def level_averages(node):
	q = [node]
	avgs = []

	while len(q) > 0:
		level = []

		for _ in range(len(q)):
			current = q.pop(0)
			level.append(current.val)

			if current.left: q.append(current.left)
			if current.right: q.append(current.right)

		avgs.append(sum(level)/len(level))
	return avgs
	


def main():
	root = TreeNode(12)
	root.left = TreeNode(7)
	root.right = TreeNode(1)
	root.left.left = TreeNode(9)
	root.right.left = TreeNode(10)
	root.right.right = TreeNode(5)
	root.right.left.left = TreeNode(20)
	root.right.left.right = TreeNode(17)
	print("Zigzag traversal: " + str(level_averages(root)))

main()
