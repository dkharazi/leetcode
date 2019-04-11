# 295. Find Median from Data Stream
#
# Median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value.
# So the median is the mean of the two middle value.
#
# Examples:
#
# [2,3,4] , the median is 3
#
# [2,3], the median is (2 + 3) / 2 = 2.5
#
# Design a data structure that supports the following two operations:
#
#     void addNum(int num) - Add a integer number from the data stream to the data structure.
#     double findMedian() - Return the median of all elements so far.
#
# For example:
#
# add(1)
# add(2)
# findMedian() -> 1.5
# add(3)
# findMedian() -> 2
#

# http://bookshadow.com/weblog/2015/10/19/leetcode-find-median-data-stream/

# 维护大顶堆（MaxHeap） + 小顶堆（MinHeap）
#
# 需要满足下面的约束条件：
#
#     大顶堆中存储的元素 均不大于 小顶堆中的元素
#     MaxHeap.size() == MinHeap.size()，或者 MaxHeap.size() == MinHeap.size() + 1
#
# 则有：
#
#     当MaxHeap.size() == MinHeap.size() + 1时，中位数就是MaxHeap的堆顶元素
#     当MaxHeap.size() == MinHeap.size()时，中位数就是MaxHeap堆顶元素与MinHeap堆顶元素的均值
#
# 使用Python的内置堆算法heapq可以很容易地实现小顶堆，而大顶堆可以通过对元素的值 * -1实现。
#
# 参考Python标准库文档：https://docs.python.org/2/library/heapq.html

from heapq import *
class MedianFinder:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.minheap = []
        self.maxheap = []

    def addNum(self, num):
        """
        Adds a num into the data structure.
        :type num: int
        :rtype: void
        """
        heappush(self.maxheap, -num)
        mintop = self.minheap[0] if len(self.minheap) else 0
        maxtop = self.maxheap[0] if len(self.maxheap) else 0
        if mintop < -maxtop or len(self.minheap) + 1 < len(self.maxheap):
            heappush(self.minheap, -heappop(self.maxheap))
        if len(self.maxheap) < len(self.minheap):
            heappush(self.maxheap, -heappop(self.minheap))

    def findMedian(self):
        """
        Returns the median of current data stream
        :rtype: float
        """
        if len(self.minheap) < len(self.maxheap):
            return -1 * self.maxheap[0]
        else:
            return (self.minheap[0] - self.maxheap[0]) / 2

# Your MedianFinder object will be instantiated and called as such:
mf = MedianFinder()
mf.addNum(1)
mf.addNum(2)
mf.addNum(3)
print(mf.findMedian())
