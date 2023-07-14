# append head to array, while counting the length
# iterate through array, every node.next = node[index+1].next
# if index + 2 > array length, check if the index is on the last one then node.next = first number on even index
# else (one index before the last one), then node.next = None
# if head = [] then return head
# if array length = 1 then return array

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        node = []
        length = 0
        if head == None:
            return head
        while head:
            node.append(head)
            length += 1
            head = head.next
        if length == 1:
            return node[0]
        for i in range(length):
            if i+2 < length:
                node[i].next = node[i+1].next
            else:
                if i % 2 != 0:
                    node[i].next = None
                else:
                    node[i].next = node[1]
        return node[0]
