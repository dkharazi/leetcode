# 155. Min Stack
#
# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
#
# push(x) -- Push element x onto stack.
# pop() -- Removes the element on top of the stack.
# top() -- Get the top element.
# getMin() -- Retrieve the minimum element in the stack.
# Example:
# MinStack minStack = new MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.getMin();   --> Returns -3.
# minStack.pop();
# minStack.top();      --> Returns 0.
# minStack.getMin();   --> Returns -2.

# http://www.cnblogs.com/zuoyuan/p/4091870.html
# use 2 stack. one for ordinary stack; one for keeping min.
# using one stack will tle


class MinStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack1 = []
        self.stack2 = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.stack1.append(x)
        if not self.stack2 or x <= self.stack2[-1]:
            self.stack2.append(x)

    def pop(self):
        """
        :rtype: void
        """
        top = self.stack1[-1]
        self.stack1.pop()
        if top == self.stack2[-1]:
            self.stack2.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.stack1[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.stack2[-1]


if __name__ == '__main__':
    minStack = MinStack();
    # print minStack.getMin()
    minStack.push(-2)
    minStack.push(0)
    minStack.push(-3)
    print minStack.getMin()  # --> Returns - 3.
    minStack.pop()
    print minStack.top()  # 0
    print minStack.getMin()  # --> Returns - 2.

    # Your MinStack object will be instantiated and called as such:
    # obj = MinStack()
    # obj.push(x)
    # obj.pop()
    # param_3 = obj.top()
    # param_4 = obj.getMin()
