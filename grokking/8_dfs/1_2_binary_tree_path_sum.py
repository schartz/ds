class TreeNode:
	def __init__(self, value):
		self.val = value
		self.left = None
		self.right = None
	def __repr__(self):
		return str(self.val)


def has_path(root, target):
	stack = []
	stack.append([root, root.val])

	while len(stack):
		current, localsum = stack.pop()
		if not current.left and not current.right:
			if target == localsum:
				return True
		else:
			if current.left:
				stack.append([current.left, current.left.val + localsum])
			if current.right:
				stack.append([current.right, current.right.val + localsum])
	return False

def main():
	root = TreeNode(12)
	root.left = TreeNode(7)
	root.right = TreeNode(1)
	root.left.left = TreeNode(9)
	root.right.left = TreeNode(10)
	root.right.right = TreeNode(5)  
	print("Tree has path: " + str(has_path(root, 23)))
	print("Tree has path: " + str(has_path(root, 16)))
main()