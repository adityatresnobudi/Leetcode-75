# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def pairSum(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
        node = []
        total = 0
        while head:
            node.append(head)
            head = head.next
        for i in range(int(len(node) / 2)):
            total = max(total, node[i].val + node[len(node)-i-1].val)
        return total
