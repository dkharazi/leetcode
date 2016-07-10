class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        result = []
        for i in xrange(numRows):
            result.append([])
            for j in xrange(i + 1):
                if j in (0, i):
                    result[i].append(1)
                else:
                    result[i].append(result[i-1][j-1] + result[i-1][j])

        return result

if __name__ == "__main__":
    #print Solution().generate(9)

    print "["
    numRows = 9
    i = numRows * 2
    for li in Solution().generate(numRows):
        i -= 1
        #print "{:>20},".format(li)
        print "{},".rjust(i).format(li)
    print "]"
