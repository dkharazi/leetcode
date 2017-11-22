# -*- coding: utf-8 -*-
# 232. Implement Queue using Stacks
#
# Implement the following operations of a queue using stacks.
#
#     push(x) -- Push element x to the back of queue.
#     pop() -- Removes the element from in front of queue.
#     peek() -- Get the front element.
#     empty() -- Return whether the queue is empty.
#
# Notes:
#
#     You must use only standard operations of a stack -- which means only push to top, peek/pop from top, size,
# and is empty operations are valid.
#     Depending on your language, stack may not be supported natively.
# You may simulate a stack by using a list or deque (double-ended queue),
# as long as you use only standard operations of a stack.
#     You may assume that all operations are valid
# (for example, no pop or peek operations will be called on an empty queue).
#
# http://blog.csdn.net/coder_orz/article/details/51586814
# 这个题目的关键点在于，只能用栈的几个操作实现。
# 由于栈先进后出，和队列先进先出天然矛盾，
# 故考虑采用两个栈，一个只进行入栈push操作，一个只进行出栈pop或peek操作。
# 当只进行出栈操作的栈空时, 将另一个栈中的内容push到该栈，
# 如此，就拥有了先进先出的特性。

class MyQueue(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.inStack, self.outStack = [], []

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        self.inStack.append(x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        self.peek() # peek first
        self.outStack.pop()

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        if not self.outStack:
            while self.inStack:
                self.outStack.append(self.inStack.pop())
        return self.outStack[-1]


    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        # both instack and outstack should be empty
        return not self.inStack and not self.outStack



# Your MyQueue object will be instantiated and called as such:
obj = MyQueue()
obj.push(1)
obj.push(2)
obj.push(3)
param_2 = obj.pop()
param_3 = obj.peek()
print param_3   # 2
param_4 = obj.empty()
print param_4