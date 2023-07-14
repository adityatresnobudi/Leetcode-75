# Make list of every node of list, and calculate number of nodes.
# If node is even then k = ceil(n/2) else n // 2 (because we want second middle)
# If length is 1 then return None (after deletion list will be empty)
# Else make middle node's previous .next to middle node's .next (skipping the middle number)
# return output[0], head of updated list.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from math import ceil
class Solution(object):
    def deleteMiddle(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        output = []
        length = 0
        pop = 0
        while head:
            output.append(head)
            length += 1
            head = head.next
        if length % 2 == 0:
            pop = int(length // 2)
        else:
            pop = int(ceil(length / 2))
        
        if length == 1:
            return None
        else:
            output[pop - 1].next = output[pop].next
            return output[0]
