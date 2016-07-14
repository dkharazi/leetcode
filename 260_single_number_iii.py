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

