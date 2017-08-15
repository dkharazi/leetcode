"""
24. Swap Nodes in Pairs

Given a linked list, swap every two adjacent nodes and return its head.

For example,
Given 1->2->3->4, you should return the list as 2->1->4->3.

Your algorithm should use only constant space.
You may not modify the values in the list, only nodes itself can be changed.

author: https://github.com/gengwg/leetcode
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

    def __repr__(self):
        return "{} -> {}".format(self.val, self.next)

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head

        p = dummy = ListNode(0); dummy.next = head
        while p.next and p.next.next:
            # exchange p.next and p.next.next

            tmp = p.next.next
            p.next.next = tmp.next
            # before deleting the link
            # we need store its addr in a tmp variable
            tmp.next = p.next
            p.next = tmp

            # advance 2 nodes
            p = p.next.next
        return dummy.next


if __name__ == '__main__':
    l = ListNode(1)
    l.next = ListNode(2)
    l.next.next = ListNode(3)
    #l.next.next.next = ListNode(4)

    print l
    print Solution().swapPairs(l)
