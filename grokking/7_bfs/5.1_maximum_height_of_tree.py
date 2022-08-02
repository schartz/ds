class TreeNode:
	def __init__(self, value):
		self.val = value
		self.left = None
		self.right = None
	def __repr__(self):
		return str(self.val)


def min_height(node):
	q = [node]
	height = 0

	while len(q) > 0:
		height += 1
		for _ in range(len(q)):
			current = q.pop(0)
			if current.left: q.append(current.left)
			if current.right: q.append(current.right)
	return height

	


def main():
	root = TreeNode(12)
	root.left = TreeNode(7)
	root.right = TreeNode(1)
	root.left.left = TreeNode(9)
	root.right.left = TreeNode(10)
	root.right.right = TreeNode(5)
	root.right.left.left = TreeNode(20)
	root.right.left.right = TreeNode(17)
	print("min height: " + str(min_height(root)))

main()
