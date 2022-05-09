class Node():
	def __init__(self, item):
		self.left = None
		self.right =  None
		self.item = item



# in ->  	left root right
# pre -> 	root left right
# post ->	left right root 


def dfs(root: Node):
	if root is None: return []

	visited = []
	stack = []
	stack.append(root)

	while len(stack) > 0 and root is not None:
		current_node = stack.pop()
		if current_node.right: 
			stack.append(current_node.right)
		if current_node.left: 
			stack.append(current_node.left)
		visited.append(current_node.item)
	print()
	print('-----------------')
	return visited




def bfs(root: Node):
	if root is None:
		return []

	visited = []
	queue = []
	queue.append(root)

	while len(queue) > 0 and root is not None:
		print(len(queue))
		current_node = queue.pop(0)
		visited.append(current_node.item)

		if current_node.left: 
			queue.append(current_node.left)
		if current_node.right: 
			queue.append(current_node.right)
		
		
	print()
	print('-----------------')
	return visited
		
		
	



tree = Node(1)
tree.right = Node(3)
tree.left = Node(2)
tree.left.right = Node(5)
tree.left.left = Node(4)

root = Node('root')
root.left = Node('left')
root.right = Node('right')
# root.left.left = Node(6)
# root.left.right = Node(8)


print(bfs(tree))



