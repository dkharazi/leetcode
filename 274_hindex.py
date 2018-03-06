# -*- coding: utf-8 -*-
#
# 274. H-Index
# 
# Given an array of citations (each citation is a non-negative integer) of a researcher, 
# write a function to compute the researcher's h-index.

# According to the definition of h-index on Wikipedia: 
# "A scientist has index h if h of his/her N papers have at least h citations each,
# and the other N-h papers have no more than h citations each."

# For example, given citations = [3, 0, 6, 1, 5], which means the researcher has 5 papers in total 
# and each of them had received 3, 0, 6, 1, 5 citations respectively. 
# Since the researcher has 3 papers with at least 3 citations each and 
# the remaining two with no more than 3 citations each, his h-index is 3.

# Note: If there are several possible values for h, the maximum one is taken as the h-index. 


class Solution(object):
    def hIndex(self, citations):
        citations.sort()
        res = 0
        while res < len(citations) and citations[len(citations) - 1 - res] > res:
            res += 1
        return res

    # https://gengwg.blogspot.com/2018/02/re-h-index.html
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        if not citations:  # []
            return 0

        # 将其发表的所有SCI论文按被引次数从高到低排序；
        citations.sort(reverse=True)
        # 从前往后查找排序后的列表，直到某篇论文的序号大于该论文被引次数。所得序号减一即为H指数。
        for idx, citation in enumerate(citations, 1):  # idx starting from 1
            if idx > citation:
                return idx - 1
        # all citations > idx. now idx == len(citations)
        return idx


print Solution().hIndex([3, 0, 6, 1, 5])
print Solution().hIndex([3, 2])
