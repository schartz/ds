class TreeNode:
	def __init__(self, value):
		self.val = value
		self.left = None
		self.right = None
		self.next = None
	
	def __repr__(self):
		return str(self.val)

	def print_level_order(self):
		nextLevelRoot = self
		while nextLevelRoot:
			current = nextLevelRoot
			nextLevelRoot = None
			while current:
				print(str(current.val) + " ", end='')
				if not nextLevelRoot:
					if current.left:
						nextLevelRoot = current.left
					elif current.right:
						nextLevelRoot = current.right
				current = current.next
			print()

def connect_level_order_siblings(root):
	q = [root]

	while len(q) > 0:
		level = []
		previous = None
		for _ in range(len(q)):
			current = q.pop(0)
			level.append(current)
			if previous:
				previous.next = current
			previous = current

			level.append(current)
			if current.left: q.append(current.left)
			if current.right: q.append(current.right)


def main():
	root = TreeNode(12)
	root.left = TreeNode(7)
	root.right = TreeNode(1)
	root.left.left = TreeNode(9)
	root.right.left = TreeNode(10)
	root.right.right = TreeNode(5)
	connect_level_order_siblings(root)
	print("Level order traversal using 'next' pointer: ")
	root.print_level_order()

main()
