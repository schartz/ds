class TreeNode:
	def __init__(self, value):
		self.val = value
		self.left = None
		self.right = None
	def __repr__(self):
		return str(self.val)


def level_order(node):
	q = [node]
	result = []
	while len(q) > 0:
		levelsize = len(q)
		level = []

		for _ in range(levelsize):
			current = q.pop(0)
			level.append(current)

			if current.left: q.append(current.left)
			if current.right: q.append(current.right)
			
		if len(level) > 0: result.append(level)

	return result



def main():
	root = TreeNode(12)
	root.left = TreeNode(7)
	root.right = TreeNode(1)
	root.left.left = TreeNode(9)
	root.right.left = TreeNode(10)
	root.right.right = TreeNode(5)
	print("Level order traversal: " + str(level_order(root)))

main()