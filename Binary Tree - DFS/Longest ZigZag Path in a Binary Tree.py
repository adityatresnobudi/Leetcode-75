# traverse tree, if go left then isLeft = 1, if go right then isLeft = 0
# everytime we took a different way, we do count + 1
# if root is None then return 0
# else return count

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def longestZigZag(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(node, isLeft, count):
            if not node:
                return count
            if isLeft:
                return max(dfs(node.right, False, count + 1), dfs(node.left, True, 0))
            return max(dfs(node.left, True, count + 1), dfs(node.right, False, 0))
        return max(dfs(root.left, True, 0), dfs(root.right, False, 0))
