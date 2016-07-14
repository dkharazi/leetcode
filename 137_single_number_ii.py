# Given an array of integers, every element appears three times except for one. Find that single one.

class Solution:
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

if __name__ == "__main__":
    print Solution().singleNumber([1, 1, 1, 2, 2, 2, 3])

