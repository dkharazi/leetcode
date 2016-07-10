class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        result = [1]
        for i in xrange(1, rowIndex + 1):
            result = [1] + [result[j-1] + result[j] for j in xrange(1, i)] + [1]
        return result + [1]

class Solution2(object):
    def getRow(self, rowIndex):
        result = [0] * (rowIndex + 1)
        for i in xrange(rowIndex + 1):
            old = result[0] = 1
            for j in xrange(1, i+1):
                old, result[j] = result[j], old + result[j]

        return result

if __name__ == "__main__":
    print Solution2().getRow(3)
