"""
25. Reverse Nodes in k-Group

Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

You may not alter the values in the nodes, only nodes itself may be changed.

Only constant memory is allowed.

For example,
Given this linked list: 1->2->3->4->5

For k = 2, you should return: 2->1->4->3->5

For k = 3, you should return: 3->2->1->4->5

"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# http://www.cnblogs.com/zuoyuan/p/3785555.html
class Solution:
    # @param head, a ListNode
    # @param k, an integer
    # @return a ListNode
    def reverse(self, start, end):
        newhead = ListNode(0);
        newhead.next = start

        while newhead.next != end:
            tmp = start.next
            start.next = tmp.next
            tmp.next = newhead.next
            newhead.next = tmp

        return [end, start]

    def reverseKGroup(self, head, k):
        if head == None: return None
        nhead = ListNode(0);
        nhead.next = head;
        start = nhead
        while start.next:
            end = start
            for i in range(k - 1):
                end = end.next
                if end.next == None: return nhead.next
            res = self.reverse(start.next, end.next)
            start.next = res[0]
            start = res[1]

        return nhead.next
