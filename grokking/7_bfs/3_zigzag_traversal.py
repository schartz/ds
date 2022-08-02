class TreeNode:
	def __init__(self, value):
		self.val = value
		self.left = None
		self.right = None
	def __repr__(self):
		return str(self.val)


def zigzag_level_order(node):
	q = [node]
	result = []
	zigzag = False
	while len(q) > 0:
		levelsize = len(q)
		level = []

		for _ in range(levelsize):
			current = q.pop(0)
			level.append(current)
			if current.left: q.append(current.left)
			if current.right: q.append(current.right)

		if len(level) > 0: 
			if zigzag:
				level.reverse()
				zigzag = False
			else:
				zigzag = True
		result.append(level)
	return result


def main():
	root = TreeNode(12)
	root.left = TreeNode(7)
	root.right = TreeNode(1)
	root.left.left = TreeNode(9)
	root.right.left = TreeNode(10)
	root.right.right = TreeNode(5)
	root.right.left.left = TreeNode(20)
	root.right.left.right = TreeNode(17)
	print("Zigzag traversal: " + str(zigzag_level_order(root)))

main()
