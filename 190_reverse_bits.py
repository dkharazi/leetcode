# 190. Reverse Bits
#
#
# Reverse bits of a given 32 bits unsigned integer.
#
# For example, given input 43261596 (represented in binary as 00000010100101000001111010011100),
# return 964176192 (represented in binary as 00111001011110000010100101000000).
#
# Follow up:
# If this function is called many times, how would you optimize it?
#
# Related problem: Reverse Integer
#
# Credits:
# Special thanks to @ts for adding this problem and creating all test cases.
#


class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        return int(bin(n)[2:].zfill(32)[::-1], 2)

    def reverseBits(self, n):
        b = bin(n)[:1:-1]
        return int(b + '0' * (32 - len(b)), 2)

    # http://blog.csdn.net/coder_orz/article/details/51705094
    def reverseBits(self, n):
        res = 0
        for i in range(32):
            res <<= 1
            res |= ((n >> i) & 1)
        return res
