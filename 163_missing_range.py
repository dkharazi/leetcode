# 163 Missing Ranges 

# Given a sorted integer array where the range of elements are [lower, upper] inclusive,
# return its missing ranges.
#
# For example, given [0, 1, 3, 50, 75], lower = 0 and upper = 99,
# return ["2", "4->49", "51->74", "76->99"].
#


class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """

        # helper function
        def rangify(lo, hi):
            if lo == hi:
                return '{}'.format(lo)
            else:
                return '{}->{}'.format(lo, hi)

        res = []
        start = lower
        for num in nums:
            # if num exists increament start
            if num == start:
                start += 1
            # if num > start, missing numbers: start->num-1
            elif num > start:
                res.append(rangify(start, num-1))
                start = num + 1
        # append last range
        if start <= upper:
            res.append(rangify(start, upper))
        return res

if __name__ == "__main__":
    print (Solution().findMissingRanges([0, 1, 3, 50, 75], 0, 99))