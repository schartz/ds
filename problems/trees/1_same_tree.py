# https://leetcode.com/problems/same-tree/

from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        queue = []
        queue.append((p, q))

        if not p and not q:
            return True


        while len(queue) > 0:
            curr_p, curr_q  = queue.pop(0)

            if curr_p and not curr_q:
                return False
            if curr_q and not curr_p:
                return False

            if curr_p.val != curr_q.val:
                return False

            if curr_p.left or curr_q.left:
                queue.append((curr_p.left, curr_q.left))

            if curr_p.right or curr_q.right:
                queue.append((curr_p.right, curr_q.right))
        return True