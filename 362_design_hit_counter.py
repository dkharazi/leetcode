# 362. Design Hit Counter

# Design a hit counter which counts the number of hits received in the past 5 minutes.

# Each function accepts a timestamp parameter (in seconds granularity) 
# and you may assume that calls are being made to the system in chronological order 
# (ie, the timestamp is monotonically increasing). 
# You may assume that the earliest timestamp starts at 1.

# It is possible that several hits arrive roughly at the same time.

# Example:

# HitCounter counter = new HitCounter();

# // hit at timestamp 1.
# counter.hit(1);

# // hit at timestamp 2.
# counter.hit(2);

# // hit at timestamp 3.
# counter.hit(3);

# // get hits at timestamp 4, should return 3.
# counter.getHits(4);

# // hit at timestamp 300.
# counter.hit(300);

# // get hits at timestamp 300, should return 4.
# counter.getHits(300);

# // get hits at timestamp 301, should return 3.
# counter.getHits(301);

from collections import deque

# https://github.com/algorhythms/LeetCode/blob/master/362%20Design%20Hit%20Counter.py
class HitCounter:
    def __init__(self):
        """
        Initialize your data structure here.
        calls are being made to the system in chronological order.
        It is possible that several hits arrive roughly at the same time.
        What if the number of hits per second could be very large? Does your design scale?  # use counter
        """
        self.q = deque()

    def hit(self, timestamp):
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: void
        """
        self.q.append(timestamp)

    def getHits(self, timestamp):
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: int
        """
        while self.q and timestamp - self.q[0] >= 300:
            self.q.popleft()
        return len(self.q)

counter = HitCounter()

# hit at timestamp 1.
counter.hit(1);

# hit at timestamp 2.
counter.hit(2);

# hit at timestamp 3.
counter.hit(3);

# get hits at timestamp 4, should return 3.
print counter.getHits(4);

# hit at timestamp 300.
counter.hit(300);

# get hits at timestamp 300, should return 4.
print counter.getHits(300);

# get hits at timestamp 301, should return 3.
print counter.getHits(301);



