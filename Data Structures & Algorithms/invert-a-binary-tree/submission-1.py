# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def switch(root):
            if root == None:
                return
            if root.left != None and root.right != None:
                dummy = root.left
                root.left = root.right
                root.right = dummy
                switch(root.left)
                switch(root.right)
                return root
            if root.left != None:
                root.right = root.left
                root.left = None
                switch(root.right)
                return root
            else:
                root.left = root.right
                root.right = None
                switch(root.left)
                return root
        return switch(root)
                