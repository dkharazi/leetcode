# 284. Peeking Iterator

# Given an Iterator class interface with methods: next() and hasNext(), 
# design and implement a PeekingIterator that support the peek() operation -- 
# it essentially peek() at the element that will be returned by the next call to next().

# Here is an example. 
# Assume that the iterator is initialized to the beginning of the list: [1, 2, 3].

# Call next() gets you 1, the first element in the list.

# Now you call peek() and it returns 2, the next element. Calling next() after that still return 2.

# You call next() the final time and it returns 3, the last element. 
# Calling hasNext() after that should return false.

# Hint:
# Think of "looking ahead". You want to cache the next element.
# Is one variable sufficient? Why or why not?
# Test your design with call order of peek() before next() vs next() before peek().
# For a clean implementation, check out Google's guava library source code.

# Follow up: How would you extend your design to be generic and work with all types, not just integer?

# Below is the interface for Iterator, which is already defined for you.

class Iterator(object):
    def __init__(self, nums):
        """
        Initializes an iterator object to the beginning of a list.
        :type nums: List[int]
        """
        self.it = iter(nums)

    def hasNext(self):
        """
        Returns true if the iteration has more elements.
        :rtype: bool
        """
        return 

    def next(self):
        """
        Returns the next element in the iteration.
        :rtype: int
        """
        # it = iter(self.nums)
        return next(self.it)

# http://bookshadow.com/weblog/2015/09/21/leetcode-peeking-iterator/
# 引入两个额外的变量nextElement和peekFlag:
# nextElement标识peek操作预先获取的下一个元素，
# peekFlag记录当前是否已经执行过peek操作

class PeekingIterator(object):
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.iter = iterator
        self.peekFlag = False
        self.nextElement = None


    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        if not self.peekFlag:           # save next element and set flag to true
            self.nextElement = self.iter.next()
            self.peekFlag = True
        return self.nextElement



    def next(self):
        """
        :rtype: int
        """
        if not self.peekFlag:           # return normal next
            return self.iter.next()
        nextElement = self.nextElement  # save next element
        self.peekFlag = False           # reset attributes back
        self.nextElement = None
        return nextElement


    def hasNext(self):
        """
        :rtype: bool
        """
        return self.peekFlag or self.iter.hasNext()

# Your PeekingIterator object will be instantiated and called as such:
nums = [1, 2, 3]
it = PeekingIterator(Iterator(nums))

val = it.peek() 
print(val)
it.next()
val = it.peek() 
print(val)
# while it.hasNext():
#     val = it.peek()   # Get the next element but not advance the iterator.
#     it.next()         # Should return the same value as [val].
