# -*- coding: utf-8 -*-
"""
92. Reverse Linked List II

Reverse a linked list from position m to n.
Do it in-place and in one-pass.

For example:
Given 1->2->3->4->5->NULL, m = 2 and n = 4,

return 1->4->3->2->5->NULL.

Note:
Given m, n satisfy the following condition:
1 ≤ m ≤ n ≤ length of list.
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        return "{} -> {}".format(self.val, self.next)


class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """

        if head is None or head.next is None:
            return head

        dummy = ListNode(0)
        dummy.next = head
        head1 = dummy
        for i in range(m - 1):
            head1 = head1.next

        p = head1.next
        for i in range(n - m):
            tmp = head1.next
            head1.next = p.next
            p.next = p.next.next
            head1.next.next = tmp

        return dummy.next

    # https://gengwg.blogspot.com/2018/03/leetcode-92-reverse-linked-list-ii.html
    # two pointers
    def reverseBetween(self, head, m, n):
        if head is None or head.next is None:
            return head

        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        curr = dummy.next

        for _ in range(m-1):
            curr = curr.next
            prev = prev.next

        for _ in range(n-m):
            temp = curr.next        # save next
            curr.next = temp.next   # point current to next.next
            temp.next = prev.next   # reverse: point next.next to next
            prev.next = temp        # point prev to temp

        return dummy.next


if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    head.next.next.next.next.next = ListNode(6)

    print Solution().reverseBetween(head, 2, 4)
