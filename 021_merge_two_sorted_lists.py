# 21. Merge Two Sorted Lists
#
# Merge two sorted linked lists and return it as a new list.
# The new list should be made by splicing together the nodes of the first two lists.
#
# https://github.com/gengwg


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        if self:
            return "{} -> {}".format(self.val, self.next)


class Solution:
    def mergeTwoLists(self, l1, l2):
        curr = dummy = ListNode(0)
        while l1 and l2:
            # connect curr to the smaller value node
            # and advance smaller node
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            # advance curr to the above smaller node
            curr = curr.next
        # connect curr to the rest of longer list
        curr.next = l1 or l2
        return dummy.next

if __name__ == "__main__":
    l1 = ListNode(1)
    l1.next = ListNode(5)

    l2 = ListNode(2)
    l2.next = ListNode(3)
    l2.next.next = ListNode(4)

    print l1
    print l2
    print Solution().mergeTwoLists(l1, l2)
