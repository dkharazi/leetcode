# 260. Single Number III
#
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
    # if seeing the element again in dict, delete it
    # things left are the single elements
    def singleNumber(self, nums):
        resultDict = {}
        for i in nums:
            if i in resultDict.keys():
                del resultDict[i]
            else:
                resultDict[i] = 1

        return list(resultDict.keys())


    # use a dictionary to store counts for each element
    def singleNumber(self, nums):
        d = {}
        for n in nums:
            if n not in d:
                d[n] = 1
            else:
                d[n] += 1
        return [k for k, v in d.items() if v == 1]
        # return [k for k in d if d[k] == 1]

    # https://www.jianshu.com/p/c31bd59d7877
    def singleNumber(self, nums):
        both = set()
        double = set()
        for n in nums:
            if n not in both:
                both.add(n)
            else:
                double.add(n)
        single = both - double
        return list(single)

if __name__ == "__main__":
    print Solution().singleNumber([1, 2, 1, 3, 2, 5])

