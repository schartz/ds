class TreeNode:
	def __init__(self, value):
		self.val = value
		self.left = None
		self.right = None
	def __repr__(self):
		return str(self.val)


def has_path(root, target):
	paths = []

	# create a stack with [root, pathsum, path]
	stack = [[root, root.val, [root]]]
	while len(stack) > 0:
		current, pathsum, path = stack.pop()
		if not current.left and not current.right:
			if pathsum == target:
				paths.append(path)
		else:
			if current.left:
				stack.append([current.left, pathsum + current.left.val, path+[current.left]])
			if current.right:
				stack.append([current.right, pathsum + current.right.val, path+[current.right]])
	return paths

def main():
	root = TreeNode(12)
	root.left = TreeNode(7)
	root.right = TreeNode(1)
	root.left.left = TreeNode(4)
	root.right.left = TreeNode(10)
	root.right.right = TreeNode(5)  
	print("Tree has path: " + str(has_path(root, 23)))
main()