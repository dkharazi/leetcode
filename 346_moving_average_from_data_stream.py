# 346. Moving Average from Data Stream   

# Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.

# For example,
	
# MovingAverage m = new MovingAverage(3);
# m.next(1) = 1
# m.next(10) = (1 + 10) / 2
# m.next(3) = (1 + 10 + 3) / 3
# m.next(5) = (10 + 3 + 5) / 3

 
class MovingAverage(object):

    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.size = size
        self.vals = [0] * size
        self.cnt = 0
        self.sum = 0

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        self.cnt += 1
        idx = (self.cnt - 1) % self.size

        # replace old value
        self.sum -= self.vals[idx]
        self.sum += val
        self.vals[idx] = val
        return float(self.sum) / self.cnt if self.cnt < self.size \
            else float(self.sum) / self.size
        # return float(self.sum) / min(self.cnt, self.size)
        # return float(self.sum) / [self.cnt, self.size][self.cnt > self.size]
# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)

if __name__ == '__main__':
    m = MovingAverage(3)
    assert m.next(1) == 1
    assert m.next(10) == (1 + 10) / 2
    assert m.next(3) == (1 + 10 + 3) / 3
    assert m.next(5) == (10 + 3 + 5) / 3