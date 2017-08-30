# 137. Single Number II
#
# Given an array of integers, every element appears three times except for one,
# which appears exactly once. Find that single one.
#
# Note:
# Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?


class Solution(object):
    def singleNumber(self, nums):
        """
        use a dictionary to record how many times each number appeared.

        :type nums: List[int]
        :rtype: int
        """
        dict = {}
        for num in nums:
            if num not in dict:
                dict[num] = 1
            else:
                dict[num] += 1

        print dict
        for num in dict:
            if dict[num] == 1:
                return num

    def singleNumber(self, nums):
        resultDict = {}
        for i in nums:
            if i in resultDict.keys():
                if resultDict[i] == 2:
                    del resultDict[i]
                else:
                    resultDict[i] += 1
            else:
                resultDict[i] = 1

        return list(resultDict.keys())[0]


if __name__ == '__main__':
    print Solution().singleNumber([1, 1, 1, 2, 3, 3, 3])
