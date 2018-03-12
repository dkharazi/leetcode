"""
86. Partition List

Given a linked list and a value x,
partition it such that all nodes less than x
come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes
in each of the two partitions.

For example,
Given 1->4->3->2->5->2 and x = 3,
return 1->2->2->4->3->5.

"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        return "{} -> {}".format(self.val, self.next)


class Solution(object):
    def partition(self, head, x):
        """
        http://blog.csdn.net/aliceyangxi1987/article/details/50739983

        use p to move from head to end
        and compare each value with x

        create two dummy point,
        one is used to link points that are <x,
        another is to link points that are >=x

        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """

        # if not head or not head.next or not x:
        #    return head

        p1 = head1 = ListNode(0)
        p2 = head2 = ListNode(0)
        p = head

        while p:
            if p.val < x:
                p1.next = p
                p1 = p1.next
            else:
                p2.next = p
                p2 = p2.next
            p = p.next
        # now list1 contains nodes <x
        # list2 contains nodes >=x

        # concatenate list1 to list2
        p1.next = head2.next
        p2.next = None

        return head1.next

    # remove variable p
    def partition(self, head, x):
        p1 = dummy1 = ListNode(0)
        p2 = dummy2 = ListNode(0)

        while head:
            if head.val < x:
                p1.next = head
                p1 = p1.next
            else:
                p2.next = head
                p2 = p2.next
            head = head.next
        p1.next = dummy2.next
        p2.next = None
        return dummy1.next


if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(4)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(2)
    head.next.next.next.next = ListNode(5)
    head.next.next.next.next.next = ListNode(2)

    print head
    print Solution().partition(head, 3)
