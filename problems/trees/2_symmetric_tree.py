from typing import Optional
Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        if root is None:
            return True

        if root.left is None and root.right is None:
            return True

        if root.left == None and root.right !=None:
            return False
        if root.left != None and root.right == None:
            return False

        left_tree = root.left
        right_tree = root.right

        queue = []
        queue.append((left_tree, right_tree))
        while len(queue) > 0:
            lt, rt = queue.pop(0)

            if lt is None or lt is None:
                return False
            if lt.val != rt.val:
                return False

            if lt.left and rt.right:
                queue.append((lt.left, rt.right))
            elif lt.left or rt.right:
                return False
            if lt.right and rt.left:
                queue.append((lt.right, rt.left))
            elif lt.right or rt.left:
                return False
        return True
            






        