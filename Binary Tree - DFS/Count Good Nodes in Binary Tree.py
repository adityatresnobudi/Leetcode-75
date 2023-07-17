# traversing through the tree
# for every root visited, check if the value is greater than maximum on the path traversed
# if yes then count + 1 else count + 0
# if root is empty then return 0
# else return count

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        
        def countGoodNodes(root, currMax):
            if not root:
                return
            if root.val >= currMax:
                count[0] += 1
                currMax = root.val
            countGoodNodes(root.left, currMax)
            countGoodNodes(root.right, currMax)
        
        count = [0]
        countGoodNodes(root, root.val)
        
        return count[0]
