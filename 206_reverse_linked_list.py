# 206. Reverse Linked List
#
# Reverse a singly linked list.
#
# click to show more hints.
#
# Hint:
# A linked list can be reversed either iteratively or recursively. Could you implement both?

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


# http://bookshadow.com/weblog/2015/05/05/leetcode-reverse-linked-list/
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # dummy-->None
        dummy = ListNode(0)
        # loop over all nodes, and insert each right after dummy node
        while head:
            # 1. use a temp variable to store next node after head
            next = head.next
            # 2. insert head between dummy and node after dummy
            # 2.1 point head to dummy.next
            head.next = dummy.next
            # 2.2 point dummy to head
            dummy.next = head
            # 3. advance head
            head = next

        return dummy.next

    def reverseList(self, head):
        return self.doReverse(head, None)

    def doReverse(self, head, newHead):
        if head is None:
            return newHead
        next = head.next
        head.next = newHead
        return self.doReverse(next, head)
