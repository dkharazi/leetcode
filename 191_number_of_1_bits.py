# 191. Number of 1 Bits
#
# Write a function that takes an unsigned integer and returns
# the number of '1' bits it has (also known as the Hamming weight).

# For example, the 32-bit integer '11' has binary representation
# 00000000000000000000000000001011, so the function should return 3.


class Solution:
    def hammingWeight(self, n):
        result = 0
        while n:
            n &= n - 1
            result += 1
        return result

    def hammingWeight(self, n):
        return bin(n).count('1')

    def hammingWeight(self, n):
        count = 0
        for c in bin(n):
            if c == '1':
                count += 1
        return count

if __name__ == "__main__":
    print Solution().hammingWeight(11)
