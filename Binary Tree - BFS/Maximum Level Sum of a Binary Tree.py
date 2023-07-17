# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxLevelSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        total = defaultdict(int)
        total[0] = -(10**5)-1
        total[1] = 0
        def levelSum(root, lvl):
            if root:
                total[lvl] += root.val
                levelSum(root.left, lvl+1)
                levelSum(root.right, lvl+1)
            lvl -= 1
            return
        levelSum(root, 1)
        key_list = list(total.keys())
        val_list = list(total.values())
        pos = val_list.index(max(val_list))
        return key_list[pos]
