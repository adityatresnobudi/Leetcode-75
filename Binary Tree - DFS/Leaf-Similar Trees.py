# using recursive
# traversal preorder
# base case => if root left and right is None then it's leaf
# regular case => when root left is not None then recursive root.left, the same with right

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def checkleaf(self, root):
        left = []
        right = []
        if root.left is None and root.right is None:
            return [root.val]
        else:
            if root.left is not None:
                left = self.checkleaf(root.left)
            if root.right is not None:
                right = self.checkleaf(root.right)
            return left + right
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        leaf1 = self.checkleaf(root1)
        leaf2 = self.checkleaf(root2)
        return leaf1 == leaf2
