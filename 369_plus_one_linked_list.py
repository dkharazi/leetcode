# 369. Plus One Linked List

# Given a non-negative number represented as a singly linked list of digits, 
# plus one to the number.

# The digits are stored such that the most significant digit is at the head of the list.

# Example:

# Input:
# 1->2->3

# Output:
# 1->2->4

class Solution:
    # https://closewen.wordpress.com/2017/04/17/369-plus-one-linked-list/

    # 遍历链表，找到第一个不为9的数字，如果找不这样的数字，说明所有数字均为9，
    # 那么在表头新建一个值为0的新节点，进行加1处理，然后把右边所有的数字都置为0即可。
    # 举例来说：

    # 比如1->2->3，那么第一个不为9的数字为3，对3进行加1，变成4，
    # 右边没有节点了，所以不做处理，返回1->2->4。

    # 再比如说8->9->9，找第一个不为9的数字为8，进行加1处理变成了9，
    # 然后把后面的数字都置0，得到结果9->0->0。

    # 再来看9->9->9的情况，找不到不为9的数字，那么再前面新建一个值为0的节点，
    # 进行加1处理变成了1，把后面的数字都置0，得到1->0->0->0。
    def plusOne(self, head):
        cur = head
        right = None
        while cur:
            if cur.val != 9:
                right = cur
            cur = cur.next

        if not right:
            right = ListNode(0)
            right.next = head
            head = right

        right.val += 1
        cur = right.next
        while cur:
            cur.val = 0
            cur = cur.next

        return head
