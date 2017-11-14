# -*- coding: utf-8 -*-
#  225. Implement Stack using Queues
#
#  Implement the following operations of a stack using queues.
#
#     push(x) -- Push element x onto stack.
#     pop() -- Removes the element on top of the stack.
#     top() -- Get the top element.
#     empty() -- Return whether the stack is empty.
#
# Notes:
#
#     You must use only standard operations of a queue --
# which means only push to back, peek/pop from front, size, and is empty operations are valid.
#     Depending on your language, queue may not be supported natively.
# You may simulate a queue by using a list or deque (double-ended queue),
# as long as you use only standard operations of a queue.
#     You may assume that all operations are valid
# (for example, no pop or top operations will be called on an empty stack).
#
# http://blog.csdn.net/coder_orz/article/details/51605052
# 队列是先进先出，每次出只能出队列的头部，而栈是后进先出，
# 所以可以想办法每次把入队的元素弄到队列头部。
# 于是可以考虑在每次push到队列的时候对其他元素做个重新pop和push将当前元素转移到队头。
# 该方法需要一个队列，push的复杂度O(n)，pop的复杂度O(1)。

class MyStack(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = []

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        # queue insert at front
        self.stack.insert(0, x)
        # move all elements except x (thus len-1) to front
        for i in range(len(self.stack) - 1):
            # insert the last element to the front
            self.stack.insert(0, self.stack[-1])
            # pop the last element so that
            # length of array not changed
            self.stack.pop()

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        self.stack.pop()

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        return self.stack[-1]

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return not self.stack



        # Your MyStack object will be instantiated and called as such:
        # obj = MyStack()
        # obj.push(x)
        # param_2 = obj.pop()
        # param_3 = obj.top()
        # param_4 = obj.empty()