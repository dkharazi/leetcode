# 382. Linked List Random Node

# Given a singly linked list, return a random node's value from the linked list.
# Each node must have the same probability of being chosen.
#
# Follow up:
# What if the linked list is extremely large and its length is unknown to you?
# Could you solve this efficiently without using extra space?
#
# Example:
#
# // Init a singly linked list [1,2,3].
# ListNode head = new ListNode(1);
# head.next = new ListNode(2);
# head.next.next = new ListNode(3);
# Solution solution = new Solution(head);
#
# // getRandom() should return either 1, 2, or 3 randomly.
# // Each element should have equal probability of returning.
# solution.getRandom();


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# https://www.hrwhisper.me/leetcode-linked-list-random-node/

# 题意: 给定一个链表，要求以相等的概率返回链表上的结点。

# 思路：
#
# 若已知链表长度len，那么直接随机一下0~len-1，然后遍历到那个结点。
#
# 如果不知道长度呢？
#
# 我们实时的计算当前遍历了多少个元素cnt，然后以 1/cnt 的概率选择 当前的元素，直到遍历完链表。
#
# 这样遍历一遍即可。
#
# 为啥是对的？
#
# 我们以第2个数为例（就是head.next.val）
#
# 选取的概率为(1/2)* （2/3）*（3/4）* ……….. (n-1) / n = 1/n
# （选取第2个数在长度为2的时候为1/2，其他的都不要选)
#
# 而对于任意的第x数，由于可以覆盖前面的数，均有： (1/x) * (x/(x+1)) *…….(n-1) / n = 1/n
#
# 第n个数就直接1/n啦
#
# 大家都是1/n~


class Solution(object):
    def __init__(self, head):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        :type head: ListNode
        """
        self.head = head

    def getRandom(self):
        """
        Returns a random node's value.
        :rtype: int
        """
        import random
        # 在代码实现上，这里的cnt 比上面讲解中的cnt 少1   randint(x,y)返回的为[x,y]的闭区间。
        ans = cnt = 0
        # save some typing by asigning it to a variable
        head = self.head
        while head:
            if random.randint(0, cnt) == 0:  # possibility is 1/cnt
                ans = head.val
            head = head.next
            cnt = cnt + 1
        return ans

# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
