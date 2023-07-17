# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        stack, subtree = [], None
        while True:
            while root:
                if root.val == val:
                    return root
                stack.append(root)
                root = root.left
            if not stack:
                return None
            root = stack.pop().right
