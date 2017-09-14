# 203. Remove Linked List Elements
#
# Remove all elements from a linked list of integers that have value val.
#
# Example
# Given: 1 --> 2 --> 6 --> 3 --> 4 --> 5 --> 6, val = 6
# Return: 1 --> 2 --> 3 --> 4 --> 5


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if not head:
            return
        # move to the first node that is not equal to val
        while head and head.val == val:
            head = head.next

        p = head
        while p and p.next:
            if p.next.val == val:
                p.next = p.next.next
                # continue
            else:
                p = p.next

        return head

    # http://bookshadow.com/weblog/2015/04/24/leetcode-remove-linked-list-elements/
    # use a dummy head node so that do not need move head to not equal val
    def removeElements(self, head, val):
        dummy = ListNode(0)
        dummy.next = head
        p = dummy
        while p and p.next:
            if p.next.val == val:
                p.next = p.next.next
            else:
                p = p.next

        return dummy.next

    # two cursors
    def removeElements(self, head, val):
        dummy = ListNode(0)
        dummy.next = head
        pre, cur = dummy, head
        while cur:
            if cur.val == val:
                pre.next = cur.next
            else:
                pre = cur
            cur = cur.next
        return dummy.next
