#
# Given an array of integers, every element appears twice except for one. Find that single one.
#

# The property of XOR.
# x ^ x = 0
# x ^ y ^ x = y (the order could in random arrangement)
# Since we have only one number appear once, other number apper perfectly twice.
# we XOR all numbers in the array, and we would finally get the number that only appears once.

import operator

class Solution:
    def singleNumber(self, A):
        # function reduce(func, seq) continually applies the function func()
        # to the sequence seq. it returns a single value.
        return reduce(operator.xor, A)

if __name__ == "__main__":
    print Solution().singleNumber([1, 1, 2, 3, 2, 4, 3])
