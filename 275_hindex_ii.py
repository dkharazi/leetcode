# 275. H-Index II
# Follow up for H-Index: What if the citations array is sorted in ascending order? Could you optimize your algorithm?

class Solution(object):
    # http://blog.csdn.net/titan0427/article/details/50650006
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        n = len(citations)
        start, end = 1, n
        while start <= end:
            h = (start + end) / 2
            if citations[n-h] < h:
                end = h-1
            elif n-h-1 >= 0 and citations[n-h-1] > h:
                start = h+1
            else:
                return h
        return 0
