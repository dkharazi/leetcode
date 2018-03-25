# 138. Copy List with Random Pointer
#
# A linked list is given such that each node contains an additional random pointer
# which could point to any node in the list or null.
#
# Return a deep copy of the list.


# Definition for singly-linked list with a random pointer.
class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None


class Solution(object):
    def copyRandomList(self, head):
        """
        http://www.cnblogs.com/zuoyuan/p/3745126.html

        解题思路：这题主要是需要深拷贝。看图就明白怎么写程序了。

        首先，在原链表的每个节点后面都插入一个新节点，新节点的内容和前面的节点一样。比如上图，1后面插入1，2后面插入2，依次类推。

        其次，原链表中的random指针如何映射呢？比如上图中，1节点的random指针指向3，4节点的random指针指向2。
        如果有一个tmp指针指向1（蓝色），则一条语句：tmp.next.random = tmp.random.next；就可以解决这个问题。

        第三步，将新的链表从上图这样的链表中拆分出来。

        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if head is None:
            return None

        # add a new node after every old node
        tmp = head
        while tmp:
            newNode = RandomListNode(tmp.label)
            newNode.next = tmp.next
            tmp.next = newNode
            tmp = tmp.next.next

        # fix random
        tmp = head
        while tmp:
            if tmp.random:
                tmp.next.random = tmp.random.next
            tmp = tmp.next.next # only loop over old lists

        # separate two lists
        newhead = head.next
        pold = head
        pnew = newhead
        while pnew.next:
            pold.next = pnew.next
            pold = pold.next
            pnew.next = pold.next
            pnew = pnew.next
        pold.next = None
        pnew.next = None

        return newhead
