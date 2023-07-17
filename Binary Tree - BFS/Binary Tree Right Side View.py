# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def rightView(root, depth):
            if root:
                if len(output) == depth:
                    output.append(root.val)
                rightView(root.right, depth+1)
                rightView(root.left, depth+1)
            return
        output = []
        rightView(root, 0)
        return output
