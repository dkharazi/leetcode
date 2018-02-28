"""
19. Remove Nth Node From End of List

Given a linked list, remove the nth node from the end of list and return its head.

For example,

   Given linked list: 1->2->3->4->5, and n = 2.

   After removing the second node from the end, the linked list becomes 1->2->3->5.

Note:
Given n will always be valid.
Try to do this in one pass.
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        s = ""
        if self != None:
            while self.next != None:
                s += str(self.val)
                s += "->"
                self = self.next
            s += str(self.val)
        return s


class Solution(object):
    # 2 pass. one pass to find the length
    def removeNthFromEnd(self, head, n):
        p = q = dummy = ListNode(0)
        dummy.next = head
        m = 0
        # calculate length of the list
        while p:
            m += 1
            p = p.next

        for _ in range(m - n - 1):
            q = q.next
        q.next = q.next.next
        return dummy.next

    # 3 pointers
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """

        p = q = dummy = ListNode(0)
        dummy.next = head

        # p, q points to dummy, instead of head
        # in order for the remove (double next) to work, when there is only 1 element

        # advance p n steps first
        for _ in range(n):
            p = p.next

        # advance p, q together to find the node to be removed
        # when p.next is None, q.next is the node to be removed.
        # do not use when p is None; q already passed the one to remove. too late.
        while p.next:
            p = p.next
            q = q.next

        # q.next is the node to be removed; q is not.
        q.next = q.next.next

        return dummy.next


if __name__ == '__main__':
    l = ListNode(1)
    l.next = ListNode(2)
    l.next.next = ListNode(3)
    l.next.next.next = ListNode(4)
    l.next.next.next.next = ListNode(5)

    print l
    print Solution().removeNthFromEnd(l, 2)
