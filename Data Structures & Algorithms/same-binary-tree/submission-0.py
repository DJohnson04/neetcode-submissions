# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def rec(p,q):
            print(p, q)
            if (p == None and q != None) or (p != None and q == None): return False
            if p == None and q == None: return True
            if p.val != q.val: return False
            left = rec(p.left, q.left)
            right = rec(p.right,q.right)
            return left and right
        return rec(p,q)