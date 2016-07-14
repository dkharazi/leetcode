# Given an array of numbers nums, in which exactly two
# elements appear only once and all the other elements
# appear exactly twice. Find the two elements that appear only once.
#
# For example:
#
# Given nums = [1, 2, 1, 3, 2, 5], return [3, 5].
#
# Note:
# The order of the result is not important. So in the
# above example, [5, 3] is also correct.

class Solution:
    def singleNumber(self, nums):
        resultDict = {}
        for i in nums:
            if i in resultDict.keys():
                del resultDict[i]
            else:
                resultDict[i] = 1

        return list(resultDict.keys())

if __name__ == "__main__":
    print Solution().singleNumber([1, 2, 1, 3, 2, 5])

