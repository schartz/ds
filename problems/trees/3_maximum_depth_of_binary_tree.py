# https://leetcode.com/problems/maximum-depth-of-binary-tree/

from typing import Optional

Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 1
        
        queue = []
        levels = []
        queue.append((root, 1))
        
        
        while len(queue) > 0:
            node, level = queue.pop(0)
            
            print(node.val)
            
            if node.left:
                queue.append((node.left, level + 1))
                levels.append(level + 1)

            if node.right:
                queue.append((node.right, level + 1))
                levels.append(level + 1)
            
            
        return max(levels)



    def maxDepth_better(self, root: Optional[TreeNode]) -> int:
	    if root is None:
	        return 0
	    if root.left is None and root.right is None:
	        return 1
	    
	    queue = []
	    depth = 1
	    queue.append((root, depth))
	    
	    
	    while len(queue) > 0:
	        node, level = queue.pop(0)
	        depth = max(depth, level)
	        if node.left:
	            queue.append((node.left, level + 1))

	        if node.right:
	            queue.append((node.right, level + 1))
	        
	    return depth
        
